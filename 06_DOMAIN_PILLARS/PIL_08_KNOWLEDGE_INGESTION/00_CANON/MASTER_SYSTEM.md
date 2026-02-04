# UNIVERSAL KNOWLEDGE INGESTION SYSTEM

**Version:** 2.0  
**Status:** Production Framework  
**Purpose:** Ingest, extract, route, and index knowledge from ANY source in real-time

---

## SYSTEM OVERVIEW

This system transforms Enterprise_OS from a chat-extraction tool into a **universal knowledge harvesting engine** that can ingest content from any source, extract actionable knowledge, route it to the correct pillar, and keep the system index updated in real-time.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    UNIVERSAL KNOWLEDGE INGESTION ENGINE                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  SOURCES                    PROCESSING                      DESTINATIONS    │
│  ═══════                    ══════════                      ════════════    │
│                                                                              │
│  ┌──────────┐              ┌──────────┐                   ┌──────────────┐  │
│  │ AI Chats │──┐           │          │                   │ PIL_02_BRAND │  │
│  └──────────┘  │           │  DETECT  │                   ├──────────────┤  │
│  ┌──────────┐  │           │    ↓     │                   │ PIL_03_COPY  │  │
│  │ YouTube  │──┤           │  FETCH   │                   ├──────────────┤  │
│  └──────────┘  │           │    ↓     │                   │ PIL_07_UI    │  │
│  ┌──────────┐  │  ┌────┐   │ EXTRACT  │   ┌────────┐      ├──────────────┤  │
│  │   RSS    │──┼─▶│QUEUE│─▶│    ↓     │──▶│ ROUTER │─────▶│ PIL_14_NAV   │  │
│  └──────────┘  │  └────┘   │ CLASSIFY │   └────────┘      ├──────────────┤  │
│  ┌──────────┐  │           │    ↓     │                   │ PIL_19_PROP  │  │
│  │ Scraping │──┤           │  SCORE   │                   ├──────────────┤  │
│  └──────────┘  │           │    ↓     │                   │ PIL_21_MKT   │  │
│  ┌──────────┐  │           │  INDEX   │                   ├──────────────┤  │
│  │ PDFs/Bks │──┘           │          │                   │    ...23     │  │
│  └──────────┘              └──────────┘                   └──────────────┘  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## PART 1: SOURCE TYPES & CONFIGURATIONS

### 1.1 AI Chat Threads (Existing - EKX-1)

```yaml
source_type: ai_chat
platforms: [claude, chatgpt, grok, gemini]
extraction_method: EKX-1 (20-section methodology)

ingestion:
  trigger: Manual upload OR browser extension
  format: Markdown export
  location: 01_INPUTS/threads_raw/
  
extraction:
  sections: 20 (narrative, objectives, decisions, SOPs, etc.)
  preserve: Full provenance with citations
  
routing:
  by: Thread topic analysis
  keywords: Extract and match to pillar domains
  
quality_score:
  completeness: 0-10
  actionability: 0-10
  uniqueness: 0-10
```

### 1.2 YouTube Transcripts (NEW)

```yaml
source_type: youtube
tools: [YouTube API, Whisper, yt-dlp]
cost: Free (API) + compute for Whisper

ingestion:
  methods:
    - Channel subscription monitoring
    - Playlist tracking
    - Keyword search alerts
    - Manual URL submission
  
  workflow:
    1. Detect new video (RSS from channel OR scheduled search)
    2. Fetch metadata (title, description, channel, duration)
    3. Download transcript (YouTube auto OR Whisper)
    4. Store in 01_INPUTS/youtube_transcripts/
    
extraction:
  - Full transcript with timestamps
  - Key topics (AI extraction)
  - Actionable insights
  - Quotes and references
  - Links mentioned
  
routing:
  by: Channel category + content analysis
  map:
    property_channels: → PIL_19_PROPERTY
    marketing_channels: → PIL_02_BRANDING, PIL_03_COPY
    tech_channels: → PIL_15_ENTERPRISE_OS
    fitness_channels: → PIL_20_FITNESS
    
quality_score:
  speaker_authority: 0-10 (known expert?)
  content_density: 0-10 (insights per minute)
  production_quality: 0-10
  
n8n_workflow:
  trigger: Schedule (hourly) OR webhook
  steps:
    - Check subscribed channels for new videos
    - Fetch transcript via API
    - Send to Claude for extraction
    - Route to pillar
    - Update index
```

### 1.3 RSS Feeds (Existing - Expand)

```yaml
source_type: rss_feed
tools: [n8n, Feedly API, RSS-Bridge, FiveFilters]
cost: £50-150/month

ingestion:
  feed_categories:
    property_news: [PropertyWire, EG, CoStar feeds]
    tech_news: [Hacker News, TechCrunch, The Verge]
    marketing: [MarketingWeek, AdAge]
    fitness: [T-Nation, BarBend]
    business: [HBR, Inc, Entrepreneur]
    
  workflow:
    1. Poll feeds (adaptive frequency based on update rate)
    2. Fetch full article (FiveFilters Full-Text RSS)
    3. Deduplicate (fuzzy matching)
    4. Extract key content
    5. Store in 01_INPUTS/rss_feeds/
    
extraction:
  - Article text (cleaned)
  - Publication date
  - Author
  - Key entities (people, companies, places)
  - Topic tags
  - Sentiment
  
routing:
  by: Feed category + entity extraction
  
quality_score:
  source_reputation: 0-10
  freshness: 0-10 (decay over time)
  relevance: 0-10 (keyword match)
```

### 1.4 Web Scraping - Apify (NEW)

```yaml
source_type: web_scrape
tools: [Apify, Scrapy Cloud, Bright Data]
cost: £299-500/month

property_market_scrapers:
  rightmove:
    actor: rightmove-scraper
    data: listings, prices, photos, descriptions
    frequency: daily
    output: JSON → 01_INPUTS/scraped_data/rightmove/
    
  zoopla:
    actor: zoopla-scraper
    data: listings, valuations, sold prices
    frequency: daily
    output: JSON → 01_INPUTS/scraped_data/zoopla/
    
  land_registry:
    actor: custom (UK Land Registry API)
    data: transactions, title info
    frequency: weekly
    output: JSON → 01_INPUTS/scraped_data/land_registry/
    
  planning_portals:
    actor: custom per council
    data: planning applications, decisions
    frequency: daily
    output: JSON → 01_INPUTS/scraped_data/planning/

data_as_service_opportunity:
  - Aggregate multi-source property data
  - Clean and normalize
  - Add AI insights layer
  - Sell via API to estate agents, investors
  - Price: £149-999/month per subscriber
  
extraction:
  - Structured data fields
  - Geocoding
  - Price history trends
  - Market comparisons
  
routing:
  all_property_data: → PIL_19_PROPERTY/05_DATA/
  market_intelligence: → PIL_21_MARKET_RESEARCH/04_DATA_SOURCES/
  
quality_score:
  data_completeness: 0-10
  freshness: 0-10
  accuracy: 0-10 (spot-check validation)
```

### 1.5 Books & PDFs (NEW)

```yaml
source_type: document
tools: [Unstructured.io, AWS Textract, Adobe PDF Services]
cost: £0.015-0.05 per page

ingestion:
  sources:
    - E-books (personal library)
    - Research papers (Semantic Scholar, arXiv)
    - Industry reports
    - Planning documents
    - Legal documents
    
  workflow:
    1. Upload to 01_INPUTS/books_pdfs/
    2. Detect document type
    3. Extract text (OCR if needed)
    4. Extract tables and figures
    5. Chunk for processing
    
extraction:
  using: Unstructured.io partition_pdf()
  output:
    - Full text (chunked)
    - Table data (structured)
    - Figure captions
    - Citations/references
    - Key concepts
    
  ai_processing:
    - Chapter summaries
    - Key insights extraction
    - Actionable takeaways
    - Cross-reference to existing knowledge
    
routing:
  by: Document type + content analysis
  map:
    business_books: → PIL_15_ENTERPRISE_OS, PIL_14_NAVIGATION
    marketing_books: → PIL_03_COPY, PIL_02_BRANDING
    property_reports: → PIL_19_PROPERTY, PIL_21_MARKET_RESEARCH
    fitness_content: → PIL_20_FITNESS
    planning_docs: → PIL_19_PROPERTY/05_DATA/
    
quality_score:
  source_authority: 0-10
  content_density: 0-10
  relevance: 0-10
```

### 1.6 Podcasts (NEW)

```yaml
source_type: podcast
tools: [Whisper, podcast RSS, Spotify API]
cost: Compute only (Whisper is free)

ingestion:
  workflow:
    1. Subscribe to podcast RSS
    2. Detect new episodes
    3. Download audio
    4. Transcribe with Whisper
    5. Store transcript + metadata
    
extraction:
  - Full transcript with timestamps
  - Speaker diarization (who said what)
  - Topic segments
  - Key quotes
  - Guest information
  
routing:
  by: Podcast category + content
```

---

## PART 2: PROCESSING PIPELINE

### 2.1 Detection Layer

```yaml
detection_methods:
  scheduled_polling:
    - RSS feeds: Every 15-60 minutes (adaptive)
    - YouTube channels: Hourly
    - Scrapers: Daily batches
    
  webhook_triggers:
    - New file in Dropbox/Drive folder
    - Email with attachment
    - API submission
    - Browser extension capture
    
  manual_submission:
    - Upload interface
    - Drag-and-drop zone
    - CLI command
```

### 2.2 Fetch Layer

```yaml
fetch_rules:
  retry: 3 attempts with exponential backoff
  timeout: 30 seconds (extend for large files)
  rate_limit: Respect source limits
  caching: Cache for 24 hours to avoid re-fetch
  
fetch_by_type:
  url: HTTP GET with proper headers
  api: Authenticated request with rate limiting
  file: Read from input folder
  stream: Chunked download for large files
```

### 2.3 Extraction Layer

```yaml
extraction_methods:
  ai_chat: EKX-1 (20-section methodology)
  youtube: Transcript + AI summarization
  rss: Full-text + entity extraction
  scrape: Structured field mapping
  document: Unstructured.io + AI processing
  
output_format:
  standard_fields:
    - source_id: unique identifier
    - source_type: ai_chat | youtube | rss | scrape | document
    - source_url: original location
    - ingested_at: timestamp
    - extracted_at: timestamp
    - content_raw: original text
    - content_structured: extracted fields
    - topics: [array of topics]
    - entities: {people, companies, places}
    - quality_score: 0-10
    - routing_destination: pillar path
```

### 2.4 Classification Layer

```yaml
classification_rules:
  topic_detection:
    method: Keyword matching + AI classification
    output: Primary topic, secondary topics
    
  domain_mapping:
    property: [real estate, housing, mortgage, landlord, tenant]
    marketing: [copy, brand, advertising, campaign, audience]
    tech: [code, api, database, architecture, system]
    fitness: [training, exercise, nutrition, health]
    business: [strategy, revenue, operations, team]
    
  pillar_routing:
    primary_topic → pillar_id
    confidence_threshold: 0.7
    fallback: 04_KNOWLEDGE_LIBRARY/ONGOING/UNROUTED/
```

### 2.5 Quality Scoring Layer

```yaml
quality_dimensions:
  completeness:
    description: How much of the expected content is present
    weight: 0.25
    
  actionability:
    description: Can you do something with this information
    weight: 0.30
    
  uniqueness:
    description: Is this new information or duplicate
    weight: 0.20
    
  authority:
    description: Is the source trustworthy
    weight: 0.15
    
  freshness:
    description: How recent is this content
    weight: 0.10
    
overall_score: weighted_average(dimensions)
threshold_for_canon: 7.0
threshold_for_review: 5.0
threshold_for_archive: < 5.0
```

### 2.6 Routing Layer

```yaml
routing_rules:
  high_confidence (>0.8):
    action: Auto-route to pillar
    notify: None
    
  medium_confidence (0.5-0.8):
    action: Route with flag for review
    notify: Daily digest
    
  low_confidence (<0.5):
    action: Route to UNROUTED folder
    notify: Immediate attention needed
    
routing_map:
  # See full pillar routing in ROUTING_RULES.md
  keywords_to_pillar:
    [navigation, goals, 5A, planning]: PIL_14_NAVIGATION
    [copy, headline, persuasion, sales]: PIL_03_COPY
    [property, estate, london, housing]: PIL_19_PROPERTY
    [ui, component, figma, react]: PIL_07_UI_LIBRARY
    [extraction, ingestion, parsing]: PIL_08_KNOWLEDGE_INGESTION
    # ... etc for all 23 pillars
```

### 2.7 Index Update Layer

```yaml
on_successful_ingestion:
  1. Add entry to MASTER_CONTENT_INDEX.md:
     - source_id
     - source_type
     - title/summary
     - ingested_at
     - routed_to
     - quality_score
     
  2. Update pillar INDEX.md:
     - Add to appropriate section
     - Update file counts
     - Update last_indexed timestamp
     
  3. Update SOURCE_REGISTRY.md:
     - Increment source counters
     - Update last_active timestamp
     
  4. Trigger notifications if high-priority:
     - Quality score > 8
     - Topic matches active goals
     - New source type
```

---

## PART 3: REAL-TIME OPERATIONS

### 3.1 n8n Orchestration Workflows

```yaml
workflow_1_rss_ingestion:
  name: RSS Feed Processor
  trigger: Schedule (every 30 min)
  steps:
    - Fetch all active feeds
    - Filter new items (since last run)
    - For each item:
        - Fetch full text
        - Extract entities
        - Classify topic
        - Score quality
        - Route to pillar
        - Update index
    - Log run stats
    
workflow_2_youtube_monitor:
  name: YouTube Channel Monitor
  trigger: Schedule (hourly)
  steps:
    - Check subscribed channels
    - For each new video:
        - Fetch transcript
        - Send to Claude for extraction
        - Classify and score
        - Route to pillar
        - Update index
    - Log run stats
    
workflow_3_scraper_orchestrator:
  name: Property Data Scraper
  trigger: Schedule (daily 2am)
  steps:
    - Trigger Apify actors (Rightmove, Zoopla)
    - Wait for completion
    - Download results
    - Process and normalize data
    - Store in PIL_19_PROPERTY/05_DATA/
    - Update index
    - Generate daily data report
    
workflow_4_document_processor:
  name: Document Intake
  trigger: Webhook (new file in folder)
  steps:
    - Detect file type
    - Extract content (Unstructured.io)
    - Send to Claude for analysis
    - Classify and score
    - Route to pillar
    - Update index
```

### 3.2 Index Structure

```markdown
# MASTER_CONTENT_INDEX.md

## Summary
- Total items: 4,521
- Last updated: 2026-02-03 08:45:00
- Sources active: 47

## By Source Type
| Type | Count | Last Ingested |
|------|-------|---------------|
| ai_chat | 1,245 | 2026-02-03 |
| youtube | 312 | 2026-02-03 |
| rss_feed | 2,156 | 2026-02-03 |
| web_scrape | 645 | 2026-02-03 |
| document | 163 | 2026-02-02 |

## By Pillar Destination
| Pillar | Count | % |
|--------|-------|---|
| PIL_19_PROPERTY | 1,892 | 42% |
| PIL_03_COPY | 534 | 12% |
| PIL_15_ENTERPRISE_OS | 423 | 9% |
| ... | ... | ... |

## Recent Additions (Last 24h)
| ID | Type | Title | Pillar | Score |
|----|------|-------|--------|-------|
| ING_4521 | youtube | "London Property Market 2026" | PIL_19 | 8.5 |
| ING_4520 | rss | "New Planning Rules Announced" | PIL_19 | 7.2 |
| ... | ... | ... | ... | ... |
```

### 3.3 Source Registry

```markdown
# SOURCE_REGISTRY.md

## Active Sources

### YouTube Channels (12)
| Channel | Category | Items | Last Check |
|---------|----------|-------|------------|
| Property Hub | property | 45 | 2026-02-03 |
| Samuel Leeds | property | 38 | 2026-02-03 |
| ... | ... | ... | ... |

### RSS Feeds (28)
| Feed | Category | Items | Frequency |
|------|----------|-------|-----------|
| PropertyWire | property | 234 | 30min |
| HBR | business | 156 | 1hr |
| ... | ... | ... | ... |

### Scrapers (5)
| Scraper | Data Type | Records | Schedule |
|---------|-----------|---------|----------|
| Rightmove | listings | 12,450 | daily |
| Zoopla | listings | 9,823 | daily |
| ... | ... | ... | ... |
```

---

## PART 4: DATA-AS-A-SERVICE OPPORTUNITY

### Property Intelligence API

```yaml
service_name: Property Connect Data API
pricing:
  starter: £149/month (1000 API calls)
  growth: £499/month (10000 API calls)
  enterprise: £999/month (unlimited)
  
endpoints:
  /listings:
    - Search by postcode, price, type
    - Include sold history
    - Market comparisons
    
  /valuations:
    - AI-powered valuations
    - Confidence scores
    - Comparable sales
    
  /planning:
    - Planning applications by area
    - Decision predictions
    - Impact assessments
    
  /market-intelligence:
    - Area trends
    - Price forecasts
    - Demand indicators
    
  /alerts:
    - New listings matching criteria
    - Price changes
    - Planning decisions
    
unique_value:
  - Multi-source aggregation (Rightmove + Zoopla + Land Registry)
  - AI-enriched insights
  - Real-time updates
  - Historical data depth
```

---

## PART 5: IMPLEMENTATION CHECKLIST

### Phase 1: Foundation (Week 1)
- [ ] Set up n8n cloud instance
- [ ] Configure Apify account
- [ ] Set up Supabase/PostgreSQL
- [ ] Create input folder structure
- [ ] Implement EKX-1 extraction prompt

### Phase 2: RSS & YouTube (Week 2)
- [ ] Build RSS ingestion workflow
- [ ] Configure feed subscriptions
- [ ] Build YouTube monitor workflow
- [ ] Test transcript extraction
- [ ] Implement routing logic

### Phase 3: Scraping (Week 3)
- [ ] Configure Apify actors
- [ ] Build scraper orchestration
- [ ] Implement data normalization
- [ ] Set up property database
- [ ] Test full pipeline

### Phase 4: Documents & Index (Week 4)
- [ ] Integrate Unstructured.io
- [ ] Build document processor
- [ ] Implement quality scoring
- [ ] Build index update system
- [ ] Test cross-source routing

### Phase 5: Production (Week 5+)
- [ ] Monitor and tune
- [ ] Build dashboards
- [ ] Document SOPs
- [ ] Train on system usage
- [ ] Launch data API (optional)

---

## PART 6: TOOL STACK SUMMARY

| Function | Tool | Cost |
|----------|------|------|
| Orchestration | n8n Cloud | £50/month |
| Web Scraping | Apify | £299/month |
| Transcription | Whisper (self-hosted) | Free |
| Document Processing | Unstructured.io | £0.015/page |
| AI Processing | Claude API | £400/month |
| Database | PostgreSQL (Supabase) | £25/month |
| Object Storage | Cloudflare R2 | £20/month |
| **Total** | | **~£800/month** |

---

**This system transforms Enterprise_OS into a universal knowledge engine that can ingest, extract, route, and index content from any source in near-real-time.**

**Your competitive advantage: While others manually process information, you have an automated intelligence pipeline feeding your entire platform ecosystem.**
