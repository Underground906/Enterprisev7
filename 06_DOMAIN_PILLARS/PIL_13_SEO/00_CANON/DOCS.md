# SYS_SEO — COMPLETE DOCUMENTATION SET

**Files:** 4 (already organized in subfolder structure)
**Date:** 2026-02-03

---

# SECTION 1: README

**System ID:** SYS_SEO  
**Type:** Operations System (applies to all content platforms)  
**Status:** Complete (4 canonical docs across 6 subfolders)

## Purpose

SYS_SEO is the **post-content SEO optimization and distribution system**. It assumes content and keywords are already created, and handles:
1. **On-Page Optimization** — Making content rank-ready
2. **Schema Markup** — Structured data for rich snippets
3. **Answer Engine Optimization** — Getting cited by AI search
4. **Syndication** — 20+ platform distribution automation
5. **Backlink Acquisition** — Outreach, guest posts, directories

## What This Is NOT
- NOT keyword research (that's PIL_12_KEYWORDS)
- NOT content creation (that's PIL_03_COPY / PIL_04_CONTENT)
- NOT the content itself — this is the **distribution engine**

## Key Assets

| Folder | File | Purpose |
|--------|------|---------|
| 00_CONTEXT | SYS_SEO_CONTEXT.md | AI context document |
| 00_CONTEXT | SYS_SEO_COMPLETE_SYSTEM.md | Full operations manual |
| 04_SYNDICATION | SYS_SEO_AUTOPOST_SYNDICATION.md | 20+ platform automation |
| 06_QUICK_REFERENCE | SYS_SEO_QUICK_REFERENCE.md | Print-and-use checklist |

## Folder Structure (Already Done)

```
SYS_SEO/
├── 00_CONTEXT/
│   ├── SYS_SEO_CONTEXT.md
│   └── SYS_SEO_COMPLETE_SYSTEM.md
├── 01_ON_PAGE/                    ← Empty (content in COMPLETE_SYSTEM)
├── 02_SCHEMA/                     ← Empty (templates in COMPLETE_SYSTEM)
├── 03_AEO/                        ← Empty (covered in COMPLETE_SYSTEM)
├── 04_SYNDICATION/
│   └── SYS_SEO_AUTOPOST_SYNDICATION.md
├── 05_BACKLINKS/                  ← Empty (covered in COMPLETE_SYSTEM)
└── 06_QUICK_REFERENCE/
    └── SYS_SEO_QUICK_REFERENCE.md
```

---

# SECTION 2: CONTEXT DOC (For AI/Agents)

## System Overview

```
CONTENT CREATED
      ↓
┌─────────────────────────────────────────────────────────┐
│                    SYS_SEO PIPELINE                      │
├─────────────────────────────────────────────────────────┤
│  1. ON-PAGE OPTIMIZATION                                │
│     └── Density, headers, meta, internal links          │
│                                                         │
│  2. SCHEMA MARKUP                                       │
│     └── Article, FAQ, HowTo, LocalBusiness, Product     │
│                                                         │
│  3. ANSWER ENGINE OPTIMIZATION (AEO)                    │
│     └── Featured snippets, AI search, voice search      │
│                                                         │
│  4. SYNDICATION & AUTO-POSTING                          │
│     └── 20+ platforms, RSS, automation                  │
│                                                         │
│  5. BACKLINK ACQUISITION                                │
│     └── Outreach, guest posts, HARO, directories        │
└─────────────────────────────────────────────────────────┘
      ↓
INDEXED, RANKING, BUILDING AUTHORITY
```

---

## KEY FRAMEWORKS

### 1. ON-PAGE SEO CHECKLIST

**Keyword Placement Rules:**
```
□ Title tag: Primary KW in first 3 words (50-60 chars)
□ H1: Primary KW (exact or close match)
□ URL: Primary KW (short, lowercase, hyphens)
□ Meta description: Primary KW natural use (150-160 chars)
□ First 100 words: Primary KW
□ Last 100 words: Primary KW
□ H2s: Secondary KWs (variations)
□ Image alt text: 1 in 3 images has KW
```

**Keyword Density Target:** 1-2% for primary keyword
```
2000 word article:
- 1% = 20 mentions
- 2% = 40 mentions
- Aim for: 25-35 mentions
```

**Internal Link Density:**
| Content Length | Internal Links | External Links |
|----------------|----------------|----------------|
| <1000 words | 3-5 | 1-2 |
| 1000-2000 words | 5-8 | 2-4 |
| 2000-3000 words | 8-12 | 3-5 |
| 3000+ words | 12-15 | 4-6 |

**Title Formula:**
```
[Primary KW] - [Benefit/Hook] | [Brand] (50-60 chars)

Examples:
- London Property Investment Guide - 2024 Returns | PropertyConnect
- Kettlebell Swing Form - 7 Mistakes Killing Progress | FitOS
```

**Meta Description Formula:**
```
[Action verb] [Primary KW]. [Benefit]. [Secondary KW]. [CTA]. (150-160 chars)
```

---

### 2. SCHEMA MARKUP TEMPLATES

**Article Schema (Most Posts):**
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{{TITLE}}",
  "description": "{{META_DESCRIPTION}}",
  "image": "{{FEATURED_IMAGE_URL}}",
  "author": {"@type": "Person", "name": "{{AUTHOR}}"},
  "datePublished": "{{DATE}}",
  "dateModified": "{{MODIFIED}}"
}
```

**FAQ Schema (Q&A Sections):**
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Q1", "acceptedAnswer": {"@type": "Answer", "text": "A1"}},
    {"@type": "Question", "name": "Q2", "acceptedAnswer": {"@type": "Answer", "text": "A2"}}
  ]
}
```

**HowTo Schema (Step-by-Step):**
```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "{{TITLE}}",
  "totalTime": "PT{{MINUTES}}M",
  "step": [
    {"@type": "HowToStep", "name": "Step 1", "text": "Description"}
  ]
}
```

**When to Use Which:**
| Content Type | Schema |
|--------------|--------|
| Blog posts | Article |
| Tutorials | HowTo |
| FAQ sections | FAQPage |
| Reviews | Review |
| Local pages | LocalBusiness |
| Products | Product |
| Videos | VideoObject |

---

### 3. ANSWER ENGINE OPTIMIZATION (AEO)

**For AI Search (ChatGPT, Perplexity, Claude):**

Goal: Get **cited as a source** when AI answers questions.

**Paragraph Snippet Format:**
```markdown
## What is [Topic]?

[Topic] is [40-60 word direct definition that completely 
answers the question. Start with topic name, use "is/are", 
provide complete answer, end with period.]
```

**List Snippet Format:**
```markdown
## How to [Do Thing] in [X] Steps

1. **Step one name** - Brief description
2. **Step two name** - Brief description
3. **Step three name** - Brief description
```

**What Makes Content Citable by AI:**
1. Direct answers (first sentence answers the question)
2. Structured data (tables, numbered lists)
3. Factual density (statistics, dates, specific numbers)
4. Authority signals (citations, expert quotes)
5. Comprehensive coverage (no gaps)

**Bad vs Good Example:**

❌ Bad (won't be cited):
> Property investment in London can be quite lucrative. There are many factors to consider...

✅ Good (will be cited):
> London property investment yields average 4.2% gross rental returns in 2024, with Zone 2 areas like Hackney and Lewisham outperforming at 5.1%. The minimum investment for a buy-to-let flat is approximately £350,000-£450,000 in these areas.

---

### 4. SYNDICATION NETWORK (20+ Platforms)

**Syndication Architecture:**
```
[ORIGINAL CONTENT]
      ↓
[WordPress/Main Site]
      ↓
┌─────────────────────────────────────────────┐
│         AUTOMATION LAYER                     │
│       (Zapier/Make/n8n/IFTTT)               │
└─────────────────────────────────────────────┘
      ↓
┌───────────────────────┬─────────────────────┐
│ IMMEDIATE (0-24 hrs)  │ DELAYED (7-14 days) │
├───────────────────────┼─────────────────────┤
│ • Twitter thread      │ • Medium (canonical)│
│ • LinkedIn post       │ • LinkedIn Article  │
│ • Facebook page       │ • Substack          │
│ • Pinterest pins      │ • Dev.to / Hashnode │
│ • Email newsletter    │ • Quora answers     │
│ • RSS syndication     │ • Reddit (if fit)   │
└───────────────────────┴─────────────────────┘
```

**Platform Tiers:**

| Tier | Platforms | DA | Link Type |
|------|-----------|-----|-----------|
| 1 - High Authority | Medium, LinkedIn, Substack | 85-98 | NoFollow |
| 2 - DoFollow | Dev.to, Hashnode, Weebly | 70-75 | DoFollow |
| 3 - Social | Twitter, LinkedIn, FB, Pinterest | - | NoFollow |
| 4 - Niche | Industry forums, communities | Varies | Mixed |

**Automation Stack (Free Tier):**
| Function | Tool | Limits |
|----------|------|--------|
| Social scheduling | Buffer Free | 3 channels, 10 posts |
| Automation | Zapier Free | 100 tasks/month |
| Automation | Make.com Free | 1000 ops/month |
| Pinterest | Tailwind Free | 100 pins |
| RSS | Feedly Free | Unlimited |

**Post-Publish Timeline:**
```
Hour 0:   Publish → Submit to GSC/Bing → Social share
Day 1-2:  Email newsletter → Pinterest pins
Day 7+:   Medium (canonical) → LinkedIn Article
Day 14+:  Quora answers → Reddit (if appropriate)
```

---

### 5. BACKLINK ACQUISITION

**Weekly Link Building Rhythm:**
| Day | Task | Target |
|-----|------|--------|
| Mon | HARO responses | 3-5 pitches |
| Tue | Guest post outreach | 2-3 emails |
| Wed | Broken link outreach | 5-10 emails |
| Thu | Directory submissions | 5-10 |
| Fri | Syndication check | All new posts |

**Safe Link Velocity:**
| Site Age | Monthly New Domains |
|----------|---------------------|
| 0-6 months | 5-15 |
| 6-12 months | 15-30 |
| 1-2 years | 30-50 |
| 2+ years | 50-100+ |

**Link Type Mix:**
- 60% editorial/content links
- 20% directory/citation links
- 10% guest posts
- 10% social/profile links

**UK Business Directories (Free):**
| Directory | DA |
|-----------|-----|
| Yell.com | 70 |
| Thomson Local | 60 |
| Yelp UK | 90 |
| Google Business | 100 |
| Bing Places | 95 |
| Apple Maps | 100 |

---

## CONTENT SCORING (Pre-Publish Audit)

| Element | Points | Check |
|---------|--------|-------|
| Title optimized | /10 | Primary KW, under 60 chars |
| Meta description | /10 | Compelling, 155 chars, CTA |
| URL structure | /5 | Short, keyword-rich |
| H1 + hierarchy | /10 | One H1, proper H2→H3 |
| KW in first 100 words | /10 | Natural placement |
| Internal links | /15 | 4-10 relevant links |
| External links | /5 | 2-4 authority sources |
| Images + alt text | /10 | Compressed, descriptive |
| Schema added | /10 | Appropriate type |
| AEO/snippet bait | /10 | Q&A or How-To section |
| Mobile friendly | /5 | Renders correctly |

**Minimum score to publish: 75/100**

---

## RED FLAGS (Don't Publish If...)

```
✗ No primary KW in title
✗ No H1 or multiple H1s
✗ Zero internal links
✗ No images
✗ Keyword density >3%
✗ Missing meta description
✗ URL has dates or weird characters
✗ No schema markup
```

---

# SECTION 3: INTEGRATION WITH ENTERPRISE_OS

```
Enterprise_OS/
├── SYS_SEO/                    ← This system
├── SYS_Content/                ← Content creation
├── SYS_Keywords/               ← Keyword research
├── PIL_12_KEYWORDS/            ← Universal keyword framework
├── PIL_03_COPY/                ← Copywriting system
├── PRJ_Property_Connect/       ← Uses SEO system
├── PRJ_Fitness_Platform/       ← Uses SEO system
└── ...
```

**Workflow:**
1. Keywords researched in PIL_12_KEYWORDS
2. Content created in PIL_03_COPY / PIL_04_CONTENT
3. **SYS_SEO optimizes and distributes**
4. Backlinks acquired, rankings monitored

---

# SECTION 4: ROUTING RULES

## Inbound
```
Keywords: SEO, search engine, optimization, schema markup,
          backlinks, syndication, meta tags, featured snippets,
          AEO, answer engine, link building, on-page
→ SYS_SEO
```

## Outbound
| To | Content |
|----|---------|
| PIL_12_KEYWORDS | Keyword research handoff |
| PIL_03_COPY | Content creation handoff |
| PIL_04_CONTENT | Content strategy |
| All domain projects | Distribution execution |

---

# SECTION 5: CANON STATUS

| File | Purpose | Status |
|------|---------|--------|
| SYS_SEO_CONTEXT.md | AI context document | ✅ Canon |
| SYS_SEO_COMPLETE_SYSTEM.md | Full operations manual | ✅ Canon |
| SYS_SEO_AUTOPOST_SYNDICATION.md | 20+ platform automation | ✅ Canon |
| SYS_SEO_QUICK_REFERENCE.md | Print-and-use checklist | ✅ Canon |

---

# SECTION 6: QUICK START

## 30-Minute Setup (Free)

1. **Buffer** (5 min) — Connect Twitter, LinkedIn, Facebook
2. **Zapier** (10 min) — Create RSS → Buffer automation
3. **Medium** (5 min) — Create account, connect to main site
4. **Dev.to** (5 min) — Connect RSS feed
5. **Pinterest** (5 min) — Create business account + boards

**Result:** Every new post automatically:
- Shares to 3 social platforms
- Appears on Dev.to
- Ready to import to Medium

## Every Post Checklist

```
□ Primary KW in: Title, H1, URL, meta, first 100 words
□ Internal links: 4-10 depending on length
□ Schema: Article + FAQ minimum
□ Featured snippet bait: "What is X?" or "How to X" H2
□ Submit to GSC immediately
□ Social share via Buffer
□ Syndicate to Medium at Day 7
```

---

**END OF SYS_SEO DOCUMENTATION**
