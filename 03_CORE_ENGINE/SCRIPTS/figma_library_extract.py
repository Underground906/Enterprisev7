#!/usr/bin/env python3
"""
Enterprise_OS V7 - Figma Library Extractor (Smart)

Extracts meaningful UI library items:
- Pages: Full page designs (large frames on canvas)
- Blocks: Section-level components (headers, heroes, footers)
- Components: Actual reusable components (COMPONENT/COMPONENT_SET)
- Atoms: Small reusable elements (buttons, inputs)

Does NOT deeply recurse into nested internal parts.
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
OUTPUT_DIR = Path("figma_library_v2")
CHECKPOINT_FILE = OUTPUT_DIR / "checkpoint.json"

# Retry settings
MAX_RETRIES = 3
RETRY_DELAY = 5
REQUEST_TIMEOUT = 120


def safe_print(text: str, end="\n"):
    """Print text safely on Windows."""
    try:
        print(text, end=end, flush=True)
    except UnicodeEncodeError:
        print(text.encode('ascii', 'replace').decode('ascii'), end=end, flush=True)


def load_checkpoint():
    if CHECKPOINT_FILE.exists():
        with open(CHECKPOINT_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {"processed": [], "items": []}


def save_checkpoint(checkpoint):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False)


def get_file_with_depth(token: str, file_key: str, depth: int = 2) -> dict:
    """Get Figma file with specified depth."""
    url = f"{FIGMA_API_BASE}/files/{file_key}?depth={depth}"
    headers = {"X-Figma-Token": token}

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
            if response.status_code == 200:
                return response.json()
            elif response.status_code in [404, 403]:
                return None
            else:
                safe_print(f"    [!] Error {response.status_code}, retrying...")
        except requests.exceptions.RequestException as e:
            safe_print(f"    [!] Connection error, retrying...")

        if attempt < MAX_RETRIES - 1:
            time.sleep(RETRY_DELAY * (attempt + 1))

    return None


def classify_item(node: dict, page_name: str) -> dict:
    """Classify a canvas item into page/block/component/atom."""
    node_type = node.get("type", "")
    name = node.get("name", "Unnamed")
    bounds = node.get("absoluteBoundingBox", {})
    width = bounds.get("width", 0)
    height = bounds.get("height", 0)

    name_lower = name.lower()

    # Determine level
    level = "other"

    # Full page designs (large frames)
    if node_type == "FRAME" and width >= 1200:
        if any(kw in name_lower for kw in ["page", "screen", "view", "home", "landing", "dashboard", "login", "signup", "profile", "settings", "checkout", "detail"]):
            level = "page"
        elif height >= 800:  # Tall enough to be a full page
            level = "page"
        else:
            level = "block"

    # Blocks/Sections
    elif node_type == "FRAME" and width >= 300:
        if any(kw in name_lower for kw in ["header", "hero", "footer", "nav", "sidebar", "section", "banner", "cta", "feature", "pricing", "testimonial", "faq", "contact", "about", "team"]):
            level = "block"
        elif height >= 200 and width >= 800:
            level = "block"
        else:
            level = "component"

    # Actual components
    elif node_type in ["COMPONENT", "COMPONENT_SET"]:
        if width < 100 and height < 100:
            level = "atom"
        elif any(kw in name_lower for kw in ["button", "btn", "input", "icon", "badge", "tag", "chip", "avatar", "checkbox", "radio", "toggle", "switch"]):
            level = "atom"
        else:
            level = "component"

    # Small frames that are atoms
    elif node_type == "FRAME" and width < 200 and height < 200:
        if any(kw in name_lower for kw in ["button", "btn", "input", "icon", "badge", "avatar"]):
            level = "atom"
        else:
            level = "component"

    # Classify category
    category = classify_category(name, page_name)

    return {
        "level": level,
        "category": category
    }


def classify_category(name: str, page_name: str) -> str:
    """Classify into functional category."""
    combined = (name + " " + page_name).lower()

    categories = {
        "navigation": ["nav", "menu", "header", "breadcrumb", "tab", "sidebar", "topbar"],
        "hero": ["hero", "banner", "jumbotron", "intro"],
        "cards": ["card", "tile", "item", "grid item"],
        "forms": ["form", "input", "field", "select", "checkbox", "radio", "button", "toggle", "search"],
        "modals": ["modal", "dialog", "popup", "overlay", "drawer", "sheet"],
        "tables": ["table", "list", "data table", "grid"],
        "footer": ["footer"],
        "pricing": ["pricing", "plan", "tier", "subscription"],
        "testimonials": ["testimonial", "review", "quote", "feedback"],
        "features": ["feature", "benefit", "service", "capability"],
        "cta": ["cta", "call to action", "signup", "subscribe", "newsletter"],
        "auth": ["login", "signin", "signup", "register", "auth", "password", "forgot"],
        "profile": ["profile", "account", "user", "avatar", "settings"],
        "dashboard": ["dashboard", "admin", "analytics", "stats", "metric", "chart", "graph"],
        "ecommerce": ["product", "cart", "checkout", "shop", "store", "payment"],
        "content": ["blog", "article", "post", "news", "content"],
        "media": ["image", "video", "gallery", "carousel", "slider"],
        "icons": ["icon", "glyph", "symbol"],
        "empty": ["empty", "no data", "placeholder", "skeleton"],
    }

    for category, keywords in categories.items():
        if any(kw in combined for kw in keywords):
            return category

    return "other"


def extract_canvas_items(file_data: dict, file_key: str, file_info: dict = None) -> list:
    """Extract meaningful items from a Figma file."""
    items = []
    file_name = file_data.get("name", file_key)
    document = file_data.get("document", {})

    for page in document.get("children", []):
        page_name = page.get("name", "Unnamed")
        page_id = page.get("id", "")

        # Skip utility pages
        if any(x in page_name.lower() for x in ["cover", "thumbnail", "---", "license", "archive", "deprecated"]):
            continue

        # Get all top-level frames on this page
        for node in page.get("children", []):
            node_type = node.get("type", "")

            # Only process frames and components
            if node_type not in ["FRAME", "COMPONENT", "COMPONENT_SET", "INSTANCE"]:
                continue

            node_id = node.get("id", "")
            node_name = node.get("name", "Unnamed")
            bounds = node.get("absoluteBoundingBox", {})

            # Skip tiny items (icons, spacers, etc.)
            width = bounds.get("width", 0)
            height = bounds.get("height", 0)
            if width < 50 or height < 50:
                continue

            # Classify the item
            classification = classify_item(node, page_name)

            # Skip "other" items unless they're components
            if classification["level"] == "other" and node_type not in ["COMPONENT", "COMPONENT_SET"]:
                continue

            item = {
                "id": node_id,
                "name": node_name,
                "type": node_type,
                "level": classification["level"],
                "category": classification["category"],
                "width": int(width),
                "height": int(height),
                "page_name": page_name,
                "page_id": page_id,
                "file_key": file_key,
                "file_name": file_name,
                "figma_url": f"https://www.figma.com/file/{file_key}?node-id={node_id}",
            }

            # Add file info if available
            if file_info:
                item["project_name"] = file_info.get("project_name", "")
                item["thumbnail_url"] = file_info.get("thumbnail_url", "")

            items.append(item)

    return items


def process_file(token: str, file_key: str, file_info: dict = None) -> list:
    """Process a single Figma file."""
    file_data = get_file_with_depth(token, file_key, depth=2)
    if not file_data:
        return []

    file_name = file_data.get("name", file_key)
    items = extract_canvas_items(file_data, file_key, file_info)

    # Count by level
    levels = {}
    for item in items:
        lvl = item["level"]
        levels[lvl] = levels.get(lvl, 0) + 1

    level_str = ", ".join(f"{k}:{v}" for k, v in sorted(levels.items()))
    safe_print(f"  [+] {file_name}: {len(items)} items ({level_str})")

    return items


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Extract Figma UI library")
    parser.add_argument("--token", required=True, help="Figma personal access token")
    parser.add_argument("--files", help="JSON file with file info")
    parser.add_argument("--keys", help="Text file with file keys")
    parser.add_argument("--output", default="library", help="Output name prefix")
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
    checkpoint = load_checkpoint() if args.resume else {"processed": [], "items": []}

    # Filter already processed
    remaining = [k for k in files_to_process if k not in checkpoint["processed"]]

    if args.resume and len(remaining) < len(files_to_process):
        safe_print(f"[*] Resuming: {len(files_to_process) - len(remaining)} done, {len(remaining)} remaining")

    safe_print(f"[*] Processing {len(remaining)} files...")

    all_items = checkpoint["items"]
    failed = []

    for i, file_key in enumerate(remaining):
        safe_print(f"\n[{i+1}/{len(remaining)}] {file_key[:20]}...")

        info = file_info.get(file_key, {})
        items = process_file(args.token, file_key, info)

        if items:
            all_items.extend(items)
        else:
            failed.append(file_key)

        checkpoint["processed"].append(file_key)
        checkpoint["items"] = all_items
        save_checkpoint(checkpoint)

        time.sleep(1)  # Rate limiting

    # Save final library
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    library_path = OUTPUT_DIR / f"{args.output}_{timestamp}.json"
    with open(library_path, "w", encoding="utf-8") as f:
        json.dump(all_items, f, indent=2, ensure_ascii=False)

    # Generate summary
    levels = {}
    categories = {}
    for item in all_items:
        lvl = item["level"]
        cat = item["category"]
        levels[lvl] = levels.get(lvl, 0) + 1
        categories[cat] = categories.get(cat, 0) + 1

    summary = {
        "total_items": len(all_items),
        "total_files": len(files_to_process) - len(failed),
        "failed_files": len(failed),
        "by_level": dict(sorted(levels.items(), key=lambda x: -x[1])),
        "by_category": dict(sorted(categories.items(), key=lambda x: -x[1])),
        "generated": datetime.now().isoformat(),
    }

    summary_path = OUTPUT_DIR / f"{args.output}_summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    safe_print("\n" + "=" * 50)
    safe_print("EXTRACTION COMPLETE")
    safe_print("=" * 50)
    safe_print(f"Total items: {len(all_items)}")
    safe_print(f"Files processed: {len(files_to_process) - len(failed)}")
    safe_print(f"Failed: {len(failed)}")
    safe_print(f"\nBy Level:")
    for lvl, count in sorted(levels.items(), key=lambda x: -x[1]):
        safe_print(f"  {lvl}: {count}")
    safe_print(f"\nBy Category (top 15):")
    for cat, count in sorted(categories.items(), key=lambda x: -x[1])[:15]:
        safe_print(f"  {cat}: {count}")
    safe_print(f"\nSaved to: {library_path}")

    if failed:
        failed_path = OUTPUT_DIR / "failed_files.txt"
        with open(failed_path, "w") as f:
            f.write("\n".join(failed))

    # Clean checkpoint on success
    if not failed and CHECKPOINT_FILE.exists():
        CHECKPOINT_FILE.unlink()


if __name__ == "__main__":
    main()
