#!/usr/bin/env python3
"""
Enterprise_OS V7 — Intake Processor
Drop files into RAW_INTAKE, run this, they get routed to the right pillar.

Usage:
    python intake_processor.py                    # Process all files in RAW_INTAKE
    python intake_processor.py --file myfile.md   # Process a single file
    python intake_processor.py --dry-run          # Show where files WOULD go without moving
    python intake_processor.py --list-unrouted    # Show files in UNROUTED folder

How it works:
    1. Reads files from 04_KNOWLEDGE_LIBRARY/EXTRACTION_PIPELINE/RAW_INTAKE/
    2. Scores each file against pillar routing keywords (from DOMAIN_REGISTRY.json)
    3. Routes to highest-scoring pillar's 01_INPUT/ folder
    4. If no confident match → sends to UNROUTED/
    5. Logs every decision to routing_logs/
"""

import os
import sys
import json
import shutil
import re
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict


# --- Configuration ---

CONFIDENCE_THRESHOLD = 2  # Minimum keyword hits to auto-route (below = UNROUTED)


def find_root():
    candidates = [
        Path.cwd(),
        Path.cwd() / "ENTERPRISE_OS_V7",
        Path(__file__).parent.parent.parent,
        Path.home() / "ENTERPRISE_OS_V7",
        Path.home() / "Documents" / "ENTERPRISE_OS_V7",
    ]
    for c in candidates:
        if (c / "00_SYSTEM_ROOT").exists():
            return c
    print("ERROR: Can't find ENTERPRISE_OS_V7.")
    sys.exit(1)


def load_registry(root):
    """Load DOMAIN_REGISTRY.json for routing keywords."""
    paths = [
        root / "03_CORE_ENGINE" / "INDICES" / "DOMAIN_REGISTRY.json",
        root / "DOMAIN_REGISTRY.json",
    ]
    for p in paths:
        if p.exists():
            with open(p) as f:
                return json.load(f)
    print("ERROR: DOMAIN_REGISTRY.json not found. Run generate_indices.py first.")
    sys.exit(1)


def extract_text(filepath):
    """Read file content for keyword matching."""
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            return f.read().lower()
    except Exception:
        return ""


def score_against_pillars(text, filename, registry):
    """
    Score content against each pillar's routing keywords.
    Returns sorted list of (pillar_id, pillar_name, score, matched_keywords).
    """
    scores = []
    # Combine filename and content for matching
    searchable = filename.lower() + " " + text

    for pillar in registry.get("pillars", []):
        keywords = pillar.get("routing_keywords", [])
        matched = []

        for kw in keywords:
            kw_lower = kw.lower()
            # Count occurrences (but cap at 3 per keyword to avoid spam)
            count = min(searchable.count(kw_lower), 3)
            if count > 0:
                matched.append(kw)

        score = len(matched)  # Simple: number of unique keywords matched

        # Boost: filename contains pillar name or ID
        pillar_name = pillar["name"].lower()
        pillar_id = pillar["id"].lower()
        if pillar_name in filename.lower() or pillar_id in filename.lower():
            score += 3

        if score > 0:
            scores.append({
                "pillar_id": pillar["id"],
                "pillar_name": pillar["name"],
                "pillar_path": pillar["path"],
                "score": score,
                "matched_keywords": matched,
            })

    scores.sort(key=lambda x: -x["score"])
    return scores


def get_destination(root, pillar_path):
    """Get the 01_INPUT folder for a pillar (create if needed)."""
    # Try 01_INPUT first, fall back to 01_threads
    input_dir = root / pillar_path / "01_INPUT"
    if not input_dir.exists():
        threads_dir = root / pillar_path / "01_threads"
        if threads_dir.exists():
            return threads_dir
        input_dir.mkdir(parents=True, exist_ok=True)
    return input_dir


def get_unrouted_dir(root):
    d = root / "04_KNOWLEDGE_LIBRARY" / "ONGOING" / "UNROUTED"
    d.mkdir(parents=True, exist_ok=True)
    return d


def get_intake_dir(root):
    d = root / "04_KNOWLEDGE_LIBRARY" / "EXTRACTION_PIPELINE" / "RAW_INTAKE"
    d.mkdir(parents=True, exist_ok=True)
    return d


def get_log_dir(root):
    d = root / "03_CORE_ENGINE" / "ROUTING_ENGINE" / "routing_logs"
    d.mkdir(parents=True, exist_ok=True)
    return d


def log_routing(log_dir, entries):
    """Write routing decisions to a timestamped log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = log_dir / f"routing_{timestamp}.md"

    lines = [
        f"# Routing Log — {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"",
        f"**Files processed:** {len(entries)}",
        f"",
        f"| File | Destination | Score | Matched Keywords |",
        f"|------|-------------|-------|------------------|",
    ]

    for entry in entries:
        keywords = ", ".join(entry.get("matched", [])[:5])
        lines.append(
            f"| {entry['filename']} | {entry['destination']} | {entry['score']} | {keywords} |"
        )

    lines.append("")
    log_file.write_text("\n".join(lines))
    return log_file


def process_file(root, filepath, registry, dry_run=False):
    """Process a single file: score, route, log."""
    filename = filepath.name
    text = extract_text(filepath)

    if not text and filepath.suffix not in (".png", ".jpg", ".jpeg", ".gif", ".svg", ".pdf"):
        return {
            "filename": filename,
            "destination": "UNROUTED (empty file)",
            "score": 0,
            "matched": [],
            "action": "skipped",
        }

    scores = score_against_pillars(text, filename, registry)

    if scores and scores[0]["score"] >= CONFIDENCE_THRESHOLD:
        best = scores[0]
        dest_dir = get_destination(root, best["pillar_path"])
        dest_path = dest_dir / filename

        # Handle duplicate filenames
        if dest_path.exists():
            stem = filepath.stem
            suffix = filepath.suffix
            counter = 1
            while dest_path.exists():
                dest_path = dest_dir / f"{stem}_{counter}{suffix}"
                counter += 1

        if not dry_run:
            shutil.move(str(filepath), str(dest_path))

        return {
            "filename": filename,
            "destination": f"{best['pillar_id']}_{best['pillar_name']} ({best['score']} hits)",
            "dest_path": str(dest_path.relative_to(root)),
            "score": best["score"],
            "matched": best["matched_keywords"],
            "action": "routed" if not dry_run else "would_route",
            "alternatives": [
                f"{s['pillar_id']}({s['score']})" for s in scores[1:3]
            ],
        }
    else:
        # Below confidence — send to UNROUTED
        unrouted = get_unrouted_dir(root)
        dest_path = unrouted / filename

        if dest_path.exists():
            stem = filepath.stem
            suffix = filepath.suffix
            counter = 1
            while dest_path.exists():
                dest_path = unrouted / f"{stem}_{counter}{suffix}"
                counter += 1

        if not dry_run:
            shutil.move(str(filepath), str(dest_path))

        top_match = f"{scores[0]['pillar_id']}({scores[0]['score']})" if scores else "none"
        return {
            "filename": filename,
            "destination": f"UNROUTED (best: {top_match})",
            "dest_path": str(dest_path.relative_to(root)),
            "score": scores[0]["score"] if scores else 0,
            "matched": scores[0]["matched_keywords"] if scores else [],
            "action": "unrouted" if not dry_run else "would_unroute",
        }


# --- Commands ---

def cmd_process(root, registry, dry_run=False):
    """Process all files in RAW_INTAKE."""
    intake = get_intake_dir(root)
    files = [f for f in intake.iterdir() if f.is_file()]

    if not files:
        print("[*] No files in RAW_INTAKE. Drop files there and re-run.")
        print(f"   Path: {intake.relative_to(root)}")
        return

    prefix = "[DRY RUN] " if dry_run else ""
    print(f"{prefix}Processing {len(files)} file(s)...\n")

    results = []
    for filepath in sorted(files):
        result = process_file(root, filepath, registry, dry_run)
        results.append(result)

        icon = "[+]" if "routed" in result["action"] else "[?]" if "unrouted" in result["action"] else "[-]"
        print(f"  {icon} {result['filename']}")
        print(f"     -> {result['destination']}")
        if result.get("matched"):
            print(f"     Keywords: {', '.join(result['matched'][:5])}")
        if result.get("alternatives"):
            print(f"     Also matched: {', '.join(result['alternatives'])}")
        print()

    # Write log
    if not dry_run and results:
        log_dir = get_log_dir(root)
        log_file = log_routing(log_dir, results)
        print(f"[*] Log written: {log_file.relative_to(root)}")

    # Summary
    routed = sum(1 for r in results if "routed" in r["action"])
    unrouted = sum(1 for r in results if "unrouted" in r["action"])
    skipped = sum(1 for r in results if "skipped" in r["action"])
    print(f"\n{'='*40}")
    print(f"{prefix}Results: {routed} routed, {unrouted} unrouted, {skipped} skipped")


def cmd_process_single(root, registry, filepath, dry_run=False):
    """Process a single specified file."""
    fp = Path(filepath)
    if not fp.exists():
        # Try relative to intake dir
        fp = get_intake_dir(root) / filepath
    if not fp.exists():
        # Try relative to root
        fp = root / filepath
    if not fp.exists():
        print(f"ERROR: File not found: {filepath}")
        return

    result = process_file(root, fp, registry, dry_run)
    prefix = "[DRY RUN] " if dry_run else ""
    print(f"{prefix}{result['filename']} -> {result['destination']}")
    if result.get("matched"):
        print(f"  Keywords: {', '.join(result['matched'])}")


def cmd_list_unrouted(root):
    """Show files sitting in UNROUTED."""
    unrouted = get_unrouted_dir(root)
    files = sorted(f for f in unrouted.iterdir() if f.is_file())

    if not files:
        print("[OK] No unrouted files. Everything has been classified.")
        return

    print(f"[?] {len(files)} unrouted file(s):\n")
    for f in files:
        size = f.stat().st_size
        print(f"  {f.name} ({size:,} bytes)")

    print(f"\n  Location: {unrouted.relative_to(root)}")
    print(f"  To re-route: move back to RAW_INTAKE and run intake_processor.py again")


def cmd_stats(root, registry):
    """Show routing statistics."""
    log_dir = get_log_dir(root)
    logs = sorted(log_dir.glob("routing_*.md"))

    intake = get_intake_dir(root)
    pending = len([f for f in intake.iterdir() if f.is_file()])

    unrouted = get_unrouted_dir(root)
    stuck = len([f for f in unrouted.iterdir() if f.is_file()])

    print(f"[*] Intake Processor Stats")
    print(f"   Pending in RAW_INTAKE: {pending}")
    print(f"   Sitting in UNROUTED: {stuck}")
    print(f"   Routing logs: {len(logs)}")

    if logs:
        latest = logs[-1]
        print(f"   Latest log: {latest.name}")


# --- Main ---

def print_usage():
    print("""
Enterprise_OS Intake Processor

Commands:
  (no args)              Process all files in RAW_INTAKE
  --file myfile.md       Process a single file
  --dry-run              Show routing decisions without moving files
  --list-unrouted        Show files that couldn't be auto-routed
  --stats                Show processing statistics

Examples:
  python intake_processor.py                         # Route everything in RAW_INTAKE
  python intake_processor.py --dry-run               # Preview without moving
  python intake_processor.py --file notes.md         # Route one file
  python intake_processor.py --list-unrouted         # Check what's stuck
""")


def main():
    root = find_root()
    registry = load_registry(root)

    dry_run = "--dry-run" in sys.argv

    if "--help" in sys.argv or "-h" in sys.argv:
        print_usage()
        return

    if "--list-unrouted" in sys.argv:
        cmd_list_unrouted(root)
        return

    if "--stats" in sys.argv:
        cmd_stats(root, registry)
        return

    if "--file" in sys.argv:
        idx = sys.argv.index("--file")
        if idx + 1 < len(sys.argv):
            cmd_process_single(root, registry, sys.argv[idx + 1], dry_run)
        else:
            print("Usage: intake_processor.py --file <filename>")
        return

    cmd_process(root, registry, dry_run)


if __name__ == "__main__":
    main()
