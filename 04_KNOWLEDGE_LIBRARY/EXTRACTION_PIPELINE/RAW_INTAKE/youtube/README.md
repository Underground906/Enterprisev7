# youtube/

Drop YouTube video transcripts here.

**What goes here:** Transcripts from YouTube videos — your own content, competitor content, educational content, research material.

**Format:** Markdown (.md), plain text (.txt), SRT subtitles (.srt).

**What happens next:**
1. `intake_processor.py` routes to the relevant pillar based on content
2. `v7_extract.py domains <file>` runs 27-domain classification
3. For sales/marketing content: `v7_extract.py copy <file>` extracts hooks, USPs, etc.

**Naming:** `YYYY-MM-DD_channel_video_title.md` (e.g. `2026-02-20_competitor_property_chatbot_demo.md`)
