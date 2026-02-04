# PIL_08_KNOWLEDGE_INGESTION — CONTEXT DOC

**Purpose:** Complete context for any AI/agent working with Knowledge Ingestion  
**Version:** 2.0  
**Status:** Production (Expanding)

---

## SYSTEM OVERVIEW

The Knowledge Ingestion pillar is the **universal content entry point** for Enterprise_OS. It ingests content from any source, extracts actionable knowledge, routes it to the correct pillar, and keeps the system index updated.

**Core Function:** Transform raw content from ANY source into structured, routed, indexed knowledge.

---

## UNIVERSAL INGESTION PIPELINE

```
SOURCE → DETECT → FETCH → EXTRACT → CLASSIFY → SCORE → ROUTE → INDEX
   ↓        ↓        ↓        ↓         ↓         ↓       ↓       ↓
 Type    Change    Raw     Structured  Type/     Quality  Pillar  System
 config  detect    content  data       Domain    1-10     dest    update
```

### Pipeline Stages

| Stage | Function | Output |
|-------|----------|--------|
| **DETECT** | Identify new content (polling/webhook) | Content alert |
| **FETCH** | Retrieve raw content | Raw text/data |
| **EXTRACT** | Apply source-specific extraction | Structured fields |
| **CLASSIFY** | Determine topic and domain | Topic tags, pillar match |
| **SCORE** | Assess quality (5 dimensions) | Quality score 0-10 |
| **ROUTE** | Send to destination pillar | File in correct location |
| **INDEX** | Update system indices | Index entries |

---

## SOURCE TYPES

### AI Chats (EKX-1)
```yaml
extraction: 20-section methodology
sections: [narrative, objectives, decisions, SOPs, scripts, inputs/outputs, 
           errors, blockers, status, progress, refinements, dependencies,
           entity maps, glossary, future, pending, open questions, 
           meta-observations, key learnings, reusable assets]
```

### YouTube Transcripts
```yaml
extraction: Transcript + AI analysis
output: Full text, key topics, quotes, timestamps
routing: By channel category + content
```

### RSS Feeds
```yaml
extraction: Full-text + entity extraction
output: Article text, author, entities, sentiment
routing: By feed category + topic
```

### Web Scraping (Apify)
```yaml
extraction: Structured field mapping
output: Property listings, prices, planning data
routing: PIL_19_PROPERTY, PIL_21_MARKET_RESEARCH
```

### Documents (PDFs/Books)
```yaml
extraction: Unstructured.io + AI processing
output: Text chunks, tables, key insights
routing: By document type + content
```

---

## QUALITY SCORING

### Five Dimensions

| Dimension | Weight | Description |
|-----------|--------|-------------|
| **Completeness** | 0.25 | How much expected content is present |
| **Actionability** | 0.30 | Can you do something with this |
| **Uniqueness** | 0.20 | Is this new information |
| **Authority** | 0.15 | Is the source trustworthy |
| **Freshness** | 0.10 | How recent is this |

### Score Thresholds
```
≥ 7.0 → Canon candidate (auto-route)
5.0-6.9 → Review queue
< 5.0 → Archive or discard
```

---

## ROUTING RULES

### Topic → Pillar Mapping

```yaml
keywords_to_pillar:
  [navigation, goals, 5A, planning, roadmap]: PIL_14_NAVIGATION
  [copy, headline, persuasion, sales, CTA]: PIL_03_COPY
  [brand, identity, visual, logo, voice]: PIL_02_BRANDING
  [property, estate, london, housing, mortgage]: PIL_19_PROPERTY
  [ui, component, figma, react, tailwind]: PIL_07_UI_LIBRARY
  [extraction, ingestion, parsing, indexing]: PIL_08_KNOWLEDGE_INGESTION
  [market, research, segment, competition]: PIL_21_MARKET_RESEARCH
  [fitness, training, exercise, kettlebell]: PIL_20_FITNESS
  [video, youtube, script, production]: PIL_06_VIDEO
  [seo, ranking, keywords, backlinks]: PIL_13_SEO
  [agent, automation, orchestration, ai]: PIL_18_AGENT_FRAMEWORK
```

### Confidence Thresholds
```
> 0.8 confidence → Auto-route
0.5-0.8 → Route with review flag
< 0.5 → Route to UNROUTED folder
```

---

## INDEX STRUCTURE

### MASTER_CONTENT_INDEX.md
```
- Total items across system
- Counts by source type
- Counts by destination pillar
- Recent additions (last 24h)
- Processing queue status
```

### SOURCE_REGISTRY.md
```
- Active YouTube channels
- Active RSS feeds
- Active scrapers
- Last check timestamps
- Item counts per source
```

### PROCESSING_QUEUE.md
```
- Items awaiting processing
- Items in review
- Failed items (need attention)
```

---

## FOLDER STRUCTURE

```
PIL_08_KNOWLEDGE_INGESTION/
├── 00_CANON/                → Production methodologies
├── 01_INPUTS/               → Raw content staging
│   ├── threads_raw/
│   ├── youtube_transcripts/
│   ├── rss_feeds/
│   ├── scraped_data/
│   └── books_pdfs/
├── 02_INVENTORIES/          → System tracking
├── 03_PIPELINES/            → Source-specific workflows
├── 04_CANON_RULES/          → Standards
├── 05_DISTRIBUTION/         → Routing config
├── 06_GOVERNANCE/           → Policies
├── 01_threads/
├── 02_artifacts/
└── 90_ARCHIVE/
```

---

## EKX-1 METHODOLOGY (AI Chats)

### 20 Extraction Sections

1. **Narrative & Context** — What is this about
2. **Objectives (Explicit)** — Stated goals
3. **Success Criteria** — How to know if done
4. **Decisions & Rules** — Established constraints
5. **SOPs / Workflows** — Step-by-step processes
6. **Scripts / Commands** — Technical structures
7. **Inputs & Outputs** — Materials and products
8. **Missteps / Errors / Risks** — What went wrong
9. **Blockers** — Obstacles
10. **Status** — Current state
11. **Progress Markers** — Milestones
12. **Refinements** — Improvements made
13. **Dependencies** — What this relies on
14. **Entity Maps** — People, tools, systems
15. **Glossary** — Terms defined
16. **Future** — Planned next steps
17. **Pending** — Awaiting action
18. **Open Questions** — Unresolved
19. **Meta-Observations** — Patterns noticed
20. **Reusable Assets** — Templates, code, frameworks

---

## TOOL STACK

| Function | Tool | Cost |
|----------|------|------|
| Orchestration | n8n | £50/month |
| Scraping | Apify | £299/month |
| Transcription | Whisper | Free |
| Documents | Unstructured.io | £0.015/page |
| AI Processing | Claude API | £400/month |
| Database | PostgreSQL | £25/month |

---

## INTEGRATION POINTS

### Receives Content From
- Browser extension exports
- File drop zones
- API submissions
- Scheduled scrapers
- RSS polling
- Email forwarding

### Sends Content To
- All 23 domain pillars
- 04_KNOWLEDGE_LIBRARY (unrouted)
- 03_CORE_ENGINE/INDICES (index updates)

### Triggers
- New content detection
- Index rebuild requests
- Quality audit requests

---

## USAGE INSTRUCTIONS

### For AI/Agents

When processing content:
1. Identify source type
2. Apply correct extraction method
3. Classify topic using keyword mapping
4. Score quality on 5 dimensions
5. Route to destination pillar
6. Update MASTER_CONTENT_INDEX.md
7. Update destination pillar INDEX.md

### For Humans

1. Drop content in appropriate 01_INPUTS subfolder
2. Run extraction workflow (or wait for scheduled)
3. Review items in processing queue
4. Verify routing decisions
5. Monitor index for new additions

---

## CANON FILES

| File | Purpose |
|------|---------|
| INGESTION_MASTER_SYSTEM.md | Complete multi-source system spec |
| EKX_1_METHODOLOGY.md | 20-section AI chat extraction |
| SOURCE_TYPE_SCHEMAS.md | Config per source type |
| QUALITY_SCORING_RULES.md | 5-dimension scoring |
| enterprise_knowledge_system.md | SQLite schema |

---

## RELATED PILLARS

| Pillar | Relationship |
|--------|--------------|
| ALL PILLARS | Content destinations |
| PIL_14_NAVIGATION | Goals trigger ingestion needs |
| PIL_15_ENTERPRISE_OS | Architecture integration |
| PIL_17_RAG_SYSTEM | Chunking for retrieval |
| 03_CORE_ENGINE | Index storage |

---

**END OF CONTEXT DOC**
