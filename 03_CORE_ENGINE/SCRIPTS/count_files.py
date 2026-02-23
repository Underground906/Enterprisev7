#!/usr/bin/env python3
"""Quick file count by component and type."""
import os
from collections import Counter

root = r"C:\Users\under\Downloads\ENTERPRISE_OS_V7"
skip_dirs = {".git", "__pycache__", "node_modules", ".venv", "venv", "V7_ARCHIVE", "chromadb_data"}

components = Counter()
kit_files = Counter()
kit_per_kit = Counter()
total = 0

for dirpath, dirnames, filenames in os.walk(root):
    dirnames[:] = [d for d in dirnames if d not in skip_dirs]
    for f in filenames:
        rel = os.path.relpath(os.path.join(dirpath, f), root).replace(os.sep, "/")
        parts = rel.split("/")
        total += 1
        if parts:
            components[parts[0]] += 1
        if "kit_screens" in rel:
            ext = f.rsplit(".", 1)[-1] if "." in f else "no_ext"
            kit_files[ext] += 1
            # Which kit?
            idx = parts.index("kit_screens") if "kit_screens" in parts else -1
            if idx >= 0 and idx + 1 < len(parts):
                kit_per_kit[parts[idx + 1]] += 1

print(f"Total files in V7: {total}")
print(f"\nBy top-level component:")
for comp, count in components.most_common():
    print(f"  {comp}: {count}")
print(f"\nKit screens by file type:")
for ext, count in kit_files.most_common():
    print(f"  .{ext}: {count}")
print(f"\nTop kits by file count:")
for kit, count in kit_per_kit.most_common(10):
    print(f"  {kit}: {count}")
