#!/usr/bin/env python3
"""
Boilerplate Page Type Matcher
==============================
Cross-references PRD screen requirements against Figma frame inventory.
Shows what page types we need, what we have, and the gaps.
"""

import json
from collections import defaultdict

# Load master inventory
with open(r"C:\Users\under\Downloads\ENTERPRISE_OS_V7\07_BUILD_FACTORY\PRJ_UI_Component_Library\kit_screens\MASTER_FRAME_INVENTORY.json", "r", encoding="utf-8") as f:
    inv = json.load(f)

# === DEFINE BOILERPLATE PAGE TYPES ===
BOILERPLATE_TYPES = {
    "Dashboard Home": ["dashboard", "home", "overview", "main"],
    "Dashboard List/Table": ["list", "table", "inbox", "queue", "history", "log", "browse", "library", "index", "directory", "manage"],
    "Dashboard Detail": ["detail", "view", "single", "info"],
    "Dashboard Form/Settings": ["setting", "config", "editor", "edit", "form", "account", "preference"],
    "Analytics/Charts": ["analytics", "chart", "report", "stats", "metric", "performance", "insight", "monitor"],
    "Auth Pages": ["login", "sign in", "signin", "register", "sign up", "signup", "forgot", "password", "auth", "verify", "otp"],
    "Onboarding/Wizard": ["onboard", "wizard", "welcome", "get started", "step"],
    "Marketing/Landing Hero": ["hero", "landing", "home page", "homepage"],
    "Pricing Page": ["pricing", "plan", "subscription"],
    "About Page": ["about", "team", "story"],
    "Contact Page": ["contact", "support", "help"],
    "Blog/Content Hub": ["blog", "article", "post", "news", "magazine", "content"],
    "Chat/AI Interface": ["chat", "message", "conversation", "ai assistant"],
    "Search/Filter Page": ["search", "filter", "explore", "find", "discover"],
    "Profile Page": ["profile", "user", "member"],
    "Cards Grid/Gallery": ["card", "grid", "gallery", "collection", "catalog", "catalogue"],
    "Map View": ["map", "location", "area"],
    "Calendar/Schedule": ["calendar", "schedule", "event", "booking"],
    "Timeline": ["timeline", "journey", "progress", "tracker", "pipeline", "kanban"],
    "Builder/Canvas": ["builder", "create", "compose", "drag", "canvas", "sequence"],
    "Notification": ["notification", "alert", "bell"],
    "Media/Video": ["video", "media", "player", "stream", "podcast"],
    "E-commerce/Shop": ["shop", "cart", "checkout", "product", "order", "ecommerce", "store"],
    "Legal Pages": ["terms", "privacy", "policy", "cookie", "legal"],
    "Error/404": ["404", "error", "not found"],
    "File/Document": ["file", "document", "upload", "storage"],
    "CRM/Pipeline": ["crm", "pipeline", "lead", "client", "deal"],
    "Component Page": ["component", "button", "input", "icon", "widget", "style guide", "typography", "color"],
}

# === CLASSIFY ALL FIGMA FRAMES ===
kit_by_type = defaultdict(list)
unclassified = []

for kit_name, kit_data in inv["kits"].items():
    for page in kit_data["pages"]:
        if page["skip"]:
            continue
        for screen_name in page.get("screen_names", []):
            lower = screen_name.lower()
            matched = False
            for bp_type, keywords in BOILERPLATE_TYPES.items():
                if any(kw in lower for kw in keywords):
                    kit_by_type[bp_type].append({
                        "kit": kit_name,
                        "screen": screen_name,
                        "page": page["page_name"],
                        "file_key": kit_data["file_key"]
                    })
                    matched = True
                    break
            if not matched:
                unclassified.append({
                    "kit": kit_name,
                    "screen": screen_name,
                    "page": page["page_name"]
                })

# === PRD SCREEN REQUIREMENTS BY TYPE ===
prd_needs = {
    "Dashboard Home": {"pcl": 3, "fitness": 2, "leadengine": 1, "enterprise": 5},
    "Dashboard List/Table": {"pcl": 15, "fitness": 3, "leadengine": 12, "enterprise": 14},
    "Dashboard Detail": {"pcl": 10, "fitness": 4, "leadengine": 3, "enterprise": 6},
    "Dashboard Form/Settings": {"pcl": 12, "fitness": 2, "leadengine": 8, "enterprise": 7},
    "Analytics/Charts": {"pcl": 8, "fitness": 2, "leadengine": 8, "enterprise": 4},
    "Auth Pages": {"pcl": 4, "fitness": 2, "leadengine": 3, "enterprise": 2},
    "Onboarding/Wizard": {"pcl": 0, "fitness": 1, "leadengine": 2, "enterprise": 1},
    "Marketing/Landing Hero": {"pcl": 10, "fitness": 1, "leadengine": 5, "enterprise": 0},
    "Pricing Page": {"pcl": 1, "fitness": 1, "leadengine": 1, "enterprise": 0},
    "About Page": {"pcl": 1, "fitness": 0, "leadengine": 1, "enterprise": 0},
    "Contact Page": {"pcl": 1, "fitness": 1, "leadengine": 0, "enterprise": 0},
    "Blog/Content Hub": {"pcl": 8, "fitness": 1, "leadengine": 0, "enterprise": 2},
    "Chat/AI Interface": {"pcl": 0, "fitness": 1, "leadengine": 5, "enterprise": 2},
    "Search/Filter Page": {"pcl": 3, "fitness": 1, "leadengine": 0, "enterprise": 2},
    "Profile Page": {"pcl": 4, "fitness": 2, "leadengine": 1, "enterprise": 0},
    "Cards Grid/Gallery": {"pcl": 3, "fitness": 2, "leadengine": 1, "enterprise": 3},
    "Map View": {"pcl": 3, "fitness": 0, "leadengine": 0, "enterprise": 0},
    "Calendar/Schedule": {"pcl": 2, "fitness": 1, "leadengine": 0, "enterprise": 0},
    "Timeline": {"pcl": 2, "fitness": 1, "leadengine": 2, "enterprise": 2},
    "Builder/Canvas": {"pcl": 0, "fitness": 0, "leadengine": 3, "enterprise": 2},
    "Notification": {"pcl": 1, "fitness": 0, "leadengine": 1, "enterprise": 0},
    "Media/Video": {"pcl": 4, "fitness": 2, "leadengine": 0, "enterprise": 0},
    "E-commerce/Shop": {"pcl": 0, "fitness": 0, "leadengine": 0, "enterprise": 0},
    "Legal Pages": {"pcl": 3, "fitness": 3, "leadengine": 0, "enterprise": 0},
    "Error/404": {"pcl": 1, "fitness": 1, "leadengine": 0, "enterprise": 0},
    "CRM/Pipeline": {"pcl": 5, "fitness": 0, "leadengine": 6, "enterprise": 0},
}

# === OUTPUT ===
print("=" * 110)
print("BOILERPLATE PAGE TYPES: PRD NEEDS vs FIGMA AVAILABILITY")
print("=" * 110)
print()
print(f"{'PAGE TYPE':<28} {'NEED':>5} {'HAVE':>5} {'GAP':>5}  {'PCL':>4} {'FIT':>4} {'LE':>4} {'ENT':>4}  TOP KITS WITH VARIANTS")
print("-" * 110)

total_need = 0
total_have = 0
gaps = []
covered = []

for bp_type in sorted(BOILERPLATE_TYPES.keys()):
    if bp_type == "Component Page":
        continue  # Skip component pages from the count

    frames = kit_by_type.get(bp_type, [])
    needs = prd_needs.get(bp_type, {})
    need_count = sum(needs.values())
    have_count = len(frames)
    gap = max(0, need_count - have_count)

    total_need += need_count
    total_have += have_count

    kit_counts = defaultdict(int)
    for f in frames:
        kit_counts[f["kit"]] += 1
    top_kits = sorted(kit_counts.items(), key=lambda x: -x[1])[:4]
    top_str = ", ".join(f"{k}({v})" for k, v in top_kits)

    marker = " **" if gap > 0 else ""
    print(f"{bp_type:<28} {need_count:>5} {have_count:>5} {gap:>5}  {needs.get('pcl',0):>4} {needs.get('fitness',0):>4} {needs.get('leadengine',0):>4} {needs.get('enterprise',0):>4}  {top_str}{marker}")

    if gap > 0:
        gaps.append((bp_type, need_count, have_count, gap))
    elif have_count > 0:
        covered.append((bp_type, need_count, have_count))

print("-" * 110)
print(f"{'TOTALS':<28} {total_need:>5} {total_have:>5} {max(0, total_need-total_have):>5}")

# Component pages (design system assets, not app screens)
comp_frames = kit_by_type.get("Component Page", [])
print(f"\nComponent/Design System frames: {len(comp_frames)} (these are building blocks, not screens)")
print(f"Unclassified frames: {len(unclassified)} (need manual review or OCR)")

print()
print("=" * 80)
print("GAPS: Page types where we need more design variants")
print("=" * 80)
for bp_type, need, have, gap in sorted(gaps, key=lambda x: -x[3]):
    print(f"\n  {bp_type}: NEED {need}, HAVE {have}, GAP {gap}")
    frames = kit_by_type.get(bp_type, [])
    if frames:
        print(f"    Available from:")
        kit_counts = defaultdict(int)
        for f in frames:
            kit_counts[f["kit"]] += 1
        for k, v in sorted(kit_counts.items(), key=lambda x: -x[1]):
            print(f"      {k}: {v} variants")

print()
print("=" * 80)
print("WELL COVERED: Page types with surplus variants to choose from")
print("=" * 80)
for bp_type, need, have in sorted(covered, key=lambda x: -(x[2]-x[1])):
    surplus = have - need
    print(f"  {bp_type}: NEED {need}, HAVE {have} (+{surplus} surplus)")

# === SAVE FULL CROSS-REFERENCE ===
output = {
    "summary": {
        "total_prd_screens_needed": total_need,
        "total_figma_variants_available": total_have,
        "unclassified_frames": len(unclassified),
        "component_frames": len(comp_frames),
    },
    "boilerplate_types": {},
    "unclassified": unclassified[:50],
}

for bp_type in sorted(BOILERPLATE_TYPES.keys()):
    frames = kit_by_type.get(bp_type, [])
    needs = prd_needs.get(bp_type, {})
    output["boilerplate_types"][bp_type] = {
        "need": sum(needs.values()),
        "have": len(frames),
        "gap": max(0, sum(needs.values()) - len(frames)),
        "needs_by_app": needs,
        "available_variants": frames,
    }

outpath = r"C:\Users\under\Downloads\ENTERPRISE_OS_V7\07_BUILD_FACTORY\PRJ_UI_Component_Library\kit_screens\BOILERPLATE_CROSSREF.json"
with open(outpath, "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2)
print(f"\nFull cross-reference saved: {outpath}")
