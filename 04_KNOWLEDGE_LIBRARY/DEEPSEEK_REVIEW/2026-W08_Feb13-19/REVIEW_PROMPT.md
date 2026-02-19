# DeepSeek Review Instructions

## Your Task

You are reviewing 7 days of work (Feb 13-19, 2026) on Enterprise OS V7 — a knowledge architecture and business automation platform. The owner (John) needs a complete, detailed record of everything that was done, every problem encountered, every solution found, and every document created.

## What To Produce

Create ONE comprehensive document with these sections:

### 1. DAY-BY-DAY WORK LOG
For each day (Feb 13, 14, 15, 16, 17, 18):
- What projects were worked on
- What was built/created
- What problems/errors occurred
- What solutions were found
- What decisions were made and why
- What files were created and their exact paths
- What API calls were made and their costs
- What counts/metrics were produced (EXACT numbers)

### 2. COMPLETE FILE INVENTORY
Every file created or modified across all 7 days. For each:
- Full path
- What it contains (1-2 sentence description)
- Which session created it
- Current status (active/stale/superseded)

### 3. ERROR & SOLUTION LOG
Every error, bug, or problem that occurred:
- What went wrong
- Root cause
- How it was fixed
- Prevention rule going forward

### 4. LOCKED COUNTS & METRICS
All verified numbers from the work. These are IMMUTABLE once verified:
- File counts per project area
- Screen counts per kit
- Template counts per kit
- Database record counts
- API costs

### 5. PROJECT STATUS SUMMARY
For each active project:
- What's DONE (with evidence)
- What's IN PROGRESS
- What's BLOCKED and by what
- What's the NEXT action

### 6. SYSTEM GAPS IDENTIFIED
Problems with the Enterprise OS system itself:
- What failed (context loss, wrong counts, missing docs)
- What was built to fix it
- What still needs fixing

### 7. KEY DOCUMENTS CREATED (with descriptions)
The most important documents and what role they play:
- Where they live
- What they're for
- Who reads them (LLM vs human)

## Files To Review

Read these files in this order:

**Session summaries (quick context):**
- SUMMARY_2026-02-13_session_01.md
- SUMMARY_2026-02-14_session_01.md
- SUMMARY_2026-02-15_session_01.md
- SUMMARY_2026-02-16_session_01.md
- SUMMARY_2026-02-16_session_02.md
- SUMMARY_2026-02-17_session_01.md
- SUMMARY_2026-02-17_session_02.md
- SUMMARY_2026-02-18_session_01.md

**Full transcripts (detailed work):**
- TRANSCRIPT_2026-02-14_session_01_full.md
- TRANSCRIPT_2026-02-15_session_01_full.md
- TRANSCRIPT_2026-02-16_session_02_full.md
- TRANSCRIPT_2026-02-17_session_02_full.md
- TRANSCRIPT_2026-02-18_session_01_full.md

**External session (another Claude instance):**
- EXTERNAL_claude_discussion_enterpriseOS.txt

**Reference docs (for context):**
- REF_V7_OPERATIONS_MANUAL.md
- REF_MASTER_CONTEXT.md
- REF_UI_LIBRARY_BUILD_METHODOLOGY.md
- SESSION_INDEX.md

## Important Context

- The system has 8 top-level components (00_SYSTEM_ROOT through 08_OPERATIONS)
- 23 domain pillars (PIL_01 through PIL_23)
- Active projects: Property Connect London (revenue), UI Component Library (tooling), Enterprise OS (the system itself), Fitness Platform (personal health)
- The UI Library work involved a 5-phase Figma pipeline: JSON extraction -> structure analysis -> layout dedup -> PNG export -> PRD matching
- There were multiple instances of errors: wrong counts, deleted files, context loss between sessions
- The system is being fixed with: SYSTEM_MANIFEST.md, PROJECT_STATE.md per project, daily checklist, weekly rollups

## Output Format

Plain markdown. Be exhaustive. Miss nothing. Every path, every count, every decision. This document becomes the canonical record of this week's work.
