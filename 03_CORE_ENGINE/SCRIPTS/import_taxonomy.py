#!/usr/bin/env python3
"""
Import canonical_taxonomy.json into PostgreSQL database.

Populates:
- component_types (31 categories)
- component_type_sections (406 sections)
- component_type_subsections (667 subsections)
- component_names (12,464 canonical names)
- functional_categories (12 from PRD)
- industry_verticals (13 from PRD)
"""

import json
import psycopg2
from psycopg2.extras import execute_batch
import re

DB_CONFIG = {
    "dbname": "ui_library",
    "user": "postgres",
    "host": "localhost"
}

def slugify(text):
    """Convert text to slug format."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    return text.strip('-')


def import_taxonomy(taxonomy_path: str):
    """Import the canonical taxonomy into PostgreSQL."""

    print(f"[*] Loading taxonomy from {taxonomy_path}...")
    with open(taxonomy_path, 'r', encoding='utf-8') as f:
        taxonomy = json.load(f)

    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    try:
        # ============================================================
        # Import Functional Categories (from PRD)
        # ============================================================
        print("[*] Importing functional categories...")
        func_cats = taxonomy.get("dimensions", {}).get("functional_categories", {}).get("categories", [])

        for i, cat in enumerate(func_cats):
            cur.execute("""
                INSERT INTO functional_categories (id, name, example_pages, sort_order)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (id) DO UPDATE SET name = EXCLUDED.name
            """, (cat["id"], cat["name"], cat.get("pages", []), i))

        print(f"    Imported {len(func_cats)} functional categories")

        # ============================================================
        # Import Industry Verticals (from PRD)
        # ============================================================
        print("[*] Importing industry verticals...")
        verticals = taxonomy.get("dimensions", {}).get("industry_verticals", {}).get("verticals", [])

        for i, vert in enumerate(verticals):
            cur.execute("""
                INSERT INTO industry_verticals (id, name, specialized_pages, sort_order)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (id) DO UPDATE SET name = EXCLUDED.name
            """, (vert["id"], vert["name"], vert.get("pages", []), i))

        print(f"    Imported {len(verticals)} industry verticals")

        # ============================================================
        # Import Component Types, Sections, Subsections, Names
        # ============================================================
        print("[*] Importing component types...")
        comp_types = taxonomy.get("component_types", {})

        type_count = 0
        section_count = 0
        subsection_count = 0
        name_count = 0

        suffix_patterns = {
            '-accessible': 'accessibility',
            '-a11y': 'accessibility',
            '-lazy': 'performance',
            '-skeleton': 'performance',
            '-rtl': 'localization',
            '-ltr': 'localization',
            '-fade': 'animation',
            '-slide': 'animation',
            '-mobile': 'responsive',
            '-tablet': 'responsive',
            '-desktop': 'responsive',
            '-error': 'error',
            '-disabled': 'state',
            '-loading': 'state',
            '-hover': 'state',
            '-active': 'state',
            '-dark': 'theme',
            '-light': 'theme'
        }

        for i, (type_key, ctype) in enumerate(comp_types.items()):
            type_id = ctype.get("id", type_key)

            # Insert component type
            cur.execute("""
                INSERT INTO component_types (id, name, sort_order, section_count, total_component_names)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (id) DO UPDATE SET name = EXCLUDED.name
            """, (
                type_id,
                ctype.get("name", type_key),
                i,
                len(ctype.get("sections", [])),
                ctype.get("total_component_names", 0)
            ))
            type_count += 1

            # Import sections
            for j, section in enumerate(ctype.get("sections", [])):
                section_id = f"{type_id}--{section.get('id', slugify(section['name']))}"

                cur.execute("""
                    INSERT INTO component_type_sections
                    (id, component_type_id, name, sort_order, direct_component_count, subsection_count)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (id) DO UPDATE SET name = EXCLUDED.name
                """, (
                    section_id,
                    type_id,
                    section["name"],
                    j,
                    len(section.get("components", [])),
                    len(section.get("subsections", []))
                ))
                section_count += 1

                # Import direct components in section
                for comp_name in section.get("components", []):
                    # Detect suffix
                    has_suffix = False
                    suffix_type = None
                    base_name = comp_name

                    for suffix, stype in suffix_patterns.items():
                        if comp_name.lower().endswith(suffix):
                            has_suffix = True
                            suffix_type = stype
                            base_name = comp_name[:-len(suffix)]
                            break

                    cur.execute("""
                        INSERT INTO component_names
                        (name, component_type_id, section_id, subsection_id, has_suffix, suffix_type, base_name)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (comp_name, type_id, section_id, None, has_suffix, suffix_type, base_name))
                    name_count += 1

                # Import subsections
                for k, subsec in enumerate(section.get("subsections", [])):
                    subsection_id = f"{section_id}--{subsec.get('id', slugify(subsec['name']))}"

                    cur.execute("""
                        INSERT INTO component_type_subsections
                        (id, section_id, component_type_id, name, sort_order, component_count)
                        VALUES (%s, %s, %s, %s, %s, %s)
                        ON CONFLICT (id) DO UPDATE SET name = EXCLUDED.name
                    """, (
                        subsection_id,
                        section_id,
                        type_id,
                        subsec["name"],
                        k,
                        len(subsec.get("components", []))
                    ))
                    subsection_count += 1

                    # Import components in subsection
                    for comp_name in subsec.get("components", []):
                        has_suffix = False
                        suffix_type = None
                        base_name = comp_name

                        for suffix, stype in suffix_patterns.items():
                            if comp_name.lower().endswith(suffix):
                                has_suffix = True
                                suffix_type = stype
                                base_name = comp_name[:-len(suffix)]
                                break

                        cur.execute("""
                            INSERT INTO component_names
                            (name, component_type_id, section_id, subsection_id, has_suffix, suffix_type, base_name)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                        """, (comp_name, type_id, section_id, subsection_id, has_suffix, suffix_type, base_name))
                        name_count += 1

            if (i + 1) % 5 == 0:
                print(f"    Processed {i + 1}/{len(comp_types)} component types...")

        conn.commit()

        print(f"\n[+] Import complete:")
        print(f"    Component types: {type_count}")
        print(f"    Sections: {section_count}")
        print(f"    Subsections: {subsection_count}")
        print(f"    Component names: {name_count}")

        # Verify counts
        cur.execute("SELECT COUNT(*) FROM component_types")
        print(f"\n[*] Verification:")
        print(f"    component_types: {cur.fetchone()[0]}")
        cur.execute("SELECT COUNT(*) FROM component_type_sections")
        print(f"    component_type_sections: {cur.fetchone()[0]}")
        cur.execute("SELECT COUNT(*) FROM component_type_subsections")
        print(f"    component_type_subsections: {cur.fetchone()[0]}")
        cur.execute("SELECT COUNT(*) FROM component_names")
        print(f"    component_names: {cur.fetchone()[0]}")
        cur.execute("SELECT COUNT(*) FROM functional_categories")
        print(f"    functional_categories: {cur.fetchone()[0]}")
        cur.execute("SELECT COUNT(*) FROM industry_verticals")
        print(f"    industry_verticals: {cur.fetchone()[0]}")

    except Exception as e:
        conn.rollback()
        print(f"[!] Error: {e}")
        raise
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    import sys
    taxonomy_path = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\under\Downloads\canonical_taxonomy.json"
    import_taxonomy(taxonomy_path)
