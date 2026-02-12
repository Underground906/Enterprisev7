# ENTERPRISE_OS UI Component Library & Platform Factory

**PRD + Project Plan + Implementation Specs**
**Version 1.0 | 6 February 2026**

---

## 1. Executive Summary

Transform 220+ Figma UI kits (including Untitled UI's 10,000+ component library) into a searchable, LLM-powered component library that enables rapid creation of hundreds of platform pages.

### The Problem
You have the largest personal UI library in existence trapped inside Figma's unstructured naming. Every attempt to index has failed because:
1. Figma naming is non-semantic
2. Rule-based Python parsing collapses on inconsistent structures
3. You tried to index before you could see what you had
4. No visual-first browsing capability existed

### The Solution
Five-system production pipeline:
1. **Figma Extraction Engine** - snapshots and indexes everything visually-first
2. **LLM Classification Pipeline** - uses vision + structure to categorize without relying on names
3. **Relume-Style Search Library** - high-quality thumbnails and filtering
4. **Platform HTML Scraper** - captures real-world UIs from 200+ platforms
5. **PRD-to-Page Assembly Engine** - takes a spec and automatically composes pages

### The Outcome
Give a PRD to Claude Code → it finds the right templates → applies your brand → generates database schema → produces working React pages.

---

## 2. Quick Start: First 4 Hours

### Hour 1: Set Up Infrastructure
- Start PostgreSQL (Docker)
- Create database tables: components_raw, component_library
- Get Figma personal access token
- List all Figma file keys in config.yaml

### Hour 2: Run Extraction
```bash
pip install requests pyyaml Pillow
python figma_deep_extractor.py --config config.yaml
psql -d enterprise_os_ui -f consolidated_import.sql
```

### Hour 3: Visual Gallery
- Next.js app scaffold
- Connect to PostgreSQL
- Build simple grid page with category filter

### Hour 4: First Classification Run
- Take 50 random thumbnails
- Send to Claude API with classification prompt
- Store results in component_library table

---

## 3. Sprint Execution Plan

### SPRINT 1: Extraction & Visual Index (Days 1-3)
Goal: See everything you have in thumbnails.

| Task | Output |
|------|--------|
| Configure Figma API tokens | config.yaml |
| Run figma_deep_extractor.py | Raw JSON + thumbnails |
| Set up PostgreSQL | Database ready |
| Build thumbnail gallery | Visual browsing |
| Manual review pass | Clean inventory |

### SPRINT 2: LLM Classification (Days 4-6)
Goal: Every component classified by function, level, device.

| Task | Output |
|------|--------|
| Build classification prompt | System prompt |
| Process thumbnails through vision LLM | Classification JSON |
| Create component_library table | Indexed library |
| Generate embeddings | Semantic search |

### SPRINT 3: Search Library Web App (Days 7-10)
Goal: Relume-quality browsing experience.

| Task | Output |
|------|--------|
| Next.js app scaffold | Web app |
| Thumbnail grid + lazy loading | Visual browsing |
| Faceted filter sidebar | Drill-down navigation |
| Full-text + semantic search | Find any component |
| Design Assets Library | Searchable assets |

### SPRINT 4: Platform Scraper MVP (Days 11-14)
Goal: Automated capture of top 50 platform UIs.

### SPRINT 5: PRD-to-Page Assembly (Days 15-18)
Goal: Give a PRD, get composed branded pages.

### SPRINT 6: Polish & Scale (Days 19-21)
Goal: Production-ready system.

---

## 4. Component Taxonomy

### 12 Functional Categories
1. Dashboard & Admin
2. Profile & Authentication
3. E-commerce & Shopping
4. Content & Publishing
5. Landing Pages & Marketing
6. Sales & Conversion
7. Website Pages & Navigation
8. Business & Professional
9. Communication & Social
10. Data & Analytics
11. Search & Discovery
12. Forms & Input

### 13 Industry Verticals
Real Estate, E-commerce, Live Streaming, E-learning, Social Network, Fitness & Wellness, Job Portal, Event Management, Hotel/Airbnb, AI Chat/Agents, Podcast, Community/Charity, Movie/Music Streaming

### Component Hierarchy
| Level | Description | Count |
|-------|-------------|-------|
| Page Template | Full page layouts | ~200-400 |
| Block/Section | Major page sections | ~800-1500 |
| Component | Reusable UI elements | ~3000-6000 |
| Atom | Basic building blocks | ~2000-4000 |

---

## 5. Technology Stack

| Layer | Technology | Cost |
|-------|------------|------|
| Frontend | Next.js 14 + Tailwind + shadcn/ui | Free |
| Database | PostgreSQL + pgvector | Free |
| LLM: Classification | DeepSeek API | ~$5-10/run |
| LLM: Assembly | Claude API | ~$0.50-2/page |
| Scraping | Playwright | Free |
| Component Browser | Storybook 8 | Free |

**Total Monthly: ~$100-120**

---

## 6. Database Schema

### Core Tables
- components_raw - Raw Figma extraction data
- component_library - Classified, searchable library
- design_tokens - Extracted color/type/spacing
- brand_systems - Brand definitions for rebranding
- page_archetypes - Template patterns
- platform_captures - Scraped platform HTML/screenshots
- assets_library - Design assets
- video_library - Video assets and motion patterns

---

## 7. What You Already Have

| Asset | Status |
|-------|--------|
| 220+ Figma UI Kits | Uploaded, unindexed |
| Untitled UI (10,000+ components) | Available, not extracted |
| Figma Deep Extractor Script | Built, untested at scale |
| 28 Naming Convention Files | Complete |
| UI Categorization System | Two versions ready |
| 12 Spec Documents (01-12) | All schemas defined |
| Master Platform Database | 1000+ SaaS platforms |
| Top 200 Platform Target List | Prioritized |
| Authenticated Scraping System | Email automation ready |

---

**This PRD is execution-ready. Start with the 4-hour quick start.**
