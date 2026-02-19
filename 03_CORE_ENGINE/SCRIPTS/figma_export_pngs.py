#!/usr/bin/env python3
"""
Figma PNG Exporter v2
=====================
Uses VERIFIED frame IDs from per-kit INVENTORY.json files (depth=2).
Only exports frames we already confirmed exist. No re-discovery.

Exports to kit_screens/{KitName}/screens/ and kit_screens/{KitName}/components/
Checkpoint after every kit.
"""

import json
import os
import sys
import time
import requests
from pathlib import Path
from datetime import datetime

FIGMA_TOKEN = os.environ.get("FIGMA_TOKEN", "")
BASE_URL = "https://api.figma.com/v1"
HEADERS = {"X-Figma-Token": FIGMA_TOKEN}

KIT_SCREENS_DIR = Path(r"C:\Users\under\Downloads\ENTERPRISE_OS_V7\07_BUILD_FACTORY\PRJ_UI_Component_Library\kit_screens")
CHECKPOINT_PATH = KIT_SCREENS_DIR / "EXPORT_CHECKPOINT_V2.json"

# Figma API: max ~100 IDs per batch, 30 req/min
BATCH_SIZE = 80
RATE_DELAY = 2.5

# Force unbuffered output
sys.stdout.reconfigure(line_buffering=True)


def load_kit_inventories():
    """Load all per-kit INVENTORY.json files. Returns {kit_name: {file_key, screens, components}}."""
    kits = {}
    for kit_dir in sorted(KIT_SCREENS_DIR.iterdir()):
        if not kit_dir.is_dir():
            continue
        inv_path = kit_dir / "INVENTORY.json"
        if not inv_path.exists():
            continue

        with open(inv_path, "r", encoding="utf-8") as f:
            inv = json.load(f)

        kit_name = inv.get("kit_name", kit_dir.name)
        file_key = inv.get("file_key", "")
        if not file_key:
            continue

        # Collect all light desktop screen and component IDs
        screens = []
        components = []
        for page in inv.get("pages", []):
            if page.get("skip_page", False):
                continue
            for s in page.get("screens", []):
                if not s.get("skip", False) and s.get("id"):
                    screens.append({
                        "id": s["id"],
                        "name": s.get("name", ""),
                        "page": page.get("page_name", ""),
                        "width": s.get("width", 0),
                        "height": s.get("height", 0),
                    })
            for c in page.get("components", []):
                if not c.get("skip", False) and c.get("id"):
                    components.append({
                        "id": c["id"],
                        "name": c.get("name", ""),
                        "page": page.get("page_name", ""),
                        "width": c.get("width", 0),
                        "height": c.get("height", 0),
                    })

        kits[kit_name] = {
            "file_key": file_key,
            "screens": screens,
            "components": components,
            "dir": kit_dir,
        }

    return kits


def load_checkpoint():
    if CHECKPOINT_PATH.exists():
        with open(CHECKPOINT_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"completed": {}, "failed": []}


def save_checkpoint(cp):
    with open(CHECKPOINT_PATH, "w", encoding="utf-8") as f:
        json.dump(cp, f, indent=2)


def export_frames(file_key, frame_ids, batch_size=50, scale=1.0):
    """Call Figma export API to get PNG URLs for frame IDs."""
    if not frame_ids:
        return {}

    all_urls = {}
    batches = [frame_ids[i:i+batch_size] for i in range(0, len(frame_ids), batch_size)]

    for batch_num, batch in enumerate(batches):
        ids_str = ",".join(batch)
        url = f"{BASE_URL}/images/{file_key}"
        params = {"ids": ids_str, "format": "png", "scale": scale}

        resp = requests.get(url, headers=HEADERS, params=params, timeout=180)
        if resp.status_code == 429:
            wait = int(resp.headers.get("Retry-After", 30))
            print(f"    Rate limited, waiting {wait}s...")
            time.sleep(wait)
            resp = requests.get(url, headers=HEADERS, params=params, timeout=180)

        if resp.status_code == 400:
            # Render timeout - retry with smaller batches
            print(f"    Batch {batch_num+1} render timeout, splitting into mini-batches of 3...")
            mini_batches = [batch[i:i+3] for i in range(0, len(batch), 3)]
            for mb in mini_batches:
                mb_str = ",".join(mb)
                mb_resp = requests.get(url, headers=HEADERS, params={"ids": mb_str, "format": "png", "scale": scale}, timeout=180)
                if mb_resp.status_code == 200:
                    mb_data = mb_resp.json()
                    for nid, img_url in mb_data.get("images", {}).items():
                        if img_url:
                            all_urls[nid] = img_url
                elif mb_resp.status_code == 429:
                    wait = int(mb_resp.headers.get("Retry-After", 30))
                    print(f"    Rate limited, waiting {wait}s...")
                    time.sleep(wait)
                time.sleep(RATE_DELAY)
            continue

        if resp.status_code != 200:
            print(f"    Export batch {batch_num+1} FAILED: {resp.status_code}")
            continue

        data = resp.json()
        err = data.get("err")
        if err:
            print(f"    API error: {err}")

        images = data.get("images", {})
        got = 0
        null_count = 0
        for nid, img_url in images.items():
            if img_url:
                all_urls[nid] = img_url
                got += 1
            else:
                null_count += 1

        if len(batches) > 1:
            print(f"    Batch {batch_num+1}/{len(batches)}: {got} URLs, {null_count} null")
        time.sleep(RATE_DELAY)

    return all_urls


def download_pngs(urls_map, frames_lookup, dest_dir):
    """Download PNGs from Figma CDN URLs."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    downloaded = 0
    errors = 0
    skipped = 0

    for node_id, url in urls_map.items():
        frame = frames_lookup.get(node_id, {})
        name = frame.get("name", node_id)
        # Sanitize filename
        safe_name = name.replace("/", "_").replace("\\", "_").replace(":", "_").replace("?", "_").replace('"', "_").replace("<", "_").replace(">", "_").replace("|", "_")
        filename = f"{node_id.replace(':', '_')}_{safe_name}.png"
        filepath = dest_dir / filename

        if filepath.exists() and filepath.stat().st_size > 1000:
            skipped += 1
            continue

        try:
            resp = requests.get(url, timeout=60)
            if resp.status_code == 200 and len(resp.content) > 500:
                with open(filepath, "wb") as f:
                    f.write(resp.content)
                downloaded += 1
            else:
                errors += 1
        except Exception as e:
            errors += 1

    return downloaded, skipped, errors


def process_kit(kit_name, kit_data):
    """Export PNGs for one kit using its inventoried frame IDs."""
    file_key = kit_data["file_key"]
    screens = kit_data["screens"]
    components = kit_data["components"]
    kit_dir = kit_data["dir"]

    total_frames = len(screens) + len(components)
    print(f"  {len(screens)} screens, {len(components)} components = {total_frames} frames")

    if total_frames == 0:
        return {"screens": 0, "components": 0, "exported": 0, "downloaded": 0, "skipped": 0, "errors": 0}

    # Build lookup
    frames_lookup = {s["id"]: s for s in screens}
    frames_lookup.update({c["id"]: c for c in components})

    # Export screens (larger batches - these render fast)
    screen_id_list = [s["id"] for s in screens]
    comp_id_list = [c["id"] for c in components]

    print(f"  Exporting {len(screen_id_list)} screens (batch=50)...")
    screen_urls = export_frames(file_key, screen_id_list, batch_size=50, scale=1.0)
    print(f"  Got {len(screen_urls)}/{len(screen_id_list)} screen URLs")

    # Export components (smaller batches - complex renders)
    print(f"  Exporting {len(comp_id_list)} components (batch=10)...")
    comp_urls = export_frames(file_key, comp_id_list, batch_size=10, scale=1.0)
    print(f"  Got {len(comp_urls)}/{len(comp_id_list)} component URLs")

    # Download screens
    screens_dir = kit_dir / "screens"
    dl_s, skip_s, err_s = download_pngs(screen_urls, frames_lookup, screens_dir)
    print(f"  Screens: {dl_s} new, {skip_s} existing, {err_s} errors")

    # Download components
    comps_dir = kit_dir / "components"
    dl_c, skip_c, err_c = download_pngs(comp_urls, frames_lookup, comps_dir)
    print(f"  Components: {dl_c} new, {skip_c} existing, {err_c} errors")

    totals = {
        "screens_found": len(screens),
        "components_found": len(components),
        "screen_urls": len(screen_urls),
        "comp_urls": len(comp_urls),
        "downloaded": dl_s + dl_c,
        "skipped_existing": skip_s + skip_c,
        "errors": err_s + err_c,
    }

    # Save export index
    index = {
        "kit": kit_name,
        "file_key": file_key,
        "exported_at": datetime.now().isoformat(),
        "totals": totals,
    }
    with open(kit_dir / "EXPORT_INDEX.json", "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    return totals


def main():
    kits = load_kit_inventories()
    checkpoint = load_checkpoint()

    print(f"\n{'='*60}")
    print(f"FIGMA PNG EXPORT v2 — {len(kits)} kits with inventories")
    print(f"Already done: {len(checkpoint['completed'])}")
    print(f"Using VERIFIED frame IDs from INVENTORY.json")
    print(f"{'='*60}\n")

    grand = {"kits": 0, "screens": 0, "components": 0, "downloaded": 0, "errors": 0, "null": 0}

    for i, (kit_name, kit_data) in enumerate(sorted(kits.items()), 1):
        if kit_name in checkpoint["completed"]:
            t = checkpoint["completed"][kit_name]
            grand["kits"] += 1
            grand["screens"] += t.get("screens_found", 0)
            grand["downloaded"] += t.get("downloaded", 0) + t.get("skipped_existing", 0)
            grand["null"] += t.get("null_urls", 0)
            print(f"[{i}/{len(kits)}] SKIP (done): {kit_name}")
            continue

        print(f"[{i}/{len(kits)}] {kit_name}")
        totals = process_kit(kit_name, kit_data)

        checkpoint["completed"][kit_name] = totals
        save_checkpoint(checkpoint)
        grand["kits"] += 1
        grand["screens"] += totals["screens_found"]
        grand["components"] += totals["components_found"]
        grand["downloaded"] += totals["downloaded"] + totals["skipped_existing"]
        grand["errors"] += totals["errors"]
        grand["null"] += totals["null_urls"]
        print(f"  DONE: {totals['downloaded']} new + {totals['skipped_existing']} existing, {totals['null_urls']} null, {totals['errors']} errors\n")

        time.sleep(RATE_DELAY)

    print(f"\n{'='*60}")
    print(f"EXPORT COMPLETE")
    print(f"Kits: {grand['kits']}")
    print(f"Screens found: {grand['screens']}")
    print(f"Components found: {grand['components']}")
    print(f"Total PNGs: {grand['downloaded']}")
    print(f"Null URLs (couldn't render): {grand['null']}")
    print(f"Errors: {grand['errors']}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
