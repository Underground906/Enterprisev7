# Property Connect London — Complete Build Specification

> **Version:** 1.0
> **Date:** 2026-02-17
> **Purpose:** Every screen, every state, every component — full endpoint fidelity across 102 pages.
> **Sources:** PCL_DEV_READY_SPEC.md, PCL_PAGE_INVENTORY.md, PCL_WEBSITE_PRD.md, PCL_APPS_PRD.md, PCL_SPOKES_PRD.md, PCL_DATA_PRD.md, PCL_PRD_ADDENDUM.md, B2C_CONSUMER_PLATFORM_STRATEGY.md, PLATFORM_DATA_MOAT.md, ACCOUNT_AREA_CONNECTION_FEATURES.md
> **Goal:** Plug-and-play specification for UI Assembly Pipeline + development sprints.

---

## Executive Summary

**What:** Dual-sided AI-native property intelligence platform for London. Hub-and-spoke model — central platform with Magazine, Newsletter, Podcast, Video/CTV, and Social spokes.

**Two Sides:**
- **B2B Professionals** (estate agents, letting agents, investors, brokers, developers, contractors) — pay for SaaS tools, AI apps, marketplace presence
- **B2C Consumers** (buyers, sellers, renters, landlords, investors, improvers) — free/freemium access, lead gen, premium tools

**The Moat:** Consumer behaviour data + professional performance data + content ecosystem = intelligence no competitor can replicate. If it works OFF the platform, it will be copied. If it REQUIRES platform data, it's your moat.

**Revenue at Scale:** £22.6M/year across 15+ streams (Pro subscriptions £1.3M/mo, Magazine £90K/mo, Video £140K/mo, Newsletter £23K/mo, Lead gen, Advertising, Data products).

**Tech:** Next.js 16 + React 19 + Tailwind v4 + PostgreSQL + pgvector + Elasticsearch + Redis + Claude API + Mapbox + Stripe.

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│           propertyconnectlondon.com                  │
│    Marketing Site + Spokes + Public Platform         │
├─────────────────────────────────────────────────────┤
│        app.propertyconnectlondon.com                 │
│   ┌──────────────┐     ┌───────────────────┐        │
│   │ B2B Pro Dash  │     │ B2C Consumer Dash │        │
│   │ (34 pages)    │     │ (28 pages)        │        │
│   └──────────────┘     └───────────────────┘        │
├─────────────────────────────────────────────────────┤
│              INTELLIGENCE LAYER                      │
│  Intent Scoring │ Demand Heatmaps │ Lead Routing     │
│  Prediction Engine │ Lifecycle Tracking               │
├─────────────────────────────────────────────────────┤
│              DATA LAYER                              │
│  PostgreSQL + pgvector │ Elasticsearch │ Redis        │
│  Land Registry │ PropertyData API │ Planning Portals  │
│  YouTube/Mux │ Claude API │ Mapbox │ Stripe           │
└─────────────────────────────────────────────────────┘
```

**5 Spokes:**
1. Magazine (print + digital, £1.08M/yr)
2. Newsletter (Beehiiv, 7 daily editions, £276K/yr)
3. Podcast (weekly interviews, £105K/yr)
4. Video/CTV (Smart TV + YouTube, £1.68M/yr)
5. Social (LinkedIn + multi-channel, £25K/yr)

---

## Conventions

**State notation:** `[SCREEN_ID].[state]`
**Modal notation:** `[SCREEN_ID].modal.[name]`
**Layout codes:** `SB` = sidebar, `SP` = split, `CT` = centered, `FC` = full_canvas, `GR` = grid, `MP` = map
**Permission:** `Public`, `Free`, `Pro` (£299/mo), `Business` (£999/mo), `Enterprise` (£2500/mo)
**Phase:** P1=Marketing MVP, P2=Spokes, P3=Platform Public, P4=Pro Dashboard, P5=Consumer Dashboard

---

# PHASE 1: MARKETING SITE (17 Pages)

---

## SCREEN MKT_01: HOMEPAGE

**Route:** `/`
**Layout:** `FC` — full-page marketing
**Permission:** Public
**Phase:** P1

### States

| State | Description |
|-------|-------------|
| `MKT_01.default` | Full marketing page — 16 sections from hero to footer CTA |
| `MKT_01.loading` | Skeleton for dynamic stats and testimonials |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Hero | `hero` | top | "London's Property Intelligence Platform". Subhead: dual-sided value prop. Primary CTA: "Join as Professional" / "Explore as Consumer". Background: London skyline imagery |
| Problem Section | `section` | below hero | Pain points for professionals (lead leakage, manual work) and consumers (opaque market, no trust) |
| Agitation | `section` | mid | Stats: "40-60% of leads lost after hours", "Average buyer searches 6 months without guidance" |
| Solution Intro | `section` | mid | PCL as the bridge — intelligence for pros, transparency for consumers |
| How It Works | `steps` | mid | 3-step for Pros: List → Get Leads → Grow. 3-step for Consumers: Search → Get Matched → Succeed |
| Channel Showcase | `card_grid` | mid | 6 cards: Platform, Magazine, Newsletter, Podcast, Video, Social — with icons and descriptions |
| Who We Serve | `tabs` | mid | Tab per segment: Estate Agents, Investors, Buyers, Sellers, Renters, Landlords — each with value prop |
| Platform Preview | `mockup` | mid | Screenshot/video of dashboard with key features highlighted |
| Results / Proof | `stats` | mid-lower | Live stats: properties tracked, professionals listed, consumer searches, data points. Testimonial carousel |
| Pricing Preview | `pricing` | lower | 3 Pro tiers (Pro/Business/Enterprise) + Free consumer tier. "See full pricing" link |
| Our Story | `section` | lower | Founder story, London-focused mission |
| FAQ | `accordion` | lower | 8-10 common questions with expandable answers |
| Free Offer CTA | `cta` | lower | "Get Your Free Property Report" with postcode input |
| Newsletter Signup | `form` | lower | Email input + segment selector (buyer/seller/investor/professional) |
| Trust Badges | `badge_group` | above footer | Data sources, security, media mentions |
| Footer CTA | `cta` | bottom | "Ready to transform your property business?" with dual CTAs |

### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `MKT_01.modal.demo_video` | "See it in action" | Platform demo video |
| `MKT_01.modal.free_report` | Free offer CTA | Postcode input → instant area overview |

### Features

| Feature | Description |
|---------|-------------|
| Dual-sided messaging | Speaks to both professionals AND consumers on same page |
| Live platform stats | Real data counters build credibility |
| Segment-specific value props | Tabs show tailored messaging per audience |
| Free report lead magnet | Postcode-based instant value → email capture |

### Benefits

| Benefit | Who | Impact |
|---------|-----|--------|
| Immediate clarity on value | All visitors | Higher conversion — understand offering in 60 seconds |
| Segment self-selection | All visitors | Routes to correct funnel |
| Lead capture via free report | Platform | Email capture from day 1 |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/stats/public` | Live platform statistics |
| POST | `/api/v1/reports/free` | Generate free area report from postcode |
| POST | `/api/v1/newsletter/subscribe` | Newsletter signup |

---

## SCREEN MKT_02-06: SERVICE PAGES (5 Pages — Shared Pattern)

Each service page follows the same layout. Specifics per page below.

**Route:** `/services/[service-slug]`
**Layout:** `FC` — marketing page
**Permission:** Public
**Phase:** P1

### Shared Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Service Hero | `hero` | top | Service-specific headline, subhead, hero image/video, primary CTA |
| What You Get | `card_grid` | mid | 4-6 deliverable cards with icons |
| Pricing Packages | `pricing` | mid | 3-4 tier cards with features |
| Process Steps | `steps` | mid | How it works (3-5 steps) |
| Portfolio / Examples | `gallery` | mid | Previous work / sample outputs |
| Testimonials | `carousel` | lower | Client quotes with photos |
| FAQ | `accordion` | lower | Service-specific questions |
| CTA | `cta` | bottom | "Book a Call" / "Get Started" with calendar link |

### MKT_02: Video Production Service

**Route:** `/services/video-production`
- Packages: Single Tour (£1,295), 5-Pack (£5K), 10-Pack (£8K), Monthly Retainer (£12K), Content Day (£3.5K)
- Deliverables: Cinematic property tours, agent interviews, area guides, how-to content
- Portfolio: Video thumbnails with play buttons

### MKT_03: Magazine Advertising

**Route:** `/services/magazine`
- Formats: 1/4 Page (£1.5K), 1/2 Page (£3K), Full Page (£5K), DPS (£8K), Premium placements (£7K)
- Distribution map: Interactive London borough map showing reach
- Editorial packages: Expert Feature (£6K/mo), Annual Partner (£60K/yr)

### MKT_04: Podcast Guest Service

**Route:** `/services/podcast`
- Packages: Single Appearance (£1.5K), Quarterly (£5K), Annual (£12K)
- Previous guests showcase
- Episode samples with audio player

### MKT_05: Sponsorship Packages

**Route:** `/services/sponsorship`
- Tiers: Bronze (£2.5K/mo), Silver (£5K/mo), Gold (£7.5K/mo), Platinum (£9.75K/mo)
- ROI calculator: interactive tool estimating reach, impressions, leads per tier
- Multi-channel breakdown showing exposure across all spokes

### MKT_06: Content & Platform Marketing

**Route:** `/services/content-marketing`
- Content creation packages
- SEO content strategy
- Platform presence optimization

---

## SCREEN MKT_07: PRICING

**Route:** `/pricing`
**Layout:** `FC`
**Permission:** Public
**Phase:** P1

### States

| State | Description |
|-------|-------------|
| `PRC.default` | Full pricing comparison — Professional tiers + Consumer tiers |
| `PRC.pro_selected` | Professional pricing expanded |
| `PRC.consumer_selected` | Consumer pricing expanded |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Toggle | `toggle` | top | "I'm a Professional" / "I'm a Consumer" |
| Pro Pricing Cards | `pricing` | main | Pro (£299/mo): Basic tools + listings. Business (£999/mo): AI apps + analytics + content tools. Enterprise (£2,500/mo): Full suite + dedicated support + custom integrations |
| Consumer Pricing Cards | `pricing` | main | Free: Basic search + alerts. Premium (£9.99/mo): AI matching + full market intel + priority. |
| Feature Comparison Table | `table` | below cards | Full feature comparison across all tiers |
| Annual Discount Badge | `badge` | on cards | "Save 20% with annual billing" |
| CTA per Tier | `button` | per card | "Start Free Trial" (Pro) / "Get Started" (Consumer) |
| Enterprise Custom | `card` | bottom | "Need custom solution? Talk to us" with contact form |
| FAQ | `accordion` | bottom | Pricing-specific questions (billing, cancellation, upgrades) |

---

## SCREEN MKT_08-12: ADDITIONAL MARKETING PAGES

### MKT_08: Free Video Funnel Landing

**Route:** `/free-video`
**Layout:** `CT`
- Hero: "Get a Free Cinematic Property Tour"
- Application form: Property address, type, agent details
- Social proof: sample video + stats
- Upsell pathway after submission

### MKT_09: About / Our Story

**Route:** `/about`
**Layout:** `FC`
- Mission statement, founder story, team (future), London focus
- Platform vision timeline
- Press/media section
- Contact CTA

### MKT_10: Contact

**Route:** `/contact`
**Layout:** `SP`
- Contact form (name, email, type: Professional/Consumer/Press/Partnership, message)
- Office info, social links
- FAQ section
- Response time promise

### MKT_11: Login

**Route:** `/login`
**Layout:** `CT`
- Email + password form
- Social login (Google, Apple, LinkedIn for pros)
- Forgot password link
- "New here? Sign up" link with role selector (Professional/Consumer)

### MKT_12: Register

**Route:** `/register`
**Layout:** `CT`
- Step 1: Role selection (Professional type dropdown / Consumer)
- Step 2: Account details (email, password, name, company for pros)
- Step 3: Profile basics (location, speciality for pros / property interest for consumers)
- Email verification flow

### MKT_13-17: Legal + Utility Pages

- `/terms` — Terms of service
- `/privacy` — Privacy policy
- `/cookies` — Cookie policy
- `/404` — Not found
- `/sitemap` — HTML sitemap for SEO

---

# PHASE 2: SPOKES (12 Pages)

---

## SCREEN SPK_01: MAGAZINE HUB

**Route:** `/magazine`
**Layout:** `GR` — editorial grid
**Permission:** Public
**Phase:** P2

### States

| State | Description |
|-------|-------------|
| `MAG.default` | Current issue cover + featured articles grid + category navigation |
| `MAG.archive` | Past issues browser |
| `MAG.category` | Filtered by category (area guides, expert features, market data, etc.) |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Current Issue Hero | `hero` | top | Cover image, issue title, "Read Now" CTA, print subscription link |
| Featured Articles | `card_grid` | main | Large card (cover story) + 4-6 smaller cards (featured articles). Image, title, category badge, read time |
| Category Nav | `tabs` | above grid | Area Guides, Expert Features, Property Tours, Market Data, Investment, Renovation, FTB, Events |
| Borough Selector | `dropdown` | top-right | Filter content by London borough |
| Subscribe Banner | `cta` | mid-page | Print subscription: £9.99/mo. Digital: free with platform account |
| Article Card | `card` | grid | Hero image, title, excerpt, author, category badge, read time, QR code badge (links to video) |
| Archive Browser | `grid` | archive state | Past issue covers in chronological grid |
| Advertise CTA | `cta` | sidebar | "Advertise in the magazine" → service page |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/magazine/current` | Current issue |
| GET | `/api/v1/magazine/articles` | Articles (paginated, filterable by category, borough) |
| GET | `/api/v1/magazine/archive` | Past issues |

---

## SCREEN SPK_02: MAGAZINE ARTICLE

**Route:** `/magazine/:slug`
**Layout:** `SB` — content + sidebar
**Permission:** Public (teaser), Free account (full)
**Phase:** P2

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Article Header | `hero` | top | Title, author with avatar, date, category badge, read time, share buttons |
| Article Body | `rich_text` | main | Full editorial content with inline images, pull quotes, data charts |
| QR-to-Video Link | `card` | inline | "Watch the video tour" with embedded video or QR code |
| Author Card | `card` | sidebar | Author bio, other articles, contact link |
| Related Articles | `card_grid` | bottom | 3-4 related articles |
| Borough Data Sidebar | `card` | sidebar | Quick stats for the borough this article covers |
| CTA: Professional | `cta` | sidebar | "Are you a [category] professional? Get listed" |
| Share Bar | `button_group` | floating | Share to LinkedIn, Twitter, Email, WhatsApp, Copy link |

---

## SCREEN SPK_03: NEWSLETTER HUB

**Route:** `/newsletter`
**Layout:** `CT`
**Permission:** Public
**Phase:** P2

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Hero | `hero` | top | "The London Property Brief" — 7 daily editions tailored to your interests |
| Edition Cards | `card_grid` | main | 7 cards (Market Monday, Professional Tuesday, Investment Wednesday, Tenant Thursday, FTB Friday, Renovation Saturday, Sunday Spotlight) — each with sample content preview |
| Signup Form | `form` | mid | Email + select editions (multi-select checkboxes) + optional: role, borough |
| Sample Preview | `card` | mid | "See a sample" — expandable preview of recent edition |
| Stats | `stat_group` | lower | Subscriber count, open rate, satisfaction score |
| Pricing | `pricing` | lower | Free (ad-supported), Premium (£9.99/mo: exclusive data, no ads), Pro (£29.99/mo: API + custom segments) |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/api/v1/newsletter/subscribe` | Subscribe with edition selection |

---

## SCREEN SPK_04: PODCAST HUB

**Route:** `/podcast`
**Layout:** `SB` — content + sidebar player
**Permission:** Public
**Phase:** P2

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Podcast Hero | `hero` | top | Artwork, title, tagline "Authority Amplifier™", platform links (Apple, Spotify, Google, YouTube) |
| Latest Episode | `card` | top-main | Large featured card with play button, title, guest, duration, description |
| Episode List | `list` | main | Chronological list: thumbnail, title, guest, date, duration, play button, download |
| Topic Filter | `tabs` | above list | Expert Interviews, Market Updates, Buyer/Seller Stories, Panel Discussions, Q&A, Area Deep-Dives |
| Audio Player | `player` | sticky bottom | Persistent player: play/pause, progress bar, speed control, skip 15s |
| Guest CTA | `cta` | sidebar | "Be a Guest — Apply" → `/services/podcast` |
| Sponsor Badge | `badge` | per episode | Episode sponsor logo + link |

---

## SCREEN SPK_05: VIDEO / CTV HUB

**Route:** `/watch`
**Layout:** `GR` — video grid
**Permission:** Public
**Phase:** P2

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Hero | `hero` | top | "Watch Property Connect London" — featured video auto-play (muted) |
| Platform Selector | `tabs` | below hero | All, Property Tours, Area Guides, Expert Interviews, How-Tos, Market Updates |
| Video Grid | `card_grid` | main | Thumbnail, title, duration, view count, date. Click → video player page |
| CTV Platforms | `badge_group` | sidebar | "Watch on:" Fire TV, Apple TV, Roku, Samsung, LG, YouTube TV |
| B2B Production CTA | `cta` | sidebar | "Get your property filmed" → `/services/video-production` |
| Subscribe CTA | `cta` | below hero | "Subscribe for new videos weekly" |

---

## SCREEN SPK_06: VIDEO PLAYER

**Route:** `/watch/:slug`
**Layout:** `FC` — video focus
**Permission:** Public
**Phase:** P2

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Video Player | `video` | top (16:9) | Mux or YouTube embed, full controls, quality selector |
| Video Info | `text` | below player | Title, date, view count, description, tags |
| Related Videos | `card_grid` | below | 4-6 related videos |
| Professional Card | `card` | sidebar | Featured professional in this video — name, rating, "View Profile" CTA |
| Property Card | `card` | sidebar (if tour) | Property details — price, beds, location, "View Listing" CTA |
| Share Bar | `button_group` | below player | Share to social, copy link, embed code |

---

## SCREEN SPK_07-12: ADDITIONAL SPOKE PAGES

### SPK_07: Social Hub (`/social-channels`)
- Links to all social channels with follower counts
- Content highlights from each platform
- "Follow us" CTAs per platform

### SPK_08: Magazine Subscribe (`/magazine/subscribe`)
- Print subscription form: address, payment, edition preferences

### SPK_09: Podcast Episode Detail (`/podcast/:slug`)
- Full episode page: player, show notes, guest bio, transcript, related episodes

### SPK_10: Newsletter Archive (`/newsletter/archive`)
- Past editions browsable by date and edition type

### SPK_11: Events Hub (`/events`)
- Upcoming property events, webinars, open houses
- RSVP/booking integration

### SPK_12: Content Hub (`/content`)
- Unified search across all content types (articles, videos, podcasts, reports)
- Filter by type, topic, borough, date

---

# PHASE 3: PLATFORM PUBLIC (11 Pages)

---

## SCREEN PUB_01: PROPERTY SEARCH

**Route:** `/properties`
**Layout:** `MP` — map + list split
**Permission:** Public (basic), Free account (save/alerts), Premium (full data)
**Phase:** P3

### States

| State | Description |
|-------|-------------|
| `SRCH.default` | Map view (right) + property list (left) with filters bar |
| `SRCH.list` | List-only view — grid of property cards |
| `SRCH.map` | Full-screen map with property pins |
| `SRCH.filtered` | Filters applied — results update in real-time |
| `SRCH.empty` | No results — "Broaden your search" suggestion |
| `SRCH.loading` | Skeleton cards + map loading |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Search Bar | `input` | top | Location search (borough, postcode, area) with autocomplete |
| Filter Bar | `filter_group` | below search | Price range (slider), Bedrooms (1-5+), Property type (flat/house/new build/commercial), Buy/Rent toggle |
| Advanced Filters | `expandable` | below filter bar | Garden, parking, chain-free, EPC rating, listing date, agent |
| Map | `map` | right panel | Mapbox GL — property pins colour-coded by type, cluster at zoom-out, click pin → preview card |
| Property Card | `card` | left list | Main image, price, address, beds/baths/sqft, agent logo, "Save" heart, days on market badge |
| View Toggle | `button_group` | top-right | List / Grid / Map view |
| Sort Dropdown | `select` | top-right | Newest, Price low→high, Price high→low, Most viewed |
| Results Count | `text` | top | "342 properties in Clapham" |
| Save Search | `button` | top | "Save this search" → create alert |
| Map Pin Preview | `popup` | on map | Mini property card on pin hover/click |

### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `SRCH.modal.save_search` | "Save Search" button | Name the search, set alert frequency (instant/daily/weekly), email notifications toggle |
| `SRCH.modal.create_alert` | "Create Alert" | Same search criteria → email/push alert when new properties match |

### Features

| Feature | Description |
|---------|-------------|
| Map-based search | Interactive Mapbox with property pins and clusters |
| Real-time filtering | Results update as filters change — no page reload |
| Save search + alerts | Persistent saved searches with configurable notifications |
| Multi-view | Switch between list, grid, and map views |

### Benefits

| Benefit | Who | Impact |
|---------|-----|--------|
| Visual property discovery | Buyers/renters | See properties in geographic context |
| Instant alerts | Active searchers | Never miss a new listing |
| Data-rich cards | All searchers | Make decisions without clicking into every listing |

### Data

| Entity | Table | Key Fields |
|--------|-------|------------|
| Properties | `properties` | id, address, postcode, borough, price, bedrooms, bathrooms, sqft, type, status, agent_id, images, created_at |
| Saved searches | `saved_searches` | user_id, criteria (JSONB), alert_frequency, active |
| Property alerts | `property_alerts` | user_id, search_id, property_id, sent_at |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/properties` | Search properties (paginated, filterable, geo-bounded) |
| GET | `/api/v1/properties/:id` | Property detail |
| POST | `/api/v1/searches/save` | Save search criteria |
| GET | `/api/v1/searches/saved` | List saved searches |
| POST | `/api/v1/alerts/create` | Create property alert |

---

## SCREEN PUB_02: PROPERTY DETAIL

**Route:** `/properties/:id`
**Layout:** `SB` — content + sidebar
**Permission:** Public (basic), Free (full detail), Premium (market context)
**Phase:** P3

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Image Gallery | `gallery` | top | Full-width carousel, thumbnail strip, fullscreen mode, floor plan tab |
| Price & Address | `heading` | below gallery | Price (bold), full address, borough badge, listing date |
| Key Facts Bar | `stat_group` | below heading | Bedrooms, bathrooms, sqft, EPC rating, property type, tenure |
| Description | `rich_text` | main | Full property description |
| Features List | `list` | main | Bullet list of features (garden, parking, period features, etc.) |
| Floor Plan | `image` | main (tab) | Floor plan viewer with room dimensions |
| Location Map | `map` | main | Mapbox showing property location + nearby amenities |
| Nearby Amenities | `card_grid` | below map | Transport (walking time to stations), schools (Ofsted rating), shops, restaurants |
| Market Context (Premium) | `card` | sidebar | Average price in area, price trend chart, demand score, comparable properties |
| Agent Card | `card` | sidebar | Agent photo, name, company, rating, response time, "Contact" CTA |
| Similar Properties | `card_grid` | bottom | 4-6 similar listings |
| Save/Share | `button_group` | top-right | Save heart, share, print |
| Energy Rating | `chart` | main | EPC bar chart (A-G) with annual cost estimates |

### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `PROP.modal.contact_agent` | "Contact Agent" | Message form, phone number reveal, booking for viewing |
| `PROP.modal.book_viewing` | "Book Viewing" | Calendar picker for available viewing slots |
| `PROP.modal.report` | "Report Listing" | Report inaccurate information |

---

## SCREEN PUB_03: AREA EXPLORER

**Route:** `/areas`
**Layout:** `MP` — interactive map + sidebar
**Permission:** Public (basic), Premium (full data layers)
**Phase:** P3

### States

| State | Description |
|-------|-------------|
| `AREA.overview` | London borough map — click borough to explore |
| `AREA.borough` | Borough detail — stats, areas within borough |
| `AREA.neighbourhood` | Neighbourhood detail — granular data |
| `AREA.compare` | Side-by-side comparison of 2-3 areas |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Interactive London Map | `map` | main | Borough boundaries, colour-coded by selected metric (price, demand, growth) |
| Borough Card | `card` | sidebar | Borough name, avg price, trend, demand score, key stats |
| Data Layer Toggle | `toggle_group` | above map | Average Price, Demand Score, Crime Rate, School Rating, Transport Score |
| Area Detail Panel | `panel` | right (on borough click) | Full area stats: demographics, prices, trends, amenities, schools, transport |
| Comparison Tool | `comparison` | full-width (compare state) | Side-by-side columns for 2-3 areas with all metrics |
| Neighbourhood List | `list` | sidebar (borough state) | Areas within borough — click to drill down |
| "People Like You" | `card` | sidebar (Premium) | "Similar buyers chose: [area]" based on search patterns |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/areas` | All boroughs with summary stats |
| GET | `/api/v1/areas/:borough` | Borough detail with data layers |
| GET | `/api/v1/areas/:borough/:neighbourhood` | Neighbourhood detail |
| GET | `/api/v1/areas/compare` | Compare multiple areas |

---

## SCREEN PUB_04: PROFESSIONAL DIRECTORY

**Route:** `/professionals`
**Layout:** `SB` — filter sidebar + card grid
**Permission:** Public
**Phase:** P3

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Search Bar | `input` | top | Search by name, company, service type |
| Category Tabs | `tabs` | below search | Estate Agents, Letting Agents, Mortgage Brokers, Solicitors, Surveyors, Contractors, Investors, Developers |
| Filter Sidebar | `sidebar` | left | Borough, Price range expertise, Rating, Verified badge, Speciality |
| Professional Card | `card` | main grid | Photo, name, company, rating stars, review count, specialities (badges), response time, "View Profile" CTA |
| Verification Badges | `badge` | on cards | ✓ Verified, ⭐ Certified Pro, 🏆 Premium Verified |
| Featured Listings | `carousel` | top of grid | Promoted professionals (paid placement) |
| Sort | `select` | top-right | Rating, Most Reviewed, Response Time, Nearest |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/professionals` | List professionals (paginated, filterable) |
| GET | `/api/v1/professionals/categories` | Service categories with counts |

---

## SCREEN PUB_05: PROFESSIONAL PROFILE

**Route:** `/professionals/:id`
**Layout:** `SB`
**Permission:** Public
**Phase:** P3

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Profile Header | `hero` | top | Photo, name, company, verification badge, rating, review count, response time |
| About | `text` | main | Bio, experience, qualifications |
| Services | `card_grid` | main | Services offered with descriptions |
| Portfolio | `gallery` | main | Properties sold/managed, content published |
| Reviews | `list` | main | Star ratings + written reviews, paginated |
| Stats | `stat_group` | sidebar | Properties listed, avg sale time, success rate, years experience |
| Contact | `card` | sidebar | Phone, email, "Send Message" CTA, "Book Consultation" CTA |
| Active Listings | `card_grid` | main | Currently listed properties |
| Content Published | `list` | main | Articles, videos, podcasts by this professional |

---

## SCREEN PUB_06-11: ADDITIONAL PUBLIC PAGES

### PUB_06: Content Hub (`/content`)
- Unified content search across articles, videos, podcasts, reports
- Filter by type, topic, borough, professional, date
- Trending content section

### PUB_07: Market Intelligence (`/market`)
- Public market dashboard: borough-level pricing, trends, volume
- Interactive charts (powered by PropertyData API + Land Registry)
- Gated reports (email capture for detailed data)

### PUB_08: Knowledge Hub (`/learn`)
- Guides for buyers, sellers, renters, landlords, investors, improvers
- Step-by-step journey guides
- Calculators (mortgage, stamp duty, affordability, rental yield)

### PUB_09: Service Marketplace (`/marketplace`)
- Vetted service providers: moving, cleaning, legal, insurance, utilities
- Quote request system (multi-provider)
- Transaction-verified reviews

### PUB_10: Events (`/events`)
- Property events, webinars, open houses
- RSVP/booking, calendar integration
- Virtual and in-person events

### PUB_11: Sustainability Hub (`/sustainability`)
- EPC data explorer
- Green professional directory
- Government grant finder
- Carbon footprint calculator

---

# PHASE 4: PROFESSIONAL DASHBOARD (34 Pages)

**Base Route:** `/pro`
**Layout:** `SB` — sidebar nav + content area (consistent across all pro pages)
**Permission:** Pro / Business / Enterprise

---

## SCREEN PRO_01: DASHBOARD HOME

**Route:** `/pro`
**Layout:** `SB`
**Permission:** Pro+

### States

| State | Description |
|-------|-------------|
| `PRO_HOME.default` | Dashboard with stats, activity feed, market pulse, alerts |
| `PRO_HOME.loading` | Skeleton cards |
| `PRO_HOME.onboarding` | First-time setup wizard — complete profile, add listings, connect tools |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Quick Stats Row | `stat_cards` | top | Active Listings, New Leads (this week), Response Rate, Revenue Forecast |
| Live Intent Dashboard | `card` | main (Business+) | Real-time buyer/tenant intent in their territory — anonymised demand signals, intent scores |
| Activity Feed | `feed` | main | Recent: new leads, listing views, enquiries, content engagement |
| Market Pulse | `card` | sidebar | Area trends: avg price change, demand vs supply, competition level |
| Alert Centre | `notification_list` | sidebar | Hot lead alerts, opportunity alerts, review alerts |
| Quick Actions | `button_group` | top-right | "Add Listing", "Create Content", "View Leads" |
| Revenue Forecast | `chart` | main (Enterprise) | Monthly revenue projection based on pipeline |

### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `PRO_HOME.modal.quick_add` | "Add Listing" | Quick listing creation form |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/pro/dashboard` | Aggregated dashboard data |
| GET | `/api/v1/pro/dashboard/intent` | Live intent signals (Business+) |
| GET | `/api/v1/pro/dashboard/activity` | Activity feed |
| GET | `/api/v1/pro/dashboard/alerts` | Alert notifications |

---

## SCREEN PRO_02: LEAD MANAGEMENT

**Route:** `/pro/leads`
**Layout:** `SB`
**Permission:** Pro+

### States

| State | Description |
|-------|-------------|
| `LEADS.pipeline` | Kanban view — columns: New, Contacted, Viewing, Offer, Exchanged, Completed |
| `LEADS.list` | Table view with sortable columns |
| `LEADS.detail` | Individual lead detail panel (split view) |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| View Toggle | `button_group` | top | Kanban / List / Map |
| Kanban Board | `kanban` | main | Drag-and-drop cards between pipeline stages |
| Lead Card | `card` | in kanban/list | Name, intent score (0-100), source, properties interested in, last activity, days in stage |
| Lead Detail Panel | `panel` | right (split) | Full behavioural profile: platform searches, properties viewed, calculator usage, content consumed, enquiries sent |
| Intent Score | `badge` | on lead cards | Colour-coded: Hot (90+, red), Warm (60-89, amber), Medium (30-59, blue), Cold (0-29, grey) |
| Buyer Readiness Breakdown | `chart` | detail panel (Business+) | Signals: calculator usage, search narrowing, return visits, timeline urgency |
| Recommended Approach | `card` | detail panel | AI-generated: best time to contact, tone, talking points |
| Smart Routing | `automation` | background | Auto-assign leads to agents based on speciality, performance, availability |
| Filter/Search | `filter_group` | top | Source, Score range, Stage, Date, Area, Assigned agent |

### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `LEADS.modal.add_note` | "Add Note" on lead | Note text, activity type (call/email/meeting/viewing), next action date |
| `LEADS.modal.assign` | "Assign" on lead | Agent selector, reason for assignment |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/pro/leads` | All leads (filterable, paginated) |
| GET | `/api/v1/pro/leads/:id` | Lead detail with behavioural profile |
| PATCH | `/api/v1/pro/leads/:id/stage` | Move lead to new pipeline stage |
| POST | `/api/v1/pro/leads/:id/notes` | Add note to lead |
| POST | `/api/v1/pro/leads/:id/assign` | Assign lead to agent |
| GET | `/api/v1/pro/leads/:id/readiness` | Buyer readiness score breakdown |

---

## SCREEN PRO_03: LISTINGS MANAGEMENT

**Route:** `/pro/listings`
**Layout:** `SB`
**Permission:** Pro+

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Listing Table | `table` | main | Property address, status (active/under offer/sold/let), views, saves, enquiries, days on market |
| Performance Metrics | `stat_cards` | top | Total active, avg views/listing, avg enquiries, conversion rate |
| Add Listing | `button` | top-right | "Add New Listing" → creation wizard |
| Listing Detail | `panel` | right (on click) | Full listing analytics: WHO's looking (buyer types), repeat viewers, comparisons, calculator usage, hot leads on this listing |
| Issue Detection | `alert` | in detail panel | "High views but low enquiries — consider reviewing pricing or photography" |
| Portal Syndication | `badge_group` | per listing | Rightmove, Zoopla, OnTheMarket — status per portal |
| Bulk Actions | `toolbar` | top | Select all, update status, archive, export |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/pro/listings` | All listings with performance data |
| POST | `/api/v1/pro/listings` | Create listing |
| PATCH | `/api/v1/pro/listings/:id` | Update listing |
| GET | `/api/v1/pro/listings/:id/analytics` | Listing performance analytics |
| GET | `/api/v1/pro/listings/:id/viewers` | Who's viewing this listing |

---

## SCREEN PRO_04: CONTENT MANAGEMENT

**Route:** `/pro/content`
**Layout:** `SB`
**Permission:** Pro+

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Content List | `table` | main | Title, type (article/video/listing), status (draft/published/scheduled), views, engagement, leads generated |
| Create Button | `button` | top-right | "Create Content" → type selector → editor |
| Content Editor | `editor` | full (on create/edit) | Rich text editor with image upload, video embed, SEO fields, preview |
| AI Content Assistant (Business+) | `card` | sidebar | Brainstorm ideas, create outlines, suggest optimizations, generate meta descriptions |
| Publishing Calendar | `calendar` | tab | Scheduled content on calendar view, drag to reschedule |
| Content→Lead Pipeline | `funnel` | analytics tab (Business+) | Readers → Searchers → Viewers → Enquirers → Clients with revenue attribution |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/pro/content` | All content items |
| POST | `/api/v1/pro/content` | Create content |
| PATCH | `/api/v1/pro/content/:id` | Update/publish content |
| GET | `/api/v1/pro/content/:id/analytics` | Content performance + lead pipeline |
| POST | `/api/v1/pro/content/ai/suggest` | AI content suggestions |

---

## SCREEN PRO_05-14: REMAINING PRO DASHBOARD PAGES

### PRO_05: Client Management / CRM (`/pro/clients`)
- Client database with lifecycle tracking, communication logs, referral tracking
- Past client activity alerts ("John bought in 2022, now searching 3-bed houses")
- Automatic remortgage reminders (2/5 year cycles)

### PRO_06: Analytics & Reporting (`/pro/analytics`)
- Performance dashboards: listing views, lead conversion, revenue
- Competitive benchmarking against other pros on platform (anonymised)
- Custom report builder (Enterprise)
- Export to PDF/CSV

### PRO_07: Market Intelligence (`/pro/market`)
- Demand heatmaps — visual map of demand vs supply in territory
- Live search volume by area, property type, price range
- Competitor intelligence — how you compare on response time, conversion, reviews
- Timing intelligence — when to contact leads (optimal windows)
- Prediction engine (Business+) — lead conversion probability, market trends

### PRO_08: AI Tools Hub (`/pro/ai-tools`)
- Access to all subscribed AI apps
- App launcher grid
- Usage stats per app
- "Explore more tools" → upgrade CTA

### PRO_09: Team Management (`/pro/team`)
- Team member list with roles and permissions
- Workload distribution view
- Lead assignment rules
- Performance comparison across team
- Multi-branch command center (Enterprise)

### PRO_10: Business Profile (`/pro/profile`)
- Public profile editor (bio, services, portfolio, certifications)
- Verification management (upload credentials, request verification)
- Review management (respond to reviews, request reviews)

### PRO_11: Marketing Tools (`/pro/marketing`)
- Campaign management
- Email templates and sending
- Promotion packages
- Referral program dashboard

### PRO_12: Learning Centre (`/pro/learning`)
- Courses, webinars, best practices
- Industry research library
- Platform tutorials

### PRO_13: Community (`/pro/community`)
- Professional networking
- Discussion forums by category
- Events

### PRO_14: Settings (`/pro/settings`)
- Account settings, billing, integrations (CRM, portal feeds)
- Notification preferences
- API keys (Enterprise)
- White-label configuration (Enterprise)

---

## PRO DASHBOARD: PLATFORM-ONLY INTELLIGENCE FEATURES

These features form the **competitive moat** — they require platform data and cannot be copied.

### Feature Set (Business/Enterprise tier)

| Feature | Data Source | Value |
|---------|-----------|-------|
| Live Intent Dashboard | Consumer search behaviour | See demand in real-time |
| Buyer Readiness Scoring (0-100) | Calculator usage, search narrowing, return visits | Prioritize hot leads |
| Demand Heatmaps | Aggregate search data | Identify opportunity areas |
| Timing Intelligence | Activity patterns | Know when to call |
| Smart Lead Routing | Performance data + specialization | Right lead → right agent |
| Competitor Benchmarking | Platform-wide anonymized data | Know your market position |
| Prediction Engine | Historical patterns | Forecast conversions + trends |
| Client Lifecycle Tracker | Past client activity | Win repeat business |
| Content → Lead Pipeline | Content engagement + lead journey | Prove content ROI |
| Listing Performance Intel | Viewer behaviour on listings | Optimize listings |
| Opportunity Alerts | Pattern detection | Never miss a signal |
| Network Effects Dashboard | Connection value metrics | Prove platform ROI |

---

# PHASE 5: CONSUMER DASHBOARD (28 Pages)

**Base Route:** `/my`
**Layout:** `SB` — sidebar nav + content area
**Permission:** Free / Premium (£9.99/mo)

---

## SCREEN CON_01: CONSUMER DASHBOARD HOME

**Route:** `/my`
**Layout:** `SB`
**Permission:** Free

### States

| State | Description |
|-------|-------------|
| `MY_HOME.default` | Journey tracker, matched professionals, property alerts, recent activity |
| `MY_HOME.onboarding` | First-time: "What are you looking for?" — buyer/seller/renter/landlord/investor/improver |
| `MY_HOME.buyer` | Buyer-focused dashboard with journey progress |
| `MY_HOME.seller` | Seller-focused with valuation + agent matching |
| `MY_HOME.renter` | Renter-focused with search + tenant tools |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Journey Stage Card | `card` | top | Current stage (Browsing/Researching/Active/Ready) with progress bar, comparison to typical timeline |
| Matched Professionals | `card_grid` | main | AI-matched pros with match score (96%), reasoning, success stats. Premium: full matching. Free: top 3 |
| Property Alerts | `list` | main | New matches from saved searches, price drops on watched properties |
| Quick Actions | `button_group` | top-right | "Search Properties", "Find an Expert", "Use Tools", "Ask AI" |
| Recommended Next Steps | `card` | sidebar | AI-generated: "Based on your activity, we recommend: [get a mortgage AIP]" |
| "People Like You" (Premium) | `card` | sidebar | "Similar users in your position searched [area] and found homes in [X] weeks" |
| Saved Properties | `card_grid` | main | Mini cards of saved/shortlisted properties |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/my/dashboard` | Consumer dashboard data |
| GET | `/api/v1/my/matches` | Matched professionals |
| GET | `/api/v1/my/journey` | Journey stage + progress |
| GET | `/api/v1/my/alerts` | Property alerts |

---

## SCREEN CON_02: PROPERTY SEARCH & SAVED

**Route:** `/my/properties`
**Layout:** `SB`
**Permission:** Free

- Enhanced version of public search with saved context
- Saved properties list with notes and comparison tool
- Side-by-side property comparison (up to 3)
- AI recommendations based on search history (Premium)

---

## SCREEN CON_03: AREA RESEARCH

**Route:** `/my/areas`
**Layout:** `MP`
**Permission:** Free (basic), Premium (full data layers)

- Personal area shortlist
- Enhanced neighbourhood data (crime, schools, transport, demographics)
- Community reviews from verified residents
- "Ask a Local" feature (Premium)

---

## SCREEN CON_04: FINANCIAL TOOLS

**Route:** `/my/tools`
**Layout:** `SB`
**Permission:** Free (basic calculators), Premium (full suite)

### Tools

| Tool | Description |
|------|-------------|
| Mortgage Calculator | Monthly payments, affordability, comparison |
| Stamp Duty Calculator | SDLT calculation with FTB relief |
| Affordability Checker | Income, debts, deposit → max purchase price |
| Rental Yield Calculator | For investor users |
| Budget Planner | Full monthly budget analysis |
| Buy vs Rent Comparison | Long-term cost analysis |
| Remortgage Calculator | Should I remortgage? |

---

## SCREEN CON_05-14: REMAINING CONSUMER PAGES

### CON_05: Purchase/Sale Tracker (`/my/tracker`)
- Timeline milestones (offer → survey → exchange → completion)
- Document checklist
- Chain status view
- Communication log

### CON_06: Landlord Dashboard (`/my/landlord`)
- Portfolio overview (properties, rental income, expenses)
- Rent tracking + arrears alerts
- Compliance calendar (gas safety, EPC, deposits)
- Maintenance request management

### CON_07: Investment Tools (`/my/invest`)
- ROI calculator, portfolio tracker
- Market insights, deal alerts
- Auction listings

### CON_08: Home Improvement Tools (`/my/improve`)
- Planning checker (permitted development)
- Renovation cost calculator
- Contractor finder
- Project tracker

### CON_09: Expert Finder (`/my/experts`)
- Enhanced directory with personal matching
- Consultation booking
- Comparison tool for professionals

### CON_10: Learning Hub (`/my/learn`)
- Step-by-step guides per journey type
- Video tutorials, articles
- Templates and checklists

### CON_11: AI Property Advisor (`/my/advisor`)
- Chat interface with AI property advisor
- Personalized recommendations
- 24/7 Q&A about property process

### CON_12: Journey Roadmaps (`/my/roadmap`)
- Customized step-by-step guide based on journey type
- Progress tracking vs typical timeline
- Celebration milestones

### CON_13: Community (`/my/community`)
- Per-borough forums
- Verified resident reviews
- Local expert identification

### CON_14: Settings (`/my/settings`)
- Profile, preferences, notification controls
- Subscription management
- Data export, privacy controls

---

# DATABASE ARCHITECTURE

## Core Tables (PostgreSQL)

```sql
-- ============================================================
-- USERS & AUTH
-- ============================================================

CREATE TABLE users (
  id BIGSERIAL PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT,
  name TEXT,
  avatar_url TEXT,
  role TEXT CHECK (role IN ('consumer', 'professional', 'admin')),
  subscription_tier TEXT DEFAULT 'free',
  stripe_customer_id TEXT,
  email_verified BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE user_preferences (
  user_id BIGINT PRIMARY KEY REFERENCES users(id),
  journey_type TEXT[],  -- buyer, seller, renter, landlord, investor, improver
  target_boroughs TEXT[],
  budget_min NUMERIC,
  budget_max NUMERIC,
  bedrooms_min INT,
  property_types TEXT[],
  notification_prefs JSONB DEFAULT '{}'
);

-- ============================================================
-- PROFESSIONALS
-- ============================================================

CREATE TABLE professionals (
  user_id BIGINT PRIMARY KEY REFERENCES users(id),
  company_name TEXT,
  category TEXT NOT NULL,  -- estate_agent, letting_agent, mortgage_broker, etc.
  specialities TEXT[],
  boroughs_served TEXT[],
  bio TEXT,
  certifications TEXT[],
  verification_level TEXT DEFAULT 'basic' CHECK (verification_level IN ('basic', 'professional', 'premium')),
  response_time_avg INT,  -- minutes
  rating_avg NUMERIC DEFAULT 0,
  review_count INT DEFAULT 0,
  featured BOOLEAN DEFAULT FALSE,
  hourly_rate NUMERIC,
  subscription_tier TEXT DEFAULT 'pro'
);

CREATE TABLE professional_services (
  id SERIAL PRIMARY KEY,
  professional_id BIGINT REFERENCES professionals(user_id),
  service_name TEXT,
  description TEXT,
  price_from NUMERIC,
  price_to NUMERIC
);

-- ============================================================
-- PROPERTIES
-- ============================================================

CREATE TABLE properties (
  id BIGSERIAL PRIMARY KEY,
  agent_id BIGINT REFERENCES professionals(user_id),
  address TEXT NOT NULL,
  postcode TEXT NOT NULL,
  borough TEXT NOT NULL,
  latitude NUMERIC,
  longitude NUMERIC,
  price NUMERIC,
  price_type TEXT CHECK (price_type IN ('sale', 'rent_pcm', 'rent_pw')),
  bedrooms INT,
  bathrooms INT,
  sqft INT,
  property_type TEXT,  -- flat, house, new_build, commercial
  tenure TEXT,  -- freehold, leasehold, share_of_freehold
  epc_rating TEXT,
  status TEXT DEFAULT 'active' CHECK (status IN ('active', 'under_offer', 'sold', 'let', 'withdrawn')),
  description TEXT,
  features TEXT[],
  images TEXT[],
  floor_plan_url TEXT,
  portal_ids JSONB,  -- {rightmove: "xxx", zoopla: "yyy"}
  views_count INT DEFAULT 0,
  saves_count INT DEFAULT 0,
  enquiries_count INT DEFAULT 0,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

-- ============================================================
-- LEADS & INTENT
-- ============================================================

CREATE TABLE leads (
  id BIGSERIAL PRIMARY KEY,
  professional_id BIGINT REFERENCES professionals(user_id),
  consumer_id BIGINT REFERENCES users(id),
  source TEXT,  -- platform, website_widget, referral, spoke
  intent_score INT DEFAULT 0 CHECK (intent_score BETWEEN 0 AND 100),
  stage TEXT DEFAULT 'new' CHECK (stage IN ('new', 'contacted', 'viewing', 'offer', 'exchanged', 'completed', 'lost')),
  assigned_agent_id BIGINT REFERENCES users(id),
  property_id BIGINT REFERENCES properties(id),
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE lead_activities (
  id BIGSERIAL PRIMARY KEY,
  lead_id BIGINT REFERENCES leads(id),
  activity_type TEXT,  -- note, call, email, viewing, meeting, system
  content TEXT,
  created_by BIGINT REFERENCES users(id),
  created_at TIMESTAMPTZ DEFAULT now()
);

-- ============================================================
-- CONTENT
-- ============================================================

CREATE TABLE content (
  id BIGSERIAL PRIMARY KEY,
  author_id BIGINT REFERENCES users(id),
  type TEXT CHECK (type IN ('article', 'video', 'podcast', 'report', 'guide')),
  title TEXT NOT NULL,
  slug TEXT UNIQUE,
  body TEXT,
  excerpt TEXT,
  cover_image TEXT,
  video_url TEXT,
  audio_url TEXT,
  category TEXT,
  borough TEXT,
  tags TEXT[],
  status TEXT DEFAULT 'draft' CHECK (status IN ('draft', 'published', 'scheduled', 'archived')),
  published_at TIMESTAMPTZ,
  views_count INT DEFAULT 0,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE content_engagement (
  id BIGSERIAL PRIMARY KEY,
  content_id BIGINT REFERENCES content(id),
  user_id BIGINT REFERENCES users(id),
  engagement_type TEXT,  -- view, read_complete, save, share, lead_generated
  created_at TIMESTAMPTZ DEFAULT now()
);

-- ============================================================
-- BEHAVIOURAL INTELLIGENCE (THE MOAT)
-- ============================================================

CREATE TABLE user_events (
  id BIGSERIAL PRIMARY KEY,
  user_id BIGINT REFERENCES users(id),
  event_type TEXT NOT NULL,  -- search, view_property, save_property, use_calculator, read_content, enquire, book_viewing
  event_data JSONB,
  session_id TEXT,
  device_type TEXT,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE search_history (
  id BIGSERIAL PRIMARY KEY,
  user_id BIGINT REFERENCES users(id),
  areas TEXT[],
  min_price NUMERIC,
  max_price NUMERIC,
  property_type TEXT,
  bedrooms INT,
  features TEXT[],
  results_count INT,
  clicked_results BIGINT[],
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE user_journey (
  user_id BIGINT PRIMARY KEY REFERENCES users(id),
  journey_type TEXT,  -- buyer, seller, renter, landlord, investor, improver
  current_stage TEXT,
  stage_entered_at TIMESTAMPTZ,
  predicted_action TEXT,
  predicted_timeline_days INT,
  confidence_score NUMERIC
);

CREATE TABLE professional_metrics (
  id BIGSERIAL PRIMARY KEY,
  professional_id BIGINT REFERENCES professionals(user_id),
  period TEXT,  -- YYYY-MM
  avg_response_time INT,
  enquiry_to_viewing_rate NUMERIC,
  viewing_to_offer_rate NUMERIC,
  review_score NUMERIC,
  content_engagement INT,
  leads_received INT,
  leads_converted INT
);

-- ============================================================
-- SAVED ITEMS & ALERTS
-- ============================================================

CREATE TABLE saved_searches (
  id BIGSERIAL PRIMARY KEY,
  user_id BIGINT REFERENCES users(id),
  name TEXT,
  criteria JSONB NOT NULL,
  alert_frequency TEXT DEFAULT 'daily' CHECK (alert_frequency IN ('instant', 'daily', 'weekly')),
  active BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE saved_properties (
  user_id BIGINT REFERENCES users(id),
  property_id BIGINT REFERENCES properties(id),
  notes TEXT,
  created_at TIMESTAMPTZ DEFAULT now(),
  PRIMARY KEY (user_id, property_id)
);

CREATE TABLE property_alerts (
  id BIGSERIAL PRIMARY KEY,
  user_id BIGINT REFERENCES users(id),
  search_id BIGINT REFERENCES saved_searches(id),
  property_id BIGINT REFERENCES properties(id),
  alert_type TEXT,  -- new_listing, price_drop, status_change
  sent_at TIMESTAMPTZ,
  read_at TIMESTAMPTZ
);

-- ============================================================
-- REVIEWS
-- ============================================================

CREATE TABLE reviews (
  id BIGSERIAL PRIMARY KEY,
  professional_id BIGINT REFERENCES professionals(user_id),
  reviewer_id BIGINT REFERENCES users(id),
  rating INT CHECK (rating BETWEEN 1 AND 5),
  review_text TEXT,
  transaction_verified BOOLEAN DEFAULT FALSE,
  response TEXT,
  response_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- ============================================================
-- SUBSCRIPTIONS & BILLING
-- ============================================================

CREATE TABLE subscriptions (
  id BIGSERIAL PRIMARY KEY,
  user_id BIGINT REFERENCES users(id),
  plan TEXT NOT NULL,
  stripe_subscription_id TEXT,
  status TEXT CHECK (status IN ('active', 'cancelled', 'past_due', 'trialing')),
  current_period_start TIMESTAMPTZ,
  current_period_end TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- ============================================================
-- MAGAZINE & NEWSLETTER
-- ============================================================

CREATE TABLE magazine_issues (
  id SERIAL PRIMARY KEY,
  issue_number INT,
  title TEXT,
  cover_image TEXT,
  published_at DATE,
  borough_focus TEXT
);

CREATE TABLE newsletter_subscribers (
  id BIGSERIAL PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  user_id BIGINT REFERENCES users(id),
  editions TEXT[],  -- market_monday, professional_tuesday, etc.
  status TEXT DEFAULT 'active',
  subscribed_at TIMESTAMPTZ DEFAULT now()
);

-- ============================================================
-- EVENTS
-- ============================================================

CREATE TABLE events (
  id BIGSERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  type TEXT,  -- webinar, open_house, networking, workshop
  description TEXT,
  location TEXT,
  virtual_url TEXT,
  starts_at TIMESTAMPTZ,
  ends_at TIMESTAMPTZ,
  capacity INT,
  created_by BIGINT REFERENCES users(id)
);

CREATE TABLE event_attendees (
  event_id BIGINT REFERENCES events(id),
  user_id BIGINT REFERENCES users(id),
  status TEXT DEFAULT 'registered',
  PRIMARY KEY (event_id, user_id)
);

-- ============================================================
-- DATA PRODUCTS
-- ============================================================

CREATE TABLE area_data (
  id SERIAL PRIMARY KEY,
  borough TEXT NOT NULL,
  neighbourhood TEXT,
  avg_price NUMERIC,
  avg_rent NUMERIC,
  price_trend_12m NUMERIC,
  demand_score INT,
  supply_count INT,
  crime_rate NUMERIC,
  school_rating NUMERIC,
  transport_score INT,
  demographics JSONB,
  updated_at TIMESTAMPTZ DEFAULT now()
);

-- ============================================================
-- INDEXES
-- ============================================================

CREATE INDEX idx_properties_borough ON properties(borough);
CREATE INDEX idx_properties_postcode ON properties(postcode);
CREATE INDEX idx_properties_price ON properties(price);
CREATE INDEX idx_properties_status ON properties(status);
CREATE INDEX idx_properties_geo ON properties USING gist (point(longitude, latitude));
CREATE INDEX idx_leads_professional ON leads(professional_id);
CREATE INDEX idx_leads_stage ON leads(stage);
CREATE INDEX idx_leads_score ON leads(intent_score);
CREATE INDEX idx_user_events_user ON user_events(user_id);
CREATE INDEX idx_user_events_type ON user_events(event_type);
CREATE INDEX idx_user_events_created ON user_events(created_at);
CREATE INDEX idx_search_history_user ON search_history(user_id);
CREATE INDEX idx_content_type ON content(type);
CREATE INDEX idx_content_borough ON content(borough);
CREATE INDEX idx_content_status ON content(status);
CREATE INDEX idx_reviews_professional ON reviews(professional_id);
CREATE INDEX idx_area_data_borough ON area_data(borough);
CREATE INDEX idx_saved_searches_user ON saved_searches(user_id);
CREATE INDEX idx_professional_metrics_pro ON professional_metrics(professional_id);
```

---

## REVENUE MODEL

### Professional Tiers

| Tier | Price | Features |
|------|-------|----------|
| Pro | £299/mo | Listings, basic leads, profile, content publishing |
| Business | £999/mo | + AI apps, analytics, intent dashboard, heatmaps, content→lead pipeline |
| Enterprise | £2,500/mo | + prediction engine, first lead access, multi-branch, API, white-label |

### Consumer Tiers

| Tier | Price | Features |
|------|-------|----------|
| Free | £0 | Basic search, alerts, calculators, 3 professional matches |
| Premium | £9.99/mo | Full AI matching, market intelligence, "People Like You", priority responses |

### Revenue Streams at Scale

| Stream | Monthly | Annual |
|--------|---------|--------|
| Pro subscriptions (1,000 × £299) | £299K | £3.6M |
| Business subscriptions (500 × £999) | £499.5K | £6M |
| Enterprise subscriptions (200 × £2,500) | £500K | £6M |
| Consumer Premium (10,000 × £9.99) | £100K | £1.2M |
| Magazine | £90K | £1.08M |
| Video production | £140K | £1.68M |
| Newsletter sponsorship | £23K | £276K |
| Podcast sponsorship | £8.75K | £105K |
| Lead generation referrals | £50K | £600K |
| Data products | £40K | £480K |
| Advertising | £30K | £360K |
| **TOTAL** | **~£1.9M/mo** | **~£22.6M/yr** |

---

## BUILD PHASES

| Phase | Weeks | Pages | Focus |
|-------|-------|-------|-------|
| P1: Marketing MVP | 1-3 | 17 | Homepage, service pages, free video funnel, pricing, auth |
| P2: Spokes | 4-6 | 12 | Magazine, newsletter, podcast, video hubs |
| P3: Platform Public | 7-10 | 11 | Property search, area explorer, directory, content hub |
| P4: Pro Dashboard | 11-16 | 34 | Full B2B dashboard with intelligence features |
| P5: Consumer Dashboard | 17-22 | 28 | Full B2C dashboard with tools and AI advisor |
| **Total** | **22 weeks** | **102** | |

---

## KEY INTEGRATIONS

| Integration | Purpose | Phase |
|-------------|---------|-------|
| Mapbox GL JS | Interactive maps, property pins, area explorer | P3 |
| Stripe | Subscription billing, one-off payments | P1 |
| Beehiiv | Newsletter management, subscriber segmentation | P2 |
| PropertyData API | Market data, sold prices, rental data | P3 |
| Land Registry | Ownership data, transaction history | P3 |
| Planning Portal APIs | Planning applications, decisions | P3 |
| YouTube / Mux | Video hosting and streaming | P2 |
| Claude API | AI advisor, content assistant, matching | P4 |
| Twilio | SMS notifications, WhatsApp | P4 |
| PostHog | Analytics, funnels, feature flags | P1 |
| Resend / SendGrid | Transactional email | P1 |
| Supabase Auth | Authentication, OAuth | P1 |

---

## 7 COMPETITIVE MOAT PILLARS

1. **Behavioural Data** — consumer search patterns, intent signals no competitor has
2. **Professional Performance** — agent response times, conversion rates, real metrics
3. **Content Ecosystem** — 5 spokes creating compounding traffic + authority
4. **Network Effects** — more consumers = more valuable to pros = more pros = more consumers
5. **Data Intelligence** — 700K keywords, 51 segment reports, proprietary market data
6. **Switching Costs** — tools, data, reviews, connections all on platform
7. **Revenue Diversification** — not dependent on any single stream

---

*This specification provides full endpoint fidelity for 102 pages across 5 build phases. Feed into UI Assembly Pipeline for component matching and development sprints.*
