# Web Design & Development Factory System v1.0
## Enterprise_OS Integration Module | Production-Ready Workflow Documentation

---

## Table of Contents

1. [System Overview](#1-system-overview)
2. [Tool Stack Reference](#2-tool-stack-reference)
3. [AntiGravity Core Setup](#3-antigravity-core-setup)
4. [OpenCode Integration (150+ Models)](#4-opencode-integration)
5. [Google AI Studio Pipeline](#5-google-ai-studio-pipeline)
6. [Motion Background Workflow (Whisk → ezGIF)](#6-motion-background-workflow)
7. [UI Component Libraries & Sniping](#7-ui-component-libraries)
8. [Backend Integration (Supabase)](#8-backend-integration)
9. [GitHub to Vercel Deployment](#9-github-to-vercel-deployment)
10. [Visual RAG Thread Integration](#10-visual-rag-thread-integration)
11. [Production Checklists](#11-production-checklists)
12. [Prompt Templates](#12-prompt-templates)

---

## 1. System Overview

### 1.1 Philosophy

This system operates on three core principles:

| Principle | Description |
|-----------|-------------|
| **Direct-to-Client Protocol** | Generate production-quality output in single shots, eliminating revision loops |
| **Design Operating System** | Combine AI Studio's visual striking output with AntiGravity's maintainable structure |
| **Progressive Embodiment** | Build React shells → validate → deploy → evolve into full platforms |

### 1.2 System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        DESIGN PHASE                                  │
├─────────────────────────────────────────────────────────────────────┤
│  Google AI Studio  →  Gemini Image Gen  →  Whisk  →  Google Flow   │
│  (Initial Design)     (Product Images)    (Effects)  (Video Gen)   │
└─────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────┐
│                      DEVELOPMENT PHASE                               │
├─────────────────────────────────────────────────────────────────────┤
│  AntiGravity + OpenCode + Claude Code                                │
│  ├── UI/UX Pro Skill (optimization)                                  │
│  ├── Magic UI / 21st.dev (component sniping)                         │
│  ├── Supabase MCP (backend/auth)                                     │
│  └── Vercel MCP (deployment automation)                              │
└─────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────┐
│                      DEPLOYMENT PHASE                                │
├─────────────────────────────────────────────────────────────────────┤
│  AntiGravity Terminal  →  GitHub  →  Vercel  →  Custom Domain       │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.3 Key Design Philosophies Comparison

| AI Studio | AntiGravity |
|-----------|-------------|
| Visually striking, "wow factor" | Professional, maintainable |
| Kitchen-sink approach | Incremental improvements |
| Less scalable structure | Best practices, accessibility |
| Perfect for initial design | Perfect for production build |

**Strategy**: Use AI Studio for 80% visual design → Import to AntiGravity for structure/scalability/optimization

---

## 2. Tool Stack Reference

### 2.1 Primary Tools

| Tool | Purpose | Cost | URL |
|------|---------|------|-----|
| Google AntiGravity | AI coding IDE | Free tier available | Built into Google ecosystem |
| Google AI Studio | Visual design generation | Free | aistudio.google.com |
| Google Whisk | Image effects/manipulation | Free | labs.google/whisk |
| Google Flow | Video generation (frame-to-video) | Free | labs.google/flow |
| Gemini | Image generation | Free | gemini.google.com |
| OpenCode | Multi-model AI agent | Free/Open Source | opencode.dev |
| Supabase | Backend/Database/Auth | Free tier | supabase.com |
| Vercel | Hosting/Deployment | Free hobby tier | vercel.com |
| GitHub | Code repository | Free | github.com |

### 2.2 UI Component Libraries

| Library | Specialty | MCP Available | URL |
|---------|-----------|---------------|-----|
| Magic UI | Animated components, buttons | Yes | magicui.design |
| 21st.dev | Copy-paste components | No | 21st.dev |
| CodePen | Community components | No | codepen.io |
| Dribbble | Design inspiration | No | dribbble.com |

### 2.3 Utility Tools

| Tool | Purpose | URL |
|------|---------|-----|
| ezGIF | Video to JPG frames conversion | ezgif.com |
| Firecrawl | Website scraping/research | firecrawl.dev |
| NanoBanana Pro | AI image generation | labs.google/flow |
| HTML Website Extractor | Extract website source | view-source tools |

---

## 3. AntiGravity Core Setup

### 3.1 Initial Configuration

**Access Agent Manager:**
```
Editor → Agent Manager (bottom left)
```

**Key Interface Areas:**
- **Playground**: Prompt conversations
- **Terminal**: Command execution, OpenCode access
- **Agent Manager**: Project management, MCP configuration
- **Preview Browser**: Live website testing

### 3.2 MCP Server Setup

**Access MCP Configuration:**
```
Additional Options → MCP Servers → Manage MCP Servers
```

**Essential MCP Servers to Install:**

1. **Supabase MCP**
   - Generate token: Supabase Dashboard → Settings → API → Generate new token
   - Paste access token in AntiGravity MCP config

2. **Vercel MCP**
   - Get API key from Vercel dashboard
   - Configuration format:
   ```json
   {
     "vercel": {
       "token": "INSERT_VERCEL_API_KEY"
     }
   }
   ```

3. **Firecrawl MCP**
   - Get API key from firecrawl.dev → API Keys
   - Format: `Bearer YOUR_API_KEY`

### 3.3 Installing Skills

**UI/UX Pro Skill Installation:**
```
Prompt: "Add this repo to this project as an AntiGravity skill: [SKILL_REPO_URL]"
```

**What the UI/UX Pro Skill Does:**
- 100+ design rules
- 57 UI styles
- SEO optimizations
- Conversion intelligence
- UX/UI frameworks
- Accessibility improvements
- 50+ automatic micro-optimizations

**Usage after installation:**
```
Prompt: "In accordance with this skill, audit and improve the website to align with the design principles outlined in the agents UI skills."
```

---

## 4. OpenCode Integration

### 4.1 Installation

**In AntiGravity Terminal:**
```bash
# Open terminal: Terminal → New Terminal
# Install OpenCode
npm install -g opencode
# OR paste the install command from opencode.dev
```

**Verify installation:**
```bash
opencode --version
```

### 4.2 Accessing OpenCode

```bash
# In terminal, type:
opencode

# View available models:
/models

# View all models (Control + A)
```

### 4.3 Model Access

**Free Models Available:**
- Big Pickle
- MiniAX MM2
- Gro Code Fast
- Plus 150+ others via OpenRouter

**Premium Models (via existing subscriptions):**
- GPT-4 (via ChatGPT Plus subscription)
- Claude models
- Gemini models

### 4.4 AntiGravity OAuth Integration (Gemini/Claude access)

**Setup:**
```
Prompt: "Install the opencode antigravity auth plugin with the antigravity model definitions to my global config using this URL: [AUTH_URL]"
```

**Process:**
1. AntiGravity opens Google account selection
2. Select account, grant permissions
3. Return to AntiGravity, accept all
4. Verify: In new terminal, type `opencode`, then `/models`
5. Should see: Claude Opus 4.5, Sonnet 4.5, all Gemini models

### 4.5 Mode Switching

```
# Switch between Plan and Build modes:
Command + Shift
```

### 4.6 Strategic Model Usage

| Task Type | Recommended Model |
|-----------|-------------------|
| Low-level/mundane tasks | Free models (BigPickle, etc.) |
| Design refinement | Gemini |
| Complex logic | Claude |
| Token-intensive operations | Free models via OpenCode |

---

## 5. Google AI Studio Pipeline

### 5.1 Design Framework (5 Components)

Use this framework to structure AI Studio prompts:

| Component | Elements |
|-----------|----------|
| **1. Panel Layout** | Hero, features, social proof, CTA, footer |
| **2. Style & Aesthetic** | Soft shadows, gradients, rounded corners, glass morphism |
| **3. Color & Theme** | Primary, secondary, accent, background, text |
| **4. Typography** | Headers, body, accent fonts |
| **5. Animations & Interactions** | Hover effects, scroll animations, transitions |

### 5.2 Pattern Layouts by Site Type

| Site Type | Typical Pattern |
|-----------|-----------------|
| SaaS | Hero → Features → Social proof → CTA |
| E-commerce | Hero → Products → Reviews → Cart CTA |
| Fintech/Crypto | Hero → Trust signals → Features → Security → CTA |
| Agency/Portfolio | Hero → Work samples → Process → Testimonials → Contact |

### 5.3 Design Inspiration Workflow

**Step 1: Gather Inspiration**
- Browse Dribbble for design inspiration
- Screenshot sections you like
- Number them (1, 2, 3...)

**Step 2: Create Mood Board (Canva)**
- Label sections: "Hero like this", "Testimonials like this"
- Screenshot the mood board

**Step 3: Extract Brand Guidelines (Firecrawl)**
```
firecrawl.dev → Playground
Enter: competitor-url.com
Format: branding
Start scraping
```
Returns: Logo, favicon, color palette, fonts

**Step 4: Website HTML Extraction**
```
Google: "HTML website extractor view page source"
Enter URL → View source code → Download
```

**Step 5: AI Studio Prompt Assembly**
```
[Paste mood board screenshot]
[Paste design framework components]
[Paste brand guidelines]

"I'm building a [SITE TYPE] website for [PURPOSE]. 
Build this using the inspiration above with the color palette provided."
```

### 5.4 Transferring to AntiGravity

**Method 1: GitHub Transfer**
1. AI Studio → Export code
2. Create GitHub repo
3. Import to AntiGravity as skill

**Method 2: Direct Import**
1. Download HTML from AI Studio
2. Upload to AntiGravity
3. Prompt: "Rebuild the website with this HTML"

---

## 6. Motion Background Workflow

### 6.1 Complete Pipeline: Gemini → Whisk → Flow → ezGIF → AntiGravity

This creates scroll-triggered animated product backgrounds.

### 6.2 Step 1: Generate Product Image (Gemini)

```
Prompt: "I need an image of [PRODUCT] with no background. 
Make it realistic and [QUALITY_DESCRIPTORS].
Cup/product has to be centered with black background."
```

**Key parameters:**
- Centered subject
- Black background (for clean effects)
- Vertical orientation
- High detail

### 6.3 Step 2: Generate End Frame (Whisk)

**Go to:** labs.google/whisk

**Upload:** Your Gemini product image

**End Frame Prompt Template:**
```
[PRODUCT] with maximum visual impact.
Add flying [ELEMENTS] in the air.
Add liquid/particles splashing.
Coffee/product stays intact, elements fly around it.
Add liquid drops falling from sky into drink.
```

**Iteration tip:** If Whisk misunderstands:
- Return to Gemini
- Refine prompt: "Don't rip the product apart. Keep [product] the same, just add flying [elements] and liquid shots in the air."

### 6.4 Step 3: Generate Animation (Google Flow)

**Go to:** labs.google/flow

**Settings:**
- Mode: Frame to Video (NOT text to video)
- Quality: VO3.1 Quality (not Fast)

**Upload:**
1. Starting frame: Original product image (crop and save)
2. End frame: Whisk-generated explosion/effect image (crop and save)

**Prompt Template:**
```
Smooth transition from static product to dynamic explosion effect.
Particles and elements flow naturally.
Professional product advertisement quality.
```

**Download:** Always select "Upscale version"

### 6.5 Step 4: Convert to Frames (ezGIF)

**Go to:** ezgif.com → Video to GIF → Video to JPG converter

**Upload:** Downloaded Flow video

**Settings:**
- Start time: 2 seconds (skip static intro)
- End time: 8 seconds
- Frame rate: 29-30 FPS

**Output:** ~120-180 individual JPG frames

**Download:** As ZIP folder

### 6.6 Step 5: Import to AntiGravity

1. Upload ZIP of frames to AntiGravity
2. Use adapted web generation prompt
3. Select Gemini 3 Pro + Planning mode
4. Generate website with scroll-triggered animation

**Prompt adaptation (via Gemini):**
```
"Adapt this web generation prompt to my [PRODUCT] and animation frames:
[BASE_WEB_GEN_PROMPT]"
```

### 6.7 Step 6: Deploy to Netlify (Static)

```
Prompt: "I want to host this on Netlify as static web. Give me code."
```

**Result:** Creates `/out` folder

**Netlify deployment:**
1. Go to netlify.com
2. Drag and drop `/out` folder
3. Domain management → Add custom domain
4. Go live

---

## 7. UI Component Libraries

### 7.1 UI Sniping Strategy

**Concept:** Find best-in-class UI components and integrate them into your builds.

### 7.2 Magic UI (magicui.design)

**Features:**
- Rainbow buttons
- Shimmer buttons
- Ripple buttons
- Text animations
- Aura effects
- Orbiting circles
- Avatar animations

**Integration Method 1: MCP**
```
Prompt: "Install Magic UI onto the terminal, then input this button at [LOCATION] replacing [EXISTING_ELEMENT]: [COMPONENT_CODE]"
```

**Integration Method 2: Manual**
1. Find component on magicui.design
2. Click "Code"
3. Copy code
4. Paste into AntiGravity with location instructions

### 7.3 21st.dev

**Access:** 21st.dev

**Usage:**
- Browse components (buttons, cards, forms, etc.)
- Click component → Copy prompt
- Paste in AntiGravity

**Alternative method (if direct copy fails):**
```
Prompt: "Head over to [21ST.DEV_COMPONENT_URL] and import this component, copying it line by line."
```

### 7.4 CodePen (codepen.io)

**Best for:**
- Unique animations
- Trending designs
- Community innovations
- Liquid gradients
- Scroll effects

**Usage:**
1. Browse trending or search specific effects
2. Copy HTML/CSS/JS
3. Paste in AntiGravity with context

### 7.5 Integration Workflow

```
1. Build base website (AI Studio → AntiGravity)
2. Run UI/UX Pro Skill audit
3. Identify enhancement opportunities
4. UI Snipe: Find superior components
5. Replace with: "Hey, replace [ELEMENT] with this [COMPONENT_CODE]"
6. Test responsiveness
7. Commit changes
```

---

## 8. Backend Integration

### 8.1 Supabase Setup

**Create Account:** supabase.com (free tier: 2 environments)

**Generate Access Token:**
```
Dashboard → Settings → Generate new token
Name: [PROJECT_NAME]
Expiry: Set as needed
Copy token
```

**Connect to AntiGravity:**
```
Additional Options → MCP Servers → Supabase → Configure
Paste access token → Save
```

### 8.2 Authentication Configuration

**Supabase Dashboard → Authentication → Sign in providers**

**Options:**
- Email (disable "Confirm email" during testing)
- Phone
- Apple
- Gmail/Google
- GitHub
- etc.

### 8.3 Database Creation via AntiGravity

```
Prompt: "Create a login section with email, name, and website fields.
When user signs up, save to Supabase.
Create a dashboard where they can enter:
- Their goal
- Their income  
- Number of active clients
Save all data to Supabase so it persists on refresh.
Connect to Supabase MCP."
```

**AntiGravity automatically:**
- Creates database tables
- Sets up authentication
- Builds CRUD operations
- Connects frontend to backend

### 8.4 Database Management

**View tables:** Supabase Dashboard → Databases → Tables

**Enable Row Level Security:**
```
Click table → RLS disabled → Enable RLS
```

### 8.5 Verifying Data Flow

1. Create account on your website
2. Enter test data
3. Go to Supabase → Table Editor
4. Verify data appears
5. Modify in Supabase → Refresh website → Verify sync

---

## 9. GitHub to Vercel Deployment

### 9.1 GitHub Repository Setup

**Create new repo:**
```
GitHub → New → Repository name → Create (public)
```

**Get push command:**
```bash
git remote add origin https://github.com/USERNAME/REPO.git
git branch -M main
git push -u origin main
```

### 9.2 Push from AntiGravity

```
Prompt: "Push this project to GitHub. Here's the repo: [GITHUB_REPO_URL].
Make sure files are in order for Vercel deployment.
Do necessary amendments and push."
```

### 9.3 Vercel Deployment

**Initial Setup:**
1. vercel.com → Create account → Connect GitHub
2. Add New → Project
3. Select repository → Import
4. Framework: (auto-detected, usually Next.js)
5. Deploy

### 9.4 Environment Variables

**For Supabase:**
```
Vercel Dashboard → Settings → Environment Variables
Add:
- NEXT_PUBLIC_SUPABASE_URL
- NEXT_PUBLIC_SUPABASE_ANON_KEY
- SUPABASE_SERVICE_ROLE_KEY
```

**Via Vercel MCP:**
AntiGravity auto-manages environment variables if MCP is configured.

### 9.5 Analytics Setup

**Vercel Dashboard → Analytics → Enable**

```
Prompt: "Add Vercel analytics to the project."
```

**Speed Insights:**
```
Prompt: "Install Vercel speed insights package: [PACKAGE_CODE]"
```

### 9.6 Continuous Deployment Workflow

```
1. Make changes in AntiGravity
2. AntiGravity pushes to GitHub
3. Vercel auto-detects changes
4. Vercel rebuilds and deploys
5. Live website updates automatically
```

### 9.7 Custom Domain

**Vercel Dashboard → Domains → Add**
- Buy through Vercel, or
- Connect existing domain via DNS

---

## 10. Visual RAG Thread Integration

### 10.1 React Shell Architecture

**Three-Layer Model:**

| Layer | Purpose | Components |
|-------|---------|------------|
| **Interaction** | User interface | Chat, file upload, streaming, citations |
| **Cognitive** | Intelligence visibility | Retrieved docs, reasoning, agent traces, confidence |
| **Control** | System orchestration | Retrieval strategies, agent toggles, memory inspection |

### 10.2 Component Structure

```
<QueryInput />           // User query entry
<RetrievalInspector />   // What docs were retrieved, why
<ChunkViewer />          // View individual chunks
<AgentTrace />           // Agent actions, tools used
<AnswerComposer />       // Final response assembly
```

### 10.3 Views Over Same Data

| View | Purpose |
|------|---------|
| Chat View | End-user conversation |
| Research View | Deep document exploration |
| Audit View | Compliance, provenance tracking |
| Debug View | System troubleshooting |
| Client View | Simplified, branded output |

### 10.4 Module Build Sequence

**Phase 1: Foundation**
- Auth (Supabase)
- Chat UI
- Backend wiring
- Observability

**Phase 2: Ingestion**
- Document upload
- Chunking
- Embedding

**Phase 3: Retrieval**
- Vector search
- Hybrid search
- Re-ranking

**Phase 4: Agents**
- Tool integration
- Agent orchestration

**Phase 5: UI Intelligence**
- Visualization
- Knowledge graphs
- Timeline views

### 10.5 Integration with WebDev Factory

```
WebDev Factory Output → React Shell Template
                     → Visual RAG Components
                     → Supabase Backend
                     → Vercel Deployment
                     → Production RAG Application
```

---

## 11. Production Checklists

### 11.1 Pre-Development Checklist

- [ ] Define site purpose (landing page, SaaS, e-commerce, etc.)
- [ ] Complete competitor research via Firecrawl
- [ ] Create mood board with numbered sections
- [ ] Extract brand guidelines
- [ ] Define pattern layout
- [ ] Set up GitHub repository
- [ ] Configure AntiGravity MCP servers

### 11.2 Design Phase Checklist

- [ ] Generate initial design in AI Studio
- [ ] Create product images (Gemini)
- [ ] Generate motion effects (Whisk → Flow → ezGIF)
- [ ] Export design to AntiGravity
- [ ] Install UI/UX Pro Skill
- [ ] Run initial audit

### 11.3 Development Phase Checklist

- [ ] Import AI Studio design
- [ ] UI Snipe key components (buttons, cards, animations)
- [ ] Run UI/UX Pro Skill optimization
- [ ] Configure Supabase backend
- [ ] Build authentication flow
- [ ] Create database tables
- [ ] Test all CRUD operations
- [ ] Mobile responsiveness check

### 11.4 Deployment Checklist

- [ ] Push to GitHub
- [ ] Connect Vercel to repo
- [ ] Configure environment variables
- [ ] Enable Vercel analytics
- [ ] Add speed insights
- [ ] Enable Row Level Security (Supabase)
- [ ] Test live deployment
- [ ] Configure custom domain
- [ ] SSL certificate verification

### 11.5 Post-Launch Checklist

- [ ] Monitor Vercel analytics
- [ ] Check page speed scores
- [ ] Verify database operations
- [ ] Test user flows end-to-end
- [ ] Set up error monitoring
- [ ] Document any custom configurations

---

## 12. Prompt Templates

### 12.1 Competitive Research

```
Hey dude, I want you to do competitive research for me on [INDUSTRY/PRODUCT].
I want you to find the top 5 brands that people buy/use.
Break down their website: positioning, CTAs, vibes, colors, logos, color palette, feel.
Anything useful for constructing my own brand.
```

### 12.2 AI Studio Design Generation

```
I'm building a [SITE_TYPE] for [PURPOSE].

Pattern layout: [Hero → Features → Social proof → CTA]
Style: [Soft shadows, gradients, rounded corners]
Colors: [PRIMARY, SECONDARY, ACCENT]
Typography: [FONT_FAMILY]
Animations: [Hover effects, scroll animations]

[PASTE MOOD BOARD SCREENSHOT]
[PASTE BRAND GUIDELINES]

Build this website with the above specifications.
```

### 12.3 Motion Effect Generation (Whisk)

```
[PRODUCT] with maximum visual impact.
Flying [ELEMENTS] in the air around the product.
Liquid splashing and drops from sky.
Product stays intact, elements create dynamic effect.
Professional advertisement quality.
```

### 12.4 Backend Creation

```
Create a login section with [FIELDS].
When user signs up, save to Supabase.
Create a dashboard with [DATA_FIELDS].
All data should persist on refresh.
Connect to Supabase MCP.
Make the form gorgeous in the same style as the site.
```

### 12.5 UI Component Integration

```
Hey dude, I want you to:
1. Install [COMPONENT_LIBRARY] onto the terminal
2. Replace [EXISTING_ELEMENT] at [LOCATION]
3. With this [COMPONENT_CODE/URL]
4. Keep the same style as the rest of the site
```

### 12.6 Deployment Preparation

```
I want to push this live to GitHub then host on Vercel.
Make sure files are in order for deployment.
Do necessary amendments.
Push to this repo: [GITHUB_URL]
Let me know when complete.
```

### 12.7 Skill Audit

```
In accordance with [SKILL_NAME], audit and improve the website.
Align with all design principles outlined in the skill.
Give me a checklist of all improvements made.
```

### 12.8 Context Reset (Long Sessions)

```
Open new chat window to avoid context rot.
Fresh context = better performance.
```

---

## Appendix A: File Structure Templates

### A.1 Standard Web Project

```
project-root/
├── .env                    # Environment variables (gitignored)
├── .env.example            # Template for env vars
├── README.md               # Project documentation
├── package.json            # Dependencies
├── next.config.js          # Next.js configuration
├── vercel.json             # Vercel deployment config
├── public/
│   ├── images/             # Static images
│   └── fonts/              # Custom fonts
├── src/
│   ├── app/                # Next.js app router
│   ├── components/         # React components
│   │   ├── ui/             # UI primitives
│   │   ├── layout/         # Layout components
│   │   └── features/       # Feature-specific components
│   ├── lib/                # Utility functions
│   ├── styles/             # Global styles
│   └── types/              # TypeScript types
└── supabase/
    └── migrations/         # Database migrations
```

### A.2 Animation Assets

```
animations/
├── frames/                 # ezGIF extracted frames
│   ├── frame_001.jpg
│   ├── frame_002.jpg
│   └── ...
├── source/
│   ├── product_original.png    # Gemini output
│   ├── effect_end_frame.png    # Whisk output
│   └── animation.mp4           # Flow output
└── processed/
    └── optimized/              # Compressed frames
```

---

## Appendix B: Quick Reference Commands

### B.1 Terminal Commands

| Action | Command |
|--------|---------|
| New terminal | Terminal → New Terminal |
| Start OpenCode | `opencode` |
| View models | `/models` |
| Select all models | `Ctrl + A` |
| Clear terminal | `Cmd + L` |
| Switch plan/build | `Cmd + Shift` |

### B.2 AntiGravity Navigation

| Location | Path |
|----------|------|
| Agent Manager | Bottom left → Agent Manager |
| Terminal | Terminal → New Terminal |
| MCP Config | Additional Options → MCP Servers |
| Skills | Within project skills folder |
| Preview | Built-in browser panel |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-01 | Initial comprehensive documentation |

---

*Part of Enterprise_OS Platform Creation Factory*
*WebDev Factory Module v1.0*
