#!/usr/bin/env python3
"""
Enterprise_OS V7 — DeepSeek Weekly Review Runner

Reads all files from a review folder, sends them to DeepSeek API with the
review prompt, and saves the comprehensive review document.

Usage:
    python deepseek_review.py
    python deepseek_review.py --folder "04_KNOWLEDGE_LIBRARY/DEEPSEEK_REVIEW/2026-W08_Feb13-19"
"""

import os
import sys
import json
import time
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERROR: 'requests' not installed. Run: pip install requests")
    sys.exit(1)

# ─── Configuration ───────────────────────────────────────────────────────────

V7_ROOT = Path(r"C:\Users\under\Downloads\ENTERPRISE_OS_V7")
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "sk-37c6535a8de54acdac169dc6b0045ac9")
DEEPSEEK_API_URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-chat"

# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Run DeepSeek weekly review")
    parser.add_argument("--folder", default="04_KNOWLEDGE_LIBRARY/DEEPSEEK_REVIEW/2026-W08_Feb13-19",
                        help="Review folder relative to V7_ROOT")
    parser.add_argument("--output", default=None, help="Output file path (default: REVIEW_OUTPUT.md in folder)")
    args = parser.parse_args()

    review_dir = V7_ROOT / args.folder
    if not review_dir.exists():
        print(f"ERROR: Review folder not found: {review_dir}")
        sys.exit(1)

    output_path = Path(args.output) if args.output else review_dir / "REVIEW_OUTPUT.md"

    # ─── Read the review prompt ───
    prompt_file = review_dir / "REVIEW_PROMPT.md"
    if not prompt_file.exists():
        print(f"ERROR: REVIEW_PROMPT.md not found in {review_dir}")
        sys.exit(1)

    review_prompt = prompt_file.read_text(encoding="utf-8")
    print(f"[1/4] Loaded review prompt ({len(review_prompt)} chars)")

    # ─── Read all files in order ───
    # Read summaries first (quick context), then transcripts, then reference docs
    summaries = sorted(review_dir.glob("SUMMARY_*.md"))
    transcripts = sorted(review_dir.glob("TRANSCRIPT_*.md"))
    externals = sorted(review_dir.glob("EXTERNAL_*.txt"))
    references = sorted(review_dir.glob("REF_*.md"))
    index_files = [f for f in review_dir.glob("SESSION_INDEX.md")]

    all_files = summaries + transcripts + externals + references + index_files
    # Exclude prompt and output files
    all_files = [f for f in all_files if f.name not in ("REVIEW_PROMPT.md", "REVIEW_OUTPUT.md")]

    combined_content = []
    total_chars = 0
    for f in all_files:
        content = f.read_text(encoding="utf-8", errors="replace")
        header = f"\n\n{'='*80}\n## FILE: {f.name}\n{'='*80}\n\n"
        combined_content.append(header + content)
        total_chars += len(content)

    all_content = "\n".join(combined_content)
    print(f"[2/4] Loaded {len(all_files)} files ({total_chars:,} chars / ~{total_chars//4:,} tokens)")

    # ─── Build the API request ───
    system_msg = """You are a meticulous technical reviewer and documentation specialist.
You produce exhaustive, detailed reviews that miss nothing.
Every path, every count, every decision must be captured.
Output in clean markdown format."""

    user_msg = f"""{review_prompt}

---

# FILES TO REVIEW

The following {len(all_files)} files contain all the work from this week:

{all_content}

---

Now produce the comprehensive review document as specified in the instructions above.
Be exhaustive. Miss nothing. Every path, every count, every decision."""

    print(f"[3/4] Sending to DeepSeek API ({len(user_msg):,} chars)...")
    print(f"       Model: {MODEL}")
    print(f"       This may take 2-5 minutes...")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg}
        ],
        "temperature": 0.3,
        "max_tokens": 8192,
        "stream": False
    }

    start_time = time.time()

    try:
        response = requests.post(
            DEEPSEEK_API_URL,
            headers=headers,
            json=payload,
            timeout=300  # 5 minute timeout
        )
        elapsed = time.time() - start_time

        if response.status_code != 200:
            print(f"ERROR: DeepSeek API returned {response.status_code}")
            print(f"Response: {response.text[:1000]}")
            # Save error for debugging
            error_path = review_dir / "REVIEW_ERROR.json"
            error_path.write_text(json.dumps({
                "status_code": response.status_code,
                "response": response.text[:2000],
                "elapsed_seconds": elapsed
            }, indent=2))
            sys.exit(1)

        result = response.json()
        review_text = result["choices"][0]["message"]["content"]
        usage = result.get("usage", {})

        print(f"[4/4] Review received! ({elapsed:.1f}s)")
        print(f"       Tokens: {usage.get('prompt_tokens', '?')} in / {usage.get('completion_tokens', '?')} out")
        print(f"       Output: {len(review_text):,} chars")

        # ─── Save output ───
        header = f"""# WEEKLY REVIEW — 2026-W08 (Feb 13-19)

> **Generated by:** DeepSeek ({MODEL})
> **Date:** {time.strftime('%Y-%m-%d %H:%M')}
> **Input:** {len(all_files)} files, {total_chars:,} chars
> **Tokens:** {usage.get('prompt_tokens', '?')} prompt / {usage.get('completion_tokens', '?')} completion
> **Processing time:** {elapsed:.1f}s

---

{review_text}
"""
        output_path.write_text(header, encoding="utf-8")
        print(f"\n  OUTPUT SAVED: {output_path}")
        print(f"  File size: {output_path.stat().st_size:,} bytes")

        # Also save raw API response for reference
        raw_path = review_dir / "REVIEW_RAW_RESPONSE.json"
        raw_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    except requests.exceptions.Timeout:
        print(f"ERROR: Request timed out after 300s")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
