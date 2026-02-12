#!/usr/bin/env python3
"""
Enterprise_OS V7 - Figma Library Catalog

Creates a lightweight catalog of Figma files and their pages.
Does NOT extract individual components - just file/page metadata.

Output: ~5,000 searchable items instead of millions.
"""

import os
import sys
import json
import requests
import time
from pathlib import Path
from datetime import datetime

# Configuration
FIGMA_API_BASE = "https://api.figma.com/v1"
OUTPUT_DIR = Path("figma_catalog")
CHECKPOINT_FILE = OUTPUT_DIR / "checkpoint.json"

# Retry settings
MAX_RETRIES = 3
RETRY_DELAY = 5
REQUEST_TIMEOUT = 60


def safe_print(text: str, end="\n"):
    """Print text safely on Windows."""
    try:
        print(text, end=end)
    except UnicodeEncodeError:
        print(text.encode('ascii', 'replace').decode('ascii'), end=end)


def load_checkpoint():
    """Load checkpoint to resume from where we left off."""
    if CHECKPOINT_FILE.exists():
        with open(CHECKPOINT_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {"processed": [], "results": []}


def save_checkpoint(checkpoint):
    """Save checkpoint for resume capability."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False)


def get_file_metadata(token: str, file_key: str) -> dict:
    """Get just the metadata and page names from a Figma file."""
    url = f"{FIGMA_API_BASE}/files/{file_key}?depth=1"  # Only get one level deep
    headers = {"X-Figma-Token": token}

    for attempt in range(MAX_RETRIES):
        try:
            safe_print(f"  Fetching: {file_key} (attempt {attempt + 1})")
            response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                safe_print(f"  [!] File not found: {file_key}")
                return None
            elif response.status_code == 403:
                safe_print(f"  [!] Access denied: {file_key}")
                return None
            else:
                safe_print(f"  [!] Error {response.status_code}, retrying...")

        except requests.exceptions.Timeout:
            safe_print(f"  [!] Timeout, retrying...")
        except requests.exceptions.RequestException as e:
            safe_print(f"  [!] Connection error, retrying...")

        if attempt < MAX_RETRIES - 1:
            time.sleep(RETRY_DELAY * (attempt + 1))

    safe_print(f"  [!] Failed after {MAX_RETRIES} attempts")
    return None


def classify_file(file_name: str, pages: list) -> list:
    """Classify file into categories based on name and page names."""
    combined = file_name.lower()
    for page in pages:
        combined += " " + page.get("name", "").lower()

    categories = []

    # UI Kit types
    if any(kw in combined for kw in ["dashboard", "admin", "analytics"]):
        categories.append("dashboard")
    if any(kw in combined for kw in ["landing", "marketing", "website"]):
        categories.append("marketing")
    if any(kw in combined for kw in ["mobile", "app", "ios", "android"]):
        categories.append("mobile")
    if any(kw in combined for kw in ["saas", "webapp", "application"]):
        categories.append("saas")
    if any(kw in combined for kw in ["ecommerce", "shop", "store", "product"]):
        categories.append("ecommerce")
    if any(kw in combined for kw in ["ai", "chatbot", "gpt", "assistant"]):
        categories.append("ai")
    if any(kw in combined for kw in ["finance", "banking", "crypto", "wallet"]):
        categories.append("finance")
    if any(kw in combined for kw in ["health", "fitness", "medical"]):
        categories.append("health")
    if any(kw in combined for kw in ["education", "learning", "course"]):
        categories.append("education")
    if any(kw in combined for kw in ["social", "community", "chat"]):
        categories.append("social")

    # Component types (from page names)
    if any(kw in combined for kw in ["component", "ui kit", "design system"]):
        categories.append("component-library")
    if any(kw in combined for kw in ["icon", "glyph"]):
        categories.append("icons")
    if any(kw in combined for kw in ["style", "guide", "brand"]):
        categories.append("styleguide")

    if not categories:
        categories.append("general")

    return categories


def process_file(token: str, file_key: str, existing_info: dict = None) -> dict:
    """Process a single Figma file - extract metadata and pages only."""

    file_data = get_file_metadata(token, file_key)
    if not file_data:
        return None

    file_name = file_data.get("name", file_key)
    document = file_data.get("document", {})
    pages = document.get("children", [])

    # Extract page info
    page_list = []
    for page in pages:
        page_name = page.get("name", "Unnamed")
        # Skip utility pages
        if any(x in page_name.lower() for x in ["cover", "thumbnail", "---", "license", "archive"]):
            continue
        page_list.append({
            "id": page.get("id"),
            "name": page_name,
        })

    categories = classify_file(file_name, pages)

    result = {
        "file_key": file_key,
        "file_name": file_name,
        "figma_url": f"https://www.figma.com/file/{file_key}",
        "last_modified": file_data.get("lastModified"),
        "categories": categories,
        "page_count": len(page_list),
        "pages": page_list,
    }

    # Merge with existing info if provided (project, thumbnail)
    if existing_info:
        result["project_name"] = existing_info.get("project_name", "")
        result["thumbnail_url"] = existing_info.get("thumbnail_url", "")

    safe_print(f"  [+] {file_name}: {len(page_list)} pages, categories: {categories}")
    return result


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Create Figma library catalog")
    parser.add_argument("--token", required=True, help="Figma personal access token")
    parser.add_argument("--files", help="JSON file with file info (from figma_list_files.py)")
    parser.add_argument("--keys", help="Text file with file keys (one per line)")
    parser.add_argument("--output", default="catalog", help="Output name prefix")
    parser.add_argument("--resume", action="store_true", help="Resume from checkpoint")

    args = parser.parse_args()

    # Load file info
    file_info = {}
    files_to_process = []

    if args.files:
        with open(args.files, encoding="utf-8") as f:
            data = json.load(f)
            for item in data:
                key = item.get("file_key")
                if key:
                    file_info[key] = item
                    files_to_process.append(key)
    elif args.keys:
        with open(args.keys) as f:
            files_to_process = [line.strip() for line in f if line.strip()]
    else:
        safe_print("[!] Provide --files (JSON) or --keys (text file)")
        sys.exit(1)

    # Load checkpoint
    checkpoint = load_checkpoint() if args.resume else {"processed": [], "results": []}

    # Filter already processed
    remaining = [k for k in files_to_process if k not in checkpoint["processed"]]

    if args.resume and len(remaining) < len(files_to_process):
        safe_print(f"[*] Resuming: {len(files_to_process) - len(remaining)} done, {len(remaining)} remaining")

    safe_print(f"[*] Processing {len(remaining)} files...")

    results = checkpoint["results"]
    failed = []

    for i, file_key in enumerate(remaining):
        safe_print(f"\n[{i+1}/{len(remaining)}]")

        existing = file_info.get(file_key, {})
        result = process_file(args.token, file_key, existing)

        if result:
            results.append(result)
        else:
            failed.append(file_key)

        checkpoint["processed"].append(file_key)
        checkpoint["results"] = results
        save_checkpoint(checkpoint)

        time.sleep(1)  # Rate limiting

    # Save final catalog
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    catalog_path = OUTPUT_DIR / f"{args.output}_{timestamp}.json"
    with open(catalog_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    # Generate summary
    total_pages = sum(r["page_count"] for r in results)
    categories = {}
    for r in results:
        for cat in r["categories"]:
            categories[cat] = categories.get(cat, 0) + 1

    summary = {
        "total_files": len(results),
        "total_pages": total_pages,
        "failed_files": len(failed),
        "by_category": dict(sorted(categories.items(), key=lambda x: -x[1])),
        "generated": datetime.now().isoformat(),
    }

    summary_path = OUTPUT_DIR / f"{args.output}_summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    safe_print("\n" + "=" * 50)
    safe_print("CATALOG COMPLETE")
    safe_print("=" * 50)
    safe_print(f"Files cataloged: {len(results)}")
    safe_print(f"Total pages: {total_pages}")
    safe_print(f"Failed: {len(failed)}")
    safe_print(f"\nBy Category:")
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        safe_print(f"  {cat}: {count}")
    safe_print(f"\nSaved to: {catalog_path}")
    safe_print(f"Summary: {summary_path}")

    if failed:
        failed_path = OUTPUT_DIR / "failed_files.txt"
        with open(failed_path, "w") as f:
            f.write("\n".join(failed))
        safe_print(f"Failed files: {failed_path}")

    # Clean checkpoint on success
    if not failed and CHECKPOINT_FILE.exists():
        CHECKPOINT_FILE.unlink()


if __name__ == "__main__":
    main()
