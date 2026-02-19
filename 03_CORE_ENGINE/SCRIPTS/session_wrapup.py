#!/usr/bin/env python3
"""
Enterprise_OS V7 — Fast Session Wrap-Up (< 3 minutes)

Automates end-of-session filing:
1. Creates session summary in Command Deck
2. Creates transcript in Knowledge Library
3. Updates SESSION_INDEX.md
4. Optionally updates PROJECT_STATE.md session links
5. Git add, commit, push

Usage:
    # Interactive (prompts for summary)
    python session_wrapup.py

    # With arguments
    python session_wrapup.py --summary "Built X, fixed Y, created Z" --projects "UI Library,PCL"

    # From file (Claude Code writes summary to temp, script files it)
    python session_wrapup.py --summary-file /path/to/summary.md --transcript-file /path/to/transcript.md

    # Quick mode (summary only, no transcript, auto-commit)
    python session_wrapup.py --quick --summary "Processed 5 kits through pipeline"
"""

import os
import sys
import json
import subprocess
import re
from datetime import datetime
from pathlib import Path


# ─── Configuration ───────────────────────────────────────────────────────────

V7_ROOT = Path(r"C:\Users\under\Downloads\ENTERPRISE_OS_V7")
COMMAND_DECK = V7_ROOT / "02_COMMAND_DECK" / "ACTIVE_SESSIONS"
ARCHIVE = V7_ROOT / "04_KNOWLEDGE_LIBRARY" / "SESSION_ARCHIVE"
SESSION_INDEX = ARCHIVE / "SESSION_INDEX.md"

PROJECT_MAP = {
    "UI Library": "PRJ_UI_Component_Library",
    "PCL": "PRJ_Property_Connect_London",
    "Property Connect": "PRJ_Property_Connect_London",
    "Enterprise": "PRJ_Enterprise_Platform",
    "Fitness": "PRJ_Fitness_Platform",
    "LeadEngine": "PRJ_LeadEngine_Platform",
    "Dog": "PRJ_Dog_Platform",
    "Voice": "PRJ_Voice_Training",
    "Chatbot": "PRJ_AI_Chatbot_Products",
}


# ─── Helpers ─────────────────────────────────────────────────────────────────

def now():
    return datetime.now()

def date_str():
    return now().strftime("%Y-%m-%d")

def month_str():
    return now().strftime("%Y-%m")

def time_str():
    return now().strftime("%H:%M")

def next_session_number(sessions_dir):
    """Find next session number for today."""
    today = date_str()
    existing = list(sessions_dir.glob(f"{today}_session_*.md"))
    return len(existing) + 1

def ensure_dir(path):
    path.mkdir(parents=True, exist_ok=True)
    return path

def git_run(*args):
    """Run git command in V7_ROOT, return (success, output)."""
    try:
        result = subprocess.run(
            ["git"] + list(args),
            cwd=str(V7_ROOT),
            capture_output=True,
            text=True,
            timeout=60
        )
        return result.returncode == 0, result.stdout.strip()
    except Exception as e:
        return False, str(e)


# ─── File Creation ───────────────────────────────────────────────────────────

def create_summary(sessions_dir, session_num, summary_text, projects_touched, key_outcome):
    """Create session summary in Command Deck."""
    filename = f"{date_str()}_session_{session_num:02d}.md"
    filepath = sessions_dir / filename

    # Parse projects into PIL/PRJ tags
    prj_tags = []
    for p in projects_touched:
        p_clean = p.strip()
        for alias, prj_name in PROJECT_MAP.items():
            if alias.lower() in p_clean.lower():
                prj_tags.append(prj_name)
                break
        else:
            prj_tags.append(p_clean)

    content = f"""# SESSION LOG — {date_str()} #{session_num}

**Start:** {time_str()}
**Projects:** {', '.join(prj_tags) if prj_tags else 'General'}
**Status:** Complete

---

## Summary

{summary_text}

## Key Outcome

{key_outcome if key_outcome else 'See summary above.'}

---

*Filed by session_wrapup.py at {time_str()}*
"""
    filepath.write_text(content, encoding="utf-8")
    return filepath


def create_transcript(archive_dir, session_num, transcript_text):
    """Create full transcript in Knowledge Library."""
    filename = f"{date_str()}_session_{session_num:02d}_full.md"
    filepath = archive_dir / filename

    content = f"""# FULL TRANSCRIPT — {date_str()} Session {session_num}

> Recorded: {date_str()} {time_str()}

---

{transcript_text}

---

*Filed by session_wrapup.py*
"""
    filepath.write_text(content, encoding="utf-8")
    return filepath


def update_session_index(session_num, summary_one_liner, projects_touched, key_outcome):
    """Append a row to SESSION_INDEX.md session log table."""
    if not SESSION_INDEX.exists():
        print(f"  [WARN] SESSION_INDEX.md not found at {SESSION_INDEX}")
        return False

    index_content = SESSION_INDEX.read_text(encoding="utf-8")

    prj_tags = []
    for p in projects_touched:
        p_clean = p.strip()
        for alias, prj_name in PROJECT_MAP.items():
            if alias.lower() in p_clean.lower():
                prj_tags.append(alias)
                break
        else:
            prj_tags.append(p_clean)

    new_row = f"| {date_str()} | {session_num:02d} | {summary_one_liner} | {', '.join(prj_tags)} | {key_outcome} |"

    # Append after the last table row
    lines = index_content.split("\n")
    last_table_line = -1
    for i, line in enumerate(lines):
        if line.startswith("| 2026-") or line.startswith("| 2025-"):
            last_table_line = i

    if last_table_line >= 0:
        lines.insert(last_table_line + 1, new_row)
    else:
        # No existing rows, append at end
        lines.append(new_row)

    SESSION_INDEX.write_text("\n".join(lines), encoding="utf-8")
    return True


def update_project_state(project_folder_name, session_num, what_was_done):
    """Add session link to PROJECT_STATE.md if it exists."""
    state_path = V7_ROOT / "07_BUILD_FACTORY" / project_folder_name / "PROJECT_STATE.md"
    if not state_path.exists():
        return False

    content = state_path.read_text(encoding="utf-8")

    new_row = f"| {date_str()} | session_{session_num:02d} | {what_was_done} |"

    # Find the SESSION LINKS table and append
    lines = content.split("\n")
    last_session_line = -1
    in_session_section = False
    for i, line in enumerate(lines):
        if "## SESSION LINKS" in line:
            in_session_section = True
        if in_session_section and line.startswith("| 2026-"):
            last_session_line = i

    if last_session_line >= 0:
        lines.insert(last_session_line + 1, new_row)
        state_path.write_text("\n".join(lines), encoding="utf-8")
        return True

    return False


def git_commit_and_push(session_num):
    """Stage new/changed files, commit, push."""
    print("\n  [GIT] Staging changes...")

    # Stage specific known paths (not git add -A)
    paths_to_stage = [
        f"02_COMMAND_DECK/ACTIVE_SESSIONS/{month_str()}/",
        f"04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/{month_str()}/",
        "04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/SESSION_INDEX.md",
    ]

    # Also stage any modified PROJECT_STATE.md files
    ok, diff_output = git_run("diff", "--name-only")
    if ok and diff_output:
        for line in diff_output.split("\n"):
            if "PROJECT_STATE.md" in line:
                paths_to_stage.append(line.strip())

    # Also check for untracked files in session dirs
    ok, status = git_run("status", "--porcelain")
    if ok and status:
        for line in status.split("\n"):
            line = line.strip()
            if line.startswith("??") and ("ACTIVE_SESSIONS" in line or "SESSION_ARCHIVE" in line or "DEEPSEEK_REVIEW" in line):
                filepath = line[3:].strip().strip('"')
                paths_to_stage.append(filepath)

    for p in paths_to_stage:
        git_run("add", p)

    # Check if there's anything to commit
    ok, staged = git_run("diff", "--cached", "--name-only")
    if not ok or not staged.strip():
        print("  [GIT] Nothing to commit.")
        return True

    staged_files = [f for f in staged.strip().split("\n") if f]
    print(f"  [GIT] Staging {len(staged_files)} files")

    commit_msg = f"Session {date_str()} #{session_num:02d} — wrap-up\n\nCo-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
    ok, output = git_run("commit", "-m", commit_msg)
    if not ok:
        print(f"  [GIT] Commit failed: {output}")
        return False
    print(f"  [GIT] Committed.")

    print("  [GIT] Pushing...")
    ok, output = git_run("push")
    if not ok:
        print(f"  [GIT] Push failed: {output}")
        print("  [GIT] You can push manually later: git push")
        return False

    print("  [GIT] Pushed to origin.")
    return True


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Fast session wrap-up (< 3 min)")
    parser.add_argument("--summary", "-s", help="Session summary text")
    parser.add_argument("--summary-file", help="Read summary from file")
    parser.add_argument("--transcript", "-t", help="Transcript text (short)")
    parser.add_argument("--transcript-file", help="Read transcript from file")
    parser.add_argument("--projects", "-p", help="Comma-separated project names touched")
    parser.add_argument("--outcome", "-o", help="One-line key outcome")
    parser.add_argument("--quick", "-q", action="store_true", help="Quick mode: summary only, auto-commit")
    parser.add_argument("--no-git", action="store_true", help="Skip git operations")
    parser.add_argument("--no-push", action="store_true", help="Commit but don't push")

    args = parser.parse_args()

    print(f"\n{'='*60}")
    print(f"  SESSION WRAP-UP — {date_str()} {time_str()}")
    print(f"{'='*60}\n")

    # ─── Gather inputs ───

    # Summary
    summary_text = None
    if args.summary_file:
        summary_text = Path(args.summary_file).read_text(encoding="utf-8")
    elif args.summary:
        summary_text = args.summary
    else:
        print("Enter session summary (end with empty line):")
        lines = []
        while True:
            try:
                line = input()
                if line == "":
                    break
                lines.append(line)
            except EOFError:
                break
        summary_text = "\n".join(lines)

    if not summary_text or not summary_text.strip():
        print("[ERROR] No summary provided. Aborting.")
        sys.exit(1)

    # Projects
    projects = []
    if args.projects:
        projects = [p.strip() for p in args.projects.split(",")]
    elif not args.quick:
        proj_input = input("Projects touched (comma-separated, or Enter to skip): ").strip()
        if proj_input:
            projects = [p.strip() for p in proj_input.split(",")]

    # Key outcome (one-liner for the index)
    key_outcome = args.outcome or ""
    if not key_outcome and not args.quick:
        key_outcome = input("Key outcome (one line, or Enter to skip): ").strip()
    if not key_outcome:
        # Extract first sentence of summary
        first_line = summary_text.strip().split("\n")[0]
        key_outcome = first_line[:100]

    # Summary one-liner for SESSION_INDEX
    summary_one_liner = summary_text.strip().split("\n")[0][:120]

    # Transcript
    transcript_text = None
    if args.transcript_file:
        transcript_text = Path(args.transcript_file).read_text(encoding="utf-8")
    elif args.transcript:
        transcript_text = args.transcript
    elif not args.quick:
        print("Paste transcript (or Enter to skip, Ctrl+Z to end):")
        lines = []
        try:
            first = input()
            if first:
                lines.append(first)
                while True:
                    try:
                        line = input()
                        lines.append(line)
                    except EOFError:
                        break
        except EOFError:
            pass
        if lines:
            transcript_text = "\n".join(lines)

    # ─── Create files ───

    sessions_dir = ensure_dir(COMMAND_DECK / month_str())
    archive_dir = ensure_dir(ARCHIVE / month_str())
    session_num = next_session_number(sessions_dir)

    print(f"  Session: {date_str()} #{session_num:02d}")
    print(f"  Projects: {', '.join(projects) if projects else 'General'}")
    print()

    # 1. Summary
    summary_path = create_summary(sessions_dir, session_num, summary_text, projects, key_outcome)
    print(f"  [1/5] Summary  -> {summary_path.relative_to(V7_ROOT)}")

    # 2. Transcript (if provided)
    if transcript_text:
        transcript_path = create_transcript(archive_dir, session_num, transcript_text)
        print(f"  [2/5] Transcript -> {transcript_path.relative_to(V7_ROOT)}")
    else:
        print(f"  [2/5] Transcript -> SKIPPED (no transcript provided)")

    # 3. Update SESSION_INDEX.md
    if update_session_index(session_num, summary_one_liner, projects, key_outcome):
        print(f"  [3/5] Index    -> SESSION_INDEX.md updated")
    else:
        print(f"  [3/5] Index    -> FAILED (check SESSION_INDEX.md)")

    # 4. Update PROJECT_STATE.md for each project
    updated_projects = []
    for proj in projects:
        for alias, folder in PROJECT_MAP.items():
            if alias.lower() in proj.lower():
                if update_project_state(folder, session_num, summary_one_liner):
                    updated_projects.append(folder)
                break
    if updated_projects:
        print(f"  [4/5] Projects -> Updated: {', '.join(updated_projects)}")
    else:
        print(f"  [4/5] Projects -> No PROJECT_STATE.md updates needed")

    # 5. Git
    if args.no_git:
        print(f"  [5/5] Git      -> SKIPPED (--no-git)")
    else:
        git_commit_and_push(session_num)

    # ─── Done ───

    print(f"\n{'='*60}")
    print(f"  WRAP-UP COMPLETE — {time_str()}")
    print(f"{'='*60}\n")

    # Print filed locations
    print("Files created/updated:")
    print(f"  Summary:    02_COMMAND_DECK/ACTIVE_SESSIONS/{month_str()}/{date_str()}_session_{session_num:02d}.md")
    if transcript_text:
        print(f"  Transcript: 04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/{month_str()}/{date_str()}_session_{session_num:02d}_full.md")
    print(f"  Index:      04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/SESSION_INDEX.md")
    for p in updated_projects:
        print(f"  Project:    07_BUILD_FACTORY/{p}/PROJECT_STATE.md")
    print()


if __name__ == "__main__":
    main()
