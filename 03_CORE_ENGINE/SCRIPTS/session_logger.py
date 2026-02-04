#!/usr/bin/env python3
"""
Enterprise_OS V7 — Session Logger
Track what you're working on with minimal friction.

Usage:
    python session_logger.py start "Building property chatbot MVP"
    python session_logger.py log "Finished React chat component"
    python session_logger.py log "Fixed routing bug in intake processor"
    python session_logger.py end
    python session_logger.py status
"""

import os
import sys
import json
from datetime import datetime, timezone
from pathlib import Path


def find_root():
    """Find ENTERPRISE_OS_V7 root by walking up from script location or cwd."""
    candidates = [
        Path.cwd(),
        Path.cwd() / "ENTERPRISE_OS_V7",
        Path(__file__).parent.parent.parent,  # scripts is 2 levels deep
        Path.home() / "ENTERPRISE_OS_V7",
        Path.home() / "Documents" / "ENTERPRISE_OS_V7",
    ]
    for c in candidates:
        if (c / "00_SYSTEM_ROOT").exists():
            return c
    print("ERROR: Can't find ENTERPRISE_OS_V7. Run from inside the repo or set --root.")
    sys.exit(1)


def now_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def today_str():
    return datetime.now().strftime("%Y-%m-%d")


def month_str():
    return datetime.now().strftime("%Y-%m")


def get_sessions_dir(root):
    d = root / "02_COMMAND_DECK" / "ACTIVE_SESSIONS" / month_str()
    d.mkdir(parents=True, exist_ok=True)
    return d


def get_state_file(root):
    """A small JSON file tracking the current active session."""
    f = root / "02_COMMAND_DECK" / ".current_session.json"
    return f


def get_current_session(root):
    state = get_state_file(root)
    if state.exists():
        with open(state) as f:
            return json.load(f)
    return None


def save_current_session(root, data):
    with open(get_state_file(root), "w") as f:
        json.dump(data, f, indent=2)


def clear_current_session(root):
    state = get_state_file(root)
    if state.exists():
        state.unlink()


def next_session_number(sessions_dir, date):
    """Find the next session number for today."""
    existing = list(sessions_dir.glob(f"{date}_session_*.md"))
    return len(existing) + 1


# --- Commands ---

def cmd_start(root, description):
    current = get_current_session(root)
    if current:
        print(f"⚠️  Session already active: {current['description']}")
        print(f"   Started: {current['start_time']}")
        print(f"   Use 'session_logger.py end' first, or 'session_logger.py log' to add to it.")
        return

    sessions_dir = get_sessions_dir(root)
    num = next_session_number(sessions_dir, today_str())
    filename = f"{today_str()}_session_{num:02d}.md"
    filepath = sessions_dir / filename

    content = f"""# SESSION LOG — {today_str()} #{num}

**Start:** {now_str()}
**Intent:** {description}
**Status:** Active

---

## Work Log

- [{now_str()}] Session started: {description}
"""

    with open(filepath, "w") as f:
        f.write(content)

    save_current_session(root, {
        "file": str(filepath),
        "description": description,
        "start_time": now_str(),
        "session_number": num,
        "log_count": 0,
    })

    print(f"✅ Session started: {description}")
    print(f"   File: {filepath.relative_to(root)}")
    print(f"   Use 'session_logger.py log \"what you did\"' to record progress.")


def cmd_log(root, message):
    current = get_current_session(root)
    if not current:
        print("⚠️  No active session. Use 'session_logger.py start \"description\"' first.")
        return

    filepath = Path(current["file"])
    if not filepath.exists():
        print(f"ERROR: Session file missing: {filepath}")
        clear_current_session(root)
        return

    entry = f"- [{now_str()}] {message}\n"

    with open(filepath, "a") as f:
        f.write(entry)

    current["log_count"] = current.get("log_count", 0) + 1
    save_current_session(root, current)

    print(f"✅ Logged: {message}")


def cmd_end(root):
    current = get_current_session(root)
    if not current:
        print("⚠️  No active session to end.")
        return

    filepath = Path(current["file"])
    if not filepath.exists():
        print(f"ERROR: Session file missing: {filepath}")
        clear_current_session(root)
        return

    end_block = f"""
- [{now_str()}] Session ended

---

## Session Summary

**Start:** {current['start_time']}
**End:** {now_str()}
**Intent:** {current['description']}
**Log entries:** {current.get('log_count', 0)}
**Status:** Complete
"""

    with open(filepath, "a") as f:
        f.write(end_block)

    # Update status line in file
    content = filepath.read_text()
    content = content.replace("**Status:** Active", "**Status:** Complete")
    filepath.write_text(content)

    clear_current_session(root)

    print(f"✅ Session ended: {current['description']}")
    print(f"   Duration: {current['start_time']} → {now_str()}")
    print(f"   Entries logged: {current.get('log_count', 0)}")
    print(f"   File: {filepath.relative_to(root)}")


def cmd_status(root):
    current = get_current_session(root)
    if not current:
        print("No active session.")
        print("Use 'session_logger.py start \"description\"' to begin one.")
        return

    print(f"📋 Active Session")
    print(f"   Description: {current['description']}")
    print(f"   Started: {current['start_time']}")
    print(f"   Entries: {current.get('log_count', 0)}")
    print(f"   File: {Path(current['file']).relative_to(root)}")


def cmd_today(root):
    """Show all sessions from today."""
    sessions_dir = get_sessions_dir(root)
    todays = sorted(sessions_dir.glob(f"{today_str()}_session_*.md"))

    if not todays:
        print(f"No sessions logged today ({today_str()}).")
        return

    print(f"📋 Sessions for {today_str()}:")
    for f in todays:
        content = f.read_text()
        # Extract intent line
        for line in content.split("\n"):
            if line.startswith("**Intent:**"):
                intent = line.replace("**Intent:**", "").strip()
                break
        else:
            intent = "Unknown"

        status = "Complete" if "**Status:** Complete" in content else "Active"
        print(f"   [{status}] {f.name}: {intent}")


# --- Main ---

def print_usage():
    print("""
Enterprise_OS Session Logger

Commands:
  start "description"   Start a new work session
  log "message"         Log progress to current session
  end                   End current session
  status                Show current session info
  today                 List all sessions from today

Examples:
  python session_logger.py start "Building property chatbot MVP"
  python session_logger.py log "Finished React chat component"
  python session_logger.py end
""")


def main():
    root = find_root()

    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1].lower()

    if command == "start":
        if len(sys.argv) < 3:
            print("Usage: session_logger.py start \"description of what you're working on\"")
            return
        cmd_start(root, " ".join(sys.argv[2:]))

    elif command == "log":
        if len(sys.argv) < 3:
            print("Usage: session_logger.py log \"what you just did\"")
            return
        cmd_log(root, " ".join(sys.argv[2:]))

    elif command == "end":
        cmd_end(root)

    elif command == "status":
        cmd_status(root)

    elif command == "today":
        cmd_today(root)

    else:
        print(f"Unknown command: {command}")
        print_usage()


if __name__ == "__main__":
    main()
