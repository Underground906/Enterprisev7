# research/

Drop research notes, competitor analysis, and market research here.

**What goes here:** Market research reports, competitor analysis docs, industry data, survey results, trend reports, keyword research exports.

**Format:** Markdown (.md), PDF, CSV, JSON.

**What happens next:**
1. `intake_processor.py` routes to PIL_21_MARKET_RESEARCH or the relevant project folder
2. `v7_extract.py domains <file>` runs 27-domain classification
3. `v7_extract.py copy <file>` extracts commercial intelligence (USPs, hooks, proof points)

**Naming:** `YYYY-MM-DD_type_description.md` (e.g. `2026-02-20_competitor_analysis_london_property_chatbots.md`)
