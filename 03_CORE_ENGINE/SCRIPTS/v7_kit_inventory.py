#!/usr/bin/env python3
"""
V7 Kit Inventory — Vision Component Extraction (Multi-Provider)

Supports: Google Gemini (default), Groq, OpenAI
Only processes LIGHT DESKTOP versions of full pages. Skips dark mode,
tablet, mobile variants and tiny asset images.

Usage:
    python v7_kit_inventory.py --api-key "YOUR_KEY"               # All kits with Gemini
    python v7_kit_inventory.py --api-key "KEY" --kit "Befit"      # One kit
    python v7_kit_inventory.py --provider groq --api-key "KEY"    # Use Groq
    python v7_kit_inventory.py --provider openai --api-key "KEY"  # Use OpenAI
    python v7_kit_inventory.py --workers 3                        # Custom workers
    python v7_kit_inventory.py --status                           # Show progress
    python v7_kit_inventory.py --report                           # Generate report
    python v7_kit_inventory.py --master                           # Rebuild master
    python v7_kit_inventory.py --force                            # Reprocess all
"""

import os
import sys
import json
import base64
import time
import argparse
import threading
import concurrent.futures
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
MAX_IMAGE_SIZE_MB = 4
MIN_IMAGE_SIZE_KB = 20   # Skip tiny assets (icons, dividers, etc)
MAX_RETRIES = 5
RETRY_DELAY = 3

# Provider defaults
PROVIDER_CONFIG = {
    "gemini": {
        "model": "gemini-2.0-flash",
        "default_workers": 3,       # 15 RPM limit on free tier
        "throttle_delay": 4.5,      # ~13 RPM, safely under 15
        "rpm_limit": 15,
        "rpd_limit": 1500,
    },
    "groq": {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "default_workers": 5,
        "throttle_delay": 0.5,
        "rpm_limit": 30,
        "rpd_limit": 14400,
    },
    "openai": {
        "model": "gpt-4o-mini",
        "default_workers": 5,
        "throttle_delay": 0.3,
        "rpm_limit": 500,
        "rpd_limit": 10000,
    },
}

# Variant suffixes to filter out (keep light desktop / base only)
DARK_VARIANTS = ["_dark", "_desktop_dark", "_tablet_dark", "_mobile_dark", "_iphone_dark"]
DEVICE_VARIANTS = ["_tablet_light", "_tablet_dark", "_mobile_light", "_mobile_dark",
                   "_iphone_light", "_iphone_dark", "_tablet", "_mobile", "_iphone"]

def find_root():
    p = Path(__file__).resolve().parent
    while p != p.parent:
        if (p / "00_SYSTEM_ROOT").is_dir():
            return p
        p = p.parent
    return Path(r"C:\Users\under\Downloads\ENTERPRISE_OS_V7")

ROOT = find_root()
EXPORTS_BASE = ROOT / "07_BUILD_FACTORY" / "PRJ_Enterprise_Platform" / "05_Development" / "enterprise-os-hub" / "public" / "figma-exports"
OUTPUT_DIR = ROOT / "03_CORE_ENGINE" / "INDICES" / "kit_inventories"
KIT_INDEX_PATH = ROOT / "07_BUILD_FACTORY" / "PRJ_UI_Component_Library" / "03_Design" / "KIT_INDEX.json"
PROGRESS_FILE = OUTPUT_DIR / "INVENTORY_PROGRESS.json"

_io_lock = threading.Lock()
_print_lock = threading.Lock()
_rate_lock = threading.Lock()
_request_times = []

def safe_print(*args, **kwargs):
    with _print_lock:
        print(*args, **kwargs)
        sys.stdout.flush()

def long_path(p):
    s = str(p)
    if sys.platform == "win32" and not s.startswith("\\\\?\\"):
        return "\\\\?\\" + os.path.abspath(s)
    return s

def rate_limit_wait(rpm_limit):
    """Enforce RPM limit across all threads."""
    with _rate_lock:
        now = time.time()
        window = 60.0
        # Remove timestamps older than window
        while _request_times and _request_times[0] < now - window:
            _request_times.pop(0)
        if len(_request_times) >= rpm_limit:
            wait_until = _request_times[0] + window
            wait_time = wait_until - now + 0.1
            if wait_time > 0:
                safe_print(f"    [RATE] Waiting {wait_time:.1f}s (at {rpm_limit} RPM limit)")
                time.sleep(wait_time)
        _request_times.append(time.time())

# ---------------------------------------------------------------------------
# Kit mapping + screen selection
# ---------------------------------------------------------------------------
def load_kit_index():
    with open(KIT_INDEX_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    kits = {}
    for kit_name, kit_data in data.items():
        kits[kit_name] = {
            "file_key": kit_data.get("file_key", ""),
            "db_items": kit_data.get("total_items", 0),
            "pages": kit_data.get("pages", {}),
        }
    return kits


def is_variant_to_skip(filename):
    """Return True if this file is a dark/tablet/mobile variant we should skip."""
    name = filename.lower().replace(".png", "")
    for v in DARK_VARIANTS:
        if name.endswith(v):
            return True
    for v in DEVICE_VARIANTS:
        if name.endswith(v):
            return True
    return False


def get_export_screens(file_key):
    """Get filtered PNG files: light desktop only, no tiny assets."""
    kit_dir_str = long_path(EXPORTS_BASE / file_key)
    kit_dir = Path(kit_dir_str)
    if not kit_dir.is_dir():
        return []

    all_screens = []
    for subfolder in ["screens", "components"]:
        sub_path = kit_dir / subfolder
        if sub_path.is_dir():
            for f in sorted(sub_path.iterdir()):
                if f.suffix.lower() != ".png":
                    continue
                try:
                    fsize = f.stat().st_size
                except OSError:
                    continue

                if fsize < MIN_IMAGE_SIZE_KB * 1024:
                    continue
                if is_variant_to_skip(f.name):
                    continue

                all_screens.append({
                    "path": str(f).replace("\\\\?\\", ""),
                    "filename": f.name,
                    "subfolder": subfolder,
                    "size_mb": round(fsize / (1024 * 1024), 2),
                    "size_bytes": fsize,
                })

    return all_screens


# ---------------------------------------------------------------------------
# Vision Prompt (shared across all providers)
# ---------------------------------------------------------------------------
VISION_PROMPT = """You are analyzing a UI design screen from a Figma kit called "{kit_name}".

Identify every distinct UI component visible on this page. For EACH component provide:

1. **component_type**: Use a standardized name from this list where possible:
   button, card, input, textarea, select, dropdown, navbar, sidebar, sidebar_nav, top_nav, bottom_nav,
   chart, tab, tab_bar, modal, dialog, avatar, badge, toggle, switch, calendar, table, data_table,
   form, hero, footer, header, pricing_card, testimonial, stat_card, progress_bar, search_bar,
   notification, breadcrumb, stepper, accordion, tooltip, snackbar, chip, tag, divider, skeleton,
   file_upload, date_picker, slider, radio, checkbox, icon_button, menu, list, grid, carousel,
   rating, timeline, alert, banner, empty_state, pagination, step_indicator, color_swatch,
   typography_sample, icon_set, illustration, image, logo, social_icons, video_player, map,
   sidebar_menu, profile_card, comment, chat_bubble, notification_panel, onboarding_step,
   login_form, signup_form, settings_panel, dashboard_widget, kanban_board, editor, player,
   feature_section, cta_section, faq_section, team_section, contact_form, newsletter_signup

2. **name**: A descriptive name for this specific instance (e.g. "Primary CTA Button", "User Profile Card", "Revenue Chart")

3. **location**: Where on the page (top-left, top-center, top-right, center, bottom, sidebar, etc.)

4. **purpose**: What this component does in the UI (1 sentence)

5. **elements**: List the sub-elements inside this component (e.g. for a card: "thumbnail image, title text, subtitle, action button, bookmark icon")

6. **variant**: Any visible variants or states (primary/secondary, hover/active/disabled, sizes)

7. **count**: How many instances or variants of this component are shown

Return ONLY a valid JSON array. Be thorough — every component matters."""


# ---------------------------------------------------------------------------
# Provider-specific analyze functions
# ---------------------------------------------------------------------------
def analyze_screen_gemini(model, image_path, kit_name, screen_name, rpm_limit):
    """Analyze a screen using Google Gemini."""
    import PIL.Image

    read_path = long_path(image_path)

    try:
        size_mb = os.path.getsize(read_path) / (1024 * 1024)
    except OSError:
        return {"status": "error", "reason": "Cannot read file", "components": []}

    if size_mb > MAX_IMAGE_SIZE_MB:
        return {"status": "skipped", "reason": f"Too large ({size_mb:.1f}MB)", "components": []}

    try:
        img = PIL.Image.open(read_path)
    except Exception as e:
        return {"status": "error", "reason": f"Cannot open image: {e}", "components": []}

    prompt = VISION_PROMPT.format(kit_name=kit_name)

    for attempt in range(MAX_RETRIES):
        try:
            rate_limit_wait(rpm_limit)
            response = model.generate_content(
                [prompt, img],
                generation_config={
                    "temperature": 0.1,
                    "max_output_tokens": 4000,
                }
            )

            raw = response.text.strip()
            return _parse_vision_response(raw)

        except Exception as e:
            err_str = str(e).lower()
            is_rate = any(x in err_str for x in ["429", "resource_exhausted", "rate", "quota"])
            is_connection = any(x in err_str for x in [
                "connection", "timeout", "reset", "eof", "broken pipe",
                "remote end closed", "ssl", "socket", "network",
            ])

            if is_rate:
                wait = 15 * (2 ** attempt)  # Longer waits for rate limits
                safe_print(f"    [RATE LIMIT] Waiting {wait}s...")
                if attempt < MAX_RETRIES - 1:
                    time.sleep(wait)
                    continue
            elif is_connection:
                wait = RETRY_DELAY * (2 ** attempt)
                if attempt < MAX_RETRIES - 1:
                    time.sleep(wait)
                    continue
            else:
                if attempt < MAX_RETRIES - 1:
                    time.sleep(RETRY_DELAY)
                    continue

            return {"status": "error", "reason": str(e)[:300], "components": []}

    return {"status": "error", "reason": "Max retries", "components": []}


def analyze_screen_groq(client, image_path, kit_name, screen_name, model_name, rpm_limit):
    """Analyze a screen using Groq Vision."""
    read_path = long_path(image_path)

    try:
        size_mb = os.path.getsize(read_path) / (1024 * 1024)
    except OSError:
        return {"status": "error", "reason": "Cannot read file", "components": []}

    if size_mb > MAX_IMAGE_SIZE_MB:
        return {"status": "skipped", "reason": f"Too large ({size_mb:.1f}MB)", "components": []}

    with open(read_path, "rb") as f:
        img_data = base64.b64encode(f.read()).decode("utf-8")

    prompt = VISION_PROMPT.format(kit_name=kit_name)

    for attempt in range(MAX_RETRIES):
        try:
            rate_limit_wait(rpm_limit)
            response = client.chat.completions.create(
                model=model_name,
                messages=[{
                    "role": "user",
                    "content": [
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_data}"}},
                        {"type": "text", "text": prompt},
                    ]
                }],
                max_tokens=4000,
                temperature=0.1,
            )

            raw = response.choices[0].message.content.strip()
            result = _parse_vision_response(raw)
            if response.usage:
                result["tokens_used"] = response.usage.total_tokens
            return result

        except json.JSONDecodeError:
            pass  # Handled in _parse_vision_response
        except Exception as e:
            err_str = str(e).lower()
            is_retryable = any(x in err_str for x in [
                "connection", "timeout", "reset", "eof", "429", "rate",
                "broken pipe", "ssl", "socket", "network", "too many",
            ])
            is_too_large = "too large" in err_str

            if is_too_large:
                return {"status": "skipped", "reason": "API payload too large", "components": []}
            elif is_retryable:
                wait = RETRY_DELAY * (2 ** attempt)
                if attempt < MAX_RETRIES - 1:
                    time.sleep(wait)
                    continue
            else:
                if attempt < MAX_RETRIES - 1:
                    time.sleep(RETRY_DELAY)
                    continue

            return {"status": "error", "reason": str(e)[:300], "components": []}

    return {"status": "error", "reason": "Max retries", "components": []}


def analyze_screen_openai(client, image_path, kit_name, screen_name, model_name, rpm_limit):
    """Analyze a screen using OpenAI Vision."""
    read_path = long_path(image_path)

    try:
        size_mb = os.path.getsize(read_path) / (1024 * 1024)
    except OSError:
        return {"status": "error", "reason": "Cannot read file", "components": []}

    if size_mb > MAX_IMAGE_SIZE_MB:
        return {"status": "skipped", "reason": f"Too large ({size_mb:.1f}MB)", "components": []}

    with open(read_path, "rb") as f:
        img_data = base64.b64encode(f.read()).decode("utf-8")

    prompt = VISION_PROMPT.format(kit_name=kit_name)

    for attempt in range(MAX_RETRIES):
        try:
            rate_limit_wait(rpm_limit)
            response = client.chat.completions.create(
                model=model_name,
                messages=[{
                    "role": "user",
                    "content": [
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_data}", "detail": "high"}},
                        {"type": "text", "text": prompt},
                    ]
                }],
                max_tokens=4000,
                temperature=0.1,
            )

            raw = response.choices[0].message.content.strip()
            result = _parse_vision_response(raw)
            if response.usage:
                result["tokens_used"] = response.usage.total_tokens
            return result

        except Exception as e:
            err_str = str(e).lower()
            is_retryable = any(x in err_str for x in [
                "connection", "timeout", "reset", "429", "rate",
                "ssl", "socket", "network", "too many",
            ])

            if is_retryable and attempt < MAX_RETRIES - 1:
                wait = RETRY_DELAY * (2 ** attempt)
                time.sleep(wait)
                continue

            return {"status": "error", "reason": str(e)[:300], "components": []}

    return {"status": "error", "reason": "Max retries", "components": []}


def _parse_vision_response(raw):
    """Parse JSON array from vision model response."""
    try:
        # Strip markdown code blocks
        if "```" in raw:
            lines = raw.split("\n")
            json_lines = []
            in_block = False
            for line in lines:
                if line.strip().startswith("```") and not in_block:
                    in_block = True
                    continue
                elif line.strip() == "```" and in_block:
                    break
                elif in_block:
                    json_lines.append(line)
            if json_lines:
                raw = "\n".join(json_lines)

        start = raw.find("[")
        end = raw.rfind("]")
        if start >= 0 and end > start:
            raw = raw[start:end+1]

        components = json.loads(raw)
        if not isinstance(components, list):
            components = [components]

        return {
            "status": "success",
            "components": components,
            "component_count": len(components),
        }
    except json.JSONDecodeError:
        return {"status": "parse_error", "reason": "Bad JSON", "raw_response": raw[:500] if raw else "", "components": []}


# ---------------------------------------------------------------------------
# Progress + Checkpointing
# ---------------------------------------------------------------------------
def load_progress():
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "started_at": datetime.now().isoformat(),
        "last_updated": None,
        "kits_completed": [],
        "total_screens_processed": 0,
        "total_components_found": 0,
        "total_errors": 0,
        "total_skipped": 0,
    }

def save_progress(progress):
    with _io_lock:
        progress["last_updated"] = datetime.now().isoformat()
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
            json.dump(progress, f, indent=2)

def safe_kit_name(kit_name):
    return kit_name.replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")

def load_kit_checkpoint(kit_name):
    path = OUTPUT_DIR / f"{safe_kit_name(kit_name)}_inventory.json"
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def save_kit_checkpoint(kit_name, inventory):
    with _io_lock:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        path = OUTPUT_DIR / f"{safe_kit_name(kit_name)}_inventory.json"
        tmp_path = OUTPUT_DIR / f"{safe_kit_name(kit_name)}_inventory.tmp"
        inventory["last_checkpoint"] = datetime.now().isoformat()
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(inventory, f, indent=2, ensure_ascii=False)
        if path.exists():
            path.unlink()
        tmp_path.rename(path)


# ---------------------------------------------------------------------------
# Parallel kit processing
# ---------------------------------------------------------------------------
def process_single_screen(analyze_fn, kit_name, screen, idx, total):
    fn = screen["filename"]
    safe_print(f"  [{idx+1}/{total}] {fn} ({screen['size_mb']}MB)...", end=" ")
    result = analyze_fn(screen["path"], kit_name, fn)
    n = len(result.get("components", []))
    if result["status"] == "success":
        safe_print(f"{n} components")
    elif result["status"] == "skipped":
        safe_print(f"SKIP")
    else:
        safe_print(f"ERR: {result.get('reason', '')[:80]}")
    return fn, screen, result


def process_kit_parallel(analyze_fn, kit_name, kit_data, progress, num_workers, throttle, force=False):
    file_key = kit_data["file_key"]
    screens = get_export_screens(file_key)

    if not screens:
        safe_print(f"  [SKIP] No screens for {kit_name}")
        return

    # Load checkpoint
    inventory = load_kit_checkpoint(kit_name)
    if inventory and not force:
        processed = set(inventory.get("processed_screens", []))
        if len(processed) >= len(screens):
            safe_print(f"  [DONE] {kit_name} ({len(processed)} screens already)")
            with _io_lock:
                if kit_name not in progress["kits_completed"]:
                    progress["kits_completed"].append(kit_name)
            save_progress(progress)
            return
        safe_print(f"  [RESUME] {kit_name}: {len(processed)}/{len(screens)}")
    else:
        inventory = {
            "kit_name": kit_name,
            "file_key": file_key,
            "db_item_count": kit_data["db_items"],
            "total_screens": len(screens),
            "processed_screens": [],
            "screens": {},
            "summary": {},
            "started_at": datetime.now().isoformat(),
        }
        processed = set()

    todo = [(i, s) for i, s in enumerate(screens) if s["filename"] not in processed]
    if not todo:
        return

    safe_print(f"  Processing {len(todo)} screens with {num_workers} workers...")

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = {}
        for i, s in todo:
            f = executor.submit(process_single_screen, analyze_fn, kit_name, s, i, len(screens))
            futures[f] = s
            time.sleep(throttle)

        batch = []
        for future in concurrent.futures.as_completed(futures):
            try:
                fn, sc, result = future.result()
                batch.append((fn, sc, result))
            except Exception as e:
                safe_print(f"  [THREAD ERR] {e}")
                with _io_lock:
                    progress["total_errors"] += 1

            # Checkpoint every 5 screens
            if len(batch) % 5 == 0 and batch:
                _flush_batch(batch, inventory, progress)
                save_kit_checkpoint(kit_name, inventory)
                save_progress(progress)

    # Final flush
    if batch:
        _flush_batch(batch, inventory, progress)

    # Summary
    all_components = []
    for sd in inventory["screens"].values():
        r = sd.get("result", {})
        if r.get("status") == "success":
            all_components.extend(r.get("components", []))

    type_counts = {}
    for c in all_components:
        ct = c.get("component_type", "unknown").lower().strip()
        type_counts[ct] = type_counts.get(ct, 0) + 1

    inventory["summary"] = {
        "total_screens": len(screens),
        "screens_processed": len(inventory["processed_screens"]),
        "screens_successful": sum(1 for s in inventory["screens"].values() if s["result"]["status"] == "success"),
        "screens_skipped": sum(1 for s in inventory["screens"].values() if s["result"]["status"] == "skipped"),
        "screens_errored": sum(1 for s in inventory["screens"].values() if s["result"]["status"] in ("error", "parse_error")),
        "total_components_identified": len(all_components),
        "unique_component_types": len(type_counts),
        "component_type_counts": dict(sorted(type_counts.items(), key=lambda x: -x[1])),
        "completed_at": datetime.now().isoformat(),
    }

    save_kit_checkpoint(kit_name, inventory)

    with _io_lock:
        if kit_name not in progress["kits_completed"]:
            progress["kits_completed"].append(kit_name)
    save_progress(progress)

    safe_print(f"  === {kit_name}: {len(all_components)} components from {len(screens)} screens ===")


def _flush_batch(batch, inventory, progress):
    """Write batch results into inventory and progress."""
    with _io_lock:
        for fn, sc, res in batch:
            if fn not in inventory["screens"]:
                inventory["screens"][fn] = {
                    "subfolder": sc["subfolder"],
                    "size_mb": sc["size_mb"],
                    "result": res,
                    "processed_at": datetime.now().isoformat(),
                }
                if fn not in inventory["processed_screens"]:
                    inventory["processed_screens"].append(fn)
                    progress["total_screens_processed"] += 1
                    n = len(res.get("components", []))
                    if res["status"] == "success":
                        progress["total_components_found"] += n
                    elif res["status"] == "skipped":
                        progress["total_skipped"] += 1
                    else:
                        progress["total_errors"] += 1
        batch.clear()


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------
def generate_master_inventory():
    master = {"generated_at": datetime.now().isoformat(), "kits": {}}
    total_components = 0
    total_screens = 0
    all_types = {}

    for f in OUTPUT_DIR.iterdir():
        if f.name.endswith("_inventory.json") and "PROGRESS" not in f.name and "MASTER" not in f.name:
            try:
                with open(f, "r", encoding="utf-8") as fh:
                    inv = json.load(fh)
            except (json.JSONDecodeError, Exception) as e:
                print(f"  WARN: Skipping corrupt file {f.name}: {e}")
                continue
            kit_name = inv.get("kit_name", f.stem.replace("_inventory", ""))
            summary = inv.get("summary", {})
            if summary:
                master["kits"][kit_name] = summary
                total_components += summary.get("total_components_identified", 0)
                total_screens += summary.get("screens_processed", 0)
                for ct, count in summary.get("component_type_counts", {}).items():
                    all_types[ct] = all_types.get(ct, 0) + count

    master["totals"] = {
        "kits_processed": len(master["kits"]),
        "total_screens": total_screens,
        "total_components": total_components,
        "unique_component_types": len(all_types),
        "global_type_counts": dict(sorted(all_types.items(), key=lambda x: -x[1])),
    }

    path = OUTPUT_DIR / "MASTER_INVENTORY.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(master, f, indent=2, ensure_ascii=False)
    print(f"\nMaster: {path}")
    print(f"  {len(master['kits'])} kits | {total_screens} screens | {total_components} components")
    return master


def generate_report(master=None, model_name="unknown"):
    if not master:
        p = OUTPUT_DIR / "MASTER_INVENTORY.json"
        if p.exists():
            with open(p, "r", encoding="utf-8") as f:
                master = json.load(f)
        else:
            print("No master inventory.")
            return

    totals = master.get("totals", {})
    lines = [
        "# UI Kit Component Inventory Report",
        f"\n**Generated:** {master.get('generated_at', 'unknown')}",
        f"**Model:** {model_name}",
        f"**Filter:** Light desktop only, min {MIN_IMAGE_SIZE_KB}KB",
        f"\n## Totals\n",
        f"- **Kits:** {totals.get('kits_processed', 0)}",
        f"- **Screens analyzed:** {totals.get('total_screens', 0)}",
        f"- **Components found:** {totals.get('total_components', 0)}",
        f"- **Component types:** {totals.get('unique_component_types', 0)}",
        "\n## Per-Kit Breakdown\n",
        "| Kit | Screens | Components | Types | Skip | Err |",
        "|-----|---------|------------|-------|------|-----|",
    ]
    for kn, s in sorted(master.get("kits", {}).items()):
        lines.append(f"| {kn} | {s.get('screens_processed',0)} | {s.get('total_components_identified',0)} | {s.get('unique_component_types',0)} | {s.get('screens_skipped',0)} | {s.get('screens_errored',0)} |")

    lines.append("\n## Top Component Types\n")
    lines.append("| Type | Count |")
    lines.append("|------|-------|")
    for ct, count in list(totals.get("global_type_counts", {}).items())[:50]:
        lines.append(f"| {ct} | {count} |")

    path = OUTPUT_DIR / "INVENTORY_REPORT.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Report: {path}")


def show_status():
    progress = load_progress()
    kits = load_kit_index()
    completed = set(progress.get("kits_completed", []))

    print(f"\n{'='*60}")
    print(f"INVENTORY PROGRESS")
    print(f"{'='*60}")
    print(f"Completed: {len(completed)} / {len(kits)} kits")
    print(f"Screens:   {progress.get('total_screens_processed', 0)}")
    print(f"Components:{progress.get('total_components_found', 0)}")
    print(f"Errors:    {progress.get('total_errors', 0)}")
    print(f"Skipped:   {progress.get('total_skipped', 0)}")

    remaining = [k for k in kits if k not in completed]
    if remaining:
        print(f"\nRemaining ({len(remaining)}):")
        for k in remaining:
            screens = get_export_screens(kits[k]["file_key"])
            cp = load_kit_checkpoint(k)
            done = len(cp.get("processed_screens", [])) if cp else 0
            print(f"  {k}: {done}/{len(screens)}")
    else:
        print("\nAll done!")
    print()


# ---------------------------------------------------------------------------
# Client setup
# ---------------------------------------------------------------------------
def create_analyze_fn(provider, api_key, model_name, rpm_limit):
    """Create a provider-specific analyze function."""
    if provider == "gemini":
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)

        def fn(image_path, kit_name, screen_name):
            return analyze_screen_gemini(model, image_path, kit_name, screen_name, rpm_limit)
        return fn

    elif provider == "groq":
        from groq import Groq
        client = Groq(api_key=api_key)

        def fn(image_path, kit_name, screen_name):
            return analyze_screen_groq(client, image_path, kit_name, screen_name, model_name, rpm_limit)
        return fn

    elif provider == "openai":
        from openai import OpenAI
        client = OpenAI(api_key=api_key)

        def fn(image_path, kit_name, screen_name):
            return analyze_screen_openai(client, image_path, kit_name, screen_name, model_name, rpm_limit)
        return fn

    else:
        raise ValueError(f"Unknown provider: {provider}")


# ---------------------------------------------------------------------------
# Entry
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="V7 Kit Inventory (Multi-Provider Vision)")
    parser.add_argument("--provider", type=str, default="gemini", choices=["gemini", "groq", "openai"])
    parser.add_argument("--api-key", type=str, help="API key (or set GEMINI_API_KEY / GROQ_API_KEY / OPENAI_API_KEY env var)")
    parser.add_argument("--model", type=str, help="Override model name")
    parser.add_argument("--kit", type=str)
    parser.add_argument("--workers", type=int)
    parser.add_argument("--status", action="store_true")
    parser.add_argument("--report", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--master", action="store_true")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if args.status:
        show_status()
        return
    if args.report:
        generate_report()
        return
    if args.master:
        master = generate_master_inventory()
        generate_report(master)
        return

    # Resolve provider config
    pconf = PROVIDER_CONFIG[args.provider]
    model_name = args.model or pconf["model"]
    num_workers = args.workers or pconf["default_workers"]
    throttle = pconf["throttle_delay"]
    rpm_limit = pconf["rpm_limit"]

    # Resolve API key
    api_key = args.api_key
    if not api_key:
        env_keys = {
            "gemini": ["GEMINI_API_KEY", "GOOGLE_API_KEY"],
            "groq": ["GROQ_API_KEY"],
            "openai": ["OPENAI_API_KEY"],
        }
        for env_name in env_keys.get(args.provider, []):
            api_key = os.environ.get(env_name)
            if api_key:
                break

    if not api_key:
        print(f"ERROR: No API key. Use --api-key or set environment variable.")
        print(f"  Gemini: https://aistudio.google.com/apikey (free, has vision)")
        print(f"  Groq:   https://console.groq.com/keys")
        print(f"  OpenAI: https://platform.openai.com/api-keys")
        sys.exit(1)

    # Create provider-specific analyze function
    try:
        analyze_fn = create_analyze_fn(args.provider, api_key, model_name, rpm_limit)
    except Exception as e:
        print(f"ERROR: Failed to initialize {args.provider}: {e}")
        sys.exit(1)

    # Quick test with provider
    print(f"Provider: {args.provider} | Model: {model_name}")
    print(f"Testing API connection...", end=" ")
    sys.stdout.flush()

    if args.provider == "gemini":
        import google.generativeai as genai
        try:
            genai.configure(api_key=api_key)
            m = genai.GenerativeModel(model_name)
            r = m.generate_content("Say OK", generation_config={"max_output_tokens": 5})
            print(f"OK ({r.text.strip()[:20]})")
        except Exception as e:
            print(f"FAILED: {e}")
            sys.exit(1)
    elif args.provider == "groq":
        from groq import Groq
        try:
            c = Groq(api_key=api_key)
            r = c.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role":"user","content":"Say OK"}], max_tokens=5)
            print(f"OK ({r.choices[0].message.content.strip()[:20]})")
        except Exception as e:
            print(f"FAILED: {e}")
            sys.exit(1)
    elif args.provider == "openai":
        from openai import OpenAI
        try:
            c = OpenAI(api_key=api_key)
            r = c.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"user","content":"Say OK"}], max_tokens=5)
            print(f"OK ({r.choices[0].message.content.strip()[:20]})")
        except Exception as e:
            print(f"FAILED: {e}")
            sys.exit(1)

    kits = load_kit_index()
    progress = load_progress()

    # Count total filtered screens
    total_screens = 0
    kit_screens = {}
    for name, data in kits.items():
        s = get_export_screens(data["file_key"])
        kit_screens[name] = len(s)
        total_screens += len(s)

    completed = set(progress.get("kits_completed", []))
    remaining_screens = sum(kit_screens.get(k, 0) for k in kits if k not in completed)

    print(f"\n{'='*60}")
    print(f"V7 KIT INVENTORY — {args.provider.upper()}")
    print(f"{'='*60}")
    print(f"Model:       {model_name}")
    print(f"Workers:     {num_workers}")
    print(f"Throttle:    {throttle}s between jobs")
    print(f"RPM limit:   {rpm_limit}")
    print(f"Kits:        {len(kits)} ({len(completed)} done, {len(kits) - len(completed)} remaining)")
    print(f"Screens:     {total_screens} total, {remaining_screens} remaining")
    print(f"Est time:    ~{remaining_screens * (throttle + 2) / num_workers / 60:.0f} min")
    print(f"{'='*60}\n")

    if args.kit:
        if args.kit not in kits:
            matches = [k for k in kits if args.kit.lower() in k.lower()]
            if len(matches) == 1:
                kit_name = matches[0]
            else:
                print(f"Not found or ambiguous: '{args.kit}'")
                return
        else:
            kit_name = args.kit
        process_kit_parallel(analyze_fn, kit_name, kits[kit_name], progress, num_workers, throttle, force=args.force)
    else:
        kit_order = sorted(kits.items(), key=lambda x: kit_screens.get(x[0], 0))

        for kit_name, kit_data in kit_order:
            if kit_name in completed and not args.force:
                continue
            sc = kit_screens.get(kit_name, 0)
            if sc == 0:
                safe_print(f"\n--- {kit_name}: no screens ---")
                continue

            safe_print(f"\n{'='*50}")
            safe_print(f"  {kit_name} ({sc} screens)")
            safe_print(f"{'='*50}")
            try:
                process_kit_parallel(analyze_fn, kit_name, kit_data, progress, num_workers, throttle, force=args.force)
            except KeyboardInterrupt:
                print("\n\nStopped. Progress saved.")
                save_progress(progress)
                sys.exit(0)
            except Exception as e:
                safe_print(f"  [FATAL] {e}")
                progress["total_errors"] += 1
                save_progress(progress)

    print(f"\n{'='*60}")
    master = generate_master_inventory()
    generate_report(master, model_name)
    print("DONE!")


if __name__ == "__main__":
    main()
