#!/usr/bin/env python3
"""
UI Kit Batch Pipeline — Phases 1-5 for ALL kits
=================================================
Runs the proven 5-phase pipeline on every kit in KIT_INDEX.json
that hasn't been processed yet.

Phase 1: Figma API deep extract (FIGMA_FULL.json)
Phase 2: Structure analysis (SCREEN_ANALYSIS.json)
Phase 3: Layout deduplication (LAYOUT_TEMPLATES.json)
Phase 4: Representative PNG export
Phase 5: PRD layout matching

Loads FIGMA_TOKEN from .env file.
Checkpoints after EVERY kit.
Skips already-processed kits.

Cost: $0 (Figma API is free for metadata + image rendering)
"""

import json
import os
import sys
import time
import requests
from pathlib import Path
from datetime import datetime
from collections import defaultdict

sys.stdout.reconfigure(line_buffering=True)

# === PATHS ===
PROJECT_ROOT = Path(r"C:\Users\under\Downloads\ENTERPRISE_OS_V7")
KIT_SCREENS_DIR = PROJECT_ROOT / "07_BUILD_FACTORY" / "PRJ_UI_Component_Library" / "kit_screens"
KIT_INDEX_PATH = PROJECT_ROOT / "07_BUILD_FACTORY" / "PRJ_UI_Component_Library" / "03_Design" / "KIT_INDEX.json"
CORE_LIBRARY_PATH = KIT_SCREENS_DIR / "CORE_LAYOUT_LIBRARY.json"
BATCH_CHECKPOINT_PATH = KIT_SCREENS_DIR / "BATCH_PIPELINE_CHECKPOINT.json"

# === FIGMA CONFIG ===
def load_env():
    """Load .env file from project root."""
    env_path = PROJECT_ROOT / ".env"
    if env_path.exists():
        with open(env_path, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    os.environ[key.strip()] = val.strip()

load_env()

FIGMA_TOKEN = os.environ.get("FIGMA_TOKEN", "")
BASE_URL = "https://api.figma.com/v1"
HEADERS = {"X-Figma-Token": FIGMA_TOKEN}

# Phase 4 settings
SCALE = 0.5
RATE_DELAY = 3.0
DOWNLOAD_TIMEOUT = 60

# Phase 2 thresholds
MIN_SCREEN_WIDTH = 1200
MIN_SCREEN_HEIGHT = 600
SIDEBAR_MAX_WIDTH = 350
HEADER_MAX_HEIGHT = 100
FOOTER_MAX_HEIGHT = 80
COMPONENT_OVERLAP_THRESHOLD = 0.6


# ============================================================
# CHECKPOINT MANAGEMENT
# ============================================================

def load_batch_checkpoint():
    if BATCH_CHECKPOINT_PATH.exists():
        with open(BATCH_CHECKPOINT_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"completed_kits": [], "failed_kits": [], "started_at": datetime.now().isoformat()}


def save_batch_checkpoint(cp):
    cp["updated_at"] = datetime.now().isoformat()
    with open(BATCH_CHECKPOINT_PATH, "w", encoding="utf-8") as f:
        json.dump(cp, f, indent=2)


# ============================================================
# PHASE 1: FIGMA DEEP EXTRACT
# ============================================================

def phase1_extract(kit_name, file_key):
    """Pull full Figma document tree via API."""
    kit_dir = KIT_SCREENS_DIR / kit_name
    out_path = kit_dir / "FIGMA_FULL.json"

    if out_path.exists() and out_path.stat().st_size > 10000:
        print(f"    Phase 1: CACHED ({out_path.stat().st_size / 1024 / 1024:.1f} MB)")
        return True

    kit_dir.mkdir(parents=True, exist_ok=True)

    url = f"{BASE_URL}/files/{file_key}"
    print(f"    Phase 1: GET {url}...")
    start = time.time()

    try:
        resp = requests.get(url, headers=HEADERS, timeout=300)

        if resp.status_code == 429:
            wait = int(resp.headers.get("Retry-After", 60))
            print(f"    Rate limited — waiting {wait}s...")
            time.sleep(wait)
            resp = requests.get(url, headers=HEADERS, timeout=300)

        elapsed = time.time() - start
        size_mb = len(resp.content) / (1024 * 1024)

        if resp.status_code != 200:
            print(f"    Phase 1 FAILED: HTTP {resp.status_code} ({elapsed:.1f}s)")
            return False

        data = resp.json()

        # Count nodes
        def count_nodes(node):
            c = 1
            for child in node.get("children", []):
                c += count_nodes(child)
            return c

        total = count_nodes(data.get("document", {}))
        data["file_key"] = file_key
        data["total_nodes"] = total
        data["extracted_at"] = datetime.now().isoformat()

        # Save compact to avoid MemoryError on huge kits
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

        final_mb = out_path.stat().st_size / 1024 / 1024
        print(f"    Phase 1: OK — {total} nodes, {final_mb:.1f} MB, {elapsed:.1f}s")
        return True

    except requests.exceptions.Timeout:
        print(f"    Phase 1 FAILED: Request timeout (>300s)")
        return False
    except Exception as e:
        print(f"    Phase 1 FAILED: {type(e).__name__}: {e}")
        return False


# ============================================================
# PHASE 2: STRUCTURE ANALYSIS (from figma_structure_analyzer.py)
# ============================================================

def extract_bbox(node):
    bbox = node.get("absoluteBoundingBox") or {}
    return {
        "x": bbox.get("x", 0), "y": bbox.get("y", 0),
        "width": bbox.get("width", 0), "height": bbox.get("height", 0),
    }


def is_screen_sized(node):
    bbox = extract_bbox(node)
    return bbox["width"] >= MIN_SCREEN_WIDTH and bbox["height"] >= MIN_SCREEN_HEIGHT


def find_all_screens(node, page_name="", path="", depth=0):
    screens = []
    node_type = node.get("type", "")
    name = node.get("name", "")
    bbox = extract_bbox(node)

    if is_screen_sized(node) and node_type in ("FRAME", "COMPONENT", "INSTANCE", "COMPONENT_SET"):
        is_canvas_board = bbox["width"] > 5000 or bbox["height"] > 5000
        if is_canvas_board:
            for child in node.get("children", []):
                screens.extend(find_all_screens(child, page_name or name, f"{path}/{name}" if path else name, depth + 1))
            return screens

        lower_name = name.lower()
        is_variant = any(kw in lower_name for kw in ["dark", "mobile", "tablet", "ipad", "android"])
        screens.append({
            "node": node, "page_name": page_name,
            "path": f"{path}/{name}" if path else name,
            "depth": depth, "is_variant": is_variant,
        })
        return screens

    if node_type in ("CANVAS", "SECTION", "GROUP", "FRAME", "COMPONENT_SET"):
        for child in node.get("children", []):
            screens.extend(find_all_screens(child, page_name or name, f"{path}/{name}" if path else name, depth + 1))

    return screens


def extract_text_content(node, max_depth=20):
    texts = []
    if max_depth <= 0:
        return texts
    if node.get("type") == "TEXT":
        chars = node.get("characters", "").strip()
        if chars and len(chars) < 500:
            texts.append(chars)
    for child in node.get("children", []):
        texts.extend(extract_text_content(child, max_depth - 1))
    return texts


def extract_component_instances(node, max_depth=20):
    instances = []
    if max_depth <= 0:
        return instances
    if node.get("type") == "INSTANCE":
        bbox = extract_bbox(node)
        inner_text = extract_text_content(node, max_depth=5)
        instances.append({
            "name": node.get("name", ""), "type": "INSTANCE",
            "component_id": node.get("componentId", ""),
            "width": bbox["width"], "height": bbox["height"],
            "text": inner_text[:5] if inner_text else [],
        })
    for child in node.get("children", []):
        if child.get("type") != "INSTANCE":
            instances.extend(extract_component_instances(child, max_depth - 1))
        else:
            bbox = extract_bbox(child)
            inner_text = extract_text_content(child, max_depth=5)
            instances.append({
                "name": child.get("name", ""), "type": "INSTANCE",
                "component_id": child.get("componentId", ""),
                "width": bbox["width"], "height": bbox["height"],
                "text": inner_text[:5] if inner_text else [],
            })
    return instances


def count_all_children(node, max_depth=20):
    if max_depth <= 0:
        return 0
    count = len(node.get("children", []))
    for child in node.get("children", []):
        count += count_all_children(child, max_depth - 1)
    return count


def classify_panel_role(panel_name, panel_texts, panel_width, position):
    name_lower = panel_name.lower()
    all_text = " ".join(panel_texts).lower()
    nav_keywords = ["nav", "menu", "sidebar", "navigation", "home", "dashboard", "settings", "profile", "files", "folders", "projects"]
    if position in ("left", "right") and panel_width < SIDEBAR_MAX_WIDTH:
        if any(kw in name_lower or kw in all_text for kw in nav_keywords):
            return "navigation_sidebar"
    prop_keywords = ["properties", "inspector", "details", "options", "config", "settings", "layers", "export", "style"]
    if position == "right" and any(kw in all_text for kw in prop_keywords):
        return "properties_panel"
    if any(kw in name_lower for kw in ["toolbar", "tools", "actions"]):
        return "toolbar"
    if position == "top":
        return "header"
    if position == "bottom":
        return "footer"
    role_map = {"left": "left_sidebar", "right": "right_panel", "center": "main_content"}
    return role_map.get(position, "unknown")


def analyze_layout(screen_node):
    screen_bbox = extract_bbox(screen_node)
    sw, sh = screen_bbox["width"], screen_bbox["height"]
    children = screen_node.get("children", [])
    if not children:
        return {"type": "empty", "description": "No children found", "panels": []}

    panels = []
    for child in children:
        child_bbox = extract_bbox(child)
        cx = child_bbox["x"] - screen_bbox["x"]
        cy = child_bbox["y"] - screen_bbox["y"]
        cw, ch = child_bbox["width"], child_bbox["height"]
        if cw < 10 or ch < 10:
            continue

        child_texts = extract_text_content(child, max_depth=5)
        position = "unknown"
        if cy < 5 and ch < HEADER_MAX_HEIGHT and cw > sw * 0.5:
            position = "top"
        elif cy > sh - FOOTER_MAX_HEIGHT - 10 and ch < FOOTER_MAX_HEIGHT and cw > sw * 0.5:
            position = "bottom"
        elif cx < 5 and cw < SIDEBAR_MAX_WIDTH:
            position = "left"
        elif cx > sw - SIDEBAR_MAX_WIDTH - 5 and cw < SIDEBAR_MAX_WIDTH:
            position = "right"
        else:
            position = "center"

        role = classify_panel_role(child.get("name", ""), child_texts, cw, position)
        panel_instances = extract_component_instances(child, max_depth=5)
        component_names = list(set(inst["name"].split("/")[0] for inst in panel_instances if inst["name"]))

        panels.append({
            "position": position, "name": child.get("name", ""),
            "width_approx": round(cw), "height_approx": round(ch),
            "role": role, "components": component_names[:20],
            "text_labels": child_texts[:15],
        })

    positions = [p["position"] for p in panels]
    has_left, has_right = "left" in positions, "right" in positions
    has_center = "center" in positions

    if has_left and has_right and has_center:
        layout_type = "three_panel"
    elif has_left and has_center:
        layout_type = "sidebar_content"
    elif has_center and not has_left and not has_right:
        center_panels = [p for p in panels if p["position"] == "center"]
        if len(center_panels) > 3:
            widths = [p["width_approx"] for p in center_panels]
            layout_type = "cards_grid" if widths and max(widths) - min(widths) < 50 else "full_canvas"
        else:
            layout_type = "full_canvas"
    elif has_left and has_right and not has_center:
        layout_type = "split_panel"
    else:
        layout_type = "other"

    parts = []
    for p in sorted(panels, key=lambda x: {"top": 0, "left": 1, "center": 2, "right": 3, "bottom": 4}.get(x["position"], 5)):
        parts.append(f"{p['position'].title()} {p['role']} ({p['width_approx']}x{p['height_approx']})")

    return {"type": layout_type, "description": ", ".join(parts) or "Unknown layout", "panels": panels}


def infer_capabilities(text_content, component_instances, layout):
    caps = set()
    all_text = " ".join(text_content).lower()
    comp_names = " ".join(inst.get("name", "") for inst in component_instances).lower()
    combined = all_text + " " + comp_names

    capability_keywords = {
        "search": ["search", "find", "filter", "query"],
        "file_management": ["files", "folders", "upload", "download", "documents"],
        "editing": ["edit", "editor", "canvas", "draw", "compose"],
        "data_table": ["table", "rows", "columns", "sort", "grid"],
        "analytics": ["analytics", "chart", "graph", "metrics", "statistics", "dashboard"],
        "user_management": ["users", "members", "team", "invite", "roles"],
        "messaging": ["chat", "message", "inbox", "conversation", "notification"],
        "settings": ["settings", "preferences", "configuration", "account"],
        "authentication": ["login", "sign in", "sign up", "register", "password"],
        "e_commerce": ["cart", "checkout", "payment", "pricing", "order", "product"],
        "navigation": ["sidebar", "menu", "nav", "breadcrumb", "tabs"],
        "content_creation": ["create", "new", "compose", "publish", "draft"],
        "calendar": ["calendar", "schedule", "date", "event", "booking"],
        "map": ["map", "location", "address", "property", "listing"],
        "media": ["video", "image", "gallery", "photo", "media"],
        "form": ["form", "input", "submit", "field"],
        "profile": ["profile", "avatar", "bio", "about"],
        "notifications": ["notification", "alert", "bell", "badge"],
    }
    for cap, keywords in capability_keywords.items():
        if any(kw in combined for kw in keywords):
            caps.add(cap)
    return sorted(caps)


def detect_theme(node, max_depth=5):
    fills = node.get("fills", [])
    for fill in fills:
        if fill.get("type") == "SOLID" and fill.get("visible", True):
            color = fill.get("color", {})
            luminance = 0.299 * color.get("r", 1) + 0.587 * color.get("g", 1) + 0.114 * color.get("b", 1)
            return luminance > 0.5
    for child in node.get("children", [])[:3]:
        if max_depth > 0:
            result = detect_theme(child, max_depth - 1)
            if result is not None:
                return result
    return True


def analyze_screen(screen_info):
    node = screen_info["node"]
    bbox = extract_bbox(node)
    all_text = extract_text_content(node, max_depth=25)
    instances = extract_component_instances(node, max_depth=25)
    layout = analyze_layout(node)
    capabilities = infer_capabilities(all_text, instances, layout)
    is_light = detect_theme(node)
    total_children = count_all_children(node, max_depth=25)

    return {
        "screen_id": node.get("id", ""), "screen_name": node.get("name", ""),
        "page": screen_info["page_name"], "path": screen_info["path"],
        "node_type": node.get("type", ""), "depth_found": screen_info["depth"],
        "is_variant": screen_info["is_variant"],
        "dimensions": {"width": round(bbox["width"]), "height": round(bbox["height"])},
        "is_light": is_light, "layout": layout, "capabilities": capabilities,
        "all_text_content": all_text[:100], "component_count": len(instances),
        "total_descendants": total_children, "nested_components": instances[:50],
    }


def phase2_analyze(kit_name):
    """Analyze Figma JSON tree into structured screen data."""
    kit_dir = KIT_SCREENS_DIR / kit_name
    full_path = kit_dir / "FIGMA_FULL.json"
    out_path = kit_dir / "SCREEN_ANALYSIS.json"

    if out_path.exists() and out_path.stat().st_size > 1000:
        print(f"    Phase 2: CACHED")
        return True

    if not full_path.exists():
        print(f"    Phase 2 FAILED: No FIGMA_FULL.json")
        return False

    print(f"    Phase 2: Loading JSON...")
    with open(full_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    doc = data.get("document", {})
    pages = doc.get("children", [])

    all_screens = []
    for page in pages:
        all_screens.extend(find_all_screens(page))

    light_screens = [s for s in all_screens if not s["is_variant"]]
    print(f"    Phase 2: {len(all_screens)} total screens, {len(light_screens)} light/desktop")

    analyzed = []
    for i, screen_info in enumerate(light_screens):
        analyzed.append(analyze_screen(screen_info))

    layout_counts = defaultdict(int)
    for screen in analyzed:
        layout_counts[screen["layout"]["type"]] += 1

    result = {
        "kit_name": kit_name,
        "file_key": data.get("file_key", ""),
        "analyzed_at": datetime.now().isoformat(),
        "summary": {
            "total_screens_found": len(all_screens),
            "light_desktop_screens": len(light_screens),
            "variant_screens_skipped": len(all_screens) - len(light_screens),
            "layout_types": dict(layout_counts),
        },
        "screens": analyzed,
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"    Phase 2: OK — {len(light_screens)} screens analyzed")
    return True


# ============================================================
# PHASE 3: LAYOUT DEDUPLICATION (from layout_deduplicator.py)
# ============================================================

def get_component_set(screen):
    components = set()
    for inst in screen.get("nested_components", []):
        name = inst.get("name", "")
        root = name.split("/")[0].strip() if "/" in name else name.strip()
        if root:
            components.add(root.lower())
    return components


def get_panel_signature(screen):
    layout = screen.get("layout", {})
    panels = layout.get("panels", [])
    sig_parts = []
    for panel in sorted(panels, key=lambda p: p.get("position", "")):
        pos = panel.get("position", "?")
        role = panel.get("role", "?")
        w = panel.get("width_approx", 0)
        w_bucket = "narrow" if w < 300 else ("medium" if w < 600 else "wide")
        sig_parts.append(f"{pos}:{role}:{w_bucket}")
    return "|".join(sig_parts)


def compute_overlap(set_a, set_b):
    if not set_a and not set_b:
        return 1.0
    if not set_a or not set_b:
        return 0.0
    intersection = len(set_a & set_b)
    union = len(set_a | set_b)
    return intersection / union if union > 0 else 0.0


def find_unique_templates(screens, kit_name):
    templates = []
    template_id_counter = 0

    layout_groups = defaultdict(list)
    for screen in screens:
        lt = screen.get("layout", {}).get("type", "unknown")
        layout_groups[lt].append(screen)

    for layout_type, group_screens in layout_groups.items():
        sig_groups = defaultdict(list)
        for screen in group_screens:
            sig = get_panel_signature(screen)
            sig_groups[sig].append(screen)

        for sig, sig_screens in sig_groups.items():
            clusters = []
            assigned = set()

            for i, screen_a in enumerate(sig_screens):
                if i in assigned:
                    continue
                cluster = [screen_a]
                comp_a = get_component_set(screen_a)
                assigned.add(i)
                for j, screen_b in enumerate(sig_screens):
                    if j in assigned:
                        continue
                    comp_b = get_component_set(screen_b)
                    if compute_overlap(comp_a, comp_b) >= COMPONENT_OVERLAP_THRESHOLD:
                        cluster.append(screen_b)
                        assigned.add(j)
                clusters.append(cluster)

            for cluster in clusters:
                template_id_counter += 1
                representative = max(cluster, key=lambda s: s.get("component_count", 0))
                all_components = set()
                for s in cluster:
                    all_components |= get_component_set(s)
                all_capabilities = set()
                for s in cluster:
                    all_capabilities.update(s.get("capabilities", []))

                kit_prefix = kit_name[:2].upper()
                templates.append({
                    "layout_id": f"{kit_prefix}_L{template_id_counter}",
                    "name": representative.get("screen_name", "Unknown"),
                    "type": layout_type,
                    "panel_signature": sig,
                    "screens_using": [s.get("screen_name", "") for s in cluster],
                    "screen_ids": [s.get("screen_id", "") for s in cluster],
                    "count": len(cluster),
                    "representative_screen": representative.get("screen_id", ""),
                    "representative_name": representative.get("screen_name", ""),
                    "dimensions": representative.get("dimensions", {}),
                    "layout_detail": representative.get("layout", {}),
                    "core_components": sorted(all_components)[:30],
                    "capabilities": sorted(all_capabilities),
                    "is_light": representative.get("is_light", True),
                })

    return templates


def phase3_dedup(kit_name):
    """Deduplicate screens into unique layout templates."""
    kit_dir = KIT_SCREENS_DIR / kit_name
    analysis_path = kit_dir / "SCREEN_ANALYSIS.json"
    out_path = kit_dir / "LAYOUT_TEMPLATES.json"

    if out_path.exists() and out_path.stat().st_size > 100:
        print(f"    Phase 3: CACHED")
        return True

    if not analysis_path.exists():
        print(f"    Phase 3 FAILED: No SCREEN_ANALYSIS.json")
        return False

    with open(analysis_path, "r", encoding="utf-8") as f:
        analysis = json.load(f)

    screens = analysis.get("screens", [])
    if not screens:
        # Save empty template file
        result = {"kit": kit_name, "unique_layouts": 0, "total_screens": 0, "layouts": []}
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"    Phase 3: OK — 0 screens, 0 templates")
        return True

    templates = find_unique_templates(screens, kit_name)

    result = {
        "kit": kit_name,
        "file_key": analysis.get("file_key", ""),
        "analyzed_at": datetime.now().isoformat(),
        "unique_layouts": len(templates),
        "total_screens": len(screens),
        "dedup_ratio": f"{len(screens)} screens -> {len(templates)} templates ({round(len(templates)/max(len(screens),1)*100)}%)",
        "layouts": templates,
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"    Phase 3: OK — {result['dedup_ratio']}")
    return True


# ============================================================
# PHASE 4: REPRESENTATIVE PNG EXPORT
# ============================================================

def sanitize_filename(name):
    for ch in ['/', '\\', ':', '?', '"', '<', '>', '|', '*']:
        name = name.replace(ch, '_')
    return name


def phase4_pngs(kit_name):
    """Export representative PNGs for this kit's templates."""
    kit_dir = KIT_SCREENS_DIR / kit_name
    templates_path = kit_dir / "LAYOUT_TEMPLATES.json"
    rep_dir = kit_dir / "representative"

    if not templates_path.exists():
        print(f"    Phase 4 FAILED: No LAYOUT_TEMPLATES.json")
        return False

    with open(templates_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    file_key = data.get("file_key", "")
    layouts = data.get("layouts", [])

    if not layouts:
        print(f"    Phase 4: SKIP (0 templates)")
        return True

    if not file_key:
        print(f"    Phase 4 FAILED: No file_key in templates")
        return False

    # Check if already done
    if rep_dir.exists():
        existing = list(rep_dir.glob("*.png"))
        if len(existing) >= len(layouts):
            print(f"    Phase 4: CACHED ({len(existing)} PNGs)")
            return True

    rep_dir.mkdir(parents=True, exist_ok=True)
    downloaded = 0
    cached = 0
    failed = 0

    for i, layout in enumerate(layouts):
        screen_id = layout.get("representative_screen", "")
        screen_name = layout.get("representative_name", layout.get("name", ""))

        if not screen_id:
            failed += 1
            continue

        safe_name = sanitize_filename(screen_name)
        safe_id = screen_id.replace(":", "_")
        filename = f"{safe_id}_{safe_name}.png"
        filepath = rep_dir / filename

        if filepath.exists() and filepath.stat().st_size > 1000:
            cached += 1
            continue

        # API call
        url = f"{BASE_URL}/images/{file_key}"
        params = {"ids": screen_id, "format": "png", "scale": SCALE}

        try:
            resp = requests.get(url, headers=HEADERS, params=params, timeout=120)
            if resp.status_code == 429:
                wait = int(resp.headers.get("Retry-After", 30))
                print(f"      Rate limited — waiting {wait}s...")
                time.sleep(wait)
                resp = requests.get(url, headers=HEADERS, params=params, timeout=120)

            if resp.status_code == 400:
                failed += 1
                continue

            if resp.status_code != 200:
                failed += 1
                continue

            img_data = resp.json()
            img_url = img_data.get("images", {}).get(screen_id)
            if not img_url:
                failed += 1
                continue

            dl_resp = requests.get(img_url, timeout=DOWNLOAD_TIMEOUT)
            if dl_resp.status_code != 200 or len(dl_resp.content) < 500:
                failed += 1
                continue

            with open(filepath, "wb") as f:
                f.write(dl_resp.content)
            downloaded += 1

        except Exception as e:
            failed += 1
            continue

        time.sleep(RATE_DELAY)

    total = downloaded + cached
    print(f"    Phase 4: OK — {downloaded} new + {cached} cached = {total} PNGs ({failed} failed)")
    return True


# ============================================================
# PHASE 5: UPDATE CORE LAYOUT LIBRARY
# ============================================================

def phase5_update_library(kit_name):
    """Add this kit to the CORE_LAYOUT_LIBRARY.json."""
    templates_path = KIT_SCREENS_DIR / kit_name / "LAYOUT_TEMPLATES.json"

    if not templates_path.exists():
        print(f"    Phase 5 FAILED: No LAYOUT_TEMPLATES.json")
        return False

    with open(templates_path, "r", encoding="utf-8") as f:
        kit_data = json.load(f)

    # Load or create library
    if CORE_LIBRARY_PATH.exists():
        with open(CORE_LIBRARY_PATH, "r", encoding="utf-8") as f:
            lib = json.load(f)
    else:
        lib = {
            "generated_at": datetime.now().isoformat(),
            "total_kits": 0,
            "grand_totals": {"total_screens": 0, "total_unique_layouts": 0, "total_representative_screens": 0},
            "kits": {},
            "all_layouts": [],
        }

    # Skip if already in library
    if kit_name in lib.get("kits", {}):
        print(f"    Phase 5: CACHED (already in library)")
        return True

    # Add kit
    lib["kits"][kit_name] = {
        "file_key": kit_data.get("file_key", ""),
        "unique_layouts": kit_data["unique_layouts"],
        "total_screens": kit_data["total_screens"],
        "dedup_ratio": kit_data["dedup_ratio"],
        "layouts": kit_data["layouts"],
    }

    for tmpl in kit_data["layouts"]:
        tmpl_copy = dict(tmpl)
        tmpl_copy["kit"] = kit_name
        lib["all_layouts"].append(tmpl_copy)

    lib["total_kits"] = len(lib["kits"])
    lib["grand_totals"]["total_screens"] += kit_data["total_screens"]
    lib["grand_totals"]["total_unique_layouts"] += kit_data["unique_layouts"]
    lib["grand_totals"]["total_representative_screens"] += kit_data["unique_layouts"]
    lib["generated_at"] = datetime.now().isoformat()

    with open(CORE_LIBRARY_PATH, "w", encoding="utf-8") as f:
        json.dump(lib, f, indent=2, ensure_ascii=False)

    print(f"    Phase 5: OK — library now has {lib['total_kits']} kits, {lib['grand_totals']['total_unique_layouts']} templates")
    return True


# ============================================================
# MAIN ORCHESTRATOR
# ============================================================

def main():
    print(f"\n{'='*70}")
    print(f"UI KIT BATCH PIPELINE — All 5 Phases")
    print(f"{'='*70}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    if not FIGMA_TOKEN:
        print("ERROR: FIGMA_TOKEN not set. Add to .env file.")
        sys.exit(1)

    # Load KIT_INDEX
    with open(KIT_INDEX_PATH, "r", encoding="utf-8") as f:
        kit_index = json.load(f)

    print(f"Total kits in KIT_INDEX: {len(kit_index)}")

    # Load checkpoint
    cp = load_batch_checkpoint()
    completed = set(cp.get("completed_kits", []))
    print(f"Already completed: {len(completed)}")

    # Determine which kits to process
    to_process = []
    for kit_name, kit_data in kit_index.items():
        file_key = kit_data.get("file_key", "")
        if not file_key:
            print(f"  SKIP {kit_name}: no file_key")
            continue
        if kit_name in completed:
            continue
        to_process.append((kit_name, file_key))

    print(f"Kits to process: {len(to_process)}")
    print(f"{'='*70}\n")

    stats = {"ok": 0, "failed": 0, "skipped": 0}

    for i, (kit_name, file_key) in enumerate(to_process, 1):
        print(f"\n[{i}/{len(to_process)}] === {kit_name} === (file: {file_key[:10]}...)")
        kit_start = time.time()

        # Run all 5 phases
        p1 = phase1_extract(kit_name, file_key)
        if not p1:
            print(f"  FAILED at Phase 1 — skipping")
            cp.setdefault("failed_kits", [])
            if kit_name not in cp["failed_kits"]:
                cp["failed_kits"].append(kit_name)
            save_batch_checkpoint(cp)
            stats["failed"] += 1
            continue

        p2 = phase2_analyze(kit_name)
        if not p2:
            print(f"  FAILED at Phase 2 — skipping")
            stats["failed"] += 1
            continue

        p3 = phase3_dedup(kit_name)
        if not p3:
            print(f"  FAILED at Phase 3 — skipping")
            stats["failed"] += 1
            continue

        p4 = phase4_pngs(kit_name)
        if not p4:
            print(f"  Phase 4 failed but continuing (PNGs are optional)")

        p5 = phase5_update_library(kit_name)

        elapsed = time.time() - kit_start
        print(f"  DONE in {elapsed:.1f}s")

        # Checkpoint
        cp["completed_kits"].append(kit_name)
        save_batch_checkpoint(cp)
        stats["ok"] += 1

    # Final summary
    print(f"\n{'='*70}")
    print(f"BATCH PIPELINE COMPLETE")
    print(f"{'='*70}")
    print(f"Processed: {stats['ok']}")
    print(f"Failed: {stats['failed']}")
    print(f"Total kits in library: {len(completed) + stats['ok']}")

    # Read final library state
    if CORE_LIBRARY_PATH.exists():
        with open(CORE_LIBRARY_PATH, "r", encoding="utf-8") as f:
            lib = json.load(f)
        print(f"Library totals: {lib['grand_totals']}")

    print(f"Finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
