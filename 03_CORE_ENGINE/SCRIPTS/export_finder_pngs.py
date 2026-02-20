#!/usr/bin/env python3
"""Export PNGs for Finder kit (was rate-limited earlier)."""
import json, os, sys, time, requests
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace', line_buffering=True)

PROJECT_ROOT = Path(r"C:\Users\under\Downloads\ENTERPRISE_OS_V7")
env_path = PROJECT_ROOT / ".env"
if env_path.exists():
    with open(env_path, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, val = line.split("=", 1)
                os.environ[key.strip()] = val.strip()

FIGMA_TOKEN = os.environ.get("FIGMA_TOKEN", "")
BASE_URL = "https://api.figma.com/v1"
HEADERS = {"X-Figma-Token": FIGMA_TOKEN}
KIT_SCREENS_DIR = PROJECT_ROOT / "07_BUILD_FACTORY" / "PRJ_UI_Component_Library" / "kit_screens"

kit_name = "Finder (Directory & Listings)"
templates_path = KIT_SCREENS_DIR / kit_name / "LAYOUT_TEMPLATES.json"
rep_dir = KIT_SCREENS_DIR / kit_name / "representative"
rep_dir.mkdir(parents=True, exist_ok=True)

with open(templates_path, "r", encoding="utf-8") as f:
    data = json.load(f)

file_key = data.get("file_key", "")
layouts = data.get("layouts", [])
print(f"Finder: {len(layouts)} templates, file_key={file_key[:10]}...")

def sanitize(name):
    for ch in "/\\:?\"<>|*":
        name = name.replace(ch, "_")
    return name

downloaded = 0
cached = 0
failed = 0

for i, layout in enumerate(layouts):
    screen_id = layout.get("representative_screen", "")
    screen_name = layout.get("representative_name", layout.get("name", ""))
    if not screen_id:
        failed += 1
        continue

    safe_name = sanitize(screen_name)
    safe_id = screen_id.replace(":", "_")
    filepath = rep_dir / f"{safe_id}_{safe_name}.png"

    if filepath.exists() and filepath.stat().st_size > 1000:
        cached += 1
        continue

    url = f"{BASE_URL}/images/{file_key}"
    params = {"ids": screen_id, "format": "png", "scale": 0.5}

    try:
        resp = requests.get(url, headers=HEADERS, params=params, timeout=120)
        if resp.status_code == 429:
            wait = min(int(resp.headers.get("Retry-After", 30)), 120)
            print(f"  Rate limited - waiting {wait}s...")
            time.sleep(wait)
            resp = requests.get(url, headers=HEADERS, params=params, timeout=120)
        if resp.status_code != 200:
            failed += 1
            print(f"  [{i+1}/{len(layouts)}] FAILED: HTTP {resp.status_code}")
            continue
        img_data = resp.json()
        img_url = img_data.get("images", {}).get(screen_id)
        if not img_url:
            failed += 1
            continue
        dl_resp = requests.get(img_url, timeout=60)
        if dl_resp.status_code != 200 or len(dl_resp.content) < 500:
            failed += 1
            continue
        with open(filepath, "wb") as f:
            f.write(dl_resp.content)
        downloaded += 1
        if downloaded % 10 == 0:
            print(f"  [{i+1}/{len(layouts)}] {downloaded} downloaded...")
    except Exception as e:
        failed += 1
        print(f"  [{i+1}/{len(layouts)}] ERROR: {e}")
        continue
    time.sleep(3)

print(f"Done: {downloaded} new + {cached} cached = {downloaded+cached} PNGs ({failed} failed)")
