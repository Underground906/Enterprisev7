# 04_KNOWLEDGE_LIBRARY — README

**Purpose:** Route all incoming knowledge. Extract value. File correctly. Never lose anything.

---

## THE FLOW

```
NEW THREAD/ARTIFACT
        ↓
    [INTAKE]
        ↓
04_KNOWLEDGE_LIBRARY/ONGOING/UNROUTED/
        ↓
    [TRIAGE]
        ↓
┌───────────────────────────────────┐
│ Can I identify the domain?        │
│                                   │
│ YES → Route to 06_DOMAIN_PILLARS/ │
│ NO  → Keep in ONGOING/By_Month/   │
└───────────────────────────────────┘
        ↓
    [EXTRACT]
        ↓
Run 27-domain extraction pass
        ↓
    [FILE]
        ↓
Outputs → appropriate folders
```

---

## FOLDER STRUCTURE

```
04_KNOWLEDGE_LIBRARY/
├── ONGOING/
│   ├── By_Month/
│   │   ├── 2026-02/          ← Current month's unprocessed
│   │   └── 2026-01/
│   └── UNROUTED/             ← Can't figure out where it goes
│
├── EXTRACTION_PIPELINE/
│   ├── RAW_INTAKE/           ← New uploads land here
│   ├── PROCESSING/           ← Currently being extracted
│   └── OUTPUTS/              ← Extracted outputs before filing
│
├── RAG_BUNDLES/
│   ├── V7_ARCHIVE/           ← Your old V7 (1,700+ files)
│   └── [Other historical bundles]
│
└── 90_ARCHIVE/
    └── [Processed batches]
```

---

## DAILY INGESTION ROUTINE

### When New Thread/Artifact Arrives

```
1. Save to: EXTRACTION_PIPELINE/RAW_INTAKE/
2. Name: YYYY-MM-DD_[Source]_[Topic].md
3. Add to today's intake log (optional)
```

### Triage (Do Weekly or When Batch Full)

```
1. Open RAW_INTAKE/
2. For each file:
   - Read first 200 lines
   - Identify primary domain
   - Move to domain pillar OR ONGOING/By_Month/
3. Update any indices
```

### Extraction (When You Have Time)

```
1. Pick file from ONGOING/ or RAW_INTAKE/
2. Run 27-domain extraction (mentally or with AI)
3. Create outputs for relevant domains
4. Move outputs to:
   - Framework → PIL_XX/02_FRAMEWORKS/
   - Schema → PIL_XX/03_SCHEMAS/
   - SOP → PIL_XX/SOPs/
   - Canon → PIL_XX/00_CANON/
5. Archive original to 90_ARCHIVE/
```

---

## 27-DOMAIN EXTRACTION CHECKLIST

When extracting from a thread, ask:

```
□ 1. Product definition — Features, capabilities?
□ 2. Benefits — User/business outcomes?
□ 3. Hooks — Marketing angles?
□ 4. Differentiation — What's unique?
□ 5. Processes — Workflows, SOPs?
□ 6. Performance — What worked/failed?
□ 7. Navigation — Goals, decisions?
□ 8. Project management — PRDs, phases?
□ 9. Roles — Who does what?
□ 10. Automation — What can be automated?
□ 11. Enforcement — Quality rules?
□ 12. Knowledge architecture — RAG implications?
□ 13. Templates — Reusable scaffolds?
□ 14. Data models — Schemas, entities?
□ 15. Libraries — UI, copy, media assets?
□ 16. UI/UX — Interface patterns?
□ 17. Engineering — APIs, infrastructure?
□ 18. Operations — Post-launch concerns?
□ 19. Monetisation — Pricing, packaging?
□ 20. Governance — Canon vs draft?
□ 21. Meta-systems — System improvements?
□ 22. Scripts — Executable code?
□ 23. Books/IP — Long-form content?
□ 24. Courses — Educational products?
□ 25. Training — Onboarding material?
□ 26. External intel — New sources?
□ 27. Routing — Where should this go?
```

---

## ROUTING RULES (QUICK REFERENCE)

| Thread About... | Route To |
|-----------------|----------|
| Copywriting, headlines, offers | PIL_03_COPY |
| Brand, identity, positioning | PIL_02_BRANDING |
| UI components, Figma, design systems | PIL_07_UI_LIBRARY |
| Keywords, SEO research | PIL_12_KEYWORDS |
| Agents, roles, orchestration | PIL_18_AGENT_FRAMEWORK |
| Property market, PCL | PIL_19_PROPERTY |
| Fitness, exercises, training | PIL_20_FITNESS |
| Market research, competitors | PIL_21_MARKET_RESEARCH |
| System architecture, Enterprise_OS | PIL_15_ENTERPRISE_OS |
| Video production | PIL_06_VIDEO |
| Goals, planning | PIL_14_NAVIGATION |
| Work sessions, productivity | PIL_10_WORKING_PRACTICES |
| Can't tell | ONGOING/UNROUTED |

---

## RAG BUNDLES

Your old V7 lives here as `RAG_BUNDLES/V7_ARCHIVE/`

**How to Use:**
- When you need historical context → Query RAG bundle
- Looking for "how did I do X before?" → Search V7_ARCHIVE
- Building on past work → Reference, don't copy

**Rules:**
- NEVER edit RAG bundles — They're historical
- ADD new bundles as you complete projects
- Each bundle should have an INDEX.md

---

## FILE NAMING CONVENTION

```
YYYY-MM-DD_[Source]_[Topic]_[Type].md

Examples:
2026-02-04_Claude_AI_Chatbot_Build_thread.md
2026-02-04_ChatGPT_LinkedIn_Strategy_artifact.md
2026-02-04_Manual_Property_Research_notes.md
```

---

## QUICK ACTIONS

### "I just had an AI conversation"
```
1. Export/save thread
2. Save to: EXTRACTION_PIPELINE/RAW_INTAKE/
3. Name properly
4. Done (triage later)
```

### "I have 10 threads to process"
```
1. Move all to RAW_INTAKE/
2. Set aside 30 min
3. Triage each (route or ONGOING)
4. Deep extract the important ones
```

### "I can't find something I worked on"
```
1. Search RAG_BUNDLES/V7_ARCHIVE/
2. Search ONGOING/By_Month/
3. Check 06_DOMAIN_PILLARS/ by likely domain
```

---

## INTEGRATION

| Connects To | How |
|-------------|-----|
| 01_NAVIGATION | Learning feeds goals |
| 02_COMMAND_DECK | Sessions generate content |
| 06_DOMAIN_PILLARS | Routed outputs land there |
| 03_CORE_ENGINE | Indices track everything |

---

*Ingestion is not about filing everything perfectly. It's about never losing anything and knowing where to look.*
