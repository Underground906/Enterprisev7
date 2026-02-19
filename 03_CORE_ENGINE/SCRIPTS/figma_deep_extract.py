#!/usr/bin/env python3
"""
Figma Deep Extract — Phase 1
==============================
Pulls the COMPLETE document tree from Figma API for 4 core kits.
No depth limit = every node, every child, full structure.

Output: kit_screens/{KitName}/FIGMA_FULL.json per kit

Cost: $0 (Figma API metadata is free)
Time: ~20s API + download time for large JSONs
"""

import json
import os
import sys
import time
import requests
from datetime import datetime

# Force unbuffered output
sys.stdout.reconfigure(line_buffering=True)

# === CONFIG ===
FIGMA_TOKEN = os.environ.get("FIGMA_TOKEN", "")
BASE_URL = "https://api.figma.com/v1"
HEADERS = {"X-Figma-Token": FIGMA_TOKEN}

KIT_SCREENS_DIR = os.path.join(
    r"C:\Users\under\Downloads\ENTERPRISE_OS_V7",
    "07_BUILD_FACTORY", "PRJ_UI_Component_Library", "kit_screens"
)

# 4 core kits — file keys from Figma
CORE_KITS = {
    "Brainwave 2.0": "6hCuwRI0GsBmIOJelAVpND",
    "Real Estate SaaS Kit": "88CZ1cuAGLBYxXI743aO1I",
    "Chroma": "TWNCPNCVswFQwUKMq99dYI",
    "Majin": "FcQ8RuwXhtMfNXOJDlZYS7",
}

CHECKPOINT_PATH = os.path.join(KIT_SCREENS_DIR, "DEEP_EXTRACT_CHECKPOINT.json")


def load_checkpoint():
    if os.path.exists(CHECKPOINT_PATH):
        with open(CHECKPOINT_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"completed": [], "failed": []}


def save_checkpoint(cp):
    with open(CHECKPOINT_PATH, "w", encoding="utf-8") as f:
        json.dump(cp, f, indent=2)


def fetch_full_tree(kit_name, file_key):
    """Fetch the FULL document tree from Figma — no depth limit."""
    url = f"{BASE_URL}/files/{file_key}"
    # NO depth param = returns full tree (all levels)
    # geometry=paths would add vector data — skip it, we only need structure
    params = {}

    print(f"  GET {url} (no depth limit, expecting large response)...")
    start = time.time()

    try:
        resp = requests.get(url, headers=HEADERS, params=params, timeout=300)

        if resp.status_code == 429:
            wait = int(resp.headers.get("Retry-After", 60))
            print(f"  Rate limited — waiting {wait}s...")
            time.sleep(wait)
            resp = requests.get(url, headers=HEADERS, params=params, timeout=300)

        elapsed = time.time() - start
        size_mb = len(resp.content) / (1024 * 1024)
        print(f"  Response: {resp.status_code}, {size_mb:.1f} MB, {elapsed:.1f}s")

        if resp.status_code != 200:
            print(f"  ERROR: {resp.status_code} — {resp.text[:300]}")
            return None

        data = resp.json()

        # Validate we got a real document tree
        doc = data.get("document", {})
        pages = doc.get("children", [])
        if not pages:
            print(f"  ERROR: No pages found in response")
            return None

        # Count nodes to verify depth
        def count_nodes(node, depth=0):
            count = 1
            max_d = depth
            for child in node.get("children", []):
                c, d = count_nodes(child, depth + 1)
                count += c
                max_d = max(max_d, d)
            return count, max_d

        total_nodes = 0
        max_depth = 0
        for page in pages:
            n, d = count_nodes(page)
            total_nodes += n
            max_depth = max(max_depth, d)

        print(f"  Pages: {len(pages)}, Total nodes: {total_nodes:,}, Max depth: {max_depth}")

        # Wrap with metadata
        result = {
            "kit_name": kit_name,
            "file_key": file_key,
            "figma_name": data.get("name", ""),
            "last_modified": data.get("lastModified", ""),
            "fetched_at": datetime.now().isoformat(),
            "response_size_mb": round(size_mb, 2),
            "total_nodes": total_nodes,
            "max_depth": max_depth,
            "page_count": len(pages),
            "document": doc,
        }

        return result

    except requests.exceptions.Timeout:
        print(f"  TIMEOUT after 300s for {kit_name}")
        return None
    except requests.exceptions.ConnectionError as e:
        print(f"  CONNECTION ERROR: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"  JSON PARSE ERROR: {e}")
        return None
    except Exception as e:
        print(f"  UNEXPECTED ERROR: {type(e).__name__}: {e}")
        return None


def main():
    print(f"\n{'='*60}")
    print(f"FIGMA DEEP EXTRACT — Phase 1")
    print(f"4 Core Kits, Full Tree (no depth limit)")
    print(f"{'='*60}")
    print(f"Output: {KIT_SCREENS_DIR}/{{KitName}}/FIGMA_FULL.json")
    print(f"{'='*60}\n")

    checkpoint = load_checkpoint()
    results = {}

    for i, (kit_name, file_key) in enumerate(CORE_KITS.items(), 1):
        if kit_name in checkpoint["completed"]:
            # Verify the file actually exists
            kit_dir = os.path.join(KIT_SCREENS_DIR, kit_name)
            full_path = os.path.join(kit_dir, "FIGMA_FULL.json")
            if os.path.exists(full_path):
                size_mb = os.path.getsize(full_path) / (1024 * 1024)
                print(f"[{i}/4] SKIP (already done): {kit_name} ({size_mb:.1f} MB)")
                results[kit_name] = {"status": "cached", "size_mb": round(size_mb, 2)}
                continue
            else:
                # Checkpoint says done but file missing — re-fetch
                print(f"[{i}/4] RE-FETCHING (file missing): {kit_name}")
                checkpoint["completed"].remove(kit_name)

        print(f"[{i}/4] {kit_name} ({file_key})")
        data = fetch_full_tree(kit_name, file_key)

        if data:
            kit_dir = os.path.join(KIT_SCREENS_DIR, kit_name)
            os.makedirs(kit_dir, exist_ok=True)
            full_path = os.path.join(kit_dir, "FIGMA_FULL.json")

            print(f"  Writing {full_path}...")
            with open(full_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            size_mb = os.path.getsize(full_path) / (1024 * 1024)
            print(f"  Saved: {size_mb:.1f} MB")

            checkpoint["completed"].append(kit_name)
            save_checkpoint(checkpoint)

            results[kit_name] = {
                "status": "ok",
                "size_mb": round(size_mb, 2),
                "total_nodes": data["total_nodes"],
                "max_depth": data["max_depth"],
                "pages": data["page_count"],
            }
        else:
            checkpoint["failed"].append(kit_name)
            save_checkpoint(checkpoint)
            results[kit_name] = {"status": "FAILED"}

        # 5s delay between kits
        if i < len(CORE_KITS):
            print(f"  Waiting 5s before next kit...")
            time.sleep(5)

    # Summary
    print(f"\n{'='*60}")
    print(f"DEEP EXTRACT COMPLETE")
    print(f"{'='*60}")
    for kit_name, info in results.items():
        status = info["status"]
        if status in ("ok", "cached"):
            print(f"  {kit_name}: {info['size_mb']:.1f} MB"
                  + (f", {info.get('total_nodes', '?'):,} nodes, depth={info.get('max_depth', '?')}" if status == "ok" else " (cached)"))
        else:
            print(f"  {kit_name}: FAILED")
    print(f"{'='*60}")
    print(f"\nNext: Run figma_structure_analyzer.py (Phase 2)")


if __name__ == "__main__":
    main()
