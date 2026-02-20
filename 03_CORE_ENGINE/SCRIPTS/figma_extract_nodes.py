#!/usr/bin/env python3
"""
Figma Targeted Node Extractor
===============================
Pulls specific nodes from a Figma file instead of the whole file.
For files too large for the full /files endpoint (HTTP 400).

Uses /files/{key}/nodes?ids=... to fetch only selected subtrees.
Then formats the output to match FIGMA_FULL.json structure for Phases 2-5.
"""

import json
import os
import sys
import time
import requests
from pathlib import Path
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8', errors='replace', line_buffering=True)

PROJECT_ROOT = Path(r"C:\Users\under\Downloads\ENTERPRISE_OS_V7")
KIT_SCREENS_DIR = PROJECT_ROOT / "07_BUILD_FACTORY" / "PRJ_UI_Component_Library" / "kit_screens"

# Load token from .env
env_path = PROJECT_ROOT / ".env"
if env_path.exists():
    with open(env_path, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, val = line.split("=", 1)
                os.environ[key.strip()] = val.strip()

FIGMA_TOKEN = os.environ.get("FIGMA_TOKEN", "")
BASE_URL = "https://api.figma.com/v1"
HEADERS = {"X-Figma-Token": FIGMA_TOKEN}


def count_nodes(node):
    c = 1
    for child in node.get("children", []):
        c += count_nodes(child)
    return c


def fetch_nodes(file_key, node_ids, kit_name):
    """Fetch specific nodes from Figma and save as FIGMA_FULL.json."""
    kit_dir = KIT_SCREENS_DIR / kit_name
    out_path = kit_dir / "FIGMA_FULL.json"

    kit_dir.mkdir(parents=True, exist_ok=True)

    # Fetch nodes one at a time to avoid size limits
    all_nodes = {}
    for node_id in node_ids:
        url = f"{BASE_URL}/files/{file_key}/nodes"
        params = {"ids": node_id}
        print(f"  Fetching node {node_id}...")
        start = time.time()

        try:
            resp = requests.get(url, headers=HEADERS, params=params, timeout=300)

            if resp.status_code == 429:
                wait = min(int(resp.headers.get("Retry-After", 60)), 120)
                print(f"  Rate limited — waiting {wait}s...")
                time.sleep(wait)
                resp = requests.get(url, headers=HEADERS, params=params, timeout=300)

            elapsed = time.time() - start
            size_mb = len(resp.content) / (1024 * 1024)

            if resp.status_code != 200:
                print(f"  FAILED: HTTP {resp.status_code} for node {node_id} ({elapsed:.1f}s)")
                continue

            data = resp.json()
            nodes_data = data.get("nodes", {})
            if node_id in nodes_data:
                node_doc = nodes_data[node_id].get("document", {})
                total = count_nodes(node_doc)
                print(f"  OK: {total} nodes, {size_mb:.1f} MB, {elapsed:.1f}s — \"{node_doc.get('name', '?')}\"")
                all_nodes[node_id] = node_doc
            else:
                print(f"  WARNING: Node {node_id} not in response")

        except Exception as e:
            print(f"  FAILED: {type(e).__name__}: {e}")
            continue

        time.sleep(3)  # Rate limit between requests

    if not all_nodes:
        print("ERROR: No nodes fetched")
        return False

    # Build a FIGMA_FULL.json-compatible structure
    # Create a fake document with each node as a "page"
    pages = []
    for node_id, node_doc in all_nodes.items():
        # Make sure the node looks like a page (CANVAS type)
        page = {
            "id": node_id,
            "name": node_doc.get("name", f"Section_{node_id}"),
            "type": "CANVAS",
            "children": node_doc.get("children", [node_doc]),
        }
        # If the node itself is a FRAME/SECTION, wrap it in a canvas
        if node_doc.get("type") in ("FRAME", "SECTION", "COMPONENT_SET"):
            page["children"] = [node_doc]
        elif node_doc.get("type") == "CANVAS":
            page = node_doc

        pages.append(page)

    total_nodes = sum(count_nodes(p) for p in pages)

    result = {
        "document": {
            "id": "0:0",
            "name": kit_name,
            "type": "DOCUMENT",
            "children": pages,
        },
        "file_key": file_key,
        "total_nodes": total_nodes,
        "extracted_at": datetime.now().isoformat(),
        "extraction_mode": "targeted_nodes",
        "source_node_ids": list(all_nodes.keys()),
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False)

    final_mb = out_path.stat().st_size / 1024 / 1024
    print(f"\nSaved: {out_path}")
    print(f"Total nodes: {total_nodes}, Size: {final_mb:.1f} MB")
    print(f"Sections: {len(pages)}")
    for p in pages:
        print(f"  \"{p['name']}\" ({count_nodes(p)} nodes)")

    return True


def main():
    print(f"\n{'='*60}")
    print(f"TARGETED NODE EXTRACTOR")
    print(f"{'='*60}")

    # Parse command-line args or use defaults
    if len(sys.argv) >= 4:
        kit_name = sys.argv[1]
        file_key = sys.argv[2]
        node_ids = sys.argv[3:]
    else:
        # Default: Untitled UI Pro
        file_key = "xjdV652MDlXv5za86ou2wo"
        kit_name = "Untitled UI Pro"
        node_ids = [
            "925:34508",
            "1030:33572",
            "1238:52",
            "1686:419020",
            "6277:315325",
        ]

    print(f"Kit: {kit_name}")
    print(f"File: {file_key}")
    print(f"Nodes to fetch: {len(node_ids)}")
    print(f"{'='*60}\n")

    ok = fetch_nodes(file_key, node_ids, kit_name)

    if ok:
        print(f"\nPhase 1 done. Run Phase 2-5 via pipeline_batch.py")
        print(f"(Remove 'Untitled UI Pro' from failed_kits in checkpoint first)")
    else:
        print(f"\nFAILED")


if __name__ == "__main__":
    main()
