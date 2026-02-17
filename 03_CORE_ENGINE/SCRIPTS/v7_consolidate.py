#!/usr/bin/env python3
"""
Enterprise OS V7 — File Consolidation Tool
Inventory, dedup, plan, and execute consolidation of scattered files.

Usage:
    python v7_consolidate.py inventory               # Scan external sources → v7_external_sources
    python v7_consolidate.py dedup                    # Compare hashes, mark duplicates
    python v7_consolidate.py plan                     # Generate consolidation plan (markdown)
    python v7_consolidate.py execute --group notebook --approved   # Move with approval

NOTHING moves without --approved flag. Script generates plans for review first.

Database: enterprise_os (PostgreSQL, localhost)
"""

import os
import sys
import json
import hashlib
import shutil
import argparse
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict

import psycopg2
from psycopg2.extras import RealDictCursor


# ============================================================
# Configuration
# ============================================================

DB_CONFIG = {
    "dbname": "enterprise_os",
    "user": "postgres",
    "host": "localhost",
}

# External source groups and their locations (relative to user home)
# Each entry: (source_path, group_name, description, default_target)
SOURCE_GROUPS = [
    {
        "name": "notebook",
        "paths": [
            "Downloads/Notebook_EnterpriseOS_temp",
            "Downloads/Notebook EnterpriseOS summary",
        ],
        "description": "Google Notebook synthesis docs",
        "default_target": "06_DOMAIN_PILLARS/PIL_15_ENTERPRISE_OS/01_INPUT",
    },
    {
        "name": "legacy",
        "paths": [
            "Downloads/Enterprise_OS",
        ],
        "description": "Legacy Enterprise_OS threads and artifacts",
        "default_target": "04_KNOWLEDGE_LIBRARY/RAW_INTAKE/legacy",
    },
    {
        "name": "collective",
        "paths": [
            "Downloads/All_Enterprise_OS/V7 Collective Docs",
            "Downloads/All_Enterprise_OS",
        ],
        "description": "V7 Collective Docs (may have duplicates)",
        "default_target": "04_KNOWLEDGE_LIBRARY/RAW_INTAKE/collective",
    },
    {
        "name": "stage1",
        "paths": [
            "Downloads/Enterprise_OS__STAGE1",
        ],
        "description": "Stage 1 duplicate staging area",
        "default_target": "04_KNOWLEDGE_LIBRARY/RAW_INTAKE/stage1",
    },
]

SKIP_EXTENSIONS = {".pyc", ".pyo", ".DS_Store", ".tmp", ".bak", ".lock"}
SKIP_DIRS = {"node_modules", "__pycache__", ".git", ".venv", "venv"}


# ============================================================
# Helpers
# ============================================================

def find_v7_root():
    """Find ENTERPRISE_OS_V7 root."""
    candidates = [
        Path.cwd(),
        Path.cwd() / "ENTERPRISE_OS_V7",
        Path(__file__).parent.parent.parent,
        Path.home() / "Downloads" / "ENTERPRISE_OS_V7",
    ]
    for c in candidates:
        if (c / "00_SYSTEM_ROOT").exists():
            return c
    print("ERROR: Could not find ENTERPRISE_OS_V7 root.")
    sys.exit(1)


def get_db():
    """Get a database connection."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        conn.autocommit = False
        return conn
    except psycopg2.OperationalError as e:
        print(f"ERROR: Cannot connect to database: {e}")
        sys.exit(1)


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


def should_skip(path: Path) -> bool:
    """Check if a path should be skipped."""
    for part in path.parts:
        if part in SKIP_DIRS:
            return True
    if path.suffix in SKIP_EXTENSIONS:
        return True
    if path.name.startswith("~$"):
        return True
    return False


# ============================================================
# Commands
# ============================================================

def cmd_inventory():
    """Scan all external source directories and catalog files in DB."""
    home = Path.home()
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    # Clear existing inventory (re-scan from scratch)
    cur.execute("DELETE FROM v7_external_sources WHERE status = 'inventoried'")
    conn.commit()

    total = 0
    group_counts = {}

    for group in SOURCE_GROUPS:
        group_name = group["name"]
        group_total = 0

        for rel_path in group["paths"]:
            source_dir = home / rel_path
            if not source_dir.exists():
                print(f"  SKIP: {source_dir} (not found)")
                continue

            print(f"\nScanning: {source_dir}")
            files = []

            for file_path in sorted(source_dir.rglob("*")):
                if not file_path.is_file():
                    continue
                if should_skip(file_path):
                    continue

                content_hash = compute_hash(file_path)
                files.append({
                    "source_path": str(file_path),
                    "filename": file_path.name,
                    "extension": file_path.suffix.lower() or None,
                    "source_group": group_name,
                    "content_hash": content_hash,
                    "size_bytes": file_path.stat().st_size,
                    "target_path": group["default_target"],
                })

            # Batch insert
            for f in files:
                cur.execute("""
                    INSERT INTO v7_external_sources
                        (source_path, filename, extension, source_group, content_hash, size_bytes, target_path)
                    VALUES (%(source_path)s, %(filename)s, %(extension)s, %(source_group)s,
                            %(content_hash)s, %(size_bytes)s, %(target_path)s)
                """, f)

            conn.commit()
            group_total += len(files)
            print(f"  Found: {len(files)} files")

            # Checkpoint after each source path
            conn.commit()

        group_counts[group_name] = group_total
        total += group_total

    print(f"\n{'='*60}")
    print(f"INVENTORY COMPLETE")
    print(f"{'='*60}")
    print(f"  Total files inventoried: {total}")
    for name, count in group_counts.items():
        print(f"  {name:20s} {count:>6}")

    conn.close()


def cmd_dedup():
    """Compare external file hashes against V7 files, mark duplicates."""
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    # Get all V7 file hashes
    cur.execute("SELECT id, content_hash FROM v7_files WHERE is_deleted = FALSE AND content_hash IS NOT NULL")
    v7_hashes = {row["content_hash"]: row["id"] for row in cur.fetchall()}

    # Get all external files
    cur.execute("SELECT id, content_hash, filename, source_group FROM v7_external_sources WHERE status = 'inventoried'")
    externals = cur.fetchall()

    if not externals:
        print("No inventoried files found. Run 'v7_consolidate.py inventory' first.")
        conn.close()
        return

    dupes = 0
    unique = 0

    for ext in externals:
        if ext["content_hash"] in v7_hashes:
            cur.execute("""
                UPDATE v7_external_sources
                SET status = 'duplicate', duplicate_of = %s, processed_at = NOW()
                WHERE id = %s
            """, (v7_hashes[ext["content_hash"]], ext["id"]))
            dupes += 1
        else:
            unique += 1

    # Also check for duplicates within external sources themselves
    cur.execute("""
        SELECT content_hash, COUNT(*) as cnt
        FROM v7_external_sources
        WHERE status = 'inventoried'
        GROUP BY content_hash
        HAVING COUNT(*) > 1
    """)
    internal_dupes = cur.fetchall()
    internal_dupe_count = sum(row["cnt"] - 1 for row in internal_dupes)

    conn.commit()

    print(f"\n{'='*60}")
    print(f"DEDUP RESULTS")
    print(f"{'='*60}")
    print(f"  Total external files:          {len(externals)}")
    print(f"  Duplicates of V7 files:        {dupes}")
    print(f"  Unique (not in V7):            {unique}")
    print(f"  Internal duplicates (same hash): {internal_dupe_count}")

    conn.close()


def cmd_plan(root: Path):
    """Generate a consolidation plan as markdown."""
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    # Get summary by group and status
    cur.execute("""
        SELECT source_group, status, COUNT(*) as count, SUM(size_bytes) as total_size
        FROM v7_external_sources
        GROUP BY source_group, status
        ORDER BY source_group, status
    """)
    summary = cur.fetchall()

    if not summary:
        print("No external files found. Run 'v7_consolidate.py inventory' first.")
        conn.close()
        return

    # Get unique files per group
    cur.execute("""
        SELECT source_group, filename, extension, size_bytes, target_path
        FROM v7_external_sources
        WHERE status = 'inventoried'
        ORDER BY source_group, filename
    """)
    unique_files = cur.fetchall()

    # Build plan
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    plan = f"""# CONSOLIDATION PLAN

**Generated:** {now}
**Status:** PENDING APPROVAL

---

## Summary by Source Group

| Group | Status | Count | Size (MB) |
|-------|--------|-------|-----------|
"""
    for row in summary:
        size_mb = (row["total_size"] or 0) / (1024 * 1024)
        plan += f"| {row['source_group']} | {row['status']} | {row['count']} | {size_mb:.1f} |\n"

    plan += f"""
## Unique Files to Consolidate

Total unique files: {len(unique_files)}

"""
    # Group by source_group
    by_group = defaultdict(list)
    for f in unique_files:
        by_group[f["source_group"]].append(f)

    for group_name, files in by_group.items():
        group_info = next((g for g in SOURCE_GROUPS if g["name"] == group_name), None)
        desc = group_info["description"] if group_info else "Unknown"
        plan += f"### {group_name} ({len(files)} files)\n\n"
        plan += f"**Description:** {desc}\n"
        plan += f"**Default target:** `{files[0]['target_path']}`\n\n"
        plan += "| # | Filename | Ext | Size |\n|---|----------|-----|------|\n"
        for i, f in enumerate(files[:50], 1):
            size_kb = f["size_bytes"] / 1024
            plan += f"| {i} | {f['filename']} | {f['extension'] or '-'} | {size_kb:.1f} KB |\n"
        if len(files) > 50:
            plan += f"| ... | *{len(files) - 50} more files* | | |\n"
        plan += "\n"

    plan += """---

## How to Execute

```bash
# After reviewing this plan, execute per group:
python v7_consolidate.py execute --group notebook --approved
python v7_consolidate.py execute --group legacy --approved
python v7_consolidate.py execute --group collective --approved
```

**WARNING:** Nothing moves without --approved flag.
"""

    # Write plan
    plan_path = root / "03_CORE_ENGINE" / "INDICES" / "CONSOLIDATION_PLAN.md"
    with open(plan_path, "w", encoding="utf-8") as f:
        f.write(plan)

    print(f"Plan written to: {plan_path.relative_to(root)}")
    print(f"\nSummary:")
    for group_name, files in by_group.items():
        print(f"  {group_name:20s} {len(files):>5} unique files")
    print(f"\nReview the plan, then run with --approved to execute.")

    conn.close()


def cmd_execute(root: Path, group: str, approved: bool):
    """Execute consolidation for a specific group."""
    if not approved:
        print("ERROR: Must pass --approved flag to execute. Review the plan first.")
        print("Run: python v7_consolidate.py plan")
        return

    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)

    # Get files for this group
    cur.execute("""
        SELECT id, source_path, filename, target_path
        FROM v7_external_sources
        WHERE source_group = %s AND status = 'inventoried'
        ORDER BY filename
    """, (group,))
    files = cur.fetchall()

    if not files:
        print(f"No files to consolidate for group '{group}'.")
        print("Either already processed, or run 'inventory' and 'dedup' first.")
        conn.close()
        return

    print(f"\nConsolidating {len(files)} files from group '{group}'")

    # Ensure target directory exists
    target_dir = root / files[0]["target_path"]
    target_dir.mkdir(parents=True, exist_ok=True)

    moved = 0
    errors = 0

    for f in files:
        source = Path(f["source_path"])
        if not source.exists():
            print(f"  SKIP (missing): {source}")
            cur.execute("""
                UPDATE v7_external_sources SET status = 'skipped', processed_at = NOW()
                WHERE id = %s
            """, (f["id"],))
            errors += 1
            continue

        dest = target_dir / f["filename"]

        # Handle name collisions
        if dest.exists():
            stem = dest.stem
            suffix = dest.suffix
            counter = 1
            while dest.exists():
                dest = target_dir / f"{stem}_{counter}{suffix}"
                counter += 1

        try:
            shutil.copy2(str(source), str(dest))
            cur.execute("""
                UPDATE v7_external_sources
                SET status = 'moved', target_path = %s, processed_at = NOW()
                WHERE id = %s
            """, (str(dest.relative_to(root)), f["id"]))
            moved += 1
        except Exception as e:
            print(f"  ERROR copying {source.name}: {e}")
            errors += 1

        # Checkpoint after every file
        conn.commit()

        if moved % 25 == 0:
            print(f"  Progress: {moved}/{len(files)} moved...")

    conn.commit()

    print(f"\n{'='*60}")
    print(f"CONSOLIDATION COMPLETE — {group}")
    print(f"{'='*60}")
    print(f"  Moved:    {moved}")
    print(f"  Errors:   {errors}")
    print(f"  Target:   {target_dir.relative_to(root)}")
    print(f"\nNote: Original files NOT deleted (copies only). Delete originals manually after verification.")

    conn.close()


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Enterprise OS V7 — File Consolidation Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Commands:
  inventory     Scan external sources → database
  dedup         Compare hashes against V7, mark duplicates
  plan          Generate consolidation plan (markdown)
  execute       Move files (requires --group and --approved)
        """,
    )
    parser.add_argument("command", help="Command: inventory, dedup, plan, execute")
    parser.add_argument("--group", help="Source group to execute (for execute command)")
    parser.add_argument("--approved", action="store_true", help="Confirm execution (required for execute)")
    parser.add_argument("--root", help="Path to ENTERPRISE_OS_V7 root")

    args = parser.parse_args()
    root = find_v7_root()

    cmd = args.command.lower()

    if cmd == "inventory":
        cmd_inventory()
    elif cmd == "dedup":
        cmd_dedup()
    elif cmd == "plan":
        cmd_plan(root)
    elif cmd == "execute":
        if not args.group:
            print("ERROR: --group required. Options: notebook, legacy, collective, stage1")
            return
        cmd_execute(root, args.group, args.approved)
    else:
        print(f"Unknown command: {cmd}")
        parser.print_help()


if __name__ == "__main__":
    main()
