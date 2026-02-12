#!/usr/bin/env python3
"""
Reclassify library items against the canonical taxonomy.

Uses fuzzy matching to:
1. Match item names to canonical component_names
2. Assign component_type_id, section_id, subsection_id
3. Map LLM categories to functional categories
"""

import psycopg2
from rapidfuzz import fuzz, process
import re
from collections import defaultdict

DB_CONFIG = {
    "dbname": "ui_library",
    "user": "postgres",
    "host": "localhost"
}


def normalize_name(name: str) -> str:
    """Normalize a name for matching."""
    if not name:
        return ""
    # Lowercase
    name = name.lower()
    # Remove special chars
    name = re.sub(r'[^a-z0-9\s-]', ' ', name)
    # Collapse whitespace
    name = re.sub(r'\s+', ' ', name).strip()
    return name


def load_canonical_names(cur):
    """Load all canonical component names for matching."""
    cur.execute("""
        SELECT id, name, component_type_id, section_id, subsection_id
        FROM component_names
    """)

    names = {}
    for row in cur.fetchall():
        norm = normalize_name(row[1])
        if norm:
            names[norm] = {
                "id": row[0],
                "name": row[1],
                "component_type_id": row[2],
                "section_id": row[3],
                "subsection_id": row[4]
            }

    return names


def load_component_types(cur):
    """Load component types for keyword matching."""
    cur.execute("SELECT id, name FROM component_types")
    types = {}
    for row in cur.fetchall():
        types[row[0]] = row[1]
        # Also add normalized name as key
        types[normalize_name(row[1])] = row[0]
    return types


def load_functional_categories(cur):
    """Load functional categories for mapping."""
    cur.execute("SELECT id, name FROM functional_categories")
    cats = {}
    for row in cur.fetchall():
        cats[row[0]] = row[1]
        # Also map by normalized name
        cats[normalize_name(row[1])] = row[0]
    return cats


# Mapping from LLM categories to functional categories
LLM_TO_FUNCTIONAL = {
    "dashboard": "dashboard-admin",
    "auth": "profile-auth",
    "profile": "profile-auth",
    "ecommerce": "ecommerce",
    "content": "content-publishing",
    "hero": "landing-marketing",
    "cta": "landing-marketing",
    "landing": "landing-marketing",
    "pricing": "sales-conversion",
    "testimonials": "sales-conversion",
    "navigation": "website-navigation",
    "footer": "website-navigation",
    "forms": "forms-input",
    "tables": "data-analytics",
    "media": "content-publishing",
    "cards": "content-publishing",
    "modals": "forms-input",
    "icons": None,  # No functional category
    "features": "landing-marketing",
    "empty": None,
    "other": None
}

# Mapping from LLM subcategories to component_type hints
SUBCATEGORY_TYPE_HINTS = {
    "nav > header": "navigation-menus",
    "nav > sidebar": "sidebars-drawers",
    "nav > mobile_menu": "navigation-menus",
    "nav > tabs": "tabs-segmented",
    "dashboard > analytics": "dashboard-analytics",
    "dashboard > overview": "dashboard-analytics",
    "dashboard > project": "dashboard-analytics",
    "dashboard > financial": "dashboard-analytics",
    "dashboard > crm": "dashboard-analytics",
    "dashboard > admin": "dashboard-analytics",
    "content > blog_post": "content-blocks",
    "content > blog_list": "content-blocks",
    "content > faq": "accordions-collapse",
    "content > about": "content-blocks",
    "ecommerce > product_detail": "ecommerce-components",
    "ecommerce > checkout": "checkout-payment",
    "ecommerce > cart": "checkout-payment",
    "auth > login": "login-register",
    "auth > signup": "login-register",
    "messaging > chat": "chat-components",
    "messaging > inbox": "chat-components"
}


def reclassify_items(batch_size: int = 1000, min_score: int = 70):
    """Reclassify all library items."""

    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    try:
        # Load reference data
        print("[*] Loading canonical names...")
        canonical_names = load_canonical_names(cur)
        print(f"    Loaded {len(canonical_names)} canonical names")

        print("[*] Loading component types...")
        comp_types = load_component_types(cur)
        print(f"    Loaded {len(comp_types)} component types")

        print("[*] Loading functional categories...")
        func_cats = load_functional_categories(cur)
        print(f"    Loaded {len(func_cats)} functional categories")

        # Get items to reclassify
        cur.execute("SELECT COUNT(*) FROM component_library")
        total = cur.fetchone()[0]
        print(f"\n[*] Reclassifying {total} items...")

        # Process in batches
        offset = 0
        matched = 0
        type_assigned = 0
        func_assigned = 0

        while offset < total:
            cur.execute("""
                SELECT id, name, llm_category, llm_subcategory
                FROM component_library
                ORDER BY id
                LIMIT %s OFFSET %s
            """, (batch_size, offset))

            items = cur.fetchall()
            if not items:
                break

            updates = []

            for item_id, name, llm_cat, llm_subcat in items:
                norm_name = normalize_name(name)

                # Initialize update values
                component_type_id = None
                section_id = None
                subsection_id = None
                functional_category_id = None
                matched_name_id = None

                # Try fuzzy match against canonical names
                if norm_name and len(norm_name) > 2:
                    # Get best matches
                    results = process.extract(
                        norm_name,
                        canonical_names.keys(),
                        scorer=fuzz.token_sort_ratio,
                        limit=3
                    )

                    if results and results[0][1] >= min_score:
                        best_match = results[0][0]
                        match_data = canonical_names[best_match]
                        component_type_id = match_data["component_type_id"]
                        section_id = match_data["section_id"]
                        subsection_id = match_data["subsection_id"]
                        matched_name_id = match_data["id"]
                        matched += 1

                # If no fuzzy match, try to assign component_type from subcategory hints
                if not component_type_id and llm_subcat:
                    hint_type = SUBCATEGORY_TYPE_HINTS.get(llm_subcat)
                    if hint_type and hint_type in comp_types:
                        component_type_id = hint_type

                # If still no type, try from LLM category keyword
                if not component_type_id and llm_cat:
                    # Check if category name matches any component type
                    for type_id, type_name in comp_types.items():
                        if isinstance(type_name, str) and llm_cat.lower() in type_name.lower():
                            component_type_id = type_id
                            break

                if component_type_id:
                    type_assigned += 1

                # Map LLM category to functional category
                if llm_cat:
                    func_id = LLM_TO_FUNCTIONAL.get(llm_cat)
                    if func_id and func_id in func_cats:
                        functional_category_id = func_id
                        func_assigned += 1

                updates.append((
                    component_type_id,
                    section_id,
                    subsection_id,
                    functional_category_id,
                    matched_name_id,
                    item_id
                ))

            # Batch update
            cur.executemany("""
                UPDATE component_library
                SET component_type_id = %s,
                    section_id = %s,
                    subsection_id = %s,
                    functional_category_id = %s,
                    matched_component_name_id = %s,
                    updated_at = NOW()
                WHERE id = %s
            """, updates)

            conn.commit()
            offset += batch_size

            if offset % 5000 == 0 or offset >= total:
                print(f"    Processed {min(offset, total)}/{total}...")

        print(f"\n[+] Reclassification complete:")
        print(f"    Fuzzy matched to canonical names: {matched}")
        print(f"    Component type assigned: {type_assigned}")
        print(f"    Functional category assigned: {func_assigned}")

        # Show distribution of assigned types
        print("\n[*] Component type distribution (top 15):")
        cur.execute("""
            SELECT ct.name, COUNT(*)
            FROM component_library cl
            JOIN component_types ct ON cl.component_type_id = ct.id
            GROUP BY ct.name
            ORDER BY COUNT(*) DESC
            LIMIT 15
        """)
        for row in cur.fetchall():
            print(f"    {row[0]}: {row[1]}")

        print("\n[*] Functional category distribution:")
        cur.execute("""
            SELECT fc.name, COUNT(*)
            FROM component_library cl
            JOIN functional_categories fc ON cl.functional_category_id = fc.id
            GROUP BY fc.name
            ORDER BY COUNT(*) DESC
        """)
        for row in cur.fetchall():
            print(f"    {row[0]}: {row[1]}")

    except Exception as e:
        conn.rollback()
        print(f"[!] Error: {e}")
        raise
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    reclassify_items()
