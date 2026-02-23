# prds/

Drop PRDs, design specs, and screen inventories here for extraction.

**What goes here:** Product Requirements Documents, screen specifications, design briefs, wireframe notes, feature specs that need intelligence extracted before filing to a project.

**Format:** Markdown (.md), PDF.

**What happens next:**
1. `intake_processor.py` routes to the relevant project's `02_Product/` folder
2. `v7_extract.py domains <file>` runs 27-domain classification
3. `v7_extract.py copy <file>` extracts: features, benefits, USPs, user problems solved

**Naming:** `YYYY-MM-DD_PRD_project_feature.md` (e.g. `2026-02-20_PRD_property_connect_chat_widget.md`)
