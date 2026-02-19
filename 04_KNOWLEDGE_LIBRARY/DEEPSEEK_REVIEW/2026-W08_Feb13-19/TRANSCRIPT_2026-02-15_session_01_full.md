# SESSION LOG — 2026-02-15 Session 01 (Full Transcript Context)
> Duration: Full day session | Priority pivot to LeadEngine Platform

---

## SESSION TRIGGER
User saw RB2B (website visitor identification tool) promoted on YouTube. Asked to research it. From that research, conceived a far more comprehensive product — LeadEngine.

---

## PART 1: RB2B RESEARCH

### What RB2B Does
- Website visitor identification platform ($7M ARR, founded by Adam Robinson)
- Tracking pixel + proprietary publisher network + Demandbase reverse-IP
- Person-level ID (US only): name, LinkedIn, email, job title
- Company-level ID (global): company name, domain, industry, size
- Features: Hot Pages, Hot Leads, Intent Scoring, CRM sync, 50+ integrations
- Pricing: Free → $79 → $149 → $199+/mo
- Self-serve API: IP→Hashed Email (1 credit), Company Domain (1 credit), LinkedIn profiles (2-4 credits)
- API credits from $0.09 to $0.0092 each at enterprise volume
- SOC2 Type II certified, GDPR compliant (geofenced to US for person-level)

### Why User Rejected Pure RB2B Clone
> "I can't see the value in this without the person involved. It's too generic for whole company, particularly for B2C companies like estate agents that get inquiries from individuals."

Key insight: Company-level identification alone isn't enough for B2C businesses like estate agents who need to capture individual buyer details.

---

## PART 2: LEADENGINE PRODUCT CONCEPT

### User's Vision (Direct Quotes)
> "I want to build an app for ecom or estate agents that uses AI based on their knowledge base and brand to act like a concierge or onboarder that personalizes their journey"

> "My whole goal is to figure out the problems or leaks in their marketing and sales, particularly when people click on their site and create a way that automates getting that client's details then shows them whatever they're looking for, answers any questions, gives them value"

> "It has to be more than just chatbots, more than automated lead capture, more than AI wiki bots, and more than just capturing the business details alone — a complete package I can build, and have 90% done so all that remains is to brand it and deploy in their own container"

### 6 Core Modules Defined
1. **AI Concierge** — RAG-powered AI that knows their business, acts like their best salesperson. Context-aware (knows what page visitor is on). Brand-matched tone. NOT a chatbot.
2. **Visitor Intelligence** — Real-time live visitor tracking, IP-to-company identification, behavioural tracking, return visitor recognition, session timeline.
3. **Lead Capture & Scoring** — Progressive detail capture through natural value exchange. Name → email → phone → requirements. Lead scoring by behaviour + demographics.
4. **Lead Routing** — Instant push to right rep (geography, product type, round-robin). Full context attached. Slack/SMS/email/CRM. SLA tracking.
5. **Funnel Analytics & Leak Detection** — Visual funnel with drop-off %. Page performance with leak scores. Traffic source ROI. Content gap analysis. Weekly automated reports.
6. **Automation & Sequences** — Email/SMS follow-up sequences. Trigger-based automation. Personalised templates. Re-engagement for return visitors.

### Commitment
> "I'm all in on this. We have the landing pages and the brain. I'm 100% focused on this. We have a week to build it. I am charging 5k a month for this, making it available only to a limited number. I'm going to create a webinar and do a limited time launch."

> "Fuck tinkering endlessly in the build stage"

---

## PART 3: COMPLETE BUILD SPEC CREATED

### Screen Count
- 42 app screens (7 concierge + 6 intelligence + 6 capture + 5 routing + 6 analytics + 5 automation + 7 shared)
- 18 marketing/sales screens (10 website + 4 webinar + 4 sales assets)
- 10 LinkedIn posts + 10 short-form videos + 4 email sequences + 10 graphics
- **Total: 94 deliverables**

### Tech Stack
- Next.js + React frontend (using existing UI kits)
- FastAPI or Next.js API routes
- PostgreSQL + Redis + ChromaDB
- Claude API (concierge LLM)
- IPinfo.io (IP-to-company, $99/mo)
- Apollo.io (contact enrichment)
- Resend (email) + Twilio (SMS)
- Docker Compose per-client deployment

### 7-Day Build Sprint
- Day 1-2: Foundation + AI concierge engine
- Day 3-4: Visitor intelligence + lead capture + scoring
- Day 5: Routing + analytics
- Day 6: Automation + Docker packaging
- Day 7: Marketing site + launch prep

### Revenue Targets
- £5,000/month per client
- 5 clients = £25,000/month
- 10 clients = £50,000/month

---

## PART 4: DESIGN WORKBENCH & DAM

### Need
User needs to mock up all 94 screens efficiently using the 38 UI kits already in PostgreSQL. Browsing 12,000+ thumbnails manually is too slow.

### Solution
- Fabric.js canvas + Figma API renderer + component browser from PostgreSQL
- Simple DAM (upload, browse, search, serve images/videos)
- AI copy generation (Claude fills in text for each screen)
- Export as PNG mockup + JSON spec

### ImageKit Analysis
- Image/video CDN + transformation API + DAM
- $89-349/mo
- Decision: Build own simple DAM instead, use CDN later if needed

### Kit-to-Screen Mapping
All 42 app screens + 18 marketing screens mapped to primary/secondary kits from the 38 target kits. Saved in DESIGN_WORKBENCH_SPEC.md.

---

## PART 5: VIDEO PRODUCTION

### AE/DaVinci Templates vs AI Analysis
- User originally planned to download After Effects/DaVinci templates and decompose them
- Considered using YouTube URLs → Google AI Studio → effect library → Remotion
- Final decision: Skip both. Claude + Remotion can generate everything from descriptions.

### Remotion Workflow
1. User provides: brand assets (logo, icons, colours, fonts) + UI screenshots
2. User writes storyboard using motion lexicon terms
3. Claude writes Remotion React code
4. `npx remotion render` → MP4 output
5. No recording needed — pixel-perfect, repeatable, any resolution

### Motion Lexicon Created
171 terms across 11 categories:
- Entry animations (23), Exit animations (11), Transitions (16)
- Text animations (17), Cursor & interaction (14), Layout & component (22)
- Background & ambient (17), Timing & easing (19), Camera & framing (11)
- Mockup & device (10), Brand & style (11)

Essential 30 terms cover 90% of needs.

### Screen Recording Tools (For Quick Content)
- FocuSee ($70, Windows) — auto-zoom on clicks, smooth cursor, polished output
- Rapidemo ($59, Windows) — similar
- Screen Studio ($89, Mac only) — gold standard but Mac only

---

## PART 6: DEPLOYMENT ARCHITECTURE

### Two Models
1. **Hosted (£5,000/mo)** — Multi-tenant SaaS. Client pastes 1 JS snippet. Dashboard at app.leadengine.io. You manage everything.
2. **Dedicated Container (£7,500/mo)** — Docker Compose per client. Custom domain. Full data isolation. One deployment script, 30 minutes to live.

### JS Snippet
- One `<script>` tag in client's `<head>`
- Loads tracking pixel + concierge widget
- Widget runs in Shadow DOM (no CSS conflicts)
- Branded as THEIR company (logo, colours, greeting)
- ~30KB gzipped, async, doesn't block page

### Multi-Branch Support
- Same container handles hundreds of branches
- Branch parameter in pixel: `le('init', 'CLIENT_ID', { branch: 'brixton' })`
- Dashboard filters by branch
- Lead routing per branch
- Per-branch knowledge base and concierge personality
- Google Tag Manager deployment for chains (one push → all branches live)

### Pricing Tiers
- Hosted: £5,000/mo
- Up to 10 branches: £7,500/mo
- Up to 50 branches: £12,000/mo
- Unlimited branches: £20,000/mo
- Dedicated container: +£2,500/mo
- Self-hosted: £10,000 setup + £2,000/mo

### Competitor Analysis
- Nobody offers per-client container deployment with full stack (AI concierge + visitor ID + lead capture + routing + funnel analytics)
- Chatwoot closest (open source Docker) but just chat
- Intercom, Drift, RB2B all SaaS-only

---

## PART 7: KNOWLEDGE BASE & AI MODEL & UPDATES

### Knowledge Base Ingestion (5 methods)
1. **Website scrape** — Paste URL, system crawls, auto-refresh daily
2. **File upload** — Drag-drop CSV/PDF/Word, auto-vectorised
3. **Google Sheets sync** — Paste share link, hourly refresh
4. **CRM integration** — Reapit, Alto, Jupix, Expert Agent APIs
5. **API webhook** — Real-time: new listing → knowledge base updated instantly

### AI Model Strategy
- Default: "LeadEngine AI" (Claude under the hood)
- Client never sees API keys or model names
- LLM cost: ~£70-230/mo per client, baked into £5k price
- Enterprise option: bring your own API key (hidden in advanced settings)

### Update Delivery
- Hosted: Standard deploy, all clients updated instantly
- Container: Watchtower auto-pulls nightly, zero client intervention
- Database migrations auto-run on startup, numbered, idempotent
- Feature flags control gradual rollout by plan tier
- Changelog notification in dashboard for new features

---

## PART 8: BOOK & CONTENT STRATEGY (End of Session)

### Book Concept
- Working title: TBD — AI in property / proptech transformation
- Target audience: Estate agency owners, property CEOs
- Founder story: 16 years of learning, trying to compete with Houzz (billions in funding) as a solo operator without VC
- Arc: Built Enterprise OS because AI changed everything, Property Connect as AI-native company
- Structure ideas:
  - How proptech and AI will change how people buy property
  - How companies can serve those trends (tied to LeadEngine apps)
  - How to improve marketing and reach (tied to content production platform)
  - How to improve internal operations (tied to Enterprise OS)
  - First principles of AI adoption for property businesses
  - Informative, NOT a blatant sales pitch
- Turn into: Email sequences, LinkedIn content, social posts, webinar material

### Content Strategy Need
- Book → chapter summaries → LinkedIn posts → email sequences
- Webinar draws from book chapters
- Blog posts are excerpts
- All lead into LeadEngine as the solution

---

## FILES CREATED THIS SESSION

| File | Location |
|------|----------|
| COMPLETE_BUILD_SPEC.md | 07_BUILD_FACTORY/PRJ_LeadEngine_Platform/02_Requirements/ |
| DESIGN_WORKBENCH_SPEC.md | 07_BUILD_FACTORY/PRJ_LeadEngine_Platform/02_Requirements/ |
| VIDEO_PRODUCTION_SPEC.md | 07_BUILD_FACTORY/PRJ_LeadEngine_Platform/02_Requirements/ |
| DEPLOYMENT_SPEC.md | 07_BUILD_FACTORY/PRJ_LeadEngine_Platform/02_Requirements/ |
| BOILERPLATE_SELECTIONS.md | 07_BUILD_FACTORY/PRJ_UI_Component_Library/03_Design/ (updated) |
| Session summary | 02_COMMAND_DECK/ACTIVE_SESSIONS/2026-02/2026-02-15_session_01.md |
| This full log | 04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/2026-02/2026-02-15_session_01_full.md |
| MEMORY.md | .claude/projects/C--Users-under/memory/ (updated) |
| kit_roles.md | .claude/projects/C--Users-under/memory/ (created) |

---

## TOMORROW'S FOCUS (Sunday 2026-02-16)
1. Design Workbench MVP (Fabric.js canvas + Figma API + DAM)
2. Start rendering LeadEngine screen mockups
3. Content strategy and marketing plan
4. Book outline / chapter structure
5. PRD refinement with end-in-mind approach
