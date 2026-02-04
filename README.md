# Enterprise_OS V7

A knowledge architecture and business automation platform that stores, routes, indexes, and retrieves every piece of knowledge a business produces.

## What Is This?

Enterprise_OS is a structured file system with automated routing, ingestion pipelines, and AI-powered knowledge management. It organises business knowledge across 23 specialist domain pillars, tracks goals and sessions, and provides machine-readable indices so AI tools (Claude Code, agents, RAG systems) can navigate and contribute to the system.

## Architecture

```
ENTERPRISE_OS_V7/
├── 00_SYSTEM_ROOT/           Governance, context docs, naming rules
├── 01_NAVIGATION_CENTRE/     Goals, state snapshots, priorities
├── 02_COMMAND_DECK/          Daily sessions, agent workspaces, task queue
├── 03_CORE_ENGINE/           Scripts, indices, routing engine
├── 04_KNOWLEDGE_LIBRARY/     Content intake, extraction pipeline, RAG bundles
├── 05_TEMPLATE_HUB/          Reusable templates (agents, docs, prompts, SOPs)
├── 06_DOMAIN_PILLARS/        23 knowledge domains (PIL_01 through PIL_23)
├── 07_BUILD_FACTORY/         Active platform builds
└── 08_OPERATIONS/            Post-launch operations
```

## Quick Start

```bash
# Clone the repo
git clone [repo-url]
cd ENTERPRISE_OS_V7

# Install Python dependencies
pip install -r requirements.txt

# Generate system indices
python 03_CORE_ENGINE/SCRIPTS/generate_indices.py

# Start a work session
python 03_CORE_ENGINE/SCRIPTS/session_logger.py start "What you're working on"

# Add content to the system
# Drop files in 04_KNOWLEDGE_LIBRARY/EXTRACTION_PIPELINE/RAW_INTAKE/
python 03_CORE_ENGINE/SCRIPTS/intake_processor.py
```

## Domain Pillars

| ID | Pillar | Focus |
|----|--------|-------|
| 01 | Avatars | Customer personas and psychographics |
| 02 | Branding | Visual + verbal brand identity |
| 03 | Copy | Copywriting frameworks and formulas |
| 04 | Content | Content strategy and distribution |
| 05 | Graphics | Visual asset systems |
| 06 | Video | Video production workflows |
| 07 | UI Library | Component library (Figma→React) |
| 08 | Knowledge Ingestion | System learning pipelines |
| 09 | Roles & Skills | Virtual workforce definitions |
| 10 | Working Practices | SOPs and session protocols |
| 11 | Build Story | Build process documentation |
| 12 | Keywords | Keyword research and mapping |
| 13 | SEO | Technical SEO and site architecture |
| 14 | Navigation | Goals, routing, session management |
| 15 | Enterprise OS | System governance and evolution |
| 16 | Content Generation | Automated content pipelines |
| 17 | RAG System | Retrieval-augmented generation |
| 18 | Agent Framework | Agent definitions and orchestration |
| 19 | Property | Property Connect London |
| 20 | Fitness | Fitness platform |
| 21 | Market Research | Research frameworks and data |
| 22 | Voice Training | Voice/speaking platform |
| 23 | Dog Platform | Dog training platform |

## For AI Assistants

See `CLAUDE.md` for full system context, routing rules, and operating instructions.

## Documentation

- **System Overview:** `00_SYSTEM_ROOT/MASTER_CONTEXT.md`
- **Architecture:** `00_SYSTEM_ROOT/V7_STRUCTURE.md`
- **Routing Rules:** `03_CORE_ENGINE/ROUTING_MANIFEST.md`
- **Naming Conventions:** `00_SYSTEM_ROOT/NAMING_CONVENTIONS.md`

## License

Proprietary. All rights reserved.
