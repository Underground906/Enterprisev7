# Enterprise OS V7 — Complete Build Specification

**Version:** 1.0
**Date:** 2026-02-17
**Owner:** John
**Revenue Target:** £100,000+/year PER CLIENT (£8,333/mo per seat)
**Sales Target:** 1,000 clients (SMB/Pro) + 200 enterprise clients = £20M+/year ARR
**Exit Position:** AI-native enterprise operating system — acquisition target at £20M+ ARR pre-sale
**Status:** DEFINITIVE BUILD SPEC — supersedes all prior PRDs for implementation purposes
**Companion PRDs:** PRD_MASTER (vision), PRD_Coherence (RAG), PRD_GRANULAR_SCREENS (UI layouts)

---

## 1. EXECUTIVE SUMMARY

### What Enterprise OS Is

Enterprise OS is an AI-native operating system for businesses. It replaces the fragmented stack of Monday.com + Basecamp + Slack + Notion + Google Drive + ChatGPT conversations with a single unified platform that captures, routes, indexes, and deploys every piece of intelligence a business produces.

**One dashboard to rule them all.**

It is simultaneously:
1. **John's internal backbone** — the file-based knowledge architecture powering all builds (Enterprise, Fitness, Property, LeadEngine)
2. **A commercial SaaS product** — white-labelable platform for teams using AI at maximum effectiveness
3. **A second brain for organisations** — institutional memory that compounds over time, survives staff turnover, and gets smarter every day

### Why It's Worth £100K+/Year Per Client

| Value Driver | Impact |
|---|---|
| Eliminates 5-8 SaaS subscriptions | £500-2,000/mo saved directly |
| AI knowledge recapture (90% of AI-generated value currently evaporates in chat histories) | Compounding IP worth millions over time |
| Zero-meeting status updates | CEO Digest, auto-rollups = 10+ hours/week recovered |
| Institutional memory | No more "the person who knew that left" |
| 7-level progressive disclosure | Everyone sees exactly what they need, nothing more |
| Multi-LLM orchestration | Not locked to one AI provider |
| Self-improving system | Gets smarter with every interaction |

### What It Replaces

| Current Tool | Enterprise OS Module | What Changes |
|---|---|---|
| Monday.com / Asana | Navigation Centre + Build Factory | Goals cascade to tasks automatically. No manual board management |
| Basecamp / ClickUp | Command Deck | Sessions replace "projects." Every action logged, every decision traced |
| Slack / Teams | Command Deck (AI Chat) + Knowledge Library | Conversations become searchable institutional knowledge, not lost threads |
| Notion / Confluence | Knowledge Library + Domain Pillars | Content auto-routed to the right domain. S>C>E governance prevents chaos |
| Google Drive / Dropbox | Core Engine (routing) + Knowledge Library | Files indexed semantically, not buried in folder hierarchies |
| ChatGPT / Claude (standalone) | Command Deck (Agent OS) | All AI interactions captured, extracted, routed. 80+ role-specific agents |
| Spreadsheets / BI tools | Operations + Navigation Centre | Real-time dashboards, auto-generated, no manual data entry |

---

## 2. THE 8-MODULE ARCHITECTURE

### The Body Metaphor

| Module | Organ | Function | Standalone App Name |
|---|---|---|---|
| Navigation Centre | Brain | Decides what matters, sets direction | NavOS |
| Command Deck | Hands | Does the work through sessions and agents | WorkPulse |
| Core Engine | Nervous System | Routes signals and intelligence everywhere | Connective |
| Knowledge Library | Stomach | Ingests and digests raw data into intelligence | DigestOS |
| Template Hub | DNA | Provides reusable blueprints for everything | Blueprint |
| Domain Pillars | Organs | 23+ specialist areas of expertise | PillarOS |
| Build Factory | Kinetic Limbs | Assembles intelligence into launched products | Velocity |
| Operations | Immune System | Protects and tracks live business performance | ScaleGuard |

Each module is a **standalone app** that plugs into the unified platform. Customers can start with 3 modules (Starter tier) and grow into all 8.

---

## 3. FEATURES & BENEFITS PER SCREEN

### How To Read This Section

Each screen includes:
- **What it does** — the feature
- **Why it matters** — the business benefit
- **Who uses it** — permission levels (L1 Freelancer → L7 CEO)
- **Key integrations** — external APIs this screen connects to
- **Database entities** — what data it reads/writes
- **Revenue enabler** — how this screen justifies the price tag

---

### MODULE 1: NAVIGATION CENTRE (The Brain)

> **Killer benefit:** "You never lose sight of what matters. The system tells you what's important today, flags what's drifting, and challenges you when you're avoiding hard decisions."

---

#### SCREEN NAV_A: Goal Intake Wizard (`/nav/goals/new`)

**What it does:**
Stream-of-consciousness goal capture → AI asks clarifying questions → auto-generates a structured 5A plan (Alignment, Awareness, Accountabilities, Activities, Assets) with timeline and milestones.

**Why it matters:**
- Executives think in fuzzy ambitions ("grow revenue 30%"). This turns fuzzy into structured.
- The 5A breakdown ensures nothing is missed: vision, risks, owners, rhythm, and resources all addressed before work begins.
- Every goal created here cascades down to tasks, sessions, and outputs — closing the gap between strategy and execution.

**Who uses it:** L2+ (Individual Pros and above)

**Key features:**
- Voice-to-text intent capture (speech recognition API)
- AI-powered refinement dialogue (multi-turn clarification)
- Automatic 5A decomposition with user editing
- Milestone timeline with dependency linking between goals
- Draft auto-save every 30 seconds
- Goal templating from previous successful goals

**Revenue enabler:** This is the entry point for strategic alignment. Without it, teams default to ad-hoc task lists. With it, every piece of work traces back to a strategic objective — the #1 pain point for companies at £1M+ revenue.

**Database entities:** `goals`, `goal_5a_sections`, `milestones`, `goal_dependencies`, `goal_templates`

**External integrations:**
- **Jira/Linear** — import existing epics as goals
- **Google Calendar** — sync milestones to calendar
- **Slack** — notify stakeholders when goals are created

---

#### SCREEN NAV_B: Role-Informed Perspective Panel (`/nav/goals/:id/perspectives`)

**What it does:**
For any goal, the system generates perspectives from multiple expert roles (SEO Lead, Data Engineer, Chief of Staff, etc.) — flagging risks, opportunities, and blind spots before work begins.

**Why it matters:**
- Solo founders get a virtual C-suite. A £99/mo subscription replaces £500K/year in executive salary for strategic review.
- Enterprises eliminate "we didn't think of that" — every goal gets stress-tested by 80+ role perspectives.
- Prevents the #1 cause of project failure: incomplete upfront thinking.

**Who uses it:** L3+ (Team Lead and above); L5+ sees full Think Tank

**Key features:**
- AI-generated perspectives from 80+ role profiles
- Risk aggregation across all perspectives (Critical/Warning/Info)
- One-click task creation from recommendations
- Add custom roles on demand
- Historical perspective accuracy tracking

**Revenue enabler:** The "virtual board of advisors" is the single most differentiated feature. No competitor offers multi-role AI stress-testing of business goals.

**Database entities:** `perspectives`, `role_profiles`, `perspective_recommendations`, `risk_flags`

**External integrations:**
- **Custom AI models** — domain-specific role perspectives
- **Industry databases** — pull market context for informed perspectives

---

#### SCREEN NAV_C: Morning Brief (`/nav/brief`)

**What it does:**
Daily auto-generated "newspaper" delivered at 6:00 AM: yesterday's wins, today's top 3 priorities, blockers, team activity summary (L3+), and strategic alignment notes (L5+).

**Why it matters:**
- Eliminates the "what should I do today?" paralysis
- Replaces morning standup meetings (10-30 min × team size × 250 days = enormous time savings)
- Every person in the org starts the day aligned without a single meeting

**Who uses it:** L1+ (everyone, adapted per level)

**Key features:**
- AI-synthesized from session logs, goal progress, and system activity
- Role-level adaptation (freelancer sees tasks; CEO sees org pulse)
- Historical briefs browsable by date
- Print/export to PDF
- Configurable delivery time

**Revenue enabler:** "You will never have another status meeting." This alone justifies the £99/mo Starter tier for teams of 5+.

**Database entities:** `briefs`, `brief_sections`, `daily_priorities`, `session_summaries`

**External integrations:**
- **Email** — brief delivered to inbox at configured time
- **Slack** — posted to team channels
- **Calendar** — pulls today's scheduled events into brief

---

#### SCREEN NAV_D: Goal Health Dashboard (`/nav/dashboard`)

**What it does:**
Visual heatmap of all active objectives with Health Scores (1-10). Card view, heatmap view, and list view. Filter by owner, department, status, time range.

**Why it matters:**
- At-a-glance strategic health — no drilling into 15 different tools
- Colour-coded urgency (green/amber/red) means intervention before crisis
- Goal health auto-degrades when tasks stall, so nothing hides

**Who uses it:** L3+ (Team Lead and above)

**Key features:**
- Three view modes: cards, heatmap, list
- Auto-calculated health scores from task completion velocity, session activity, milestone progress
- Quick-update slider (change health + note in 3 clicks)
- Goal actions: edit, archive, generate perspectives, view history
- Summary stats: total goals, average health, at-risk count, completed this month

**Revenue enabler:** Replaces Monday.com dashboards + custom BI reporting. One screen, always current, zero manual data entry.

**Database entities:** `goals`, `goal_health_scores`, `goal_health_history`, `goal_tags`

**External integrations:**
- **Monday.com** — bidirectional sync of project status
- **Jira** — epic progress maps to goal health
- **Power BI / Tableau** — export health data for enterprise reporting

---

#### SCREEN NAV_E: Decision & Iteration Log (`/nav/decisions`)

**What it does:**
Chronological timeline of every strategic decision — what changed, why, what the before/after was. Version control for strategy.

**Why it matters:**
- "Why did we pivot on that?" is answered in seconds, not hours of email archaeology
- Institutional memory of strategic thinking — survives staff turnover
- Audit trail for boards, investors, and compliance

**Who uses it:** L3+ (Team Lead and above)

**Key features:**
- Timeline view with decision cards
- Before/after comparison view
- Full-text search across all decisions
- Filter by goal, author, decision type (pivot/commitment/cancellation)
- Linked artifacts showing what evidence informed the decision

**Revenue enabler:** Decision traceability is a compliance requirement for regulated industries (finance, legal, healthcare). This screen alone opens enterprise sales.

**Database entities:** `decisions`, `decision_iterations`, `decision_artifacts`, `decision_tags`

**External integrations:**
- **Notion** — sync decision logs
- **Compliance tools** — export audit trail

---

#### SCREEN NAV_F: AI Challenge Console (`/nav/challenges`)

**What it does:**
Proactive AI that challenges stale goals, abandoned tasks, and strategic drift. "This task has been on the list for 5 days. Delete or commit a date?"

**Why it matters:**
- Prevents the silent death of initiatives — tasks that nobody cancels but nobody does
- Forces intellectual honesty: is this still worth doing?
- The AI doesn't have feelings or politics — it calls out what humans won't

**Who uses it:** L5+ (Executive and above)

**Key features:**
- Auto-generated challenges based on system activity patterns
- Severity levels: Critical, Warning, Info
- Conversational response (debate the AI)
- One-click task creation from accepted challenges
- Snooze with accountability (snoozed items escalate if not addressed)
- Challenge accuracy tracking (did acting on challenges improve outcomes?)

**Revenue enabler:** "Your AI executive coach." Premium feature for £499+ tiers. No other platform does proactive strategic intervention.

**Database entities:** `challenges`, `challenge_responses`, `challenge_escalations`

---

#### SCREEN NAV_G: State Snapshot (`/nav/state`)

**What it does:**
AI-refreshed daily summary of "what is true right now" across the entire organisation. Strategic alignment score, active goals, risk register, resource allocation, key metrics.

**Why it matters:**
- The CEO's single source of truth — one page, one glance, complete picture
- Diff view shows exactly what changed day-to-day
- AI commentary interprets the data and recommends actions

**Who uses it:** L6+ (C-Suite and above)

**Key features:**
- Auto-generated from all system activity
- Strategic alignment score (1-10) with 5A dimension breakdown
- Risk register: stale goals, blocked tasks, alignment drift
- Resource allocation: who's working on what, utilisation %
- Diff comparison between any two dates
- AI commentary with recommended actions

**Revenue enabler:** "Your daily board report, written by AI, always current." Enterprise tier premium — C-Suite pay premium for this.

**Database entities:** `state_snapshots`, `alignment_scores`, `risk_items`, `resource_allocations`

---

### MODULE 2: COMMAND DECK (The Hands)

> **Killer benefit:** "Every piece of work you do is captured, every AI conversation becomes institutional knowledge, every decision is logged. Nothing falls through the cracks. Ever."

---

#### SCREEN CMD_A: Active Cockpit (`/cmd/session`)

**What it does:**
Three-pane workspace: Running Log (left), AI Chat (middle), Outputs Pane (right). Every action timestamped. Every AI interaction captured. Every output auto-routed to the right pillar.

**Why it matters:**
- Replaces "23 browser tabs + ChatGPT window + Slack + Google Docs" with one unified workspace
- Total Recall: resume any complex task with full context — even months later
- The Three-Habit Loop (Start → Work → End) ensures nothing is forgotten
- Auto-synthesis at session end creates manager-ready summaries without effort

**Who uses it:** L1+ (everyone)

**Key features:**
- Session intent declaration (one-line purpose)
- Running log with entry types: work, decision, output, note, milestone
- AI chat with 80+ switchable role profiles
- Output cards with auto-routing to domain pillars
- Source link tracking (capture every URL, thread, file used)
- Auto-synthesis on session end
- Session timer with pause/resume
- Keyboard shortcuts for rapid logging

**Revenue enabler:** This IS the product for individual users. "Total recall for knowledge workers." Every AI conversation you've ever had, searchable and actionable forever.

**Database entities:** `sessions`, `session_events`, `session_outputs`, `session_sources`, `agent_activations`, `session_digests`

**External integrations:**
- **Slack** — pull messages into session context
- **GitHub** — link commits to sessions
- **Google Docs** — attach docs as session sources
- **Figma** — link designs to sessions
- **ChatGPT/Claude** — import external AI conversations
- **Zoom/Teams** — auto-log meeting transcripts as sessions

---

#### SCREEN CMD_B: Session History (`/cmd/sessions`)

**What it does:**
Searchable, filterable table of all past sessions. Click any session to see full context: intent, duration, log entries, outputs, sources.

**Why it matters:**
- "What did I work on last Tuesday?" — answered instantly
- Team leads see all team sessions (L3+) without asking
- Auto-generated Friday rollups eliminate "what did you do this week?" meetings

**Who uses it:** L1+ (L3+ sees team sessions)

**Key features:**
- Full-text search across all session content
- Filter by date, goal, user, has-outputs
- Session detail with full log replay
- Export as Markdown/PDF
- Team rollup view (L3+)

**Revenue enabler:** Audit trail for consultancies billing by the hour. Proof of work for remote teams. Eliminates timesheets.

**Database entities:** `sessions`, `session_events` (read-only)

---

#### SCREEN CMD_C: Auto-Digest Generation (`/cmd/digests`)

**What it does:**
Split-screen: messy raw session log (left) transforms into polished, manager-ready summary (right). AI does the heavy lifting; human reviews and approves.

**Why it matters:**
- The gap between "what I actually did" and "what my manager needs to know" is bridged automatically
- Consistent quality: every session produces a professional summary
- No more end-of-week scramble to remember what happened

**Who uses it:** L3+ (Team Lead and above)

**Key features:**
- AI transforms raw session log → structured digest
- Key decisions highlighted
- Outputs listed with routing info
- Next steps extracted
- Edit before approval
- Regenerate with different emphasis
- Auto-route approved digests to stakeholders

**Revenue enabler:** "Your team's work, summarised automatically, every day." Managers pay for this.

**Database entities:** `session_digests`, `digest_approvals`

---

#### SCREEN CMD_D: Agent Registry (`/cmd/agents`)

**What it does:**
Library of 80+ AI role profiles (SEO Lead, Data Engineer, Brand Strategist, etc.). Search, browse, activate for the current session. Create custom agents (L4+).

**Why it matters:**
- Instead of generic AI, you get domain-expert AI
- A brand strategist agent knows about positioning, messaging, competitive analysis — it doesn't need to be told
- Custom agents encode institutional knowledge: "Our SEO agent knows our keyword strategy"

**Who uses it:** L2+ (L4+ creates custom agents)

**Key features:**
- 80+ pre-built role profiles with expertise areas
- Category tabs: Knowledge, Creation, Platform, System, Custom
- Most-used section for quick access
- Custom agent builder (name, avatar, expertise, system prompt, tools)
- Activation history and effectiveness tracking
- Agent-to-agent collaboration (multi-agent workflows)

**Revenue enabler:** "80 expert consultants for £99/mo." The role profile system is Enterprise OS's moat. Custom agents are the upsell to £499+ tiers.

**Database entities:** `agents`, `agent_profiles`, `agent_activations`, `custom_agents`, `agent_tools`

**External integrations:**
- **OpenAI / Anthropic / Cohere / open-source** — multi-LLM agent backends
- **Custom tools** — agents can call calculators, APIs, databases

---

#### SCREEN CMD_E: Approval & Governance Queue (`/cmd/approvals`)

**What it does:**
Queue of items pending promotion from Staging (🟡) to Canonical (🟢). Swipe-to-approve interface with diff views, batch operations, and rejection workflows.

**Why it matters:**
- S>C>E governance prevents "AI chaos" — raw AI output doesn't become truth until a human approves it
- Quality gate between messy work-in-progress and institutional source of truth
- Batch operations for efficiency (approve 20 items in 30 seconds)

**Who uses it:** L4+ (Department Head and above)

**Key features:**
- Queue table with type, pillar, submitter, date, preview
- Full content review with diff against existing canonical
- Promote / Reject / Request Changes workflow
- Bulk select for batch operations
- Rejection with feedback (auto-notifies submitter)
- Stats: pending, approved today, rejected today, average review time

**Revenue enabler:** Governance is the enterprise sales differentiator. "AI generates chaos; Enterprise OS governs it." Compliance officers love this.

**Database entities:** `staging_items`, `canonical_items`, `promotion_logs`, `rejection_logs`, `audit_trail`

---

### MODULE 3: CORE ENGINE (The Nervous System)

> **Killer benefit:** "Every piece of data in your organisation is indexed, searchable, and traceable back to its source. Nothing lost, nothing duplicated, everything findable in seconds."

---

#### SCREEN ENG_A: Universal Index (`/engine/index`)

**What it does:**
Master data table of every file, artifact, and knowledge item in the system. Sortable, filterable, searchable by name, type, pillar, S>C>E state, date, tags.

**Why it matters:**
- Single source of truth for "what do we have?"
- Provenance chain for every item (where it came from, how it was routed)
- Epoch counts: total items by state, type, pillar — at a glance

**Who uses it:** L2+ (Individual Pro and above)

**Key features:**
- Full data table with sortable columns
- Semantic + keyword search
- Filter by: pillar (23), artifact type (29), S>C>E state, date range, tags
- Item detail panel with full metadata, preview, provenance chain, routing history
- Bulk operations: route, tag, export
- CSV/JSON export

**Revenue enabler:** "Where is that thing?" — the most asked question in every company. This screen answers it instantly.

**Database entities:** `documents`, `document_metadata`, `provenance_chain`, `routing_history`, `tags`

---

#### SCREEN ENG_B: Routing Rules Editor (`/engine/routing`)

**What it does:**
Logic builder for content routing rules. Set keyword weights, thresholds, and LLM fallback per pillar. Test mode: paste content, see where it would route.

**Why it matters:**
- Automatic content organisation — no more "put it in the shared drive and hope"
- Customisable per business: a law firm's routing rules differ from a tech startup's
- Test mode prevents misconfiguration before going live

**Who uses it:** L4+ (Department Head and above)

**Key features:**
- Per-pillar keyword lists with weight sliders
- Threshold configuration (minimum score to route)
- LLM fallback toggle (use AI when keywords aren't enough)
- Test mode: paste content → see routing score per pillar
- Routing logs: recent decisions with scores
- Save/revert

**Revenue enabler:** Customisable routing is the "power user" feature that justifies Professional tier. Generic RAG tools don't let you tune routing.

**Database entities:** `routing_rules`, `routing_keywords`, `routing_logs`, `routing_tests`

---

#### SCREEN ENG_C: RAG Quality Dashboard (`/engine/rag`)

**What it does:**
Monitoring dashboard for the RAG pipeline: chunking efficiency, embedding coverage per pillar, query latency, retrieval quality scores from user feedback.

**Why it matters:**
- RAG quality degrades silently without monitoring — this makes it visible
- Identifies knowledge gaps: "PIL_12 has 0% embedding coverage"
- Query latency tracking ensures the system stays fast

**Who uses it:** L4+ (Department Head and above)

**Key features:**
- Stat cards: total chunks, avg size, total embeddings, index health %, query latency P50/P95
- Chunking distribution chart
- Embedding coverage per pillar
- Query performance over time
- User feedback correlation (quality ratings vs. retrieval scores)

**Revenue enabler:** Enterprise customers require SLA-level monitoring. This screen proves the system is working.

**Database entities:** `embedding_metadata`, `query_logs`, `query_feedback`, `rag_metrics`

---

#### SCREEN ENG_D: Schema & Data Model Library (`/engine/schemas`)

**What it does:**
Library of all PostgreSQL, JSON, and API schemas used across projects. Browse, preview, copy, and deploy schemas into new projects.

**Why it matters:**
- Don't reinvent database schemas — reuse proven structures
- New projects start with tested schemas in seconds
- Cross-project consistency: all platforms share the same user/auth/notification patterns

**Who uses it:** L3+ (Team Lead and above)

**Key features:**
- Schema cards with type, table count, last modified
- Syntax-highlighted SQL/JSON viewer
- ERD diagram (if available)
- Copy to clipboard
- "Use in Project" — deploy schema to Build Factory project
- Version history

**Revenue enabler:** "Start any project with proven database architecture." Speed-to-market for enterprises building new products.

**Database entities:** `schemas`, `schema_versions`, `schema_deployments`

---

#### SCREEN ENG_E: Error Library & Failure Log (`/engine/errors`)

**What it does:**
Diagnostic heart monitor: every script error, API failure, routing failure, and ingestion error logged with full stack traces, context, and resolution workflow.

**Why it matters:**
- Systems fail silently. This makes every failure visible.
- Resolution notes build a troubleshooting knowledge base
- Pattern detection: "this API fails every Tuesday at 2am"

**Who uses it:** L3+ (Team Lead and above)

**Key features:**
- Error table with severity badges (critical/warning/info)
- Filter by severity, source, status, date
- Full error detail: stack trace, context, affected items
- Mark Resolved with resolution notes
- Stats: open errors, resolved today, avg resolution time, critical count

**Revenue enabler:** Operational reliability is non-negotiable for enterprise customers. This proves the system is monitored and maintained.

**Database entities:** `errors`, `error_resolutions`, `error_patterns`

---

### MODULE 4: KNOWLEDGE LIBRARY (The Stomach)

> **Killer benefit:** "90% of the value from AI conversations evaporates in chat histories. Enterprise OS captures it all — extracts the 29 types of value, routes it to the right place, and makes it searchable forever."

---

#### SCREEN LIB_A: Ingestion Inbox (`/library/inbox`)

**What it does:**
Global inbox for all incoming content. Drag-and-drop upload, URL sniffer, connected data sources. Every item tracked through: Pending → Processing → Routed/Unrouted/Failed.

**Why it matters:**
- Single entry point for ALL content: documents, URLs, AI chats, Slack messages, emails
- Processing pipeline is visible — you can see what's happening to your content
- Failed items don't disappear — they show up for retry

**Who uses it:** L2+ (Individual Pro and above)

**Key features:**
- Drag-and-drop multi-file upload (PDF, Word, MD, TXT, CSV, JSON, Excel, PowerPoint)
- URL sniffer: paste URL → system fetches, parses, extracts
- Connected data sources: Google Drive, Slack, Teams, GitHub, Dropbox, email
- Status tracking per item with progress indicators
- Manual routing for unrouted items
- Scheduled fetching (RSS, sitemaps, recurring URL scraping)
- Bulk operations: route all, retry failed, delete selected
- OCR for scanned documents
- Stats: today's ingested, processed, routed, failed

**Revenue enabler:** "Plug in your existing tools and the system starts learning." This is the onboarding hook. Once data flows in, customers are retained.

**Database entities:** `ingestion_jobs`, `ingestion_logs`, `documents`, `data_sources`, `data_source_configs`

**External integrations:**
- **Google Drive** — OAuth connection, auto-sync selected folders
- **Slack** — channel monitoring, message ingestion
- **Microsoft Teams** — channel monitoring
- **GitHub** — repo/wiki ingestion
- **Dropbox** — folder sync
- **OneDrive / Box** — folder sync
- **Email** (IMAP/Gmail API) — inbox monitoring
- **RSS feeds** — scheduled fetching
- **YouTube** — transcript ingestion
- **Notion** — page/database sync
- **Confluence** — space sync

---

#### SCREEN LIB_B: Artifact Extraction View (`/library/extract/:id`)

**What it does:**
Split-screen: raw source document (left) with highlighted extraction zones, 29 artifact type tabs (right) showing what was extracted. Review, edit, approve, route.

**Why it matters:**
- The EKX-1 methodology: systematic extraction of ALL value from any content
- 29 artifact types means nothing is missed: frameworks, SOPs, decisions, code snippets, market intel, hooks, UI specs, database schemas, and 21 more
- Confidence scoring prevents low-quality extractions from polluting the knowledge base

**Who uses it:** L3+ (Team Lead and above)

**Key features:**
- Raw source with highlighted extraction zones
- 29 artifact type tabs (only active types shown)
- Per-artifact: extracted text, confidence score, suggested pillar, edit, route
- Source-to-artifact linking (click artifact → highlights source section)
- Re-extract with different parameters
- Approve all or individual routing
- Extraction stats: artifacts found, by type, confidence average

**Revenue enabler:** "We don't just store your documents — we decompose them into 29 types of actionable intelligence." This is the core IP. No competitor does systematic multi-type extraction.

**Database entities:** `extraction_jobs`, `extracted_artifacts`, `artifact_confidence_scores`

---

#### SCREEN LIB_C: Promotion Console (`/library/promote`)

**What it does:**
Quality gate for promoting content from Staging (🟡) to Canonical (🟢). Review queue with diff views, quality scores, and batch operations.

**Why it matters:**
- Canonical = Source of Truth. AI agents read ONLY from Canonical.
- This screen is the firewall between raw AI output and trusted institutional knowledge.
- Quality scoring (AI-assessed) helps prioritise review.

**Who uses it:** L4+ (Department Head and above)

**Key features:**
- Promotion queue with AI quality scores (high/medium/low)
- Diff against current canonical (if updating)
- Promote to Canonical / Reject with reason
- Batch operations
- Filter by pillar, type, quality, date

**Revenue enabler:** S>C>E governance is Enterprise OS's competitive moat. "AI generates chaos; we govern it."

**Database entities:** `staging_items`, `canonical_items`, `promotion_logs`

---

#### SCREEN LIB_D: Semantic Search (`/library/search`)

**What it does:**
Natural language search across all knowledge. AI-generated answer with citations at the top, followed by ranked results with facets. Hybrid search: semantic (meaning) + keyword (exact match).

**Why it matters:**
- "Find the thing" in seconds, not hours
- AI-generated answers with citations — not just links, but actual answers with proof
- Faceted search by pillar, type, date, S>C>E state — the filters competitors don't have

**Who uses it:** L1+ (everyone)

**Key features:**
- Natural language queries
- AI-generated answer card with inline citations [1][2]
- Confidence badge on AI answer
- Ranked results with relevance scores
- Facets: pillar, type, date, S>C>E state, source
- View modes: by relevance, by date, by pillar
- Search history with recent queries
- Saved searches
- Voice search option

**Revenue enabler:** "Ask your organisation anything." This is the demo screen. It sells Enterprise OS in 30 seconds.

**Database entities:** `queries`, `query_results`, `query_feedback`, `saved_searches`

**External integrations:**
- **Elasticsearch** — hybrid search backend
- **pgvector** — vector similarity search
- **OpenAI/Cohere** — embedding models

---

#### SCREEN LIB_E: Pipeline Health Monitor (`/library/health`)

**What it does:**
Real-time status of the 5-stage metabolic pipeline (Capture → Extract → Classify → Store → Index). Queue sizes, processing rates, error counts, connected source status.

**Why it matters:**
- Ingestion is the heartbeat of the system — if it stops, knowledge stops flowing
- Immediate visibility into bottlenecks and failures
- Source connectivity monitoring (is the Slack integration still working?)

**Who uses it:** L4+ (Department Head and above)

**Key features:**
- 5-stage pipeline visualisation with live queue sizes
- Active jobs table with progress and ETA
- Throughput chart (items/hour, items/day)
- Error rate by stage
- Source status cards (connected, synced, errors)

**Revenue enabler:** Operational transparency. Enterprise customers need proof the system is running correctly 24/7.

**Database entities:** `pipeline_stages`, `pipeline_metrics`, `data_source_status`

---

### MODULE 5: TEMPLATE HUB (The DNA)

> **Killer benefit:** "If a process is mastered once, it's never reinvented. Push-button start for any task, ensuring standardised excellence at scale."

---

#### SCREEN TPL_A: Template Catalogue (`/templates/browse`)

**What it does:**
Searchable grid of all templates: Agent profiles, prompt chains, SOPs, project scaffolds, frameworks, schemas, wizards. Use count and favourites for quick access.

**Why it matters:**
- New hires produce at expert level on Day 1 (using proven templates)
- Consistency across the organisation — everyone uses the same frameworks
- Template usage tracking shows what's actually valuable

**Who uses it:** L1+ (everyone)

**Key features:**
- Template cards with type badge, description, use count
- Category tabs: Agents, Prompts, SOPs, Scaffolds, Frameworks, Schemas, Wizards
- Search and favourites
- Most popular section
- Template detail with parameters, preview, version history

**Revenue enabler:** "Encode your best practices. Scale them instantly." Template libraries are how consulting firms charge £2,000/day.

**Database entities:** `templates`, `template_categories`, `template_usage`, `template_favourites`

---

#### SCREEN TPL_B: Dynamic Document Generator (`/templates/generate`)

**What it does:**
3-step wizard: select blueprint → fill parameters → AI generates high-fidelity document. Optional Brand DNA injection and multi-role perspective inclusion.

**Why it matters:**
- A PRD, SOP, or client brief that used to take 4 hours takes 10 minutes
- Brand DNA injection ensures every document is on-brand without thinking about it
- Role perspectives built in means documents are pre-reviewed

**Who uses it:** L2+ (Individual Pro and above)

**Key features:**
- Blueprint selection from template catalogue
- Dynamic parameter forms (context-aware)
- Brand DNA auto-injection toggle
- Role perspective toggle
- AI generation with progress stages
- Preview, edit, save, and route

**Revenue enabler:** "10-minute PRDs that used to take 4 hours." Time savings quantifiable for ROI calculations.

**Database entities:** `generated_documents`, `generation_logs`

---

#### SCREEN TPL_C: Scaffold Replicator (`/templates/scaffold`)

**What it does:**
One-click deployment of standardised folder structures: 9-folder project scaffold or 16-folder domain scaffold. Includes pre-populated templates.

**Why it matters:**
- "Zero Abstraction": every project and domain uses the same structure. Learn one, navigate all.
- New projects start with architecture on Day 1, not Week 3
- Pre-populated templates (README, canon doc, routing rules) mean folders aren't empty

**Who uses it:** L4+ (Department Head and above)

**Key features:**
- Visual folder tree preview before deployment
- Configuration: name, location, included templates
- Progress tracking during deployment
- Recent deployments log

**Revenue enabler:** "Start any project with battle-tested architecture." Eliminates the chaos of ad-hoc project organisation.

**Database entities:** `scaffolds`, `scaffold_deployments`, `scaffold_templates`

---

#### SCREEN TPL_D: Prompt Chain Editor (`/templates/prompts`)

**What it does:**
Visual flow builder for multi-step AI prompt chains. Drag-and-drop nodes (Prompt, Condition, Loop, Human Review, Output) connected by data flow edges. Live test execution.

**Why it matters:**
- Complex AI workflows become visual and repeatable
- Non-technical users can build sophisticated AI pipelines
- Human-in-the-loop gates ensure quality at critical steps

**Who uses it:** L3+ (Team Lead and above)

**Key features:**
- Visual canvas with draggable node types
- Node properties: model selector, prompt, temperature, max tokens, output format
- Connector lines showing data flow
- Conditional logic nodes
- Human review gates
- Loop nodes for iterative processing
- Live test execution with streaming output per node
- Save and share chains

**Revenue enabler:** "No-code AI workflow builder." Competes with LangChain/Flowise but integrated into the platform.

**Database entities:** `prompt_chains`, `chain_nodes`, `chain_executions`, `chain_results`

---

#### SCREEN TPL_E: Brand DNA Vault (`/templates/brand`)

**What it does:**
Irreducible brand backbone: vision, mission, voice rules, unique mechanisms, colour palette, typography, tone guidelines. Read-only for most users; editable by L5+.

**Why it matters:**
- Every AI agent, every template, every generated document pulls from this vault
- Brand consistency without manual review (the AI already knows the rules)
- "Unique Mechanisms" — named proprietary frameworks that become competitive moats

**Who uses it:** L2+ (read); L5+ (edit)

**Key features:**
- Section cards: Vision, Mission, Voice Rules, Unique Mechanisms, Colours, Typography, Tone
- Colour palette with hex values
- Typography samples
- Voice rules with do's/don'ts
- Unique mechanism definitions
- Version history
- Lock indicator for read-only users

**Revenue enabler:** "Your brand, encoded into AI." Marketing teams pay premium for brand-consistent AI output.

**Database entities:** `brand_dna`, `brand_sections`, `brand_versions`

---

### MODULE 6: DOMAIN PILLARS (The Organs)

> **Killer benefit:** "23 specialist expert brains, each maintaining canonical truth for their domain. Scattered expertise becomes compounding IP."

---

#### SCREEN PIL_A: Pillar Grid (`/pillars`)

**What it does:**
Bird's-eye view of all 23 domain pillars. Each card shows item count, health score (freshness), canonical-to-staging ratio, last update. Grouped by functional area.

**Why it matters:**
- Instant view of where knowledge is strong and where it's weak
- Health scoring means stale domains get flagged before they become dangerous
- Functional grouping (Knowledge, Creation, Platform, System) maps to org structure

**Who uses it:** L2+ (Individual Pro and above)

**Key features:**
- 23 pillar cards with health indicators
- Group tabs: All, Knowledge, Creation, Platform, System
- Health legend: Green (fresh), Amber (aging), Red (stale)
- Sort by name, health, item count, last update
- Summary stats: total items, total canonical, pillars needing attention

**Revenue enabler:** "See your organisation's knowledge health at a glance." CIOs and CTOs pay for this visibility.

**Database entities:** `pillars`, `pillar_health`, `pillar_metrics`

---

#### SCREEN PIL_B: Pillar Detail / Canon Viewer (`/pillars/:id`)

**What it does:**
Deep dive into a single pillar: canonical reference document (the source of truth), 16-folder scaffold browser, recent activity, health metrics.

**Why it matters:**
- The Canon Document is what AI agents read as their primary instruction set
- 16-folder scaffold ensures every pillar is organised identically
- Recent activity shows what's changing in real-time

**Who uses it:** L1+ (read); L5+ (edit canon)

**Key features:**
- Tabs: Canon, Folders, Artifacts, Threads, Routing
- Canon document: rich text, S>C>E badge (🟢), read-only except L5+
- 16-folder scaffold browser with item counts per zone
- Recent activity feed
- Health metrics: freshness, items this week, canonical ratio

**Revenue enabler:** "Every domain has a single source of truth that AI reads." This is how Enterprise OS prevents hallucination — agents only read verified knowledge.

**Database entities:** `pillars`, `canon_documents`, `pillar_folders`, `pillar_activity`

---

#### SCREENS PIL_C, PIL_D, PIL_E

- **PIL_C: Artifact Browser** — filterable grid of all extracted artifacts in a pillar
- **PIL_D: Thread Archive** — raw AI conversation histories with full provenance
- **PIL_E: Pillar Routing Rules** — per-pillar routing configuration (same as ENG_B, scoped)

All follow the standard SB layout with filter bars, detail panels, and search.

---

### MODULE 7: BUILD FACTORY (The Kinetic Limbs)

> **Killer benefit:** "Concept to revenue in days, not months. Intelligence from pillars assembled onto standardised scaffolds. The assembly line for digital products."

---

#### SCREEN BLD_A: Project Registry (`/factory/projects`)

**What it does:**
Grid of all active projects with maturity grades: Speculative (idea), Operational (building), Production-Ready (launching). Create new projects with one-click scaffold deployment.

**Why it matters:**
- Visibility into everything being built across the org
- Maturity grades prevent scope creep — Speculative projects don't get Production resources
- One-click scaffold deployment means projects start with architecture, not a blank page

**Who uses it:** L2+ (L3+ creates projects)

**Key features:**
- Project cards with maturity badges, progress %, team avatars
- Maturity tabs: All, Speculative, Operational, Production-Ready, Archived
- Create project with auto-scaffold deployment
- Stats: total projects, in production, launched this month, blocked

**Revenue enabler:** "See everything being built. Know what stage it's at." Product managers live in this screen.

**Database entities:** `projects`, `project_maturity`, `project_teams`, `project_goals`

---

#### SCREEN BLD_B: 17-Step Mission Control (`/factory/:id/pipeline`)

**What it does:**
Linear production pipeline tracking: 17 steps across 4 tracks (Intelligence, Foundation, Brand & Creative, Build & Launch). Each step has deliverables, assignments, and completion tracking.

**Why it matters:**
- The 17-step pipeline is the operational secret sauce
- Nothing gets skipped: market analysis → keywords → architecture → design → build → test → launch
- Track view groups steps into 4 parallel workstreams

**Who uses it:** L3+ (Team Lead and above)

**Key features:**
- 17-step pipeline with status per step (not started, in progress, complete, blocked)
- 4-track view: Intelligence (1-5), Foundation (6-9), Brand & Creative (10-13), Build & Launch (14-17)
- Per-step deliverable checklists
- Timeline view (Gantt-style)
- Assignment and resource tracking

**Revenue enabler:** "The production line for digital products." This is the methodology IP — reproducible, scalable product launches.

**Database entities:** `build_stages`, `stage_deliverables`, `stage_assignments`, `stage_status`

---

#### SCREEN BLD_C: Assembly Dashboard (`/factory/:id/assemble`)

**What it does:**
Drag-and-drop assembly: snap copy frameworks, UI components, database schemas, and templates from the library onto the project scaffold.

**Why it matters:**
- Building gets FAST here. Minutes per page, not hours.
- Component reuse across projects — same button component, swap brand tokens
- Visual assembly makes it accessible to non-developers

**Who uses it:** L3+ (Team Lead and above)

**Key features:**
- Component palette: Copy, UI, Schema, Templates (searchable)
- Assembly canvas: 9-folder scaffold visualisation
- Drag components into scaffold positions
- Preview assembled page
- Undo/redo

**Revenue enabler:** "Assemble, don't build from scratch." The productivity multiplier that justifies Enterprise tier pricing.

**Database entities:** `assembly_configs`, `component_placements`, `assembly_previews`

---

#### SCREEN BLD_D: PRD Editor (`/factory/:id/prd`)

**What it does:**
Rich text PRD editor (left) with AI multi-role review panel (right). Write the spec, then send it to 5-10 AI experts for feedback before coding begins.

**Why it matters:**
- PRDs get stress-tested by multiple perspectives before a single line of code
- Reduces "we built the wrong thing" by 80%
- Version history captures PRD evolution

**Who uses it:** L3+ (Team Lead and above)

**Key features:**
- Rich text editor with section navigation
- AI multi-role review: each role provides feedback, risks, recommendations
- Accept/flag/dismiss per recommendation
- Version history
- Export as Markdown/PDF

**Revenue enabler:** "Your PRD reviewed by 10 experts in 60 seconds." Product teams pay premium for this.

**Database entities:** `prds`, `prd_versions`, `prd_reviews`, `prd_recommendations`

---

#### SCREEN BLD_E: Build Story (`/factory/:id/story`)

**What it does:**
Chronological timeline of every breakthrough, anti-pattern, milestone, and note from a project's build journey.

**Why it matters:**
- Institutional memory of HOW things get built (not just what)
- Anti-patterns prevent repeating mistakes
- Breakthroughs become templates for future projects

**Who uses it:** L2+ (Individual Pro and above)

**Key features:**
- Timeline with typed entries: breakthrough (🟢), anti-pattern (🔴), milestone (🔵), note (⚪)
- Search and filter by type
- Linked to sessions for full context
- Add entries manually

**Revenue enabler:** "Never make the same mistake twice." Learning organisations pay for institutional memory.

**Database entities:** `build_story_entries`, `entry_links`

---

### MODULE 8: OPERATIONS (The Immune System)

> **Killer benefit:** "Post-launch governance that closes the loop between strategic intent and live business results. The system tells you how the organisation is actually performing — no manual reporting."

---

#### SCREEN OPS_A: System Health Dashboard (`/ops/health`)

**What it does:**
Org heatmap: 23 pillars as coloured cells (green/amber/red for freshness). Ingestion rate, routing accuracy, active sessions, canonical ratio, error rate — all live.

**Who uses it:** L4+ (Department Head and above)

**Key features:**
- 23-pillar heatmap with drill-through
- Stat cards: ingestion rate, routing accuracy, active sessions, canonical ratio, error rate
- Ingestion chart (items/day)
- Routing accuracy over time
- Pillar freshness table with trends

---

#### SCREEN OPS_B: Strategic Goal Cascade (`/ops/goals`)

**What it does:**
Visual tree: CEO goals → Department goals → Team goals → Individual tasks. Progress auto-rolls up from task completion to strategic objectives.

**Who uses it:** L5+ (Executive and above)

**Key features:**
- Interactive goal tree with expand/collapse
- Progress rollup: company %, departments on track, at-risk goals
- Coherence Loop indicator: Know → Build → Ship → Learn
- Node detail with owner, progress, health trend

**Revenue enabler:** "Zero-effort strategic reporting." The CEO sees real progress, not status theatre.

---

#### SCREEN OPS_C: Canonisation Queue (`/ops/canon`)

Same structure as CMD_E but aggregated across ALL modules.

#### SCREEN OPS_D: Daily Digest Viewer (`/ops/digest`)

Same structure as NAV_C with additional team/org-level views for L5+.

#### SCREEN OPS_E: Whole-Org Pulse (`/ops/pulse`)

**What it does:**
Real-time activity feed: who's working on what, where. Active sessions, bottleneck alerts, stuck items. The CEO's live view of the entire organisation.

**Who uses it:** L6+ (C-Suite and above)

**Key features:**
- Live auto-scrolling feed: avatar + name + action + module + timestamp
- Active sessions panel (who, intent, duration)
- Bottleneck alerts: items stuck >24h, failed ingestions, approval backlog
- Filter by module, user, activity type

**Revenue enabler:** "Real-time organisational visibility." This is the feature CIOs buy Enterprise OS for.

---

### SHARED SCREENS

#### AUTH_A: Login (`/login`)
Split layout: form + SSO (left), brand panel (right). Email/password + Google SSO + Microsoft SSO + 2FA support.

#### AUTH_B: Register / Onboarding (`/register`)
5-step wizard: Account → Organisation → Role → Data Sources → Welcome Tour.

#### ADMIN_A: User Management (`/admin/users`)
User table with L1-L7 levels, invite workflow, bulk actions.

#### SETTINGS: Settings (`/settings`)
Profile, Notifications, Integrations, Appearance (light/dark), Security (password, 2FA).

#### SEARCH: Global Search (`/search`)
Identical to LIB_D, accessible from global topbar.

---

## 4. CROSS-CUTTING FEATURES

These features span all modules and are NOT tied to a single screen.

### 4.1 Authentication & Authorization

| Feature | Detail |
|---|---|
| Email/password login | bcrypt hashed, rate-limited |
| SSO | Google, Microsoft, Okta, Auth0, SAML |
| 2FA | TOTP (Google Authenticator, Authy) |
| 7-level permissions | L1 Freelancer → L7 CEO. Progressive data disclosure |
| Row-level security | PostgreSQL RLS policies per user/org/level |
| API keys | Per-user keys for external integrations |
| Session management | JWT with refresh tokens, 24h access / 30d refresh |
| Org switching | Users can belong to multiple orgs |

### 4.2 Notification System

| Channel | When |
|---|---|
| In-app | All events: new items routed, approvals pending, challenges, briefs ready |
| Email | Configurable per event type. Daily digest option |
| Slack | Webhook integration for team channels |
| Browser push | Critical alerts (failed ingestions, security events) |
| Mobile push | Future: mobile app notifications |

### 4.3 Activity Tracking

Every user action logged:
- Session start/end
- Content ingested/routed/promoted
- Goals created/updated
- Decisions logged
- AI interactions
- Searches performed
- Templates used

Used for: briefs, digests, rollups, analytics, audit trail.

### 4.4 Search (Universal)

- Available from every screen (Cmd+K / topbar)
- Semantic + keyword hybrid
- Results scoped by user permissions
- Recent searches and saved searches
- AI-generated answer with citations

### 4.5 S>C>E Governance (Universal)

Every content item displays its state badge:
- 🟡 **Staging** — raw, unverified, work-in-progress
- 🟢 **Canonical** — human-approved, source of truth
- 🔵 **Execution** — generated from Canonical by AI agents

AI agents read ONLY from 🟢 Canonical. This is the core governance mechanism that prevents AI chaos.

### 4.6 Real-time Updates

- WebSocket connections for live data
- Optimistic UI updates
- Presence indicators (who's online, who's in which session)
- Live collaboration on shared documents

### 4.7 Export & Import

| Format | Support |
|---|---|
| Markdown | All documents, sessions, digests |
| PDF | Reports, briefs, PRDs |
| CSV | Tables, indices, analytics |
| JSON | API responses, schemas, configurations |
| Word/PowerPoint | Future: enterprise document formats |

### 4.8 Audit Trail

Complete audit trail for compliance:
- Every promotion (Staging → Canonical) with who, when, why
- Every permission change
- Every data source connection
- Every deletion (soft delete — nothing truly destroyed)
- Exportable for compliance audits

---

## 5. API INTEGRATIONS

### 5.1 Project Management (Replaces)

| Platform | Integration Type | What Flows |
|---|---|---|
| **Monday.com** | Bidirectional API | Goals ↔ Boards, Tasks ↔ Items, Status sync |
| **Asana** | Bidirectional API | Goals ↔ Projects, Tasks ↔ Tasks, Milestones sync |
| **Jira** | Bidirectional API | Goals ↔ Epics, Build stages ↔ Sprints, Issues → Error log |
| **Linear** | Bidirectional API | Goals ↔ Projects, Tasks ↔ Issues |
| **Trello** | Import + Sync | Boards → Projects, Cards → Tasks |
| **ClickUp** | Import + Sync | Spaces → Projects, Tasks → Tasks |
| **Basecamp** | Import + Sync | Projects → Sessions, Messages → Knowledge Library |

### 5.2 Communication (Replaces)

| Platform | Integration Type | What Flows |
|---|---|---|
| **Slack** | Deep integration | Channels → Knowledge Library, Briefs → Channels, Session notifications |
| **Microsoft Teams** | Deep integration | Same as Slack |
| **Discord** | Webhook | Notifications, brief delivery |
| **Email** (Gmail/Outlook) | IMAP + API | Email → Ingestion, Briefs → Inbox, Notifications |

### 5.3 Knowledge & Documentation (Replaces)

| Platform | Integration Type | What Flows |
|---|---|---|
| **Notion** | Bidirectional API | Pages → Knowledge Library, Databases → Pillars |
| **Confluence** | Import + Sync | Spaces → Pillars, Pages → Canon documents |
| **Google Docs** | API | Docs → Knowledge Library, Shared docs → Session sources |
| **Dropbox Paper** | Import | Papers → Knowledge Library |

### 5.4 File Storage

| Platform | Integration Type | What Flows |
|---|---|---|
| **Google Drive** | OAuth + Sync | Selected folders → Ingestion, continuous monitoring |
| **Dropbox** | OAuth + Sync | Selected folders → Ingestion |
| **OneDrive** | OAuth + Sync | Selected folders → Ingestion |
| **Box** | OAuth + Sync | Selected folders → Ingestion |
| **S3/R2** | Direct | Object storage for Enterprise OS files |

### 5.5 Development

| Platform | Integration Type | What Flows |
|---|---|---|
| **GitHub** | Deep integration | Repos → Knowledge Library, Commits → Sessions, Issues → Error log, PRs → Build story |
| **GitLab** | API | Same as GitHub |
| **Bitbucket** | API | Same as GitHub |
| **Vercel** | Webhook | Deploy status → Build Factory |
| **AWS/GCP** | API | Infrastructure metrics → Operations |

### 5.6 AI & ML

| Platform | Integration Type | What Flows |
|---|---|---|
| **OpenAI (GPT-4, GPT-4o)** | API | Agent backends, extraction, generation, embeddings |
| **Anthropic (Claude)** | API | Primary agent backend, analysis, extraction |
| **Cohere** | API | Embeddings, reranking |
| **Open-source (Ollama, vLLM)** | API | Self-hosted model options |
| **Hugging Face** | API | Custom model deployment |

### 5.7 Analytics & Reporting

| Platform | Integration Type | What Flows |
|---|---|---|
| **Power BI** | Export API | Health data, goal metrics, pillar analytics |
| **Tableau** | Export API | Same as Power BI |
| **Google Analytics** | Import | Web metrics → Operations |
| **Mixpanel** | Import | Product usage → Operations |

### 5.8 CRM & Sales

| Platform | Integration Type | What Flows |
|---|---|---|
| **HubSpot** | API | Contacts → Knowledge Library, Deal stages → Build Factory |
| **Salesforce** | API | Same as HubSpot |
| **Pipedrive** | API | Same as HubSpot |

### 5.9 Payment & Billing

| Platform | Integration Type | What Flows |
|---|---|---|
| **Stripe** | API | Subscription management, usage-based billing |
| **Paddle** | API | Alternative payment processor |

---

## 6. DATABASE ARCHITECTURE

### 6.1 Core Schema

```sql
-- ============================================
-- ORGANISATIONS & USERS
-- ============================================

CREATE TABLE organizations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    slug VARCHAR(100) UNIQUE NOT NULL,
    logo_url TEXT,
    industry VARCHAR(100),
    size_range VARCHAR(50), -- '1-10', '11-50', '51-200', '201-1000', '1000+'
    subscription_tier VARCHAR(50) DEFAULT 'starter', -- starter, professional, enterprise
    stripe_customer_id VARCHAR(255),
    settings JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255),
    name VARCHAR(255) NOT NULL,
    avatar_url TEXT,
    bio TEXT,
    timezone VARCHAR(50) DEFAULT 'Europe/London',
    settings JSONB DEFAULT '{}',
    last_active TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE user_org_memberships (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    org_id UUID REFERENCES organizations(id),
    level INTEGER NOT NULL CHECK (level BETWEEN 1 AND 7), -- L1-L7
    role VARCHAR(100), -- 'CEO', 'Marketing Lead', etc.
    department VARCHAR(100),
    status VARCHAR(20) DEFAULT 'active', -- active, invited, suspended
    invited_at TIMESTAMPTZ,
    joined_at TIMESTAMPTZ,
    UNIQUE(user_id, org_id)
);

-- ============================================
-- MODULE 1: NAVIGATION CENTRE
-- ============================================

CREATE TABLE goals (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID REFERENCES organizations(id),
    created_by UUID REFERENCES users(id),
    title VARCHAR(500) NOT NULL,
    description TEXT,
    status VARCHAR(50) DEFAULT 'active', -- active, completed, archived, paused
    health_score NUMERIC(3,1) CHECK (health_score BETWEEN 0 AND 10),
    target_date DATE,
    parent_goal_id UUID REFERENCES goals(id), -- goal cascade
    template_id UUID, -- if created from template
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE goal_5a_sections (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    goal_id UUID REFERENCES goals(id) ON DELETE CASCADE,
    section_type VARCHAR(20) NOT NULL, -- alignment, awareness, accountabilities, activities, assets
    content TEXT NOT NULL,
    sort_order INTEGER DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE milestones (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    goal_id UUID REFERENCES goals(id) ON DELETE CASCADE,
    title VARCHAR(500) NOT NULL,
    target_date DATE,
    completed_at TIMESTAMPTZ,
    sort_order INTEGER DEFAULT 0
);

CREATE TABLE goal_health_history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    goal_id UUID REFERENCES goals(id),
    score NUMERIC(3,1),
    note TEXT,
    recorded_by UUID REFERENCES users(id),
    recorded_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE perspectives (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    goal_id UUID REFERENCES goals(id) ON DELETE CASCADE,
    role_profile_id UUID,
    role_name VARCHAR(100) NOT NULL,
    risks TEXT[],
    opportunities TEXT[],
    recommendations TEXT[],
    generated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE decisions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID REFERENCES organizations(id),
    goal_id UUID REFERENCES goals(id),
    session_id UUID, -- linked session
    title VARCHAR(500) NOT NULL,
    rationale TEXT NOT NULL,
    decision_type VARCHAR(50), -- pivot, commitment, cancellation, adjustment
    before_state TEXT,
    after_state TEXT,
    made_by UUID REFERENCES users(id),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE challenges (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID REFERENCES organizations(id),
    goal_id UUID REFERENCES goals(id),
    title VARCHAR(500) NOT NULL,
    description TEXT NOT NULL,
    severity VARCHAR(20) NOT NULL, -- critical, warning, info
    status VARCHAR(20) DEFAULT 'active', -- active, resolved, snoozed, dismissed
    snoozed_until TIMESTAMPTZ,
    response TEXT,
    resolved_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE state_snapshots (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID REFERENCES organizations(id),
    alignment_score NUMERIC(3,1),
    risk_items JSONB DEFAULT '[]',
    resource_allocations JSONB DEFAULT '{}',
    key_metrics JSONB DEFAULT '{}',
    ai_commentary TEXT,
    snapshot_date DATE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(org_id, snapshot_date)
);

CREATE TABLE briefs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID REFERENCES organizations(id),
    user_id UUID REFERENCES users(id),
    brief_date DATE NOT NULL,
    content JSONB NOT NULL, -- {yesterdays_wins, top_3, blockers, team_activity, strategic_note}
    generated_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(org_id, user_id, brief_date)
);

-- ============================================
-- MODULE 2: COMMAND DECK
-- ============================================

CREATE TABLE sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID REFERENCES organizations(id),
    user_id UUID REFERENCES users(id),
    intent TEXT NOT NULL,
    goal_id UUID REFERENCES goals(id),
    status VARCHAR(20) DEFAULT 'active', -- active, paused, ended
    started_at TIMESTAMPTZ DEFAULT NOW(),
    ended_at TIMESTAMPTZ,
    duration_seconds INTEGER,
    auto_digest TEXT,
    digest_approved BOOLEAN DEFAULT FALSE
);

CREATE TABLE session_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID REFERENCES sessions(id) ON DELETE CASCADE,
    event_type VARCHAR(50) NOT NULL, -- work, decision, output, note, milestone, ai_message, user_message
    content TEXT NOT NULL,
    metadata JSONB DEFAULT '{}', -- {source_url, output_path, output_type, agent_id}
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE session_sources (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID REFERENCES sessions(id) ON DELETE CASCADE,
    source_type VARCHAR(50), -- url, file, ai_thread, slack_message
    source_url TEXT,
    source_name VARCHAR(500),
    added_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE agent_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID, -- NULL = system default
    name VARCHAR(100) NOT NULL,
    avatar_url TEXT,
    category VARCHAR(50), -- knowledge, creation, platform, system, custom
    description TEXT,
    expertise TEXT[],
    system_prompt TEXT,
    tools TEXT[], -- available tools/integrations
    is_custom BOOLEAN DEFAULT FALSE,
    created_by UUID REFERENCES users(id),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE agent_activations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID REFERENCES sessions(id),
    agent_id UUID REFERENCES agent_profiles(id),
    activated_at TIMESTAMPTZ DEFAULT NOW(),
    deactivated_at TIMESTAMPTZ
);

-- ============================================
-- MODULE 3: CORE ENGINE
-- ============================================

CREATE TABLE routing_rules (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID REFERENCES organizations(id),
    pillar_id UUID REFERENCES pillars(id),
    keywords TEXT[] NOT NULL,
    keyword_weights JSONB DEFAULT '{}', -- {keyword: weight}
    threshold NUMERIC(5,2) DEFAULT 0.5,
    use_llm_fallback BOOLEAN DEFAULT TRUE,
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE routing_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID REFERENCES organizations(id),
    document_id UUID,
    content_snippet TEXT,
    matched_pillar_id UUID REFERENCES pillars(id),
    score NUMERIC(5,3),
    method VARCHAR(20), -- keyword, llm, manual
    routed_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================
-- MODULE 4: KNOWLEDGE LIBRARY
-- ============================================

CREATE TABLE data_sources (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID REFERENCES organizations(id),
    source_type VARCHAR(50) NOT NULL, -- google_drive, slack, github, upload, url, email
    name VARCHAR(255) NOT NULL,
    config JSONB DEFAULT '{}', -- OAuth tokens, folder IDs, channel IDs, etc.
    status VARCHAR(20) DEFAULT 'active', -- active, paused, error, disconnected
    last_sync TIMESTAMPTZ,
    error_message TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID REFERENCES organizations(id),
    data_source_id UUID REFERENCES data_sources(id),
    pillar_id UUID REFERENCES pillars(id),
    title VARCHAR(500) NOT NULL,
    content TEXT,
    content_type VARCHAR(50), -- pdf, word, markdown, url, ai_chat, slack, email
    sce_state VARCHAR(20) DEFAULT 'staging', -- staging, canonical, execution
    file_url TEXT,
    file_size INTEGER,
    word_count INTEGER,
    metadata JSONB DEFAULT '{}', -- {author, original_date, source_url, tags}
    ingested_at TIMESTAMPTZ DEFAULT NOW(),
    promoted_at TIMESTAMPTZ,
    promoted_by UUID REFERENCES users(id)
);

CREATE TABLE document_chunks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    document_id UUID REFERENCES documents(id) ON DELETE CASCADE,
    chunk_index INTEGER NOT NULL,
    content TEXT NOT NULL,
    token_count INTEGER,
    embedding vector(1536), -- pgvector
    metadata JSONB DEFAULT '{}'
);

CREATE TABLE ingestion_jobs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID REFERENCES organizations(id),
    document_id UUID REFERENCES documents(id),
    status VARCHAR(20) DEFAULT 'pending', -- pending, processing, completed, failed
    stage VARCHAR(50), -- parsing, chunking, embedding, classifying, routing
    progress NUMERIC(5,2) DEFAULT 0,
    error_message TEXT,
    started_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE extracted_artifacts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    document_id UUID REFERENCES documents(id),
    artifact_type VARCHAR(50) NOT NULL, -- framework, sop, decision, code_snippet, market_intel, hook, ui_spec, etc.
    content TEXT NOT NULL,
    confidence NUMERIC(3,2) CHECK (confidence BETWEEN 0 AND 1),
    pillar_id UUID REFERENCES pillars(id),
    sce_state VARCHAR(20) DEFAULT 'staging',
    source_highlight JSONB, -- {start_offset, end_offset} in original doc
    extracted_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE queries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID REFERENCES organizations(id),
    user_id UUID REFERENCES users(id),
    query_text TEXT NOT NULL,
    query_type VARCHAR(20), -- semantic, keyword, hybrid
    ai_answer TEXT,
    ai_confidence NUMERIC(3,2),
    citations JSONB DEFAULT '[]',
    result_count INTEGER,
    latency_ms INTEGER,
    user_feedback INTEGER CHECK (user_feedback BETWEEN 1 AND 5),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================
-- MODULE 5: TEMPLATE HUB
-- ============================================

CREATE TABLE templates (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID, -- NULL = system default
    name VARCHAR(255) NOT NULL,
    category VARCHAR(50), -- agent, prompt, sop, scaffold, framework, schema, wizard
    description TEXT,
    content TEXT NOT NULL, -- template content with {{parameters}}
    parameters JSONB DEFAULT '[]', -- [{name, type, required, default, options}]
    use_count INTEGER DEFAULT 0,
    version INTEGER DEFAULT 1,
    created_by UUID REFERENCES users(id),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE prompt_chains (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID REFERENCES organizations(id),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    nodes JSONB NOT NULL, -- [{id, type, prompt, model, config, position}]
    edges JSONB NOT NULL, -- [{source, target, data_mapping}]
    created_by UUID REFERENCES users(id),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE brand_dna (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID REFERENCES organizations(id) UNIQUE,
    vision TEXT,
    mission TEXT,
    voice_rules JSONB, -- {dos: [], donts: [], tone_examples: []}
    unique_mechanisms JSONB, -- [{name, description}]
    colour_palette JSONB, -- [{name, hex, usage}]
    typography JSONB, -- [{font, usage, sizes}]
    version INTEGER DEFAULT 1,
    updated_by UUID REFERENCES users(id),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================
-- MODULE 6: DOMAIN PILLARS
-- ============================================

CREATE TABLE pillars (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID REFERENCES organizations(id),
    code VARCHAR(20) NOT NULL, -- PIL_01 through PIL_23
    name VARCHAR(100) NOT NULL,
    description TEXT,
    functional_group VARCHAR(50), -- knowledge, creation, platform, system
    health_score NUMERIC(3,1),
    item_count INTEGER DEFAULT 0,
    canonical_count INTEGER DEFAULT 0,
    last_activity TIMESTAMPTZ,
    canon_document TEXT, -- the canonical reference doc
    UNIQUE(org_id, code)
);

CREATE TABLE pillar_health_history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pillar_id UUID REFERENCES pillars(id),
    score NUMERIC(3,1),
    items_added INTEGER DEFAULT 0,
    items_promoted INTEGER DEFAULT 0,
    recorded_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================
-- MODULE 7: BUILD FACTORY
-- ============================================

CREATE TABLE projects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID REFERENCES organizations(id),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    maturity VARCHAR(50) DEFAULT 'speculative', -- speculative, operational, production_ready, archived
    goal_id UUID REFERENCES goals(id),
    progress NUMERIC(5,2) DEFAULT 0,
    scaffold_deployed BOOLEAN DEFAULT FALSE,
    created_by UUID REFERENCES users(id),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE build_stages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id UUID REFERENCES projects(id) ON DELETE CASCADE,
    stage_number INTEGER NOT NULL CHECK (stage_number BETWEEN 1 AND 17),
    track INTEGER NOT NULL CHECK (track BETWEEN 1 AND 4), -- intelligence, foundation, brand_creative, build_launch
    name VARCHAR(255) NOT NULL,
    status VARCHAR(20) DEFAULT 'not_started', -- not_started, in_progress, complete, blocked
    assigned_to UUID REFERENCES users(id),
    completion NUMERIC(5,2) DEFAULT 0,
    started_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    UNIQUE(project_id, stage_number)
);

CREATE TABLE stage_deliverables (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    stage_id UUID REFERENCES build_stages(id) ON DELETE CASCADE,
    title VARCHAR(500) NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    completed_at TIMESTAMPTZ,
    sort_order INTEGER DEFAULT 0
);

CREATE TABLE build_story_entries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id UUID REFERENCES projects(id),
    entry_type VARCHAR(20) NOT NULL, -- breakthrough, anti_pattern, milestone, note
    title VARCHAR(500) NOT NULL,
    description TEXT,
    session_id UUID REFERENCES sessions(id),
    created_by UUID REFERENCES users(id),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE prds (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id UUID REFERENCES projects(id),
    content TEXT NOT NULL,
    version INTEGER DEFAULT 1,
    reviews JSONB DEFAULT '[]', -- [{role, feedback, risks, recommendations, timestamp}]
    updated_by UUID REFERENCES users(id),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================
-- MODULE 8: OPERATIONS
-- ============================================

CREATE TABLE ops_metrics (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID REFERENCES organizations(id),
    metric_date DATE NOT NULL,
    ingestion_count INTEGER DEFAULT 0,
    routing_accuracy NUMERIC(5,2),
    active_sessions INTEGER DEFAULT 0,
    canonical_ratio NUMERIC(5,2),
    error_count INTEGER DEFAULT 0,
    UNIQUE(org_id, metric_date)
);

CREATE TABLE errors (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID REFERENCES organizations(id),
    source VARCHAR(100), -- script, api, routing, ingestion
    severity VARCHAR(20), -- critical, warning, info
    message TEXT NOT NULL,
    stack_trace TEXT,
    context JSONB DEFAULT '{}',
    status VARCHAR(20) DEFAULT 'open', -- open, resolved
    resolution_notes TEXT,
    resolved_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================
-- GOVERNANCE & AUDIT
-- ============================================

CREATE TABLE promotion_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID REFERENCES organizations(id),
    document_id UUID REFERENCES documents(id),
    from_state VARCHAR(20) NOT NULL,
    to_state VARCHAR(20) NOT NULL,
    promoted_by UUID REFERENCES users(id),
    reason TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE audit_trail (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID REFERENCES organizations(id),
    user_id UUID REFERENCES users(id),
    action VARCHAR(100) NOT NULL,
    entity_type VARCHAR(50),
    entity_id UUID,
    details JSONB DEFAULT '{}',
    ip_address INET,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE notifications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID REFERENCES organizations(id),
    user_id UUID REFERENCES users(id),
    type VARCHAR(50) NOT NULL, -- approval_pending, brief_ready, challenge_new, ingestion_complete, etc.
    title VARCHAR(500) NOT NULL,
    body TEXT,
    link VARCHAR(500),
    read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================================
-- INDEXES
-- ============================================

CREATE INDEX idx_documents_org_pillar ON documents(org_id, pillar_id);
CREATE INDEX idx_documents_sce_state ON documents(sce_state);
CREATE INDEX idx_document_chunks_embedding ON document_chunks USING ivfflat (embedding vector_cosine_ops);
CREATE INDEX idx_sessions_org_user ON sessions(org_id, user_id);
CREATE INDEX idx_session_events_session ON session_events(session_id);
CREATE INDEX idx_goals_org ON goals(org_id);
CREATE INDEX idx_routing_logs_org ON routing_logs(org_id);
CREATE INDEX idx_audit_trail_org ON audit_trail(org_id, created_at);
CREATE INDEX idx_notifications_user ON notifications(user_id, read);
CREATE INDEX idx_extracted_artifacts_doc ON extracted_artifacts(document_id);
CREATE INDEX idx_ingestion_jobs_status ON ingestion_jobs(status);
```

### 6.2 Entity Relationship Summary

```
organizations ─┬─ users (via memberships, L1-L7)
               ├─ goals ──┬── 5a_sections
               │          ├── milestones
               │          ├── perspectives
               │          ├── decisions
               │          ├── challenges
               │          └── health_history
               ├─ sessions ──┬── session_events
               │             ├── session_sources
               │             └── agent_activations
               ├─ pillars ──┬── documents ──┬── document_chunks (+ embeddings)
               │            │              └── extracted_artifacts
               │            ├── health_history
               │            └── routing_rules
               ├─ data_sources ── ingestion_jobs
               ├─ templates
               ├─ prompt_chains
               ├─ brand_dna
               ├─ projects ──┬── build_stages ── deliverables
               │             ├── prds
               │             └── build_story_entries
               ├─ state_snapshots
               ├─ briefs
               ├─ ops_metrics
               ├─ errors
               ├─ notifications
               └─ audit_trail
```

### 6.3 Table Count: ~35 core tables

---

## 7. TECHNICAL ARCHITECTURE

### 7.1 System Stack

| Layer | Technology | Rationale |
|---|---|---|
| **Frontend** | Next.js 16 + React 19 + Tailwind CSS v4 | SSR, app router, fast, proven at scale |
| **UI Components** | Custom library (Brainwave base + Anima conversions) | Pixel-perfect to Figma designs |
| **State Management** | React Server Components + Zustand (client) | Minimal client JS, fast page loads |
| **API** | Next.js API routes + tRPC | Type-safe, co-located with frontend |
| **Database** | PostgreSQL 16 + pgvector | Relational + vector in one DB, no extra infra |
| **Cache** | Redis | Session state, job queues, real-time |
| **Object Storage** | S3 / Cloudflare R2 | File uploads, generated assets |
| **Search** | pgvector + pg_trgm | Start simple, add Elasticsearch when needed |
| **Job Queue** | BullMQ (Redis) | Ingestion pipeline, extraction, briefs |
| **WebSocket** | Socket.io | Real-time feed, presence, live updates |
| **Auth** | NextAuth.js v5 | SSO, JWT, session management |
| **LLM** | Claude API (primary) + OpenAI (secondary) | Multi-LLM, no vendor lock |
| **Embeddings** | OpenAI text-embedding-3-small | 1536 dimensions, cost-efficient |
| **Hosting** | Vercel (frontend) + Railway/Fly.io (API/DB) | Simple deployment, auto-scaling |
| **CI/CD** | GitHub Actions | Automated testing and deployment |
| **Monitoring** | Sentry (errors) + Posthog (analytics) | Error tracking + product analytics |

### 7.2 Infrastructure Cost Estimate (Monthly)

| Service | Starter (10 users) | Professional (50 users) | Enterprise (200+ users) |
|---|---|---|---|
| Vercel | Free | £20 | £150 |
| Database (Railway) | £5 | £25 | £100 |
| Redis | £0 (included) | £10 | £30 |
| Object Storage | £1 | £10 | £50 |
| LLM API (Claude/OpenAI) | £50 | £200 | £1,000 |
| Embedding API | £10 | £50 | £200 |
| Monitoring | Free | £30 | £100 |
| **TOTAL** | **~£70/mo** | **~£345/mo** | **~£1,630/mo** |
| **Revenue** | **£99/mo** | **£499/mo** | **£2,000+/mo** |
| **Margin** | **29%** | **31%** | **18%+** |

---

## 8. PRICING MODEL

| Tier | Price | Users | Documents | Modules | LLM | Support |
|---|---|---|---|---|---|---|
| **Starter** | £99/mo | 10 | 10,000 | Nav + Command + Knowledge | Standard (GPT-3.5 + Claude Haiku) | Community |
| **Professional** | £499/mo | 50 | 100,000 | All 8 modules | Premium (GPT-4 + Claude Sonnet) | Email |
| **Enterprise** | £2,000+/mo | Unlimited | Unlimited | All + custom agents + SSO | All models + custom fine-tuning | Dedicated |

### Usage-Based Add-Ons
- Additional LLM credits: £0.01-0.05 per query beyond tier limit
- Additional storage: £5 per 10GB
- Custom model fine-tuning: £500+ setup
- Priority processing: £100/mo

### Implementation Services
- Custom onboarding: £2,000-10,000
- Data migration: £5,000-50,000
- Custom agent development: £2,000-20,000
- Training workshops: £1,000/day

---

## 9. GO-TO-MARKET

### Phase 1: Internal Dogfood (Now - Month 3)
- Build V7 as the internal backbone
- Property Connect, Fitness, LeadEngine through the Build Factory
- Validate all 8 modules through daily use
- **Exit criteria:** All 8 modules working, 3+ platforms built through the factory

### Phase 2: MVP & Beta (Months 4-6)
- Nav + Command + Knowledge as SaaS (3-module Starter)
- Beta with 10 friendly companies (agencies, consultancies)
- Iterate based on feedback
- **Exit criteria:** 10 beta customers, <5% daily churn, NPS 50+

### Phase 3: Product Launch (Months 7-9)
- All 8 modules live
- Public Starter tier
- Content marketing: blog, case studies, YouTube
- **Exit criteria:** 50 paying customers, £5K MRR

### Phase 4: Scale (Months 10-18)
- Professional and Enterprise tiers
- Agent orchestration, knowledge graph
- Sales team (3-5 people)
- **Exit criteria:** 200 customers, £2M ARR

### Phase 5: Aggressive Growth (Year 2-3)
- 1,000 SMB/Pro clients at £6K-£24K/year
- 200 enterprise clients at £100K+/year
- Strategic partnerships, industry-specific solutions
- Multiple deployment options (cloud, on-prem, hybrid)
- **Exit criteria:** £20M+ ARR, acquisition conversations at £100M+ valuation

---

## 10. COMPETITIVE DIFFERENTIATION

| Feature | Enterprise OS | Notion AI | Glean | Monday.com |
|---|---|---|---|---|
| 8-module architecture | ✅ | ❌ | ❌ | ❌ |
| S>C>E governance | ✅ | ❌ | ❌ | ❌ |
| 29 artifact extraction | ✅ | ❌ | ❌ | ❌ |
| 80+ role AI agents | ✅ | ❌ | ❌ | ❌ |
| Multi-LLM | ✅ | ❌ | ✅ | ❌ |
| 7-level permissions | ✅ | ❌ | ✅ | Partial |
| Goal cascade | ✅ | ❌ | ❌ | Partial |
| Build factory | ✅ | ❌ | ❌ | ❌ |
| Knowledge graph | ✅ | ❌ | ✅ | ❌ |
| Proactive AI challenges | ✅ | ❌ | ❌ | ❌ |

---

## 11. SUCCESS METRICS

### Month 6
- Internal V7 fully operational (all 8 modules active)
- 3+ platforms built through Build Factory
- 10 beta customers
- <3s query latency
- 90%+ routing accuracy

### Month 12
- 50 paying customers
- £500K ARR
- Agent orchestration live
- Knowledge graph functional
- NPS 50+, <5% monthly churn

### Month 24
- 1,000+ SMB/Pro clients + 200 enterprise clients
- £20M+ ARR
- Enterprise features complete
- Strategic partnerships established
- Acquisition conversations at £100M+ valuation

---

## 12. SCREEN COUNT SUMMARY

| Section | Screens | States | Modals |
|---|---|---|---|
| Hub | 1 | 10 | 3 |
| Navigation Centre | 7 | 30 | 7 |
| Command Deck | 5 | 24 | 9 |
| Core Engine | 5 | 19 | 2 |
| Knowledge Library | 5 | 24 | 4 |
| Template Hub | 5 | 19 | 0 |
| Domain Pillars | 5 | 14 | 0 |
| Build Factory | 5 | 18 | 2 |
| Operations | 5 | 14 | 0 |
| Shared/Global | 5 | 16 | 2 |
| **TOTAL** | **48** | **188** | **29** |

---

## 13. BUILD PRIORITY

### Sprint 1 (Week 1-2): Foundation
- [ ] Database schema deployed (all 35 tables)
- [ ] Auth system (NextAuth.js v5 + L1-L7 levels)
- [ ] AppShell (Brainwave sidebar + topbar)
- [ ] Hub screen (HUB.default)
- [ ] Settings screen (SETTINGS.profile)

### Sprint 2 (Week 3-4): Command Deck + Knowledge
- [ ] Active Cockpit (CMD_A) — the core workspace
- [ ] Session History (CMD_B)
- [ ] Ingestion Inbox (LIB_A) — file upload + URL sniffer
- [ ] Semantic Search (LIB_D)
- [ ] Agent Registry (CMD_D) — 80+ role profiles

### Sprint 3 (Week 5-6): Navigation + Governance
- [ ] Goal Intake Wizard (NAV_A)
- [ ] Goal Health Dashboard (NAV_D)
- [ ] Morning Brief (NAV_C)
- [ ] Approval Queue (CMD_E)
- [ ] Universal Index (ENG_A)

### Sprint 4 (Week 7-8): Build Factory + Operations
- [ ] Project Registry (BLD_A)
- [ ] 17-Step Mission Control (BLD_B)
- [ ] System Health Dashboard (OPS_A)
- [ ] Org Pulse (OPS_E)
- [ ] Pillar Grid (PIL_A) + Detail (PIL_B)

### Sprint 5 (Week 9-10): Advanced Features
- [ ] Artifact Extraction (LIB_B)
- [ ] Prompt Chain Editor (TPL_D)
- [ ] Assembly Dashboard (BLD_C)
- [ ] PRD Editor (BLD_D)
- [ ] AI Challenge Console (NAV_F)
- [ ] Role Perspectives (NAV_B)

### Sprint 6 (Week 11-12): Polish & Integrations
- [ ] External integrations (Slack, Google Drive, GitHub)
- [ ] Real-time WebSocket feeds
- [ ] Email delivery (briefs, notifications)
- [ ] Brand DNA Vault (TPL_E)
- [ ] Template Catalogue (TPL_A)
- [ ] Performance optimisation, testing, deployment

---

**END OF COMPLETE BUILD SPECIFICATION**

**This document is the single source of truth for building Enterprise OS V7.**
**All implementation decisions reference this spec.**
**Last Updated:** 2026-02-17
