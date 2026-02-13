# PRD 1: Property Connect London (PCL)

**Version:** 2.0  
**Date:** 2025-11-04  
**Priority:** CRITICAL  

---

## Vision

Become the definitive intelligence and media hub for London property professionals and investors, combining data-driven insights with premium content across magazine, podcast, newsletter, Connected TV, and B2B data services.

---

## Target Audiences

### Primary (B2B)
- Estate agents & property managers
- Property investors (individual & institutional)
- Mortgage brokers & financial advisors
- Property developers
- Property lawyers & conveyancers
- Surveyors & inspectors
- Renovation contractors

### Secondary (B2C)
- First-time buyers
- Property sellers
- Landlords & tenants
- Property investors
- Renovation enthusiasts

---

## Platform Components

### 1. Newsletter (Launch Priority 1)
- **Daily:** Market updates, price movements, mortgage rates, featured properties
- **Weekly:** Deep dives, expert insights, data analysis
- **Format:** Email + web archive
- **Revenue:** Subscriptions (free/premium), sponsored sections

### 2. Digital Magazine (Launch Priority 2)
- **Monthly publication**
- **Content:** Market analysis, investment guides, expert interviews, area spotlights
- **Format:** Web, mobile app, PDF
- **Revenue:** Subscriptions, advertising, sponsored content

### 3. Podcast (Launch Priority 2)
- **Weekly episodes** (30-45 mins)
- **Content:** Expert interviews, market deep-dives, investment strategies
- **Distribution:** All major platforms + website
- **Revenue:** Sponsorships, ads, premium content

### 4. Connected TV Channel (Launch Priority 3)
- **Format:** Streaming video content
- **Shows:** 
  - Weekly market update
  - Luxury property tours
  - Expert panels
  - Renovation series
  - Investment masterclasses
- **Distribution:** Roku, Fire TV, Apple TV, web
- **Revenue:** Advertising, premium subscriptions

### 5. Data Services Platform (See PRD 8)
- B2B property intelligence
- API access
- Custom reports
- White-label solutions

---

## Content Strategy - 7 Property Pillars

### PILLAR 1: BUYING
**Newsletter Topics (125 identified):**
- First-time buyer guides
- Mortgage comparison & advice
- Area spotlights with pricing data
- Viewing tips & negotiation tactics
- Legal process walkthroughs
- Survey & inspection guides
- Moving & setup advice

**Vendor Directory:**
- Estate agents
- Mortgage brokers
- Conveyancing solicitors
- Surveyors
- Removals companies
- Insurance brokers

### PILLAR 2: SELLING
**Newsletter Topics (125 identified):**
- Home staging strategies
- Pricing optimization
- Estate agent selection
- Marketing tactics
- Seasonal selling patterns
- Negotiation strategies
- Quick sale methods

**Vendor Directory:**
- Estate agents (traditional/online/hybrid)
- Property photographers
- Home stagers
- Conveyancing solicitors
- Tax advisors

### PILLAR 3: RENTING
**Newsletter Topics (125 identified):**
- Rental market trends
- Tenant rights & responsibilities
- Property search strategies
- Contract negotiation
- Deposit protection
- Maintenance issues
- Area rental guides

**Vendor Directory:**
- Letting agents
- Tenant referencing services
- Guarantor services
- Renters insurance
- Furniture rental

### PILLAR 4: LETTING
**Newsletter Topics (125 identified):**
- Landlord compliance guides
- Tenant selection strategies
- Property management tips
- Yield optimization
- Legal requirements (gas safety, EPC, etc.)
- Tax efficiency
- Maintenance scheduling

**Vendor Directory:**
- Letting agents
- Property management companies
- Compliance specialists
- Landlord insurance
- Maintenance contractors

### PILLAR 5: INVESTING
**Newsletter Topics (125 identified):**
- Investment strategies (BTL, HMO, commercial)
- Market analysis & predictions
- ROI calculations
- Portfolio building
- Finance options
- Tax optimization
- Deal sourcing

**Vendor Directory:**
- Investment consultants
- BTL mortgage brokers
- Property sourcers
- Portfolio accountants
- Tax advisors

### PILLAR 6: RENOVATING
**Newsletter Topics (125 identified):**
- Renovation ROI analysis
- Design trends
- Cost estimation
- Project management
- Contractor selection
- Planning permission guides
- Before/after case studies

**Vendor Directory:**
- Architects
- Builders/contractors
- Interior designers
- Material suppliers
- Project managers

### PILLAR 7: BUILDING
**Newsletter Topics (125 identified):**
- Development opportunities
- Planning process guides
- Construction cost analysis
- Development finance
- Site acquisition
- Build methods
- New build market analysis

**Vendor Directory:**
- Architects
- Planning consultants
- Main contractors
- Development finance brokers
- Building materials suppliers

---

## Content Calendar Structure

### Daily Newsletter
- **Monday:** Market Week Ahead
- **Tuesday:** Deep Dive (pillar rotation)
- **Wednesday:** Pro Tips
- **Thursday:** Data Drop
- **Friday:** Weekend Read
- **Weekend:** Community features

### Weekly Recurring
- Luxury property tour (video)
- Area spotlight with data
- Expert Q&A
- Reader success story
- Investment opportunity analysis

### Monthly Features
- Market report (all 7 pillars)
- Borough deep-dive
- Professional of the month
- Investment strategy guide
- Renovation showcase

---

## Revenue Model

### Subscriptions (40% target)
- **Free:** Limited newsletter, basic content
- **Standard (£9.99/mo):** Full newsletter, magazine, podcast
- **Premium (£29.99/mo):** Everything + data access, advanced analytics
- **Professional (£99/mo):** B2B features, lead gen, vendor directory

### Advertising (30% target)
- Display ads (web/mobile)
- Newsletter sponsorships
- Podcast sponsorships
- TV commercials
- Native content

### Data Services (20% target)
- API access
- Custom reports
- Market intelligence
- White-label data

### Vendor Services (10% target)
- Directory listings
- Lead generation
- Featured profiles
- Quote requests

### Year 1 Targets
- **Revenue:** £250K
- **Subscribers:** 50,000 total
- **Premium conversions:** 5% (2,500)
- **Professional subscribers:** 500
- **Vendor partners:** 100

---

## Technical Architecture

### Frontend Stack
- **Web:** Next.js, React, Tailwind CSS
- **Mobile:** React Native
- **TV Apps:** Platform SDKs (Roku, Fire TV)
- **CMS:** Headless (Strapi or Sanity)

### Backend Stack
- **API:** Node.js/Express or Python/FastAPI
- **Database:** PostgreSQL (primary), Redis (cache)
- **Media Storage:** S3/Cloudflare R2
- **CDN:** Cloudflare
- **Search:** Elasticsearch

### Key Integrations
- **Email:** SendGrid
- **Payments:** Stripe
- **Analytics:** Mixpanel + Google Analytics
- **CRM:** HubSpot
- **Video:** YouTube API, Vimeo
- **Property Data:** Multiple providers (see PRD 8)

---

## Database Schema (Core Tables)

### Content Tables
- articles
- newsletters
- podcast_episodes
- tv_episodes
- videos
- authors

### User Tables
- users
- subscriptions
- preferences
- activity_logs

### Property Data Tables
- properties
- areas (boroughs, neighborhoods)
- price_data
- market_metrics
- transactions

### Vendor Tables
- vendors
- vendor_services
- reviews
- leads

### Keyword Research Tables
- keywords (15,000+ for London property)
- keyword_categories
- search_volumes
- content_mapping

---

## Content Production Requirements

### Newsletter
- **Daily:** 1 writer + 1 editor
- **Production time:** 2-3 hours/day
- **Tools:** Email platform, analytics, CMS

### Magazine
- **Monthly:** 1 editor + 3 writers + 1 designer
- **Production time:** 80 hours/month
- **Tools:** InDesign, Figma, CMS

### Podcast
- **Weekly:** 1 host + 1 producer + 1 editor
- **Production time:** 8 hours/episode
- **Tools:** Recording setup, editing software

### TV Content
- **Weekly:** 1 host + 1 videographer + 1 editor
- **Production time:** 16 hours/episode
- **Tools:** Video production setup, editing software

---

## Brand Identity

### Brand DNA
- **Authoritative:** Data-driven, expert-backed
- **Accessible:** Complex topics made simple
- **Premium:** High-quality production
- **Connected:** Community-focused
- **Forward-thinking:** Anticipating trends

### Visual Style
- Modern, professional design
- London-centric imagery
- Data visualization standards
- Consistent typography
- Brand colors: [TBD - see Branding Platform PRD]

### Voice & Tone
- Professional but approachable
- Confident and knowledgeable
- Educational, not condescending
- Market-focused and practical

---

## Go-to-Market Timeline

### Month 1-2: Foundation
- Launch website
- Begin daily newsletter
- Establish vendor partnerships
- Build initial subscriber base (5,000)
- Set up analytics

### Month 3-4: Content Expansion
- Launch podcast
- Expand newsletter features
- Introduce premium tier
- Grow to 15,000 subscribers

### Month 5-6: Magazine Launch
- Launch digital magazine
- Increase content production
- Add advertising partners
- Reach 25,000 subscribers

### Month 7-9: TV Launch
- Launch Connected TV channel
- Produce pilot shows
- Secure distribution deals
- Target 40,000 subscribers

### Month 10-12: Data Services
- Launch B2B data platform (see PRD 8)
- Introduce API access
- White-label partnerships
- Reach 50,000+ total users

---

## Key Metrics & KPIs

### Audience Metrics
- Total subscribers/users
- Monthly active users (MAU)
- Email open rate (target: 35%+)
- Click-through rate (target: 5%+)
- Free-to-paid conversion (target: 5%)
- Churn rate (target: <5% monthly)

### Engagement Metrics
- Average time on site
- Pages per session
- Podcast downloads/listens
- Video views/watch time
- Social media engagement

### Revenue Metrics
- MRR (Monthly Recurring Revenue)
- ARPU (Average Revenue Per User)
- CAC (Customer Acquisition Cost)
- LTV (Lifetime Value)
- LTV:CAC ratio (target: 3:1)

### Content Metrics
- Articles published/month
- Newsletter open rates
- Most popular topics
- Traffic sources
- SEO rankings

---

## Dependencies & Integration Points

### Links to Other Platforms
- **Copy Platform (PRD 6):** All content creation, frameworks, swipes
- **Branding Platform (PRD 7):** Visual identity, brand guidelines
- **UI Library:** Component designs, page templates
- **Database/RAG:** Content storage, knowledge management
- **Agent OS:** Workflow orchestration, task management

### External Dependencies
- Property data providers (see PRD 8)
- Video production services
- Email delivery infrastructure
- Payment processing
- Cloud hosting

---

## Phase 1 Priorities (Months 1-3)

### Critical
1. Website development (core pages)
2. Newsletter infrastructure setup
3. Content creation workflow
4. Initial vendor partnerships (10-20)
5. Keyword research implementation (15,000+ keywords ready)
6. Database schema deployment
7. Payment/subscription system

### High
1. Brand identity finalization
2. UI component library
3. Content calendar (3 months ahead)
4. Social media presence
5. SEO foundation
6. Analytics setup
7. CRM integration

### Medium
1. Podcast production setup
2. Video content planning
3. Community features
4. Advanced analytics
5. Mobile app planning

---

## Success Criteria

### Month 3
- 5,000 subscribers
- Daily newsletter launched
- 20 vendor partners
- £5K MRR

### Month 6
- 15,000 subscribers
- Magazine + podcast live
- 50 vendor partners
- £25K MRR

### Month 12
- 50,000 subscribers
- All channels operational
- 100+ vendor partners
- £69K MRR
- Profitable

---

## Risk Mitigation

### Content Production Risks
- **Risk:** Can't maintain daily schedule
- **Mitigation:** Build content buffer, automate where possible, hire support

### Data Quality Risks
- **Risk:** Property data accuracy issues
- **Mitigation:** Multiple data sources, verification processes, user reporting

### Competition Risks
- **Risk:** Existing players dominate
- **Mitigation:** Unique multi-channel approach, superior data, community focus

### Revenue Risks
- **Risk:** Slow subscriber growth
- **Mitigation:** Strong SEO, content marketing, vendor partnerships, referral program

---

## Next Steps

1. Finalize brand identity (Branding Platform)
2. Complete UI design library
3. Set up keyword research infrastructure
4. Begin daily content production
5. Establish vendor partnerships
6. Launch MVP website + newsletter
7. Implement analytics/tracking

---

**Status:** Ready to begin Phase 1 execution
**Owner:** [Your Name]
**Last Updated:** 2025-11-04
