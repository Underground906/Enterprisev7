#!/usr/bin/env python3
"""
Enterprise OS V7 — Search API
FastAPI service for querying the V7 registry and ChromaDB.

Usage:
    python v7_search_api.py
    # or
    uvicorn v7_search_api:app --host 0.0.0.0 --port 8100 --reload

Endpoints:
    GET  /files          - Query v7_files with filters
    GET  /search         - Semantic search via ChromaDB
    GET  /health         - System health summary
    GET  /sessions       - Recent sessions
    GET  /changes        - Audit trail
    GET  /snapshots      - System state history

Port: 8100 (avoids conflict with ui_library search_api on 5000)
"""

import os
import sys
from datetime import datetime, timezone, date
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor
import uvicorn
import json


# ============================================================
# Configuration
# ============================================================

DB_CONFIG = {
    "dbname": "enterprise_os",
    "user": "postgres",
    "host": "localhost",
}

app = FastAPI(
    title="Enterprise OS V7 — Search API",
    description="Query the V7 file registry, sessions, and semantic search",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# Database helpers
# ============================================================

def get_db():
    conn = psycopg2.connect(**DB_CONFIG)
    conn.autocommit = True
    return conn


def json_serializer(obj):
    """Handle datetime serialization for JSON responses."""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")


# ============================================================
# Endpoints
# ============================================================

@app.get("/files")
def list_files(
    component: Optional[str] = Query(None, description="Filter by component (e.g., CORE_ENGINE)"),
    pillar: Optional[str] = Query(None, description="Filter by pillar (e.g., PIL_03_COPY)"),
    project: Optional[str] = Query(None, description="Filter by project (e.g., PRJ_Enterprise_Platform)"),
    file_type: Optional[str] = Query(None, description="Filter by file type (e.g., script, document)"),
    extension: Optional[str] = Query(None, description="Filter by extension (e.g., .md, .py)"),
    q: Optional[str] = Query(None, description="Search filename/title"),
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
):
    """Query the V7 file registry with filters."""
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    conditions = ["is_deleted = FALSE"]
    params = []

    if component:
        conditions.append("component = %s")
        params.append(component)
    if pillar:
        conditions.append("pillar = %s")
        params.append(pillar)
    if project:
        conditions.append("project = %s")
        params.append(project)
    if file_type:
        conditions.append("file_type = %s")
        params.append(file_type)
    if extension:
        conditions.append("extension = %s")
        params.append(extension)
    if q:
        conditions.append("(filename ILIKE %s OR title ILIKE %s)")
        params.extend([f"%{q}%", f"%{q}%"])

    where = " AND ".join(conditions)

    # Get total count
    cur.execute(f"SELECT COUNT(*) as total FROM v7_files WHERE {where}", params)
    total = cur.fetchone()["total"]

    # Get files
    cur.execute(f"""
        SELECT id, relative_path, filename, extension, component, pillar, project,
               file_type, size_bytes, line_count, word_count, title,
               file_modified, first_seen, last_scanned
        FROM v7_files
        WHERE {where}
        ORDER BY relative_path
        LIMIT %s OFFSET %s
    """, params + [limit, offset])

    files = cur.fetchall()
    conn.close()

    return {
        "total": total,
        "limit": limit,
        "offset": offset,
        "files": files,
    }


@app.get("/search")
def semantic_search(
    q: str = Query(..., description="Search query"),
    n_results: int = Query(10, ge=1, le=50),
    component: Optional[str] = None,
    pillar: Optional[str] = None,
):
    """Semantic search via ChromaDB."""
    try:
        import chromadb

        v7_root = find_v7_root()
        chroma_dir = v7_root / "03_CORE_ENGINE" / "CONFIG" / "chromadb_data"

        if not chroma_dir.exists():
            raise HTTPException(
                status_code=503,
                detail="ChromaDB not initialized. Run: python v7_registry.py chromadb-sync",
            )

        client = chromadb.PersistentClient(path=str(chroma_dir))

        try:
            from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
            embed_fn = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
            collection = client.get_collection(name="v7_documents", embedding_function=embed_fn)
        except Exception:
            collection = client.get_collection(name="v7_documents")

        # Build where filter
        where_filter = None
        if component and pillar:
            where_filter = {"$and": [{"component": component}, {"pillar": pillar}]}
        elif component:
            where_filter = {"component": component}
        elif pillar:
            where_filter = {"pillar": pillar}

        results = collection.query(
            query_texts=[q],
            n_results=n_results,
            where=where_filter,
            include=["documents", "metadatas", "distances"],
        )

        hits = []
        if results and results["ids"] and results["ids"][0]:
            for i, doc_id in enumerate(results["ids"][0]):
                hits.append({
                    "id": doc_id,
                    "document": results["documents"][0][i][:300],
                    "metadata": results["metadatas"][0][i],
                    "distance": results["distances"][0][i],
                })

        return {"query": q, "results": hits}

    except ImportError:
        raise HTTPException(
            status_code=503,
            detail="ChromaDB not installed. Run: pip install chromadb",
        )


@app.get("/health")
def health_summary():
    """System health summary from database."""
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    # Total files
    cur.execute("SELECT COUNT(*) as total FROM v7_files WHERE is_deleted = FALSE")
    total = cur.fetchone()["total"]

    # By component
    cur.execute("""
        SELECT component, COUNT(*) as count
        FROM v7_files WHERE is_deleted = FALSE
        GROUP BY component ORDER BY count DESC
    """)
    by_component = {row["component"]: row["count"] for row in cur.fetchall()}

    # By pillar
    cur.execute("""
        SELECT pillar, COUNT(*) as count
        FROM v7_files WHERE is_deleted = FALSE AND pillar IS NOT NULL
        GROUP BY pillar ORDER BY pillar
    """)
    by_pillar = {row["pillar"]: row["count"] for row in cur.fetchall()}

    # Total size
    cur.execute("SELECT SUM(size_bytes) as total_size FROM v7_files WHERE is_deleted = FALSE")
    total_size = cur.fetchone()["total_size"] or 0

    # Stale files
    cur.execute("""
        SELECT COUNT(*) as stale FROM v7_files
        WHERE is_deleted = FALSE AND file_modified < NOW() - INTERVAL '30 days'
    """)
    stale = cur.fetchone()["stale"]

    # Latest snapshot
    cur.execute("SELECT * FROM v7_system_state ORDER BY id DESC LIMIT 1")
    latest_snapshot = cur.fetchone()

    # Active session
    cur.execute("SELECT * FROM v7_sessions WHERE status = 'active' ORDER BY id DESC LIMIT 1")
    active_session = cur.fetchone()

    conn.close()

    return {
        "total_files": total,
        "total_size_mb": round(total_size / (1024 * 1024), 2),
        "stale_files_30d": stale,
        "files_by_component": by_component,
        "files_by_pillar": by_pillar,
        "latest_snapshot": latest_snapshot,
        "active_session": active_session,
    }


@app.get("/sessions")
def list_sessions(
    limit: int = Query(20, ge=1, le=100),
    status: Optional[str] = Query(None, description="Filter: active, complete, abandoned"),
):
    """List recent sessions."""
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    if status:
        cur.execute("""
            SELECT * FROM v7_sessions WHERE status = %s
            ORDER BY id DESC LIMIT %s
        """, (status, limit))
    else:
        cur.execute("SELECT * FROM v7_sessions ORDER BY id DESC LIMIT %s", (limit,))

    sessions = cur.fetchall()
    conn.close()

    return {"sessions": sessions}


@app.get("/changes")
def list_changes(
    since: Optional[str] = Query(None, description="ISO date (YYYY-MM-DD)"),
    change_type: Optional[str] = Query(None, description="created, modified, deleted, renamed"),
    session_id: Optional[int] = None,
    limit: int = Query(100, ge=1, le=1000),
):
    """Audit trail of file changes."""
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    conditions = []
    params = []

    if since:
        conditions.append("changed_at >= %s")
        params.append(since)
    if change_type:
        conditions.append("change_type = %s")
        params.append(change_type)
    if session_id:
        conditions.append("session_id = %s")
        params.append(session_id)

    where = " AND ".join(conditions) if conditions else "TRUE"

    cur.execute(f"""
        SELECT c.*, f.filename, f.component, f.pillar
        FROM v7_changes c
        LEFT JOIN v7_files f ON c.file_id = f.id
        WHERE {where}
        ORDER BY c.changed_at DESC
        LIMIT %s
    """, params + [limit])

    changes = cur.fetchall()
    conn.close()

    return {"changes": changes}


@app.get("/snapshots")
def list_snapshots(limit: int = Query(30, ge=1, le=365)):
    """System state history."""
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""
        SELECT id, snapshot_date, total_files, total_size_mb,
               empty_pillars, stale_files, triggered_by
        FROM v7_system_state
        ORDER BY id DESC LIMIT %s
    """, (limit,))

    snapshots = cur.fetchall()
    conn.close()

    return {"snapshots": snapshots}


@app.get("/stats")
def file_stats():
    """Aggregated file statistics."""
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    # By extension
    cur.execute("""
        SELECT extension, COUNT(*) as count, SUM(size_bytes) as total_size
        FROM v7_files WHERE is_deleted = FALSE
        GROUP BY extension ORDER BY count DESC
    """)
    by_extension = cur.fetchall()

    # By file type
    cur.execute("""
        SELECT file_type, COUNT(*) as count
        FROM v7_files WHERE is_deleted = FALSE
        GROUP BY file_type ORDER BY count DESC
    """)
    by_type = cur.fetchall()

    # Largest files
    cur.execute("""
        SELECT relative_path, size_bytes, file_type
        FROM v7_files WHERE is_deleted = FALSE
        ORDER BY size_bytes DESC LIMIT 20
    """)
    largest = cur.fetchall()

    conn.close()

    return {
        "by_extension": by_extension,
        "by_type": by_type,
        "largest_files": largest,
    }


# ============================================================
# V7 root finder
# ============================================================

def find_v7_root():
    candidates = [
        Path.cwd(),
        Path.cwd() / "ENTERPRISE_OS_V7",
        Path(__file__).parent.parent.parent,
        Path.home() / "Downloads" / "ENTERPRISE_OS_V7",
    ]
    for c in candidates:
        if (c / "00_SYSTEM_ROOT").exists():
            return c
    return None


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    print("Starting Enterprise OS V7 Search API on http://localhost:8100")
    uvicorn.run(app, host="0.0.0.0", port=8100)
