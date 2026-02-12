#!/usr/bin/env python3
"""
Enterprise_OS V7 - Figma Library Subcategorizer

Adds granular subcategories to each item using LLM analysis.
Transforms broad categories into specific page types.

Example outputs:
- dashboard > analytics
- dashboard > user_management
- auth > login
- auth > signup
- auth > password_reset
- ecommerce > product_detail
- ecommerce > cart
- ecommerce > checkout
"""

import json
import os
import sys
import time
import re
from pathlib import Path
from datetime import datetime

try:
    import anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False
    print("[!] anthropic not installed. Run: pip install anthropic")

INPUT_FILE = Path("figma_library_v2/ui_library_classified_20260207_201810.json")
OUTPUT_DIR = Path("figma_library_v2")
CHECKPOINT_FILE = OUTPUT_DIR / "subcategorize_checkpoint.json"

# Comprehensive subcategory taxonomy
SUBCATEGORY_TAXONOMY = """
## Dashboard Types
- dashboard > analytics (charts, graphs, metrics, KPIs, reports)
- dashboard > admin (admin panel, system settings, configuration)
- dashboard > user (user dashboard, my dashboard, personal stats)
- dashboard > overview (home dashboard, main view, summary)
- dashboard > project (project management, kanban, tasks)
- dashboard > crm (customer management, leads, contacts)
- dashboard > financial (revenue, transactions, billing dashboard)

## Auth/Onboarding Types
- auth > login (sign in, log in)
- auth > signup (register, create account, sign up)
- auth > password_reset (forgot password, reset password)
- auth > email_verification (verify email, check email, confirm)
- auth > 2fa (two factor, OTP, verification code)
- auth > sso (social login, oauth, google/apple sign in)
- onboarding > welcome (welcome screen, intro, get started)
- onboarding > setup (account setup, profile setup, configuration)
- onboarding > tutorial (guide, walkthrough, tooltips)
- onboarding > permissions (allow notifications, enable location)

## Profile/Settings Types
- profile > view (user profile, my profile, public profile)
- profile > edit (edit profile, update info)
- settings > general (general settings, preferences)
- settings > account (account settings, security)
- settings > billing (payments, subscriptions, invoices)
- settings > notifications (notification preferences, alerts)
- settings > privacy (privacy settings, data, permissions)
- settings > team (team settings, members, roles)
- settings > integrations (connected apps, API keys)

## E-commerce Types
- ecommerce > home (shop home, store front)
- ecommerce > category (product category, collection)
- ecommerce > product_list (product grid, search results)
- ecommerce > product_detail (product page, item detail)
- ecommerce > cart (shopping cart, bag)
- ecommerce > checkout (checkout flow, payment)
- ecommerce > order_confirmation (thank you, order complete)
- ecommerce > order_history (my orders, purchase history)
- ecommerce > wishlist (saved items, favorites)

## Content Types
- content > blog_list (blog index, articles list)
- content > blog_post (article, blog detail)
- content > about (about us, company info)
- content > contact (contact us, get in touch)
- content > faq (help, questions)
- content > terms (legal, privacy policy, terms)
- content > portfolio (work, projects, case studies)
- content > team (our team, about team)

## Landing/Marketing Types
- landing > home (homepage, main landing)
- landing > features (features page, product features)
- landing > pricing (pricing page, plans)
- landing > testimonials (reviews, social proof)
- landing > cta (call to action, signup prompt)
- landing > comparison (vs competitors, comparison table)

## Communication Types
- messaging > inbox (messages, conversations list)
- messaging > chat (chat window, conversation)
- messaging > compose (new message, compose)
- notifications > list (notification center, alerts)
- notifications > detail (notification detail)

## Data/Tables Types
- tables > list (data table, records list)
- tables > detail (record detail, item view)
- tables > edit (edit record, form)
- tables > kanban (board view, columns)
- tables > calendar (calendar view, schedule)

## Empty/Error States
- empty > no_data (empty state, no items)
- empty > search (no results, not found)
- error > 404 (page not found)
- error > 500 (server error)
- error > maintenance (under construction)
- loading > skeleton (loading state, placeholder)

## Navigation Types
- nav > header (top nav, main header)
- nav > sidebar (side menu, drawer)
- nav > footer (page footer)
- nav > tabs (tab navigation)
- nav > breadcrumb (breadcrumbs)
- nav > mobile_menu (hamburger menu, mobile nav)

## Modal/Overlay Types
- modal > confirm (confirmation dialog, are you sure)
- modal > form (modal form, popup form)
- modal > info (info modal, details popup)
- modal > success (success message, complete)
- modal > error (error message, failed)

## Media Types
- media > gallery (image gallery, photos)
- media > video (video player, video page)
- media > upload (file upload, drag drop)
- media > preview (file preview, document view)

## Other Specific Types
- search > results (search results page)
- search > filters (filter panel, advanced search)
- map > view (map interface, location)
- calendar > view (calendar, date picker)
- chat > bot (chatbot, AI assistant)
- social > feed (activity feed, timeline)
- social > profile (social profile, user page)
"""


def safe_print(text: str):
    try:
        print(text, flush=True)
    except UnicodeEncodeError:
        print(text.encode('ascii', 'replace').decode('ascii'), flush=True)


def load_checkpoint():
    if CHECKPOINT_FILE.exists():
        with open(CHECKPOINT_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {"processed_ids": [], "results": {}}


def save_checkpoint(checkpoint):
    with open(CHECKPOINT_FILE, "w", encoding="utf-8") as f:
        json.dump(checkpoint, f, ensure_ascii=False)


def subcategorize_with_llm(client, items_batch: list) -> dict:
    """Use Claude to extract granular subcategories."""

    items_text = ""
    for item in items_batch:
        items_text += f"""
ID: {item['id']}
Name: {item['name']}
Category: {item['category']}
Page: {item['page_name']}
File: {item['file_name']}
---
"""

    prompt = f"""Analyze these UI components and assign granular subcategories.

Use this taxonomy:
{SUBCATEGORY_TAXONOMY}

For each item, determine the most specific subcategory that matches.
If nothing fits well, use the format: category > specific_type

Items to categorize:
{items_text}

Respond with ONLY valid JSON mapping ID to subcategory:
{{"id1": "dashboard > analytics", "id2": "auth > login", ...}}"""

    try:
        response = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}]
        )

        text = response.content[0].text.strip()
        # Find JSON in response
        match = re.search(r'\{[^{}]*\}', text, re.DOTALL)
        if match:
            return json.loads(match.group())
    except Exception as e:
        safe_print(f"  [!] LLM error: {str(e)[:50]}")

    return {}


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Add subcategories to Figma library")
    parser.add_argument("--input", default=str(INPUT_FILE), help="Input JSON file")
    parser.add_argument("--batch-size", type=int, default=15, help="LLM batch size")
    parser.add_argument("--limit", type=int, default=0, help="Limit items (0=all)")
    parser.add_argument("--resume", action="store_true", help="Resume from checkpoint")
    parser.add_argument("--category", help="Only process specific category")

    args = parser.parse_args()

    if not HAS_ANTHROPIC:
        safe_print("[!] anthropic required. Run: pip install anthropic")
        sys.exit(1)

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        safe_print("[!] ANTHROPIC_API_KEY not set")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    # Load data
    safe_print(f"[*] Loading {args.input}...")
    with open(args.input, encoding="utf-8") as f:
        items = json.load(f)
    safe_print(f"[*] Loaded {len(items)} items")

    # Filter by category if specified
    if args.category:
        items = [i for i in items if i["category"] == args.category]
        safe_print(f"[*] Filtered to {len(items)} items in category '{args.category}'")

    # Load checkpoint
    checkpoint = load_checkpoint() if args.resume else {"processed_ids": [], "results": {}}
    processed_ids = set(checkpoint["processed_ids"])

    # Filter out already processed
    to_process = [i for i in items if i["id"] not in processed_ids]

    if args.limit > 0:
        to_process = to_process[:args.limit]

    safe_print(f"[*] {len(processed_ids)} already processed, {len(to_process)} remaining")

    if len(to_process) == 0:
        safe_print("[+] All items already processed!")
    else:
        # Process in batches
        safe_print(f"[*] Processing {len(to_process)} items in batches of {args.batch_size}...")

        for i in range(0, len(to_process), args.batch_size):
            batch = to_process[i:i + args.batch_size]
            batch_num = i // args.batch_size + 1
            total_batches = (len(to_process) + args.batch_size - 1) // args.batch_size

            safe_print(f"  Batch {batch_num}/{total_batches}: processing {len(batch)} items...")

            results = subcategorize_with_llm(client, batch)

            for item in batch:
                checkpoint["processed_ids"].append(item["id"])
                if item["id"] in results:
                    checkpoint["results"][item["id"]] = results[item["id"]]

            save_checkpoint(checkpoint)
            time.sleep(0.5)

    # Apply results to items
    safe_print("\n[*] Applying subcategories to items...")

    # Reload full item list
    with open(args.input, encoding="utf-8") as f:
        all_items = json.load(f)

    subcats_applied = 0
    for item in all_items:
        if item["id"] in checkpoint["results"]:
            item["subcategory"] = checkpoint["results"][item["id"]]
            subcats_applied += 1
        else:
            # Generate basic subcategory from name
            item["subcategory"] = f"{item['category']} > general"

    safe_print(f"[*] Applied {subcats_applied} LLM subcategories")

    # Count subcategories
    subcat_counts = {}
    for item in all_items:
        sc = item.get("subcategory", "unknown")
        subcat_counts[sc] = subcat_counts.get(sc, 0) + 1

    safe_print(f"\n[*] Top 30 subcategories:")
    for sc, count in sorted(subcat_counts.items(), key=lambda x: -x[1])[:30]:
        safe_print(f"  {sc}: {count}")

    # Save enriched data
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = OUTPUT_DIR / f"ui_library_subcategorized_{timestamp}.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_items, f, indent=2, ensure_ascii=False)

    safe_print(f"\n[+] Saved to: {output_path}")
    safe_print(f"[+] Total subcategories: {len(subcat_counts)}")


if __name__ == "__main__":
    main()
