#!/usr/bin/env python3
"""
UI Library Search API

A simple Flask API for searching the UI library.
Supports multi-dimensional filtering and full-text search.

Usage:
    python search_api.py

Endpoints:
    GET /search?q=dashboard&type=navigation&category=admin&limit=50
    GET /types - List component types
    GET /categories - List functional categories
    GET /verticals - List industry verticals
    GET /stats - Library statistics
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = Flask(__name__)
CORS(app)

DB_CONFIG = {
    "dbname": "ui_library",
    "user": "postgres",
    "host": "localhost"
}

THUMBS_BASE = "figma_library_v2/thumbnails"


def get_db():
    """Get database connection."""
    return psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)


@app.route("/search")
def search():
    """
    Search the library with multi-dimensional filtering.

    Query params:
    - q: Full-text search query
    - type: Component type ID
    - section: Section ID
    - category: Functional category ID
    - vertical: Industry vertical ID
    - level: Component level (page, block, component, atom)
    - device: Device type (desktop, tablet, mobile)
    - llm_cat: LLM category (original classification)
    - llm_subcat: LLM subcategory
    - review: Review status (unreviewed, kept, discarded)
    - limit: Max results (default 50, max 200)
    - offset: Pagination offset
    """
    conn = get_db()
    cur = conn.cursor()

    try:
        # Build query
        conditions = []
        params = []

        # Full-text search
        q = request.args.get("q")
        if q:
            conditions.append("search_text ILIKE %s")
            params.append(f"%{q}%")

        # Component type filter
        comp_type = request.args.get("type")
        if comp_type:
            conditions.append("component_type_id = %s")
            params.append(comp_type)

        # Section filter
        section = request.args.get("section")
        if section:
            conditions.append("section_id = %s")
            params.append(section)

        # Functional category filter
        func_cat = request.args.get("category")
        if func_cat:
            conditions.append("functional_category_id = %s")
            params.append(func_cat)

        # Industry vertical filter
        vertical = request.args.get("vertical")
        if vertical:
            conditions.append("industry_vertical_id = %s")
            params.append(vertical)

        # Component level filter
        level = request.args.get("level")
        if level:
            conditions.append("component_level = %s")
            params.append(level)

        # Device type filter
        device = request.args.get("device")
        if device:
            conditions.append("device_type = %s")
            params.append(device)

        # LLM category filter (original)
        llm_cat = request.args.get("llm_cat")
        if llm_cat:
            conditions.append("llm_category = %s")
            params.append(llm_cat)

        # LLM subcategory filter
        llm_subcat = request.args.get("llm_subcat")
        if llm_subcat:
            conditions.append("llm_subcategory = %s")
            params.append(llm_subcat)

        # Review status filter
        review = request.args.get("review")
        if review:
            conditions.append("review_status = %s")
            params.append(review)

        # Kit category filter (Figma project group)
        kit_cat = request.args.get("kit_category")
        if kit_cat:
            conditions.append("cl.file_key IN (SELECT file_key FROM kits WHERE project_name = %s)")
            params.append(kit_cat)

        # Pagination
        limit = min(int(request.args.get("limit", 50)), 200)
        offset = int(request.args.get("offset", 0))

        # Build WHERE clause
        where = ""
        if conditions:
            where = "WHERE " + " AND ".join(conditions)

        # Execute query
        query = f"""
            SELECT
                cl.id,
                cl.name,
                cl.component_type_id,
                ct.name as component_type_name,
                cl.section_id,
                cl.functional_category_id,
                fc.name as functional_category_name,
                cl.component_level,
                cl.device_type,
                cl.thumbnail_path,
                cl.thumbnail_url,
                cl.width,
                cl.height,
                cl.file_key,
                cl.file_name,
                cl.page_name,
                cl.llm_category,
                cl.llm_subcategory,
                cl.review_status,
                cl.matched_component_name_id
            FROM component_library cl
            LEFT JOIN component_types ct ON cl.component_type_id = ct.id
            LEFT JOIN functional_categories fc ON cl.functional_category_id = fc.id
            {where}
            ORDER BY cl.name
            LIMIT %s OFFSET %s
        """
        params.extend([limit, offset])

        cur.execute(query, params)
        results = cur.fetchall()

        # Get total count
        count_query = f"SELECT COUNT(*) as total FROM component_library {where}"
        cur.execute(count_query, params[:-2] if params else [])
        total = cur.fetchone()["total"]

        return jsonify({
            "results": [dict(r) for r in results],
            "total": total,
            "limit": limit,
            "offset": offset
        })

    finally:
        cur.close()
        conn.close()


@app.route("/types")
def list_types():
    """List all component types with counts."""
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT
                ct.id,
                ct.name,
                ct.section_count,
                ct.total_component_names,
                COUNT(cl.id) as library_count
            FROM component_types ct
            LEFT JOIN component_library cl ON ct.id = cl.component_type_id
            GROUP BY ct.id, ct.name, ct.section_count, ct.total_component_names
            ORDER BY library_count DESC
        """)
        return jsonify([dict(r) for r in cur.fetchall()])
    finally:
        cur.close()
        conn.close()


@app.route("/types/<type_id>/sections")
def list_sections(type_id):
    """List sections for a component type."""
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT
                s.id,
                s.name,
                s.direct_component_count,
                s.subsection_count,
                COUNT(cl.id) as library_count
            FROM component_type_sections s
            LEFT JOIN component_library cl ON s.id = cl.section_id
            WHERE s.component_type_id = %s
            GROUP BY s.id, s.name, s.direct_component_count, s.subsection_count
            ORDER BY library_count DESC
        """, (type_id,))
        return jsonify([dict(r) for r in cur.fetchall()])
    finally:
        cur.close()
        conn.close()


@app.route("/categories")
def list_categories():
    """List all functional categories with counts."""
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT
                fc.id,
                fc.name,
                fc.example_pages,
                COUNT(cl.id) as library_count
            FROM functional_categories fc
            LEFT JOIN component_library cl ON fc.id = cl.functional_category_id
            GROUP BY fc.id, fc.name, fc.example_pages
            ORDER BY library_count DESC
        """)
        return jsonify([dict(r) for r in cur.fetchall()])
    finally:
        cur.close()
        conn.close()


@app.route("/verticals")
def list_verticals():
    """List all industry verticals."""
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT
                iv.id,
                iv.name,
                iv.specialized_pages,
                COUNT(cl.id) as library_count
            FROM industry_verticals iv
            LEFT JOIN component_library cl ON iv.id = cl.industry_vertical_id
            GROUP BY iv.id, iv.name, iv.specialized_pages
            ORDER BY library_count DESC
        """)
        return jsonify([dict(r) for r in cur.fetchall()])
    finally:
        cur.close()
        conn.close()


@app.route("/kits")
def list_kits():
    """List all kits with item counts."""
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT
                file_key,
                file_name,
                project_name,
                item_count,
                quality_rating,
                niche
            FROM kits
            ORDER BY item_count DESC
            LIMIT 100
        """)
        return jsonify([dict(r) for r in cur.fetchall()])
    finally:
        cur.close()
        conn.close()


@app.route("/kit-categories")
def list_kit_categories():
    """List all kit categories (Figma project groups) with counts."""
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT
                k.project_name,
                COUNT(DISTINCT k.file_key) as kit_count,
                COUNT(cl.id) as item_count
            FROM kits k
            LEFT JOIN component_library cl ON k.file_key = cl.file_key
            WHERE k.project_name IS NOT NULL AND k.project_name != ''
            GROUP BY k.project_name
            ORDER BY item_count DESC
        """)
        return jsonify([dict(r) for r in cur.fetchall()])
    finally:
        cur.close()
        conn.close()


@app.route("/stats")
def stats():
    """Get library statistics."""
    conn = get_db()
    cur = conn.cursor()

    try:
        stats = {}

        cur.execute("SELECT COUNT(*) as cnt FROM component_library")
        stats["total_items"] = cur.fetchone()["cnt"]

        cur.execute("SELECT COUNT(*) as cnt FROM component_types")
        stats["component_types"] = cur.fetchone()["cnt"]

        cur.execute("SELECT COUNT(*) as cnt FROM component_type_sections")
        stats["sections"] = cur.fetchone()["cnt"]

        cur.execute("SELECT COUNT(*) as cnt FROM component_names")
        stats["canonical_names"] = cur.fetchone()["cnt"]

        cur.execute("SELECT COUNT(*) as cnt FROM kits")
        stats["kits"] = cur.fetchone()["cnt"]

        cur.execute("SELECT COUNT(*) as cnt FROM component_library WHERE component_type_id IS NOT NULL")
        stats["items_with_type"] = cur.fetchone()["cnt"]

        cur.execute("SELECT COUNT(*) as cnt FROM component_library WHERE matched_component_name_id IS NOT NULL")
        stats["items_matched_to_canonical"] = cur.fetchone()["cnt"]

        cur.execute("SELECT COUNT(*) as cnt FROM component_library WHERE review_status = 'kept'")
        stats["items_kept"] = cur.fetchone()["cnt"]

        cur.execute("SELECT COUNT(*) as cnt FROM component_library WHERE review_status = 'discarded'")
        stats["items_discarded"] = cur.fetchone()["cnt"]

        return jsonify(stats)
    finally:
        cur.close()
        conn.close()


@app.route("/item/<item_id>")
def get_item(item_id):
    """Get full details for a single item."""
    conn = get_db()
    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT
                cl.*,
                ct.name as component_type_name,
                fc.name as functional_category_name,
                iv.name as industry_vertical_name,
                cn.name as matched_canonical_name
            FROM component_library cl
            LEFT JOIN component_types ct ON cl.component_type_id = ct.id
            LEFT JOIN functional_categories fc ON cl.functional_category_id = fc.id
            LEFT JOIN industry_verticals iv ON cl.industry_vertical_id = iv.id
            LEFT JOIN component_names cn ON cl.matched_component_name_id = cn.id
            WHERE cl.id = %s
        """, (item_id,))

        result = cur.fetchone()
        if result:
            return jsonify(dict(result))
        return jsonify({"error": "Item not found"}), 404
    finally:
        cur.close()
        conn.close()


@app.route("/item/<item_id>/review", methods=["POST"])
def review_item(item_id):
    """Update review status for an item."""
    conn = get_db()
    cur = conn.cursor()

    try:
        data = request.get_json()
        status = data.get("status")

        if status not in ["unreviewed", "kept", "discarded", "flagged"]:
            return jsonify({"error": "Invalid status"}), 400

        cur.execute("""
            UPDATE component_library
            SET review_status = %s, updated_at = NOW()
            WHERE id = %s
        """, (status, item_id))
        conn.commit()

        return jsonify({"success": True, "status": status})
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    print("\n" + "="*60)
    print("UI Library Search API")
    print("="*60)
    print("\nEndpoints:")
    print("  GET /search?q=dashboard&type=navigation&limit=50")
    print("  GET /types")
    print("  GET /types/<type_id>/sections")
    print("  GET /categories")
    print("  GET /verticals")
    print("  GET /kits")
    print("  GET /stats")
    print("  GET /item/<item_id>")
    print("  POST /item/<item_id>/review")
    print("\n" + "="*60 + "\n")

    app.run(host="0.0.0.0", port=5000, debug=True)
