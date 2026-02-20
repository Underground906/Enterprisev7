#!/usr/bin/env python3
"""Run Phases 2-5 for a given kit. Usage: python strivo_phases.py [kit_name]"""
import json, os, sys, time, requests
from pathlib import Path
from datetime import datetime
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8', errors='replace', line_buffering=True)

PROJECT_ROOT = Path(r"C:\Users\under\Downloads\ENTERPRISE_OS_V7")
KIT_SCREENS_DIR = PROJECT_ROOT / "07_BUILD_FACTORY" / "PRJ_UI_Component_Library" / "kit_screens"

env_path = PROJECT_ROOT / ".env"
if env_path.exists():
    with open(env_path, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, val = line.split("=", 1)
                os.environ[key.strip()] = val.strip()

FIGMA_TOKEN = os.environ.get("FIGMA_TOKEN", "")
HEADERS = {"X-Figma-Token": FIGMA_TOKEN}

kit_name = sys.argv[1] if len(sys.argv) >= 2 else "Strivo"
kit_dir = KIT_SCREENS_DIR / kit_name

# --- PHASE 2: Structure Analysis ---
print(f"Phase 2: Loading FIGMA_FULL.json...")
with open(kit_dir / "FIGMA_FULL.json", "r", encoding="utf-8") as f:
    figma = json.load(f)

file_key = figma.get("file_key", "")


def classify_layout(node):
    w = node.get("absoluteBoundingBox", {}).get("width", 0)
    h = node.get("absoluteBoundingBox", {}).get("height", 0)
    children = node.get("children", [])
    name_lower = node.get("name", "").lower()

    has_sidebar = False
    has_nav = False
    has_table = False
    has_cards = False
    has_form = False
    has_hero = False

    for ch in children:
        cn = ch.get("name", "").lower()
        cw = ch.get("absoluteBoundingBox", {}).get("width", 0)

        if ("sidebar" in cn or "side-bar" in cn or "nav" in cn) and cw < w * 0.3:
            has_sidebar = True
        if "nav" in cn or "header" in cn or "topbar" in cn:
            has_nav = True
        if "table" in cn or "grid" in cn or "list" in cn:
            has_table = True
        if "card" in cn:
            has_cards = True
        if "form" in cn or "input" in cn or "field" in cn:
            has_form = True
        if "hero" in cn:
            has_hero = True

    if has_sidebar:
        return "sidebar_content"
    elif has_table:
        return "data_table"
    elif has_cards:
        return "card_grid"
    elif has_form:
        return "form_layout"
    elif has_hero:
        return "hero_section"
    elif w > 1200:
        return "full_canvas"
    else:
        return "standard"


screens = []
doc = figma.get("document", {})
for page in doc.get("children", []):
    for child in page.get("children", []):
        if child.get("type") in ("FRAME", "COMPONENT", "COMPONENT_SET"):
            bbox = child.get("absoluteBoundingBox", {})
            w = bbox.get("width", 0)
            h = bbox.get("height", 0)
            if w >= 300 and h >= 300:
                screen = {
                    "id": child.get("id", ""),
                    "name": child.get("name", ""),
                    "page": page.get("name", ""),
                    "type": child.get("type", ""),
                    "width": w,
                    "height": h,
                    "layout_type": classify_layout(child),
                    "child_count": len(child.get("children", [])),
                }
                screens.append(screen)
        # Also check nested sections
        if child.get("type") == "SECTION":
            for subchild in child.get("children", []):
                if subchild.get("type") in ("FRAME", "COMPONENT", "COMPONENT_SET"):
                    bbox = subchild.get("absoluteBoundingBox", {})
                    w = bbox.get("width", 0)
                    h = bbox.get("height", 0)
                    if w >= 300 and h >= 300:
                        screen = {
                            "id": subchild.get("id", ""),
                            "name": subchild.get("name", ""),
                            "page": page.get("name", "") + " / " + child.get("name", ""),
                            "type": subchild.get("type", ""),
                            "width": w,
                            "height": h,
                            "layout_type": classify_layout(subchild),
                            "child_count": len(subchild.get("children", [])),
                        }
                        screens.append(screen)

# Filter: desktop, light mode
filtered = []
for s in screens:
    name_lower = s["name"].lower()
    if "mobile" in name_lower or "tablet" in name_lower:
        continue
    if "dark" in name_lower:
        continue
    if s["width"] < 900:
        continue
    filtered.append(s)

print(f"Phase 2: {len(screens)} total screens, {len(filtered)} light/desktop")

analysis = {
    "kit_name": kit_name,
    "file_key": file_key,
    "total_screens": len(screens),
    "filtered_screens": len(filtered),
    "screens": filtered,
    "all_screens": screens,
    "analyzed_at": datetime.now().isoformat(),
}
with open(kit_dir / "SCREEN_ANALYSIS.json", "w", encoding="utf-8") as f:
    json.dump(analysis, f, ensure_ascii=False, indent=2)
print(f"Phase 2: OK - {len(filtered)} screens analyzed")

# --- PHASE 3: Layout Deduplication ---
def layout_signature(screen):
    return f"{screen['layout_type']}_{screen['width']}x{screen['height']}_{screen['child_count']}"


groups = defaultdict(list)
for s in filtered:
    sig = layout_signature(s)
    groups[sig].append(s)

templates = []
for sig, group in groups.items():
    rep = group[0]
    templates.append({
        "name": rep["name"],
        "layout_type": rep["layout_type"],
        "width": rep["width"],
        "height": rep["height"],
        "child_count": rep["child_count"],
        "representative_screen": rep["id"],
        "representative_name": rep["name"],
        "screens_using": len(group),
        "screen_ids": [s["id"] for s in group],
        "screen_names": [s["name"] for s in group],
    })

templates.sort(key=lambda t: t["screens_using"], reverse=True)
reduction = round((1 - len(templates) / max(len(filtered), 1)) * 100)

layout_data = {
    "kit_name": kit_name,
    "file_key": file_key,
    "total_screens": len(filtered),
    "unique_layouts": len(templates),
    "reduction_percent": reduction,
    "layouts": templates,
    "generated_at": datetime.now().isoformat(),
}
with open(kit_dir / "LAYOUT_TEMPLATES.json", "w", encoding="utf-8") as f:
    json.dump(layout_data, f, ensure_ascii=False, indent=2)
print(f"Phase 3: OK - {len(filtered)} screens -> {len(templates)} templates ({reduction}%)")

# --- PHASE 4: PNG Export ---
rep_dir = kit_dir / "representative"
rep_dir.mkdir(parents=True, exist_ok=True)


def sanitize(name):
    for ch in "/\\:?\"<>|*":
        name = name.replace(ch, "_")
    return name


downloaded = 0
cached = 0
failed = 0

for i, tmpl in enumerate(templates):
    screen_id = tmpl.get("representative_screen", "")
    screen_name = tmpl.get("representative_name", tmpl.get("name", ""))
    if not screen_id:
        failed += 1
        continue
    safe_name = sanitize(screen_name)
    safe_id = screen_id.replace(":", "_")
    filepath = rep_dir / f"{safe_id}_{safe_name}.png"

    if filepath.exists() and filepath.stat().st_size > 1000:
        cached += 1
        continue

    url = f"https://api.figma.com/v1/images/{file_key}"
    params = {"ids": screen_id, "format": "png", "scale": 0.5}

    try:
        resp = requests.get(url, headers=HEADERS, params=params, timeout=120)
        if resp.status_code == 429:
            wait = min(int(resp.headers.get("Retry-After", 30)), 120)
            print(f"  Rate limited - waiting {wait}s...")
            time.sleep(wait)
            resp = requests.get(url, headers=HEADERS, params=params, timeout=120)
        if resp.status_code != 200:
            failed += 1
            print(f"  [{i+1}/{len(templates)}] FAILED: HTTP {resp.status_code}")
            continue
        img_data = resp.json()
        img_url = img_data.get("images", {}).get(screen_id)
        if not img_url:
            failed += 1
            continue
        dl_resp = requests.get(img_url, timeout=60)
        if dl_resp.status_code != 200 or len(dl_resp.content) < 500:
            failed += 1
            continue
        with open(filepath, "wb") as f:
            f.write(dl_resp.content)
        downloaded += 1
        if downloaded % 10 == 0:
            print(f"  [{i+1}/{len(templates)}] {downloaded} downloaded...")
    except Exception as e:
        failed += 1
        print(f"  [{i+1}/{len(templates)}] ERROR: {e}")
    time.sleep(3)

print(f"Phase 4: OK - {downloaded} new + {cached} cached = {downloaded+cached} PNGs ({failed} failed)")

# --- PHASE 5: Update Library ---
library_path = KIT_SCREENS_DIR / "CORE_LAYOUT_LIBRARY.json"
if library_path.exists():
    with open(library_path, "r", encoding="utf-8") as f:
        library = json.load(f)
else:
    library = {"kits": {}, "metadata": {}}

kits = library.get("kits", {})
kits[kit_name] = {
    "file_key": file_key,
    "total_screens": len(filtered),
    "unique_layouts": len(templates),
    "reduction_percent": reduction,
    "layouts": templates,
    "updated_at": datetime.now().isoformat(),
}

total_screens = sum(k.get("total_screens", 0) for k in kits.values())
total_layouts = sum(k.get("unique_layouts", 0) for k in kits.values())

library["kits"] = kits
library["metadata"] = {
    "total_kits": len(kits),
    "total_screens": total_screens,
    "total_unique_layouts": total_layouts,
    "total_representative_screens": total_layouts,
    "updated_at": datetime.now().isoformat(),
}

with open(library_path, "w", encoding="utf-8") as f:
    json.dump(library, f, ensure_ascii=False, indent=2)

print(f"Phase 5: OK - library now has {len(kits)} kits, {total_layouts} templates")

# Update checkpoint
cp_path = KIT_SCREENS_DIR / "BATCH_PIPELINE_CHECKPOINT.json"
if cp_path.exists():
    with open(cp_path, "r", encoding="utf-8") as f:
        cp = json.load(f)
else:
    cp = {"completed_kits": [], "failed_kits": []}

if kit_name not in cp["completed_kits"]:
    cp["completed_kits"].append(kit_name)
if kit_name in cp.get("failed_kits", []):
    cp["failed_kits"].remove(kit_name)
cp["updated_at"] = datetime.now().isoformat()

with open(cp_path, "w", encoding="utf-8") as f:
    json.dump(cp, f, ensure_ascii=False, indent=2)

print(f"\nStrivo DONE - moved from failed to completed")
