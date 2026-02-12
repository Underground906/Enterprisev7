#!/usr/bin/env python3
"""
Enterprise_OS V7 - Figma Library Classifier

Enriches extracted library with:
1. device_type (from dimensions)
2. industry_vertical (from file/project names)
3. Better functional_category (LLM classification for "other" items)
"""

import json
import os
import sys
import time
import re
from pathlib import Path
from datetime import datetime

# Try to import anthropic for LLM classification
try:
    import anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False
    print("[!] anthropic not installed. Run: pip install anthropic")

INPUT_FILE = Path("figma_library_v2/ui_library_20260207_191656.json")
OUTPUT_DIR = Path("figma_library_v2")
CHECKPOINT_FILE = OUTPUT_DIR / "classify_checkpoint.json"

# Industry vertical patterns
INDUSTRY_PATTERNS = {
    "saas": ["saas", "dashboard", "admin", "analytics", "crm", "erp", "management", "platform"],
    "ecommerce": ["ecommerce", "e-commerce", "shop", "store", "product", "cart", "checkout", "retail", "fashion"],
    "finance": ["finance", "fintech", "banking", "payment", "wallet", "crypto", "trading", "money", "invest"],
    "healthcare": ["health", "medical", "clinic", "hospital", "doctor", "patient", "wellness", "care"],
    "education": ["education", "learning", "course", "school", "university", "training", "study", "e-learning"],
    "real_estate": ["real estate", "property", "house", "home", "apartment", "realty", "listing"],
    "travel": ["travel", "booking", "hotel", "flight", "trip", "vacation", "tourism", "destination"],
    "food": ["food", "restaurant", "delivery", "menu", "recipe", "cafe", "dining", "grocery"],
    "fitness": ["fitness", "gym", "workout", "exercise", "health", "sport", "training"],
    "entertainment": ["entertainment", "streaming", "movie", "video", "music", "gaming", "media"],
    "professional": ["agency", "portfolio", "consulting", "business", "corporate", "service"],
    "marketplace": ["marketplace", "listing", "buy", "sell", "auction", "classifieds"],
    "social": ["social", "community", "chat", "messaging", "network", "forum", "feed"],
    "ai": ["ai", "artificial intelligence", "chatbot", "gpt", "assistant", "machine learning"],
}

# Functional category patterns for reclassification
CATEGORY_PATTERNS = {
    "navigation": ["nav", "menu", "header", "sidebar", "topbar", "breadcrumb", "tab", "navbar"],
    "hero": ["hero", "banner", "intro", "landing", "jumbotron", "welcome"],
    "cta": ["cta", "call to action", "subscribe", "signup", "newsletter", "get started"],
    "cards": ["card", "tile", "grid item", "list item"],
    "forms": ["form", "input", "field", "search", "filter", "login", "register", "contact"],
    "tables": ["table", "list", "data grid", "records"],
    "modals": ["modal", "dialog", "popup", "overlay", "drawer", "sheet", "toast"],
    "footer": ["footer", "bottom"],
    "pricing": ["pricing", "plan", "subscription", "tier", "package"],
    "testimonials": ["testimonial", "review", "feedback", "quote", "rating"],
    "features": ["feature", "benefit", "service", "capability", "highlight"],
    "auth": ["login", "signin", "signup", "register", "password", "forgot", "auth", "verification"],
    "profile": ["profile", "account", "user", "settings", "preferences", "avatar"],
    "dashboard": ["dashboard", "analytics", "stats", "metrics", "chart", "graph", "report"],
    "ecommerce": ["product", "cart", "checkout", "order", "shop", "catalog"],
    "content": ["blog", "article", "post", "news", "content", "text"],
    "media": ["image", "video", "gallery", "carousel", "slider", "photo"],
    "icons": ["icon", "glyph", "symbol", "pictogram"],
    "empty": ["empty", "no data", "placeholder", "skeleton", "loading"],
}


def safe_print(text: str):
    try:
        print(text, flush=True)
    except UnicodeEncodeError:
        print(text.encode('ascii', 'replace').decode('ascii'), flush=True)


def load_checkpoint():
    if CHECKPOINT_FILE.exists():
        with open(CHECKPOINT_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {"classified_ids": [], "results": {}}


def save_checkpoint(checkpoint):
    with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False)


def get_device_type(width: int) -> str:
    """Infer device type from width."""
    if width >= 1200:
        return "desktop"
    elif width >= 768:
        return "tablet"
    else:
        return "mobile"


def get_industry_vertical(file_name: str, project_name: str, item_name: str) -> str:
    """Infer industry vertical from names."""
    combined = f"{file_name} {project_name} {item_name}".lower()

    for industry, patterns in INDUSTRY_PATTERNS.items():
        if any(p in combined for p in patterns):
            return industry

    return "general"


def reclassify_category(name: str, page_name: str, current_category: str) -> str:
    """Try to reclassify 'other' items based on name patterns."""
    if current_category != "other":
        return current_category

    combined = f"{name} {page_name}".lower()

    for category, patterns in CATEGORY_PATTERNS.items():
        if any(p in combined for p in patterns):
            return category

    return "other"


def classify_with_llm(client, items_batch: list) -> dict:
    """Use Claude to classify items that couldn't be pattern-matched."""

    # Build prompt with batch of items
    items_text = ""
    for item in items_batch:
        items_text += f"""
ID: {item['id']}
Name: {item['name']}
File: {item['file_name']}
Page: {item['page_name']}
Size: {item['width']}x{item['height']}
Current Category: {item['category']}
---
"""

    prompt = f"""Classify these UI components into functional categories.

For each item, respond with ONLY a JSON object mapping ID to category.
Categories: navigation, hero, cta, cards, forms, tables, modals, footer, pricing, testimonials, features, auth, profile, dashboard, ecommerce, content, media, icons, empty, other

Items to classify:
{items_text}

Respond with ONLY valid JSON like: {{"id1": "category1", "id2": "category2"}}"""

    try:
        response = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )

        # Extract JSON from response
        text = response.content[0].text.strip()
        # Find JSON in response
        match = re.search(r'\{[^}]+\}', text, re.DOTALL)
        if match:
            return json.loads(match.group())
    except Exception as e:
        safe_print(f"  [!] LLM error: {str(e)[:50]}")

    return {}


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Classify Figma library items")
    parser.add_argument("--input", default=str(INPUT_FILE), help="Input JSON file")
    parser.add_argument("--llm", action="store_true", help="Use LLM for 'other' items")
    parser.add_argument("--batch-size", type=int, default=20, help="LLM batch size")
    parser.add_argument("--limit", type=int, default=0, help="Limit LLM calls (0=all)")

    args = parser.parse_args()

    # Load data
    safe_print(f"[*] Loading {args.input}...")
    with open(args.input, encoding="utf-8") as f:
        items = json.load(f)

    safe_print(f"[*] Loaded {len(items)} items")

    # PASS 1: Add device_type and industry_vertical (no API needed)
    safe_print("\n[PASS 1] Adding device_type and industry_vertical...")

    for item in items:
        item["device_type"] = get_device_type(item["width"])
        item["industry_vertical"] = get_industry_vertical(
            item["file_name"],
            item.get("project_name", ""),
            item["name"]
        )

    # Count device types
    devices = {}
    for item in items:
        d = item["device_type"]
        devices[d] = devices.get(d, 0) + 1
    safe_print(f"  Device types: {devices}")

    # Count industries
    industries = {}
    for item in items:
        ind = item["industry_vertical"]
        industries[ind] = industries.get(ind, 0) + 1
    safe_print(f"  Industries: {dict(sorted(industries.items(), key=lambda x: -x[1]))}")

    # PASS 2: Reclassify 'other' items with pattern matching
    safe_print("\n[PASS 2] Reclassifying 'other' items with patterns...")

    other_before = sum(1 for i in items if i["category"] == "other")

    for item in items:
        item["category"] = reclassify_category(
            item["name"],
            item["page_name"],
            item["category"]
        )

    other_after = sum(1 for i in items if i["category"] == "other")
    safe_print(f"  Reduced 'other' from {other_before} to {other_after} ({other_before - other_after} reclassified)")

    # Count categories after pattern matching
    cats = {}
    for item in items:
        c = item["category"]
        cats[c] = cats.get(c, 0) + 1
    safe_print(f"  Categories: {dict(sorted(cats.items(), key=lambda x: -x[1]))}")

    # PASS 3: LLM classification for remaining 'other' items
    if args.llm and HAS_ANTHROPIC:
        safe_print("\n[PASS 3] LLM classification for remaining 'other' items...")

        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            safe_print("[!] ANTHROPIC_API_KEY not set. Skipping LLM pass.")
        else:
            client = anthropic.Anthropic(api_key=api_key)

            # Get items still categorized as 'other'
            other_items = [i for i in items if i["category"] == "other"]

            if args.limit > 0:
                other_items = other_items[:args.limit * args.batch_size]

            safe_print(f"  Processing {len(other_items)} items in batches of {args.batch_size}...")

            # Load checkpoint
            checkpoint = load_checkpoint()

            # Process in batches
            classified = 0
            for i in range(0, len(other_items), args.batch_size):
                batch = other_items[i:i + args.batch_size]

                # Skip already classified
                batch = [item for item in batch if item["id"] not in checkpoint["classified_ids"]]
                if not batch:
                    continue

                safe_print(f"  Batch {i // args.batch_size + 1}: classifying {len(batch)} items...")

                results = classify_with_llm(client, batch)

                for item in batch:
                    if item["id"] in results:
                        new_cat = results[item["id"]]
                        if new_cat in CATEGORY_PATTERNS or new_cat == "other":
                            item["category"] = new_cat
                            classified += 1
                    checkpoint["classified_ids"].append(item["id"])

                checkpoint["results"].update(results)
                save_checkpoint(checkpoint)

                time.sleep(0.5)  # Rate limiting

            safe_print(f"  LLM classified {classified} items")

            # Update main items list with LLM results
            id_to_item = {i["id"]: i for i in items}
            for item_id, category in checkpoint["results"].items():
                if item_id in id_to_item:
                    id_to_item[item_id]["category"] = category

    # Final counts
    safe_print("\n[FINAL] Category distribution:")
    cats = {}
    for item in items:
        c = item["category"]
        cats[c] = cats.get(c, 0) + 1
    for c, n in sorted(cats.items(), key=lambda x: -x[1]):
        safe_print(f"  {c}: {n}")

    # Save enriched data
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = OUTPUT_DIR / f"ui_library_classified_{timestamp}.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)

    safe_print(f"\n[+] Saved to: {output_path}")

    # Also save summary
    summary = {
        "total_items": len(items),
        "by_level": {},
        "by_category": {},
        "by_device": {},
        "by_industry": {},
        "generated": datetime.now().isoformat(),
    }

    for item in items:
        summary["by_level"][item["level"]] = summary["by_level"].get(item["level"], 0) + 1
        summary["by_category"][item["category"]] = summary["by_category"].get(item["category"], 0) + 1
        summary["by_device"][item["device_type"]] = summary["by_device"].get(item["device_type"], 0) + 1
        summary["by_industry"][item["industry_vertical"]] = summary["by_industry"].get(item["industry_vertical"], 0) + 1

    summary_path = OUTPUT_DIR / f"ui_library_classified_summary_{timestamp}.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    safe_print(f"[+] Summary: {summary_path}")


if __name__ == "__main__":
    main()
