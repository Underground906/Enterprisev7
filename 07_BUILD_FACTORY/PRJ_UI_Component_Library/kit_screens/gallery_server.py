#!/usr/bin/env python3
"""
UI Kit Screen Gallery Server v3
Serves freshly-exported PNGs from kit_screens/{KitName}/screens/ and components/
Run: python gallery_server.py
Open: http://localhost:8080
"""
import http.server, json, os, socketserver, urllib.parse, webbrowser
from pathlib import Path
from collections import defaultdict

PORT = 8080
BASE_DIR = Path(__file__).parent  # kit_screens/

# === BUILD DATA AT STARTUP ===
print("Building gallery data from exported PNGs...")

KIT_PNGS = defaultdict(list)  # kit_name -> [{path, name, type, kit}]
ALL_PNGS = []

# Scan kit_screens/ for kit directories with screens/ and components/ subdirs
for kit_dir in sorted(BASE_DIR.iterdir()):
    if not kit_dir.is_dir():
        continue
    kit_name = kit_dir.name
    # Skip non-kit directories
    if kit_name.startswith(".") or kit_name in ("__pycache__",):
        continue

    # Check for screens/ and components/ subdirs
    for subtype in ("screens", "components"):
        sub_dir = kit_dir / subtype
        if not sub_dir.exists():
            continue
        for png in sorted(sub_dir.glob("*.png")):
            # Filename format: nodeId_Name.png (e.g., 0_123_Dashboard Home.png)
            # Parse display name from filename
            stem = png.stem
            # Remove node ID prefix (everything before first underscore pair)
            parts = stem.split("_", 1)
            display_name = parts[1] if len(parts) > 1 else stem
            # Clean up node ID remnants at start
            if display_name and display_name[0].isdigit():
                inner = display_name.split("_", 1)
                if len(inner) > 1:
                    display_name = inner[1]

            # Filter: skip dark/mobile/tablet
            lower = display_name.lower()
            skip = any(x in lower for x in ["dark", "mobile", "tablet", "ipad", "android"])

            entry = {
                "path": f"{kit_name}/{subtype}/{png.name}",
                "cat": subtype,  # "screens" or "components"
                "kit": kit_name,
                "name": display_name,
                "file": png.name,
                "skip": skip,
                "size": png.stat().st_size,
            }
            KIT_PNGS[kit_name].append(entry)
            ALL_PNGS.append(entry)

# Also scan old thumbnails as fallback (figma_library_v2/thumbnails/)
THUMBS_DIR = BASE_DIR.parent / "figma_library_v2" / "thumbnails"
KIT_INDEX_PATH = BASE_DIR.parent / "03_Design" / "KIT_INDEX.json"

FK_TO_KIT = {}
if KIT_INDEX_PATH.exists():
    with open(KIT_INDEX_PATH, "r", encoding="utf-8") as f:
        ki = json.load(f)
    for name, data in ki.items():
        FK_TO_KIT[data.get("file_key", "")] = name
    FK_TO_KIT["CiyOckN4TAM0u6mfSsl4QI"] = "Core Dashboard Builder"
    FK_TO_KIT["t5IRTNkDbSGsiLrtawggae"] = "Tuskter CRM"

# Track which kits already have exported PNGs
kits_with_exports = set(KIT_PNGS.keys())

if THUMBS_DIR.exists():
    for cat_dir in sorted(THUMBS_DIR.iterdir()):
        if not cat_dir.is_dir():
            continue
        cat = cat_dir.name
        for fk_dir in sorted(cat_dir.iterdir()):
            if not fk_dir.is_dir():
                continue
            fk = fk_dir.name
            kit_name = FK_TO_KIT.get(fk, None)
            if kit_name is None:
                continue
            # Skip if we already have fresh exports for this kit
            if kit_name in kits_with_exports:
                continue
            for png in sorted(fk_dir.glob("*.png")):
                parts = png.stem.split("_", 2)
                display_name = parts[2] if len(parts) >= 3 else png.stem
                lower = display_name.lower()
                skip = any(x in lower for x in ["dark", "mobile", "tablet", "ipad", "android"])
                entry = {
                    "path": f"__thumbs__/{cat}/{fk}/{png.name}",
                    "cat": cat,
                    "kit": kit_name,
                    "name": display_name,
                    "file": png.name,
                    "skip": skip,
                    "size": png.stat().st_size,
                }
                KIT_PNGS[kit_name].append(entry)
                ALL_PNGS.append(entry)

# Filter light desktop only
LIGHT_PNGS = [p for p in ALL_PNGS if not p["skip"]]

# Build kit summary
KIT_SUMMARY = []
for kit_name in sorted(KIT_PNGS.keys()):
    pngs = KIT_PNGS[kit_name]
    light = [p for p in pngs if not p["skip"]]
    screens = [p for p in light if p["cat"] == "screens"]
    comps = [p for p in light if p["cat"] == "components"]
    source = "exported" if kit_name in kits_with_exports else "thumbnails"
    KIT_SUMMARY.append({
        "name": kit_name,
        "total": len(pngs),
        "light": len(light),
        "screens": len(screens),
        "components": len(comps),
        "dark_mobile": len(pngs) - len(light),
        "source": source,
    })

print(f"Total PNGs: {len(ALL_PNGS)}, Light desktop: {len(LIGHT_PNGS)}")
print(f"Kits with fresh exports: {len(kits_with_exports)}")
print(f"Kits from old thumbnails: {len(KIT_PNGS) - len(kits_with_exports)}")
print(f"Total kits: {len(KIT_SUMMARY)}")

# Pre-serialize
API_KITS = json.dumps({"kits": KIT_SUMMARY}).encode()


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        qs = urllib.parse.parse_qs(parsed.query)

        if path == "/" or path == "/index.html":
            self._file(BASE_DIR / "gallery.html", "text/html")
        elif path == "/api/summary":
            self._bytes(API_KITS, "application/json")
        elif path == "/api/kit":
            kit = qs.get("name", [""])[0]
            light_only = qs.get("light", ["1"])[0] == "1"
            cat_filter = qs.get("cat", [""])[0]  # "screens" or "components" or ""
            pngs = KIT_PNGS.get(kit, [])
            if light_only:
                pngs = [p for p in pngs if not p["skip"]]
            if cat_filter:
                pngs = [p for p in pngs if p["cat"] == cat_filter]
            self._bytes(json.dumps(pngs).encode(), "application/json")
        elif path == "/api/search":
            q = qs.get("q", [""])[0].lower()
            results = [p for p in LIGHT_PNGS if q in p["name"].lower() or q in p["kit"].lower()][:200]
            self._bytes(json.dumps(results).encode(), "application/json")
        elif path.startswith("/img/"):
            rel = urllib.parse.unquote(path[5:])
            # Check if it's an old thumbnail reference
            if rel.startswith("__thumbs__/"):
                full = THUMBS_DIR / rel[11:]
            else:
                full = BASE_DIR / rel
            if full.exists() and full.is_file():
                self._file(full, "image/png", cache=True)
            else:
                self.send_error(404)
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == "/api/save":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            save_path = BASE_DIR / "SELECTED_SCREENS.json"
            with open(save_path, "w", encoding="utf-8") as f:
                f.write(body.decode("utf-8"))
            self._bytes(json.dumps({"ok": True, "path": str(save_path)}).encode(), "application/json")
        else:
            self.send_error(404)

    def _bytes(self, data, ct):
        self.send_response(200)
        self.send_header("Content-Type", ct)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(data)

    def _file(self, fp, ct, cache=False):
        mode = "rb" if ct.startswith("image") else "r"
        enc = None if ct.startswith("image") else "utf-8"
        with open(fp, mode, encoding=enc) as f:
            data = f.read()
        if isinstance(data, str):
            data = data.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", ct)
        self.send_header("Content-Length", str(len(data)))
        if cache:
            self.send_header("Cache-Control", "max-age=86400")
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):
        msg = str(args[0]) if args else ""
        if "/img/" not in msg:
            super().log_message(fmt, *args)


if __name__ == "__main__":
    os.chdir(str(BASE_DIR))
    socketserver.TCPServer.allow_reuse_address = True
    print(f"\n>>> Gallery: http://localhost:{PORT}")
    print(">>> Press Ctrl+C to stop\n")
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        webbrowser.open(f"http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")
