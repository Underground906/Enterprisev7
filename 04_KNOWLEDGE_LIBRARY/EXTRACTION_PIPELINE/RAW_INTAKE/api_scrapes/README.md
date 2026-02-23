# api_scrapes/

Drop structured data from external API scrapes here.

**What goes here:** Property listing data, competitor pricing data, market data exports, any structured data pulled from external APIs or services.

**Format:** JSON (.json), CSV (.csv), markdown (.md).

**What happens next:**
1. `intake_processor.py` routes to the relevant pillar or project folder
2. `v7_extract.py domains <file>` runs 27-domain classification
3. For project-specific data: `v7_extract.py copy <file>` extracts commercial intelligence

**Naming:** `YYYY-MM-DD_source_description.json` (e.g. `2026-02-20_rightmove_london_listings.json`)
