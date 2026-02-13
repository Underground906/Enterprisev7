# 03_CORE_ENGINE — README

**Body Metaphor:** The Nervous System
**Status:** Active — scripts operational, indices generated
**Standalone App Name:** Connective.ai / InfrastructureOS

---

## Purpose

The hidden conductor of Enterprise OS. The Core Engine routes signals everywhere — ensuring that if the business needs to know something, it is stored, indexed, and accessible. It manages the enterprise's wiring through deterministic routing, semantic indexing, and a centralized script library.

---

## What Belongs Here

- Scripts (Python) that power the system: ingestion, indexing, routing, search
- Database schemas (SQL, JSON)
- System indices (FILE_INDEX, DOMAIN_REGISTRY, SYSTEM_HEALTH)
- Routing rules and routing logs
- System configuration files
- The Semantic Router logic

## What Does NOT Belong Here

- Raw content or threads (go to `04_KNOWLEDGE_LIBRARY`)
- Templates or scaffolds (go to `05_TEMPLATE_HUB`)
- Domain-specific knowledge (go to `06_DOMAIN_PILLARS`)
- Project builds (go to `07_BUILD_FACTORY`)
- Session logs (go to `02_COMMAND_DECK`)

---

## Folder Structure

```
03_CORE_ENGINE/
├── CONFIG/               → System configuration files
├── INDICES/              → Generated indices and health reports
│   ├── DOMAIN_REGISTRY.json    → All 23 pillar definitions
│   ├── FILE_INDEX.json         → Master file location index
│   └── SYSTEM_HEALTH.md        → Auto-generated health report
├── ROUTING_ENGINE/       → Routing logic and execution logs
│   └── routing_logs/           → Timestamped routing decisions
├── ROUTING_MANIFEST.md   → Current routing queue (75 artifacts + 12 threads)
├── SCHEMAS/              → Database and data model definitions
├── SCRIPTS/              → All executable Python scripts
│   ├── search_api.py           → Flask search API (localhost:5000)
│   ├── generate_indices.py     → Rebuild FILE_INDEX + SYSTEM_HEALTH
│   ├── intake_processor.py     → Process RAW_INTAKE files
│   ├── session_logger.py       → Session start/log/end
│   ├── figma_*.py              → Figma API extraction suite (7 scripts)
│   ├── import_library_items.py → PostgreSQL UI library importer
│   ├── import_taxonomy.py      → Category/taxonomy importer
│   ├── reclassify_library.py   → Re-categorize library items
│   └── schema_ui_library.sql   → UI library database schema
└── 90_ARCHIVE/           → Superseded scripts and configs
```

---

## Key Systems

### 1. Routing Engine
Routes incoming content to the correct domain pillar using keyword scoring + LLM fallback.
- Rules defined in `ROUTING_MANIFEST.md`
- Logs written to `ROUTING_ENGINE/routing_logs/`
- References the 27 extraction domains from `MASTER_CONTEXT.md`

### 2. Index Generator
`generate_indices.py` scans the entire V7 tree and produces:
- `FILE_INDEX.json` — every file's path, type, and component
- `DOMAIN_REGISTRY.json` — all 23 pillar definitions
- `SYSTEM_HEALTH.md` — pillar health scores, action items

### 3. Search API
`search_api.py` runs a Flask API on localhost:5000 serving the UI component library:
- `/search` — full-text + filtered search across 19,659 items
- `/kit-categories` — Figma project groups with counts
- `/review` — mark items as kept/discarded
- Connected to PostgreSQL `ui_library` database

### 4. Figma Extraction Suite
7 scripts for extracting, cataloguing, and classifying Figma components:
- `figma_list_files.py` — enumerate all team files
- `figma_extractor.py` — extract component data via API
- `figma_extract_tokens.py` — pull design tokens (colors, typography, effects)
- `figma_classify.py` / `figma_subcategorize.py` — AI-powered categorization
- `figma_catalog.py` — build browsable catalogue
- `figma_download_images.py` — download component thumbnails

### 5. Intake Processor
`intake_processor.py` watches `04_KNOWLEDGE_LIBRARY/EXTRACTION_PIPELINE/RAW_INTAKE/` and processes new files through the routing pipeline.

---

## Chain of Provenance

Every piece of data in the system can be traced back to its source:
```
Raw Source (AI thread, PDF, URL)
    → EXTRACTION_PIPELINE/RAW_INTAKE/
    → Routing Engine (keyword score + pillar assignment)
    → routing_logs/ (timestamped decision)
    → Domain Pillar destination
    → FILE_INDEX.json (permanent record)
```

---

## Integration

| Connects To | How |
|-------------|-----|
| 00_SYSTEM_ROOT | Reads MASTER_CONTEXT.md for system rules |
| 01_NAVIGATION | Goal tracker reads/writes state snapshots |
| 02_COMMAND_DECK | Session logger writes session records |
| 04_KNOWLEDGE_LIBRARY | Intake processor routes from RAW_INTAKE |
| 06_DOMAIN_PILLARS | Routing engine sends content to correct pillar |
| 07_BUILD_FACTORY | Schemas feed into project architectures |

---

## Quick Start

1. **Run the search API:** `python SCRIPTS/search_api.py` (needs PostgreSQL `ui_library`)
2. **Regenerate indices:** `python SCRIPTS/generate_indices.py`
3. **Process new intake:** `python SCRIPTS/intake_processor.py`
4. **Start a session:** `python SCRIPTS/session_logger.py start "Your intent here"`

---

## Environment Requirements

- Python 3.11+
- PostgreSQL (for UI library)
- `FIGMA_TOKEN` env var (for Figma scripts)
- Flask, psycopg2, requests (pip packages)

---

**Last Updated:** 2026-02-13
