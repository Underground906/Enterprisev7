#!/usr/bin/env python3
"""
Enterprise_OS V7 — Figma Library Extractor

Extracts components from Figma files and builds a searchable library.
With retry logic, checkpointing, and error handling for large libraries.
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
OUTPUT_DIR = Path("figma_library")
THUMBNAILS_DIR = OUTPUT_DIR / "thumbnails"
DATA_DIR = OUTPUT_DIR / "data"
CHECKPOINT_FILE = OUTPUT_DIR / "checkpoint.json"

# Retry settings
MAX_RETRIES = 3
RETRY_DELAY = 5
REQUEST_TIMEOUT = 120


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


def get_file_structure(token: str, file_key: str) -> dict:
    """Get the full structure of a Figma file with retry logic."""
    url = f"{FIGMA_API_BASE}/files/{file_key}"
    headers = {"X-Figma-Token": token}

    for attempt in range(MAX_RETRIES):
        try:
            safe_print(f"[*] Fetching file: {file_key} (attempt {attempt + 1})")
            response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                safe_print(f"[!] File not found: {file_key}")
                return None
            elif response.status_code == 403:
                safe_print(f"[!] Access denied: {file_key}")
                return None
            else:
                safe_print(f"[!] Error {response.status_code}, retrying...")

        except requests.exceptions.Timeout:
            safe_print(f"[!] Timeout, retrying...")
        except requests.exceptions.RequestException as e:
            safe_print(f"[!] Connection error: {str(e)[:50]}, retrying...")

        if attempt < MAX_RETRIES - 1:
            time.sleep(RETRY_DELAY * (attempt + 1))

    safe_print(f"[!] Failed after {MAX_RETRIES} attempts: {file_key}")
    return None


def get_file_images(token: str, file_key: str, node_ids: list, scale: float = 0.5) -> dict:
    """Get thumbnail images for specific nodes."""
    if not node_ids:
        return {}

    all_images = {}
    batch_size = 50  # Smaller batches for stability

    for i in range(0, len(node_ids), batch_size):
        batch = node_ids[i:i + batch_size]
        ids_param = ",".join(batch)

        url = f"{FIGMA_API_BASE}/images/{file_key}"
        params = {"ids": ids_param, "scale": scale, "format": "png"}
        headers = {"X-Figma-Token": token}

        try:
            response = requests.get(url, headers=headers, params=params, timeout=60)
            if response.status_code == 200:
                data = response.json()
                if "images" in data:
                    all_images.update(data["images"])
        except Exception as e:
            safe_print(f"[!] Thumbnail batch failed: {str(e)[:30]}")

        time.sleep(0.5)

    return all_images


def extract_components(node: dict, parent_path: str = "", depth: int = 0, max_depth: int = 3) -> list:
    """Extract top-level components from a Figma node tree.

    Only extracts:
    - Depth 1-2: Page-level frames (full pages/screens)
    - Depth 2-3: Section-level blocks (headers, heroes, footers, etc.)
    - COMPONENT/COMPONENT_SET at any depth up to max_depth (actual reusable components)

    Skips deeply nested elements (individual buttons, icons, text layers).
    """
    components = []

    node_id = node.get("id", "")
    node_name = node.get("name", "Unnamed")
    node_type = node.get("type", "UNKNOWN")
    bounds = node.get("absoluteBoundingBox", {})
    width = bounds.get("width", 0)
    height = bounds.get("height", 0)

    current_path = f"{parent_path}/{node_name}" if parent_path else node_name

    # Skip if too deep (unless it's an actual component definition)
    if depth > max_depth and node_type not in ["COMPONENT", "COMPONENT_SET"]:
        return components

    # Skip tiny elements (icons, buttons, badges) - less than 100x100
    if width < 100 and height < 100 and depth > 2:
        return components

    # Determine if this is worth extracting
    is_page_level = depth <= 2 and node_type == "FRAME" and width >= 300
    is_section_block = depth <= 3 and node_type == "FRAME" and width >= 300 and height >= 100
    is_component_def = node_type in ["COMPONENT", "COMPONENT_SET"]

    if is_page_level or is_section_block or is_component_def:
        level = classify_level(node_type, node_name, depth)

        component = {
            "id": node_id,
            "name": node_name,
            "type": node_type,
            "path": current_path,
            "level": level,
            "width": width,
            "height": height,
            "depth": depth,
            "child_count": len(node.get("children", [])),
            "category": classify_category(node_name, current_path),
        }
        components.append(component)

    # Only recurse if we haven't hit max depth
    if depth < max_depth:
        for child in node.get("children", []):
            components.extend(extract_components(child, current_path, depth + 1, max_depth))

    return components


def classify_level(node_type: str, name: str, depth: int) -> str:
    """Classify component as page/block/component/atom."""
    name_lower = name.lower()

    if depth <= 2 and any(x in name_lower for x in ["page", "screen", "view", "dashboard", "home", "landing"]):
        return "page"
    if any(x in name_lower for x in ["section", "hero", "header", "footer", "nav", "sidebar", "card group"]):
        return "block"
    if any(x in name_lower for x in ["button", "input", "icon", "label", "badge", "avatar", "checkbox", "radio"]):
        return "atom"
    if node_type in ["COMPONENT", "COMPONENT_SET"]:
        return "component"
    if node_type == "FRAME" and depth <= 3:
        return "block"

    return "component"


def classify_category(name: str, path: str) -> str:
    """Classify component into functional category."""
    combined = (name + " " + path).lower()

    categories = {
        "navigation": ["nav", "menu", "header", "breadcrumb", "tab", "sidebar"],
        "hero": ["hero", "banner", "jumbotron"],
        "cards": ["card", "tile", "item"],
        "forms": ["form", "input", "field", "select", "checkbox", "radio", "button", "toggle"],
        "modals": ["modal", "dialog", "popup", "overlay", "drawer"],
        "tables": ["table", "list", "grid", "data"],
        "footer": ["footer"],
        "pricing": ["pricing", "plan", "tier"],
        "testimonials": ["testimonial", "review", "quote"],
        "features": ["feature", "benefit", "service"],
        "cta": ["cta", "call to action", "signup", "subscribe"],
        "auth": ["login", "signin", "signup", "register", "auth", "password"],
        "profile": ["profile", "account", "user", "avatar"],
        "dashboard": ["dashboard", "admin", "analytics", "stats", "metric"],
        "icons": ["icon", "glyph", "symbol"],
        "images": ["image", "photo", "illustration", "graphic"],
    }

    for category, keywords in categories.items():
        if any(kw in combined for kw in keywords):
            return category

    return "other"


def download_thumbnail(url: str, save_path: Path) -> bool:
    """Download a thumbnail image."""
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            save_path.parent.mkdir(parents=True, exist_ok=True)
            with open(save_path, "wb") as f:
                f.write(response.content)
            return True
    except Exception:
        pass
    return False


def process_file(token: str, file_key: str, download_thumbs: bool = False) -> dict:
    """Process a single Figma file."""
    file_data = get_file_structure(token, file_key)
    if not file_data:
        return None

    file_name = file_data.get("name", file_key)
    safe_print(f"[+] Processing: {file_name}")

    all_components = []
    document = file_data.get("document", {})

    for page in document.get("children", []):
        page_name = page.get("name", "Unnamed Page")
        safe_print(f"    Page: {page_name}")

        components = extract_components(page, page_name, depth=1)
        for comp in components:
            comp["file_key"] = file_key
            comp["file_name"] = file_name
            comp["page_name"] = page_name

        all_components.extend(components)

    safe_print(f"    Found {len(all_components)} components")

    # Get thumbnails for top-level items only
    if download_thumbs and all_components:
        thumb_nodes = [c["id"] for c in all_components if c["depth"] <= 3][:100]

        if thumb_nodes:
            safe_print(f"    Fetching {len(thumb_nodes)} thumbnails...")
            images = get_file_images(token, file_key, thumb_nodes)

            for comp in all_components:
                if comp["id"] in images and images[comp["id"]]:
                    comp["thumbnail_url"] = images[comp["id"]]

    return {
        "file_key": file_key,
        "file_name": file_name,
        "last_modified": file_data.get("lastModified"),
        "component_count": len(all_components),
        "components": all_components
    }


def save_results(results: list, output_name: str = "library"):
    """Save extraction results to JSON."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = DATA_DIR / f"{output_name}_{timestamp}.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    safe_print(f"\n[+] Saved to: {output_path}")
    return output_path


def generate_summary(results: list) -> dict:
    """Generate a summary of the extracted library."""
    summary = {
        "total_files": len(results),
        "total_components": sum(r["component_count"] for r in results if r),
        "by_level": {"page": 0, "block": 0, "component": 0, "atom": 0},
        "by_category": {},
        "files": []
    }

    for result in results:
        if not result:
            continue

        summary["files"].append({
            "name": result["file_name"],
            "key": result["file_key"],
            "components": result["component_count"]
        })

        for comp in result["components"]:
            level = comp.get("level", "component")
            summary["by_level"][level] = summary["by_level"].get(level, 0) + 1

            category = comp.get("category", "other")
            summary["by_category"][category] = summary["by_category"].get(category, 0) + 1

    return summary


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Extract Figma library components")
    parser.add_argument("--token", required=True, help="Figma personal access token")
    parser.add_argument("--file", help="Single Figma file key")
    parser.add_argument("--files", help="Text file with file keys (one per line)")
    parser.add_argument("--thumbnails", action="store_true", help="Download thumbnails")
    parser.add_argument("--output", default="library", help="Output name prefix")
    parser.add_argument("--resume", action="store_true", help="Resume from checkpoint")

    args = parser.parse_args()

    # Collect file keys
    file_keys = []

    if args.file:
        file_keys.append(args.file)

    if args.files:
        with open(args.files) as f:
            file_keys.extend(line.strip() for line in f if line.strip())

    if not file_keys:
        safe_print("[!] No file keys provided. Use --file or --files")
        sys.exit(1)

    # Load checkpoint if resuming
    checkpoint = load_checkpoint() if args.resume else {"processed": [], "results": []}

    # Filter out already processed files
    remaining = [k for k in file_keys if k not in checkpoint["processed"]]

    if args.resume and len(remaining) < len(file_keys):
        safe_print(f"[*] Resuming: {len(file_keys) - len(remaining)} already done, {len(remaining)} remaining")

    safe_print(f"[*] Processing {len(remaining)} file(s)...")

    results = checkpoint["results"]
    failed = []

    for i, file_key in enumerate(remaining):
        safe_print(f"\n[{i+1}/{len(remaining)}] ", end="")

        result = process_file(args.token, file_key, args.thumbnails)

        if result:
            results.append(result)
            checkpoint["processed"].append(file_key)
            checkpoint["results"] = results
            save_checkpoint(checkpoint)
        else:
            failed.append(file_key)
            checkpoint["processed"].append(file_key)  # Mark as attempted
            save_checkpoint(checkpoint)

        # Rate limiting
        time.sleep(1.5)

    # Save final results
    output_path = save_results(results, args.output)

    # Generate and print summary
    summary = generate_summary(results)

    safe_print("\n" + "=" * 50)
    safe_print("EXTRACTION SUMMARY")
    safe_print("=" * 50)
    safe_print(f"Files processed: {summary['total_files']}")
    safe_print(f"Files failed: {len(failed)}")
    safe_print(f"Total components: {summary['total_components']}")
    safe_print(f"\nBy Level:")
    for level, count in summary["by_level"].items():
        safe_print(f"  {level}: {count}")
    safe_print(f"\nBy Category (top 10):")
    for category, count in sorted(summary["by_category"].items(), key=lambda x: -x[1])[:10]:
        safe_print(f"  {category}: {count}")

    # Save summary
    summary_path = DATA_DIR / f"{args.output}_summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    safe_print(f"\n[+] Summary saved to: {summary_path}")

    if failed:
        failed_path = DATA_DIR / "failed_files.txt"
        with open(failed_path, "w") as f:
            f.write("\n".join(failed))
        safe_print(f"[!] Failed files saved to: {failed_path}")

    # Clean up checkpoint on success
    if not failed and CHECKPOINT_FILE.exists():
        CHECKPOINT_FILE.unlink()


if __name__ == "__main__":
    main()
