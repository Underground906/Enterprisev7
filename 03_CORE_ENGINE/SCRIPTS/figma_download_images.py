#!/usr/bin/env python3
"""
Enterprise_OS V7 - Figma Node Image Downloader

Downloads actual rendered images of each UI component using Figma's Images API.
Each node gets its own properly-rendered thumbnail.
"""

import json
import os
import sys
import time
import requests
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from urllib.parse import quote

# Configuration
FIGMA_API_BASE = "https://api.figma.com/v1"
INPUT_FILE = Path("figma_library_v2/ui_library_classified_20260207_201810.json")
OUTPUT_DIR = Path("figma_library_v2/thumbnails")
CHECKPOINT_FILE = Path("figma_library_v2/image_download_checkpoint.json")

# Image settings
IMAGE_SCALE = 1  # 1x for faster rendering (still good quality)
IMAGE_FORMAT = "png"
MAX_NODES_PER_REQUEST = 5  # Small batches to avoid render timeout

# Retry settings
MAX_RETRIES = 3
RETRY_DELAY = 2
REQUEST_TIMEOUT = 60


def safe_print(text: str):
    try:
        print(text, flush=True)
    except UnicodeEncodeError:
        print(text.encode('ascii', 'replace').decode('ascii'), flush=True)


def load_checkpoint():
    if CHECKPOINT_FILE.exists():
        with open(CHECKPOINT_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {"downloaded": [], "failed": []}


def save_checkpoint(checkpoint):
    with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False)


def get_node_images(token: str, file_key: str, node_ids: list) -> dict:
    """Get rendered images for multiple nodes in a file."""
    # URL-encode each node ID (colons become %3A)
    encoded_ids = [quote(nid, safe='') for nid in node_ids]
    ids_param = ",".join(encoded_ids)
    url = f"{FIGMA_API_BASE}/images/{file_key}?ids={ids_param}&scale={IMAGE_SCALE}&format={IMAGE_FORMAT}"
    headers = {"X-Figma-Token": token}

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
            if response.status_code == 200:
                data = response.json()
                if data.get("err"):
                    safe_print(f"    [!] API error: {data.get('err')}")
                    return {}
                return data.get("images", {})
            elif response.status_code == 404:
                safe_print(f"    [!] File not found: {file_key}")
                return {}
            elif response.status_code == 429:
                safe_print(f"    [!] Rate limited, waiting 30s...")
                time.sleep(30)
            elif response.status_code == 400:
                err_text = response.text[:200]
                if "timeout" in err_text.lower():
                    safe_print(f"    [!] Render timeout - trying one at a time")
                    return "TIMEOUT"  # Signal to retry one-by-one
                safe_print(f"    [!] Error 400: {err_text}")
                return {}
            else:
                safe_print(f"    [!] Error {response.status_code}, retrying...")
        except requests.exceptions.RequestException as e:
            safe_print(f"    [!] Connection error: {str(e)[:50]}")

        if attempt < MAX_RETRIES - 1:
            time.sleep(RETRY_DELAY * (attempt + 1))

    return {}


def download_image(url: str, output_path: Path) -> bool:
    """Download an image from URL to local file."""
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(response.content)
            return True
    except Exception as e:
        safe_print(f"    [!] Download failed: {str(e)[:50]}")
    return False


def sanitize_filename(name: str) -> str:
    """Create a safe filename from node name."""
    # Replace problematic characters
    for char in ['/', '\\', ':', '*', '?', '"', '<', '>', '|']:
        name = name.replace(char, '_')
    # Limit length
    return name[:50]


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Download Figma node images")
    parser.add_argument("--token", required=True, help="Figma personal access token")
    parser.add_argument("--input", default=str(INPUT_FILE), help="Input JSON file")
    parser.add_argument("--limit", type=int, default=0, help="Limit files to process (0=all)")
    parser.add_argument("--resume", action="store_true", help="Resume from checkpoint")
    parser.add_argument("--category", help="Only process specific category")
    parser.add_argument("--level", help="Only process specific level (page/block/component/atom)")

    args = parser.parse_args()

    # Load items
    safe_print(f"[*] Loading {args.input}...")
    with open(args.input, encoding="utf-8") as f:
        items = json.load(f)
    safe_print(f"[*] Loaded {len(items)} items")

    # Filter by category/level if specified
    if args.category:
        items = [i for i in items if i["category"] == args.category]
        safe_print(f"[*] Filtered to {len(items)} items in category '{args.category}'")

    if args.level:
        items = [i for i in items if i["level"] == args.level]
        safe_print(f"[*] Filtered to {len(items)} items at level '{args.level}'")

    # Group items by file_key for batch processing
    by_file = defaultdict(list)
    for item in items:
        by_file[item["file_key"]].append(item)

    safe_print(f"[*] Processing {len(by_file)} Figma files")

    # Load checkpoint
    checkpoint = load_checkpoint() if args.resume else {"downloaded": [], "failed": []}
    downloaded_ids = set(checkpoint["downloaded"])

    # Filter out already downloaded
    for file_key in by_file:
        by_file[file_key] = [i for i in by_file[file_key] if i["id"] not in downloaded_ids]

    total_remaining = sum(len(nodes) for nodes in by_file.values())
    safe_print(f"[*] {len(downloaded_ids)} already downloaded, {total_remaining} remaining")

    if total_remaining == 0:
        safe_print("[+] All images already downloaded!")
        return

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Process files
    file_keys = list(by_file.keys())
    if args.limit > 0:
        file_keys = file_keys[:args.limit]

    total_downloaded = 0
    total_failed = 0

    for i, file_key in enumerate(file_keys):
        nodes = by_file[file_key]
        if not nodes:
            continue

        file_name = nodes[0].get("file_name", file_key)
        safe_print(f"\n[{i+1}/{len(file_keys)}] {file_name[:40]}... ({len(nodes)} nodes)")

        # Process in batches
        for batch_start in range(0, len(nodes), MAX_NODES_PER_REQUEST):
            batch = nodes[batch_start:batch_start + MAX_NODES_PER_REQUEST]
            node_ids = [n["id"] for n in batch]

            safe_print(f"  Fetching {len(batch)} images...")
            images = get_node_images(args.token, file_key, node_ids)

            # Handle render timeout - retry one at a time
            if images == "TIMEOUT":
                safe_print(f"  Retrying {len(batch)} images one-by-one...")
                images = {}
                for node in batch:
                    single_result = get_node_images(args.token, file_key, [node["id"]])
                    if single_result and single_result != "TIMEOUT":
                        images.update(single_result)
                    time.sleep(0.5)

            if not images:
                safe_print(f"  [!] Failed to get images for batch")
                for node in batch:
                    checkpoint["failed"].append(node["id"])
                    total_failed += 1
                save_checkpoint(checkpoint)
                continue

            # Download each image
            for node in batch:
                node_id = node["id"]
                image_url = images.get(node_id)

                if not image_url:
                    checkpoint["failed"].append(node_id)
                    total_failed += 1
                    continue

                # Create filename: category/file_key/node_id.png
                safe_name = sanitize_filename(node["name"])
                output_path = OUTPUT_DIR / node["category"] / file_key / f"{node_id.replace(':', '_')}_{safe_name}.png"

                if download_image(image_url, output_path):
                    checkpoint["downloaded"].append(node_id)
                    total_downloaded += 1
                else:
                    checkpoint["failed"].append(node_id)
                    total_failed += 1

            save_checkpoint(checkpoint)

            # Progress
            if total_downloaded % 50 == 0:
                safe_print(f"  Progress: {total_downloaded} downloaded, {total_failed} failed")

            time.sleep(0.5)  # Rate limiting

        time.sleep(1)  # Between files

    # Final summary
    safe_print("\n" + "=" * 50)
    safe_print("DOWNLOAD COMPLETE")
    safe_print("=" * 50)
    safe_print(f"Downloaded: {total_downloaded}")
    safe_print(f"Failed: {total_failed}")
    safe_print(f"Total in checkpoint: {len(checkpoint['downloaded'])}")
    safe_print(f"Output directory: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
