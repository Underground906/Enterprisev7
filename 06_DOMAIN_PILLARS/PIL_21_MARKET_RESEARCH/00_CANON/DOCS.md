# PIL_21_MARKET_RESEARCH — COMPLETE DOCUMENTATION SET

**Files:** 4 threads + 65 artifacts = **69 total**
**Date:** 2026-02-03

---

# SECTION 1: README

**Pillar ID:** PIL_21  
**Domain:** Property Platform Core  
**Status:** Active (London property market intelligence)

## Purpose

The Market Research pillar contains **comprehensive London property market intelligence** including competitor analysis, data sourcing strategies, segment reports for 30+ audience types, implementation roadmaps, and monetization strategies for Property Connect London.

## Key Assets

| Asset Type | Count | Description |
|------------|-------|-------------|
| Strategic Docs | 8 | Master index, competitor analysis, roadmap |
| Segment Reports | 31 | All buyer/renter/investor/landlord types |
| Data/Technical | 4 | Data sources, scraping, AI/ML, infrastructure |
| Content Strategy | 8 | B2B vendors, data opportunities, content angles |
| PDFs/Docs | 10 | Sales reports for niche segments |

## Folder Structure

```
PIL_21_MARKET_RESEARCH/
├── 00_CANON/
│   ├── 00_MASTER_INDEX.md
│   ├── 01_Competitor_Analysis_Deep_Dive.md
│   └── 08_Executive_Summary_Quick_Start.md
├── 01_STRATEGIC/
│   ├── 06_Monetization_Strategy.md
│   ├── 07_90_Day_Implementation_Roadmap.md
│   └── Competitive_Domination_Strategy.md
├── 02_DATA_INFRASTRUCTURE/
│   ├── 02_Data_Sources_Catalog.md
│   ├── 03_Web_Scraping_Ingestion_Tools.md
│   ├── 04_AI_ML_Tools.md
│   └── 05_Infrastructure_Storage.md
├── 03_SEGMENT_REPORTS/
│   ├── buyers/
│   ├── renters/
│   ├── investors/
│   └── landlords/
├── 04_CONTENT_STRATEGY/
├── 01_threads/
├── 02_artifacts/
└── 90_ARCHIVE/
```

---

# SECTION 2: CONTEXT DOC (For AI/Agents)

## System Overview

PIL_21_MARKET_RESEARCH provides **complete market intelligence** for the London property platform. It covers competitor positioning, data sourcing strategies, audience segments, and implementation roadmaps.

## Competitor Analysis (7 Competitors)

### 1. ADEMA.AI (AI-Native)
```
STRENGTHS: ML-driven analytics, planning intelligence, NLP processing
WEAKNESSES: Over-engineered, high costs, narrow professional focus
OPPORTUNITY: London-specific expertise, consumer angle, content
```

### 2. NIMBUS MAPS (Incumbent)
```
STRENGTHS: 1,000+ data sources, owner contact info, Brickflow integration
WEAKNESSES: Enterprise pricing, complexity, slow onboarding
OPPORTUNITY: Simpler UX, lower price point, content marketing
```

### 3. PROPERTYDATA (Data Provider)
```
STRENGTHS: Comprehensive planning data, valuation tools
WEAKNESSES: Desktop-focused, limited mobile, dated UI
OPPORTUNITY: Modern interface, API access, developer tools
```

### 4. HOMETRACK (Analytics)
```
STRENGTHS: Established brand, institutional clients
WEAKNESSES: Expensive, enterprise-only, limited innovation
OPPORTUNITY: Agile development, consumer products
```

### Additional competitors: LonRes, Dataloft, EGi

## Data Sources Catalog (Tiered)

```
TIER 1 — ESSENTIAL (Start here):
├── Land Registry (£20k/year API)
├── EPC Register (Free API)
├── Planning Portal (Scraping)
└── Rightmove/Zoopla (Scraping with care)

TIER 2 — ENHANCED:
├── Companies House (Free API)
├── Flood data (Free)
├── Transport data (TfL API)
└── Crime statistics (Free)

TIER 3 — PREMIUM:
├── Demographics (ONS, Experian)
├── Valuation models (Hometrack, CACI)
└── Commercial data (CoStar)

TIER 4 — SPECIALIST:
├── Listed buildings (Historic England)
├── Conservation areas (Local authorities)
└── SHLAA sites (Planning documents)
```

## 31 Segment Reports

### BUYERS (10 segments)
| Segment | Key Focus |
|---------|-----------|
| First-Time Buyers | Deposit, mortgages, Help to Buy |
| Upsizers/Second-Time | School catchments, space |
| Downsizers/Retirees | Equity release, accessibility |
| High Net Worth | PCL, off-market, discretion |
| International/Overseas | Currency, tax, residency |
| Institutional Buyers | BTR, portfolios, scale |
| Right to Buy | Discounts, eligibility |
| Affordable Scheme | Shared ownership, First Homes |
| Second Home | Stamp duty, letting |
| Auction Buyers | Below market, cash |

### RENTERS (8 segments)
| Segment | Key Focus |
|---------|-----------|
| General Private | Standard ASTs, references |
| Students | University proximity, HMO |
| Corporate | Relocation, furnished |
| Expats | International, guarantors |
| DSS/Housing Benefit | Universal Credit, guarantees |
| Luxury | PCL, high-end, concierge |
| Short-Term | Airbnb alternatives, corporate |
| Flatshares/Co-Living | Young professionals, community |

### INVESTORS (6 segments)
| Segment | Key Focus |
|---------|-----------|
| Buy-to-Let | Yield, Section 24, EPC |
| HMO Investors | Licensing, room rates |
| Overseas Investors | Tax treaties, management |
| Auction Investors | Refurb, flip, BMV |
| Developers/Flippers | Planning gain, GDV |
| Build-to-Rent | Scale, institutional |

### LANDLORDS/LETTING (7 segments)
| Segment | Key Focus |
|---------|-----------|
| General Letting | Tenant find, management |
| Full Management | Hands-off, fees |
| Student Letting | Term-time, HMO |
| Corporate Letting | Company lets, serviced |
| DSS Letting | Guaranteed rent, risk |
| Luxury Letting | PCL, discretion |
| HMO Management | Compliance, licensing |

## Segment Report Structure

Each report follows consistent format:
```
1. EXECUTIVE SUMMARY
2. MARKET OVERVIEW
   - Dynamics, price/yield, financing, supply
3. AUDIENCE / PERSONAS
   - 3-4 detailed buyer/renter types
4. COMMERCIAL STAKEHOLDERS
   - Agents, lenders, solicitors, etc.
5. REGULATORY & LEGAL
   - Taxation, compliance, licensing
6. CONTENT & PLATFORM OPPORTUNITIES
   - Educational content, tools, data
7. KEY CHALLENGES & RISKS
   - Market, regulatory, economic
8. COMMON QUESTIONS
   - Top 4-5 FAQs with answers
9. STRATEGIC NOTES
   - Actionable insights
```

## Tech Stack Recommendations

```
DATA INGESTION:
├── Scraping: Apify, Scrapy
├── ETL: Airbyte, n8n
├── Document: Unstructured.io
└── Change detection: Visualping

AI/ML:
├── LLM: Claude API, GPT-4
├── Embeddings: OpenAI, Cohere
├── Vector DB: Pinecone, Weaviate
└── ML: scikit-learn, XGBoost

INFRASTRUCTURE:
├── Database: PostgreSQL + PostGIS
├── Analytics: ClickHouse
├── Storage: Cloudflare R2
├── Compute: Railway, Fly.io
└── Search: Meilisearch
```

## Monetization Tiers

```
FREE: Basic search, limited data
STARTER (£29/mo): Enhanced search, alerts
PRO (£99/mo): Full data, API access
AGENCY (£299/mo): Team features, white-label
ENTERPRISE (Custom): Dedicated support, SLA
```

## 90-Day Implementation Roadmap

```
DAYS 1-30: Foundation
├── Core infrastructure setup
├── Data pipeline v1
├── MVP landing page
└── First 3 segment reports

DAYS 31-60: Growth
├── User authentication
├── Search functionality
├── 10 more segment reports
└── Newsletter launch

DAYS 61-90: Revenue
├── Payment integration
├── Premium features
├── API v1
└── First paying customers
```

---

# SECTION 3: INDEX

## 00_CANON/ (3 files)

| File | Purpose |
|------|---------|
| 00_MASTER_INDEX.md | Complete document navigation |
| 01_Competitor_Analysis_Deep_Dive.md | 7 competitor profiles |
| 08_Executive_Summary_Quick_Start.md | One-page strategy |

## 01_STRATEGIC/ (5 files)

| File | Purpose |
|------|---------|
| 06_Monetization_Strategy.md | 5-tier pricing, path to £10M ARR |
| 07_90_Day_Implementation_Roadmap.md | Week-by-week plan |
| Competitive_Domination_Strategy.md | Market positioning |
| London_Property_Data_Sourcing_Strategy.md | Data acquisition |
| Complete_Knowledge_Ingestion_Toolkit.md | Processing pipeline |

## 02_DATA_INFRASTRUCTURE/ (4 files)

| File | Purpose |
|------|---------|
| 02_Data_Sources_Catalog.md | Tiered data sources |
| 03_Web_Scraping_Ingestion_Tools.md | Tool recommendations |
| 04_AI_ML_Tools.md | AI/ML stack |
| 05_Infrastructure_Storage.md | Tech architecture |

## 03_SEGMENT_REPORTS/ (31 files)

**Buyers:** affordable_scheme, auction, downsizers, first-time, high_net_worth, institutional, international, right_to_buy, second_home, upsizers

**Renters:** corporate_tenants, dss_housing_benefit, expat, flatshares_co_living, general_private, luxury, short_term, student

**Investors:** auction_property, build_to_rent, buy_to_let, hmo, overseas_property, property_developers_flippers

**Landlords:** corporate_lettings, dss_lettings, full_property_management, general_letting, guaranteed_rent, hmos, luxury_lettings, student_lettings

## 04_CONTENT_STRATEGY/ (8 files)

Part1 through Part8: B2B Vendors, Data Opportunities, Serial Content, Audience Participation, High-Value Angles, Integration, Vendor Engagement, Data Needs

---

# SECTION 4: ROUTING RULES

## Inbound
```
Keywords: market research, competitor analysis, London property,
          segment, buyer, renter, investor, landlord, data sources,
          property platform, monetization, implementation
→ PIL_21_MARKET_RESEARCH
```

## Outbound
| To | Content |
|----|---------|
| PIL_01_AVATARS | Segment profiles → avatar definitions |
| PIL_04_CONTENT | Segment reports → content strategy |
| PIL_12_KEYWORDS | Segment keywords → SEO |
| PIL_19_PROPERTY | Platform implementation |

## Cross-References
- PIL_01_AVATARS → Uses segment profiles
- PIL_04_CONTENT → Uses segment content angles
- PIL_08_KNOWLEDGE_INGESTION → Uses data source specs
- PIL_12_KEYWORDS → Uses segment terminology

---

# SECTION 5: CANON STATUS

| Status | Count | Notes |
|--------|-------|-------|
| ✅ Canon | 3 | Master index, competitor, exec summary |
| ✅ Strategic | 5 | Implementation docs |
| ✅ Data/Tech | 4 | Infrastructure specs |
| ✅ Segments | 31 | All market segments |
| ✅ Content | 8 | Content strategy parts |
| Keep threads | 4 | Source discussions |
| PDFs/Docs | 10 | Sales collateral |

---

# SECTION 6: KEY FRAMEWORKS

## Competitive Positioning

```
VS ADEMA.AI: Simpler, London-specific, content-led
VS NIMBUS: Lower price, better UX, consumer angle
VS PROPERTYDATA: Modern stack, API-first, mobile
VS HOMETRACK: Agile, innovative, accessible pricing
```

## Segment Priority Matrix

```
HIGH VALUE + HIGH CONTENT APPETITE:
├── First-Time Buyers (education hungry)
├── Buy-to-Let Investors (data hungry)
└── Property Professionals (tool hungry)

HIGH VALUE + LOWER VOLUME:
├── High Net Worth (premium pricing)
├── Institutional (enterprise deals)
└── International (specialized service)

VOLUME PLAYS:
├── General Renters (traffic)
├── Students (seasonal)
└── Flatshares (community)
```

## Revenue Model

```
YEAR 1: £500K ARR
├── 1,000 Pro subscribers (£99/mo)
├── 100 Agency subscribers (£299/mo)
├── 10 Enterprise (£5K/mo)

YEAR 3: £3M ARR
├── 10,000 Pro subscribers
├── 500 Agency subscribers
├── 50 Enterprise

YEAR 5: £10M ARR
├── Market leader position
├── Platform ecosystem
├── API revenue stream
```

---

**END OF PIL_21_MARKET_RESEARCH DOCUMENTATION**
