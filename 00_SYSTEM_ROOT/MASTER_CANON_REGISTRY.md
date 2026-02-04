# ENTERPRISE_OS V7 — MASTER CANON REGISTRY

**Purpose:** Single source of truth for ALL canon documents across ALL pillars  
**Last Updated:** 2026-02-03  
**Status:** Living document — update as pillars are processed

---

## OVERVIEW

This registry tracks every production-ready canon document in Enterprise_OS V7, organized by pillar. Use this when:
- Starting implementation
- Looking for a specific framework
- Understanding cross-pillar dependencies
- Auditing system completeness

---

## PILLARS PROCESSED

| Pillar | Status | Canon Docs | Total Files | Key Framework |
|--------|--------|------------|-------------|---------------|
| PIL_14_NAVIGATION | ✅ Complete | 6 | 23 | 5A+5 Dynamic Layers |
| PIL_08_KNOWLEDGE_INGESTION | ✅ Complete | 8 | 19 | Universal Ingestion Pipeline |
| PIL_10_WORKING_PRACTICES | ✅ Complete | 8 | 22 | Milestone Anchor Loop |
| PIL_12_KEYWORDS | ✅ Complete | 8 | 68 | Universal Keyword Framework |
| PIL_02_BRANDING | ✅ Complete | 5+25+20 | 106 | 5-Phase Brand System |
| PIL_03_COPY | ✅ Complete | 14 | 286 | Copy Block Functions |
| PIL_04_CONTENT | ✅ Complete | 2 | 8 | Content Strategy + Research System |
| PIL_05_GRAPHIC_DESIGN | ✅ Complete | 1 | 5 | Visual Assets Taxonomy (1,200+ types) |
| PIL_06_VIDEO | ✅ Complete | 4 | 10 | AI Video Production Pipeline |
| PIL_07_UI_LIBRARY | ✅ Complete | 10 | 84 | Component Taxonomy |
| PIL_18_AGENT_FRAMEWORK | ✅ Complete | 1+40+40+11 | 87 | 40 Canonical Roles |
| PIL_21_MARKET_RESEARCH | ✅ Complete | 3+31+8 | 69 | London Property Intelligence |
| PIL_19_PROPERTY | ✅ Complete | 15+51+10 | 173 | PCL Implementation + 700K Keywords |
| PIL_20_FITNESS | ✅ Complete | 30+7+5 | 590 | 30 Exercise Pillars + DB Architecture |
| SYS_SEO | ✅ Complete | 4 | 4 | SEO Operations + Syndication System |
| LATEST_THINKING | ✅ Complete | 6 frameworks | 87 | Visual RAG + WebDev Factory + Platform Principles |
| PIL_15_ENTERPRISE_OS | ✅ FINAL | 27 domains | 77 | Orchestration Layer + 27 Extraction Domains + V7 Architecture |

---

## CANON DOCUMENTS BY PILLAR

### PIL_14_NAVIGATION (Goals & Planning)

**Location:** `06_DOMAIN_PILLARS/PIL_14_NAVIGATION/00_CANON/`

| Canon Doc | Purpose | Dependencies |
|-----------|---------|--------------|
| 5A_PLUS_5_FRAMEWORK.md | Dynamic navigation layers | — |
| GOAL_INTAKE_PIPELINE.md | Goal capture → active system | PIL_10 |
| NAVIGATION_STATE_MACHINE.md | State transitions | — |
| PILLAR_ROUTING_MAP.md | Route goals to pillars | All pillars |
| SESSION_PRIORITY_ENGINE.md | Daily/weekly priorities | PIL_10 |
| GOAL_TEMPLATES.md | Reusable goal structures | — |

**Key Frameworks:**
- 5A Layers: Ambitions → Arenas → Aims → Actions → Atoms
- +5 Dynamic: Progress, Priorities, Problems, Pivots, Patterns

---

### PIL_08_KNOWLEDGE_INGESTION (Content Extraction)

**Location:** `06_DOMAIN_PILLARS/PIL_08_KNOWLEDGE_INGESTION/00_CANON/`

| Canon Doc | Purpose | Dependencies |
|-----------|---------|--------------|
| INGESTION_MASTER_SYSTEM.md | Universal multi-source system | n8n, Apify |
| EKX_1_METHODOLOGY.md | 20-section AI chat extraction | — |
| UNIVERSAL_INGESTION_PIPELINE.md | Source→Route→Index flow | All pillars |
| SOURCE_TYPE_CONFIGS.md | YouTube, RSS, Scraping, PDFs | External tools |
| QUALITY_SCORING_SYSTEM.md | 5-dimension scoring | — |
| ROUTING_RULES.md | Topic→Pillar mapping | All pillars |
| INDEX_STRUCTURE.md | Master content index | 04_KNOWLEDGE |
| TOOL_STACK.md | n8n, Apify, Whisper, etc. | — |

**Key Frameworks:**
- EKX-1: 20-section extraction (narrative, decisions, SOPs, scripts, etc.)
- 3-Lane Ingestion: Historical, Fresh, External
- Quality Score: Completeness, Actionability, Uniqueness, Authority, Freshness

---

### PIL_10_WORKING_PRACTICES (Session Design)

**Location:** `06_DOMAIN_PILLARS/PIL_10_WORKING_PRACTICES/00_CANON/`

| Canon Doc | Purpose | Dependencies |
|-----------|---------|--------------|
| MASTER_MILESTONE_MAP.md | 7-milestone dependency graph | — |
| MILESTONE_ANCHOR_LOOP.md | 90-120 min work cycle | — |
| THREE_LANE_INGESTION.md | Historical/Fresh/External | PIL_08 |
| SESSION_HYGIENE.md | File-as-you-go + PARA | — |
| AGENT_HANDOFF_PROTOCOL.md | Automation handoff | PIL_18 |
| TWO_HOUR_WORK_BLOCKS.md | Sustainable pacing | — |
| PARA_IMPLEMENTATION.md | Folder methodology | — |
| MODEL_SELECTION_GUIDE.md | Which AI for what | — |

**Key Frameworks:**
- Milestone Anchor Loop: Inventory→Extract→Synthesize→Derive→File→Log
- 7 Milestones: M1-M7 dependency chain
- Two-Hour Blocks: ≤3 decisions, visible win, next step

---

### PIL_12_KEYWORDS (Keyword Research)

**Location:** `06_DOMAIN_PILLARS/PIL_12_KEYWORDS/00_CANON/`

| Canon Doc | Purpose | Dependencies |
|-----------|---------|--------------|
| UNIVERSAL_KEYWORD_FRAMEWORK.md | Any-niche keyword system | — |
| COMPREHENSIVE_SYSTEM_ANALYSIS.md | Full system documentation | — |
| KEYWORD_RESEARCH_WORKFLOW.md | Research process | — |
| KEYWORD_PERMUTATION_PATTERNS.md | 76 structural + 150 intent | — |
| EXTRACTION_PROMPTS.md | AI extraction templates | — |
| LONDON_GEO_KEYWORDS.md | Geographic structure | PIL_19 |
| KEYWORD_DATABASE_SCHEMA.md | Storage structure | — |
| SEGMENT_KEYWORD_INDEX.md | 32 avatar reports | PIL_01 |

**Key Frameworks:**
- Universal Permutation: 76 structural + 150+ intent patterns
- 7-Pillar Property Structure: Buying, Selling, Renting, Letting, Investing, Renovating, Building
- Modifier System: Location, Type, Intent, Qualifier, Action, Time, Audience

---

### PIL_02_BRANDING (Brand Development System)

**Location:** `06_DOMAIN_PILLARS/PIL_02_BRANDING/`

| Canon Doc | Purpose | Dependencies |
|-----------|---------|--------------|
| brand_system_source_of_truth.markdown | Master reference (41 files) | — |
| brand_identity_system.md | Social/digital brand kit | — |
| comprehensive-brand-taxonomy.sql | Full database schema | — |
| phase1_discovery.markdown | Discovery framework | — |
| phase2_strategy.markdown | Strategy framework | Phase 1 |
| phase3_identity.markdown | Social identity framework | Phase 2 |
| phase4_visual_identity.markdown | Visual identity framework | Phase 3 |
| phase5_management.markdown | Operational management | Phase 4 |
| 20+ JSON schemas | Automation-ready data | — |

**Key Frameworks:**
- 5-Phase Brand Development: Discovery → Strategy → Social → Visual → Management
- Tagline Formula: Keyword + Emotion + Promise
- Color System: Primary/Secondary/Functional with HEX/RGB/CMYK
- Typography Hierarchy: Display → H1-H3 → Body → Caption → UI
- Social Media Specs: Platform-specific sizes and templates

---

### PIL_03_COPY (Copywriting)

**Location:** `06_DOMAIN_PILLARS/PIL_03_COPY/00_CANON/`

| Canon Doc | Purpose | Dependencies |
|-----------|---------|--------------|
| COPYWRITING_FORMULAS.md | Master formulas (Schwartz, Kennedy, etc.) | — |
| COPY_BLOCK_FUNCTIONS.md | Psychological trigger blocks | — |
| BUSINESS_COPY_TAXONOMY.md | Full asset taxonomy | — |
| COMPLETE_FUNNEL_TAXONOMY.md | TOFU→MOFU→BOFU→Post | — |
| DIRECT_RESPONSE_FRAMEWORK.md | DR methodology | — |
| CUSTOMER_AWARENESS_STAGES.md | Stage-based copy | PIL_01 |
| PERSUASION_DEVICES.md | Persuasion techniques | — |
| MECLABS_VALUE_PROP.md | Value proposition | — |
| BRAND_IDENTITY_SYSTEM.md | Brand voice integration | PIL_02 |
| SPECIALIZED_OFFERS_GUIDE.md | Offer structures | — |

**Asset Templates (163 files in 03_ASSET_TEMPLATES/):**
- Website (19), Funnel (25), Email (30), Social (40+)
- Ads (15), Video (12), App (10), Physical (8), Events (10), Community (9)

**Key Frameworks:**
- Copy Block Functions: Attention, Trust, Conversion blocks with psychological triggers
- Universal Copy Formula: Headline→Subhead→Lead→Body→Offer→CTA→Close
- 163 Channel Templates: Every asset type with element-by-element structure

---

### PIL_04_CONTENT (Content Strategy)

**Location:** `06_DOMAIN_PILLARS/PIL_04_CONTENT/00_CANON/`

| Canon Doc | Purpose | Dependencies |
|-----------|---------|--------------|
| london_property_content_strategy.md | Multi-segment strategy | PIL_01 |
| content_research_system.md | Daily/weekly research workflow | — |

**Key Frameworks:**
- Priority Audience Tiers: Primary (content-hungry) → Secondary (high-value) → Tertiary (B2B)
- Weekly Newsletter Structure: Market Monday → Professional Tuesday → Investment Wednesday → Tenant Thursday → First-Time Buyer Friday → Renovation Saturday → Sunday Spotlight
- Daily Research Routine: 30 min/day across market intel, professional pain points, investment, rental, consumer questions
- Content Platform Ecosystem: Newsletter → Podcast → Magazine → Connected TV → Professional Platform

---

### PIL_05_GRAPHIC_DESIGN (Visual Assets)

**Location:** `06_DOMAIN_PILLARS/PIL_05_GRAPHIC_DESIGN/00_CANON/`

| Canon Doc | Purpose | Dependencies |
|-----------|---------|--------------|
| master_visual_assets_taxonomy.md | Complete 1,150-line taxonomy | — |

**Key Frameworks:**
- Hero & Banner Systems: 60+ styles (photography, gradients, 3D, animation)
- Iconography: 15 styles × 20 categories = 400+ icons
- Illustrations: 20 styles with use case mappings
- Photography: Categories + Styles + Treatments
- Mockups: 100+ device/scene/print combinations
- Lottie Animations: 70 motion types
- Product Shots: E-commerce, Tech, Food, Fashion treatments
- Data Visualization: Charts, Infographics, Icon-based
- Effects: 80+ post-processing treatments

---

### PIL_06_VIDEO (AI Video Production)

**Location:** `06_DOMAIN_PILLARS/PIL_06_VIDEO/00_CANON/`

| Canon Doc | Purpose | Dependencies |
|-----------|---------|--------------|
| AI_Video_Production_Automation_Framework.md | Complete pipeline | Remotion, FFmpeg |
| Forms_of_Video_Content.md | Video content taxonomy | — |
| MVP_Architecture_Diagram_Sketch.md | System design | — |
| Video_Summarizer_LLM_Overview.md | Analysis tools | — |

**Key Frameworks:**
- Script-to-Video Pipeline: Script→NLP→Classify→Match→Voice→Assemble→Render
- Template Structure: Parameterized video templates with timing/assets
- Tool Stack: Remotion.js, FFmpeg, ElevenLabs, Lottie

---

### PIL_07_UI_LIBRARY (UI Components)

**Location:** `06_DOMAIN_PILLARS/PIL_07_UI_LIBRARY/00_CANON/`

| Canon Doc | Purpose | Dependencies |
|-----------|---------|--------------|
| UI_CATEGORIZATION_SYSTEM.md | Master taxonomy | — |
| REACT_COMPONENTS_TAXONOMY.md | React component structure | — |
| WEB_INTERFACE_TAXONOMY.md | Web UI patterns | — |
| COMPLETE_FIGMA_LIBRARY.md | Figma organization | — |
| NAMING_CONVENTIONS_MASTER.md | Universal naming | — |
| COMPONENT_EXTRACTION_PROMPT.md | Claude Code extraction | — |
| PLATFORM_DATABASE.md | UI kit sources | — |
| HTML_TO_FIGMA_AUTOMATION.md | Conversion workflow | — |

**Naming Convention Files (12):**
- buttons, forms, cards, alerts, headers, footers, sidebars
- modals, charts, grids, search, social, hero, chat

**Key Frameworks:**
- Component Taxonomy: 15+ categories with subcategories
- Naming Conventions: [Category]_[Type]_[Variant]_[State]
- 300+ Figma kits indexed

---

### PIL_18_AGENT_FRAMEWORK (Roles & Teams)

**Location:** `06_DOMAIN_PILLARS/PIL_18_AGENT_FRAMEWORK/`

| Canon Doc | Purpose | Dependencies |
|-----------|---------|--------------|
| all_roles_canonical_list_40.md | Master role index | — |
| 40 role definitions | Complete role specs | — |
| 40 skill stacks | Concrete tool requirements | — |
| 11 team structures | Functional groupings | — |

**Key Frameworks:**
- 40 Canonical Roles: Executive, Product, Engineering, Knowledge, GTM, Operations, Risk, Partnerships
- Role Schema: Identity, Intent, Stakeholder Map, Produce/Consume, Authority, Interfaces, Tools
- Role Types: Human, AI, Hybrid
- Authority Levels: Override, Approve, Recommend, Execute

---

### PIL_21_MARKET_RESEARCH (London Property Intelligence)

**Location:** `06_DOMAIN_PILLARS/PIL_21_MARKET_RESEARCH/`

| Canon Doc | Purpose | Dependencies |
|-----------|---------|--------------|
| 00_MASTER_INDEX.md | Document navigation | — |
| 01_Competitor_Analysis_Deep_Dive.md | 7 competitor profiles | — |
| 08_Executive_Summary_Quick_Start.md | One-page strategy | — |
| 31 Segment Reports | All buyer/renter/investor/landlord types | — |
| Data/Infrastructure Docs | Tech stack specs | — |

**Key Frameworks:**
- Competitor Analysis: Adema.ai, Nimbus, PropertyData, Hometrack, etc.
- Data Sources: 4-tier catalog (Essential → Premium → Specialist)
- 31 Segment Reports: 10 buyers + 8 renters + 6 investors + 7 landlords
- Monetization: 5-tier SaaS (Free → Starter → Pro → Agency → Enterprise)
- 90-Day Roadmap: Foundation → Growth → Revenue phases

---

### PIL_19_PROPERTY (Property Connect London Implementation)

**Location:** `06_DOMAIN_PILLARS/PIL_19_PROPERTY/`

| Canon Doc | Purpose | Dependencies |
|-----------|---------|--------------|
| KEYWORD_RESEARCH_WORKFLOW.md | 4-phase keyword system | PIL_12 |
| generic_lsi_keyword_matrix_system.md | Universal framework | — |
| london_property_lsi_matrix_final.md | London implementation | — |
| property-connect-london-master-overview.md | Full ecosystem strategy | — |
| property-connect-london-pillar-by-pillar-strategy.md | 7-pillar breakdown | — |
| 51 segment reports | All market segments | PIL_21 |
| Content Multiplier Engine docs | CTV 20x production | — |
| Pillar Keywords (7 docs) | 700K+ keyword database | — |

**Key Frameworks:**
- 700K Keyword Database: 7 pillars × 20 categories × 50-100 permutations per keyword
- 5-Channel Media Ecosystem: Platform, Magazine, CTV, Podcast, Newsletter
- Proprietary Systems: Rotational Reach Maximizer™, Expert Content Catalyst™, Content Multiplier Engine™, Authority Amplifier™
- Spider Web Lead Gen: Content → Traffic → Signups → Engagement → Revenue
- Universal vs London-Specific: Generic frameworks plus London implementation

---

## CROSS-PILLAR DEPENDENCIES

```
PIL_14_NAVIGATION
    ↓ Goals drive...
PIL_10_WORKING_PRACTICES
    ↓ Sessions use...
PIL_08_KNOWLEDGE_INGESTION
    ↓ Content routes to...
ALL DOMAIN PILLARS (PIL_01 through PIL_23)
    ↓ Which use...
PIL_03_COPY (for messaging)
PIL_07_UI (for interfaces)
PIL_12_KEYWORDS (for SEO/content)
    ↓ All governed by...
PIL_15_ENTERPRISE_OS (system architecture)
```

---

## IMPLEMENTATION ORDER

**Phase 1: Foundation**
1. PIL_15_ENTERPRISE_OS — System architecture (DO LAST for full context)
2. PIL_14_NAVIGATION — Goal system
3. PIL_10_WORKING_PRACTICES — Session methodology

**Phase 2: Content Engine**
4. PIL_08_KNOWLEDGE_INGESTION — Content pipeline
5. PIL_12_KEYWORDS — Keyword system
6. PIL_03_COPY — Copywriting system

**Phase 3: Production**
7. PIL_07_UI_LIBRARY — UI components
8. Domain pillars (PIL_19_PROPERTY, PIL_01_AVATARS, etc.)

---

## FILE LOCATIONS SUMMARY

```
ENTERPRISE_OS_V7/
├── 06_DOMAIN_PILLARS/
│   ├── PIL_02_BRANDING/                → 5 canon + 25 phase docs + 20 JSON
│   ├── PIL_03_COPY/00_CANON/           → 14 canon + 163 templates
│   ├── PIL_04_CONTENT/00_CANON/        → 2 canon
│   ├── PIL_05_GRAPHIC_DESIGN/00_CANON/ → 1 canon (1,150 lines)
│   ├── PIL_06_VIDEO/00_CANON/          → 4 canon
│   ├── PIL_07_UI_LIBRARY/00_CANON/     → 10 canon + 12 naming
│   ├── PIL_08_KNOWLEDGE_INGESTION/00_CANON/ → 8 canon
│   ├── PIL_10_WORKING_PRACTICES/00_CANON/   → 8 canon
│   ├── PIL_12_KEYWORDS/00_CANON/       → 8 canon + 32 segments
│   ├── PIL_14_NAVIGATION/00_CANON/     → 6 canon
│   ├── PIL_18_AGENT_FRAMEWORK/         → 1 index + 40 roles + 40 stacks + 11 teams
│   ├── PIL_19_PROPERTY/                → 15 canon + 51 segments + 700K keywords
│   ├── PIL_21_MARKET_RESEARCH/         → 3 canon + 31 segments + 8 content
│   └── PIL_15_ENTERPRISE_OS/00_CANON/  → TBD (capstone)
```

---

## DOCUMENTATION OUTPUTS PER PILLAR

Each processed pillar produces:
1. **CONTEXT.md** — Full context for AI/agents
2. **README.md** — Human introduction
3. **INDEX.md** — File inventory
4. **ROUTING_RULES.md** — Content flow in/out
5. **CANON_STATUS.md** — Production vs WIP status
6. **ROUTE_PIL_XX.ps1** — PowerShell reorganization script

All outputs stored in: `/mnt/user-data/outputs/PIL_XX_*.md`

---

## NEXT PILLARS TO PROCESS

| Pillar | Priority | Files Est. | Notes |
|--------|----------|------------|-------|
| PIL_01_AVATARS | High | ~50 | Feeds copy, keywords, content |
| PIL_02_BRANDING | High | ~30 | Brand voice, identity |
| PIL_04_CONTENT | High | ~40 | Content strategy |
| PIL_19_PROPERTY | High | ~100+ | Primary platform |
| PIL_21_MARKET_RESEARCH | Medium | ~40 | Market intelligence |
| PIL_15_ENTERPRISE_OS | LAST | ~50+ | System capstone |

---

**This registry is your implementation roadmap. Update as pillars are processed.**

---

**END OF MASTER CANON REGISTRY**
