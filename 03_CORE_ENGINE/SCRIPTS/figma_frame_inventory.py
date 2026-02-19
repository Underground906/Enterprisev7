#!/usr/bin/env python3
"""
Figma Frame Title Inventory
============================
Pulls page/frame/component metadata from Figma API for all kits.
NO PNGs, NO vision API. Just structured names from the document tree.

Output: kit_screens/{KitName}/INVENTORY.json per kit
        kit_screens/MASTER_FRAME_INVENTORY.json (all kits combined)

Cost: $0 (Figma API metadata is free)
"""

import json
import os
import sys
import time
import requests
from datetime import datetime

# === CONFIG ===
FIGMA_TOKEN = os.environ.get("FIGMA_TOKEN", "")
BASE_URL = "https://api.figma.com/v1"
OUTPUT_DIR = r"C:\Users\under\Downloads\ENTERPRISE_OS_V7\07_BUILD_FACTORY\PRJ_UI_Component_Library\kit_screens"
KIT_INDEX_PATH = r"C:\Users\under\Downloads\ENTERPRISE_OS_V7\07_BUILD_FACTORY\PRJ_UI_Component_Library\03_Design\KIT_INDEX.json"
CHECKPOINT_PATH = os.path.join(OUTPUT_DIR, "CHECKPOINT.json")

# Skip patterns for filtering
SKIP_PATTERNS = ["dark", "mobile", "tablet", "ipad", "android", "responsive"]

# Untitled UI Pro - only these specific node IDs
UNTITLED_UI_NODES = ["6277-291692", "1664-398802", "1686-419020", "6277-315325"]

# Extra kits not in KIT_INDEX
EXTRA_KITS = {
    "Core Dashboard Builder": {"file_key": "CiyOckN4TAM0u6mfSsl4QI"},
    "Tuskter CRM": {"file_key": "t5IRTNkDbSGsiLrtawggae"}
}

# Skip these kits
SKIP_KITS = ["Fitness Pro"]

HEADERS = {"X-Figma-Token": FIGMA_TOKEN}


def load_kit_list():
    """Load all kits from KIT_INDEX + extras, minus skips."""
    with open(KIT_INDEX_PATH, "r", encoding="utf-8") as f:
        kit_index = json.load(f)

    kits = {}
    for name, data in kit_index.items():
        if name in SKIP_KITS:
            continue
        kits[name] = data.get("file_key", "")

    for name, data in EXTRA_KITS.items():
        kits[name] = data["file_key"]

    return kits


def load_checkpoint():
    """Load checkpoint of completed kits."""
    if os.path.exists(CHECKPOINT_PATH):
        with open(CHECKPOINT_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"completed": [], "failed": []}


def save_checkpoint(checkpoint):
    with open(CHECKPOINT_PATH, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, indent=2)


def is_skip_name(name):
    """Check if a page/frame name should be filtered out (dark/mobile/tablet)."""
    lower = name.lower()
    for pattern in SKIP_PATTERNS:
        if pattern in lower:
            return True
    return False


def classify_node(node, depth=0):
    """Classify a node as screen or component based on type and position."""
    node_type = node.get("type", "")
    name = node.get("name", "")

    result = {
        "id": node.get("id", ""),
        "name": name,
        "type": node_type,
        "skip": is_skip_name(name),
    }

    # Add size if available
    bbox = node.get("absoluteBoundingBox", {})
    if bbox:
        result["width"] = bbox.get("width", 0)
        result["height"] = bbox.get("height", 0)

    return result


def process_page(page_node):
    """Process a single page node and extract all top-level frames."""
    page_name = page_node.get("name", "Unknown")
    page_id = page_node.get("id", "")
    skip_page = is_skip_name(page_name)

    frames = []
    components = []
    children = page_node.get("children", [])

    for child in children:
        info = classify_node(child)
        child_type = child.get("type", "")
        child_name = child.get("name", "")

        # Determine if this is a component page or a screen page
        if child_type in ("COMPONENT", "COMPONENT_SET"):
            components.append(info)
        elif child_type == "FRAME":
            # Check if it looks like a component (small size, or component-like name)
            w = info.get("width", 0)
            h = info.get("height", 0)
            # Full screens are typically >900px wide
            if w >= 900:
                frames.append(info)
            else:
                components.append(info)
        elif child_type == "GROUP":
            frames.append(info)
        else:
            # Instance, rectangle, etc - treat as component
            components.append(info)

    return {
        "page_id": page_id,
        "page_name": page_name,
        "skip_page": skip_page,
        "screens": frames,
        "components": components,
        "screen_count": len(frames),
        "component_count": len(components),
        "light_desktop_screens": len([f for f in frames if not f["skip"]]),
        "light_desktop_components": len([c for c in components if not c["skip"]]),
    }


def fetch_kit(kit_name, file_key, specific_nodes=None):
    """Fetch a kit's document tree from Figma API."""
    print(f"  Fetching: {kit_name} ({file_key})...")

    url = f"{BASE_URL}/files/{file_key}"
    params = {"depth": 2}  # Get pages + top-level children

    if specific_nodes:
        # For Untitled UI, only get specific nodes
        params["ids"] = ",".join(specific_nodes)

    try:
        resp = requests.get(url, headers=HEADERS, params=params, timeout=60)

        if resp.status_code == 429:
            # Rate limited - wait and retry
            wait = int(resp.headers.get("Retry-After", 30))
            print(f"    Rate limited. Waiting {wait}s...")
            time.sleep(wait)
            resp = requests.get(url, headers=HEADERS, params=params, timeout=60)

        if resp.status_code != 200:
            print(f"    ERROR: {resp.status_code} - {resp.text[:200]}")
            return None

        data = resp.json()
        doc = data.get("document", {})
        pages = doc.get("children", [])

        kit_result = {
            "kit_name": kit_name,
            "file_key": file_key,
            "figma_name": data.get("name", ""),
            "last_modified": data.get("lastModified", ""),
            "fetched_at": datetime.now().isoformat(),
            "pages": [],
            "totals": {
                "pages": 0,
                "all_screens": 0,
                "all_components": 0,
                "light_desktop_screens": 0,
                "light_desktop_components": 0,
                "skipped_screens": 0,
                "skipped_components": 0,
            }
        }

        for page in pages:
            page_data = process_page(page)
            kit_result["pages"].append(page_data)

            kit_result["totals"]["pages"] += 1
            kit_result["totals"]["all_screens"] += page_data["screen_count"]
            kit_result["totals"]["all_components"] += page_data["component_count"]
            kit_result["totals"]["light_desktop_screens"] += page_data["light_desktop_screens"]
            kit_result["totals"]["light_desktop_components"] += page_data["light_desktop_components"]
            kit_result["totals"]["skipped_screens"] += (page_data["screen_count"] - page_data["light_desktop_screens"])
            kit_result["totals"]["skipped_components"] += (page_data["component_count"] - page_data["light_desktop_components"])

        return kit_result

    except requests.exceptions.Timeout:
        print(f"    TIMEOUT for {kit_name}")
        return None
    except Exception as e:
        print(f"    ERROR: {e}")
        return None


def run_inventory():
    """Run the full inventory across all kits."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    kits = load_kit_list()
    checkpoint = load_checkpoint()

    total_kits = len(kits)
    print(f"\n{'='*60}")
    print(f"FIGMA FRAME TITLE INVENTORY")
    print(f"{'='*60}")
    print(f"Total kits: {total_kits}")
    print(f"Already completed: {len(checkpoint['completed'])}")
    print(f"Remaining: {total_kits - len(checkpoint['completed'])}")
    print(f"{'='*60}\n")

    master_inventory = {}
    grand_totals = {
        "kits_processed": 0,
        "kits_failed": 0,
        "total_pages": 0,
        "total_screens": 0,
        "total_components": 0,
        "light_desktop_screens": 0,
        "light_desktop_components": 0,
        "needs_ocr": 0,
    }

    for i, (kit_name, file_key) in enumerate(sorted(kits.items()), 1):
        if kit_name in checkpoint["completed"]:
            # Load existing result
            kit_dir = os.path.join(OUTPUT_DIR, kit_name.replace("/", "_"))
            inv_path = os.path.join(kit_dir, "INVENTORY.json")
            if os.path.exists(inv_path):
                with open(inv_path, "r", encoding="utf-8") as f:
                    result = json.load(f)
                master_inventory[kit_name] = result
                t = result["totals"]
                grand_totals["kits_processed"] += 1
                grand_totals["total_pages"] += t["pages"]
                grand_totals["total_screens"] += t["all_screens"]
                grand_totals["total_components"] += t["all_components"]
                grand_totals["light_desktop_screens"] += t["light_desktop_screens"]
                grand_totals["light_desktop_components"] += t["light_desktop_components"]
            print(f"[{i}/{total_kits}] SKIP (already done): {kit_name}")
            continue

        print(f"[{i}/{total_kits}] {kit_name}")

        # Special handling for Untitled UI Pro
        specific_nodes = None
        if kit_name == "Untitled UI Pro":
            specific_nodes = UNTITLED_UI_NODES

        result = fetch_kit(kit_name, file_key, specific_nodes)

        if result:
            # Save per-kit inventory
            kit_dir = os.path.join(OUTPUT_DIR, kit_name.replace("/", "_"))
            os.makedirs(kit_dir, exist_ok=True)
            inv_path = os.path.join(kit_dir, "INVENTORY.json")
            with open(inv_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2)

            master_inventory[kit_name] = result
            t = result["totals"]
            grand_totals["kits_processed"] += 1
            grand_totals["total_pages"] += t["pages"]
            grand_totals["total_screens"] += t["all_screens"]
            grand_totals["total_components"] += t["all_components"]
            grand_totals["light_desktop_screens"] += t["light_desktop_screens"]
            grand_totals["light_desktop_components"] += t["light_desktop_components"]

            checkpoint["completed"].append(kit_name)
            save_checkpoint(checkpoint)

            print(f"    Pages: {t['pages']} | Screens: {t['light_desktop_screens']} (skip {t['skipped_screens']}) | Components: {t['light_desktop_components']} (skip {t['skipped_components']})")
        else:
            grand_totals["kits_failed"] += 1
            checkpoint["failed"].append(kit_name)
            save_checkpoint(checkpoint)
            print(f"    FAILED")

        # Rate limit: 30 req/min for Figma API
        time.sleep(2)

    # Save master inventory
    master_path = os.path.join(OUTPUT_DIR, "MASTER_FRAME_INVENTORY.json")
    master_output = {
        "generated_at": datetime.now().isoformat(),
        "grand_totals": grand_totals,
        "kits": {}
    }

    # Summary per kit for master (not full detail)
    for kit_name, result in master_inventory.items():
        t = result["totals"]
        pages_summary = []
        for p in result["pages"]:
            pages_summary.append({
                "page_name": p["page_name"],
                "page_id": p["page_id"],
                "skip": p["skip_page"],
                "screens": p["light_desktop_screens"],
                "components": p["light_desktop_components"],
                "screen_names": [s["name"] for s in p["screens"] if not s["skip"]],
            })
        master_output["kits"][kit_name] = {
            "file_key": result["file_key"],
            "figma_name": result["figma_name"],
            "totals": t,
            "pages": pages_summary,
        }

    with open(master_path, "w", encoding="utf-8") as f:
        json.dump(master_output, f, indent=2)

    # Print summary
    print(f"\n{'='*60}")
    print(f"INVENTORY COMPLETE")
    print(f"{'='*60}")
    print(f"Kits processed: {grand_totals['kits_processed']}")
    print(f"Kits failed: {grand_totals['kits_failed']}")
    print(f"Total pages: {grand_totals['total_pages']}")
    print(f"Total screens (all): {grand_totals['total_screens']}")
    print(f"Light desktop screens: {grand_totals['light_desktop_screens']}")
    print(f"Total components (all): {grand_totals['total_components']}")
    print(f"Light desktop components: {grand_totals['light_desktop_components']}")
    print(f"{'='*60}")
    print(f"\nPer-kit inventories: {OUTPUT_DIR}/{{KitName}}/INVENTORY.json")
    print(f"Master inventory: {master_path}")

    # Print per-kit summary table
    print(f"\n{'Kit Name':<35} {'Pages':>6} {'Screens':>8} {'Comps':>8} {'Skip':>6}")
    print("-" * 70)
    for kit_name in sorted(master_inventory.keys()):
        t = master_inventory[kit_name]["totals"]
        skip = t["skipped_screens"] + t["skipped_components"]
        print(f"{kit_name:<35} {t['pages']:>6} {t['light_desktop_screens']:>8} {t['light_desktop_components']:>8} {skip:>6}")


if __name__ == "__main__":
    run_inventory()
