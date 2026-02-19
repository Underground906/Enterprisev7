#!/usr/bin/env python3
"""
Figma Structure Analyzer — Phase 2
=====================================
Walks the full Figma JSON tree (from Phase 1) and builds structured
screen/layout/component analysis for each of 4 core kits.

Layout detection is purely mechanical — no AI, no API calls, $0 cost.
Classifies screens by child position analysis, extracts all text content,
and maps every component instance.

Input:  kit_screens/{KitName}/FIGMA_FULL.json (from Phase 1)
Output: kit_screens/{KitName}/SCREEN_ANALYSIS.json (per kit)
        kit_screens/CORE_KITS_LIBRARY.json (combined)
"""

import json
import os
import sys
from datetime import datetime
from collections import defaultdict

sys.stdout.reconfigure(line_buffering=True)

KIT_SCREENS_DIR = os.path.join(
    r"C:\Users\under\Downloads\ENTERPRISE_OS_V7",
    "07_BUILD_FACTORY", "PRJ_UI_Component_Library", "kit_screens"
)

CORE_KITS = ["Brainwave 2.0", "Real Estate SaaS Kit", "Chroma", "Majin"]

# Screen detection thresholds
MIN_SCREEN_WIDTH = 1200   # Minimum width to be considered a screen
MIN_SCREEN_HEIGHT = 600   # Minimum height to be considered a screen

# Layout panel thresholds
SIDEBAR_MAX_WIDTH = 350   # Left/right sidebars are typically < 350px
HEADER_MAX_HEIGHT = 100   # Top headers/navbars < 100px
FOOTER_MAX_HEIGHT = 80    # Bottom bars < 80px


def extract_bbox(node):
    """Get bounding box from a node."""
    bbox = node.get("absoluteBoundingBox") or {}
    return {
        "x": bbox.get("x", 0),
        "y": bbox.get("y", 0),
        "width": bbox.get("width", 0),
        "height": bbox.get("height", 0),
    }


def is_screen_sized(node):
    """Check if a node is screen-sized (>= 1200x600)."""
    bbox = extract_bbox(node)
    return bbox["width"] >= MIN_SCREEN_WIDTH and bbox["height"] >= MIN_SCREEN_HEIGHT


def find_all_screens(node, page_name="", path="", depth=0):
    """
    Recursively find all screen-sized nodes at ANY depth.
    This is the key fix — depth=2 inventory missed screens inside
    SECTIONs and those typed as COMPONENT/INSTANCE.
    """
    screens = []
    node_type = node.get("type", "")
    name = node.get("name", "")
    bbox = extract_bbox(node)

    # Is this node itself a screen?
    if is_screen_sized(node) and node_type in ("FRAME", "COMPONENT", "INSTANCE", "COMPONENT_SET"):
        # Check if this is a DESIGN CANVAS (huge layout board containing many screens)
        # rather than an actual screen. Design canvases are typically > 5000px in either dimension.
        is_canvas_board = bbox["width"] > 5000 or bbox["height"] > 5000

        if is_canvas_board:
            # This is a layout board — recurse into children to find actual screens
            for child in node.get("children", []):
                child_page = page_name if page_name else name
                child_path = f"{path}/{name}" if path else name
                screens.extend(find_all_screens(child, child_page, child_path, depth + 1))
            return screens

        # Skip dark/mobile/tablet variants
        lower_name = name.lower()
        is_variant = any(kw in lower_name for kw in ["dark", "mobile", "tablet", "ipad", "android"])

        screens.append({
            "node": node,
            "page_name": page_name,
            "path": f"{path}/{name}" if path else name,
            "depth": depth,
            "is_variant": is_variant,
        })
        # Don't recurse into screens — the screen IS the unit we analyze
        return screens

    # For SECTIONs, GROUPs, and pages — recurse into children
    if node_type in ("CANVAS", "SECTION", "GROUP", "FRAME", "COMPONENT_SET"):
        for child in node.get("children", []):
            child_page = page_name if page_name else name
            child_path = f"{path}/{name}" if path else name
            screens.extend(find_all_screens(child, child_page, child_path, depth + 1))

    return screens


def extract_text_content(node, max_depth=20):
    """Walk all TEXT nodes and extract their characters."""
    texts = []
    if max_depth <= 0:
        return texts

    if node.get("type") == "TEXT":
        chars = node.get("characters", "").strip()
        if chars and len(chars) < 500:  # Skip giant text blocks
            texts.append(chars)

    for child in node.get("children", []):
        texts.extend(extract_text_content(child, max_depth - 1))

    return texts


def extract_component_instances(node, max_depth=20):
    """Find all INSTANCE nodes (references to master components)."""
    instances = []
    if max_depth <= 0:
        return instances

    if node.get("type") == "INSTANCE":
        bbox = extract_bbox(node)
        # Get text from within this instance
        inner_text = extract_text_content(node, max_depth=5)
        instances.append({
            "name": node.get("name", ""),
            "type": "INSTANCE",
            "component_id": node.get("componentId", ""),
            "width": bbox["width"],
            "height": bbox["height"],
            "text": inner_text[:5] if inner_text else [],  # First 5 text items
        })

    for child in node.get("children", []):
        if child.get("type") != "INSTANCE":
            # Don't recurse into instances (we already captured them)
            instances.extend(extract_component_instances(child, max_depth - 1))
        else:
            bbox = extract_bbox(child)
            inner_text = extract_text_content(child, max_depth=5)
            instances.append({
                "name": child.get("name", ""),
                "type": "INSTANCE",
                "component_id": child.get("componentId", ""),
                "width": bbox["width"],
                "height": bbox["height"],
                "text": inner_text[:5] if inner_text else [],
            })

    return instances


def count_all_children(node, max_depth=20):
    """Count total descendant nodes."""
    if max_depth <= 0:
        return 0
    count = len(node.get("children", []))
    for child in node.get("children", []):
        count += count_all_children(child, max_depth - 1)
    return count


def classify_panel_role(panel_name, panel_texts, panel_width, position):
    """Infer panel role from name, text content, width, and position."""
    name_lower = panel_name.lower()
    all_text = " ".join(panel_texts).lower()

    # Navigation sidebar indicators
    nav_keywords = ["nav", "menu", "sidebar", "navigation", "home", "dashboard",
                    "settings", "profile", "files", "folders", "projects"]
    if position in ("left", "right") and panel_width < SIDEBAR_MAX_WIDTH:
        if any(kw in name_lower or kw in all_text for kw in nav_keywords):
            return "navigation_sidebar"

    # Properties panel indicators
    prop_keywords = ["properties", "inspector", "details", "options", "config",
                     "settings", "layers", "export", "style"]
    if position == "right" and any(kw in all_text for kw in prop_keywords):
        return "properties_panel"

    # Toolbar indicators
    toolbar_keywords = ["toolbar", "tools", "actions"]
    if any(kw in name_lower for kw in toolbar_keywords):
        return "toolbar"

    # Header/topbar indicators
    if position == "top":
        return "header"

    # Footer indicators
    if position == "bottom":
        return "footer"

    # Default by position
    role_map = {"left": "left_sidebar", "right": "right_panel", "center": "main_content"}
    return role_map.get(position, "unknown")


def analyze_layout(screen_node):
    """
    Analyze the layout of a screen by examining direct children positions.

    Returns layout classification and panel breakdown.
    """
    screen_bbox = extract_bbox(screen_node)
    sw = screen_bbox["width"]
    sh = screen_bbox["height"]

    children = screen_node.get("children", [])
    if not children:
        return {"type": "empty", "description": "No children found", "panels": []}

    # Analyze each direct child's position relative to the screen
    panels = []
    for child in children:
        child_bbox = extract_bbox(child)
        cx = child_bbox["x"] - screen_bbox["x"]  # Relative x
        cy = child_bbox["y"] - screen_bbox["y"]  # Relative y
        cw = child_bbox["width"]
        ch = child_bbox["height"]

        if cw < 10 or ch < 10:
            continue  # Skip tiny elements (decorators, dividers)

        child_texts = extract_text_content(child, max_depth=5)

        # Classify position
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

        # Extract component names from instances in this panel
        panel_instances = extract_component_instances(child, max_depth=5)
        component_names = list(set(inst["name"].split("/")[0] for inst in panel_instances if inst["name"]))

        panels.append({
            "position": position,
            "name": child.get("name", ""),
            "width_approx": round(cw),
            "height_approx": round(ch),
            "role": role,
            "components": component_names[:20],  # Top 20 unique component roots
            "text_labels": child_texts[:15],      # First 15 text items
        })

    # Classify overall layout type
    positions = [p["position"] for p in panels]
    has_left = "left" in positions
    has_right = "right" in positions
    has_top = "top" in positions
    has_bottom = "bottom" in positions
    has_center = "center" in positions

    if has_left and has_right and has_center:
        layout_type = "three_panel"
    elif has_left and has_center:
        layout_type = "sidebar_content"
    elif has_center and not has_left and not has_right:
        # Check if center has repeated similar-sized children (grid)
        center_panels = [p for p in panels if p["position"] == "center"]
        if len(center_panels) > 3:
            widths = [p["width_approx"] for p in center_panels]
            if widths and max(widths) - min(widths) < 50:
                layout_type = "cards_grid"
            else:
                layout_type = "full_canvas"
        else:
            layout_type = "full_canvas"
    elif has_left and has_right and not has_center:
        layout_type = "split_panel"
    elif has_top and has_bottom and has_center:
        layout_type = "header_content_footer"
    else:
        layout_type = "other"

    # Build description
    parts = []
    for p in sorted(panels, key=lambda x: {"top": 0, "left": 1, "center": 2, "right": 3, "bottom": 4}.get(x["position"], 5)):
        parts.append(f"{p['position'].title()} {p['role']} ({p['width_approx']}×{p['height_approx']})")
    description = ", ".join(parts) if parts else "Unknown layout"

    return {
        "type": layout_type,
        "description": description,
        "panels": panels,
    }


def infer_capabilities(text_content, component_instances, layout):
    """Infer screen capabilities from text, components, and layout."""
    caps = set()
    all_text = " ".join(text_content).lower()
    comp_names = " ".join(inst.get("name", "") for inst in component_instances).lower()
    combined = all_text + " " + comp_names

    capability_keywords = {
        "search": ["search", "find", "filter", "query"],
        "file_management": ["files", "folders", "upload", "download", "documents"],
        "editing": ["edit", "editor", "canvas", "draw", "compose"],
        "3d_editing": ["3d", "scene", "viewport", "render", "material"],
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
    """Detect if a screen is light or dark theme based on background fills."""
    fills = node.get("fills", [])
    for fill in fills:
        if fill.get("type") == "SOLID" and fill.get("visible", True):
            color = fill.get("color", {})
            r = color.get("r", 1)
            g = color.get("g", 1)
            b = color.get("b", 1)
            luminance = 0.299 * r + 0.587 * g + 0.114 * b
            return luminance > 0.5  # True = light, False = dark

    # Check first child with a fill
    for child in node.get("children", [])[:3]:
        if max_depth > 0:
            result = detect_theme(child, max_depth - 1)
            if result is not None:
                return result

    return True  # Default to light


def analyze_screen(screen_info):
    """Full analysis of a single screen node."""
    node = screen_info["node"]
    bbox = extract_bbox(node)

    # Extract all text content
    all_text = extract_text_content(node, max_depth=25)

    # Extract all component instances
    instances = extract_component_instances(node, max_depth=25)

    # Analyze layout
    layout = analyze_layout(node)

    # Infer capabilities
    capabilities = infer_capabilities(all_text, instances, layout)

    # Detect theme
    is_light = detect_theme(node)

    # Count total components
    total_children = count_all_children(node, max_depth=25)

    return {
        "screen_id": node.get("id", ""),
        "screen_name": node.get("name", ""),
        "page": screen_info["page_name"],
        "path": screen_info["path"],
        "node_type": node.get("type", ""),
        "depth_found": screen_info["depth"],
        "is_variant": screen_info["is_variant"],
        "dimensions": {
            "width": round(bbox["width"]),
            "height": round(bbox["height"]),
        },
        "is_light": is_light,
        "layout": layout,
        "capabilities": capabilities,
        "all_text_content": all_text[:100],  # First 100 text items
        "component_count": len(instances),
        "total_descendants": total_children,
        "nested_components": instances[:50],  # First 50 instances
    }


def analyze_kit(kit_name):
    """Analyze all screens in a single kit's FIGMA_FULL.json."""
    full_path = os.path.join(KIT_SCREENS_DIR, kit_name, "FIGMA_FULL.json")

    if not os.path.exists(full_path):
        print(f"  ERROR: {full_path} not found. Run Phase 1 first.")
        return None

    print(f"  Loading {full_path}...")
    with open(full_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    doc = data.get("document", {})
    pages = doc.get("children", [])

    print(f"  Pages: {len(pages)}, Total nodes: {data.get('total_nodes', '?')}")

    # Find ALL screens at any depth
    all_screens = []
    for page in pages:
        page_screens = find_all_screens(page)
        all_screens.extend(page_screens)

    print(f"  Found {len(all_screens)} screen-sized nodes (>= {MIN_SCREEN_WIDTH}x{MIN_SCREEN_HEIGHT})")

    # Filter out dark/mobile variants
    light_screens = [s for s in all_screens if not s["is_variant"]]
    variant_screens = [s for s in all_screens if s["is_variant"]]
    print(f"  Light/desktop: {len(light_screens)}, Variants (dark/mobile): {len(variant_screens)}")

    # Analyze each screen
    analyzed = []
    for i, screen_info in enumerate(light_screens):
        name = screen_info["node"].get("name", "")
        if (i + 1) % 10 == 0 or i == 0:
            print(f"  Analyzing screen {i+1}/{len(light_screens)}: {name}")
        analyzed.append(analyze_screen(screen_info))

    # Build kit result
    result = {
        "kit_name": kit_name,
        "file_key": data.get("file_key", ""),
        "analyzed_at": datetime.now().isoformat(),
        "source_file": full_path,
        "summary": {
            "total_screens_found": len(all_screens),
            "light_desktop_screens": len(light_screens),
            "variant_screens_skipped": len(variant_screens),
            "pages_with_screens": len(set(s["page_name"] for s in all_screens)),
            "deepest_screen": max((s["depth"] for s in all_screens), default=0),
            "layout_types": dict(defaultdict(int)),
            "node_types": dict(defaultdict(int)),
        },
        "screens": analyzed,
        "variant_screens": [
            {
                "screen_id": s["node"].get("id", ""),
                "screen_name": s["node"].get("name", ""),
                "page": s["page_name"],
                "node_type": s["node"].get("type", ""),
            }
            for s in variant_screens
        ],
    }

    # Count layout types and node types
    layout_counts = defaultdict(int)
    node_type_counts = defaultdict(int)
    for screen in analyzed:
        layout_counts[screen["layout"]["type"]] += 1
        node_type_counts[screen["node_type"]] += 1
    result["summary"]["layout_types"] = dict(layout_counts)
    result["summary"]["node_types"] = dict(node_type_counts)

    return result


def main():
    print(f"\n{'='*60}")
    print(f"FIGMA STRUCTURE ANALYZER — Phase 2")
    print(f"Parse full JSON trees into screen/layout/component data")
    print(f"{'='*60}")
    print(f"Input:  kit_screens/{{Kit}}/FIGMA_FULL.json")
    print(f"Output: kit_screens/{{Kit}}/SCREEN_ANALYSIS.json")
    print(f"        kit_screens/CORE_KITS_LIBRARY.json")
    print(f"{'='*60}\n")

    combined = {
        "generated_at": datetime.now().isoformat(),
        "kits": {},
        "grand_totals": {
            "total_screens": 0,
            "total_light_screens": 0,
            "total_variants_skipped": 0,
            "layout_type_totals": defaultdict(int),
        },
    }

    for kit_name in CORE_KITS:
        print(f"\n--- {kit_name} ---")
        result = analyze_kit(kit_name)

        if result is None:
            print(f"  SKIPPED (no data)")
            continue

        # Save per-kit analysis
        out_path = os.path.join(KIT_SCREENS_DIR, kit_name, "SCREEN_ANALYSIS.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"  Saved: {out_path}")

        # Add to combined
        combined["kits"][kit_name] = {
            "file_key": result["file_key"],
            "summary": result["summary"],
            "screens": result["screens"],
        }
        combined["grand_totals"]["total_screens"] += result["summary"]["total_screens_found"]
        combined["grand_totals"]["total_light_screens"] += result["summary"]["light_desktop_screens"]
        combined["grand_totals"]["total_variants_skipped"] += result["summary"]["variant_screens_skipped"]
        for lt, count in result["summary"]["layout_types"].items():
            combined["grand_totals"]["layout_type_totals"][lt] += count

    # Convert defaultdict to dict for JSON
    combined["grand_totals"]["layout_type_totals"] = dict(combined["grand_totals"]["layout_type_totals"])

    # Save combined library
    combined_path = os.path.join(KIT_SCREENS_DIR, "CORE_KITS_LIBRARY.json")
    with open(combined_path, "w", encoding="utf-8") as f:
        json.dump(combined, f, indent=2, ensure_ascii=False)
    print(f"\nCombined library: {combined_path}")

    # Summary
    print(f"\n{'='*60}")
    print(f"ANALYSIS COMPLETE")
    print(f"{'='*60}")
    print(f"Total screens found: {combined['grand_totals']['total_screens']}")
    print(f"Light/desktop screens: {combined['grand_totals']['total_light_screens']}")
    print(f"Variants skipped: {combined['grand_totals']['total_variants_skipped']}")
    print(f"\nLayout types across all kits:")
    for lt, count in sorted(combined["grand_totals"]["layout_type_totals"].items(), key=lambda x: -x[1]):
        print(f"  {lt}: {count}")

    print(f"\nPer-kit breakdown:")
    for kit_name, kit_data in combined["kits"].items():
        s = kit_data["summary"]
        print(f"  {kit_name}: {s['light_desktop_screens']} screens, "
              f"deepest at depth={s['deepest_screen']}, "
              f"layout types: {s['layout_types']}")

    print(f"\n{'='*60}")
    print(f"Next: Run layout_deduplicator.py (Phase 3)")


if __name__ == "__main__":
    main()
