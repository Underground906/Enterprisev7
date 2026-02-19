# SESSION SUMMARY — 2026-02-15 Session 01
> Full spec: `07_BUILD_FACTORY/PRJ_LeadEngine_Platform/02_Requirements/COMPLETE_BUILD_SPEC.md`

## MAJOR PIVOT — New Priority Build

**LeadEngine Platform** — AI-powered conversion intelligence platform.
- Replaces all previous build priorities as #1 focus
- £5,000/month, limited availability, webinar launch
- Target: Estate agents + home goods stores
- Timeline: 1 week to build, 2 weeks to first client

## What Happened
1. Researched RB2B (website visitor identification tool) — full product/pricing/API teardown
2. User identified gap: company-level ID alone isn't enough for B2C (estate agents get individual inquiries)
3. Conceived full-funnel conversion intelligence platform: AI concierge + visitor intelligence + lead capture + routing + funnel analytics + automation
4. Built complete spec: 42 app screens, 18 marketing screens, social content plan, 7-day build sprint
5. Saved as PRJ_LeadEngine_Platform in Build Factory

## Key Decisions
- NOT using RB2B API (they'd see and cut out)
- Building independently: IPinfo.io for company ID, Apollo for enrichment, own AI concierge via RAG+LLM
- £5,000/month pricing, limited spots, webinar launch model
- Docker-containerised for per-client deployment
- Chroma design system for marketing site, Brainwave for app dashboard

## Outputs
- `07_BUILD_FACTORY/PRJ_LeadEngine_Platform/02_Requirements/COMPLETE_BUILD_SPEC.md`
- `04_KNOWLEDGE_LIBRARY/SESSION_ARCHIVE/2026-02/2026-02-15_session_01_full.md`

## Additional Outputs
- `02_Requirements/DESIGN_WORKBENCH_SPEC.md` — Fabric.js canvas + Figma API renderer + DAM spec
- `02_Requirements/VIDEO_PRODUCTION_SPEC.md` — 171-term motion lexicon + storyboard template + 10 videos needed
- `02_Requirements/DEPLOYMENT_SPEC.md` — Hosted vs Container deployment, Docker Compose, deploy script, pricing tiers, competitor analysis
- Includes kit-to-screen mapping for all 42 app screens + 18 marketing screens
- ImageKit.io analysed — building own DAM instead
- Remotion + Claude workflow confirmed for all video production
- RB2B, Chatwoot, Intercom, Drift competitor landscape mapped
- Knowledge base ingestion (5 methods: website scrape, file upload, Google Sheets sync, CRM API, webhook)
- AI model strategy (Claude under the hood, branded "LeadEngine AI", ~£70-230/mo LLM cost per client)
- Update delivery via Watchtower (nightly Docker pull), numbered idempotent migrations
- Multi-branch support (same container, branch param in pixel, per-branch knowledge base)
- Book concept discussed: AI in property / proptech transformation, 16-year founder story, not a sales pitch — turn into email sequences, LinkedIn content, webinar material

## Tomorrow (Sunday): DESIGN WORKBENCH
- AM: Fabric.js canvas + component browser from PostgreSQL
- PM: Simple DAM (upload, browse, search) + AI copy integration
- Evening: Start rendering LeadEngine screen mockups

## Monday: BUILD STARTS
- Day 1-2: Foundation + AI concierge engine
- Day 3-4: Visitor intelligence + lead capture
- Day 5: Routing + analytics
- Day 6: Automation + Docker packaging
- Day 7: Marketing site + launch prep
