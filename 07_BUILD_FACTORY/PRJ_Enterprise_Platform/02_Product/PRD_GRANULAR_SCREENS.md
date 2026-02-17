# Enterprise OS V7 — Granular Screen Specification

> **Version:** 1.0
> **Date:** 2026-02-16
> **Purpose:** Every screen, every state, every modal, every tab — down to component level.
> **Source:** PRD_Enterprise_OS_V7_MASTER.md, SCREEN_INVENTORY.md, Google Notebook summaries (8 reports + 3 PDFs)
> **Goal:** Feed directly into UI Assembly Pipeline for automated component matching

---

## Conventions

**State notation:** `[screen_id].[state]` — e.g., `HUB.loading`, `NAV_A.step_2`
**Modal notation:** `[screen_id].modal.[name]` — e.g., `CMD_A.modal.end_session`
**Permission badge:** `L1`–`L7` (who can see this)
**S>C>E badges:** 🟡 Staging | 🟢 Canonical | 🔵 Execution — visible on all content items
**Layout codes:** `SB` = sidebar_content, `SP` = split, `CT` = centered, `FC` = full_canvas, `GR` = grid

---

## SCREEN 0: THE HUB (Home Screen)

**Route:** `/`
**Layout:** `SB` (sidebar collapsed) → responsive grid
**Permission:** All levels (L1–L7), content adapts per level

### States

| State | Description |
|-------|-------------|
| `HUB.default` | Main view — 8 module tiles in 2x4 grid, Morning Brief card, quick actions |
| `HUB.loading` | Skeleton loaders for tiles and brief |
| `HUB.first_login` | Onboarding overlay — guided tour of 8 modules |
| `HUB.l1_view` | Freelancer: assigned tasks list + relevant templates only |
| `HUB.l2_view` | Pro: sessions, outputs, today's priorities |
| `HUB.l3_view` | Team Lead: + team activity feed |
| `HUB.l4_view` | Dept Head: + pillar health cards |
| `HUB.l5_view` | Executive: + build milestones, resource gaps |
| `HUB.l6_view` | C-Suite: + KPI pulse, MRR widget |
| `HUB.l7_view` | CEO: + Org Pulse feed, State Snapshot, AI Challenge alerts |

### Components

| Component | Type | Details |
|-----------|------|---------|
| Module Tile (×8) | `card` | Icon, module name, health indicator (green/amber/red dot), key metric number, click → module tab |
| Morning Brief Card | `card` | "Good morning, [Name]" header, yesterday's wins (bulleted), today's top 3 priorities, generated timestamp |
| Quick Action Bar | `button_group` | "Start Session", "Search", "Ingest Content", "View Goals" |
| Org Pulse Feed (L5+) | `feed` | Live activity stream — avatar + name + action + timestamp, auto-scrolling |
| State Snapshot (L7) | `card` | Strategic alignment score (1-10), key risk summary, auto-generated daily |
| AI Challenge Alert | `notification` | Orange badge count on Hub, expandable to show stale task warnings |
| Sidebar Nav | `sidebar` | Collapsed by default on Hub, 8 module icons + home icon, expand on hover |
| Topbar | `topbar` | Logo (left), global search (centre), notification bell, user avatar (right) |

### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `HUB.modal.quick_start_session` | "Start Session" button | Intent input field, goal selector dropdown, "Begin" button |
| `HUB.modal.notifications` | Bell icon click | List of notifications: new approvals, completed ingestions, challenge alerts. Mark read/unread |
| `HUB.modal.user_menu` | Avatar click | Profile link, Settings link, Switch workspace, Logout |

---

## TAB 1: NAVIGATION CENTRE (The Brain)

---

### SCREEN NAV_A: Goal Intake Wizard

**Route:** `/nav/goals/new`
**Layout:** `CT` → multi-step wizard
**Permission:** L2+

#### States

| State | Description |
|-------|-------------|
| `NAV_A.step_1` | Intent Capture — large textarea "What do you want to achieve?", freeform, voice-to-text option |
| `NAV_A.step_2` | AI Refinement — AI asks clarifying questions (chat-style), user responds, intent gets sharper |
| `NAV_A.step_3` | 5A Breakdown — AI generates: Alignment (vision), Awareness (risks), Accountabilities (owners), Activities (rhythm), Assets (resources). User edits each |
| `NAV_A.step_4` | Timeline & Milestones — Calendar picker, milestone cards, dependency linking |
| `NAV_A.step_5` | Review & Confirm — Summary card of full goal. "Create Goal" CTA |
| `NAV_A.ai_thinking` | AI processing animation (spinner + "Analyzing your intent...") |
| `NAV_A.completed` | Success state — goal created, redirect option to Goal Health Dashboard |
| `NAV_A.error` | API failure — retry button, save draft option |
| `NAV_A.draft_saved` | Auto-save indicator — "Draft saved" toast |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Step Progress Bar | `progress` | top | 5 steps, current highlighted, completed steps have checkmarks |
| Intent Textarea | `textarea` | centre | Large, auto-expanding, placeholder text, character count |
| Voice Input Button | `button` | beside textarea | Microphone icon, toggles voice-to-text |
| AI Chat Thread | `chat` | centre (step 2) | AI messages left-aligned, user messages right-aligned, typing indicator |
| 5A Cards (×5) | `card` | centre (step 3) | Editable title + body, colour-coded per A, expand/collapse |
| Milestone Timeline | `timeline` | centre (step 4) | Vertical timeline, add milestone (+), drag to reorder, date pickers |
| Summary Card | `card` | centre (step 5) | Read-only formatted goal with all 5A sections |
| Navigation Buttons | `button_group` | bottom | "Back", "Next" / "Create Goal", "Save Draft" |
| AI Suggestion Chips | `chip` | inline | Suggested tags, categories, related goals — click to accept |

#### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `NAV_A.modal.discard_draft` | "Back" on step 1 with content | "Discard this draft?" — Discard / Save Draft |
| `NAV_A.modal.link_existing_goal` | Step 4 dependency | Search existing goals, click to link as dependency |

---

### SCREEN NAV_B: Role-Informed Perspective Panel

**Route:** `/nav/goals/:id/perspectives`
**Layout:** `SB`
**Permission:** L3+ (L5+ sees full Think Tank)

#### States

| State | Description |
|-------|-------------|
| `NAV_B.default` | Goal summary (top), perspective cards below in grid (3-col) |
| `NAV_B.generating` | AI generating perspectives — skeleton cards with shimmer |
| `NAV_B.expanded_role` | One perspective expanded full-width, others collapsed |
| `NAV_B.add_role` | Dropdown to request additional role perspective |
| `NAV_B.empty` | No perspectives yet — "Generate Perspectives" CTA |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Goal Summary Banner | `card` | top | Goal title, health score, 5A status indicators |
| Role Perspective Card (×N) | `card` | main grid | Avatar icon + role name (header), risk flags (badges), opportunities (bulleted), recommended actions, expand/collapse |
| Add Role Button | `button` | top-right | "+ Add Perspective" → dropdown of 80+ roles |
| Risk Summary Bar | `badge_group` | below banner | Aggregated risk count across all perspectives: Critical (red), Warning (amber), Info (blue) |
| Sidebar Nav | `sidebar` | left | Module navigation, current goal context |
| Action Panel | `card` | right sidebar | "Accept recommendation", "Flag for review", "Dismiss" per perspective |

#### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `NAV_B.modal.role_detail` | Click role avatar | Full role profile: name, responsibilities, expertise areas, typical concerns |
| `NAV_B.modal.create_task` | "Accept recommendation" | Pre-filled task from recommendation, assign owner, set due date |

---

### SCREEN NAV_C: Morning Brief

**Route:** `/nav/brief`
**Layout:** `CT` (single-column readable)
**Permission:** L1+

#### States

| State | Description |
|-------|-------------|
| `NAV_C.default` | Today's brief — newspaper-style layout |
| `NAV_C.loading` | Skeleton with brief structure |
| `NAV_C.generating` | "Preparing your brief..." — AI synthesis in progress |
| `NAV_C.historical` | Viewing past brief (date picker active) |
| `NAV_C.empty` | First day, no data yet — "Your first brief will appear tomorrow" |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Date Header | `text` | top | "Monday, 17 February 2026" + "Generated at 6:00 AM" |
| Yesterday's Wins Section | `card` | top section | Green-accented, bulleted list of completed items |
| Today's Top 3 | `card` | middle section | Numbered priority list with goal links, estimated effort |
| Blockers & Risks | `card` | middle section | Amber-accented, items needing attention |
| Team Activity Summary (L3+) | `card` | lower section | Team members' session completions, outputs |
| Strategic Alignment Note (L5+) | `card` | lower section | How today's priorities connect to 90-day goals |
| Date Picker | `dropdown` | top-right | View any previous brief |
| Print / Export | `button` | top-right | PDF export or print |

---

### SCREEN NAV_D: Goal Health Dashboard

**Route:** `/nav/dashboard`
**Layout:** `SB`
**Permission:** L3+

#### States

| State | Description |
|-------|-------------|
| `NAV_D.default` | Grid of goal cards with health scores |
| `NAV_D.loading` | Skeleton goal cards |
| `NAV_D.heatmap_view` | Toggle to heatmap visualisation (colour grid) |
| `NAV_D.list_view` | Toggle to table/list of goals |
| `NAV_D.filtered` | Active filter applied (by owner, department, status) |
| `NAV_D.goal_detail` | Expanded single goal panel (right side) |
| `NAV_D.empty` | No goals — "Create your first goal" CTA |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| View Toggle | `tabs` | top | "Cards" / "Heatmap" / "List" |
| Filter Bar | `dropdown_group` | top | Owner, Department, Status, Time Range |
| Goal Card (×N) | `card` | main grid | Title, health score (1-10 with colour), owner avatar, progress bar, 5A mini-indicators, last activity date |
| Health Score Legend | `badge_group` | top-right | 8-10 Green, 5-7 Amber, 1-4 Red |
| Heatmap Grid | `grid` | main (heatmap view) | Goals as coloured cells, size = importance, colour = health |
| Goal Detail Panel | `card` | right panel (expanded) | Full 5A breakdown, decision log excerpt, linked tasks, health trend chart |
| Summary Stats | `stat_cards` | top | Total goals, Average health, At-risk count, Completed this month |
| Sidebar Nav | `sidebar` | left | Module navigation |

#### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `NAV_D.modal.goal_actions` | Right-click / kebab on goal card | "Edit", "Archive", "Generate Perspectives", "View History" |
| `NAV_D.modal.quick_update` | "Update" button on goal card | Health score slider, brief note field, "Save" |

---

### SCREEN NAV_E: Decision & Iteration Log

**Route:** `/nav/decisions`
**Layout:** `SB`
**Permission:** L3+

#### States

| State | Description |
|-------|-------------|
| `NAV_E.default` | Timeline view of all decisions, most recent first |
| `NAV_E.filtered` | Filtered by goal, date range, or decision type |
| `NAV_E.detail` | Expanded decision entry (right panel) |
| `NAV_E.compare` | Side-by-side comparison of two iterations |
| `NAV_E.loading` | Skeleton timeline |
| `NAV_E.empty` | No decisions — "Decisions will be logged as you work" |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Decision Timeline | `timeline` | main | Vertical timeline: date markers, decision cards, iteration nodes |
| Decision Card (×N) | `card` | in timeline | Decision title, rationale text, related goal badge, author avatar, timestamp, before/after summary |
| Filter Bar | `dropdown_group` | top | Goal, Date Range, Type (pivot/commitment/cancellation), Author |
| Search | `search_bar` | top | Full-text search across decisions |
| Detail Panel | `card` | right | Full decision: context, rationale, impact assessment, linked artifacts |
| Compare View | `split` | main (compare mode) | Two decisions side-by-side, diffs highlighted |
| Stats Summary | `stat_cards` | top | Total decisions, Pivots this month, Average time-to-decision |
| Sidebar Nav | `sidebar` | left | Module navigation |

---

### SCREEN NAV_F: AI Challenge Console

**Route:** `/nav/challenges`
**Layout:** `SP` (chat left, context right)
**Permission:** L5+

#### States

| State | Description |
|-------|-------------|
| `NAV_F.default` | Active challenges list (left), selected challenge detail (right) |
| `NAV_F.chat_mode` | AI dialogue — conversational challenge/response |
| `NAV_F.resolved` | Viewing resolved challenges (historical) |
| `NAV_F.empty` | No active challenges — "Your system is healthy" |
| `NAV_F.loading` | AI analysing system for new challenges |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Challenge List | `card_list` | left panel | Priority-sorted: each card has challenge title, age, severity badge (critical/warning/info), related goal |
| Challenge Detail | `card` | right panel | Full description, AI's reasoning, suggested actions, data evidence |
| Action Buttons | `button_group` | right panel bottom | "Accept & Create Task", "Dismiss", "Snooze 7 days", "Respond to AI" |
| AI Chat | `chat` | right panel (chat mode) | Dialogue between user and AI about the challenge |
| Severity Filter | `tabs` | top | "All" / "Critical" / "Warning" / "Info" |
| Challenge Count Badge | `badge` | tab header | Number of unresolved challenges |
| Sidebar Nav | `sidebar` | left | Module navigation |

#### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `NAV_F.modal.create_task` | "Accept & Create Task" | Pre-filled task: title, description, suggested owner, due date |
| `NAV_F.modal.snooze` | "Snooze" | Duration picker: 1 day, 3 days, 7 days, custom |

---

### SCREEN NAV_G: State Snapshot (NEW — from Notebook analysis)

**Route:** `/nav/state`
**Layout:** `CT`
**Permission:** L6+

#### States

| State | Description |
|-------|-------------|
| `NAV_G.default` | Current state: AI-refreshed daily summary of "what is true right now" |
| `NAV_G.historical` | Past snapshot selected via date picker |
| `NAV_G.generating` | AI refreshing the state — progress indicator |
| `NAV_G.diff_view` | Comparing today's state vs. previous date |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| State Header | `text` | top | "System State — [date]", last refresh time |
| Strategic Alignment Score | `stat_card` | top | 1-10 score, trend arrow, breakdown by 5A dimension |
| Active Goals Summary | `card` | main | Table: goal name, health, owner, last activity |
| Risk Register | `card` | main | Flagged items: stale goals, blocked tasks, alignment drift |
| Resource Allocation | `card` | main | Who's working on what, utilisation % |
| Key Metrics Row | `stat_cards` | top | Sessions today, Artifacts produced, Promotions pending, Routing accuracy |
| Date Picker | `dropdown` | top-right | Historical snapshots |
| Compare Button | `button` | top-right | "Compare with..." → opens diff view |
| AI Commentary | `card` | bottom | AI's interpretation of the state, recommended actions |

---

## TAB 2: COMMAND DECK (The Hands)

---

### SCREEN CMD_A: Active Cockpit

**Route:** `/cmd/session`
**Layout:** `SP` (three-pane: log | chat | outputs)
**Permission:** L1+

#### States

| State | Description |
|-------|-------------|
| `CMD_A.no_session` | No active session — "Start Session" CTA with intent field |
| `CMD_A.active` | Session running: three-pane layout active |
| `CMD_A.paused` | Session paused — timer stopped, resume button |
| `CMD_A.ending` | Auto-synthesis in progress — AI generating summary |
| `CMD_A.ended` | Session complete — summary view, "Start New" option |
| `CMD_A.loading` | Resuming previous session |

#### Components — Three-Pane Layout

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| **LEFT PANE: Running Log** | | | |
| Session Header | `card` | top-left | Intent statement, timer, goal link, session ID |
| Log Entry (×N) | `card` | left scroll | Timestamp, entry type badge (work/decision/output/note/milestone), message, source link |
| Add Entry Buttons | `button_group` | left bottom | "Note", "Decision", "Milestone", "Output" |
| **MIDDLE PANE: AI Chat** | | | |
| Chat Messages | `chat` | middle scroll | AI and user messages, code blocks, embedded files |
| Chat Input | `textarea` | middle bottom | Message input, attach file, send button |
| Agent Selector | `dropdown` | middle top | Active agent role (default: General, switch to SEO Lead, etc.) |
| **RIGHT PANE: Outputs** | | | |
| Output Cards (×N) | `card` | right scroll | Generated artifacts: type badge, preview, "Route to Pillar" button |
| Source Links | `card` | right | Input sources used this session: URLs, thread links, file references |
| Session Stats | `stat_cards` | right bottom | Duration, entries count, outputs count, AI calls |

#### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `CMD_A.modal.start_session` | "Start Session" CTA | Intent textarea, goal selector, agent picker, "Begin" button |
| `CMD_A.modal.end_session` | "End Session" button | Confirm, AI generates summary preview, edit summary, "Save & Close" |
| `CMD_A.modal.route_output` | "Route to Pillar" on output card | Pillar selector, S>C>E state picker, confirm routing |
| `CMD_A.modal.add_source` | "Add Source" | URL input, platform dropdown (ChatGPT/Claude/GitHub/etc.), thread name |
| `CMD_A.modal.switch_agent` | Agent selector click | Grid of 80+ role profiles, search, select to activate |

---

### SCREEN CMD_B: Session History

**Route:** `/cmd/sessions`
**Layout:** `SB`
**Permission:** L1+ (L3+ sees team sessions)

#### States

| State | Description |
|-------|-------------|
| `CMD_B.default` | Table of past sessions, most recent first |
| `CMD_B.filtered` | Filtered by date, goal, user (L3+) |
| `CMD_B.detail` | Expanded session in right panel |
| `CMD_B.loading` | Skeleton table |
| `CMD_B.empty` | No sessions yet — "Start your first session" |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Session Table | `table` | main | Columns: Date, Intent, Duration, Entries, Outputs, Goal, Owner (L3+) |
| Filter Bar | `dropdown_group` | top | Date range, Goal, User (L3+), Has outputs |
| Search | `search_bar` | top | Search session content |
| Session Detail Panel | `card` | right | Full session: auto-digest, log entries, outputs list, source links |
| Pagination | `pagination` | bottom | Page through sessions |
| Export Button | `button` | top-right | Export session as Markdown/PDF |
| Sidebar Nav | `sidebar` | left | Module navigation |

---

### SCREEN CMD_C: Auto-Digest Generation

**Route:** `/cmd/digests`
**Layout:** `SP` (raw log left, polished digest right)
**Permission:** L3+

#### States

| State | Description |
|-------|-------------|
| `CMD_C.default` | List of sessions awaiting digest |
| `CMD_C.generating` | AI transforming selected session log → digest |
| `CMD_C.review` | Split view: raw (left) vs. digest (right) |
| `CMD_C.editing` | Editing the generated digest |
| `CMD_C.approved` | Digest approved and saved |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Session Selector | `table` | left (default) or top | Pick session to digest |
| Raw Log View | `text` | left pane (split) | Scrollable raw session log with timestamps |
| Digest Preview | `card` | right pane (split) | AI-generated polished summary: key decisions, outputs, next steps |
| Edit Button | `button` | right pane top | Toggle edit mode on digest |
| Digest Editor | `textarea` | right pane (editing) | Rich text editor for the digest |
| Approve Button | `button` | right pane bottom | "Approve & Route" — saves and routes to relevant stakeholders |
| Regenerate Button | `button` | right pane top | "Regenerate" — ask AI to redo the digest |

---

### SCREEN CMD_D: Agent Registry

**Route:** `/cmd/agents`
**Layout:** `SB`
**Permission:** L2+

#### States

| State | Description |
|-------|-------------|
| `CMD_D.default` | Grid of agent cards, searchable |
| `CMD_D.filtered` | Filtered by category (Knowledge/Creation/Platform/System) |
| `CMD_D.detail` | Selected agent expanded — full profile |
| `CMD_D.creating` | Creating custom agent (L4+) |
| `CMD_D.loading` | Skeleton grid |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Agent Card (×80+) | `card` | main grid | Avatar, role name, specialisation, "Activate" button |
| Category Tabs | `tabs` | top | "All" / "Knowledge" / "Creation" / "Platform" / "System" / "Custom" |
| Search | `search_bar` | top | Search by name or expertise |
| Agent Detail Panel | `card` | right (expanded) | Full profile: responsibilities, tools, expertise, example prompts, activation history |
| Create Agent Button (L4+) | `button` | top-right | "+ Custom Agent" |
| Most Used Section | `card_row` | top of grid | Top 5 most-activated agents |
| Sidebar Nav | `sidebar` | left | Module navigation |

#### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `CMD_D.modal.create_agent` | "+ Custom Agent" | Name, avatar, role description, expertise areas, tools, system prompt |
| `CMD_D.modal.activate` | "Activate" on agent card | Confirm activation for current session, option to set as default |

---

### SCREEN CMD_E: Approval & Governance Queue

**Route:** `/cmd/approvals`
**Layout:** `SB`
**Permission:** L4+

#### States

| State | Description |
|-------|-------------|
| `CMD_E.default` | Queue of items pending promotion (Staging → Canonical) |
| `CMD_E.filtered` | Filtered by pillar, type, submitter |
| `CMD_E.reviewing` | Single item expanded for review |
| `CMD_E.empty` | No pending approvals — "All caught up" |
| `CMD_E.bulk_mode` | Multi-select for batch approve/reject |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Queue Table | `table` | main | Columns: Item, Type, Source Pillar, Submitter, Date, S>C>E badge (always 🟡), Preview |
| Filter Bar | `dropdown_group` | top | Pillar, Type, Date range, Submitter |
| Review Panel | `card` | right (expanded) | Full content preview, source provenance, diff against existing canonical (if updating) |
| Action Buttons | `button_group` | review panel bottom | "Promote to Canonical" (green), "Reject" (red), "Request Changes" (amber), "Skip" |
| Bulk Select | `checkbox` | table rows | Select multiple, batch approve/reject |
| Stats Bar | `stat_cards` | top | Pending, Approved today, Rejected today, Average review time |
| Sidebar Nav | `sidebar` | left | Module navigation |

#### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `CMD_E.modal.reject_reason` | "Reject" | Reason textarea, "Reject & Notify" button |
| `CMD_E.modal.request_changes` | "Request Changes" | Feedback textarea, specific change requests, "Send Back" |
| `CMD_E.modal.bulk_confirm` | Bulk approve/reject | "You are about to [approve/reject] N items. Confirm?" |

---

## TAB 3: CORE ENGINE (The Nervous System)

---

### SCREEN ENG_A: Universal Index

**Route:** `/engine/index`
**Layout:** `SB`
**Permission:** L2+

#### States

| State | Description |
|-------|-------------|
| `ENG_A.default` | Full data table of all system files/artifacts |
| `ENG_A.filtered` | Active filters applied |
| `ENG_A.detail` | Selected item expanded in right panel |
| `ENG_A.loading` | Skeleton table |
| `ENG_A.empty` | No items — shouldn't happen in production |
| `ENG_A.bulk_actions` | Multi-select mode for batch operations |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Data Table | `table` | main | Columns: Name, Type, Pillar, S>C>E State (badge), Size, Created, Modified, Provenance Source, Tags |
| Column Sort | `sort` | table headers | Click to sort by any column |
| Filter Bar | `dropdown_group` | top | Pillar, Type (29 artifact types), S>C>E state, Date range, Tags |
| Search | `search_bar` | top | Full-text + semantic search |
| Item Detail Panel | `card` | right | Full metadata, preview, provenance chain, routing history |
| Epoch Counts | `stat_cards` | top | Total items, By state (Staging/Canonical/Execution), By pillar |
| Export | `button` | top-right | CSV, JSON export |
| Bulk Actions Bar | `button_group` | bottom (bulk mode) | "Route Selected", "Tag Selected", "Export Selected" |
| Pagination | `pagination` | bottom | Page through items |
| Sidebar Nav | `sidebar` | left | Module navigation |

---

### SCREEN ENG_B: Routing Rules Editor

**Route:** `/engine/routing`
**Layout:** `SB`
**Permission:** L4+

#### States

| State | Description |
|-------|-------------|
| `ENG_B.default` | List of routing rules by pillar |
| `ENG_B.editing` | Editing a specific rule set |
| `ENG_B.testing` | Test mode — paste content, see where it would route |
| `ENG_B.logs` | View routing logs/history |
| `ENG_B.loading` | Loading rules |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Pillar Rule List | `table` | main | Each pillar: name, keyword count, threshold score, fallback setting, last modified |
| Rule Editor | `form` | right panel | Keywords (tag input), weight sliders, threshold number, LLM fallback toggle, test button |
| Test Panel | `card` | right panel (test mode) | Textarea for content, "Route" button, shows: matched pillars with scores |
| Routing Logs | `table` | main (logs tab) | Recent routing decisions: content snippet, matched pillar, score, timestamp |
| View Tabs | `tabs` | top | "Rules" / "Test" / "Logs" |
| Save Button | `button` | right panel bottom | "Save Rules" |
| Sidebar Nav | `sidebar` | left | Module navigation |

#### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `ENG_B.modal.add_keywords` | "Add Keywords" in rule editor | Bulk keyword input, paste or type, auto-deduplicate |
| `ENG_B.modal.discard_changes` | Navigate away with unsaved changes | "Discard changes?" — Discard / Save |

---

### SCREEN ENG_C: RAG Quality Dashboard

**Route:** `/engine/rag`
**Layout:** `SB`
**Permission:** L4+

#### States

| State | Description |
|-------|-------------|
| `ENG_C.default` | Charts and metrics overview |
| `ENG_C.filtered` | Filtered by pillar, date range |
| `ENG_C.detail` | Drill into specific metric |
| `ENG_C.loading` | Skeleton charts |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Stat Cards Row | `stat_cards` | top | Total chunks, Avg chunk size, Total embeddings, Index health %, Query latency P50/P95 |
| Chunking Efficiency Chart | `chart` | main | Bar chart: chunk size distribution |
| Embedding Coverage Chart | `chart` | main | Pillar coverage: % of documents embedded per pillar |
| Query Performance Chart | `chart` | main | Line chart: latency over time, queries per day |
| Retrieval Quality Table | `table` | main | Recent queries: query, top results, relevance score, user feedback |
| Filter Bar | `dropdown_group` | top | Pillar, Date range |
| Sidebar Nav | `sidebar` | left | Module navigation |

---

### SCREEN ENG_D: Schema & Data Model Library

**Route:** `/engine/schemas`
**Layout:** `SB`
**Permission:** L3+

#### States

| State | Description |
|-------|-------------|
| `ENG_D.default` | Grid of schema cards |
| `ENG_D.detail` | Selected schema: full definition view |
| `ENG_D.editing` | Editing a schema (L5+) |
| `ENG_D.loading` | Skeleton grid |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Schema Card (×N) | `card` | main grid | Name, type (PostgreSQL/JSON/API), table count, last modified, S>C>E badge |
| Search | `search_bar` | top | Search schemas by name or table |
| Category Tabs | `tabs` | top | "All" / "PostgreSQL" / "JSON" / "API" |
| Schema Viewer | `card` | right panel | Full schema: tables, columns, relationships, ERD diagram (if available) |
| Code Block | `code` | in viewer | Syntax-highlighted SQL/JSON |
| Copy Button | `button` | viewer top-right | Copy schema to clipboard |
| Use in Project Button | `button` | viewer bottom | "Use in Project" → picks project from Build Factory |
| Sidebar Nav | `sidebar` | left | Module navigation |

---

### SCREEN ENG_E: Error Library & Failure Log

**Route:** `/engine/errors`
**Layout:** `SB`
**Permission:** L3+

#### States

| State | Description |
|-------|-------------|
| `ENG_E.default` | Table of errors/failures, most recent first |
| `ENG_E.filtered` | Filtered by severity, source, date |
| `ENG_E.detail` | Selected error expanded |
| `ENG_E.resolved` | Viewing resolved errors |
| `ENG_E.loading` | Skeleton table |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Error Table | `table` | main | Columns: Timestamp, Source (script/API/routing), Severity badge (critical/warning/info), Message, Status (open/resolved) |
| Filter Bar | `dropdown_group` | top | Severity, Source, Status, Date range |
| Error Detail Panel | `card` | right | Full error: stack trace, context, affected items, resolution notes |
| Status Tabs | `tabs` | top | "Open" / "Resolved" / "All" |
| Resolve Button | `button` | detail panel | "Mark Resolved" + resolution notes |
| Stats Bar | `stat_cards` | top | Open errors, Resolved today, Avg resolution time, Critical count |
| Sidebar Nav | `sidebar` | left | Module navigation |

---

## TAB 4: KNOWLEDGE LIBRARY (The Stomach)

---

### SCREEN LIB_A: Ingestion Inbox

**Route:** `/library/inbox`
**Layout:** `SB`
**Permission:** L2+

#### States

| State | Description |
|-------|-------------|
| `LIB_A.default` | Inbox table: all ingestion items |
| `LIB_A.filtered` | Filtered by status, source type, date |
| `LIB_A.processing` | Items actively being processed — progress indicators |
| `LIB_A.detail` | Selected item expanded |
| `LIB_A.uploading` | File upload in progress |
| `LIB_A.empty` | No items — "Start ingesting content" CTA |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Inbox Table | `table` | main | Columns: Name, Source Type badge (PDF/URL/AI Chat/etc.), Status (pending/processing/routed/unrouted/failed), Pillar (if routed), Date, Size |
| Status Tabs | `tabs` | top | "All" / "Pending" / "Processing" / "Routed" / "Unrouted" / "Failed" |
| Upload Area | `dropzone` | top | Drag-and-drop + "Browse" button, accepts: PDF, Word, MD, TXT, CSV, JSON |
| URL Sniffer Input | `input` | top | "Paste URL to ingest" + "Fetch" button |
| Filter Bar | `dropdown_group` | below tabs | Source type, Date range, Pillar |
| Item Detail Panel | `card` | right | Full metadata, content preview, extracted artifacts preview, routing suggestion |
| Processing Progress | `progress` | in table row | For items currently being processed |
| Retry Button | `button` | failed items | "Retry Ingestion" |
| Bulk Actions | `button_group` | bottom (multi-select) | "Route All", "Retry Failed", "Delete Selected" |
| Stats Bar | `stat_cards` | top | Today: ingested, processed, routed, failed |
| Sidebar Nav | `sidebar` | left | Module navigation |

#### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `LIB_A.modal.manual_route` | "Route" on unrouted item | Pillar selector, S>C>E state, confirm |
| `LIB_A.modal.url_options` | URL Sniffer "Fetch" | Depth setting (page only / follow links), schedule recurring, confirm |
| `LIB_A.modal.connect_source` | "Connect Source" button | Source type grid (Google Drive, Slack, GitHub, etc.), OAuth flow |

---

### SCREEN LIB_B: Artifact Extraction View

**Route:** `/library/extract/:id`
**Layout:** `SP` (raw source left, extracted artifacts right)
**Permission:** L3+

#### States

| State | Description |
|-------|-------------|
| `LIB_B.default` | Split view with raw source and 29 artifact type tabs |
| `LIB_B.extracting` | AI extraction in progress — shimmer on right panel |
| `LIB_B.reviewing` | Extraction complete, user reviewing results |
| `LIB_B.editing` | User editing an extracted artifact |
| `LIB_B.approved` | Artifacts approved and routed |
| `LIB_B.loading` | Loading source document |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Raw Source View | `text` | left pane | Scrollable raw document with highlighting of extracted sections |
| Artifact Type Tabs | `tabs` | right pane top | 29 types: Frameworks, SOPs, Decisions, Code, Market Intel, Hooks, UI Specs, etc. — only tabs with found artifacts are active |
| Artifact Card (×N) | `card` | right pane | Per artifact: type badge, extracted text, confidence score, edit button |
| Source Highlight Link | `link` | in artifact card | Click to highlight corresponding section in raw source |
| Extraction Stats | `stat_cards` | right pane top | Artifacts found, By type breakdown, Confidence average |
| Approve All Button | `button` | right pane bottom | "Approve & Route All" |
| Individual Route Button | `button` | per artifact card | "Route to [suggested pillar]" |
| Edit Button | `button` | per artifact card | Inline edit of extracted content |
| Re-Extract Button | `button` | right pane top | "Re-Extract" — run AI again |

#### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `LIB_B.modal.route_artifact` | "Route" on artifact | Pillar selector (pre-filled with suggestion), S>C>E state, confirm |
| `LIB_B.modal.edit_artifact` | "Edit" on artifact | Rich text editor for artifact content, save |

---

### SCREEN LIB_C: Promotion Console

**Route:** `/library/promote`
**Layout:** `SB`
**Permission:** L4+

#### States

| State | Description |
|-------|-------------|
| `LIB_C.default` | Queue of Staging items pending promotion |
| `LIB_C.reviewing` | Single item review with diff view |
| `LIB_C.empty` | No items pending — "All promoted" |
| `LIB_C.bulk_mode` | Multi-select for batch operations |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Promotion Queue | `table` | main | Items in Staging: name, type, pillar, author, date, quality score |
| Review Panel | `card` | right | Full content, diff against current canonical (if exists), provenance |
| Promote Button | `button` | review panel | 🟡→🟢 "Promote to Canonical" |
| Reject Button | `button` | review panel | "Reject" with reason |
| Quality Score | `badge` | per item | AI-assessed quality (high/medium/low) |
| Filter Bar | `dropdown_group` | top | Pillar, Type, Quality score, Date |
| Sidebar Nav | `sidebar` | left | Module navigation |

---

### SCREEN LIB_D: Semantic Search

**Route:** `/library/search`
**Layout:** `CT` → `SB` (results view)
**Permission:** L1+

#### States

| State | Description |
|-------|-------------|
| `LIB_D.empty` | Search landing — large search bar, suggested queries |
| `LIB_D.searching` | AI processing query — loading indicator |
| `LIB_D.results` | Results displayed with facets |
| `LIB_D.detail` | Expanded result in right panel |
| `LIB_D.no_results` | No matches — suggested alternative queries |
| `LIB_D.ai_answer` | AI-generated answer with citations at top of results |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Search Bar | `search_bar` | top (centre) | Large input, "Search all knowledge" placeholder, voice option |
| AI Answer Card | `card` | top of results | AI-generated answer with inline citations [1][2], confidence badge |
| Result Cards (×N) | `card` | results list | Title, snippet with highlights, source pillar badge, S>C>E badge, relevance score, date |
| Facet Sidebar | `sidebar` | left (results) | Pillar filter, Type filter, Date range, S>C>E state, Source |
| View Modes | `tabs` | results top | "Relevance" / "Recent" / "By Pillar" |
| Result Detail Panel | `card` | right | Full document preview, provenance, related items |
| Suggested Queries | `chip_group` | below search (empty state) | Clickable suggested searches |
| Search History | `dropdown` | search bar | Recent searches on focus |
| Pagination | `pagination` | results bottom | Page through results |

---

### SCREEN LIB_E: Pipeline Health Monitor

**Route:** `/library/health`
**Layout:** `SB`
**Permission:** L4+

#### States

| State | Description |
|-------|-------------|
| `LIB_E.default` | Real-time pipeline status |
| `LIB_E.detail` | Drill into specific pipeline stage |
| `LIB_E.historical` | Historical throughput view |
| `LIB_E.loading` | Skeleton dashboard |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Pipeline Stages | `progress_pipeline` | main | 5 stages (Capture→Extract→Classify→Store→Index) — each shows: queue size, processing rate, error count |
| Active Jobs Table | `table` | main | Currently processing: name, stage, progress %, started, ETA |
| Throughput Chart | `chart` | main | Line chart: items processed per hour/day |
| Error Rate Chart | `chart` | main | Error % by stage over time |
| Source Status Cards | `stat_cards` | main | Connected sources: Google Drive (✓ synced), Slack (⚠ 2 errors), GitHub (✓ synced), etc. |
| Stats Bar | `stat_cards` | top | Items in queue, Processing now, Completed today, Failed today |
| Sidebar Nav | `sidebar` | left | Module navigation |

---

## TAB 5: TEMPLATE HUB (The DNA)

---

### SCREEN TPL_A: Template Catalogue

**Route:** `/templates/browse`
**Layout:** `SB`
**Permission:** L1+

#### States

| State | Description |
|-------|-------------|
| `TPL_A.default` | Grid of template cards |
| `TPL_A.filtered` | Filtered by category, type |
| `TPL_A.detail` | Selected template expanded |
| `TPL_A.loading` | Skeleton grid |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Template Card (×N) | `card` | main grid | Icon, name, type badge, description, use count, "Use" button |
| Category Tabs | `tabs` | top | "All" / "Agents" / "Prompts" / "SOPs" / "Scaffolds" / "Frameworks" / "Schemas" / "Wizards" |
| Search | `search_bar` | top | Search templates |
| Template Detail Panel | `card` | right | Full description, parameters, preview, usage history, version |
| Use Button | `button` | detail panel | "Use Template" → starts generation |
| Favourite Button | `button` | card/detail | Star to favourite |
| Most Popular Section | `card_row` | top of grid | Top 5 most-used templates |
| Sidebar Nav | `sidebar` | left | Module navigation |

---

### SCREEN TPL_B: Dynamic Document Generator

**Route:** `/templates/generate`
**Layout:** `CT` → multi-step wizard
**Permission:** L2+

#### States

| State | Description |
|-------|-------------|
| `TPL_B.select` | Step 1: Choose template blueprint |
| `TPL_B.configure` | Step 2: Fill parameters |
| `TPL_B.generating` | AI assembling document |
| `TPL_B.preview` | Step 3: Preview generated document |
| `TPL_B.editing` | Editing generated content |
| `TPL_B.saved` | Document saved and routed |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Blueprint Selector | `card_grid` | step 1 | Available blueprints with descriptions |
| Parameter Form | `form` | step 2 | Dynamic fields based on template: text inputs, dropdowns, toggles, date pickers |
| Brand DNA Injection | `toggle` | step 2 | "Apply Brand DNA" — auto-injects voice rules, unique mechanisms |
| Role Perspective Toggle | `toggle` | step 2 | "Include role perspectives" — adds multi-role input |
| AI Generation Progress | `progress` | step 3 | "Generating... Step 2/4" with stage descriptions |
| Document Preview | `card` | step 3 | Rich text preview of generated document |
| Edit Button | `button` | preview | "Edit" → opens rich text editor |
| Save & Route | `button` | preview bottom | Save to pillar, choose S>C>E state |
| Step Progress Bar | `progress` | top | 3 steps: Select → Configure → Generate |

---

### SCREEN TPL_C: Scaffold Replicator

**Route:** `/templates/scaffold`
**Layout:** `SB`
**Permission:** L4+

#### States

| State | Description |
|-------|-------------|
| `TPL_C.default` | Available scaffolds: 9-folder (project) and 16-folder (pillar) |
| `TPL_C.configuring` | Setting up scaffold parameters |
| `TPL_C.deploying` | Creating folder structure |
| `TPL_C.complete` | Scaffold deployed — link to new structure |
| `TPL_C.error` | Deployment failed — retry option |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Scaffold Cards (×2+) | `card` | main | "9-Folder Project Scaffold" and "16-Folder Domain Scaffold" — description, folder tree preview, "Deploy" |
| Folder Tree Preview | `tree` | card/detail | Visual folder hierarchy |
| Configuration Form | `form` | right panel | Name, parent location, included templates (checkboxes), permissions |
| Deploy Button | `button` | form bottom | "Deploy Scaffold" |
| Progress | `progress` | deploying state | "Creating folders... 7/9 complete" |
| Recent Deployments | `table` | bottom | Last 10 scaffolds deployed: name, type, date, location |
| Sidebar Nav | `sidebar` | left | Module navigation |

---

### SCREEN TPL_D: Prompt Chain Editor

**Route:** `/templates/prompts`
**Layout:** `FC` (full canvas) with sidebar
**Permission:** L3+

#### States

| State | Description |
|-------|-------------|
| `TPL_D.default` | List/grid of saved prompt chains |
| `TPL_D.editing` | Canvas view: visual flow builder |
| `TPL_D.testing` | Running a chain — live output |
| `TPL_D.loading` | Loading chain |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Chain List | `card_grid` | main (default) | Saved chains: name, step count, last run, "Edit" / "Run" buttons |
| Canvas | `canvas` | main (editing) | Visual flow: nodes (prompts) connected by edges (data flow), drag to arrange |
| Node (×N) | `card` | on canvas | Prompt step: model selector, prompt text, input variables, output mapping |
| Connector Lines | `line` | canvas | Data flow between nodes |
| Properties Panel | `form` | right sidebar | Selected node properties: prompt, model, temperature, max tokens, output format |
| Node Palette | `card_list` | left sidebar | Draggable node types: "Prompt", "Condition", "Loop", "Human Review", "Output" |
| Run Button | `button` | top-right | "Run Chain" — executes with live output |
| Output Panel | `card` | bottom (testing) | Live streaming output from each node |
| Save Button | `button` | top-right | "Save Chain" |

---

### SCREEN TPL_E: Brand DNA Vault

**Route:** `/templates/brand`
**Layout:** `SB` → detail view
**Permission:** L2+

#### States

| State | Description |
|-------|-------------|
| `TPL_E.default` | Brand DNA sections as cards/accordion |
| `TPL_E.editing` | Editing brand DNA (L5+ only) |
| `TPL_E.locked` | Read-only view for L2-L4 |
| `TPL_E.loading` | Loading brand assets |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Brand Section Cards | `card` | main | Sections: Vision, Mission, Voice Rules, Unique Mechanisms, Colour Palette, Typography, Tone Guidelines |
| Colour Palette Display | `card` | in sections | Colour swatches with hex values: #0B8C00 primary, #49ba61 alt |
| Typography Display | `card` | in sections | Font samples: Inter (apps), DM Sans (website) |
| Voice Rules | `card` | in sections | Do's and Don'ts, tone examples |
| Unique Mechanisms | `card` | in sections | Named frameworks and their descriptions |
| Edit Button (L5+) | `button` | per section | "Edit" — toggles to form view |
| Lock Indicator (L2-L4) | `badge` | per section | "Read Only" |
| Version History | `button` | top-right | View previous versions of brand DNA |
| Sidebar Nav | `sidebar` | left | Module navigation |

---

## TAB 6: DOMAIN PILLARS (The Organs)

---

### SCREEN PIL_A: Pillar Grid

**Route:** `/pillars`
**Layout:** `SB`
**Permission:** L2+

#### States

| State | Description |
|-------|-------------|
| `PIL_A.default` | Grid of 23 pillar cards |
| `PIL_A.grouped` | Grouped by functional area (Knowledge/Creation/Platform/System) |
| `PIL_A.loading` | Skeleton grid |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Pillar Card (×23) | `card` | main grid | Pillar name, icon, item count, health score (freshness), Canonical vs Staging ratio bar, last update, click → pillar detail |
| Group Tabs | `tabs` | top | "All" / "Knowledge" / "Creation" / "Platform" / "System" |
| Health Legend | `badge_group` | top-right | Green (fresh), Amber (aging), Red (stale) |
| Summary Stats | `stat_cards` | top | Total items, Total canonical, Pillars needing attention, Items processed today |
| Sort Options | `dropdown` | top | Sort by: Name, Health, Item count, Last update |
| Sidebar Nav | `sidebar` | left | Module navigation |

---

### SCREEN PIL_B: Pillar Detail / Canon Viewer

**Route:** `/pillars/:id`
**Layout:** `SB`
**Permission:** L1+

#### States

| State | Description |
|-------|-------------|
| `PIL_B.default` | Pillar overview with 16-folder scaffold and canon document |
| `PIL_B.canon` | Reading the canonical reference document |
| `PIL_B.folders` | Browsing the 16-folder scaffold |
| `PIL_B.loading` | Loading pillar data |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Pillar Header | `card` | top | Name, description, health score, item count, last update |
| View Tabs | `tabs` | below header | "Canon" / "Folders" / "Artifacts" / "Threads" / "Routing" |
| Canon Document | `text` | main (canon tab) | Rich text display of canonical reference. S>C>E badge (🟢). Read-only for most levels |
| Folder Tree | `tree` | main (folders tab) | 16-folder scaffold: Zone A (Ingestion), Zone B (Digestion), Zone C (Canon), Zone D (Execution), Zone E (Governance) — expandable, item counts per folder |
| Recent Activity | `card` | right sidebar | Last 10 items added/modified in this pillar |
| Health Metrics | `stat_cards` | right sidebar | Freshness score, Items this week, Canonical ratio |
| Edit Canon Button (L5+) | `button` | canon view | "Edit" — must be explicitly approved |
| Sidebar Nav | `sidebar` | left | Module navigation |

---

### SCREEN PIL_C: Artifact Browser

**Route:** `/pillars/:id/artifacts`
**Layout:** `SB`
**Permission:** L2+

#### States

| State | Description |
|-------|-------------|
| `PIL_C.default` | Grid/list of artifacts in this pillar |
| `PIL_C.filtered` | Filtered by artifact type, S>C>E state |
| `PIL_C.detail` | Selected artifact expanded |
| `PIL_C.loading` | Skeleton grid |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Artifact Cards (×N) | `card` | main | Name, type badge, S>C>E badge, excerpt, date |
| Type Tabs | `tabs` | top | "All" + active artifact types in this pillar |
| Search | `search_bar` | top | Search within pillar |
| Filter Bar | `dropdown_group` | top | Type, S>C>E state, Date |
| Artifact Detail Panel | `card` | right | Full content, provenance, related items, "Promote" button (L4+) |
| View Toggle | `button_group` | top-right | Grid / List view |
| Sidebar Nav | `sidebar` | left | Module navigation |

---

### SCREEN PIL_D: Thread Archive

**Route:** `/pillars/:id/threads`
**Layout:** `SB`
**Permission:** L3+

#### States

| State | Description |
|-------|-------------|
| `PIL_D.default` | List of raw AI threads |
| `PIL_D.detail` | Selected thread expanded |
| `PIL_D.filtered` | Filtered by date, source |
| `PIL_D.loading` | Skeleton list |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Thread Table | `table` | main | Columns: Title, Source (ChatGPT/Claude/etc.), Date, Word count, Extracted artifacts count |
| Search | `search_bar` | top | Search thread content |
| Filter Bar | `dropdown_group` | top | Source, Date range |
| Thread Reader | `text` | right panel | Full thread content, scrollable, extracted sections highlighted |
| Extracted Artifacts Link | `badge_group` | in reader | Click to see artifacts extracted from this thread |
| Pagination | `pagination` | bottom | Page through threads |
| Sidebar Nav | `sidebar` | left | Module navigation |

---

### SCREEN PIL_E: Pillar Routing Rules

**Route:** `/pillars/:id/routing`
**Layout:** `SB`
**Permission:** L4+

Identical structure to `ENG_B` (Routing Rules Editor) but scoped to a single pillar.

---

## TAB 7: BUILD FACTORY (The Kinetic Limbs)

---

### SCREEN BLD_A: Project Registry

**Route:** `/factory/projects`
**Layout:** `SB`
**Permission:** L2+

#### States

| State | Description |
|-------|-------------|
| `BLD_A.default` | Grid/table of active projects |
| `BLD_A.filtered` | Filtered by maturity, status |
| `BLD_A.detail` | Selected project expanded |
| `BLD_A.loading` | Skeleton grid |
| `BLD_A.empty` | No projects — "Create your first project" |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Project Card (×N) | `card` | main | Name, maturity badge (Speculative/Operational/Production-Ready), progress %, active stage, team avatars, last activity |
| Maturity Tabs | `tabs` | top | "All" / "Speculative" / "Operational" / "Production-Ready" / "Archived" |
| Search | `search_bar` | top | Search projects |
| Create Project Button (L3+) | `button` | top-right | "+ New Project" |
| Project Detail Panel | `card` | right | 9-folder scaffold status, current stage, team, timeline, linked goals |
| Stats Bar | `stat_cards` | top | Total projects, In production, Launched this month, Blocked |
| Sidebar Nav | `sidebar` | left | Module navigation |

#### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `BLD_A.modal.create_project` | "+ New Project" | Name, description, type, deploy scaffold checkbox, team assignment |

---

### SCREEN BLD_B: 17-Step Mission Control

**Route:** `/factory/:id/pipeline`
**Layout:** `SB`
**Permission:** L3+

#### States

| State | Description |
|-------|-------------|
| `BLD_B.default` | Pipeline view — 17 steps with status indicators |
| `BLD_B.step_detail` | Selected step expanded |
| `BLD_B.track_view` | Grouped by 4 tracks |
| `BLD_B.loading` | Skeleton pipeline |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Pipeline Track Rows (×4) | `card` | main | Track 1: Intelligence (steps 1-5), Track 2: Foundation (6-9), Track 3: Brand & Creative (10-13), Track 4: Build & Launch (14-17) |
| Step Node (×17) | `badge_card` | in pipeline | Step number, name, status (not started/in progress/complete/blocked), assigned team, completion % |
| Step Detail Panel | `card` | right | Full step: description, deliverables checklist, assigned resources, timeline, linked artifacts |
| Project Header | `card` | top | Project name, overall progress %, current stage, timeline |
| View Toggle | `tabs` | top | "Pipeline" / "Tracks" / "Timeline" (Gantt-style) |
| Deliverable Checklist | `checklist` | step detail | Per-step deliverables with checkboxes |
| Sidebar Nav | `sidebar` | left | Module navigation |

---

### SCREEN BLD_C: Assembly Dashboard

**Route:** `/factory/:id/assemble`
**Layout:** `SB` with drag-drop zone
**Permission:** L3+

#### States

| State | Description |
|-------|-------------|
| `BLD_C.default` | Assembly canvas with available components |
| `BLD_C.dragging` | Item being dragged |
| `BLD_C.preview` | Preview assembled page |
| `BLD_C.loading` | Loading project assets |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Component Palette | `card_list` | left sidebar | Available assets: Copy Frameworks, UI Components, Database Schemas, Templates — draggable |
| Assembly Canvas | `canvas` | main | Drop zone: 9-folder scaffold visualisation, snap components into folders |
| Preview Panel | `card` | right | Preview of assembled component/page |
| Search Components | `search_bar` | left sidebar top | Search available components |
| Filter Components | `tabs` | left sidebar | "Copy" / "UI" / "Schema" / "Templates" |
| Undo/Redo | `button_group` | top | Undo/Redo assembly actions |
| Save Assembly | `button` | top-right | Save current assembly state |
| Sidebar Nav | `sidebar` | left (collapsed) | Module navigation |

---

### SCREEN BLD_D: PRD Editor

**Route:** `/factory/:id/prd`
**Layout:** `SP` (editor left, AI review right)
**Permission:** L3+

#### States

| State | Description |
|-------|-------------|
| `BLD_D.default` | PRD document editor |
| `BLD_D.reviewing` | AI multi-role review in progress |
| `BLD_D.review_complete` | Review feedback displayed |
| `BLD_D.loading` | Loading PRD |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| PRD Editor | `textarea` | left pane | Rich text editor for PRD content, section headings, markdown support |
| AI Review Panel | `card` | right pane | Role perspectives: each role's feedback as collapsible cards |
| Review Trigger | `button` | top-right | "Request AI Review" → sends to multi-role analysis |
| Role Feedback Card (×N) | `card` | right pane | Role avatar + name, risk flags, recommendations, approve/flag buttons |
| Section Navigator | `sidebar` | left | PRD section outline: Vision, Target Market, Screens, Technical, etc. |
| Version History | `button` | top | View previous versions |
| Export | `button` | top-right | Export as Markdown/PDF |

---

### SCREEN BLD_E: Build Story

**Route:** `/factory/:id/story`
**Layout:** `SB`
**Permission:** L2+

#### States

| State | Description |
|-------|-------------|
| `BLD_E.default` | Chronological timeline |
| `BLD_E.filtered` | Filtered by type (breakthrough/anti-pattern/milestone) |
| `BLD_E.adding` | Adding new entry |
| `BLD_E.loading` | Skeleton timeline |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Story Timeline | `timeline` | main | Vertical timeline: date markers, entry cards |
| Entry Card (×N) | `card` | in timeline | Type badge (breakthrough 🟢 / anti-pattern 🔴 / milestone 🔵 / note ⚪), title, description, linked session |
| Add Entry Button | `button` | top-right | "+ Add Entry" |
| Type Filter | `tabs` | top | "All" / "Breakthroughs" / "Anti-patterns" / "Milestones" / "Notes" |
| Search | `search_bar` | top | Search story entries |
| Sidebar Nav | `sidebar` | left | Module navigation |

#### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `BLD_E.modal.add_entry` | "+ Add Entry" | Type selector, title, description, link to session, "Save" |

---

## TAB 8: OPERATIONS (The Immune System)

---

### SCREEN OPS_A: System Health Dashboard

**Route:** `/ops/health`
**Layout:** `SB`
**Permission:** L4+

#### States

| State | Description |
|-------|-------------|
| `OPS_A.default` | Health metrics overview |
| `OPS_A.detail` | Drill into specific metric |
| `OPS_A.historical` | Viewing historical health data |
| `OPS_A.loading` | Skeleton dashboard |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Org Heatmap | `grid` | main | 23 pillars as cells, colour = freshness (green/amber/red), click to drill |
| Stat Cards Row | `stat_cards` | top | Ingestion rate, Routing accuracy, Active sessions, Canonical ratio, Error rate |
| Ingestion Chart | `chart` | main | Items ingested per day (bar chart) |
| Routing Accuracy Chart | `chart` | main | % correctly routed over time (line chart) |
| Pillar Freshness Table | `table` | main | All 23 pillars: last update, item count, health score, trend arrow |
| Date Range Picker | `dropdown` | top | Last 7d / 30d / 90d / Custom |
| Sidebar Nav | `sidebar` | left | Module navigation |

---

### SCREEN OPS_B: Strategic Goal Cascade

**Route:** `/ops/goals`
**Layout:** `SB`
**Permission:** L5+

#### States

| State | Description |
|-------|-------------|
| `OPS_B.default` | Tree visualisation of goal cascade |
| `OPS_B.expanded` | Expanded tree node detail |
| `OPS_B.collapsed` | Collapsed to top-level only |
| `OPS_B.loading` | Skeleton tree |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Goal Tree | `tree` | main | Hierarchy: CEO goals → Department goals → Team goals → Individual tasks. Each node: name, progress %, health colour |
| Node Detail Panel | `card` | right | Selected node: owner, progress, linked tasks, health trend |
| Zoom Controls | `button_group` | top | Expand all / Collapse all / Zoom to fit |
| Progress Rollup | `stat_cards` | top | Company progress %, Departments on track, At-risk goals |
| Coherence Loop Indicator | `badge` | top | "Know → Build → Ship → Learn" cycle status |
| Sidebar Nav | `sidebar` | left | Module navigation |

---

### SCREEN OPS_C: Canonisation Queue

**Route:** `/ops/canon`
**Layout:** `SB`
**Permission:** L4+

Same structure as `CMD_E` (Approval & Governance Queue) but aggregated across ALL modules, not just Command Deck.

---

### SCREEN OPS_D: Daily Digest Viewer

**Route:** `/ops/digest`
**Layout:** `CT`
**Permission:** L3+

Same structure as `NAV_C` (Morning Brief) but accessed from Operations tab with additional team/org-level views for L5+.

---

### SCREEN OPS_E: Whole-Org Pulse

**Route:** `/ops/pulse`
**Layout:** `SB`
**Permission:** L6+

#### States

| State | Description |
|-------|-------------|
| `OPS_E.default` | Live activity feed |
| `OPS_E.filtered` | Filtered by module, user, activity type |
| `OPS_E.paused` | Feed paused for reading |
| `OPS_E.loading` | Loading feed |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Live Feed | `feed` | main | Real-time stream: avatar + name + action + module badge + timestamp. Auto-scrolling |
| Filter Bar | `dropdown_group` | top | Module, User/Team, Activity type (session/routing/ingestion/approval) |
| Pause/Resume | `button` | top-right | Pause feed for reading |
| Active Sessions Panel | `card` | right sidebar | Currently active sessions: who, what intent, duration |
| Bottleneck Alerts | `card` | right sidebar | Items stuck > 24h, failed ingestions, approval backlog |
| Stats Bar | `stat_cards` | top | Active users now, Sessions today, Outputs today, Routing decisions today |
| Sidebar Nav | `sidebar` | left | Module navigation |

---

## SHARED / GLOBAL SCREENS

---

### SCREEN AUTH_A: Login

**Route:** `/login`
**Layout:** `SP` (form left, branding right)
**Permission:** Public

#### States

| State | Description |
|-------|-------------|
| `AUTH_A.default` | Email + password form |
| `AUTH_A.sso` | SSO provider buttons |
| `AUTH_A.loading` | Authenticating spinner |
| `AUTH_A.error` | Invalid credentials — error message |
| `AUTH_A.forgot_password` | Password reset form |
| `AUTH_A.2fa` | Two-factor authentication input |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Login Form | `form` | left pane | Email input, password input, "Remember me" checkbox, "Login" button |
| SSO Buttons | `button_group` | left pane | "Sign in with Google", "Sign in with Microsoft" |
| Forgot Password Link | `link` | left pane | Opens forgot password form |
| Brand Panel | `image` + `text` | right pane | Enterprise OS logo, tagline, illustration |
| Error Message | `notification` | left pane top | Red error banner |
| 2FA Input | `input` | left pane (2FA state) | 6-digit code input |

---

### SCREEN AUTH_B: Register / Onboarding

**Route:** `/register`
**Layout:** `CT` → multi-step wizard
**Permission:** Public

#### States

| State | Description |
|-------|-------------|
| `AUTH_B.step_1` | Account creation: name, email, password |
| `AUTH_B.step_2` | Organization setup: org name, size, industry |
| `AUTH_B.step_3` | Role assignment: select L1-L7 (admin assigns) |
| `AUTH_B.step_4` | Data sources: connect initial sources |
| `AUTH_B.step_5` | Welcome tour: guided walkthrough of 8 modules |
| `AUTH_B.complete` | Setup complete — redirect to Hub |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Step Progress | `progress` | top | 5 steps with labels |
| Account Form | `form` | step 1 | Name, email, password, confirm password |
| Org Form | `form` | step 2 | Org name, size dropdown, industry dropdown, logo upload (optional) |
| Role Grid | `card_grid` | step 3 | 7 role cards with descriptions, select one |
| Source Connectors | `card_grid` | step 4 | Available sources: Google Drive, Slack, etc. — "Connect" buttons, "Skip" option |
| Tour Overlay | `overlay` | step 5 | Guided tooltips highlighting 8 module tiles |
| Navigation Buttons | `button_group` | bottom | "Back", "Next" / "Complete Setup" |

---

### SCREEN ADMIN_A: User Management

**Route:** `/admin/users`
**Layout:** `SB`
**Permission:** L6+

#### States

| State | Description |
|-------|-------------|
| `ADMIN_A.default` | User table |
| `ADMIN_A.detail` | Selected user profile |
| `ADMIN_A.inviting` | Invite new user form |
| `ADMIN_A.loading` | Skeleton table |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| User Table | `table` | main | Columns: Name, Email, Role, Level (L1-L7), Status (active/invited/suspended), Last active |
| Invite Button | `button` | top-right | "+ Invite User" |
| User Detail Panel | `card` | right | Full profile, role history, session count, permissions, edit button |
| Level Filter | `dropdown` | top | Filter by L1-L7 |
| Role Filter | `dropdown` | top | Filter by role |
| Bulk Actions | `button_group` | bottom | "Change Level", "Suspend", "Remove" |
| Sidebar Nav | `sidebar` | left | Module navigation |

#### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `ADMIN_A.modal.invite` | "+ Invite User" | Email, role, level, team, custom message, "Send Invite" |
| `ADMIN_A.modal.change_level` | "Change Level" | Level selector with description of what each level sees |

---

### SCREEN SETTINGS: Settings

**Route:** `/settings`
**Layout:** `SB`
**Permission:** L1+

#### States

| State | Description |
|-------|-------------|
| `SETTINGS.profile` | Profile settings |
| `SETTINGS.notifications` | Notification preferences |
| `SETTINGS.integrations` | Connected services |
| `SETTINGS.appearance` | Theme and display settings |
| `SETTINGS.security` | Password and 2FA |

#### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Settings Nav | `tabs` (vertical) | left | Profile / Notifications / Integrations / Appearance / Security |
| Profile Form | `form` | main | Name, email, avatar upload, bio, timezone |
| Notification Toggles | `toggle_group` | main | Per-event notification preferences: email, in-app, digest |
| Integration Cards | `card_grid` | main | Connected services with connect/disconnect buttons |
| Theme Selector | `card_grid` | main | Light / Dark / System |
| Security Form | `form` | main | Change password, enable 2FA |
| Save Button | `button` | bottom | "Save Changes" |

---

### SCREEN SEARCH: Global Search

**Route:** `/search`
**Layout:** Same as `LIB_D` (Semantic Search)
**Permission:** L1+

Identical to Semantic Search but accessible from the global topbar. Opens as overlay or full page.

---

## SUMMARY

### Screen Count

| Section | Screens | States | Modals |
|---------|---------|--------|--------|
| Hub | 1 | 10 | 3 |
| Tab 1: Navigation | 7 | 30 | 7 |
| Tab 2: Command Deck | 5 | 24 | 9 |
| Tab 3: Core Engine | 5 | 19 | 2 |
| Tab 4: Knowledge Library | 5 | 24 | 4 |
| Tab 5: Template Hub | 5 | 19 | 0 |
| Tab 6: Domain Pillars | 5 | 14 | 0 |
| Tab 7: Build Factory | 5 | 18 | 2 |
| Tab 8: Operations | 5 | 14 | 0 |
| Shared/Global | 5 | 16 | 2 |
| **TOTAL** | **48** | **188** | **29** |

### Boilerplate Reuse

| Boilerplate | Used By | Count |
|-------------|---------|-------|
| Dashboard List (table + filters + detail panel) | CMD_B, ENG_A, ENG_E, LIB_A, PIL_C, PIL_D, BLD_A, ADMIN_A | 8 |
| Dashboard Analytics (charts + stat cards) | NAV_D, ENG_C, LIB_E, OPS_A | 4 |
| Dashboard Form/Editor | ENG_B, TPL_E, SETTINGS | 3 |
| Multi-step Wizard | NAV_A, TPL_B, AUTH_B | 3 |
| Split View (comparison) | CMD_C, LIB_B, BLD_D | 3 |
| Card Grid (searchable) | CMD_D, TPL_A, PIL_A | 3 |
| Chat/Feed Interface | NAV_F, CMD_A, OPS_E | 3 |
| Approval Queue | CMD_E, LIB_C, OPS_C | 3 |
| Timeline | NAV_E, BLD_B, BLD_E | 3 |
| Search Results | LIB_D, SEARCH | 2 |
| Auth (split brand + form) | AUTH_A, AUTH_B | 2 |
| Canvas/Flow Builder | TPL_D, BLD_C | 2 |
| Read-only Digest/Brief | NAV_C, OPS_D | 2 |
| Tree Visualisation | TPL_C, OPS_B | 2 |
| **Unique: Active Cockpit (3-pane)** | CMD_A | 1 |

### Component Inventory Need

| Component | Estimated Instances Across All Screens |
|-----------|---------------------------------------|
| `table` | 15+ |
| `card` | 100+ |
| `button` / `button_group` | 80+ |
| `sidebar` | 40+ (every SB layout) |
| `topbar` | 1 (global, all screens) |
| `tabs` | 25+ |
| `search_bar` | 15+ |
| `badge` | 50+ (S>C>E + status + type badges) |
| `dropdown` | 30+ (filters, selectors) |
| `form` / `input` / `textarea` | 20+ |
| `chart` | 10+ |
| `stat_cards` | 15+ |
| `progress` | 10+ |
| `timeline` | 5+ |
| `tree` | 3+ |
| `feed` | 3+ |
| `chat` | 3+ |
| `modal` | 29 defined |
| `notification` / `toast` | 10+ |
| `pagination` | 8+ |
| `avatar` | 15+ |
| `toggle` | 10+ |
| `checklist` | 3+ |
| `canvas` | 2 |
| `dropzone` | 2 |
| `code` | 2 |
