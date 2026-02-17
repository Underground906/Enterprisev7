#!/usr/bin/env python3
"""
Enterprise OS V7 — System Registry
Single CLI tool for file tracking, session management, and system health.

Usage:
    python v7_registry.py scan                          # Full scan, populate v7_files
    python v7_registry.py scan --diff                   # Show what changed since last scan
    python v7_registry.py health                        # System health report
    python v7_registry.py stale [--days 30]             # List files past freshness threshold
    python v7_registry.py snapshot                      # Take system state snapshot
    python v7_registry.py session start "description"   # Start work session
    python v7_registry.py session end                   # End work session
    python v7_registry.py session log "message"         # Log to current session
    python v7_registry.py session status                # Show current session
    python v7_registry.py chromadb-sync                 # Sync markdown to ChromaDB

Database: enterprise_os (PostgreSQL, localhost)
"""

import os
import sys
import json
import hashlib
import argparse
from datetime import datetime, timezone, timedelta
from pathlib import Path
from collections import defaultdict

import psycopg2
from psycopg2.extras import RealDictCursor, execute_batch


# ============================================================
# Configuration
# ============================================================

DB_CONFIG = {
    "dbname": "enterprise_os",
    "user": "postgres",
    "host": "localhost",
}

SKIP_DIRS = {
    "V7_ARCHIVE",
    "90_ARCHIVE",
    "node_modules",
    ".next",
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    "figma_library_v2",
    "chromadb_data",
}

SKIP_EXTENSIONS = {".pyc", ".pyo", ".DS_Store", ".tmp", ".bak", ".lock"}

# Component mapping from top-level folder name
COMPONENT_MAP = {
    "00_SYSTEM_ROOT": "SYSTEM_ROOT",
    "01_NAVIGATION_CENTRE": "NAVIGATION",
    "02_COMMAND_DECK": "COMMAND_DECK",
    "03_CORE_ENGINE": "CORE_ENGINE",
    "04_KNOWLEDGE_LIBRARY": "KNOWLEDGE_LIBRARY",
    "05_TEMPLATE_HUB": "TEMPLATE_HUB",
    "06_DOMAIN_PILLARS": "DOMAIN_PILLARS",
    "07_BUILD_FACTORY": "BUILD_FACTORY",
    "08_OPERATIONS": "OPERATIONS",
}

# File type classification (matches generate_indices.py patterns)
FILE_TYPE_RULES = [
    (lambda n, e: n in ("README.MD", "DOCS.MD", "CONTEXT.MD"), "context_doc"),
    (lambda n, e: n in ("ANALYSIS.MD", "ROUTING_RULES.MD"), "analysis_doc"),
    (lambda n, e: "CANON" in n or "MASTER" in n, "canon_doc"),
    (lambda n, e: "TEMPLATE" in n, "template"),
    (lambda n, e: "PRD" in n, "prd"),
    (lambda n, e: "INDEX" in n or "REGISTRY" in n or "MANIFEST" in n, "index"),
    (lambda n, e: e == ".py", "script"),
    (lambda n, e: e == ".ps1", "script"),
    (lambda n, e: e == ".sql", "schema"),
    (lambda n, e: e == ".json", "data"),
    (lambda n, e: e in (".yaml", ".yml"), "config"),
    (lambda n, e: e == ".html", "web"),
    (lambda n, e: e == ".css", "style"),
    (lambda n, e: e in (".js", ".jsx", ".ts", ".tsx"), "code"),
    (lambda n, e: e == ".md", "document"),
]


# ============================================================
# Root finder (matches existing pattern)
# ============================================================

def find_root(provided_root=None):
    """Find the ENTERPRISE_OS_V7 root directory."""
    if provided_root:
        p = Path(provided_root)
        if (p / "00_SYSTEM_ROOT").exists():
            return p
        print(f"ERROR: {p} does not contain 00_SYSTEM_ROOT")
        sys.exit(1)

    candidates = [
        Path.cwd(),
        Path.cwd() / "ENTERPRISE_OS_V7",
        Path(__file__).parent.parent.parent,
        Path.home() / "Downloads" / "ENTERPRISE_OS_V7",
        Path.home() / "ENTERPRISE_OS_V7",
        Path.home() / "Documents" / "ENTERPRISE_OS_V7",
    ]
    for c in candidates:
        if (c / "00_SYSTEM_ROOT").exists():
            return c

    print("ERROR: Could not find ENTERPRISE_OS_V7 root directory.")
    print("Run with: python v7_registry.py --root /path/to/ENTERPRISE_OS_V7")
    sys.exit(1)


# ============================================================
# Database connection
# ============================================================

def get_db():
    """Get a database connection."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        conn.autocommit = False
        return conn
    except psycopg2.OperationalError as e:
        print(f"ERROR: Cannot connect to database 'enterprise_os': {e}")
        print("Make sure PostgreSQL is running and the database exists.")
        sys.exit(1)


# ============================================================
# File scanning
# ============================================================

def should_skip(path: Path) -> bool:
    """Check if a path should be skipped during scanning."""
    for part in path.parts:
        if part in SKIP_DIRS:
            return True
    if path.suffix in SKIP_EXTENSIONS:
        return True
    # Skip hidden files
    if path.name.startswith(".") and path.name != ".gitignore":
        return True
    return False


def compute_hash(file_path: Path) -> str:
    """SHA-256 hash of file contents."""
    h = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()
    except (PermissionError, OSError):
        return "ERROR_READING"


def extract_title(file_path: Path) -> str:
    """Extract the first markdown heading from a file."""
    if file_path.suffix.lower() != ".md":
        return None
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                line = line.strip()
                if line.startswith("# "):
                    title = sanitize_text(line[2:].strip()[:200])
                    return title
        return None
    except (PermissionError, OSError):
        return None


def sanitize_text(text: str) -> str:
    """Remove NUL bytes and other problematic characters for PostgreSQL."""
    if text is None:
        return None
    return text.replace("\x00", "").replace("\0", "")


def extract_summary(file_path: Path) -> str:
    """Extract first 500 chars of readable content."""
    text_exts = {".md", ".txt", ".py", ".sql", ".json", ".yaml", ".yml", ".html", ".css", ".js", ".ts", ".tsx", ".jsx"}
    if file_path.suffix.lower() not in text_exts:
        return None
    try:
        if file_path.stat().st_size > 10 * 1024 * 1024:
            return None
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read(500)
        content = sanitize_text(content)
        return content.strip() if content and content.strip() else None
    except (PermissionError, OSError, MemoryError):
        return None


def count_lines_words(file_path: Path) -> tuple:
    """Count lines and words in text files. Skips files > 10MB."""
    text_exts = {".md", ".txt", ".py", ".sql", ".json", ".yaml", ".yml", ".html", ".css", ".js", ".ts", ".tsx", ".jsx"}
    if file_path.suffix.lower() not in text_exts:
        return None, None
    try:
        size = file_path.stat().st_size
        if size > 10 * 1024 * 1024:  # Skip files > 10MB
            return None, None
        lines = 0
        words = 0
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                lines += 1
                words += len(line.split())
        return lines, words
    except (PermissionError, OSError, MemoryError):
        return None, None


def identify_component(rel_path: str) -> str:
    """Identify which top-level component a file belongs to."""
    parts = rel_path.replace("\\", "/").split("/")
    if parts:
        return COMPONENT_MAP.get(parts[0], "UNKNOWN")
    return "ROOT"


def identify_pillar(rel_path: str) -> str:
    """Identify which pillar a file belongs to (if any)."""
    parts = rel_path.replace("\\", "/").split("/")
    for part in parts:
        if part.startswith("PIL_"):
            return part
    return None


def identify_project(rel_path: str) -> str:
    """Identify which project a file belongs to (if any)."""
    parts = rel_path.replace("\\", "/").split("/")
    for part in parts:
        if part.startswith("PRJ_"):
            return part
    return None


def classify_file(file_path: Path) -> str:
    """Classify a file by its type/purpose."""
    name = file_path.name.upper()
    ext = file_path.suffix.lower()
    for rule_fn, file_type in FILE_TYPE_RULES:
        if rule_fn(name, ext):
            return file_type
    return "other"


def scan_filesystem(root: Path) -> list:
    """Scan all files in V7, returning metadata dicts."""
    files = []
    print(f"Scanning: {root}")

    for file_path in sorted(root.rglob("*")):
        if not file_path.is_file():
            continue
        if should_skip(file_path):
            continue

        rel_path = str(file_path.relative_to(root)).replace("\\", "/")
        stat = file_path.stat()
        lines, words = count_lines_words(file_path)

        files.append({
            "relative_path": rel_path,
            "filename": file_path.name,
            "extension": file_path.suffix.lower() or None,
            "component": identify_component(rel_path),
            "pillar": identify_pillar(rel_path),
            "project": identify_project(rel_path),
            "file_type": classify_file(file_path),
            "content_hash": compute_hash(file_path),
            "size_bytes": stat.st_size,
            "line_count": lines,
            "word_count": words,
            "title": extract_title(file_path),
            "summary": extract_summary(file_path),
            "file_modified": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc),
        })

    return files


# ============================================================
# Database operations
# ============================================================

def upsert_files(conn, files: list) -> dict:
    """Insert or update files in v7_files. Returns change stats."""
    cur = conn.cursor(cursor_factory=RealDictCursor)

    # Get existing files from DB
    cur.execute("SELECT id, relative_path, content_hash, size_bytes FROM v7_files WHERE is_deleted = FALSE")
    existing = {row["relative_path"]: row for row in cur.fetchall()}

    stats = {"new": 0, "modified": 0, "unchanged": 0, "deleted": 0}
    new_paths = set()
    changes = []

    for f in files:
        new_paths.add(f["relative_path"])
        ex = existing.get(f["relative_path"])

        if ex is None:
            # New file
            cur.execute("""
                INSERT INTO v7_files (relative_path, filename, extension, component, pillar, project,
                    file_type, content_hash, size_bytes, line_count, word_count, title, summary,
                    file_modified, first_seen, last_scanned)
                VALUES (%(relative_path)s, %(filename)s, %(extension)s, %(component)s, %(pillar)s,
                    %(project)s, %(file_type)s, %(content_hash)s, %(size_bytes)s, %(line_count)s,
                    %(word_count)s, %(title)s, %(summary)s, %(file_modified)s, NOW(), NOW())
            """, f)
            stats["new"] += 1
            changes.append(("created", f["relative_path"], None, f["content_hash"]))

        elif ex["content_hash"] != f["content_hash"]:
            # Modified file
            cur.execute("""
                UPDATE v7_files SET
                    filename = %(filename)s, extension = %(extension)s, component = %(component)s,
                    pillar = %(pillar)s, project = %(project)s, file_type = %(file_type)s,
                    content_hash = %(content_hash)s, size_bytes = %(size_bytes)s,
                    line_count = %(line_count)s, word_count = %(word_count)s,
                    title = %(title)s, summary = %(summary)s,
                    file_modified = %(file_modified)s, last_scanned = NOW()
                WHERE relative_path = %(relative_path)s
            """, f)
            stats["modified"] += 1
            changes.append(("modified", f["relative_path"], ex["content_hash"], f["content_hash"]))

        else:
            # Unchanged
            cur.execute("""
                UPDATE v7_files SET last_scanned = NOW()
                WHERE relative_path = %(relative_path)s
            """, {"relative_path": f["relative_path"]})
            stats["unchanged"] += 1

    # Mark deleted files
    for path, row in existing.items():
        if path not in new_paths:
            cur.execute("""
                UPDATE v7_files SET is_deleted = TRUE, deleted_at = NOW()
                WHERE id = %s
            """, (row["id"],))
            stats["deleted"] += 1
            changes.append(("deleted", path, row["content_hash"], None))

    conn.commit()
    return stats, changes


def log_changes(conn, changes: list, session_id: int = None):
    """Write changes to v7_changes table."""
    if not changes:
        return

    cur = conn.cursor(cursor_factory=RealDictCursor)

    for change_type, path, old_hash, new_hash in changes:
        # Look up file_id
        cur.execute("SELECT id FROM v7_files WHERE relative_path = %s", (path,))
        row = cur.fetchone()
        file_id = row["id"] if row else None

        cur.execute("""
            INSERT INTO v7_changes (session_id, file_id, relative_path, change_type,
                old_hash, new_hash, detected_by)
            VALUES (%s, %s, %s, %s, %s, %s, 'scan')
        """, (session_id, file_id, path, change_type, old_hash, new_hash))

    conn.commit()


# ============================================================
# Commands
# ============================================================

def cmd_scan(root: Path, diff_only: bool = False):
    """Full filesystem scan → database."""
    files = scan_filesystem(root)
    print(f"Found {len(files)} files (excluding skipped dirs)")

    conn = get_db()

    if diff_only:
        # Compare against DB without writing
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT relative_path, content_hash, size_bytes FROM v7_files WHERE is_deleted = FALSE")
        existing = {row["relative_path"]: row for row in cur.fetchall()}

        new_files = []
        modified = []
        deleted = []
        unchanged = 0

        scanned_paths = set()
        for f in files:
            scanned_paths.add(f["relative_path"])
            ex = existing.get(f["relative_path"])
            if ex is None:
                new_files.append(f["relative_path"])
            elif ex["content_hash"] != f["content_hash"]:
                modified.append(f["relative_path"])
            else:
                unchanged += 1

        for path in existing:
            if path not in scanned_paths:
                deleted.append(path)

        print(f"\n{'='*60}")
        print(f"DIFF REPORT (scan vs database)")
        print(f"{'='*60}")
        print(f"  New files:       {len(new_files)}")
        print(f"  Modified files:  {len(modified)}")
        print(f"  Deleted files:   {len(deleted)}")
        print(f"  Unchanged:       {unchanged}")
        print()

        if new_files:
            print("NEW FILES:")
            for p in new_files[:50]:
                print(f"  + {p}")
            if len(new_files) > 50:
                print(f"  ... and {len(new_files) - 50} more")
            print()

        if modified:
            print("MODIFIED FILES:")
            for p in modified[:50]:
                print(f"  ~ {p}")
            if len(modified) > 50:
                print(f"  ... and {len(modified) - 50} more")
            print()

        if deleted:
            print("DELETED FILES:")
            for p in deleted[:50]:
                print(f"  - {p}")
            if len(deleted) > 50:
                print(f"  ... and {len(deleted) - 50} more")
            print()

        conn.close()
        return

    # Full scan — upsert into DB
    stats, changes = upsert_files(conn, files)

    # Get active session for change logging
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT id FROM v7_sessions WHERE status = 'active' ORDER BY id DESC LIMIT 1")
    session_row = cur.fetchone()
    session_id = session_row["id"] if session_row else None

    log_changes(conn, changes, session_id)

    print(f"\n{'='*60}")
    print(f"SCAN COMPLETE")
    print(f"{'='*60}")
    print(f"  Total files scanned: {len(files)}")
    print(f"  New:                 {stats['new']}")
    print(f"  Modified:            {stats['modified']}")
    print(f"  Unchanged:           {stats['unchanged']}")
    print(f"  Deleted (marked):    {stats['deleted']}")
    print()

    conn.close()


def cmd_health(root: Path):
    """Generate system health report from database."""
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    # Total files
    cur.execute("SELECT COUNT(*) as total FROM v7_files WHERE is_deleted = FALSE")
    total = cur.fetchone()["total"]

    if total == 0:
        print("No files in database. Run 'v7_registry.py scan' first.")
        conn.close()
        return

    # By component
    cur.execute("""
        SELECT component, COUNT(*) as count
        FROM v7_files WHERE is_deleted = FALSE
        GROUP BY component ORDER BY count DESC
    """)
    by_component = cur.fetchall()

    # By file type
    cur.execute("""
        SELECT file_type, COUNT(*) as count
        FROM v7_files WHERE is_deleted = FALSE
        GROUP BY file_type ORDER BY count DESC
    """)
    by_type = cur.fetchall()

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

    # Stale files (30+ days)
    cur.execute("""
        SELECT COUNT(*) as stale
        FROM v7_files
        WHERE is_deleted = FALSE AND file_modified < NOW() - INTERVAL '30 days'
    """)
    stale_count = cur.fetchone()["stale"]

    # Recent changes
    cur.execute("""
        SELECT change_type, COUNT(*) as count
        FROM v7_changes
        WHERE changed_at > NOW() - INTERVAL '7 days'
        GROUP BY change_type
    """)
    recent_changes = {row["change_type"]: row["count"] for row in cur.fetchall()}

    # All 23 pillars — check which have files
    all_pillars = [
        "PIL_01_AVATARS", "PIL_02_BRANDING", "PIL_03_COPY", "PIL_04_CONTENT",
        "PIL_05_GRAPHICS", "PIL_06_VIDEO", "PIL_07_UI_LIBRARY",
        "PIL_08_KNOWLEDGE_INGESTION", "PIL_09_ROLES_SKILLS", "PIL_10_WORKING_PRACTICES",
        "PIL_11_BUILD_STORY", "PIL_12_KEYWORDS", "PIL_13_SEO", "PIL_14_NAVIGATION",
        "PIL_15_ENTERPRISE_OS", "PIL_16_CONTENT_GENERATION", "PIL_17_RAG_SYSTEM",
        "PIL_18_AGENT_FRAMEWORK", "PIL_19_PROPERTY", "PIL_20_FITNESS",
        "PIL_21_MARKET_RESEARCH", "PIL_22_VOICE_TRAINING", "PIL_23_DOG_PLATFORM",
    ]
    empty_pillars = [p for p in all_pillars if by_pillar.get(p, 0) == 0]

    # Print report
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"\n{'='*60}")
    print(f"SYSTEM HEALTH REPORT — {now}")
    print(f"{'='*60}")
    print(f"\n  Total files:        {total}")
    print(f"  Total size:         {total_size / (1024*1024):.1f} MB")
    print(f"  Stale (30+ days):   {stale_count}")
    print(f"  Empty pillars:      {len(empty_pillars)} / 23")

    if recent_changes:
        print(f"\n  Changes (last 7 days):")
        for ct, cnt in recent_changes.items():
            print(f"    {ct}: {cnt}")

    print(f"\n--- Files by Component ---")
    for row in by_component:
        print(f"  {row['component']:25s} {row['count']:>5}")

    print(f"\n--- Files by Type ---")
    for row in by_type:
        print(f"  {row['file_type']:25s} {row['count']:>5}")

    print(f"\n--- Pillar Status ---")
    for p in all_pillars:
        count = by_pillar.get(p, 0)
        status = "EMPTY" if count == 0 else f"{count} files"
        marker = "  " if count > 0 else "!!"
        print(f"  {marker} {p:35s} {status}")

    if empty_pillars:
        print(f"\n--- Action Items ---")
        for p in empty_pillars:
            print(f"  !! {p} — needs content")

    # Write report to file
    report_path = root / "03_CORE_ENGINE" / "INDICES" / "SYSTEM_HEALTH.md"
    report = f"# SYSTEM HEALTH REPORT\n\n"
    report += f"**Generated:** {now}\n\n"
    report += f"| Metric | Value |\n|--------|-------|\n"
    report += f"| Total files | {total} |\n"
    report += f"| Total size | {total_size / (1024*1024):.1f} MB |\n"
    report += f"| Stale files (30+ days) | {stale_count} |\n"
    report += f"| Empty pillars | {len(empty_pillars)} / 23 |\n\n"

    report += f"## Files by Component\n\n| Component | Count |\n|-----------|-------|\n"
    for row in by_component:
        report += f"| {row['component']} | {row['count']} |\n"

    report += f"\n## Files by Type\n\n| Type | Count |\n|------|-------|\n"
    for row in by_type:
        report += f"| {row['file_type']} | {row['count']} |\n"

    report += f"\n## Pillar Status\n\n| Pillar | Files | Status |\n|--------|-------|--------|\n"
    for p in all_pillars:
        count = by_pillar.get(p, 0)
        status = "EMPTY" if count == 0 else "Active"
        report += f"| {p} | {count} | {status} |\n"

    report += f"\n---\n*Generated by v7_registry.py*\n"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\nReport written to: {report_path.relative_to(root)}")

    conn.close()


def cmd_stale(root: Path, days: int = 30):
    """List files not modified in N days."""
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""
        SELECT relative_path, file_type, component, pillar,
               file_modified, size_bytes
        FROM v7_files
        WHERE is_deleted = FALSE
          AND file_modified < NOW() - INTERVAL '%s days'
        ORDER BY file_modified ASC
    """, (days,))

    rows = cur.fetchall()
    print(f"\n{'='*60}")
    print(f"STALE FILES (not modified in {days}+ days)")
    print(f"{'='*60}")
    print(f"  Found: {len(rows)} files\n")

    if rows:
        for row in rows[:100]:
            age = (datetime.now(timezone.utc) - row["file_modified"]).days
            print(f"  [{age:>4}d] {row['relative_path']}")

        if len(rows) > 100:
            print(f"\n  ... and {len(rows) - 100} more")

    conn.close()


def cmd_snapshot(root: Path):
    """Take a system state snapshot and store in DB."""
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    # Gather stats
    cur.execute("SELECT COUNT(*) as total FROM v7_files WHERE is_deleted = FALSE")
    total = cur.fetchone()["total"]

    cur.execute("SELECT SUM(size_bytes) as total_size FROM v7_files WHERE is_deleted = FALSE")
    total_size = cur.fetchone()["total_size"] or 0

    cur.execute("""
        SELECT component, COUNT(*) as count
        FROM v7_files WHERE is_deleted = FALSE
        GROUP BY component
    """)
    by_component = {row["component"]: row["count"] for row in cur.fetchall()}

    cur.execute("""
        SELECT file_type, COUNT(*) as count
        FROM v7_files WHERE is_deleted = FALSE
        GROUP BY file_type
    """)
    by_type = {row["file_type"]: row["count"] for row in cur.fetchall()}

    cur.execute("""
        SELECT pillar, COUNT(*) as count
        FROM v7_files WHERE is_deleted = FALSE AND pillar IS NOT NULL
        GROUP BY pillar
    """)
    by_pillar = {row["pillar"]: row["count"] for row in cur.fetchall()}

    all_pillars = [
        "PIL_01_AVATARS", "PIL_02_BRANDING", "PIL_03_COPY", "PIL_04_CONTENT",
        "PIL_05_GRAPHICS", "PIL_06_VIDEO", "PIL_07_UI_LIBRARY",
        "PIL_08_KNOWLEDGE_INGESTION", "PIL_09_ROLES_SKILLS", "PIL_10_WORKING_PRACTICES",
        "PIL_11_BUILD_STORY", "PIL_12_KEYWORDS", "PIL_13_SEO", "PIL_14_NAVIGATION",
        "PIL_15_ENTERPRISE_OS", "PIL_16_CONTENT_GENERATION", "PIL_17_RAG_SYSTEM",
        "PIL_18_AGENT_FRAMEWORK", "PIL_19_PROPERTY", "PIL_20_FITNESS",
        "PIL_21_MARKET_RESEARCH", "PIL_22_VOICE_TRAINING", "PIL_23_DOG_PLATFORM",
    ]
    empty_count = sum(1 for p in all_pillars if by_pillar.get(p, 0) == 0)

    cur.execute("""
        SELECT COUNT(*) as stale FROM v7_files
        WHERE is_deleted = FALSE AND file_modified < NOW() - INTERVAL '30 days'
    """)
    stale = cur.fetchone()["stale"]

    # Get active session
    cur.execute("SELECT id FROM v7_sessions WHERE status = 'active' ORDER BY id DESC LIMIT 1")
    session_row = cur.fetchone()
    session_id = session_row["id"] if session_row else None

    # Insert snapshot
    cur.execute("""
        INSERT INTO v7_system_state
            (snapshot_date, total_files, total_size_mb,
             files_by_component, files_by_type, files_by_pillar,
             empty_pillars, stale_files, session_id, triggered_by)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id
    """, (
        datetime.now().date(), total, round(total_size / (1024*1024), 2),
        json.dumps(by_component), json.dumps(by_type), json.dumps(by_pillar),
        empty_count, stale, session_id, "manual",
    ))
    snap_id = cur.fetchone()["id"]
    conn.commit()

    print(f"[OK] Snapshot #{snap_id} saved")
    print(f"  Total files:     {total}")
    print(f"  Total size:      {round(total_size / (1024*1024), 2)} MB")
    print(f"  Empty pillars:   {empty_count}")
    print(f"  Stale files:     {stale}")

    conn.close()


# ============================================================
# Session management
# ============================================================

def get_state_file(root: Path) -> Path:
    return root / "02_COMMAND_DECK" / ".current_session.json"


def get_current_session(root: Path) -> dict:
    state = get_state_file(root)
    if state.exists():
        with open(state) as f:
            return json.load(f)
    return None


def save_session_state(root: Path, data: dict):
    with open(get_state_file(root), "w") as f:
        json.dump(data, f, indent=2)


def clear_session_state(root: Path):
    state = get_state_file(root)
    if state.exists():
        state.unlink()


def cmd_session_start(root: Path, description: str):
    """Start a new work session."""
    current = get_current_session(root)
    if current:
        print(f"[!] Session already active: {current['description']}")
        print(f"    Started: {current['start_time']}")
        print(f"    Use 'v7_registry.py session end' first.")
        return

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    month = now.strftime("%Y-%m")
    now_str = now.strftime("%Y-%m-%d %H:%M")

    # Create session in DB
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    # Find next session number for today
    cur.execute("SELECT COALESCE(MAX(session_number), 0) + 1 as next FROM v7_sessions WHERE date = %s", (date,))
    num = cur.fetchone()["next"]

    cur.execute("""
        INSERT INTO v7_sessions (date, session_number, description, started_at, status)
        VALUES (%s, %s, %s, NOW(), 'active')
        RETURNING id
    """, (date, num, description))
    session_id = cur.fetchone()["id"]
    conn.commit()
    conn.close()

    # Create markdown log (compatible with session_logger.py format)
    sessions_dir = root / "02_COMMAND_DECK" / "ACTIVE_SESSIONS" / month
    sessions_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{date}_session_{num:02d}.md"
    filepath = sessions_dir / filename

    log_content = f"""# SESSION LOG — {date} #{num}

**Start:** {now_str}
**Intent:** {description}
**Status:** Active
**DB Session ID:** {session_id}

---

## Work Log

- [{now_str}] Session started: {description}
"""
    with open(filepath, "w") as f:
        f.write(log_content)

    # Save state
    save_session_state(root, {
        "session_id": session_id,
        "file": str(filepath),
        "description": description,
        "start_time": now_str,
        "session_number": num,
        "log_count": 0,
    })

    # Quick diff
    print(f"[OK] Session #{num} started: {description}")
    print(f"     DB ID: {session_id}")
    print(f"     Log: {filepath.relative_to(root)}")

    # Show last session summary
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
        SELECT description, date, session_number, files_created, files_modified
        FROM v7_sessions
        WHERE status = 'complete'
        ORDER BY id DESC LIMIT 1
    """)
    last = cur.fetchone()
    if last:
        print(f"\n     Last session: {last['date']} #{last['session_number']} — {last['description']}")
        if last["files_created"] or last["files_modified"]:
            print(f"       Created: {last['files_created']}, Modified: {last['files_modified']}")
    conn.close()


def cmd_session_log(root: Path, message: str, file_path: str = None, action: str = None):
    """Log an entry to the current session."""
    current = get_current_session(root)
    if not current:
        print("[!] No active session. Use 'v7_registry.py session start \"description\"' first.")
        return

    filepath = Path(current["file"])
    if not filepath.exists():
        print(f"ERROR: Session file missing: {filepath}")
        clear_session_state(root)
        return

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"- [{now_str}] {message}"
    if file_path:
        entry += f" (file: {file_path}"
        if action:
            entry += f", action: {action}"
        entry += ")"
    entry += "\n"

    with open(filepath, "a") as f:
        f.write(entry)

    current["log_count"] = current.get("log_count", 0) + 1
    save_session_state(root, current)

    # If file action specified, log to v7_changes
    if file_path and action:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO v7_changes (session_id, relative_path, change_type, description, detected_by)
            VALUES (%s, %s, %s, %s, 'session_log')
        """, (current["session_id"], file_path, action, message))
        conn.commit()
        conn.close()

    print(f"[OK] Logged: {message}")


def cmd_session_end(root: Path):
    """End the current session."""
    current = get_current_session(root)
    if not current:
        print("[!] No active session to end.")
        return

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    filepath = Path(current["file"])

    # Run a quick diff to catch unlogged changes
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    # Count changes during this session
    cur.execute("""
        SELECT change_type, COUNT(*) as count
        FROM v7_changes
        WHERE session_id = %s
        GROUP BY change_type
    """, (current["session_id"],))
    change_counts = {row["change_type"]: row["count"] for row in cur.fetchall()}

    files_created = change_counts.get("created", 0)
    files_modified = change_counts.get("modified", 0)
    files_deleted = change_counts.get("deleted", 0)

    # Update DB session
    cur.execute("""
        UPDATE v7_sessions SET
            ended_at = NOW(),
            files_created = %s,
            files_modified = %s,
            files_deleted = %s,
            log_entries = %s,
            log_path = %s,
            status = 'complete'
        WHERE id = %s
    """, (
        files_created, files_modified, files_deleted,
        current.get("log_count", 0),
        str(filepath),
        current["session_id"],
    ))
    conn.commit()
    conn.close()

    # Update markdown log
    if filepath.exists():
        end_block = f"""
- [{now_str}] Session ended

---

## Session Summary

**Start:** {current['start_time']}
**End:** {now_str}
**Intent:** {current['description']}
**Log entries:** {current.get('log_count', 0)}
**Files created:** {files_created}
**Files modified:** {files_modified}
**Status:** Complete
"""
        with open(filepath, "a") as f:
            f.write(end_block)

        # Update status line
        content = filepath.read_text()
        content = content.replace("**Status:** Active", "**Status:** Complete")
        filepath.write_text(content)

    clear_session_state(root)

    print(f"[OK] Session ended: {current['description']}")
    print(f"     Duration: {current['start_time']} -> {now_str}")
    print(f"     Log entries: {current.get('log_count', 0)}")
    print(f"     Files created: {files_created}, modified: {files_modified}")


def cmd_session_status(root: Path):
    """Show current session info."""
    current = get_current_session(root)
    if not current:
        print("No active session.")
        print("Use 'v7_registry.py session start \"description\"' to begin one.")
        return

    print(f"[*] Active Session")
    print(f"    DB ID: {current.get('session_id', 'N/A')}")
    print(f"    Description: {current['description']}")
    print(f"    Started: {current['start_time']}")
    print(f"    Log entries: {current.get('log_count', 0)}")
    print(f"    File: {current['file']}")


# ============================================================
# ChromaDB sync
# ============================================================

def cmd_chromadb_sync(root: Path):
    """Sync markdown files to ChromaDB for semantic search."""
    try:
        import chromadb
        from chromadb.config import Settings
    except ImportError:
        print("ERROR: chromadb not installed. Run: pip install chromadb")
        return

    chroma_dir = root / "03_CORE_ENGINE" / "CONFIG" / "chromadb_data"
    chroma_dir.mkdir(parents=True, exist_ok=True)

    client = chromadb.PersistentClient(path=str(chroma_dir))

    # Try to use sentence-transformers embedding
    try:
        from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
        embed_fn = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
        collection = client.get_or_create_collection(
            name="v7_documents",
            embedding_function=embed_fn,
            metadata={"hnsw:space": "cosine"},
        )
    except Exception:
        print("WARNING: sentence-transformers not available, using default embeddings")
        collection = client.get_or_create_collection(
            name="v7_documents",
            metadata={"hnsw:space": "cosine"},
        )

    # Get markdown files from DB
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
        SELECT relative_path, filename, component, pillar, project, file_type, title
        FROM v7_files
        WHERE is_deleted = FALSE AND extension = '.md'
        ORDER BY relative_path
    """)
    md_files = cur.fetchall()
    conn.close()

    print(f"Found {len(md_files)} markdown files to sync")

    synced = 0
    errors = 0

    for row in md_files:
        file_path = root / row["relative_path"]
        if not file_path.exists():
            continue

        try:
            content = file_path.read_text(encoding="utf-8", errors="replace")
        except (PermissionError, OSError):
            errors += 1
            continue

        # Heading-aware chunking
        chunks = chunk_markdown(content, max_chars=1000)

        for i, chunk in enumerate(chunks):
            if not chunk.strip():
                continue

            doc_id = f"{row['relative_path']}::chunk_{i}"
            metadata = {
                "source": row["relative_path"],
                "filename": row["filename"],
                "component": row["component"] or "",
                "pillar": row["pillar"] or "",
                "project": row["project"] or "",
                "file_type": row["file_type"] or "",
                "title": row["title"] or "",
                "chunk_index": i,
            }

            try:
                collection.upsert(
                    ids=[doc_id],
                    documents=[chunk],
                    metadatas=[metadata],
                )
            except Exception as e:
                errors += 1
                if errors <= 5:
                    print(f"  ERROR on {doc_id}: {e}")
                continue

        synced += 1
        if synced % 10 == 0:
            print(f"  Synced {synced}/{len(md_files)} files...")

    print(f"\n[OK] ChromaDB sync complete")
    print(f"     Files synced: {synced}")
    print(f"     Errors: {errors}")
    print(f"     Collection: v7_documents ({collection.count()} chunks)")


def chunk_markdown(content: str, max_chars: int = 1000) -> list:
    """Split markdown by headings, respecting max chunk size."""
    lines = content.split("\n")
    chunks = []
    current_chunk = []
    current_len = 0

    for line in lines:
        # Split on headings
        if line.startswith("#") and current_chunk:
            chunks.append("\n".join(current_chunk))
            current_chunk = [line]
            current_len = len(line)
        else:
            if current_len + len(line) > max_chars and current_chunk:
                chunks.append("\n".join(current_chunk))
                current_chunk = [line]
                current_len = len(line)
            else:
                current_chunk.append(line)
                current_len += len(line)

    if current_chunk:
        chunks.append("\n".join(current_chunk))

    return chunks


# ============================================================
# CLI argument parser
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Enterprise OS V7 — System Registry",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Commands:
  scan                  Full filesystem scan → database
  scan --diff           Show changes without writing to DB
  health                System health report
  stale                 List files not modified in 30+ days
  snapshot              Take system state snapshot
  session start "desc"  Start a work session
  session end           End current session
  session log "msg"     Log to current session
  session status        Show current session
  chromadb-sync         Sync markdown to ChromaDB
        """,
    )
    parser.add_argument("--root", help="Path to ENTERPRISE_OS_V7 root")
    parser.add_argument("command", nargs="?", help="Command to run")
    parser.add_argument("subcommand", nargs="?", help="Subcommand (for session)")
    parser.add_argument("args", nargs="*", help="Additional arguments")
    parser.add_argument("--diff", action="store_true", help="Show diff only (for scan)")
    parser.add_argument("--days", type=int, default=30, help="Days threshold (for stale)")
    parser.add_argument("--file", help="File path (for session log)")
    parser.add_argument("--action", help="Action type (for session log)")

    args = parser.parse_args()
    root = find_root(args.root)

    if not args.command:
        parser.print_help()
        return

    cmd = args.command.lower()

    if cmd == "scan":
        cmd_scan(root, diff_only=args.diff)

    elif cmd == "health":
        cmd_health(root)

    elif cmd == "stale":
        cmd_stale(root, days=args.days)

    elif cmd == "snapshot":
        cmd_snapshot(root)

    elif cmd == "session":
        if not args.subcommand:
            print("Usage: v7_registry.py session {start|end|log|status}")
            return

        sub = args.subcommand.lower()
        if sub == "start":
            desc = " ".join(args.args) if args.args else None
            if not desc:
                print("Usage: v7_registry.py session start \"description\"")
                return
            cmd_session_start(root, desc)
        elif sub == "end":
            cmd_session_end(root)
        elif sub == "log":
            msg = " ".join(args.args) if args.args else None
            if not msg:
                print("Usage: v7_registry.py session log \"message\"")
                return
            cmd_session_log(root, msg, file_path=args.file, action=args.action)
        elif sub == "status":
            cmd_session_status(root)
        else:
            print(f"Unknown session subcommand: {sub}")

    elif cmd in ("chromadb-sync", "chromadb_sync"):
        cmd_chromadb_sync(root)

    else:
        print(f"Unknown command: {cmd}")
        parser.print_help()


if __name__ == "__main__":
    main()
