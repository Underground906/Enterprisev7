#!/usr/bin/env python3
"""
PRD Layout Matcher — Phase 5
==============================
Matches PRD screen requirements to layout templates from the 4 core kits.

For each PRD screen, finds:
1. Which layout template matches the required layout type
2. Which kit has the best component coverage
3. What components are missing and need sourcing from other kits

Input:  kit_screens/CORE_LAYOUT_LIBRARY.json (from Phase 3)
        03_Design/PRD_SCREEN_REQUIREMENTS.json
Output: kit_screens/PRD_LAYOUT_MATCHES.json

Cost: $0 (local computation only)
"""

import json
import os
import sys
from datetime import datetime
from collections import defaultdict

sys.stdout.reconfigure(line_buffering=True)

V7_ROOT = r"C:\Users\under\Downloads\ENTERPRISE_OS_V7"
KIT_SCREENS_DIR = os.path.join(
    V7_ROOT, "07_BUILD_FACTORY", "PRJ_UI_Component_Library", "kit_screens"
)
PRD_PATH = os.path.join(
    V7_ROOT, "07_BUILD_FACTORY", "PRJ_UI_Component_Library",
    "03_Design", "PRD_SCREEN_REQUIREMENTS.json"
)
LIBRARY_PATH = os.path.join(KIT_SCREENS_DIR, "CORE_LAYOUT_LIBRARY.json")
OUTPUT_PATH = os.path.join(KIT_SCREENS_DIR, "PRD_LAYOUT_MATCHES.json")

# Map PRD layout codes to Phase 2/3 layout types
LAYOUT_CODE_MAP = {
    "FC": ["full_canvas", "header_content_footer", "cards_grid"],
    "full-canvas": ["full_canvas", "header_content_footer", "cards_grid"],
    "SC": ["sidebar_content", "three_panel"],
    "sidebar-content": ["sidebar_content", "three_panel"],
    "TP": ["three_panel"],
    "three-panel": ["three_panel"],
    "SP": ["split_panel"],
    "split-panel": ["split_panel"],
    "CG": ["cards_grid", "full_canvas"],
    "cards-grid": ["cards_grid", "full_canvas"],
    "HCF": ["header_content_footer", "full_canvas"],
    "header-content-footer": ["header_content_footer", "full_canvas"],
}

# Normalize component names for matching
COMPONENT_ALIASES = {
    "topbar": ["header", "navbar", "top bar", "navigation"],
    "button": ["button", "btn", "cta"],
    "card": ["card", "tile", "panel"],
    "tabs": ["tab", "tabs", "tabbar"],
    "carousel": ["carousel", "slider", "swiper"],
    "accordion": ["accordion", "collapse", "expandable", "faq"],
    "form": ["form", "input", "field", "textarea"],
    "badge": ["badge", "tag", "chip", "label"],
    "modal": ["modal", "dialog", "popup", "overlay"],
    "search_bar": ["search", "search bar", "search field"],
    "table": ["table", "data table", "grid", "list"],
    "chart": ["chart", "graph", "analytics", "metric"],
    "avatar": ["avatar", "profile", "user icon"],
    "dropdown": ["dropdown", "select", "combobox", "menu"],
    "sidebar": ["sidebar", "sidenav", "navigation"],
    "breadcrumb": ["breadcrumb", "path"],
    "progress": ["progress", "stepper", "wizard"],
    "map": ["map", "location", "geo"],
    "calendar": ["calendar", "date picker", "scheduler"],
    "pagination": ["pagination", "pager"],
    "tooltip": ["tooltip", "popover"],
    "notification": ["notification", "alert", "toast", "snackbar"],
    "toggle": ["toggle", "switch"],
    "checkbox": ["checkbox", "check"],
    "radio": ["radio", "option"],
    "slider": ["slider", "range"],
    "upload": ["upload", "dropzone", "file"],
    "video": ["video", "player", "media"],
    "image": ["image", "photo", "gallery", "thumbnail"],
}


def normalize_component(name):
    """Map a component name to its canonical form."""
    lower = name.lower().strip()
    for canonical, aliases in COMPONENT_ALIASES.items():
        if any(alias in lower for alias in aliases):
            return canonical
    return lower


def compute_component_coverage(prd_components, template_components):
    """
    How many of the PRD's required components are available in the template?
    Returns (coverage_ratio, matched_components, missing_components).
    """
    if not prd_components:
        return 1.0, [], []

    prd_normalized = {normalize_component(c) for c in prd_components}
    template_normalized = {normalize_component(c) for c in template_components}

    matched = prd_normalized & template_normalized
    missing = prd_normalized - template_normalized

    coverage = len(matched) / len(prd_normalized) if prd_normalized else 1.0
    return coverage, sorted(matched), sorted(missing)


def score_match(prd_screen, template):
    """
    Score how well a template matches a PRD screen requirement.
    Returns a score 0-100 and match details.
    """
    score = 0
    details = {}

    # Layout type match (40 points)
    prd_layout = prd_screen.get("layout_code", prd_screen.get("layout", ""))
    compatible_types = LAYOUT_CODE_MAP.get(prd_layout, [])
    template_type = template.get("type", "")

    if template_type in compatible_types:
        # Direct match
        idx = compatible_types.index(template_type)
        layout_score = 40 - (idx * 10)  # First match = 40, second = 30, etc.
        score += max(layout_score, 10)
        details["layout_match"] = "direct"
    else:
        details["layout_match"] = "none"

    # Component coverage (40 points)
    prd_components = prd_screen.get("components_needed", [])
    template_components = template.get("core_components", [])
    coverage, matched, missing = compute_component_coverage(prd_components, template_components)
    comp_score = round(coverage * 40)
    score += comp_score
    details["component_coverage"] = round(coverage, 2)
    details["matched_components"] = matched
    details["missing_components"] = missing

    # Capability overlap (20 points)
    prd_notes = prd_screen.get("notes", "").lower()
    template_caps = template.get("capabilities", [])
    cap_hits = sum(1 for cap in template_caps if cap.replace("_", " ") in prd_notes)
    cap_score = min(cap_hits * 5, 20)
    score += cap_score
    details["capability_hits"] = cap_hits

    return min(score, 100), details


def find_matches_for_screen(prd_screen, all_templates):
    """Find the best matching templates for a PRD screen."""
    matches = []

    for template in all_templates:
        score, details = score_match(prd_screen, template)
        if score > 0:
            matches.append({
                "layout_id": template.get("layout_id", ""),
                "kit": template.get("kit", ""),
                "template_name": template.get("name", ""),
                "layout_type": template.get("type", ""),
                "score": score,
                "details": details,
                "representative_screen": template.get("representative_screen", ""),
                "screens_count": template.get("count", 0),
            })

    # Sort by score descending
    matches.sort(key=lambda m: m["score"], reverse=True)
    return matches[:5]  # Top 5 matches


def find_component_sources(missing_components, all_templates):
    """
    For missing components, find which kits/templates have them.
    Returns {component: [{kit, template, layout_id}]}.
    """
    sources = {}
    for comp in missing_components:
        comp_norm = normalize_component(comp)
        sources[comp] = []
        for tmpl in all_templates:
            tmpl_comps = {normalize_component(c) for c in tmpl.get("core_components", [])}
            if comp_norm in tmpl_comps:
                sources[comp].append({
                    "kit": tmpl.get("kit", ""),
                    "layout_id": tmpl.get("layout_id", ""),
                    "template_name": tmpl.get("name", ""),
                })
        # Dedupe by kit
        seen_kits = set()
        deduped = []
        for src in sources[comp]:
            if src["kit"] not in seen_kits:
                deduped.append(src)
                seen_kits.add(src["kit"])
        sources[comp] = deduped[:3]  # Top 3 sources

    return sources


def main():
    print(f"\n{'='*60}")
    print(f"PRD LAYOUT MATCHER — Phase 5")
    print(f"Match PRD screens to layout templates from 4 core kits")
    print(f"{'='*60}")

    # Load layout library
    if not os.path.exists(LIBRARY_PATH):
        print(f"ERROR: {LIBRARY_PATH} not found. Run Phase 3 first.")
        sys.exit(1)

    with open(LIBRARY_PATH, "r", encoding="utf-8") as f:
        library = json.load(f)

    all_templates = library.get("all_layouts", [])
    print(f"Layout templates loaded: {len(all_templates)} across {len(library.get('kits', {}))} kits")

    # Load PRD screen requirements
    if not os.path.exists(PRD_PATH):
        print(f"ERROR: {PRD_PATH} not found.")
        sys.exit(1)

    with open(PRD_PATH, "r", encoding="utf-8") as f:
        prd_data = json.load(f)

    # Collect all screens from all platforms
    all_prd_screens = []
    platforms = prd_data.get("platforms", {})
    for platform_key, platform_data in platforms.items():
        screens = platform_data.get("screens", [])
        for screen in screens:
            screen["platform"] = platform_key
        all_prd_screens.extend(screens)

    print(f"PRD screens loaded: {len(all_prd_screens)} across {len(platforms)} platforms")
    print(f"{'='*60}\n")

    # Match each PRD screen
    results = {
        "generated_at": datetime.now().isoformat(),
        "prd_source": PRD_PATH,
        "library_source": LIBRARY_PATH,
        "total_prd_screens": len(all_prd_screens),
        "total_templates": len(all_templates),
        "matches": [],
        "summary": {
            "perfect_matches": 0,    # score >= 70
            "good_matches": 0,       # score 40-69
            "weak_matches": 0,       # score 10-39
            "no_match": 0,           # score < 10 or no matches
            "missing_components_all": defaultdict(int),
            "best_kit_per_screen": defaultdict(int),
        },
    }

    for i, prd_screen in enumerate(all_prd_screens):
        screen_id = prd_screen.get("screen_id", f"SCREEN_{i}")
        screen_name = prd_screen.get("name", "Unknown")
        platform = prd_screen.get("platform", "")

        matches = find_matches_for_screen(prd_screen, all_templates)

        if matches:
            best = matches[0]
            best_score = best["score"]

            # Collect all missing components from the best match
            missing = best["details"].get("missing_components", [])
            component_sources = find_component_sources(missing, all_templates)

            if best_score >= 70:
                results["summary"]["perfect_matches"] += 1
                quality = "PERFECT"
            elif best_score >= 40:
                results["summary"]["good_matches"] += 1
                quality = "GOOD"
            else:
                results["summary"]["weak_matches"] += 1
                quality = "WEAK"

            results["summary"]["best_kit_per_screen"][best["kit"]] += 1
            for comp in missing:
                results["summary"]["missing_components_all"][comp] += 1

            if (i + 1) % 20 == 0 or i == 0:
                print(f"[{i+1}/{len(all_prd_screens)}] {screen_id} \"{screen_name}\" -> "
                      f"{quality} ({best_score}) via {best['kit']}/{best['layout_id']}"
                      + (f" [missing: {', '.join(missing)}]" if missing else ""))
        else:
            results["summary"]["no_match"] += 1
            quality = "NONE"
            component_sources = {}

            if (i + 1) % 20 == 0 or i == 0:
                print(f"[{i+1}/{len(all_prd_screens)}] {screen_id} \"{screen_name}\" -> NO MATCH")

        results["matches"].append({
            "prd_screen_id": screen_id,
            "prd_screen_name": screen_name,
            "platform": platform,
            "prd_layout": prd_screen.get("layout_code", prd_screen.get("layout", "")),
            "prd_components": prd_screen.get("components_needed", []),
            "priority": prd_screen.get("priority", ""),
            "match_quality": quality,
            "top_matches": matches,
            "component_sources": component_sources,
        })

    # Convert defaultdicts to dicts for JSON
    results["summary"]["missing_components_all"] = dict(results["summary"]["missing_components_all"])
    results["summary"]["best_kit_per_screen"] = dict(results["summary"]["best_kit_per_screen"])

    # Save results
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved: {OUTPUT_PATH}")

    # Summary
    s = results["summary"]
    print(f"\n{'='*60}")
    print(f"MATCHING COMPLETE")
    print(f"{'='*60}")
    print(f"Total PRD screens: {len(all_prd_screens)}")
    print(f"  Perfect matches (70+): {s['perfect_matches']}")
    print(f"  Good matches (40-69):  {s['good_matches']}")
    print(f"  Weak matches (10-39):  {s['weak_matches']}")
    print(f"  No match:              {s['no_match']}")

    coverage = (s["perfect_matches"] + s["good_matches"]) / max(len(all_prd_screens), 1) * 100
    print(f"\nCoverage (perfect + good): {coverage:.0f}%")

    print(f"\nBest kit per screen:")
    for kit, count in sorted(s["best_kit_per_screen"].items(), key=lambda x: -x[1]):
        print(f"  {kit}: {count} screens")

    if s["missing_components_all"]:
        print(f"\nMost commonly missing components:")
        for comp, count in sorted(s["missing_components_all"].items(), key=lambda x: -x[1])[:10]:
            print(f"  {comp}: needed by {count} screens")

    print(f"\n{'='*60}")
    print(f"Pipeline complete! Review PRD_LAYOUT_MATCHES.json for full details.")
    print(f"For each PRD screen, you now know:")
    print(f"  1. Which layout template to use (from which kit)")
    print(f"  2. What components are covered")
    print(f"  3. What's missing and where to source it")


if __name__ == "__main__":
    main()
