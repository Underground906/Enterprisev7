# Property Connect London — AI Apps Complete Specification

> **Version:** 1.0
> **Date:** 2026-02-17
> **Purpose:** Full spec for all 52 B2B professional apps (6 suites) + 20+ B2C consumer apps.
> **Source:** PCL_APPS_PRD.md, 01_ESTATE_AGENTS_AI_SUITE.md, B2C_CONSUMER_PLATFORM_STRATEGY.md
> **Deployment:** White-label (on client sites) + Platform-native (on PCL) + Hybrid (both)

---

## Architecture

Every app follows the same deployment pattern:

```
┌────────────────────────────────┐
│      CORE CALCULATION ENGINE    │
│  (Deal analysis, valuations,    │
│   matching, scoring, routing)   │
└──────────┬─────────────────────┘
     ┌─────┼─────┐
     ↓     ↓     ↓
   B2B   B2C   B2C
   API   Web   App
   │     │     │
   ↓     ↓     ↓
 Agent's  PCL   PCL
 Website  .com  App
```

Same code, different deployment — multi-tenant with shared core, isolated data.

### Standard App Components

Every app includes:
- **Chat Widget** — Conversational AI interface (Claude API)
- **Config JSON** — Per-client branding, tone, knowledge base, rules
- **Admin Panel** — Client manages settings, views analytics
- **Analytics Dashboard** — Usage, leads captured, conversion tracking
- **Webhook System** — Pipe leads/data to client's CRM
- **Embed Script** — `<script>` tag for white-label deployment

### Tech Stack Per App

| Layer | Technology |
|-------|-----------|
| Frontend | React widget (embeddable), Next.js (platform) |
| AI | Claude API (conversation), pgvector (knowledge retrieval) |
| Backend | Next.js API routes, PostgreSQL |
| Deployment | Docker per-client, Vercel for platform |
| Payments | Stripe (subscription + metered billing) |

---

## Revenue Model

| Pricing Tier | Setup Fee | Monthly | Target |
|-------------|-----------|---------|--------|
| Single App | £2K-5K | £99-499/mo | Small independents |
| Suite (6-12 apps) | £5K-10K | £990-2,990/mo | Medium agencies |
| Full Platform | £10K+ | £4,990-7,990/mo | Enterprise chains |

### Unit Economics Example
- Estate agent pays £1,490/mo for AI Property Concierge
- One closed deal from AI-captured lead = £8,250 commission
- ROI: 0.18 deals/month to break even = **454% annual ROI**

---

# B2B SUITE 1: ESTATE AGENTS (18 Apps)

**Market:** 5,000+ agencies in London, 15,000+ branches, £2.5B+ annual commission.
**Target Tiers:** Ultra-Prime (£2-50M+), Premium Independents (£1-5M), Growth Chains.

---

## APP EA_01: AI PROPERTY CONCIERGE

**Type:** Client-facing widget (Type A)
**Deploy:** White-label on agent's website + PCL platform
**Pricing:** £1,490/mo + £490/mo per additional branch. Setup: £2,500

### What It Does

| Function | Description |
|----------|-------------|
| Greet & Engage | Time-aware greeting, return visitor detection, personalisation |
| Qualify Leads | Budget, timeline, situation, area, mortgage status, chain position |
| Answer Questions | Connected to live listing feed, area data, school/transport info |
| Book Viewings | Calendar integration, group bookings, confirmation + reminders |
| Capture Leads | Progressive capture (name → email → phone), quality scoring, CRM routing |
| 24/7 Operation | Never sleeps, handles multiple conversations, escalates to human when needed |

### Screen: Widget Interface

**Layout:** Floating chat bubble (bottom-right) → expands to chat panel

| State | Description |
|-------|-------------|
| `EA01.bubble` | Floating button with greeting preview |
| `EA01.open` | Chat panel open — greeting message displayed |
| `EA01.conversation` | Active chat with AI |
| `EA01.booking` | Calendar view for viewing booking |
| `EA01.captured` | Lead captured — thank you + next steps |
| `EA01.handoff` | Escalated to human agent — "Connecting you with [Agent Name]" |

### Components

| Component | Type | Details |
|-----------|------|---------|
| Chat Bubble | `floating_button` | Pulsing dot, configurable position, brand-coloured |
| Chat Panel | `panel` | Agent branding header, message thread, input bar |
| AI Message | `chat_message` | Text + property cards + area data cards + quick reply buttons |
| Property Card (inline) | `card` | Image, price, address, beds, "View Details" / "Book Viewing" |
| Lead Capture Form | `form` | Progressive: first name → email → phone → preferences (appears naturally in chat) |
| Calendar Picker | `calendar` | Available viewing slots from agent's calendar |
| Typing Indicator | `animation` | Dots animation while AI processes |
| Quick Replies | `chip_group` | Suggested responses: "I'm looking to buy", "What's available in [area]?" |

### Admin Panel

| Section | Features |
|---------|----------|
| Dashboard | Conversations today, leads captured, viewings booked, response time |
| Conversations | Full chat logs, lead quality scores, handoff records |
| Knowledge Base | Upload listings feed, area data, FAQs, company info |
| Settings | Brand colours, logo, greeting message, working hours, escalation rules |
| Integrations | CRM (Reapit, Alto, Street), Calendar (Google/Outlook), Portal feeds (Rightmove) |
| Analytics | Conversion funnel, busiest hours, common questions, lead sources |

### Database

| Table | Key Fields |
|-------|------------|
| `app_instances` | client_id, app_type, config (JSONB), active |
| `conversations` | instance_id, visitor_id, messages (JSONB), lead_score, status |
| `captured_leads` | instance_id, name, email, phone, preferences, score, source |
| `viewing_bookings` | lead_id, property_id, datetime, status, confirmed |
| `app_analytics` | instance_id, date, conversations, leads, viewings, conversions |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/api/v1/apps/ea01/chat` | Send message, get AI response |
| GET | `/api/v1/apps/ea01/properties` | Get listings for this instance |
| POST | `/api/v1/apps/ea01/leads` | Capture lead |
| POST | `/api/v1/apps/ea01/viewings` | Book viewing |
| GET | `/api/v1/apps/ea01/analytics` | Instance analytics |
| PATCH | `/api/v1/apps/ea01/config` | Update instance config |

---

## APPS EA_02-18: REMAINING ESTATE AGENT APPS

### EA_02: AI Listing Engine
**Type B (Agent-facing)** | £990/mo
- AI-generates property descriptions from photos + floor plans + features
- SEO-optimized for portal listing
- Multiple tone options (luxury, family, investment)
- Auto-generates social media posts per listing

### EA_03: Viewing Scheduler
**Type A (Client-facing)** | £490/mo
- Calendar integration, self-service booking
- Automated confirmations + reminders (email + SMS)
- Group viewing management
- Post-viewing feedback collection

### EA_04: Lead Intelligence
**Type B (Agent-facing)** | £1,490/mo (Business tier feature)
- Lead scoring (0-100) based on behavioural signals
- Buyer readiness breakdown
- Recommended approach per lead
- Optimal contact timing

### EA_05: Market Report Generator
**Type B (Agent-facing)** | £990/mo
- Auto-generates branded area market reports
- Data from PropertyData API + Land Registry
- Monthly or on-demand
- PDF export, email-ready, social shareable

### EA_06: Vendor Management System
**Type B (Agent-facing)** | £1,490/mo
- Vendor pipeline: instruction → marketing → viewings → offers → exchange → completion
- Automated vendor updates at each stage
- Comparable evidence for pricing discussions
- Price reduction recommendation engine

### EA_07: Property Comparison Tool
**Type A (Client-facing)** | £490/mo
- Side-by-side comparison of 2-4 properties
- Auto-populated data (price, specs, area stats)
- Shareable comparison reports
- "Which is right for me?" AI advisor

### EA_08: Area Intelligence Bot
**Type A (Client-facing)** | £790/mo
- Chat-based area Q&A: schools, transport, crime, prices, lifestyle
- Connected to live data sources
- Borough + neighbourhood level detail
- "What's it like to live in [area]?" conversational format

### EA_09: Chain Tracker
**Type B (Agent-facing)** + **Type A (Client-facing)** | £790/mo
- Visual chain diagram (who's waiting on whom)
- Status updates per link in chain
- Delay alerting + suggested interventions
- Client-facing view: "Where am I in the chain?"

### EA_10: AI Voice Receptionist
**Type A (Client-facing)** | £1,990/mo
- Phone answering AI (via Twilio)
- Books viewings, captures leads, answers FAQs
- Transfers to human when needed
- After-hours coverage

### EA_11: Full Property Intelligence Suite
**Type C (Management dashboard)** | £4,990/mo
- Aggregates all agent tools into single dashboard
- Cross-listing analytics
- Team performance
- Market positioning

### EA_12: White-Label Data Portal
**Type D (Full suite)** | £2,990/mo
- Branded market data portal on agent's website
- Area data, price trends, heatmaps
- Lead generation through data access

### EA_13: Competitor Intelligence
**Type B** | £1,490/mo
- Track competitor listings, pricing, time on market
- Market share analysis
- Win/loss analysis

### EA_14: AI Negotiation Coach
**Type B** | £990/mo
- AI analyses offer vs comparable data
- Recommends counter-offer strategies
- Vendor communication templates
- Market evidence compilation

### EA_15: Staff Training Academy
**Type B** | £1,490/mo
- AI-powered training modules
- Role-play scenarios (buyer calls, vendor appointments)
- Performance assessment
- Onboarding automation

### EA_16: Video-to-3D Converter
**Type B** | £2,990/mo
- Convert video tours to interactive 3D walkthroughs
- Floor plan generation from video
- Virtual staging overlay
- Embed on listings

### EA_17: Multi-Branch Command Center
**Type C** | £7,990/mo (Enterprise)
- Aggregate view across all branches
- Lead routing between branches
- Performance benchmarking
- Resource allocation

### EA_18: Compliance Monitor
**Type B** | £490/mo
- Tracks regulatory requirements (AML, GDPR, CPRs)
- Document checklist per transaction
- Expiry alerts for certifications
- Audit trail

---

# B2B SUITE 2: LETTING AGENTS (12 Apps)

**Pricing range:** £990-2,990/mo

| App | Name | Type | Price | Key Features |
|-----|------|------|-------|-------------|
| LA_01 | Tenant Acquisition Bot | A | £990/mo | Chat widget for rental enquiries, viewings, lead capture |
| LA_02 | Tenant Screening | B | £990/mo | AI-powered reference checking, credit scoring, risk assessment |
| LA_03 | Compliance Command Center | B | £1,490/mo | Gas safety, EPC, deposit protection, licensing — deadline tracking + auto-alerts |
| LA_04 | Maintenance Dispatch | A+B | £990/mo | Tenant reports issue → AI triages → routes to contractor → tracks resolution |
| LA_05 | Landlord Portal | A | £1,490/mo | White-label portal for landlord clients: income, expenses, compliance, reports |
| LA_06 | Rent Collection Intelligence | B | £990/mo | Payment tracking, arrears prediction, auto-reminders, escalation workflow |
| LA_07 | HMO Navigator | B | £1,990/mo | HMO licensing rules by borough, compliance checker, room-by-room assessment |
| LA_08 | Tenancy Document Generator | B | £490/mo | AI generates: ASTs, section notices, inspection reports, inventories |
| LA_09 | Tenant Communication Hub | A+B | £990/mo | Unified messaging: tenant ↔ agent ↔ landlord with templates + scheduling |
| LA_10 | Void Period Optimizer | B | £990/mo | Predicts void periods, recommends pricing/marketing changes, benchmarks |
| LA_11 | Section Notice Generator | B | £490/mo | Generate section 8/21/13 notices with AI compliance checking |
| LA_12 | Inventory Report Generator | B | £790/mo | Photo + AI description → professional inventory report |

---

# B2B SUITE 3: PROPERTY INVESTORS (10 Apps)

**Pricing range:** £990-4,990/mo

| App | Name | Type | Price | Key Features |
|-----|------|------|-------|-------------|
| PI_01 | Deal Analyzer Pro | B | £1,990/mo | Input property details → AI calculates: yield, ROI, cash flow, stress test |
| PI_02 | Portfolio Command Center | C | £2,990/mo | All properties: valuations, income, expenses, performance, rebalancing |
| PI_03 | Auction Intelligence | B | £1,490/mo | Track auctions, price predictions, lot analysis, alert on criteria matches |
| PI_04 | Development Feasibility | B | £2,990/mo | Land + build cost + planning + sales analysis → viability report |
| PI_05 | Tax Optimization Advisor | B | £990/mo | Structure analysis (personal/LTD/trust), CGT planning, expense optimization |
| PI_06 | Market Timing System | B | £1,490/mo | Buy/hold/sell signals based on market data + economic indicators |
| PI_07 | Refinance Calculator Pro | B | £990/mo | Current vs available rates, equity release options, cost analysis |
| PI_08 | Comparable Finder | B | £990/mo | Find comparables by criteria, data from Land Registry + portals |
| PI_09 | Cash Flow Projector | B | £990/mo | Multi-year projections with scenario modelling (rate changes, voids, capex) |
| PI_10 | Investor Deal Flow Platform | C | £4,990/mo | Source off-market deals, manage pipeline, investor matching |

---

# B2B SUITE 4: HOME FURNISHING & E-COMMERCE (8 Apps)

**Pricing range:** £990-2,990/mo

| App | Name | Type | Price | Key Features |
|-----|------|------|-------|-------------|
| HF_01 | AI Shopping Concierge | A | £1,490/mo | Chat-based product discovery, room-based recommendations |
| HF_02 | Room Design Advisor | A | £990/mo | Upload room photo → AI suggests furniture/decor from catalog |
| HF_03 | Product Comparison Engine | A | £990/mo | Side-by-side product comparison with specs + reviews |
| HF_04 | Style Quiz System | A | £990/mo | Interactive quiz → style profile → personalized product feed |
| HF_05 | Order Intelligence Bot | A | £990/mo | Order tracking, returns, warranty claims via chat |
| HF_06 | Trade Account Portal | B | £1,490/mo | B2B ordering, bulk pricing, project management for trade customers |
| HF_07 | Visual Search Engine | A | £2,990/mo | Upload photo → find matching products (image similarity) |
| HF_08 | Returns & Warranty Handler | A | £990/mo | Automated returns processing, warranty claim management |

---

# B2B SUITE 5: MORTGAGE & FINANCE (7 Apps)

**Pricing range:** £790-1,990/mo

| App | Name | Type | Price | Key Features |
|-----|------|------|-------|-------------|
| MF_01 | Mortgage Qualifier Bot | A | £990/mo | Chat-based pre-qualification: income, debts, deposit → eligible products |
| MF_02 | Rate Intelligence Dashboard | B | £1,490/mo | Live rate tracking, market comparison, alert on rate changes |
| MF_03 | Application Tracker | A+B | £790/mo | Client tracks application status, broker manages pipeline |
| MF_04 | Affordability Calculator Pro | A | £490/mo | Advanced affordability with stress testing, scenario modelling |
| MF_05 | BTL Analysis System | B | £1,490/mo | Buy-to-let specific: yield, stress test, portfolio impact, tax |
| MF_06 | Remortgage Alert System | B | £990/mo | Track client mortgage expiries, auto-alert at optimal timing |
| MF_07 | Document Collection Bot | A | £790/mo | AI guides clients through document requirements, validates uploads |

---

# B2B SUITE 6: DEVELOPERS & CONTRACTORS (7 Apps)

**Pricing range:** £990-4,990/mo

| App | Name | Type | Price | Key Features |
|-----|------|------|-------|-------------|
| DC_01 | Development Feasibility Engine | B | £2,990/mo | Land + build + planning + sales → viability with scenario modelling |
| DC_02 | Planning Intelligence System | B | £1,990/mo | Planning application tracking, success rate analysis, policy monitoring |
| DC_03 | Quote Generation System | B | £990/mo | AI-assisted quote builder from scope → materials → labour → margins |
| DC_04 | Project Scheduling Platform | B | £1,490/mo | Gantt charts, contractor scheduling, milestone tracking, delay prediction |
| DC_05 | Client Enquiry Handler | A | £990/mo | Chat widget for builders: scope discussion, lead capture, quote requests |
| DC_06 | Invoice & Payment System | B | £990/mo | Generate invoices, track payments, stage billing, late payment reminders |
| DC_07 | Portfolio Showcase System | A | £990/mo | Interactive project gallery with before/after, testimonials, specs |

---

# B2C CONSUMER APPS (20+ Apps)

These run on the PCL platform (not white-label). Free basic versions drive engagement; premium features drive subscriptions.

---

## SEGMENT 1: HOME BUYERS (4 Apps)

| App | Name | Free Features | Premium Features |
|-----|------|--------------|-----------------|
| BC_01 | Home Search Assistant | Basic search, 3 alerts | AI-powered recommendations, unlimited alerts, "People Like You" |
| BC_02 | Affordability & Budget Planner | Basic calculator | Full stress test, scenario modelling, hidden costs breakdown |
| BC_03 | Area Explorer | Borough-level data | Neighbourhood detail, community reviews, crime/school/transport layers |
| BC_04 | My Home Purchase Tracker | Basic timeline | Full milestone tracker, document checklist, chain status, professional matching |

---

## SEGMENT 2: HOME SELLERS (4 Apps)

| App | Name | Free Features | Premium Features |
|-----|------|--------------|-----------------|
| BC_05 | Instant Home Valuation | Postcode estimate | Full comparable analysis, price trend, optimal timing |
| BC_06 | Agent Comparison Tool | Top 3 agents | Full comparison: fees, performance data, reviews, specialities |
| BC_07 | My Sale Tracker | Basic timeline | Full pipeline, chain status, communication log, milestone reminders |
| BC_08 | Home Staging Advisor | Basic tips | AI room-by-room recommendations from photos, cost estimates |

---

## SEGMENT 3: RENTERS (3 Apps)

| App | Name | Free Features | Premium Features |
|-----|------|--------------|-----------------|
| BC_09 | Rental Search Assistant | Basic search | AI matching, area scoring, commute calculator, rent negotiation tips |
| BC_10 | Tenant Toolkit | Basic guides | Document templates, deposit protection check, rights guide, dispute helper |
| BC_11 | Rental Dispute Helper | Basic info | AI-guided dispute process, template letters, ombudsman info |

---

## SEGMENT 4: LANDLORDS (3 Apps)

| App | Name | Free Features | Premium Features |
|-----|------|--------------|-----------------|
| BC_12 | Should I Let My Property? | Basic yield calc | Full analysis: income projection, costs, tax, regulations, risk score |
| BC_13 | Landlord Starter Kit | Basic guides | Step-by-step setup, compliance checklist, template documents |
| BC_14 | DIY Landlord Dashboard | Basic tracking | Full portfolio: income, expenses, compliance calendar, maintenance, tax reports |

---

## SEGMENT 5: ASPIRING INVESTORS (2 Apps)

| App | Name | Free Features | Premium Features |
|-----|------|--------------|-----------------|
| BC_15 | Property Investment Academy | Intro content | Full course library, deal analysis walkthroughs, strategy guides |
| BC_16 | First Investment Finder | Basic search | AI-matched deals, ROI calculations, risk assessment, finance options |

---

## SEGMENT 6: HOME IMPROVERS (4 Apps)

| App | Name | Free Features | Premium Features |
|-----|------|--------------|-----------------|
| BC_17 | Can I Build It? | Basic PD check | Full planning feasibility, local precedent analysis, success probability |
| BC_18 | Renovation Cost Calculator | Basic estimates | Detailed breakdown by trade, material options, contingency planning |
| BC_19 | Find a Contractor | Basic directory | AI-matched, verified, rated, quote comparison, project management |
| BC_20 | My Renovation Tracker | Basic checklist | Full project management: budget, timeline, contractor comms, document storage |

---

## B2B ↔ B2C APP CONNECTIONS (The Flywheel)

The same core engine powers both sides — creating network effects:

| B2B App (Pro Pays) | B2C App (Consumer Uses) | Data Created |
|--------------------|------------------------|-------------|
| AI Property Concierge (EA_01) | Home Search Assistant (BC_01) | Intent signals, preferences |
| Lead Intelligence (EA_04) | Property Journey Planner (BC_04) | Readiness scores |
| Market Report Generator (EA_05) | Instant Home Valuation (BC_05) | Market context |
| Vendor Management (EA_06) | My Sale Tracker (BC_07) | Transaction flow |
| Chain Tracker (EA_09) | My Chain Status (BC_04) | Chain intelligence |
| Viewing Scheduler (EA_03) | Book Viewings (BC_01) | Demand data |
| Tenant Acquisition Bot (LA_01) | Rental Search Assistant (BC_09) | Rental demand |
| Compliance Command (LA_03) | Landlord Compliance Checker (BC_14) | Compliance intelligence |
| Mortgage Qualifier Bot (MF_01) | Can I Get a Mortgage? (BC_02) | Finance readiness |
| Dev Feasibility Engine (DC_01) | Can I Build It? (BC_17) | Planning intelligence |

**Every B2C interaction generates data that makes B2B tools more valuable. Every B2B client serving consumers better drives more consumers to the platform.**

---

## BUILD PRIORITY

### Phase 1 (Months 1-2): 4 Core Apps
1. **EA_01: AI Property Concierge** — immediate revenue, proves concept
2. **LA_03: Compliance Command Center** — pain-point driven, high retention
3. **MF_01: Mortgage Qualifier Bot** — high demand, simple build
4. **PI_01: Deal Analyzer Pro** — investor market, premium pricing

### Phase 2 (Months 3-4): 8 More Apps
- EA_02 (Listing Engine), EA_05 (Market Reports), EA_03 (Viewing Scheduler)
- LA_01 (Tenant Acquisition), LA_04 (Maintenance Dispatch)
- BC_01 (Home Search Assistant), BC_05 (Instant Valuation), BC_02 (Affordability)

### Phase 3 (Months 5-6): Full 72+ Apps
- Complete all suites
- B2C consumer apps on platform
- Cross-app intelligence features

### Revenue Trajectory

| Milestone | Apps Live | Avg Revenue/App | MRR |
|-----------|----------|----------------|-----|
| Month 2 | 4 | £1,500 | £6K |
| Month 4 | 12 | £1,500 | £18K |
| Month 6 | 30 | £1,500 | £45K |
| Month 12 | 72+ | £1,500 | £150K+ |

Year 1 total: **£1.8M app revenue + £250K setup fees = £2.05M**

---

## SHARED DATABASE SCHEMA (App Layer)

```sql
-- App instances (one per client per app)
CREATE TABLE app_instances (
  id BIGSERIAL PRIMARY KEY,
  client_id BIGINT REFERENCES users(id),
  app_type TEXT NOT NULL,  -- EA_01, LA_03, etc.
  config JSONB NOT NULL DEFAULT '{}',  -- branding, tone, knowledge base, rules
  status TEXT DEFAULT 'active',
  created_at TIMESTAMPTZ DEFAULT now()
);

-- Conversations (all chat-based apps)
CREATE TABLE app_conversations (
  id BIGSERIAL PRIMARY KEY,
  instance_id BIGINT REFERENCES app_instances(id),
  visitor_id TEXT,  -- anonymous or user_id
  messages JSONB NOT NULL DEFAULT '[]',
  lead_score INT,
  status TEXT DEFAULT 'active',
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

-- Captured leads (from any app)
CREATE TABLE app_leads (
  id BIGSERIAL PRIMARY KEY,
  instance_id BIGINT REFERENCES app_instances(id),
  conversation_id BIGINT REFERENCES app_conversations(id),
  name TEXT,
  email TEXT,
  phone TEXT,
  preferences JSONB,
  score INT,
  status TEXT DEFAULT 'new',
  exported_to_crm BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- App analytics (daily aggregates)
CREATE TABLE app_analytics (
  id BIGSERIAL PRIMARY KEY,
  instance_id BIGINT REFERENCES app_instances(id),
  date DATE NOT NULL,
  conversations INT DEFAULT 0,
  leads_captured INT DEFAULT 0,
  viewings_booked INT DEFAULT 0,
  reports_generated INT DEFAULT 0,
  api_calls INT DEFAULT 0
);

-- Knowledge base per instance
CREATE TABLE app_knowledge (
  id BIGSERIAL PRIMARY KEY,
  instance_id BIGINT REFERENCES app_instances(id),
  type TEXT,  -- listing, faq, company_info, area_data
  content TEXT NOT NULL,
  embedding vector(1536),  -- pgvector for RAG
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_app_instances_client ON app_instances(client_id);
CREATE INDEX idx_app_conversations_instance ON app_conversations(instance_id);
CREATE INDEX idx_app_leads_instance ON app_leads(instance_id);
CREATE INDEX idx_app_analytics_instance ON app_analytics(instance_id, date);
CREATE INDEX idx_app_knowledge_embedding ON app_knowledge USING ivfflat (embedding vector_cosine_ops);
```

---

*72+ apps, 6 B2B suites, 6 B2C segments, shared engine, multi-tenant deployment. Build 4 first, prove revenue, scale to full suite.*
