#!/usr/bin/env python3
"""
Figma Design Token Extractor

Extracts design tokens from Figma files via API:
- Color styles (primitives + semantic)
- Text styles (typography scale)
- Effect styles (shadows, blurs)
- Variables (new token system with modes)
- Spacing, radius, and other design decisions from component inspection

Usage:
    python figma_extract_tokens.py <file_key> [--output tokens.json]
    python figma_extract_tokens.py --batch kits.json  # Process multiple kits

Requires FIGMA_TOKEN environment variable or --token argument.
"""

import os
import sys
import json
import re
import argparse
import requests
from datetime import datetime
from collections import defaultdict
from pathlib import Path

FIGMA_API_BASE = "https://api.figma.com/v1"

def get_token():
    """Get Figma API token from env or argument."""
    return os.environ.get("FIGMA_TOKEN") or ""

def api_get(endpoint: str, token: str) -> dict:
    """Make authenticated GET request to Figma API."""
    headers = {"X-Figma-Token": token}
    url = f"{FIGMA_API_BASE}{endpoint}"
    response = requests.get(url, headers=headers, timeout=60)
    if response.status_code != 200:
        print(f"[!] API error {response.status_code}: {response.text[:200]}")
        return {}
    return response.json()


def extract_styles(file_key: str, token: str) -> dict:
    """Extract all styles from a Figma file."""
    print(f"[*] Extracting styles from {file_key}...")

    data = api_get(f"/files/{file_key}/styles", token)
    if not data or "meta" not in data:
        print("[!] No styles found or API error")
        return {"colors": [], "text": [], "effects": []}

    styles = data.get("meta", {}).get("styles", [])

    result = {
        "colors": [],
        "text": [],
        "effects": [],
        "grids": []
    }

    for style in styles:
        style_type = style.get("style_type", "").upper()
        style_info = {
            "key": style.get("key"),
            "name": style.get("name"),
            "description": style.get("description", ""),
            "node_id": style.get("node_id")
        }

        if style_type == "FILL":
            result["colors"].append(style_info)
        elif style_type == "TEXT":
            result["text"].append(style_info)
        elif style_type == "EFFECT":
            result["effects"].append(style_info)
        elif style_type == "GRID":
            result["grids"].append(style_info)

    print(f"    Colors: {len(result['colors'])}")
    print(f"    Text: {len(result['text'])}")
    print(f"    Effects: {len(result['effects'])}")
    print(f"    Grids: {len(result['grids'])}")

    return result


def extract_variables(file_key: str, token: str) -> dict:
    """Extract variables (design tokens) from a Figma file."""
    print(f"[*] Extracting variables from {file_key}...")

    # Try the variables endpoint (requires paid plan for some files)
    data = api_get(f"/files/{file_key}/variables/local", token)

    if not data or "meta" not in data:
        print("[!] No variables found (file may not use Variables, or requires different access)")
        return {"collections": [], "variables": []}

    meta = data.get("meta", {})
    collections = meta.get("variableCollections", {})
    variables = meta.get("variables", {})

    result = {
        "collections": [],
        "variables": []
    }

    # Process collections (e.g., "Primitives", "Semantic", "Component")
    for coll_id, coll in collections.items():
        coll_info = {
            "id": coll_id,
            "name": coll.get("name"),
            "modes": [{"id": m.get("modeId"), "name": m.get("name")} for m in coll.get("modes", [])],
            "variable_count": len(coll.get("variableIds", []))
        }
        result["collections"].append(coll_info)

    # Process variables
    for var_id, var in variables.items():
        var_info = {
            "id": var_id,
            "name": var.get("name"),
            "resolved_type": var.get("resolvedType"),  # COLOR, FLOAT, STRING, BOOLEAN
            "collection_id": var.get("variableCollectionId"),
            "values_by_mode": var.get("valuesByMode", {}),
            "description": var.get("description", ""),
            "scopes": var.get("scopes", [])
        }
        result["variables"].append(var_info)

    print(f"    Collections: {len(result['collections'])}")
    print(f"    Variables: {len(result['variables'])}")

    return result


def rgba_to_hex(r, g, b, a=1):
    """Convert RGBA (0-1 range) to hex color."""
    return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"


def extract_file_tokens(file_key: str, token: str) -> dict:
    """Extract detailed token values by parsing the file structure."""
    print(f"[*] Extracting file structure for token values...")

    # Get full file - need deeper depth to find token pages
    data = api_get(f"/files/{file_key}?depth=3", token)

    if not data or "document" not in data:
        print("[!] Could not fetch file structure")
        return {}

    result = {
        "file_name": data.get("name", ""),
        "last_modified": data.get("lastModified", ""),
        "color_values": [],
        "text_values": [],
        "effect_values": [],
        "component_sets": [],
        "extracted_colors": [],
        "extracted_typography": [],
        "extracted_effects": []
    }

    # Extract published styles with their values
    styles = data.get("styles", {})

    for style_id, style in styles.items():
        style_data = {
            "id": style_id,
            "name": style.get("name", ""),
            "type": style.get("styleType", ""),
            "description": style.get("description", "")
        }

        style_type = style.get("styleType", "").upper()
        if style_type == "FILL":
            result["color_values"].append(style_data)
        elif style_type == "TEXT":
            result["text_values"].append(style_data)
        elif style_type == "EFFECT":
            result["effect_values"].append(style_data)

    # Deep extraction from node tree
    seen_colors = set()
    seen_fonts = set()

    def extract_from_node(node, path=""):
        node_name = node.get("name", "")
        node_type = node.get("type", "")

        # Extract colors from fills
        fills = node.get("fills", [])
        for fill in fills:
            if fill.get("type") == "SOLID" and fill.get("visible", True):
                color = fill.get("color", {})
                if color:
                    hex_val = rgba_to_hex(color.get("r", 0), color.get("g", 0), color.get("b", 0))
                    opacity = fill.get("opacity", 1)
                    color_key = f"{hex_val}_{opacity}"
                    if color_key not in seen_colors:
                        seen_colors.add(color_key)
                        result["extracted_colors"].append({
                            "hex": hex_val,
                            "opacity": opacity,
                            "source_node": node_name,
                            "source_path": path,
                            "rgba": color
                        })

        # Extract typography from text nodes
        if node_type == "TEXT":
            style = node.get("style", {})
            if style:
                font_key = f"{style.get('fontFamily')}_{style.get('fontSize')}_{style.get('fontWeight')}"
                if font_key not in seen_fonts:
                    seen_fonts.add(font_key)
                    result["extracted_typography"].append({
                        "font_family": style.get("fontFamily"),
                        "font_size": style.get("fontSize"),
                        "font_weight": style.get("fontWeight"),
                        "line_height": style.get("lineHeightPx"),
                        "letter_spacing": style.get("letterSpacing"),
                        "text_align": style.get("textAlignHorizontal"),
                        "source_node": node_name,
                        "source_path": path
                    })

        # Extract effects (shadows, blurs)
        effects = node.get("effects", [])
        for effect in effects:
            if effect.get("visible", True):
                effect_type = effect.get("type")
                effect_data = {
                    "type": effect_type,
                    "source_node": node_name,
                    "source_path": path
                }
                if effect_type in ["DROP_SHADOW", "INNER_SHADOW"]:
                    color = effect.get("color", {})
                    effect_data.update({
                        "color": rgba_to_hex(color.get("r", 0), color.get("g", 0), color.get("b", 0)),
                        "opacity": color.get("a", 1),
                        "offset_x": effect.get("offset", {}).get("x", 0),
                        "offset_y": effect.get("offset", {}).get("y", 0),
                        "radius": effect.get("radius", 0),
                        "spread": effect.get("spread", 0)
                    })
                elif effect_type in ["LAYER_BLUR", "BACKGROUND_BLUR"]:
                    effect_data["radius"] = effect.get("radius", 0)
                result["extracted_effects"].append(effect_data)

        # Find component sets
        if node_type == "COMPONENT_SET":
            result["component_sets"].append({
                "name": node_name,
                "path": path,
                "children_count": len(node.get("children", []))
            })

        # Recurse into children
        for child in node.get("children", []):
            extract_from_node(child, f"{path}/{node_name}")

    extract_from_node(data.get("document", {}))

    print(f"    Component sets: {len(result['component_sets'])}")
    print(f"    Extracted colors: {len(result['extracted_colors'])}")
    print(f"    Extracted typography: {len(result['extracted_typography'])}")
    print(f"    Extracted effects: {len(result['extracted_effects'])}")

    return result


def parse_color_name(name: str) -> dict:
    """Parse a color style name to extract semantic meaning."""
    # Common patterns in design systems:
    # gray/50, gray/100, gray/200...
    # primary/500, secondary/300
    # bg-primary, text-secondary
    # Colors/Primitives/Gray/50

    parts = re.split(r'[/\-_]', name.lower())

    result = {
        "raw_name": name,
        "normalized": "-".join(parts),
        "category": None,
        "shade": None,
        "semantic_role": None
    }

    # Detect category
    color_categories = ["gray", "grey", "slate", "zinc", "neutral", "stone",
                       "red", "orange", "amber", "yellow", "lime", "green",
                       "emerald", "teal", "cyan", "sky", "blue", "indigo",
                       "violet", "purple", "fuchsia", "pink", "rose",
                       "primary", "secondary", "accent", "success", "warning",
                       "error", "danger", "info"]

    for part in parts:
        if part in color_categories:
            result["category"] = part
        if part.isdigit():
            result["shade"] = int(part)

    # Detect semantic role
    semantic_patterns = {
        "bg": "background",
        "background": "background",
        "text": "text",
        "foreground": "text",
        "fg": "text",
        "border": "border",
        "stroke": "border",
        "outline": "border",
        "surface": "surface",
        "overlay": "overlay"
    }

    for part in parts:
        if part in semantic_patterns:
            result["semantic_role"] = semantic_patterns[part]

    return result


def parse_text_style_name(name: str) -> dict:
    """Parse a text style name to extract typography info."""
    parts = re.split(r'[/\-_\s]', name.lower())

    result = {
        "raw_name": name,
        "normalized": "-".join(parts),
        "category": None,  # display, heading, body, label, caption
        "size": None,      # xs, sm, md, lg, xl, 2xl...
        "weight": None     # regular, medium, semibold, bold
    }

    size_patterns = {
        "2xs": "2xs", "xxs": "2xs",
        "xs": "xs", "xsmall": "xs",
        "sm": "sm", "small": "sm",
        "md": "md", "medium": "md", "base": "md",
        "lg": "lg", "large": "lg",
        "xl": "xl", "xlarge": "xl",
        "2xl": "2xl", "xxl": "2xl",
        "3xl": "3xl", "4xl": "4xl", "5xl": "5xl", "6xl": "6xl"
    }

    category_patterns = {
        "display": "display",
        "heading": "heading", "h1": "heading", "h2": "heading", "h3": "heading",
        "title": "heading",
        "body": "body", "paragraph": "body", "text": "body",
        "label": "label",
        "caption": "caption",
        "button": "button", "btn": "button",
        "link": "link"
    }

    weight_patterns = {
        "regular": "regular", "normal": "regular",
        "medium": "medium",
        "semibold": "semibold", "semi": "semibold",
        "bold": "bold"
    }

    for part in parts:
        if part in size_patterns:
            result["size"] = size_patterns[part]
        if part in category_patterns:
            result["category"] = category_patterns[part]
        if part in weight_patterns:
            result["weight"] = weight_patterns[part]

    return result


def build_token_taxonomy(styles: dict, variables: dict, file_info: dict) -> dict:
    """Build a structured token taxonomy from extracted data."""

    taxonomy = {
        "colors": {
            "primitives": [],    # Raw color values (gray-50, primary-500)
            "semantic": []       # Mapped colors (bg-primary, text-secondary)
        },
        "typography": {
            "scale": [],         # Size scale (text-xs, text-sm, text-base...)
            "styles": []         # Full styles (display-2xl-bold, body-md-regular)
        },
        "effects": {
            "shadows": [],
            "blurs": []
        },
        "spacing": [],           # Extracted from component analysis
        "radius": [],
        "meta": {
            "file_name": file_info.get("file_name", ""),
            "extracted_at": datetime.now().isoformat(),
            "source_file_key": file_info.get("file_key", "")
        }
    }

    # Process color styles
    for color in styles.get("colors", []):
        parsed = parse_color_name(color.get("name", ""))
        color_entry = {
            **color,
            **parsed
        }

        if parsed.get("semantic_role"):
            taxonomy["colors"]["semantic"].append(color_entry)
        else:
            taxonomy["colors"]["primitives"].append(color_entry)

    # Process text styles
    for text in styles.get("text", []):
        parsed = parse_text_style_name(text.get("name", ""))
        text_entry = {
            **text,
            **parsed
        }
        taxonomy["typography"]["styles"].append(text_entry)

    # Process effect styles
    for effect in styles.get("effects", []):
        name_lower = effect.get("name", "").lower()
        if "shadow" in name_lower or "elevation" in name_lower:
            taxonomy["effects"]["shadows"].append(effect)
        elif "blur" in name_lower:
            taxonomy["effects"]["blurs"].append(effect)
        else:
            taxonomy["effects"]["shadows"].append(effect)  # Default to shadow

    # Process variables (if available)
    if variables.get("variables"):
        for var in variables["variables"]:
            var_type = var.get("resolved_type", "")
            var_name = var.get("name", "").lower()

            if var_type == "COLOR":
                parsed = parse_color_name(var.get("name", ""))
                var_entry = {**var, **parsed, "source": "variable"}
                if parsed.get("semantic_role"):
                    taxonomy["colors"]["semantic"].append(var_entry)
                else:
                    taxonomy["colors"]["primitives"].append(var_entry)

            elif var_type == "FLOAT":
                # Could be spacing, radius, or other numeric token
                if any(x in var_name for x in ["space", "gap", "padding", "margin"]):
                    taxonomy["spacing"].append(var)
                elif any(x in var_name for x in ["radius", "corner", "round"]):
                    taxonomy["radius"].append(var)

    return taxonomy


def extract_kit_tokens(file_key: str, token: str, output_path: str = None) -> dict:
    """Full token extraction pipeline for a single kit."""

    print(f"\n{'='*60}")
    print(f"EXTRACTING TOKENS: {file_key}")
    print(f"{'='*60}\n")

    # Extract all data
    styles = extract_styles(file_key, token)
    variables = extract_variables(file_key, token)
    file_info = extract_file_tokens(file_key, token)
    file_info["file_key"] = file_key

    # Build taxonomy
    taxonomy = build_token_taxonomy(styles, variables, file_info)

    # Summary
    print(f"\n[+] Token Summary:")
    print(f"    Color primitives: {len(taxonomy['colors']['primitives'])}")
    print(f"    Color semantic: {len(taxonomy['colors']['semantic'])}")
    print(f"    Typography styles: {len(taxonomy['typography']['styles'])}")
    print(f"    Shadows: {len(taxonomy['effects']['shadows'])}")
    print(f"    Spacing tokens: {len(taxonomy['spacing'])}")
    print(f"    Radius tokens: {len(taxonomy['radius'])}")

    # Save if output path provided
    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump({
                "styles_raw": styles,
                "variables_raw": variables,
                "file_info": file_info,
                "taxonomy": taxonomy
            }, f, indent=2, ensure_ascii=False)
        print(f"\n[+] Saved to: {output_path}")

    return taxonomy


def batch_extract(kits_file: str, token: str, output_dir: str) -> dict:
    """Extract tokens from multiple kits."""

    with open(kits_file, 'r', encoding='utf-8') as f:
        kits = json.load(f)

    all_tokens = {}

    for kit in kits:
        file_key = kit.get("file_key") or kit.get("key")
        kit_name = kit.get("name", file_key)

        if not file_key:
            continue

        output_path = os.path.join(output_dir, f"{kit_name.replace(' ', '_')}_tokens.json")

        try:
            taxonomy = extract_kit_tokens(file_key, token, output_path)
            all_tokens[kit_name] = taxonomy
        except Exception as e:
            print(f"[!] Error processing {kit_name}: {e}")

    # Save combined
    combined_path = os.path.join(output_dir, "all_tokens_combined.json")
    with open(combined_path, 'w', encoding='utf-8') as f:
        json.dump(all_tokens, f, indent=2, ensure_ascii=False)
    print(f"\n[+] Combined tokens saved to: {combined_path}")

    return all_tokens


def main():
    parser = argparse.ArgumentParser(description="Extract design tokens from Figma files")
    parser.add_argument("file_key", nargs="?", help="Figma file key to extract from")
    parser.add_argument("--batch", help="JSON file with list of kits to process")
    parser.add_argument("--output", "-o", default="tokens.json", help="Output file path")
    parser.add_argument("--token", "-t", help="Figma API token (or set FIGMA_TOKEN env var)")

    args = parser.parse_args()

    token = args.token or get_token()
    if not token:
        print("Error: No Figma token provided. Set FIGMA_TOKEN or use --token")
        sys.exit(1)

    if args.batch:
        output_dir = os.path.dirname(args.output) or "figma_library_v2/tokens"
        batch_extract(args.batch, token, output_dir)
    elif args.file_key:
        extract_kit_tokens(args.file_key, token, args.output)
    else:
        print("Error: Provide a file_key or --batch file")
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
