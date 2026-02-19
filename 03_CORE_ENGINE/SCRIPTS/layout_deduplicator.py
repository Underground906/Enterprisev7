#!/usr/bin/env python3
"""
Layout Deduplicator — Phase 3
================================
Groups screens by layout type + component pattern to find unique templates.
Most kits have 70+ screens but only 5-10 unique layout patterns.

Input:  kit_screens/{KitName}/SCREEN_ANALYSIS.json (from Phase 2)
Output: kit_screens/{KitName}/LAYOUT_TEMPLATES.json (per kit)
        kit_screens/CORE_LAYOUT_LIBRARY.json (combined)

Cost: $0 (local computation only)
"""

import json
import os
import sys
from datetime import datetime
from collections import defaultdict

sys.stdout.reconfigure(line_buffering=True)

KIT_SCREENS_DIR = os.path.join(
    r"C:\Users\under\Downloads\ENTERPRISE_OS_V7",
    "07_BUILD_FACTORY", "PRJ_UI_Component_Library", "kit_screens"
)

CORE_KITS = ["Brainwave 2.0", "Real Estate SaaS Kit", "Chroma", "Majin"]

# Similarity threshold for grouping screens into the same template
COMPONENT_OVERLAP_THRESHOLD = 0.6  # 60% overlap = same template


def get_component_set(screen):
    """Extract a set of component root names from a screen's instances."""
    components = set()
    for inst in screen.get("nested_components", []):
        name = inst.get("name", "")
        if "/" in name:
            root = name.split("/")[0].strip()
        else:
            root = name.strip()
        if root:
            components.add(root.lower())
    return components


def get_panel_signature(screen):
    """Create a panel-based signature for layout comparison."""
    layout = screen.get("layout", {})
    panels = layout.get("panels", [])

    sig_parts = []
    for panel in sorted(panels, key=lambda p: p.get("position", "")):
        pos = panel.get("position", "?")
        role = panel.get("role", "?")
        w = panel.get("width_approx", 0)
        # Bucket widths: narrow (<300), medium (300-600), wide (>600)
        w_bucket = "narrow" if w < 300 else ("medium" if w < 600 else "wide")
        sig_parts.append(f"{pos}:{role}:{w_bucket}")

    return "|".join(sig_parts)


def compute_overlap(set_a, set_b):
    """Jaccard similarity between two sets."""
    if not set_a and not set_b:
        return 1.0
    if not set_a or not set_b:
        return 0.0
    intersection = len(set_a & set_b)
    union = len(set_a | set_b)
    return intersection / union if union > 0 else 0.0


def group_by_layout_type(screens):
    """Group screens by their layout type (from Phase 2 analysis)."""
    groups = defaultdict(list)
    for screen in screens:
        lt = screen.get("layout", {}).get("type", "unknown")
        groups[lt].append(screen)
    return dict(groups)


def find_unique_templates(screens, kit_name):
    """
    Within a set of screens, find unique layout templates.

    Algorithm:
    1. Group by layout type (sidebar_content, three_panel, etc.)
    2. Within each group, compare panel signatures
    3. Screens with same panel signature AND 60%+ component overlap = same template
    4. Pick the screen with most components as representative
    """
    templates = []
    template_id_counter = 0

    # First group by layout type
    layout_groups = group_by_layout_type(screens)

    for layout_type, group_screens in layout_groups.items():
        # Sub-group by panel signature
        sig_groups = defaultdict(list)
        for screen in group_screens:
            sig = get_panel_signature(screen)
            sig_groups[sig].append(screen)

        for sig, sig_screens in sig_groups.items():
            # Within same signature, merge by component overlap
            clusters = []
            assigned = set()

            for i, screen_a in enumerate(sig_screens):
                if i in assigned:
                    continue

                cluster = [screen_a]
                comp_a = get_component_set(screen_a)
                assigned.add(i)

                for j, screen_b in enumerate(sig_screens):
                    if j in assigned:
                        continue
                    comp_b = get_component_set(screen_b)
                    overlap = compute_overlap(comp_a, comp_b)
                    if overlap >= COMPONENT_OVERLAP_THRESHOLD:
                        cluster.append(screen_b)
                        assigned.add(j)

                clusters.append(cluster)

            # Each cluster is a unique template
            for cluster in clusters:
                template_id_counter += 1
                # Pick representative = screen with most components
                representative = max(cluster, key=lambda s: s.get("component_count", 0))

                # Collect all unique components across cluster
                all_components = set()
                for s in cluster:
                    all_components |= get_component_set(s)

                # Collect all capabilities across cluster
                all_capabilities = set()
                for s in cluster:
                    all_capabilities.update(s.get("capabilities", []))

                kit_prefix = kit_name[:2].upper()
                template = {
                    "layout_id": f"{kit_prefix}_L{template_id_counter}",
                    "name": representative.get("screen_name", "Unknown"),
                    "type": layout_type,
                    "panel_signature": sig,
                    "screens_using": [s.get("screen_name", "") for s in cluster],
                    "screen_ids": [s.get("screen_id", "") for s in cluster],
                    "count": len(cluster),
                    "representative_screen": representative.get("screen_id", ""),
                    "representative_name": representative.get("screen_name", ""),
                    "dimensions": representative.get("dimensions", {}),
                    "layout_detail": representative.get("layout", {}),
                    "core_components": sorted(all_components)[:30],
                    "capabilities": sorted(all_capabilities),
                    "is_light": representative.get("is_light", True),
                }
                templates.append(template)

    return templates


def process_kit(kit_name):
    """Process one kit's SCREEN_ANALYSIS.json and find unique templates."""
    analysis_path = os.path.join(KIT_SCREENS_DIR, kit_name, "SCREEN_ANALYSIS.json")

    if not os.path.exists(analysis_path):
        print(f"  ERROR: {analysis_path} not found. Run Phase 2 first.")
        return None

    with open(analysis_path, "r", encoding="utf-8") as f:
        analysis = json.load(f)

    screens = analysis.get("screens", [])
    print(f"  {len(screens)} screens to analyze")

    if not screens:
        return {
            "kit": kit_name,
            "unique_layouts": 0,
            "total_screens": 0,
            "layouts": [],
        }

    templates = find_unique_templates(screens, kit_name)

    result = {
        "kit": kit_name,
        "file_key": analysis.get("file_key", ""),
        "analyzed_at": datetime.now().isoformat(),
        "unique_layouts": len(templates),
        "total_screens": len(screens),
        "dedup_ratio": f"{len(screens)} screens -> {len(templates)} templates ({round(len(templates)/max(len(screens),1)*100)}%)",
        "layouts": templates,
    }

    return result


def main():
    print(f"\n{'='*60}")
    print(f"LAYOUT DEDUPLICATOR — Phase 3")
    print(f"Find unique layout templates across 4 core kits")
    print(f"{'='*60}")
    print(f"Input:  kit_screens/{{Kit}}/SCREEN_ANALYSIS.json")
    print(f"Output: kit_screens/{{Kit}}/LAYOUT_TEMPLATES.json")
    print(f"        kit_screens/CORE_LAYOUT_LIBRARY.json")
    print(f"{'='*60}\n")

    combined = {
        "generated_at": datetime.now().isoformat(),
        "total_kits": len(CORE_KITS),
        "grand_totals": {
            "total_screens": 0,
            "total_unique_layouts": 0,
            "total_representative_screens": 0,
        },
        "kits": {},
        "all_layouts": [],  # Flat list for easy searching
    }

    for kit_name in CORE_KITS:
        print(f"\n--- {kit_name} ---")
        result = process_kit(kit_name)

        if result is None:
            continue

        # Save per-kit templates
        out_path = os.path.join(KIT_SCREENS_DIR, kit_name, "LAYOUT_TEMPLATES.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"  {result['dedup_ratio']}")
        print(f"  Saved: {out_path}")

        # List templates
        for tmpl in result["layouts"]:
            screens_preview = tmpl["screens_using"][:3]
            more = f" +{len(tmpl['screens_using'])-3} more" if len(tmpl["screens_using"]) > 3 else ""
            print(f"    [{tmpl['layout_id']}] {tmpl['type']} — \"{tmpl['name']}\" "
                  f"({tmpl['count']} screens: {', '.join(screens_preview)}{more})")

        # Add to combined
        combined["kits"][kit_name] = {
            "file_key": result.get("file_key", ""),
            "unique_layouts": result["unique_layouts"],
            "total_screens": result["total_screens"],
            "dedup_ratio": result["dedup_ratio"],
            "layouts": result["layouts"],
        }
        combined["grand_totals"]["total_screens"] += result["total_screens"]
        combined["grand_totals"]["total_unique_layouts"] += result["unique_layouts"]
        combined["grand_totals"]["total_representative_screens"] += result["unique_layouts"]

        # Add to flat list with kit name
        for tmpl in result["layouts"]:
            tmpl_copy = dict(tmpl)
            tmpl_copy["kit"] = kit_name
            combined["all_layouts"].append(tmpl_copy)

    # Save combined library
    combined_path = os.path.join(KIT_SCREENS_DIR, "CORE_LAYOUT_LIBRARY.json")
    with open(combined_path, "w", encoding="utf-8") as f:
        json.dump(combined, f, indent=2, ensure_ascii=False)
    print(f"\nCombined library: {combined_path}")

    # Summary
    print(f"\n{'='*60}")
    print(f"DEDUPLICATION COMPLETE")
    print(f"{'='*60}")
    print(f"Total screens across 4 kits: {combined['grand_totals']['total_screens']}")
    print(f"Unique layout templates: {combined['grand_totals']['total_unique_layouts']}")
    print(f"Representative screens for PNG export: {combined['grand_totals']['total_representative_screens']}")
    print(f"\nPer-kit:")
    for kit_name, kit_data in combined["kits"].items():
        print(f"  {kit_name}: {kit_data['dedup_ratio']}")

    # Layout type distribution
    type_counts = defaultdict(int)
    for layout in combined["all_layouts"]:
        type_counts[layout["type"]] += 1
    print(f"\nLayout type distribution:")
    for lt, count in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"  {lt}: {count} templates")

    print(f"\n{'='*60}")
    print(f"Next: Run figma_export_representative.py (Phase 4) for {combined['grand_totals']['total_representative_screens']} PNGs")


if __name__ == "__main__":
    main()
