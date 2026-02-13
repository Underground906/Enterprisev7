# PROPERTY CONNECT LONDON — WEBSITE PRD
## Complete Site Architecture, Funnel Structure & Page Specifications

**Version:** 1.0  
**Date:** February 2026  
**Purpose:** Dev-ready blueprint for building the complete PCL web presence

---

## EXECUTIVE SUMMARY

### What You're Building

**THREE INTERCONNECTED WEB PROPERTIES:**

1. **PRESELL SITE** (propertyconnectlondon.com) — Marketing/education site that warms leads before they hit the platform
2. **THE PLATFORM** (app.propertyconnectlondon.com) — The actual product: B2B pro dashboard + B2C consumer dashboard
3. **THE SPOKES** (subdomains or sections) — Magazine, Newsletter, Podcast, Video, CTV landing pages

**PLUS FUNNELS:**
- Free Video Lead Magnet Funnel
- Sponsorship Application Funnel
- Platform Trial Funnel
- Magazine Subscription Funnel

### Revenue Targets (Year 1)
- Magazine: £2.68M (editorial sponsors £1.45M + ads £440K + subs £400K + sponsor packages £125K)
- Platform: £8.21M (business users + enhanced consumers)
- Video Production: £900K
- CTV Subscriptions: £120K
- **Total Y1 Target: £11.9M**

---

## PART 1: SITE ARCHITECTURE OVERVIEW

```
propertyconnectlondon.com (PRESELL/MARKETING SITE)
├── / (Homepage - Central Sales Page)
├── /about
├── /services
│   ├── /services/video-production
│   ├── /services/magazine-advertising
│   ├── /services/content-creation
│   ├── /services/platform-marketing
│   └── /services/sponsorship
├── /magazine
│   ├── /magazine/current-issue
│   ├── /magazine/archive
│   ├── /magazine/subscribe
│   └── /magazine/advertise
├── /podcast
│   ├── /podcast/episodes
│   ├── /podcast/guests
│   └── /podcast/sponsor
├── /video
│   └── /video/property-tours
├── /tv (Connected TV)
│   └── /tv/subscribe
├── /platform (Platform landing/education)
│   ├── /platform/professionals
│   └── /platform/consumers
├── /pricing
├── /blog
├── /contact
└── /free-video (Lead Magnet Funnel)

app.propertyconnectlondon.com (THE PLATFORM)
├── /login
├── /register
├── /onboarding
├── PRO DASHBOARD (/pro/...)
│   ├── /pro/dashboard
│   ├── /pro/content
│   ├── /pro/clients
│   ├── /pro/analytics
│   ├── /pro/profile
│   ├── /pro/marketing
│   ├── /pro/learning
│   ├── /pro/community
│   └── /pro/settings
└── CONSUMER DASHBOARD (/user/...)
    ├── /user/dashboard
    ├── /user/feed
    ├── /user/explore
    ├── /user/experts
    ├── /user/tools
    ├── /user/learning
    ├── /user/community
    └── /user/settings

PUBLIC PLATFORM PAGES (app.propertyconnectlondon.com)
├── /search (Property search)
├── /areas (Area explorer)
├── /directory (Professional directory)
├── /content (Content hub - articles, videos, podcasts)
├── /events
├── /jobs
└── /shop
```

---

## PART 2: PRESELL SITE (Marketing Website)

### Purpose
Educate visitors on what PCL offers, build trust, capture leads, and drive them to either:
- Sign up for platform (free or paid)
- Book a call for B2B services
- Subscribe to magazine/newsletter
- Claim free video offer

### 2.1 HOMEPAGE (Central Sales Page)

**URL:** propertyconnectlondon.com/

**Page Structure (16 Sections):**

| # | Section | Content |
|---|---------|---------|
| 1 | **Hero** | Headline + subhead + primary CTA |
| 2 | **Problem** | What's broken in property marketing |
| 3 | **Agitation** | Cost of staying stuck |
| 4 | **Solution Intro** | The Omni-Channel Content Engine™ |
| 5 | **How It Works** | 3-step process visual |
| 6 | **Our Channels** | Magazine, Podcast, Video, CTV, Platform icons/cards |
| 7 | **Who We Serve** | Pro segments (agents, developers, investors, etc.) |
| 8 | **Platform Preview** | Screenshot/video of dashboard |
| 9 | **Results/Proof** | Stats, testimonials, case studies |
| 10 | **Pricing Preview** | 3-tier cards (link to /pricing) |
| 11 | **Our Story** | Brief founder story |
| 12 | **FAQ** | Top 5 questions |
| 13 | **Free Offer CTA** | "Get Your Free Video" banner |
| 14 | **Newsletter Signup** | Email capture |
| 15 | **Trust Badges** | Logos, certifications, press mentions |
| 16 | **Footer CTA** | Final push + contact |

**Key Copy Elements:**

```
HEADLINE OPTIONS:
- "Your Competitors Are Everywhere — Why Aren't You?"
- "The First Omni-Channel Property Media Platform"
- "10x Your Property Marketing — Without 10x the Effort"

SUBHEAD:
Get your content in front of your ideal clients across print, digital, 
social, and Connected TV — all from one platform.

PRIMARY CTA: "See How It Works" → /platform/professionals
SECONDARY CTA: "Get Your Free Video" → /free-video
```

**Components Needed:**
- Hero with video background (property footage)
- Animated channel cards (hover states)
- Testimonial carousel
- Pricing comparison table (mini)
- Email capture with segment selection
- FAQ accordion

---

### 2.2 SERVICES PAGES

**URL Pattern:** /services/{service-slug}

#### 2.2.1 Video Production Service Page

**URL:** /services/video-production

| Section | Content |
|---------|---------|
| Hero | "Professional Property Video Tours" + example reel |
| Problem | DIY videos look amateur, hurt brand |
| Solution | The Content Multiplier Engine™ — 20 videos from 1 shoot |
| Packages | Tour packages with pricing |
| Portfolio | Before/after, showcase grid |
| Process | Book → Shoot → Edit → Distribute |
| CTA | "Get Your Free Video" |

**Packages to Display:**
- Single Property Tour: £1,295
- 5-Pack: £5,000 (save £1,475)
- 10-Pack: £8,000 (save £4,950)
- 20-Pack Monthly: £12,000/mo

---

#### 2.2.2 Magazine Advertising Service Page

**URL:** /services/magazine-advertising

| Section | Content |
|---------|---------|
| Hero | Magazine cover image + "Reach 50,000 Londoners Monthly" |
| Why Print | Stats on print effectiveness (from MPA research) |
| The Model | Rotational Reach Maximizer™ — 12 boroughs/year |
| Ad Formats | Full page, half, quarter, DPS with pricing |
| Editorial Packages | Feature, interview, advertorial options |
| Distribution | Map showing borough rotation |
| CTA | "Download Media Kit" / "Book a Call" |

**Pricing Display:**
- Quarter Page: £1,500
- Half Page: £2,500
- Full Page: £4,500
- DPS: £8,000
- Editorial Feature: £6,000/month (12-month commitment)

---

#### 2.2.3 Sponsorship Service Page

**URL:** /services/sponsorship

| Section | Content |
|---------|---------|
| Hero | "Become the Go-To Name in Your Niche" |
| What You Get | Exclusive category ownership |
| Package Breakdown | Platform section, magazine, newsletter, podcast |
| ROI Calculator | Input their niche → show reach/value |
| Testimonials | Sponsor success stories |
| CTA | "Apply for Sponsorship" → form |

**Sponsorship Tiers:**
- Bronze: £2,500/month (1 channel)
- Silver: £5,000/month (3 channels)
- Gold: £7,500/month (all channels + exclusivity)
- Platinum: £9,750/month (everything + quarterly feature)

---

### 2.3 MAGAZINE SECTION

**URL:** /magazine

**Sub-pages:**
- /magazine/current-issue — Flipbook embed + highlights
- /magazine/archive — Past issues grid
- /magazine/subscribe — £7.99/mo or £79/year
- /magazine/advertise — Links to /services/magazine-advertising
- /magazine/contribute — Writer/expert submission form

---

### 2.4 PODCAST SECTION

**URL:** /podcast

**Sub-pages:**
- /podcast/episodes — Episode grid with player
- /podcast/guests — Guest directory with bio + episodes
- /podcast/sponsor — Sponsorship opportunities
- /podcast/apply — Guest application form

---

### 2.5 VIDEO/CTV SECTION

**URL:** /video and /tv

**Video Sub-pages:**
- /video/property-tours — Showcase of produced tours
- /video/services — Links to video production service

**TV Sub-pages:**
- /tv — CTV channel overview
- /tv/subscribe — £9.99/month streaming subscription
- /tv/apps — Download links for Fire TV, Apple TV, Roku

---

### 2.6 PLATFORM LANDING PAGES

**URL:** /platform

Two distinct landing pages for the two audiences:

#### /platform/professionals (B2B)
| Section | Content |
|---------|---------|
| Hero | "Your Command Center for Property Marketing" |
| Dashboard Preview | Animated GIF/video of pro dashboard |
| Key Features | Content hub, client management, analytics, AI tools |
| Pricing | £199/mo Pro, £499/mo Business, £999/mo Enterprise |
| Free Trial CTA | "Start 14-Day Free Trial" |

#### /platform/consumers (B2C)
| Section | Content |
|---------|---------|
| Hero | "Find Your Perfect Property Expert" |
| Feed Preview | Personalized content discovery |
| Key Features | Expert finder, tools, learning, community |
| Pricing | Free / £9.99 Enhanced / £19.99 Pro |
| Sign Up CTA | "Create Free Account" |

---

### 2.7 PRICING PAGE

**URL:** /pricing

**Structure:**
1. Toggle: Professionals | Consumers
2. Tier cards (3-4 per audience)
3. Feature comparison table
4. FAQ
5. "Not sure? Book a call" CTA

**Professional Tiers:**
| Tier | Price | Key Features |
|------|-------|--------------|
| Starter | Free | Basic profile, 3 posts/month |
| Pro | £199/mo | Unlimited content, analytics, lead tools |
| Business | £499/mo | Team accounts, CRM, priority support |
| Enterprise | £999/mo | White-label, API access, dedicated manager |

**Consumer Tiers:**
| Tier | Price | Key Features |
|------|-------|--------------|
| Free | £0 | Browse, save, basic tools |
| Enhanced | £9.99/mo | Priority alerts, full tools, ad-free |
| Pro | £19.99/mo | All tools, premium content, direct expert access |

---

### 2.8 FREE VIDEO FUNNEL (Lead Magnet)

**URL:** /free-video

**Funnel Flow:**
```
/free-video (Landing Page)
    ↓ [Claim Your Free Video]
/free-video/apply (Application Form)
    ↓ [Submit]
/free-video/thank-you (Confirmation + Upsell)
    ↓ [Email Sequence]
Discovery Call Booking
```

**Landing Page Sections:**
1. Headline: "Get a £1,295 Professional Property Video — FREE"
2. Video preview (sample tour)
3. What's included (shoot, edit, distribution)
4. Why we're doing this (build relationship)
5. Who qualifies (London property pros)
6. Simple form (name, email, company, property type)
7. FAQ (no catch, no obligation)

**Form Fields:**
- Full Name
- Email
- Company Name
- Role (dropdown: Agent, Developer, Investor, Other)
- Property Type (dropdown: Residential, Commercial, Development)
- Borough/Area
- Phone (optional)

---

## PART 3: THE PLATFORM (Product)

### 3.1 PUBLIC PAGES (No Auth Required)

#### Property Search
**URL:** /search

**Features:**
- Map-based search (Mapbox/Google Maps)
- Filter panel: price, beds, type, area
- List/Grid/Map view toggle
- Save search, set alerts (requires login)
- Property cards with quick view

#### Area Explorer
**URL:** /areas

**Features:**
- Interactive London map (clickable boroughs)
- Per-area pages with:
  - Price data (avg, trends)
  - Schools (Ofsted ratings)
  - Transport (tube/rail times)
  - Crime stats
  - Demographics
  - Development pipeline
- Compare areas (side-by-side)

#### Professional Directory
**URL:** /directory

**Categories (from your 7 pillars):**
- Estate Agents
- Letting Agents
- Property Managers
- Mortgage Brokers
- Solicitors/Conveyancers
- Surveyors
- Architects
- Interior Designers
- Builders/Contractors
- Investment Advisors
- Tax Accountants
- Insurance Brokers

**Listing Tiers:**
- Basic (free): Name, contact, 1 photo
- Enhanced (£199/mo): Full profile, reviews, featured
- Premium (£499/mo): Top placement, badges, lead priority

#### Content Hub
**URL:** /content

**Content Types (from Miro export):**
- Articles
- Videos
- Podcasts
- Properties
- Projects
- Jobs
- Events
- Q&A
- Shop/Products

---

### 3.2 PRO DASHBOARD (B2B — Authenticated)

**Base URL:** /pro/

#### Dashboard Home (/pro/dashboard)
| Component | Data |
|-----------|------|
| Quick Stats Panel | Profile views, content engagement, leads, appointments |
| Activity Feed | Recent interactions, comments, inquiries |
| Performance Snapshot | Charts: views, engagement, leads over time |
| Market Pulse | Trending topics, competitor activity, AI content suggestions |
| Upcoming | Scheduled content, appointments, events |

#### Content Management Hub (/pro/content)
| Sub-section | Features |
|-------------|----------|
| Content Library | All published + drafts + scheduled |
| Content Creation Tools | Article editor, video upload, podcast publisher, listing creator, event builder, job posting |
| Media Library | Images, videos, documents |
| Content Calendar | Visual scheduler with AI optimal time suggestions |
| Distribution | Platform feed, social integration, newsletter, syndication |
| AI Assistant | Content suggestions, writing help, SEO optimization |

#### Client Management Center (/pro/clients)
| Sub-section | Features |
|-------------|----------|
| Client Database | Contact management, communication history, notes |
| Lead Management | New leads, qualification, follow-up scheduling |
| Client Journey | Status tracking (inquiry → consultation → service → follow-up) |
| Testimonials | Review management, request tools, showcase builder |

#### Analytics & Insights (/pro/analytics)
| Sub-section | Features |
|-------------|----------|
| Performance Dashboard | Content by type, audience demographics, engagement, leads |
| Competitive Analysis | Market position, peer benchmarks, gap analysis |
| Custom Reports | Drag-drop builder, scheduled exports |

#### Business Profile (/pro/profile)
| Sub-section | Features |
|-------------|----------|
| Profile Editor | Services, expertise, coverage, credentials, team, portfolio |
| Service Packages | Package builder, pricing, availability, booking |

#### Marketing Tools (/pro/marketing)
| Sub-section | Features |
|-------------|----------|
| Campaign Builder | Multi-channel campaigns, audience selector, calendar |
| Email Marketing | Templates, segmentation, sequences, A/B testing |
| Promotional Tools | Special offers, referral program, loyalty system |

#### Learning Center (/pro/learning)
| Sub-section | Features |
|-------------|----------|
| Market Research | Industry reports, trends, consumer studies, regulatory updates |
| Professional Development | Courses, certifications, webinars, best practices |

#### Community & Networking (/pro/community)
| Sub-section | Features |
|-------------|----------|
| Professional Network | Connections, collaborations, referrals, partnerships |
| Community Engagement | Forums, Q&A, expert panels, speaking opportunities |
| Event Management | Webinars, in-person, virtual meetups |

#### Settings & Integrations (/pro/settings)
| Sub-section | Features |
|-------------|----------|
| Account Settings | Subscription, billing, notifications, privacy |
| Integrations | CRM, email platforms, social, calendar, property software |

---

### 3.3 CONSUMER DASHBOARD (B2C — Authenticated)

**Base URL:** /user/

#### Dashboard Home (/user/dashboard)
| Component | Data |
|-----------|------|
| Personalized Feed | AI-curated content based on interests |
| Market Pulse | Price trends, news, rate updates for saved areas |
| Quick Tools | Property search, calculators, expert finder |
| Saved Items | Properties, areas, experts, content |
| Activity | Recent searches, viewed content |

#### Content & Feed (/user/feed)
| Features |
|----------|
| Content Library | Articles, videos, podcasts filtered by interests |
| Followed Experts | New content from followed professionals |
| Trending | Popular in selected interests |
| Recommendations | AI suggestions based on behavior |

#### Property Explorer (/user/explore)
| Sub-section | Features |
|-------------|----------|
| Advanced Search | Map, filters, save, compare |
| Market Analysis | Price comparison, trends, rental yields |
| New Developments | Off-plan, completed projects, developer profiles |

#### Expert Finder (/user/experts)
| Sub-section | Features |
|-------------|----------|
| Directory | Search by specialty, location, ratings |
| Comparison | Side-by-side, fees, reviews |
| Consultation Booking | Calendar, video/call options, questionnaires |
| Expert Q&A | Public questions, answered archive |

#### Tools (/user/tools)
| Tool | Function |
|------|----------|
| Property Search | Advanced search with save |
| Mortgage Calculator | Affordability, repayments |
| Stamp Duty Calculator | Including surcharges |
| Rental Yield Calculator | For investors |
| Property Value Estimator | AVM estimate |
| Budget Planner | All costs breakdown |

#### Learning Hub (/user/learning)
| Sub-section | Features |
|-------------|----------|
| Beginner Guides | By journey stage (buying, renting, etc.) |
| Process Maps | Step-by-step for each journey |
| Video Tutorials | How-tos |
| Jargon Buster | Terminology explained |
| Templates & Checklists | Downloadable resources |

#### Community (/user/community)
| Sub-section | Features |
|-------------|----------|
| Discussion Forums | By category, Q&A, local areas |
| Reviews | Professional services, developments, areas |
| Events | Viewings, open houses, webinars, auctions |
| Marketplace | Services, items, deals |

#### Settings (/user/settings)
| Sub-section | Features |
|-------------|----------|
| Content Preferences | Interests, expert suggestions, format preferences |
| Notifications | Email, mobile, frequency |
| Privacy | Visibility, data sharing, communication |
| Account | Profile, subscription, security |

---

## PART 4: PAGE COMPONENT LIBRARY

### Required UI Components

**Navigation:**
- Main nav (desktop mega menu)
- Mobile nav (hamburger + drawer)
- Dashboard sidebar
- Breadcrumbs
- Tab navigation

**Heroes:**
- Video background hero
- Split hero (text + image/video)
- Centered hero
- Dashboard header with stats

**Cards:**
- Service card (icon, title, description, CTA)
- Pricing card (tier, price, features, CTA)
- Property card (image, price, beds, location)
- Expert card (photo, name, specialty, rating)
- Content card (thumbnail, title, type badge, date)
- Testimonial card (quote, photo, name, company)

**Forms:**
- Contact form
- Lead capture (email + segment)
- Multi-step application form
- Search filters panel
- Profile editor

**Data Display:**
- Stats grid (4-up metrics)
- Comparison table
- Feature checklist
- Timeline/process steps
- Charts (line, bar, pie)
- Interactive map

**Feedback:**
- Toast notifications
- Modal dialogs
- Empty states
- Loading skeletons
- Error states

**Content:**
- Article layout
- Video player embed
- Podcast player
- FAQ accordion
- Tabbed content
- Image gallery/lightbox

---

## PART 5: TECHNICAL REQUIREMENTS

### Stack Recommendation
- **Frontend:** Next.js 14+ (App Router)
- **Styling:** Tailwind CSS + shadcn/ui
- **Backend:** Supabase (Auth, Database, Storage)
- **Maps:** Mapbox GL JS
- **Video:** Mux or Cloudflare Stream
- **Email:** Resend or SendGrid
- **Payments:** Stripe
- **Analytics:** PostHog or Mixpanel
- **CMS:** Sanity or Payload (for blog/magazine content)

### Key Integrations
- Property data: PropertyData API, Land Registry
- Calendar: Google Calendar, Outlook
- CRM: Reapit, Alto (for estate agents)
- Social: LinkedIn, Instagram, YouTube APIs
- Streaming: Fire TV, Apple TV, Roku SDKs (for CTV)

### Database Schema (Core Tables)
```sql
-- Users
users (id, email, role, profile_data, created_at)
user_preferences (user_id, interests[], notification_settings)

-- Professionals
professionals (id, user_id, business_name, tier, profile_data)
professional_services (professional_id, service_type, pricing)

-- Content
content (id, author_id, type, title, body, status, published_at)
content_engagement (content_id, user_id, action_type, created_at)

-- Properties
properties (id, professional_id, address, price, beds, type, data)
property_alerts (user_id, search_criteria, frequency)

-- Leads
leads (id, professional_id, user_id, source, status, created_at)
lead_activities (lead_id, activity_type, notes, created_at)

-- Subscriptions
subscriptions (id, user_id, tier, stripe_subscription_id, status)
```

---

## PART 6: BUILD PRIORITY

### Phase 1: Marketing Site MVP (Weeks 1-3)
1. Homepage (16-section layout)
2. /services/video-production
3. /services/magazine-advertising
4. /free-video funnel (lead magnet)
5. /pricing
6. /contact
7. Email capture + basic CRM

**Deliverables:** Live marketing site capturing leads

### Phase 2: Platform Shell (Weeks 4-6)
1. Auth (login/register/onboarding)
2. Pro dashboard shell (navigation + quick stats)
3. Consumer dashboard shell
4. Public directory page
5. Public content hub

**Deliverables:** Working platform users can log into

### Phase 3: Core Features (Weeks 7-10)
1. Pro: Content creation tools
2. Pro: Profile management
3. Pro: Basic analytics
4. Consumer: Feed + preferences
5. Consumer: Expert finder
6. Consumer: Basic tools (calculators)

**Deliverables:** Functional MVP for both audiences

### Phase 4: Spoke Integration (Weeks 11-14)
1. Magazine section + subscription
2. Podcast section + player
3. Video section + player
4. CTV landing page
5. Newsletter integration (Beehiiv embed)

**Deliverables:** Full spoke ecosystem connected

### Phase 5: Advanced Features (Weeks 15-20)
1. Pro: Full CRM + lead management
2. Pro: Marketing tools + campaigns
3. Consumer: Full property search + alerts
4. Consumer: Area explorer
5. Integrations (Stripe, calendars, social)

**Deliverables:** Production-ready platform

---

## PART 7: DEMO/PROMO ASSETS NEEDED

### GIFs/Videos for Marketing
1. **Pro Dashboard Overview** — 15-sec GIF showing dashboard navigation
2. **Content Creation Flow** — 20-sec video: create article → schedule → publish
3. **Lead Management** — 15-sec GIF: new lead notification → qualification → follow-up
4. **Consumer Feed** — 15-sec GIF: personalized feed scrolling, saving content
5. **Expert Finder** — 20-sec video: search → compare → book consultation
6. **Property Search** — 15-sec GIF: map search → filters → save
7. **Calculator Tools** — 10-sec GIF: mortgage calculator in action
8. **Magazine Flipbook** — 10-sec preview of digital magazine
9. **Video Tour Sample** — 30-sec highlight reel of property tours
10. **CTV Interface** — 15-sec preview of TV app

### Screenshots Needed
- Pro dashboard home (with sample data)
- Content editor
- Analytics charts
- Consumer feed
- Expert profile page
- Property listing page
- Mobile app screens (if applicable)

---

## APPENDIX: COPY CHEAT SHEET

### Headlines by Page

| Page | Headline |
|------|----------|
| Homepage | "Your Competitors Are Everywhere — Why Aren't You?" |
| Video Service | "Professional Property Videos That Sell" |
| Magazine | "Reach 50,000 London Property Buyers Monthly" |
| Sponsorship | "Own Your Category. Become the Go-To Name." |
| Platform (Pro) | "Your Command Center for Property Marketing" |
| Platform (Consumer) | "Find Your Perfect Property Expert" |
| Free Video | "Get a £1,295 Property Video — FREE" |
| Pricing | "Choose Your Path to Property Marketing Success" |

### Unique Mechanisms (Proprietary Names)

| Name | What It Is |
|------|------------|
| **Omni-Channel Content Engine™** | The full ecosystem: one content piece → multiple channels |
| **Content Multiplier Engine™** | Video production: 1 shoot day → 20 videos |
| **Rotational Reach Maximizer™** | Magazine: 12 boroughs/year = 600K readers |
| **Content Discovery Network™** | Platform: AI-personalized feeds matching users to experts |

### Key Stats to Use
- 50,000 magazine readers per borough
- 600,000 annual reach (12 boroughs)
- 20x content multiplier (video production)
- 200+ professional categories
- 32 London boroughs covered
- 7 property pillars (buy, sell, rent, let, invest, renovate, build)

---

## NEXT STEPS

1. **Review this PRD** — Flag any missing pages or features
2. **Confirm priority** — Which phase to start with
3. **Design system** — Build UI component library
4. **Wireframes** — Low-fi layouts for priority pages
5. **React demos** — Build interactive prototypes for key flows
6. **Content population** — Write clean copy for each page section

**Ready to start building the UI library and page templates?**
