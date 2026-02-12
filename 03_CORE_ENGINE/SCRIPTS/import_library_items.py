#!/usr/bin/env python3
"""
Import the 22,555 Figma library items into PostgreSQL.

Populates:
- components_raw (raw extraction data)
- component_library (classified, searchable)
- kits (file-level metadata)
"""

import json
import psycopg2
from psycopg2.extras import execute_batch
import os
from datetime import datetime

DB_CONFIG = {
    "dbname": "ui_library",
    "user": "postgres",
    "host": "localhost"
}


def import_library(json_path: str, thumbs_dir: str = None):
    """Import library items into PostgreSQL."""

    print(f"[*] Loading library from {json_path}...")
    with open(json_path, 'r', encoding='utf-8') as f:
        items = json.load(f)

    print(f"[*] Loaded {len(items)} items")

    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    try:
        # ============================================================
        # Extract kits (unique file_key + file_name)
        # ============================================================
        print("[*] Extracting kit metadata...")
        kits = {}
        for item in items:
            fk = item.get("file_key")
            if fk and fk not in kits:
                kits[fk] = {
                    "file_key": fk,
                    "file_name": item.get("file_name", ""),
                    "project_name": item.get("project_name"),
                    "item_count": 0
                }
            if fk:
                kits[fk]["item_count"] += 1

        print(f"    Found {len(kits)} unique kits")

        # Insert kits
        for kit in kits.values():
            cur.execute("""
                INSERT INTO kits (file_key, file_name, project_name, item_count)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (file_key) DO UPDATE SET item_count = EXCLUDED.item_count
            """, (kit["file_key"], kit["file_name"], kit["project_name"], kit["item_count"]))

        # ============================================================
        # Import items into components_raw and component_library
        # ============================================================
        print("[*] Importing library items...")

        raw_batch = []
        lib_batch = []

        for i, item in enumerate(items):
            item_id = item.get("id", f"item_{i}")

            # Build thumbnail path
            thumb_path = None
            if thumbs_dir and item.get("file_key") and item.get("category"):
                safe_id = item_id.replace(':', '_')
                safe_name = (item.get("name", "")[:50]).replace('/', '_').replace('\\', '_').replace(':', '_')
                safe_name = safe_name.replace('*', '_').replace('?', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_')
                thumb_path = f"{item.get('category')}/{item.get('file_key')}/{safe_id}_{safe_name}.png"

            # components_raw data
            raw_data = (
                item_id,
                item.get("id"),
                item.get("parent_id"),
                json.dumps(item) if item else None,  # raw_json
                thumb_path,  # image_path
                item.get("thumbnail_url"),
                json.dumps({"width": item.get("width"), "height": item.get("height")}) if item.get("width") else None,
                item.get("child_count", 0),
                item.get("source_file"),
                item.get("file_key"),
                item.get("file_name"),
                item.get("page_name"),
                item.get("project_name"),
                item.get("width"),
                item.get("height")
            )
            raw_batch.append(raw_data)

            # Determine device type from dimensions
            width = item.get("width", 0)
            if width >= 1200:
                device_type = "desktop"
            elif width >= 768:
                device_type = "tablet"
            elif width >= 320:
                device_type = "mobile"
            else:
                device_type = "responsive"

            # Build search text
            search_parts = [
                item.get("name", ""),
                item.get("file_name", ""),
                item.get("page_name", ""),
                item.get("project_name", ""),
                item.get("category", ""),
                item.get("subcategory", "")
            ]
            search_text = " ".join(filter(None, search_parts))

            # component_library data
            lib_data = (
                item_id,
                item_id,  # raw_id references components_raw
                item.get("name", f"Unnamed {i}"),
                item.get("level"),  # component_level
                device_type,
                thumb_path,
                item.get("thumbnail_url"),
                item.get("width"),
                item.get("height"),
                item.get("file_key"),
                item.get("file_name"),
                item.get("page_name"),
                item.get("project_name"),
                search_text,
                item.get("category"),  # llm_category
                item.get("subcategory")  # llm_subcategory
            )
            lib_batch.append(lib_data)

            if (i + 1) % 5000 == 0:
                print(f"    Processed {i + 1}/{len(items)}...")

        # Batch insert into components_raw
        print("[*] Inserting into components_raw...")
        execute_batch(cur, """
            INSERT INTO components_raw
            (id, figma_node_id, parent_id, raw_json, image_path, thumbnail_url, bounds,
             child_count, source_file, file_key, file_name, page_name, project_name, width, height)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING
        """, raw_batch, page_size=1000)

        # Batch insert into component_library
        print("[*] Inserting into component_library...")
        execute_batch(cur, """
            INSERT INTO component_library
            (id, raw_id, name, component_level, device_type, thumbnail_path, thumbnail_url,
             width, height, file_key, file_name, page_name, project_name, search_text,
             llm_category, llm_subcategory)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING
        """, lib_batch, page_size=1000)

        conn.commit()

        # Verification
        cur.execute("SELECT COUNT(*) FROM components_raw")
        raw_count = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM component_library")
        lib_count = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM kits")
        kit_count = cur.fetchone()[0]

        print(f"\n[+] Import complete:")
        print(f"    components_raw: {raw_count}")
        print(f"    component_library: {lib_count}")
        print(f"    kits: {kit_count}")

        # Show category distribution
        print("\n[*] Category distribution:")
        cur.execute("""
            SELECT llm_category, COUNT(*)
            FROM component_library
            GROUP BY llm_category
            ORDER BY COUNT(*) DESC
            LIMIT 15
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
    import sys

    json_path = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\under\Downloads\ENTERPRISE_OS_V7\figma_library_v2\ui_library_subcategorized_20260207_220336.json"
    thumbs_dir = r"C:\Users\under\Downloads\ENTERPRISE_OS_V7\figma_library_v2\thumbnails"

    import_library(json_path, thumbs_dir)
