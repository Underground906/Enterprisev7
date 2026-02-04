#!/usr/bin/env python3
"""
Enterprise_OS V7 — Index Generator
Scans the entire system and produces machine-readable indices + health report.

Usage:
    python generate_indices.py [--root /path/to/ENTERPRISE_OS_V7]
    
Outputs:
    - 03_CORE_ENGINE/INDICES/FILE_INDEX.json
    - 03_CORE_ENGINE/INDICES/SYSTEM_HEALTH.md
    - Updates file_count in DOMAIN_REGISTRY.json
"""

import os
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict

# --- Configuration ---

SKIP_DIRS = {
    "V7_ARCHIVE",       # RAG bundles — too many hash files
    "90_ARCHIVE",       # Archived content
    "node_modules",
    "__pycache__",
    ".git",
    ".venv",
    "venv",
}

SKIP_EXTENSIONS = {".pyc", ".pyo", ".DS_Store", ".tmp", ".bak"}


def find_root(provided_root=None):
    """Find the ENTERPRISE_OS_V7 root directory."""
    if provided_root:
        return Path(provided_root)
    
    # Try common locations
    candidates = [
        Path.cwd(),
        Path.cwd() / "ENTERPRISE_OS_V7",
        Path.home() / "ENTERPRISE_OS_V7",
        Path.home() / "Documents" / "ENTERPRISE_OS_V7",
    ]
    
    for candidate in candidates:
        if (candidate / "00_SYSTEM_ROOT").exists():
            return candidate
    
    print("ERROR: Could not find ENTERPRISE_OS_V7 root directory.")
    print("Run with: python generate_indices.py --root /path/to/ENTERPRISE_OS_V7")
    sys.exit(1)


def should_skip(path: Path) -> bool:
    """Check if a path should be skipped during scanning."""
    parts = path.parts
    for skip in SKIP_DIRS:
        if skip in parts:
            return True
    if path.suffix in SKIP_EXTENSIONS:
        return True
    return False


def scan_files(root: Path) -> list[dict]:
    """Scan all files in the system, skipping archives and junk."""
    files = []
    
    for file_path in sorted(root.rglob("*")):
        if not file_path.is_file():
            continue
        if should_skip(file_path):
            continue
            
        rel_path = file_path.relative_to(root)
        stat = file_path.stat()
        
        # Determine which pillar/component this belongs to
        pillar = identify_pillar(str(rel_path))
        
        # Determine file type
        file_type = classify_file(file_path)
        
        files.append({
            "path": str(rel_path),
            "filename": file_path.name,
            "extension": file_path.suffix,
            "type": file_type,
            "pillar": pillar,
            "size_bytes": stat.st_size,
            "last_modified": datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
        })
    
    return files


def identify_pillar(rel_path: str) -> str:
    """Identify which pillar or component a file belongs to."""
    parts = rel_path.split(os.sep)
    
    # Check for domain pillar
    for part in parts:
        if part.startswith("PIL_"):
            return part
    
    # Check for top-level component
    component_map = {
        "00_SYSTEM_ROOT": "SYSTEM_ROOT",
        "01_NAVIGATION_CENTRE": "NAVIGATION",
        "02_COMMAND_DECK": "COMMAND_DECK",
        "03_CORE_ENGINE": "CORE_ENGINE",
        "04_KNOWLEDGE_LIBRARY": "KNOWLEDGE_LIBRARY",
        "05_TEMPLATE_HUB": "TEMPLATE_HUB",
        "07_BUILD_FACTORY": "BUILD_FACTORY",
        "08_OPERATIONS": "OPERATIONS",
    }
    
    if parts:
        return component_map.get(parts[0], "UNKNOWN")
    
    return "ROOT"


def classify_file(file_path: Path) -> str:
    """Classify a file by its type/purpose."""
    name = file_path.name.upper()
    ext = file_path.suffix.lower()
    
    if name in ("README.MD", "DOCS.MD", "CONTEXT.MD"):
        return "context_doc"
    if name in ("ANALYSIS.MD", "ROUTING_RULES.MD"):
        return "analysis_doc"
    if "CANON" in name or "MASTER" in name:
        return "canon_doc"
    if "TEMPLATE" in name:
        return "template"
    if "INDEX" in name or "REGISTRY" in name or "MANIFEST" in name:
        return "index"
    if ext == ".py":
        return "script"
    if ext == ".ps1":
        return "script"
    if ext == ".json":
        return "data"
    if ext == ".yaml" or ext == ".yml":
        return "config"
    if ext == ".md":
        return "document"
    
    return "other"


def count_empty_dirs(root: Path) -> int:
    """Count directories that have no files (recursively empty)."""
    empty = 0
    for dir_path in root.rglob("*"):
        if not dir_path.is_dir():
            continue
        if should_skip(dir_path):
            continue
        # Check if directory has any files (not counting subdirs)
        has_files = any(f.is_file() for f in dir_path.iterdir() if not should_skip(f))
        if not has_files:
            # Check if any subdirectory has files
            has_nested_files = any(
                f.is_file() for f in dir_path.rglob("*") 
                if not should_skip(f)
            )
            if not has_nested_files:
                empty += 1
    return empty


def generate_health_report(root: Path, files: list[dict], registry: dict) -> str:
    """Generate a human-readable system health report."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    
    # Count by pillar
    pillar_counts = defaultdict(int)
    for f in files:
        pillar_counts[f["pillar"]] += 1
    
    # Count by type
    type_counts = defaultdict(int)
    for f in files:
        type_counts[f["type"]] += 1
    
    # Count empty directories
    empty_dirs = count_empty_dirs(root)
    total_dirs = sum(1 for _ in root.rglob("*") if _.is_dir() and not should_skip(_))
    
    # Pillar health
    pillar_health = []
    for p in registry.get("pillars", []):
        pid = p["id"].replace("PIL_", "PIL_") + "_" + p["name"]
        count = pillar_counts.get(pid, 0)
        status = p.get("canon_status", "unknown")
        priority = p.get("priority", "unknown")
        
        if status == "complete" and count >= 3:
            health = "🟢 Healthy"
        elif status == "has_docs":
            health = "🟡 Partial"
        elif count > 0:
            health = "🟡 Has files, needs canon"
        else:
            health = "🔴 Empty"
        
        pillar_health.append((p["id"], p["name"], count, status, priority, health))
    
    report = f"""# SYSTEM HEALTH REPORT

**Generated:** {now}
**Root:** {root}

---

## Summary

| Metric | Value |
|--------|-------|
| Total indexed files | {len(files)} |
| Total directories (excl. archives) | {total_dirs} |
| Empty directories | {empty_dirs} |
| Pillars with canon docs | {sum(1 for p in registry.get('pillars', []) if p.get('canon_status') in ('has_docs', 'complete'))} / {len(registry.get('pillars', []))} |

## Files by Type

| Type | Count |
|------|-------|
"""
    for ftype, count in sorted(type_counts.items(), key=lambda x: -x[1]):
        report += f"| {ftype} | {count} |\n"
    
    report += f"""
## Pillar Health

| ID | Name | Files | Canon | Priority | Health |
|----|------|-------|-------|----------|--------|
"""
    for pid, name, count, status, priority, health in pillar_health:
        report += f"| {pid} | {name} | {count} | {status} | {priority} | {health} |\n"
    
    report += f"""
## Files by Component

| Component | Count |
|-----------|-------|
"""
    component_counts = defaultdict(int)
    for f in files:
        component_counts[f["pillar"]] += 1
    
    for comp, count in sorted(component_counts.items(), key=lambda x: -x[1]):
        report += f"| {comp} | {count} |\n"
    
    report += f"""
---

## Action Items

"""
    # Flag empty critical pillars
    for pid, name, count, status, priority, health in pillar_health:
        if priority in ("critical", "high") and status == "empty":
            report += f"- 🔴 **{pid} {name}** — Priority {priority} but no canon docs. Create README.md in 00_CANON/\n"
    
    # Flag stale content would go here (needs last_modified comparison)
    
    report += f"\n---\n*Report generated by generate_indices.py*\n"
    
    return report


def update_registry_counts(registry: dict, files: list[dict]) -> dict:
    """Update file counts in the domain registry."""
    pillar_counts = defaultdict(int)
    for f in files:
        pillar_counts[f["pillar"]] += 1
    
    for pillar in registry.get("pillars", []):
        key = pillar["id"].replace("PIL_", "PIL_") + "_" + pillar["name"]
        pillar["file_count"] = pillar_counts.get(key, 0)
    
    registry["last_updated"] = datetime.now(timezone.utc).isoformat()
    return registry


def main():
    # Parse arguments
    root_path = None
    if "--root" in sys.argv:
        idx = sys.argv.index("--root")
        if idx + 1 < len(sys.argv):
            root_path = sys.argv[idx + 1]
    
    root = find_root(root_path)
    print(f"Scanning: {root}")
    
    # Ensure indices directory exists
    indices_dir = root / "03_CORE_ENGINE" / "INDICES"
    indices_dir.mkdir(parents=True, exist_ok=True)
    
    # Scan files
    files = scan_files(root)
    print(f"Found {len(files)} files (excluding archives)")
    
    # Build FILE_INDEX.json
    file_index = {
        "last_scan": datetime.now(timezone.utc).isoformat(),
        "scanner_version": "1.0",
        "root": str(root),
        "total_files": len(files),
        "files": files,
    }
    
    file_index_path = indices_dir / "FILE_INDEX.json"
    with open(file_index_path, "w") as f:
        json.dump(file_index, f, indent=2)
    print(f"Written: {file_index_path}")
    
    # Update DOMAIN_REGISTRY.json if it exists
    registry_path = indices_dir / "DOMAIN_REGISTRY.json"
    if registry_path.exists():
        with open(registry_path) as f:
            registry = json.load(f)
        registry = update_registry_counts(registry, files)
        with open(registry_path, "w") as f:
            json.dump(registry, f, indent=2)
        print(f"Updated: {registry_path}")
    else:
        # Check if it's at root level (initial placement)
        root_registry = root / "DOMAIN_REGISTRY.json"
        if root_registry.exists():
            with open(root_registry) as f:
                registry = json.load(f)
            registry = update_registry_counts(registry, files)
            with open(registry_path, "w") as f:
                json.dump(registry, f, indent=2)
            print(f"Moved and updated registry to: {registry_path}")
        else:
            registry = {"pillars": []}
            print("WARNING: No DOMAIN_REGISTRY.json found. Create one and re-run.")
    
    # Generate health report
    report = generate_health_report(root, files, registry)
    health_path = indices_dir / "SYSTEM_HEALTH.md"
    with open(health_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"Written: {health_path}")
    
    # Print summary
    print(f"\n{'='*50}")
    print(f"SCAN COMPLETE")
    print(f"{'='*50}")
    print(f"Files indexed: {len(files)}")
    print(f"Outputs:")
    print(f"  - {file_index_path}")
    print(f"  - {health_path}")
    if registry_path.exists():
        print(f"  - {registry_path}")
    print()


if __name__ == "__main__":
    main()
