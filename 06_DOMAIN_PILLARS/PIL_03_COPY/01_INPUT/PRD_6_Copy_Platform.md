# PRD 6: Copy Platform

**Version:** 2.0  
**Date:** 2025-11-04  
**Priority:** HIGH  

---

## Vision

Create a comprehensive copywriting platform that combines frameworks, swipe files, AI-powered generation, and workflow management to enable businesses and agencies to produce high-converting copy at scale across all channels and formats.

---

## Target Audience

### Primary (B2B)
- Marketing agencies
- Freelance copywriters
- In-house marketing teams
- E-commerce businesses
- SaaS companies
- Professional services firms

### Secondary (B2C)
- Solopreneurs
- Content creators
- Small business owners
- Startup founders

---

## Core Platform Components

### 1. Copywriting Frameworks Library

**Strategic Frameworks:**
- **AIDA** (Attention, Interest, Desire, Action)
- **PAS** (Problem, Agitate, Solution)
- **PASTOR** (Problem, Amplify, Story, Testimony, Offer, Response)
- **BAB** (Before, After, Bridge)
- **4 Ps** (Picture, Promise, Prove, Push)
- **QUEST** (Qualify, Understand, Educate, Stimulate, Transition)
- **FAB** (Features, Advantages, Benefits)
- **ACCA** (Awareness, Comprehension, Conviction, Action)
- **The Slippery Slide**
- **Unique Mechanism**
- **Million Dollar Process**

**Copy Types by Framework:**
- **Sales Pages:** Long-form persuasion frameworks
- **Landing Pages:** Conversion-focused structures
- **Email Sequences:** Nurture and sales frameworks
- **Social Media:** Engagement and conversion formulas
- **Ads:** Short-form attention frameworks
- **VSLs:** Video sales letter structures
- **Webinars:** Educational selling frameworks

**Framework Details Include:**
- When to use this framework
- Step-by-step structure
- Example copy for each section
- Best practices and tips
- Common mistakes to avoid
- Industry-specific adaptations

### 2. Swipe File Library

**Comprehensive Collection:**
- **Sales Pages:** 500+ high-converting examples
- **Emails:** 1,000+ sequences and individual emails
- **Headlines:** 2,000+ proven headlines
- **Subject Lines:** 1,000+ high-open subject lines
- **CTAs:** 500+ action-driving calls-to-action
- **Social Posts:** 500+ engagement-driving posts
- **Ad Copy:** 500+ paid ad examples (Facebook, Google, etc.)
- **Product Descriptions:** 300+ e-commerce examples
- **VSL Scripts:** 100+ video sales scripts

**Swipe Organization:**
- By industry (SaaS, e-commerce, coaching, etc.)
- By format (email, landing page, ad, etc.)
- By objective (awareness, consideration, conversion)
- By emotion (urgency, curiosity, fear, desire, etc.)
- By technique (scarcity, social proof, guarantee, etc.)

**Swipe Features:**
- Search and filter
- Save to collections
- Add personal notes
- Rate and review
- Share with team
- Version comparison
- A/B test results (when available)

### 3. AI Copy Generator

**Generation Capabilities:**
- **Input Requirements:**
  - Target audience description
  - Product/service details
  - Unique value propositions
  - Framework selection
  - Tone and voice preferences
  - Length requirements

- **Generated Outputs:**
  - Full copy based on framework
  - Multiple variations
  - A/B test alternatives
  - Different emotional angles
  - Various lengths (short/medium/long)

- **AI Models:**
  - GPT-4 for long-form copy
  - Claude for nuanced, on-brand copy
  - Fine-tuned models for specific industries
  - Ensemble approach for best results

**Editing & Refinement:**
- In-app copy editor
- AI-powered suggestions
- Readability scoring
- Tone analysis
- Plagiarism checking
- Brand voice consistency check

### 4. Copy Research Tools

**Audience Research:**
- **Avatar Builder:**
  - Demographics
  - Psychographics
  - Pain points and desires
  - Objections and concerns
  - Language and terminology
  - Buying behaviors

- **Voice of Customer (VOC) Analysis:**
  - Review mining (Amazon, G2, etc.)
  - Survey data input
  - Social listening summaries
  - Customer interview transcripts
  - Support ticket analysis

**Competitor Analysis:**
- Competitor copy collection
- Messaging analysis
- Unique positioning identification
- Differentiation opportunities
- Pricing and offer structures

**Market Research:**
- Industry trends
- Keyword research integration
- Google Trends integration
- Social media trending topics
- Forum/community insights (Reddit, Quora)

### 5. Copy Asset Management

**Organized Storage:**
- **Projects:** Client/project-based organization
- **Templates:** Reusable copy templates
- **Snippets:** Commonly used phrases and sections
- **Brand Guidelines:** Voice, tone, messaging docs
- **Approved Copy:** Finalized, client-approved versions

**Version Control:**
- Track changes over time
- Revert to previous versions
- Compare versions side-by-side
- Approval workflows
- Comments and feedback

**Collaboration:**
- Team workspaces
- Assign copy tasks
- Review and approval process
- Real-time co-editing
- Comment threads
- @mention teammates

### 6. Copy Workflow Automation

**Process Templates:**
- **Client Onboarding:**
  - Discovery questionnaire
  - Avatar building worksheet
  - Competitor analysis
  - Brand voice extraction

- **Copy Production:**
  - Research phase checklist
  - First draft generation
  - Review and revision cycles
  - Client feedback collection
  - Final approval process

- **Launch & Optimization:**
  - A/B test setup
  - Performance tracking
  - Iteration based on data
  - Continuous improvement

**Task Management:**
- Project timelines
- Deadline tracking
- Automated reminders
- Status updates
- Workload distribution

### 7. Copy Analytics & Testing

**Performance Tracking:**
- **Email Campaigns:**
  - Open rates
  - Click-through rates
  - Conversion rates
  - Revenue attribution

- **Landing Pages:**
  - Traffic sources
  - Bounce rate
  - Conversion rate
  - Scroll depth
  - Heatmaps (integration with Hotjar, etc.)

- **Social Media:**
  - Engagement rates
  - Click-through rates
  - Share rates
  - Comment sentiment

- **Ads:**
  - CTR
  - Conversion rate
  - Cost per acquisition
  - ROAS

**A/B Testing:**
- Test creation interface
- Variation management
- Statistical significance calculation
- Winner declaration
- Learning documentation

**Copy Insights:**
- What works (successful patterns)
- What doesn't (failures and learnings)
- Best-performing frameworks
- Industry benchmarks
- Continuous learning

---

## Technical Architecture

### Platform Stack

**Frontend:**
- **Web App:** Next.js, React, Tailwind CSS
- **Editor:** TipTap or Draft.js (rich text)
- **Collaboration:** WebSockets (real-time editing)

**Backend:**
- **API:** Node.js (Express) or Python (FastAPI)
- **Database:** PostgreSQL (relational data)
- **Search:** Elasticsearch (swipe file search)
- **Queue:** Redis + Bull (AI generation jobs)

**AI/ML:**
- **LLMs:** OpenAI GPT-4, Anthropic Claude
- **Fine-tuning:** Custom models for specific copy types
- **Analysis:** NLP models for tone, readability

**Integrations:**
- **Email Platforms:** Mailchimp, SendGrid, HubSpot
- **CMS:** WordPress, Webflow, Shopify
- **Analytics:** Google Analytics, Mixpanel
- **Design Tools:** Figma, Canva (export copy)
- **Project Management:** Asana, ClickUp, Monday

---

## Database Schema

```sql
-- Organizations & Users
organizations
users
teams
team_members

-- Copy Assets
projects
copy_documents (versions tracked)
copy_snippets (reusable elements)
templates
swipe_files

-- Frameworks
frameworks (framework library)
framework_sections (parts of framework)
framework_examples

-- Research
avatars (target audience personas)
voc_data (voice of customer research)
competitor_analyses

-- Workflow
workflows (process templates)
tasks
task_assignments
approvals

-- AI Generation
generation_jobs (queued AI tasks)
generation_results
generation_feedback

-- Analytics
performance_data
ab_tests
test_variations
test_results

-- Integrations
integration_connections (linked accounts)
integration_sync_logs
```

---

## Key Features Detail

### AI Copy Generator Deep-Dive

**Input Form:**
```
1. What are you creating?
   - Sales page, email, ad, social post, etc.

2. Who is your target audience?
   - Demographics, pain points, desires

3. What are you selling?
   - Product/service description, features, benefits

4. What's your unique mechanism/angle?
   - What makes you different?

5. Choose a framework:
   - AIDA, PAS, PASTOR, etc.

6. Desired tone:
   - Professional, casual, urgent, empathetic, etc.

7. Length:
   - Short (100-300 words)
   - Medium (300-800 words)
   - Long (800-2000+ words)

8. Additional requirements:
   - Specific phrases to include/avoid
   - Brand guidelines
   - Competitor references
```

**Generation Process:**
1. User fills out form
2. System constructs comprehensive prompt
3. AI generates 3 variations
4. User selects favorite or requests refinement
5. User edits in rich text editor
6. Save to project

**Refinement Options:**
- "Make it more urgent"
- "Add more social proof"
- "Simplify language"
- "Add a guarantee"
- "Include testimonial placeholder"

### Swipe File Power Features

**Advanced Search:**
```
Filters:
- Industry: SaaS, E-commerce, Coaching, Finance, etc.
- Format: Email, Landing Page, Ad, Social, etc.
- Framework: AIDA, PAS, BAB, etc.
- Technique: Scarcity, Urgency, Social Proof, etc.
- Performance: High-converting, Award-winning, etc.
- Company: Search by brand name
- Keywords: Full-text search
```

**Learning from Swipes:**
- Annotated swipes (why it works)
- Framework breakdown
- Emotional trigger analysis
- Conversion elements highlighted
- Before/after comparisons (A/B test winners)

**Personal Swipe Collection:**
- Save favorites
- Organize into folders
- Add personal notes
- Tag for easy retrieval
- Share with team

### Copywriting Frameworks in Action

**Example: AIDA Framework**

**Structure:**
1. **Attention:** Headline and opening hook
2. **Interest:** Expand on promise, relate to pain
3. **Desire:** Paint picture of transformation, build credibility
4. **Action:** Clear CTA, remove friction

**Platform Features:**
- Step-by-step wizard
- Example copy for each section
- AI generation for each section
- Mix-and-match different examples
- Export to various formats

---

## User Experience Flow

### Onboarding
1. Create account
2. Select role (agency, freelancer, in-house, etc.)
3. Industry selection
4. Quick tour of features
5. Create first project
6. Generate first copy piece

### Creating Copy (Typical Flow)

**Research Phase:**
1. Create project
2. Build avatar (or use existing)
3. Conduct competitor analysis
4. Extract VOC data (if available)

**Generation Phase:**
1. Select copy type
2. Choose framework
3. Fill out generation form
4. Review 3 AI-generated variations
5. Select and refine

**Editing Phase:**
1. Edit in rich text editor
2. Get AI suggestions
3. Check readability and tone
4. Review against brand guidelines
5. Share with team for feedback

**Finalization Phase:**
1. Incorporate feedback
2. Get final approval
3. Export in desired format
4. Integrate with platform (email, CMS, etc.)
5. Track performance

---

## Pricing Model

### Subscription Tiers

**Solo (£29/mo):**
- 1 user
- 50 AI generations/month
- Access to frameworks
- 500 swipe files
- Basic templates
- Community support

**Team (£99/mo):**
- Up to 5 users
- 200 AI generations/month
- Full swipe library (10,000+)
- All frameworks
- Collaboration features
- Version control
- Email support
- Brand voice analysis

**Agency (£299/mo):**
- Up to 20 users
- 1,000 AI generations/month
- Everything in Team, plus:
- Client workspaces
- White-label option
- Advanced analytics
- A/B testing tools
- API access
- Priority support

**Enterprise (Custom):**
- Unlimited users
- Unlimited AI generations
- Custom integrations
- Dedicated account manager
- On-prem option
- SLA guarantee
- Custom training

### Add-Ons
- Additional AI generations (£10/100)
- Premium swipe files (curated collections - £49)
- One-on-one copywriting coaching (£200/hour)
- Done-for-you copy reviews (£500+)

---

## Go-to-Market Strategy

### Phase 1: MVP Launch (Months 1-3)
- Core frameworks (10)
- AI generation (basic)
- Swipe library (500 examples)
- Copy editor
- Beta with 50 users
- Target: Product-market fit validation

### Phase 2: Growth (Months 4-6)
- Expand frameworks to 30
- Swipe library to 5,000
- Add collaboration features
- Launch paid tiers
- Content marketing
- Target: 500 paying users

### Phase 3: Scale (Months 7-12)
- Full swipe library (10,000+)
- Advanced AI features
- Analytics and A/B testing
- Integrations (Mailchimp, HubSpot, etc.)
- Agency outreach
- Target: 2,000 paying users, £100K MRR

---

## Key Metrics

### Product Metrics
- AI generations per user
- Swipe file views/saves
- Time spent in editor
- Projects created
- Copy pieces produced
- Feature adoption rates

### Business Metrics
- MRR/ARR
- User count by tier
- Churn rate
- LTV:CAC ratio
- Expansion revenue (upgrades)

### User Success Metrics
- Copy conversion rates (when tracked)
- User-reported satisfaction
- Copy pieces published (vs generated)
- Collaboration activity

---

## Dependencies

### Internal
- **Branding Platform:** Visual identity
- **UI Library:** Component designs
- **Database:** PostgreSQL setup
- **Agent OS:** Workflow orchestration
- **Coherence Platform:** Knowledge management

### External
- LLM API access (OpenAI, Anthropic)
- Cloud infrastructure
- Payment processing
- Email sending (for notifications)
- Integration APIs (Mailchimp, etc.)

---

## Success Criteria

### Month 3
- MVP launched
- 10 frameworks live
- 500 swipe files
- AI generation working
- 50 beta users providing feedback

### Month 6
- 500 paying users
- £25K MRR
- 30 frameworks
- 5,000 swipe files
- Collaboration features live

### Month 12
- 2,000 paying users
- £100K MRR
- 50+ frameworks
- 10,000 swipe files
- 90% user satisfaction
- Profitable

---

## Competitive Analysis

### vs Copy.ai / Jasper
- **Advantage:** Framework-driven (structure + generation), swipe library, workflow management
- **Disadvantage:** Later to market (mitigated by superior features)

### vs Swipe File Services
- **Advantage:** AI generation, not just inspiration
- **Disadvantage:** Smaller swipe collection initially (grows over time)

### vs Freelance Copywriters
- **Advantage:** Faster, more affordable, consistent quality, 24/7 availability
- **Disadvantage:** Less human creativity (mitigated by AI + human editing hybrid)

---

## Risk Mitigation

### AI Quality Risks
- **Risk:** Generated copy is generic or poor quality
- **Mitigation:** Fine-tuned models, framework-driven prompts, human editing expected

### Competition Risks
- **Risk:** Larger players (Jasper, Copy.ai) add similar features
- **Mitigation:** Focus on frameworks + swipes + workflow (comprehensive platform)

### User Retention Risks
- **Risk:** Users churn after initial usage
- **Mitigation:** Continuous value delivery (new swipes, frameworks, features), community engagement

---

## Next Steps

1. Finalize MVP feature set
2. Curate initial 500 swipe files
3. Document first 10 frameworks
4. Design AI generation prompts
5. Build copy editor interface
6. Recruit beta users (50)
7. Launch and iterate

---

**Status:** Ready for MVP development
**Owner:** [Your Name]
**Last Updated:** 2025-11-04
