#!/usr/bin/env python3
"""
Enterprise OS V7 — Daily Maintenance Runner
One command to run all daily checks.

Usage:
    python v7_daily.py              # Run full daily sequence
    python v7_daily.py --quick      # Just scan diff + health (skip snapshot)

Runs:
    1. Scan --diff (what changed since last scan?)
    2. Full scan (update database)
    3. Health report
    4. System state snapshot
    5. Stale file check

All zero-cost — no LLM tokens, just filesystem + PostgreSQL.
"""

import sys
import subprocess
from datetime import datetime
from pathlib import Path


def find_root():
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


def run_command(label, cmd, root):
    """Run a v7_registry.py command and capture output."""
    script = str(root / "03_CORE_ENGINE" / "SCRIPTS" / "v7_registry.py")
    full_cmd = [sys.executable, script] + cmd

    print(f"\n{'-'*60}")
    print(f"  {label}")
    print(f"{'-'*60}")

    result = subprocess.run(
        full_cmd,
        cwd=str(root),
        capture_output=False,
        text=True,
    )

    if result.returncode != 0:
        print(f"  !! Command failed with exit code {result.returncode}")

    return result.returncode


def main():
    root = find_root()
    quick = "--quick" in sys.argv

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"{'='*60}")
    print(f"  ENTERPRISE OS V7 — DAILY MAINTENANCE")
    print(f"  {now}")
    print(f"{'='*60}")

    steps = [
        ("Step 1: Diff (what changed?)", ["scan", "--diff"]),
        ("Step 2: Full scan (update DB)", ["scan"]),
        ("Step 3: Health report", ["health"]),
    ]

    if not quick:
        steps.extend([
            ("Step 4: System snapshot", ["snapshot"]),
            ("Step 5: Stale files (30+ days)", ["stale"]),
        ])

    failures = 0
    for label, cmd in steps:
        rc = run_command(label, cmd, root)
        if rc != 0:
            failures += 1

    print(f"\n{'='*60}")
    print(f"  DAILY MAINTENANCE COMPLETE")
    print(f"  Steps run: {len(steps)}")
    print(f"  Failures:  {failures}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
