# threads/

Drop AI conversation exports here.

**What goes here:** Claude Code session transcripts, Claude.ai chat exports, ChatGPT exports, DeepSeek chat exports, Gemini exports.

**Format:** Markdown (.md) preferred. Plain text (.txt) accepted.

**What happens next:**
1. `intake_processor.py` scores content and routes to the correct pillar's `01_threads/` folder
2. `v7_extract.py thread <file>` runs EKX-1 extraction (20-section structured summary)
3. Extraction output saved alongside the file AND in `EXTRACTIONS/by_mode/thread/`

**Naming:** `YYYY-MM-DD_platform_description.md` (e.g. `2026-02-20_claude_extraction_engine_build.md`)
