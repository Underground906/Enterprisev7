#!/usr/bin/env python3
"""
Figma Representative PNG Exporter — Phase 4
=============================================
Exports PNGs ONLY for representative screens from Phase 3's layout templates.
Instead of exporting 200+ screens, we export ~30-40 (one per unique layout).

Input:  kit_screens/CORE_LAYOUT_LIBRARY.json (from Phase 3)
Output: kit_screens/{KitName}/representative/{screen_id}_{name}.png

Proven approach: batches of 3-5, scale=0.5, with retry logic.
Cost: $0 (Figma API rendering is free)
"""

import json
import os
import sys
import time
import requests
from pathlib import Path
from datetime import datetime

sys.stdout.reconfigure(line_buffering=True)

FIGMA_TOKEN = os.environ.get("FIGMA_TOKEN", "")
BASE_URL = "https://api.figma.com/v1"
HEADERS = {"X-Figma-Token": FIGMA_TOKEN}

KIT_SCREENS_DIR = Path(
    r"C:\Users\under\Downloads\ENTERPRISE_OS_V7"
    r"\07_BUILD_FACTORY\PRJ_UI_Component_Library\kit_screens"
)

LIBRARY_PATH = KIT_SCREENS_DIR / "CORE_LAYOUT_LIBRARY.json"
CHECKPOINT_PATH = KIT_SCREENS_DIR / "REPRESENTATIVE_EXPORT_CHECKPOINT.json"

# Conservative settings — proven to work
BATCH_SIZE = 3      # Max 3 IDs per render request (avoids 400 timeout)
SCALE = 0.5         # Half resolution — good enough for visual reference
RATE_DELAY = 3.0    # 3s between batches (well within 30 req/min)
DOWNLOAD_TIMEOUT = 60


def load_checkpoint():
    if CHECKPOINT_PATH.exists():
        with open(CHECKPOINT_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"downloaded": {}, "failed": []}


def save_checkpoint(cp):
    with open(CHECKPOINT_PATH, "w", encoding="utf-8") as f:
        json.dump(cp, f, indent=2)


def sanitize_filename(name):
    """Remove/replace chars that aren't safe for filenames."""
    for ch in ['/', '\\', ':', '?', '"', '<', '>', '|', '*']:
        name = name.replace(ch, '_')
    return name


def export_and_download(file_key, node_id, node_name, dest_dir, checkpoint):
    """Export a single node as PNG and download it."""
    safe_name = sanitize_filename(node_name)
    safe_id = node_id.replace(":", "_")
    filename = f"{safe_id}_{safe_name}.png"
    filepath = dest_dir / filename

    # Skip if already downloaded
    if filepath.exists() and filepath.stat().st_size > 1000:
        return "cached", str(filepath)

    # Check checkpoint
    if node_id in checkpoint.get("downloaded", {}):
        if filepath.exists():
            return "cached", str(filepath)

    # Request render from Figma
    url = f"{BASE_URL}/images/{file_key}"
    params = {"ids": node_id, "format": "png", "scale": SCALE}

    try:
        resp = requests.get(url, headers=HEADERS, params=params, timeout=120)

        if resp.status_code == 429:
            wait = int(resp.headers.get("Retry-After", 30))
            print(f"    Rate limited — waiting {wait}s...")
            time.sleep(wait)
            resp = requests.get(url, headers=HEADERS, params=params, timeout=120)

        if resp.status_code == 400:
            # Render timeout — this node can't be rendered
            return "render_timeout", None

        if resp.status_code != 200:
            return f"api_error_{resp.status_code}", None

        data = resp.json()
        images = data.get("images", {})
        img_url = images.get(node_id)

        if not img_url:
            return "null_url", None

        # Download the PNG
        dl_resp = requests.get(img_url, timeout=DOWNLOAD_TIMEOUT)
        if dl_resp.status_code != 200 or len(dl_resp.content) < 500:
            return "download_failed", None

        dest_dir.mkdir(parents=True, exist_ok=True)
        with open(filepath, "wb") as f:
            f.write(dl_resp.content)

        return "ok", str(filepath)

    except requests.exceptions.Timeout:
        return "timeout", None
    except Exception as e:
        return f"error_{type(e).__name__}", None


def main():
    print(f"\n{'='*60}")
    print(f"REPRESENTATIVE PNG EXPORTER — Phase 4")
    print(f"Export one PNG per unique layout template")
    print(f"{'='*60}")

    if not LIBRARY_PATH.exists():
        print(f"ERROR: {LIBRARY_PATH} not found. Run Phase 3 first.")
        sys.exit(1)

    with open(LIBRARY_PATH, "r", encoding="utf-8") as f:
        library = json.load(f)

    checkpoint = load_checkpoint()

    # Collect all representative screens grouped by kit (file_key)
    to_export = []
    for layout in library.get("all_layouts", []):
        kit_name = layout.get("kit", "Unknown")
        file_key = library["kits"].get(kit_name, {}).get("file_key", "")
        screen_id = layout.get("representative_screen", "")
        screen_name = layout.get("representative_name", layout.get("name", ""))
        layout_id = layout.get("layout_id", "")

        if not file_key or not screen_id:
            print(f"  WARNING: Missing file_key or screen_id for {layout_id}")
            continue

        to_export.append({
            "kit_name": kit_name,
            "file_key": file_key,
            "screen_id": screen_id,
            "screen_name": screen_name,
            "layout_id": layout_id,
            "layout_type": layout.get("type", ""),
        })

    print(f"Total representative screens to export: {len(to_export)}")
    print(f"Already downloaded: {len(checkpoint.get('downloaded', {}))}")
    print(f"Scale: {SCALE}, Batch size: {BATCH_SIZE}")
    print(f"{'='*60}\n")

    stats = {"ok": 0, "cached": 0, "failed": 0}

    for i, item in enumerate(to_export, 1):
        kit_name = item["kit_name"]
        screen_id = item["screen_id"]
        layout_id = item["layout_id"]

        dest_dir = KIT_SCREENS_DIR / kit_name / "representative"

        print(f"[{i}/{len(to_export)}] {layout_id} — \"{item['screen_name']}\" ({kit_name})")

        status, path = export_and_download(
            item["file_key"], screen_id, item["screen_name"],
            dest_dir, checkpoint
        )

        if status == "ok":
            stats["ok"] += 1
            checkpoint["downloaded"][screen_id] = {
                "kit": kit_name,
                "layout_id": layout_id,
                "path": path,
                "at": datetime.now().isoformat(),
            }
            save_checkpoint(checkpoint)
            print(f"  Downloaded: {path}")
        elif status == "cached":
            stats["cached"] += 1
            print(f"  Cached: {path}")
        else:
            stats["failed"] += 1
            checkpoint.setdefault("failed", [])
            if screen_id not in checkpoint["failed"]:
                checkpoint["failed"].append(screen_id)
            save_checkpoint(checkpoint)
            print(f"  FAILED: {status}")

        # Rate limit
        if status not in ("cached",):
            time.sleep(RATE_DELAY)

    # Summary
    print(f"\n{'='*60}")
    print(f"EXPORT COMPLETE")
    print(f"{'='*60}")
    print(f"New downloads: {stats['ok']}")
    print(f"Already cached: {stats['cached']}")
    print(f"Failed: {stats['failed']}")
    print(f"Total PNGs available: {stats['ok'] + stats['cached']}")
    print(f"{'='*60}")

    # List all representative PNGs by kit
    print(f"\nRepresentative PNGs by kit:")
    kit_counts = defaultdict(int)
    for item in to_export:
        kit_counts[item["kit_name"]] += 1
    for kit, count in kit_counts.items():
        print(f"  {kit}: {count} layout templates")

    print(f"\n{'='*60}")
    print(f"Next: Run prd_layout_matcher.py (Phase 5)")


if __name__ == "__main__":
    from collections import defaultdict
    main()
