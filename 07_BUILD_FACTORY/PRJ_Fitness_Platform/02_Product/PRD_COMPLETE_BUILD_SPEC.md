# Fitness Platform — Complete Build Specification

> **Version:** 1.0
> **Date:** 2026-02-17
> **Purpose:** Every screen, every state, every component, every API endpoint — full endpoint fidelity.
> **Sources:** PRD_2_Fitness_Platform.md, SCREEN_INVENTORY.md, fitness_ingestion_app_blueprint_v_1.md, fitness_app_framework.md, 30 exercise pillar breakdowns
> **Goal:** Plug-and-play specification. Feed directly into UI Assembly Pipeline + development sprints.

---

## Executive Summary

**What:** AI-first fitness platform. Not a program browser — a conversational workout generator that learns you and adapts in real-time.

**Core Loop:** Tell the AI what you've got → Get a personalised workout → Do it → Track it → AI gets smarter about you.

**Scale:** 500+ exercises across 30 training domains, 7 movement patterns, 4 planes of motion, 11 modalities, constraint-based planner guaranteeing weekly coverage.

**Revenue:** Freemium — Free / £9.99 Premium / £29 Trainer. Target: 50K users, 10% conversion = £50K MRR by Month 12.

**Tech:** Next.js 16 + React 19 + Tailwind v4 + PostgreSQL + pgvector + Claude API + YouTube Data API v3.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────┐
│              FRONTEND (Next.js 16)               │
│  Marketing | Auth | App Shell | Active Workout   │
└──────────────────────┬──────────────────────────┘
                       │ API Routes
┌──────────────────────┴──────────────────────────┐
│              BACKEND (API Layer)                  │
│  Auth | Workout Gen | Exercise DB | Tracking     │
│  Programs | Social | Marketplace | Analytics     │
└──────────────────────┬──────────────────────────┘
                       │
┌──────────────────────┴──────────────────────────┐
│              DATA LAYER                          │
│  PostgreSQL + pgvector │ Redis (sessions/cache)  │
│  YouTube API v3        │ Claude API (AI gen)     │
│  S3/Cloudflare R2      │ Apple Health / Google   │
└─────────────────────────────────────────────────┘
```

---

## Conventions

**State notation:** `[SCREEN_ID].[state]` — e.g., `GEN.loading`, `WKT.rest_timer`
**Modal notation:** `[SCREEN_ID].modal.[name]` — e.g., `DASH.modal.quick_generate`
**Layout codes:** `SB` = sidebar_content, `SP` = split, `CT` = centered, `FC` = full_canvas, `GR` = grid, `CH` = chat
**Permission:** `Free`, `Premium`, `Trainer` (subscription tiers)
**Phase:** `MVP` (build now), `P2` (plan now, build later)

---

## SCREEN 1: LANDING / MARKETING

**Route:** `/`
**Layout:** `FC` — full-page marketing layout
**Permission:** Public (no auth required)
**Phase:** MVP

### States

| State | Description |
|-------|-------------|
| `LAND.default` | Full marketing page with hero, features, social proof, pricing, CTA |
| `LAND.loading` | Skeleton loaders for dynamic content (testimonials, stats) |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Hero Section | `hero` | top | Headline: "Your AI Training Partner". Subhead explaining AI-first approach. Primary CTA: "Start Free". Secondary: "See it in action". Background: workout imagery or animation |
| Problem Section | `section` | below hero | "Most fitness apps give you a program and hope you stick to it. Life doesn't work that way." 3 pain points with icons |
| Solution Section | `section` | mid | "Tell the AI what you've got. Get a workout that fits." Visual showing chat → workout output flow |
| How It Works | `steps` | mid | 3-step visual: 1) Tell it your situation, 2) Get a personalised workout, 3) Track & improve. Animated or illustrated |
| Exercise Pillars Showcase | `carousel` | mid | 30 training domains displayed as scrollable cards — Kettlebells, Calisthenics, Olympic Lifting, Yoga, etc. Shows depth of library |
| Social Proof | `testimonials` | mid-lower | User quotes, workout count stat, exercise count stat |
| Pricing Cards | `pricing` | lower | 3 tiers (Free/Premium/Trainer) with feature comparison |
| Final CTA | `cta` | bottom | "Start Your Free Account" with email input |
| Navigation | `navbar` | sticky top | Logo, Features, Pricing, Sign In, "Get Started" button |
| Footer | `footer` | bottom | Links, social icons, legal |

### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `LAND.modal.demo_video` | "See it in action" link | Embedded video showing AI workout generation in real-time |

### Features

| Feature | Description |
|---------|-------------|
| AI-first messaging | Communicate that this isn't a program library — it's a personal AI trainer |
| Social proof counters | Live workout count, exercise database size, user count |
| Pricing transparency | Full tier comparison visible before signup |

### Benefits

| Benefit | Who | Impact |
|---------|-----|--------|
| Instant understanding of value prop | Prospects | Higher conversion — they get it immediately |
| No commitment barrier | Free tier users | Reduces signup friction |
| Trainer tier visibility | Personal trainers | Secondary revenue stream from day 1 |

### Data

| Entity | Table | Key Fields |
|--------|-------|------------|
| Landing analytics | `page_events` | page_view, scroll_depth, cta_clicks |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/stats/public` | Public stats (exercise count, workout count) |

---

## SCREEN 2: AUTH (Sign Up / Sign In)

**Route:** `/auth`
**Layout:** `CT` — centered form
**Permission:** Public
**Phase:** MVP

### States

| State | Description |
|-------|-------------|
| `AUTH.signup` | Registration form — email, password, confirm |
| `AUTH.signin` | Login form — email, password |
| `AUTH.forgot` | Password reset — email input |
| `AUTH.reset` | New password form (from email link) |
| `AUTH.verify` | Email verification pending screen |
| `AUTH.error` | Auth failure — invalid credentials, account exists, etc. |
| `AUTH.loading` | Processing auth request |
| `AUTH.social` | OAuth redirect in progress |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Auth Card | `card` | center | Logo at top, form below, toggle between Sign Up / Sign In |
| Email Input | `input` | form | Email validation, auto-focus |
| Password Input | `input` | form | Strength indicator on signup, show/hide toggle |
| Social Auth Buttons | `button_group` | below form | Google, Apple sign-in |
| Submit Button | `button` | form bottom | "Create Account" / "Sign In", loading state |
| Terms Checkbox | `checkbox` | below form (signup) | "I agree to Terms & Privacy Policy" |
| Error Alert | `alert` | above form | Red banner with specific error message |
| Forgot Password Link | `link` | below sign-in form | Opens forgot password state |

### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `AUTH.modal.terms` | Terms link click | Terms of service full text |
| `AUTH.modal.privacy` | Privacy link click | Privacy policy full text |

### Features

| Feature | Description |
|---------|-------------|
| Email/password auth | Standard authentication |
| Social auth (Google, Apple) | OAuth2 integration |
| Password strength meter | Real-time strength indicator |
| Email verification | Confirm email before access |

### Benefits

| Benefit | Who | Impact |
|---------|-----|--------|
| Low-friction signup | All users | Higher registration completion |
| Social auth | Users with Google/Apple | One-click signup |
| Email verification | Platform | Reduces spam accounts |

### Data

| Entity | Table | Key Fields |
|--------|-------|------------|
| User | `users` | id, email, password_hash, email_verified, created_at |
| Auth session | `sessions` | user_id, token, expires_at, device_info |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/api/v1/auth/register` | Create account |
| POST | `/api/v1/auth/login` | Sign in |
| POST | `/api/v1/auth/logout` | End session |
| POST | `/api/v1/auth/forgot-password` | Request password reset |
| POST | `/api/v1/auth/reset-password` | Set new password |
| GET | `/api/v1/auth/verify/:token` | Verify email |
| POST | `/api/v1/auth/oauth/google` | Google OAuth |
| POST | `/api/v1/auth/oauth/apple` | Apple OAuth |

---

## SCREEN 3: ONBOARDING INTAKE

**Route:** `/onboarding`
**Layout:** `CT` — centered multi-step wizard
**Permission:** Authenticated (all tiers)
**Phase:** MVP

### States

| State | Description |
|-------|-------------|
| `ONB.step_1` | Goals — what do you want to achieve? (multi-select: build muscle, lose fat, get stronger, improve mobility, general fitness, sport-specific) |
| `ONB.step_2` | Experience level — beginner / intermediate / advanced (with descriptions) |
| `ONB.step_3` | Equipment access — what do you have? (multi-select: bodyweight only, dumbbells, barbell, kettlebells, pull-up bar, resistance bands, machines, full gym) |
| `ONB.step_4` | Schedule — how many days/week? How long per session? Preferred times? |
| `ONB.step_5` | Injuries/limitations — any areas to avoid or be careful with? (body map selector) |
| `ONB.step_6` | Preferences — favourite training styles from the 30 pillars (optional, AI will learn over time) |
| `ONB.completed` | "You're all set! Let's generate your first workout." with CTA to AI Generator |
| `ONB.skip` | Skip option available — "These are starting points. The AI will learn as you go." |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Step Progress Bar | `progress` | top | 6 steps, current highlighted, completed checkmarks |
| Goal Selector | `chip_group` | center | Multi-select chips with icons per goal |
| Experience Cards | `card_group` | center | 3 cards (Beginner/Intermediate/Advanced) with descriptions of what each means |
| Equipment Checklist | `checklist` | center | Visual icons for each equipment type, multi-select |
| Schedule Picker | `form` | center | Day-of-week toggles + session duration slider (15-90 min) |
| Body Map | `interactive` | center | Visual body outline — tap areas to mark injuries/limitations |
| Pillar Preference Grid | `chip_group` | center | 30 pillar chips (Kettlebells, Yoga, etc.) — select favourites |
| Skip Link | `link` | bottom-right | "Skip for now — AI will learn as you go" |
| Navigation Buttons | `button_group` | bottom | "Back" + "Next" / "Let's Go!" |

### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `ONB.modal.injury_detail` | Tap body area | "Tell us more about this area" — severity, recent surgery, physio guidance |

### Features

| Feature | Description |
|---------|-------------|
| Light-touch intake | Starting points, not permanent profiles. AI adapts over time |
| Skip option | User isn't forced to complete — reduces drop-off |
| Body map for injuries | Visual, intuitive injury marking |
| 30-pillar preference selection | Surfaces the depth of the exercise library immediately |

### Benefits

| Benefit | Who | Impact |
|---------|-----|--------|
| Better first workout | New users | AI has baseline to generate relevant workout |
| Injury safety | Users with limitations | Contraindicated exercises excluded from generation |
| Reduced onboarding friction | All users | Skip option means nobody gets stuck |

### Data

| Entity | Table | Key Fields |
|--------|-------|------------|
| User profile | `user_profiles` | user_id, goals[], experience_level, equipment[], schedule, session_duration_min |
| Injuries | `user_injuries` | user_id, body_area, severity, notes, active |
| Preferences | `user_preferences` | user_id, preferred_pillars[], preferred_modalities[] |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/api/v1/onboarding/profile` | Save full onboarding profile |
| PATCH | `/api/v1/onboarding/profile` | Update individual steps |
| GET | `/api/v1/onboarding/status` | Check if onboarding completed |

---

## SCREEN 4: AI WORKOUT GENERATOR (THE CORE SCREEN)

**Route:** `/generate`
**Layout:** `CH` — chat/conversational interface with output panel
**Permission:** Free (limited generations/day), Premium (unlimited)
**Phase:** MVP

### States

| State | Description |
|-------|-------------|
| `GEN.default` | Chat interface ready. Quick-start suggestions: "30 min dumbbell workout", "Full body no equipment", "Heavy legs day" |
| `GEN.chat` | Active conversation — user typing, AI responding with clarifying questions or workout |
| `GEN.generating` | AI processing — animated loading ("Building your workout...") with exercise-related tips cycling |
| `GEN.workout_ready` | Workout card displayed — exercises, sets, reps, rest, estimated time. Actions: Start, Modify, Save, Share |
| `GEN.modifying` | User requesting changes: "swap the squats for lunges", "make it harder", "add more core" |
| `GEN.limit_reached` | Free tier daily limit hit — upgrade CTA with workout preview |
| `GEN.error` | AI generation failure — retry button + fallback suggestion |
| `GEN.history` | Previous generated workouts in sidebar/panel |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Chat Input | `textarea` | bottom | Auto-expanding, placeholder: "What have you got today?", send button, voice input option |
| AI Message Bubble | `chat_message` | main area | AI responses — questions, suggestions, workout output |
| User Message Bubble | `chat_message` | main area | Right-aligned user messages |
| Circumstance Quick Input | `chip_group` | above chat input | Quick chips: time (15/30/45/60 min), equipment (gym/home/none), energy (low/medium/high), focus (upper/lower/full) |
| Workout Output Card | `card` | main area / side panel | Structured workout: exercise name, sets × reps, rest, target muscles, video thumbnail. Expandable per exercise |
| Exercise Row | `list_item` | within workout card | Exercise name, set scheme, muscle tags, swap button, info button |
| Swap Suggestion | `popover` | on exercise row | AI suggests 3 alternatives with reasoning |
| Generation Counter | `badge` | top bar | Free: "3/5 generations today" | Premium: hidden |
| Start Workout Button | `button` | workout card bottom | Primary CTA — launches Active Workout Mode |
| Save Workout Button | `button` | workout card bottom | Save to history for future use |
| Workout Stats Preview | `stats` | workout card top | Estimated duration, muscle groups hit, modalities covered, difficulty |

### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `GEN.modal.exercise_detail` | Tap exercise info icon | Full exercise detail: video, form cues, muscles, variations |
| `GEN.modal.upgrade` | Free tier limit reached | "Unlock unlimited AI workouts" — Premium benefits + CTA |
| `GEN.modal.save_workout` | Save button | Name the workout, add tags, save to library |

### Features

| Feature | Description |
|---------|-------------|
| Conversational AI generation | Natural language: "I've got 30 mins, dumbbells, and I'm tired" → personalised workout |
| Circumstance awareness | AI factors in equipment, time, energy, goals, injuries, history |
| Exercise swapping | Swap any exercise mid-generation with AI alternatives |
| Progressive learning | AI gets smarter with each workout — learns preferences, strengths, patterns |
| Quick-start suggestions | Pre-built prompts for common scenarios |
| Workout modification | Chat to modify: "make it harder", "add more core", "less time" |
| Generation history | Access previous workouts for repeat use |

### Benefits

| Benefit | Who | Impact |
|---------|-----|--------|
| No planning required | All users | Removes the biggest barrier to working out — deciding what to do |
| Adapts to circumstance | All users | Travel, new gym, home day, low energy — always gets a workout |
| Learns over time | Regular users | Workouts improve with usage — stronger retention |
| 30-pillar exercise depth | Advanced users | Not limited to basic exercises — kettlebells, Olympic lifting, calisthenics, mobility, etc. |

### Data

| Entity | Table | Key Fields |
|--------|-------|------------|
| Generated workouts | `generated_workouts` | id, user_id, prompt, workout_data (JSONB), generated_at |
| Chat messages | `generation_chat_log` | id, workout_id, role, content, created_at |
| Generation count | `user_generation_count` | user_id, date, count |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/api/v1/generate/workout` | Generate workout from prompt + user context |
| POST | `/api/v1/generate/modify` | Modify existing workout via chat |
| POST | `/api/v1/generate/swap` | Swap single exercise with AI alternatives |
| GET | `/api/v1/generate/history` | List previous generated workouts |
| GET | `/api/v1/generate/limit` | Check remaining free generations |

---

## SCREEN 5: ACTIVE WORKOUT MODE

**Route:** `/workout/:id`
**Layout:** `FC` — full-screen workout experience
**Permission:** All tiers (Free workouts from generations, Premium for saved programs)
**Phase:** MVP

### States

| State | Description |
|-------|-------------|
| `WKT.overview` | Workout summary before starting: exercise list, estimated time, muscle groups, "Begin Workout" CTA |
| `WKT.active` | Current exercise displayed — video, set/rep targets, logging inputs, rest timer |
| `WKT.rest_timer` | Between-set rest countdown — configurable duration, skip button, next exercise preview |
| `WKT.exercise_transition` | Between exercises — "Next: [Exercise Name]" with video preview, quick swap option |
| `WKT.logging` | User logging set data — weight, reps, RPE inputs |
| `WKT.paused` | Workout paused — "Resume" / "End Early" / "Skip Exercise" |
| `WKT.completed` | Workout finished — summary stats, PRs hit, volume total, "Save & Exit" |
| `WKT.abandoned` | Left early — partial log saved, prompt to finish later |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Exercise Video Player | `video` | top half | YouTube embed or hosted video, auto-plays current exercise demo, loop option |
| Exercise Info Bar | `bar` | below video | Exercise name, set X of Y, target: 3×12 @ 20kg, muscles (badges) |
| Set Logger | `form` | center | Weight input (kg/lbs toggle), reps input, RPE slider (1-10), "Log Set" button |
| Previous Performance | `stats` | beside logger | "Last time: 20kg × 12, 12, 10" — comparison at a glance |
| Rest Timer | `timer` | center (during rest) | Large countdown (configurable 30s-5min), skip button, auto-start option |
| Progress Bar | `progress` | top | Exercises completed / total, current position indicator |
| Exercise Queue | `list` | collapsible sidebar/bottom | Upcoming exercises list, completed checkmarks, drag-to-reorder |
| Form Cues | `card` | below video | Key coaching cues for current exercise (from exercise DB) |
| Swap Button | `button` | exercise info bar | Offer AI alternatives for current exercise |
| Workout Controls | `button_group` | bottom | "Pause" / "Skip Exercise" / "End Workout" |

### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `WKT.modal.end_early` | "End Workout" button | "End this workout? Your progress is saved." — End / Continue |
| `WKT.modal.exercise_swap` | Swap button | 3 AI-suggested alternatives with reasoning. Select to swap |
| `WKT.modal.personal_record` | PR detected during logging | Celebration animation — "New PR! Bench Press: 80kg × 8" |
| `WKT.modal.add_note` | Note icon on exercise | Free-text note for this exercise/set (form feedback, pain, modification) |

### Features

| Feature | Description |
|---------|-------------|
| Exercise-by-exercise guidance | Step through workout with video + targets + logging |
| Real-time set logging | Weight, reps, RPE per set — fast inline entry |
| Configurable rest timer | Auto-countdown between sets, customisable per exercise |
| Previous performance display | See last session's numbers for comparison |
| Auto-advance | Moves to next exercise after final set logged |
| PR detection | Automatic personal record detection and celebration |
| Exercise swapping mid-workout | Swap any exercise on the fly with AI alternatives |
| Workout notes | Add notes per exercise for future reference |

### Benefits

| Benefit | Who | Impact |
|---------|-----|--------|
| Hands-free-ish experience | Active users | Minimal interaction needed during workout |
| Progressive overload tracking | All users | See last session's numbers → push harder |
| PR motivation | All users | Celebrates achievements → dopamine → retention |
| Flexibility mid-workout | Users in crowded gyms | Equipment taken? Swap instantly |

### Data

| Entity | Table | Key Fields |
|--------|-------|------------|
| Workout log | `user_workouts` | id, user_id, workout_template_id, started_at, completed_at, status |
| Set log | `workout_sets` | id, user_workout_id, exercise_id, set_number, weight_kg, reps, rpe, rest_seconds |
| Notes | `workout_notes` | id, user_workout_id, exercise_id, note, created_at |
| PRs | `personal_records` | id, user_id, exercise_id, metric (weight/reps/volume), value, achieved_at |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/api/v1/workouts/start` | Start workout session |
| POST | `/api/v1/workouts/:id/sets` | Log a set |
| PATCH | `/api/v1/workouts/:id/complete` | Complete workout |
| POST | `/api/v1/workouts/:id/notes` | Add workout note |
| GET | `/api/v1/workouts/:id/previous` | Get previous performance for same workout |
| POST | `/api/v1/workouts/:id/swap/:exercise_id` | Swap exercise mid-workout |

---

## SCREEN 6: EXERCISE LIBRARY

**Route:** `/exercises`
**Layout:** `SB` — sidebar filters + content grid
**Permission:** Free (limited), Premium (full)
**Phase:** MVP

### States

| State | Description |
|-------|-------------|
| `LIB.default` | Full exercise grid with filter sidebar, search bar |
| `LIB.filtered` | Applied filters — results update in real-time |
| `LIB.search` | Search results — exercise name fuzzy match |
| `LIB.empty` | No results matching filters — "Try broadening your search" |
| `LIB.loading` | Skeleton card grid while fetching |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Search Bar | `input` | top | Fuzzy search across exercise names and aliases |
| Filter Sidebar | `sidebar` | left | Collapsible sections: Muscle Group (body map or checklist), Equipment, Movement Pattern, Modality, Plane of Motion, Difficulty, Pillar (30 domains) |
| Exercise Card | `card` | main grid | Video thumbnail, exercise name, muscle badges, difficulty badge, equipment icon. Click → Exercise Detail |
| Muscle Group Selector | `interactive` | filter sidebar | Visual body map — click muscle to filter |
| Equipment Filter | `checklist` | filter sidebar | Icons for each equipment type |
| Pillar Filter | `chip_group` | filter sidebar | 30 training domain chips |
| Results Count | `text` | above grid | "Showing 142 of 500+ exercises" |
| Sort Dropdown | `select` | top-right | Name A-Z, Difficulty, Most Popular, Recently Added |
| Pagination | `pagination` | bottom | Load more / infinite scroll |

### Modals

None — clicking an exercise navigates to Exercise Detail.

### Features

| Feature | Description |
|---------|-------------|
| Multi-dimensional filtering | Filter by muscle, equipment, pattern, modality, plane, difficulty, pillar simultaneously |
| Visual body map filter | Tap muscles on body outline to filter exercises |
| Fuzzy search with aliases | "Skull crusher" finds "Lying Tricep Extension" |
| 30-pillar categorization | Browse by training domain (Kettlebells, Calisthenics, etc.) |

### Benefits

| Benefit | Who | Impact |
|---------|-----|--------|
| Discovery | All users | Find exercises they didn't know existed |
| Education | Beginners | Learn proper exercise names and categories |
| Workout planning | Advanced users | Browse and build custom routines |

### Data

| Entity | Table | Key Fields |
|--------|-------|------------|
| Exercises | `exercises` | id, slug, name, description, difficulty, progression_level |
| Muscles | `exercise_muscles` | exercise_id, muscle_id, role |
| Equipment | `exercise_equipment` | exercise_id, equipment_id |
| Patterns | `exercise_patterns` | exercise_id, pattern_id |
| Modalities | `exercise_modalities` | exercise_id, modality_id |
| Planes | `exercise_planes` | exercise_id, plane_id |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/exercises` | List exercises (paginated, filterable) |
| GET | `/api/v1/exercises/search?q=` | Fuzzy search exercises |
| GET | `/api/v1/exercises/filters` | Get all filter options (muscles, equipment, etc.) |

---

## SCREEN 7: EXERCISE DETAIL

**Route:** `/exercises/:id`
**Layout:** `SB` — content area with sidebar info
**Permission:** Free (basic), Premium (full videos + progressions)
**Phase:** MVP

### States

| State | Description |
|-------|-------------|
| `EXD.default` | Full exercise detail — video, description, muscles, cues, variations |
| `EXD.loading` | Skeleton layout while fetching |
| `EXD.video_playing` | Video player expanded/active |
| `EXD.progression_view` | Progression/regression chain visible |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Exercise Video Player | `video` | top | Primary demo video (YouTube embed), multiple angle options if available |
| Exercise Title | `heading` | below video | Name + aliases (e.g., "Barbell Back Squat (aka Back Squat, BB Squat)") |
| Muscle Map | `interactive` | sidebar | Visual body highlighting primary (dark) / secondary (light) / stabilizer (outline) muscles |
| Attribute Badges | `badge_group` | below title | Difficulty, Equipment, Modality, Plane, Pattern — all as colour-coded badges |
| Form Cues | `list` | main | Ordered coaching cues with emphasis on key points |
| Steps | `list` | main | Step-by-step execution instructions |
| Common Mistakes | `list` | main | Numbered list of errors to avoid |
| Contraindications | `alert` | main | Warning badges for injury considerations |
| Progression Chain | `timeline` | sidebar/bottom | Visual regression → current → progression path. Click any to navigate |
| Variations Grid | `card_grid` | bottom | Related exercises as small cards with thumbnails |
| Add to Workout Button | `button` | floating/sidebar | "Add to next workout" or "Generate workout with this exercise" |
| Source Attribution | `text` | bottom | Source reference (book, channel, website) |

### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `EXD.modal.add_to_workout` | "Add to Workout" button | Select existing workout or generate new one including this exercise |

### Features

| Feature | Description |
|---------|-------------|
| Multi-source video demos | Multiple video demonstrations from vetted channels |
| Visual muscle targeting | Interactive body map showing exactly what the exercise hits |
| Progression/regression chain | See easier and harder versions of every exercise |
| Form cues + common mistakes | Expert coaching tips from ingested content |
| Contraindication flags | Safety warnings for injury-prone movements |

### Benefits

| Benefit | Who | Impact |
|---------|-----|--------|
| Learn proper form | Beginners | Reduces injury risk |
| Find progressions | Intermediate | Clear path to harder variations |
| Find regressions | Injured/returning | Safe alternatives |
| Deep exercise knowledge | All users | Platform becomes a learning resource, not just a tracker |

### Data

| Entity | Table | Key Fields |
|--------|-------|------------|
| Exercise | `exercises` | All fields — name, description, difficulty, cues, steps, contraindications |
| Media | `media` | exercise_id, type, uri, thumbnail |
| Progressions | `progressions` | from_exercise, to_exercise, relation |
| Sources | `exercise_sources` | exercise_id, source_id |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/exercises/:id` | Full exercise detail |
| GET | `/api/v1/exercises/:id/progressions` | Progression/regression chain |
| GET | `/api/v1/exercises/:id/related` | Related exercises (same muscles/patterns) |

---

## SCREEN 8: DASHBOARD / HOME

**Route:** `/dashboard`
**Layout:** `SB` — sidebar nav + content area
**Permission:** Authenticated (all tiers)
**Phase:** MVP

### States

| State | Description |
|-------|-------------|
| `DASH.default` | Dashboard with today's suggestion, recent activity, stats, streaks |
| `DASH.loading` | Skeleton cards while fetching |
| `DASH.first_visit` | Post-onboarding — "Generate your first workout!" prominent CTA |
| `DASH.rest_day` | AI suggests rest — "Recovery day. Here's some mobility work if you want it." |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| AI Suggestion Card | `card` | top/hero | "Today's suggestion: Upper Body Push — 45 min" with reasoning based on recent history. CTA: "Generate" or "Customise" |
| Quick Generate Button | `button` | top-right | "Quick Workout" — opens AI generator with one click |
| Streak Counter | `stat_card` | stats row | Current streak (days), longest streak, fire emoji animation on active streak |
| Weekly Volume Chart | `chart` | stats row | Mini bar chart — this week's volume by muscle group vs target |
| Recent Workouts | `list` | main | Last 5 workouts: date, name, duration, volume. Click to view details or repeat |
| Upcoming Schedule | `calendar` | sidebar or main | Next 7 days — AI-suggested workout types based on recovery and goals |
| PR Highlights | `card` | stats row | Recent personal records with celebrations |
| Body Metrics Summary | `stat_card` | stats row | Current weight, trend arrow, days since last measurement |
| Quick Actions | `button_group` | below hero | "Generate Workout", "Browse Exercises", "View Progress", "Update Goals" |

### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `DASH.modal.quick_generate` | "Quick Workout" button | Circumstance inputs (time, equipment, energy) → instant generation |
| `DASH.modal.log_weight` | Weight stat card click | Quick body weight logger |

### Features

| Feature | Description |
|---------|-------------|
| AI daily suggestion | Based on workout history, recovery patterns, and goals |
| Streak tracking | Gamification — consecutive workout days |
| Weekly muscle coverage | Visual of which muscles need attention |
| Quick generation | One-tap to start AI workout generation |

### Benefits

| Benefit | Who | Impact |
|---------|-----|--------|
| Removes decision fatigue | Daily users | Open app → see what to do → do it |
| Streak motivation | All users | Habit formation through visible streaks |
| Recovery awareness | Active users | AI prevents overtraining by suggesting rest |

### Data

| Entity | Table | Key Fields |
|--------|-------|------------|
| Dashboard cache | `user_dashboard_state` | user_id, last_workout, current_streak, weekly_volume |
| Streaks | `user_streaks` | user_id, current_streak, longest_streak, last_workout_date |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/dashboard` | Aggregated dashboard data |
| GET | `/api/v1/dashboard/suggestion` | AI daily workout suggestion |
| GET | `/api/v1/dashboard/recent` | Recent workouts |
| GET | `/api/v1/dashboard/streaks` | Streak data |

---

## SCREEN 9: PROGRESS & HISTORY

**Route:** `/progress`
**Layout:** `SB` — sidebar nav + tabbed content
**Permission:** Free (basic), Premium (advanced analytics, photos)
**Phase:** MVP

### States

| State | Description |
|-------|-------------|
| `PRG.overview` | Summary dashboard — key charts, PRs, body metrics |
| `PRG.workouts` | Workout history list — filterable by date, type, muscle group |
| `PRG.body` | Body metrics — weight chart, measurements, progress photos |
| `PRG.records` | Personal records — per exercise, sortable |
| `PRG.analytics` | Advanced analytics (Premium) — volume trends, frequency heatmap, muscle balance |
| `PRG.empty` | No data yet — "Complete your first workout to see progress" |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Tab Navigation | `tabs` | top | Overview, Workouts, Body, Records, Analytics |
| Volume Chart | `chart` | overview | Line/bar chart — total volume over weeks/months |
| Frequency Heatmap | `heatmap` | overview | GitHub-style calendar showing workout days |
| PR Board | `card_grid` | records tab | Per-exercise PR cards: exercise name, best weight × reps, date achieved |
| Weight Trend | `chart` | body tab | Line chart with trend line, goal line |
| Measurement Log | `table` | body tab | Date, chest, waist, biceps, thighs — with change deltas |
| Progress Photos | `gallery` | body tab (Premium) | Timeline of progress photos, before/after comparison slider |
| Workout History List | `list` | workouts tab | Paginated list: date, workout name, duration, volume, exercises. Expandable to see sets |
| Muscle Balance Chart | `radar` | analytics tab (Premium) | Radar chart showing volume distribution across muscle groups |
| Exercise Frequency | `bar_chart` | analytics tab | Most performed exercises ranked |
| Export Button | `button` | top-right | Export data as CSV |

### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `PRG.modal.add_photo` | "Add Photo" button | Camera/upload photo, select date, body part tag |
| `PRG.modal.add_measurement` | "Log Measurement" button | Body measurement form: weight, chest, waist, arms, legs, etc. |
| `PRG.modal.workout_detail` | Click workout in history | Full workout detail: every exercise, every set, notes |

### Features

| Feature | Description |
|---------|-------------|
| Multi-dimensional progress tracking | Volume, frequency, body metrics, PRs — all in one place |
| GitHub-style heatmap | Visual consistency tracker |
| Progress photos with comparison | Before/after slider |
| Per-exercise PR history | Track personal bests over time |
| Data export | CSV export for external analysis |

### Benefits

| Benefit | Who | Impact |
|---------|-----|--------|
| Visible progress | All users | Seeing improvement = continued motivation |
| Body composition tracking | Weight management users | Track changes beyond the scale |
| Training insight | Advanced users | Identify imbalances, adjust programming |

### Data

| Entity | Table | Key Fields |
|--------|-------|------------|
| Body measurements | `body_measurements` | user_id, date, weight_kg, chest_cm, waist_cm, bicep_cm, thigh_cm |
| Progress photos | `progress_photos` | user_id, date, photo_url, body_part_tag |
| Aggregated stats | `user_analytics_cache` | user_id, period, total_volume, workout_count, muscle_distribution |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/progress/overview` | Dashboard aggregates |
| GET | `/api/v1/progress/workouts` | Workout history (paginated, filterable) |
| GET | `/api/v1/progress/body` | Body measurements history |
| POST | `/api/v1/progress/body` | Log new measurement |
| GET | `/api/v1/progress/records` | Personal records list |
| GET | `/api/v1/progress/analytics` | Advanced analytics data |
| POST | `/api/v1/progress/photos` | Upload progress photo |
| GET | `/api/v1/progress/export` | CSV export |

---

## SCREEN 10: SETTINGS / PROFILE

**Route:** `/settings`
**Layout:** `SB` — sidebar nav + form content
**Permission:** Authenticated
**Phase:** MVP

### States

| State | Description |
|-------|-------------|
| `SET.profile` | Personal info — name, email, avatar |
| `SET.fitness` | Fitness profile — goals, experience, equipment, injuries (re-do onboarding) |
| `SET.preferences` | App preferences — units (kg/lbs), rest timer defaults, notification settings |
| `SET.subscription` | Subscription management — current plan, upgrade/downgrade, billing |
| `SET.data` | Data management — export all data, delete account |
| `SET.notifications` | Notification preferences — workout reminders, PR alerts, rest day suggestions |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Settings Nav | `list` | sidebar | Profile, Fitness, Preferences, Subscription, Notifications, Data |
| Profile Form | `form` | main | Name, email, avatar upload, password change |
| Fitness Profile Form | `form` | main | Goals, experience, equipment, injuries — same as onboarding but editable |
| Unit Toggle | `toggle` | preferences | kg/lbs, km/miles |
| Rest Timer Default | `slider` | preferences | Default rest time between sets (30s-5min) |
| Subscription Card | `card` | subscription | Current plan, features, next billing date, "Upgrade" / "Manage" |
| Notification Toggles | `toggle_group` | notifications | Workout reminders, PR notifications, rest day suggestions, weekly summary |
| Export Data Button | `button` | data | "Export All My Data" — generates downloadable JSON/CSV |
| Delete Account | `button` | data | "Delete Account" — dangerous action with confirmation |

### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `SET.modal.delete_account` | Delete Account button | "This will permanently delete all your data. Type DELETE to confirm." |
| `SET.modal.upgrade` | "Upgrade" button | Pricing comparison + payment form (Stripe) |
| `SET.modal.change_password` | "Change Password" link | Current password + new password + confirm |

### Features

| Feature | Description |
|---------|-------------|
| Editable fitness profile | Update goals, equipment, injuries as circumstances change — feeds back to AI |
| Unit preferences | kg/lbs toggle for international users |
| Subscription management | Self-serve upgrade/downgrade |
| Data portability | Full data export |
| Account deletion | GDPR-compliant data deletion |

### Benefits

| Benefit | Who | Impact |
|---------|-----|--------|
| Circumstance updates | All users | Got a home gym? Update equipment → AI adapts immediately |
| Self-serve billing | Premium users | No support tickets for plan changes |
| Trust through data control | All users | Export and delete builds confidence |

### Data

| Entity | Table | Key Fields |
|--------|-------|------------|
| User settings | `user_settings` | user_id, units, default_rest_seconds, notification_prefs |
| Subscriptions | `subscriptions` | user_id, plan, stripe_customer_id, current_period_end |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/settings/profile` | Get user profile |
| PATCH | `/api/v1/settings/profile` | Update profile |
| PATCH | `/api/v1/settings/fitness` | Update fitness profile |
| PATCH | `/api/v1/settings/preferences` | Update preferences |
| GET | `/api/v1/settings/subscription` | Get subscription status |
| POST | `/api/v1/settings/subscription/upgrade` | Upgrade plan |
| POST | `/api/v1/settings/subscription/cancel` | Cancel subscription |
| GET | `/api/v1/settings/export` | Export all user data |
| DELETE | `/api/v1/settings/account` | Delete account |

---

## SCREEN 11: TRAINER / INFLUENCER PROFILES (Phase 2 — Marketplace)

**Route:** `/trainers`
**Layout:** `SB` — filter sidebar + card grid
**Permission:** All tiers
**Phase:** P2

### States

| State | Description |
|-------|-------------|
| `TRN.default` | Directory of trainers/influencers — grid with search + filters |
| `TRN.filtered` | Applied filters — speciality, location, price range, rating |
| `TRN.empty` | No trainers matching filters |
| `TRN.loading` | Skeleton cards |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Search Bar | `input` | top | Search by name, speciality, location |
| Filter Sidebar | `sidebar` | left | Speciality (strength, mobility, etc.), Price range, Rating, Location, Certification |
| Trainer Card | `card` | main grid | Photo, name, speciality badges, rating stars, price range, program count, "View Profile" CTA |
| Featured Trainers | `carousel` | top of grid | Highlighted/promoted trainers |
| Sort Dropdown | `select` | top-right | Rating, Price, Most Programs, Newest |

### Modals

None — cards navigate to Trainer Detail.

### Features

| Feature | Description |
|---------|-------------|
| Trainer marketplace | Connect users with qualified trainers and influencers |
| Multi-filter directory | Find trainers by speciality, price, rating |
| Featured placement | Revenue opportunity for trainer promotion |

### Benefits

| Benefit | Who | Impact |
|---------|-----|--------|
| Expert guidance | Users wanting coaching | Access to qualified trainers |
| Client acquisition | Trainers | New revenue channel |
| Platform stickiness | All users | More reasons to stay on platform |

### Data

| Entity | Table | Key Fields |
|--------|-------|------------|
| Trainer profiles | `trainer_profiles` | user_id, bio, certifications, specialities[], hourly_rate, featured |
| Reviews | `trainer_reviews` | trainer_id, reviewer_id, rating, review_text |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/trainers` | List trainers (paginated, filterable) |
| GET | `/api/v1/trainers/featured` | Featured trainers |

---

## SCREEN 12: TRAINER DETAIL (Phase 2)

**Route:** `/trainers/:id`
**Layout:** `SB` — profile content + sidebar actions
**Permission:** All tiers
**Phase:** P2

### States

| State | Description |
|-------|-------------|
| `TRD.default` | Full trainer profile — bio, certifications, programs, reviews |
| `TRD.loading` | Skeleton layout |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Trainer Header | `hero` | top | Photo, name, speciality badges, rating, location |
| Bio Section | `text` | main | Trainer bio, philosophy, experience |
| Certifications | `badge_group` | main | Verified certification badges |
| Programs List | `card_grid` | main | Programs offered with price, duration, difficulty |
| Reviews | `list` | main | Rating stars + review text, paginated |
| Contact / Book CTA | `button` | sidebar | "Message", "Book Session", pricing info |
| Stats | `stat_group` | sidebar | Programs sold, average rating, years experience |

### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `TRD.modal.contact` | "Message" button | Message form to trainer |
| `TRD.modal.book` | "Book Session" button | Calendar + time slot picker + payment |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/trainers/:id` | Full trainer profile |
| GET | `/api/v1/trainers/:id/programs` | Trainer's programs |
| GET | `/api/v1/trainers/:id/reviews` | Trainer reviews |
| POST | `/api/v1/trainers/:id/contact` | Send message to trainer |

---

## SCREEN 13: PRE-BUILT PROGRAMS (Phase 2 — Marketplace)

**Route:** `/programs`
**Layout:** `SB` — filter + card grid
**Permission:** Free (browse), Premium (follow free programs), Purchase (paid programs)
**Phase:** P2

### States

| State | Description |
|-------|-------------|
| `PGM.default` | Program directory — grid with filters |
| `PGM.filtered` | Filtered results |
| `PGM.empty` | No matching programs |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Search Bar | `input` | top | Search programs by name, trainer, goal |
| Filter Sidebar | `sidebar` | left | Goal, Duration (weeks), Difficulty, Equipment, Price (free/paid), Trainer |
| Program Card | `card` | main grid | Cover image, name, trainer avatar + name, duration, difficulty, price, rating, "View" CTA |
| Category Tabs | `tabs` | above grid | All, Strength, Hypertrophy, Weight Loss, Mobility, Sport-Specific |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/programs` | List programs (paginated, filterable) |
| GET | `/api/v1/programs/categories` | Program categories |

---

## SCREEN 14: PROGRAM DETAIL / FLOW (Phase 2)

**Route:** `/programs/:id`
**Layout:** `SB` — program content + sidebar actions
**Permission:** As per program pricing
**Phase:** P2

### States

| State | Description |
|-------|-------------|
| `PGD.preview` | Program overview — description, schedule preview, reviews. "Start Program" CTA |
| `PGD.active` | Following program — current week highlighted, today's workout, progress through program |
| `PGD.week_view` | Expanded week — daily workouts listed with exercises |
| `PGD.completed` | Program finished — results summary, review prompt, next program suggestions |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Program Header | `hero` | top | Cover, title, trainer, duration, difficulty, price |
| Program Description | `text` | main | What the program is, who it's for, expected results |
| Weekly Schedule | `accordion` | main | Expandable weeks showing daily workout summaries |
| Current Week Card | `card` | main (active) | Highlighted current week with today's workout prominent |
| Start/Buy Button | `button` | sidebar | "Start Program" (free) or "Buy £X" (paid) |
| Progress Bar | `progress` | sidebar (active) | Week X of Y completed |
| Reviews | `list` | bottom | User reviews and ratings |
| Trainer Card | `card` | sidebar | Mini trainer profile with link |

### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `PGD.modal.purchase` | "Buy" button | Stripe checkout for paid programs |
| `PGD.modal.review` | Program completion | Rate and review the program |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/programs/:id` | Full program detail |
| POST | `/api/v1/programs/:id/start` | Start following program |
| POST | `/api/v1/programs/:id/purchase` | Purchase paid program |
| GET | `/api/v1/programs/:id/progress` | User's progress in program |
| POST | `/api/v1/programs/:id/review` | Submit review |

---

## SCREEN 15: SOCIAL FEED (Phase 2)

**Route:** `/social`
**Layout:** `SB` — sidebar + feed
**Permission:** Authenticated (all tiers)
**Phase:** P2

### States

| State | Description |
|-------|-------------|
| `SOC.feed` | Chronological feed of posts from followed users and community |
| `SOC.discover` | Trending posts, popular workouts, suggested users |
| `SOC.empty` | No posts — "Follow some athletes or share your first workout" |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Feed Toggle | `tabs` | top | Following, Discover |
| Post Card | `card` | feed | User avatar, name, post text, shared workout summary, progress photo, likes, comments |
| Create Post Button | `button` | floating | "Share" — share a workout, achievement, or text post |
| Like/Comment Actions | `button_group` | per post | Heart + comment count + share |
| Comment Thread | `list` | expanded post | Threaded comments |
| Suggested Users | `card_list` | sidebar | "People to follow" based on similar training styles |

### Modals

| Modal | Trigger | Content |
|-------|---------|---------|
| `SOC.modal.create_post` | "Share" button | Post creator: text, attach workout, attach photo, visibility settings |
| `SOC.modal.share_workout` | "Share Workout" from post-workout | Pre-filled with workout summary |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/social/feed` | User's feed (paginated) |
| GET | `/api/v1/social/discover` | Trending/discover feed |
| POST | `/api/v1/social/posts` | Create post |
| POST | `/api/v1/social/posts/:id/like` | Like a post |
| POST | `/api/v1/social/posts/:id/comments` | Comment on post |
| POST | `/api/v1/social/follow/:user_id` | Follow user |

---

## SCREEN 16: USER PROFILE (Public — Phase 2)

**Route:** `/users/:id`
**Layout:** `SB` — profile content
**Permission:** Public (limited), Authenticated (full)
**Phase:** P2

### States

| State | Description |
|-------|-------------|
| `USR.default` | Public profile — stats, shared workouts, achievements, followers |
| `USR.own` | Own profile — edit button visible, private stats shown |

### Components

| Component | Type | Location | Details |
|-----------|------|----------|---------|
| Profile Header | `hero` | top | Avatar, name, bio, join date, follower/following counts |
| Stats Grid | `stat_group` | below header | Total workouts, current streak, PRs count, favourite pillar |
| Achievement Badges | `badge_grid` | main | Earned badges: "100 Workouts", "30-Day Streak", "First PR", etc. |
| Shared Workouts | `list` | main | Public workouts shared by user |
| Follow/Message Buttons | `button_group` | header | "Follow" / "Message" (or "Edit Profile" if own) |

### API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1/users/:id/profile` | Public profile data |
| GET | `/api/v1/users/:id/workouts` | User's shared workouts |
| GET | `/api/v1/users/:id/achievements` | User's achievement badges |

---

## DATABASE ARCHITECTURE

### Full PostgreSQL DDL

```sql
-- ============================================================
-- TAXONOMY TABLES (Reference Data)
-- ============================================================

CREATE TABLE IF NOT EXISTS movement_planes (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE NOT NULL  -- sagittal, frontal, transverse, multiplanar
);

CREATE TABLE IF NOT EXISTS movement_patterns (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE NOT NULL  -- squat, hinge, lunge, push, pull, carry, rotation, anti-rotation, gait, crawl, jump, throw
);

CREATE TABLE IF NOT EXISTS modalities (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE NOT NULL  -- strength, endurance, cardio, explosive/power, mobility, flexibility, balance, agility, coordination, rehab, isometric
);

CREATE TABLE IF NOT EXISTS equipment (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE NOT NULL  -- bodyweight, barbell, dumbbell, kettlebell, band, machine, rings, TRX, cable, etc.
);

CREATE TABLE IF NOT EXISTS energy_systems (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE NOT NULL  -- alactic, lactic, aerobic
);

CREATE TABLE IF NOT EXISTS muscle_groups (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE NOT NULL  -- chest, back, shoulders, biceps, triceps, quads, hamstrings, glutes, calves, core, forearms, neck
);

CREATE TABLE IF NOT EXISTS muscles (
  id SERIAL PRIMARY KEY,
  group_id INT REFERENCES muscle_groups(id) ON DELETE SET NULL,
  name TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS exercise_pillars (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE NOT NULL,  -- Kettlebells, Hypertrophy, Strength, Power, Plyometrics, etc. (30 pillars)
  description TEXT
);

-- ============================================================
-- EXERCISE LIBRARY
-- ============================================================

CREATE TABLE IF NOT EXISTS sources (
  id SERIAL PRIMARY KEY,
  type TEXT CHECK (type IN ('pdf', 'book', 'youtube', 'website', 'other')),
  title TEXT,
  author TEXT,
  url TEXT,
  publisher TEXT,
  published_at DATE
);

CREATE TABLE IF NOT EXISTS exercises (
  id BIGSERIAL PRIMARY KEY,
  slug TEXT UNIQUE,
  name TEXT NOT NULL,
  description TEXT,
  purpose TEXT[],
  difficulty TEXT CHECK (difficulty IN ('beginner', 'intermediate', 'advanced', 'elite')),
  progression_level SMALLINT CHECK (progression_level BETWEEN 1 AND 10),
  isometric BOOLEAN DEFAULT FALSE,
  unilateral BOOLEAN DEFAULT FALSE,
  dynamic BOOLEAN DEFAULT TRUE,
  cues TEXT[],
  steps TEXT[],
  common_mistakes TEXT[],
  contraindications TEXT[],
  tempo TEXT,
  load_type TEXT,
  pillar_id INT REFERENCES exercise_pillars(id),
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS exercise_aliases (
  exercise_id BIGINT REFERENCES exercises(id) ON DELETE CASCADE,
  alias TEXT NOT NULL,
  PRIMARY KEY (exercise_id, alias)
);

CREATE TABLE IF NOT EXISTS exercise_muscles (
  exercise_id BIGINT REFERENCES exercises(id) ON DELETE CASCADE,
  muscle_id INT REFERENCES muscles(id) ON DELETE CASCADE,
  role TEXT CHECK (role IN ('primary', 'secondary', 'stabilizer')),
  PRIMARY KEY (exercise_id, muscle_id, role)
);

CREATE TABLE IF NOT EXISTS exercise_patterns (
  exercise_id BIGINT REFERENCES exercises(id) ON DELETE CASCADE,
  pattern_id INT REFERENCES movement_patterns(id) ON DELETE CASCADE,
  PRIMARY KEY (exercise_id, pattern_id)
);

CREATE TABLE IF NOT EXISTS exercise_planes (
  exercise_id BIGINT REFERENCES exercises(id) ON DELETE CASCADE,
  plane_id INT REFERENCES movement_planes(id) ON DELETE CASCADE,
  PRIMARY KEY (exercise_id, plane_id)
);

CREATE TABLE IF NOT EXISTS exercise_modalities (
  exercise_id BIGINT REFERENCES exercises(id) ON DELETE CASCADE,
  modality_id INT REFERENCES modalities(id) ON DELETE CASCADE,
  PRIMARY KEY (exercise_id, modality_id)
);

CREATE TABLE IF NOT EXISTS exercise_equipment (
  exercise_id BIGINT REFERENCES exercises(id) ON DELETE CASCADE,
  equipment_id INT REFERENCES equipment(id) ON DELETE CASCADE,
  PRIMARY KEY (exercise_id, equipment_id)
);

CREATE TABLE IF NOT EXISTS exercise_energy_systems (
  exercise_id BIGINT REFERENCES exercises(id) ON DELETE CASCADE,
  energy_id INT REFERENCES energy_systems(id) ON DELETE CASCADE,
  PRIMARY KEY (exercise_id, energy_id)
);

CREATE TABLE IF NOT EXISTS media (
  id BIGSERIAL PRIMARY KEY,
  exercise_id BIGINT REFERENCES exercises(id) ON DELETE CASCADE,
  type TEXT CHECK (type IN ('image', 'video')),
  uri TEXT NOT NULL,
  start_seconds NUMERIC,
  end_seconds NUMERIC,
  thumbnail TEXT,
  license TEXT,
  attribution TEXT
);

CREATE TABLE IF NOT EXISTS exercise_sources (
  exercise_id BIGINT REFERENCES exercises(id) ON DELETE CASCADE,
  source_id INT REFERENCES sources(id) ON DELETE CASCADE,
  notes TEXT,
  PRIMARY KEY (exercise_id, source_id)
);

CREATE TABLE IF NOT EXISTS progressions (
  from_exercise BIGINT REFERENCES exercises(id) ON DELETE CASCADE,
  to_exercise BIGINT REFERENCES exercises(id) ON DELETE CASCADE,
  relation TEXT CHECK (relation IN ('regression', 'progression')) NOT NULL,
  PRIMARY KEY (from_exercise, to_exercise, relation)
);

-- ============================================================
-- USER SYSTEM
-- ============================================================

CREATE TABLE IF NOT EXISTS users (
  id BIGSERIAL PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT,
  name TEXT,
  avatar_url TEXT,
  email_verified BOOLEAN DEFAULT FALSE,
  oauth_provider TEXT,
  oauth_id TEXT,
  subscription_tier TEXT DEFAULT 'free' CHECK (subscription_tier IN ('free', 'premium', 'trainer')),
  stripe_customer_id TEXT,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS user_profiles (
  user_id BIGINT PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
  goals TEXT[],
  experience_level TEXT CHECK (experience_level IN ('beginner', 'intermediate', 'advanced')),
  equipment TEXT[],
  preferred_pillars TEXT[],
  preferred_modalities TEXT[],
  schedule_days INT DEFAULT 4,
  session_duration_min INT DEFAULT 45,
  onboarding_completed BOOLEAN DEFAULT FALSE,
  updated_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS user_injuries (
  id SERIAL PRIMARY KEY,
  user_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
  body_area TEXT NOT NULL,
  severity TEXT CHECK (severity IN ('mild', 'moderate', 'severe')),
  notes TEXT,
  active BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS user_settings (
  user_id BIGINT PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
  units TEXT DEFAULT 'metric' CHECK (units IN ('metric', 'imperial')),
  default_rest_seconds INT DEFAULT 90,
  notification_workout_reminder BOOLEAN DEFAULT TRUE,
  notification_pr_alerts BOOLEAN DEFAULT TRUE,
  notification_rest_day BOOLEAN DEFAULT TRUE,
  notification_weekly_summary BOOLEAN DEFAULT TRUE
);

-- ============================================================
-- WORKOUT TRACKING
-- ============================================================

CREATE TABLE IF NOT EXISTS generated_workouts (
  id BIGSERIAL PRIMARY KEY,
  user_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
  prompt TEXT,
  workout_data JSONB NOT NULL,  -- Full workout structure: exercises, sets, reps, rest
  ai_reasoning TEXT,
  generated_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS generation_chat_log (
  id BIGSERIAL PRIMARY KEY,
  workout_id BIGINT REFERENCES generated_workouts(id) ON DELETE CASCADE,
  role TEXT CHECK (role IN ('user', 'assistant', 'system')),
  content TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS user_generation_count (
  user_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
  date DATE NOT NULL,
  count INT DEFAULT 0,
  PRIMARY KEY (user_id, date)
);

CREATE TABLE IF NOT EXISTS user_workouts (
  id BIGSERIAL PRIMARY KEY,
  user_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
  generated_workout_id BIGINT REFERENCES generated_workouts(id),
  program_id BIGINT,  -- FK to programs if following a program
  name TEXT,
  started_at TIMESTAMPTZ NOT NULL,
  completed_at TIMESTAMPTZ,
  status TEXT DEFAULT 'in_progress' CHECK (status IN ('in_progress', 'completed', 'abandoned')),
  total_volume_kg NUMERIC,
  duration_minutes INT,
  notes TEXT
);

CREATE TABLE IF NOT EXISTS workout_sets (
  id BIGSERIAL PRIMARY KEY,
  user_workout_id BIGINT REFERENCES user_workouts(id) ON DELETE CASCADE,
  exercise_id BIGINT REFERENCES exercises(id),
  set_number INT NOT NULL,
  weight_kg NUMERIC,
  reps INT,
  rpe NUMERIC CHECK (rpe BETWEEN 1 AND 10),
  time_seconds INT,
  distance_meters INT,
  rest_seconds INT,
  notes TEXT,
  logged_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS workout_notes (
  id BIGSERIAL PRIMARY KEY,
  user_workout_id BIGINT REFERENCES user_workouts(id) ON DELETE CASCADE,
  exercise_id BIGINT REFERENCES exercises(id),
  note TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS personal_records (
  id BIGSERIAL PRIMARY KEY,
  user_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
  exercise_id BIGINT REFERENCES exercises(id),
  metric TEXT CHECK (metric IN ('weight', 'reps', 'volume', 'time', 'distance')),
  value NUMERIC NOT NULL,
  achieved_at TIMESTAMPTZ DEFAULT now()
);

-- ============================================================
-- BODY TRACKING
-- ============================================================

CREATE TABLE IF NOT EXISTS body_measurements (
  id BIGSERIAL PRIMARY KEY,
  user_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
  date DATE NOT NULL,
  weight_kg NUMERIC,
  chest_cm NUMERIC,
  waist_cm NUMERIC,
  hips_cm NUMERIC,
  bicep_left_cm NUMERIC,
  bicep_right_cm NUMERIC,
  thigh_left_cm NUMERIC,
  thigh_right_cm NUMERIC,
  body_fat_pct NUMERIC,
  notes TEXT
);

CREATE TABLE IF NOT EXISTS progress_photos (
  id BIGSERIAL PRIMARY KEY,
  user_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
  date DATE NOT NULL,
  photo_url TEXT NOT NULL,
  body_part_tag TEXT,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- ============================================================
-- STREAKS & ACHIEVEMENTS
-- ============================================================

CREATE TABLE IF NOT EXISTS user_streaks (
  user_id BIGINT PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
  current_streak INT DEFAULT 0,
  longest_streak INT DEFAULT 0,
  last_workout_date DATE
);

CREATE TABLE IF NOT EXISTS achievements (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE NOT NULL,
  description TEXT,
  icon TEXT,
  criteria JSONB  -- {"type": "workout_count", "threshold": 100}
);

CREATE TABLE IF NOT EXISTS user_achievements (
  user_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
  achievement_id INT REFERENCES achievements(id),
  earned_at TIMESTAMPTZ DEFAULT now(),
  PRIMARY KEY (user_id, achievement_id)
);

-- ============================================================
-- SUBSCRIPTIONS
-- ============================================================

CREATE TABLE IF NOT EXISTS subscriptions (
  id BIGSERIAL PRIMARY KEY,
  user_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
  plan TEXT CHECK (plan IN ('free', 'premium', 'trainer')),
  stripe_subscription_id TEXT,
  status TEXT CHECK (status IN ('active', 'cancelled', 'past_due', 'trialing')),
  current_period_start TIMESTAMPTZ,
  current_period_end TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- ============================================================
-- SOCIAL (Phase 2)
-- ============================================================

CREATE TABLE IF NOT EXISTS social_posts (
  id BIGSERIAL PRIMARY KEY,
  user_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
  content TEXT,
  workout_id BIGINT REFERENCES user_workouts(id),
  photo_url TEXT,
  likes_count INT DEFAULT 0,
  comments_count INT DEFAULT 0,
  visibility TEXT DEFAULT 'public' CHECK (visibility IN ('public', 'followers', 'private')),
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS social_likes (
  user_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
  post_id BIGINT REFERENCES social_posts(id) ON DELETE CASCADE,
  created_at TIMESTAMPTZ DEFAULT now(),
  PRIMARY KEY (user_id, post_id)
);

CREATE TABLE IF NOT EXISTS social_comments (
  id BIGSERIAL PRIMARY KEY,
  post_id BIGINT REFERENCES social_posts(id) ON DELETE CASCADE,
  user_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
  content TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS social_follows (
  follower_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
  following_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
  created_at TIMESTAMPTZ DEFAULT now(),
  PRIMARY KEY (follower_id, following_id)
);

-- ============================================================
-- MARKETPLACE (Phase 2)
-- ============================================================

CREATE TABLE IF NOT EXISTS trainer_profiles (
  user_id BIGINT PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
  bio TEXT,
  certifications TEXT[],
  specialities TEXT[],
  hourly_rate NUMERIC,
  featured BOOLEAN DEFAULT FALSE,
  location TEXT,
  verified BOOLEAN DEFAULT FALSE,
  rating_avg NUMERIC DEFAULT 0,
  review_count INT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS programs (
  id BIGSERIAL PRIMARY KEY,
  trainer_id BIGINT REFERENCES users(id),
  name TEXT NOT NULL,
  description TEXT,
  duration_weeks INT,
  difficulty TEXT,
  goals TEXT[],
  equipment TEXT[],
  price NUMERIC DEFAULT 0,  -- 0 = free
  rating_avg NUMERIC DEFAULT 0,
  review_count INT DEFAULT 0,
  published BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS program_weeks (
  id BIGSERIAL PRIMARY KEY,
  program_id BIGINT REFERENCES programs(id) ON DELETE CASCADE,
  week_number INT NOT NULL,
  focus TEXT
);

CREATE TABLE IF NOT EXISTS program_workouts (
  id BIGSERIAL PRIMARY KEY,
  week_id BIGINT REFERENCES program_weeks(id) ON DELETE CASCADE,
  day_of_week INT,  -- 1=Mon, 7=Sun
  workout_data JSONB NOT NULL
);

CREATE TABLE IF NOT EXISTS user_programs (
  user_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
  program_id BIGINT REFERENCES programs(id) ON DELETE CASCADE,
  started_at TIMESTAMPTZ DEFAULT now(),
  current_week INT DEFAULT 1,
  status TEXT DEFAULT 'active' CHECK (status IN ('active', 'paused', 'completed', 'abandoned')),
  PRIMARY KEY (user_id, program_id)
);

CREATE TABLE IF NOT EXISTS trainer_reviews (
  id BIGSERIAL PRIMARY KEY,
  trainer_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
  reviewer_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
  rating INT CHECK (rating BETWEEN 1 AND 5),
  review_text TEXT,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE IF NOT EXISTS program_reviews (
  id BIGSERIAL PRIMARY KEY,
  program_id BIGINT REFERENCES programs(id) ON DELETE CASCADE,
  reviewer_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
  rating INT CHECK (rating BETWEEN 1 AND 5),
  review_text TEXT,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- ============================================================
-- INDEXES
-- ============================================================

CREATE INDEX idx_exercises_slug ON exercises(slug);
CREATE INDEX idx_exercises_name ON exercises(name);
CREATE INDEX idx_exercises_difficulty ON exercises(difficulty);
CREATE INDEX idx_exercises_pillar ON exercises(pillar_id);
CREATE INDEX idx_exercise_muscles_muscle ON exercise_muscles(muscle_id);
CREATE INDEX idx_exercise_patterns_pattern ON exercise_patterns(pattern_id);
CREATE INDEX idx_exercise_equipment_equip ON exercise_equipment(equipment_id);
CREATE INDEX idx_user_workouts_user ON user_workouts(user_id);
CREATE INDEX idx_user_workouts_date ON user_workouts(started_at);
CREATE INDEX idx_workout_sets_workout ON workout_sets(user_workout_id);
CREATE INDEX idx_workout_sets_exercise ON workout_sets(exercise_id);
CREATE INDEX idx_personal_records_user ON personal_records(user_id);
CREATE INDEX idx_personal_records_exercise ON personal_records(exercise_id);
CREATE INDEX idx_generated_workouts_user ON generated_workouts(user_id);
CREATE INDEX idx_body_measurements_user ON body_measurements(user_id);
CREATE INDEX idx_social_posts_user ON social_posts(user_id);
CREATE INDEX idx_social_posts_created ON social_posts(created_at);
CREATE INDEX idx_programs_trainer ON programs(trainer_id);
```

---

## 30 EXERCISE PILLARS

The exercise database spans 30 training domains, each with full breakdowns, variables, and movement variants:

| # | Pillar | Focus | Example Exercises |
|---|--------|-------|-------------------|
| 01 | Kettlebells | Ballistic + grind KB work | Swings, cleans, snatches, TGU, windmills |
| 02 | Hypertrophy | Muscle growth protocols | Compound + isolation, volume work |
| 03 | Strength | Max force production | Squat, bench, deadlift, press |
| 04 | Power | Rate of force development | Clean & jerk, box jumps, med ball throws |
| 05 | Plyometrics | Reactive training | Depth jumps, bounds, hurdle hops |
| 06 | Powerlifting | Competition lifts | Squat, bench, deadlift + accessories |
| 07 | Olympic Lifting | Snatch + clean & jerk | Full lifts + variations + pulls |
| 08 | Bodyweight | No-equipment training | Push-ups, pull-ups, squats, dips |
| 09 | Calisthenics | Progressive bodyweight | Levers, planches, muscle-ups, flags |
| 10 | Gymnastic Strength | GST methodology | Rings, handstands, L-sits, holds |
| 11 | Movement & Locomotion | Animal flow, crawling | Bear crawl, crab walk, animal flows |
| 12 | Flexibility | Static + PNF stretching | Splits, backbends, stretch routines |
| 13 | Mobility | Joint range + control | CARs, PAILs/RAILs, joint circles |
| 14 | Isometrics | Static holds | Planks, wall sits, iso holds |
| 15 | Balance | Stability training | Single-leg, balance board, BOSU |
| 16 | Agility | Change of direction | Ladders, cone drills, shuttle runs |
| 17 | Jump Rope | Skipping protocols | Single/double unders, crossovers |
| 18 | Bands | Resistance band work | Banded pulls, presses, rehab |
| 19 | Rope Flow | Flow training | Patterns, combinations, rhythmic |
| 20 | Clubs & Mace | Unconventional tools | Steel mace, Indian clubs, flows |
| 21 | Conditioning | Energy system work | Circuits, intervals, complexes |
| 22 | Yoga & Somatics | Mind-body practice | Vinyasa, yin, somatic movements |
| 23 | Breathwork | Respiratory training | Wim Hof, box breathing, nasal |
| 24 | Prehab & Rehab | Injury prevention + recovery | Rotator cuff, knee stability, back |
| 25 | Core | Trunk stability + strength | Anti-extension, anti-rotation, flexion |
| 26 | Grip | Hand/forearm strength | Pinch, crush, hang, wrist work |
| 27 | Neck | Neck strength + mobility | Neck curls, bridges, isometric |
| 28 | Warm-Up & Cool-Down | Session bookends | Dynamic warm-up, cool-down flows |
| 29 | Nervous System | CNS training + regulation | Vagal toning, reflexive stability |
| 30 | Sleep & Recovery | Rest protocols | Sleep hygiene, recovery modalities |

---

## TECHNICAL ARCHITECTURE

### Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Frontend | Next.js 16 + React 19 | SSR, routing, app shell |
| Styling | Tailwind CSS v4 | Utility-first CSS |
| State | Zustand | Client state management |
| Database | PostgreSQL 16 | Primary data store |
| Vector | pgvector | Exercise semantic search + dedup |
| Cache | Redis | Session cache, rate limiting, generation counts |
| AI | Claude API (Anthropic) | Workout generation, exercise swapping, suggestions |
| Video | YouTube Data API v3 | Exercise video integration |
| Auth | NextAuth.js / Auth.js | Email + OAuth authentication |
| Payments | Stripe | Subscription billing |
| Storage | Cloudflare R2 / S3 | Progress photos, avatars |
| Hosting | Vercel | Frontend deployment |
| Monitoring | PostHog | Analytics + feature flags |

### Key Integrations

| Integration | Purpose | Cost |
|-------------|---------|------|
| Claude API | AI workout generation, exercise recommendations | Usage-based (~£0.01 per generation) |
| YouTube Data API v3 | Exercise video metadata + embed | 10,000 units/day free |
| Stripe | Subscription management + payments | 1.4% + 20p per transaction |
| Apple Health / Google Fit | Import external workout/health data (Phase 2) | Free |
| PostHog | Analytics, funnels, feature flags | Free tier generous |

---

## PRICING & REVENUE

| Tier | Price | Features |
|------|-------|----------|
| Free | £0 | 5 AI generations/day, basic exercise library (100), basic logging, 1 pre-built program |
| Premium | £9.99/mo or £79/yr | Unlimited AI, full library (500+), advanced analytics, progress photos, PRs, all programs, no ads |
| Trainer | £29/mo | Everything Premium + multi-client profiles, program creation, marketplace listing, custom branding |

### Revenue Targets

| Milestone | Users | Conversion | MRR |
|-----------|-------|-----------|-----|
| Month 3 | 500 | 5% (25 premium) | £250 |
| Month 6 | 5,000 | 7% (350 premium) | £3,500 |
| Month 12 | 50,000 | 10% (5,000 premium) | £50,000 |

---

## BUILD PHASES

### Phase 1: MVP (Months 1-3) — 10 Screens

| Sprint | Deliverables |
|--------|-------------|
| Sprint 1 (Wk 1-2) | Database setup (full DDL), Auth (email + Google), basic API structure |
| Sprint 2 (Wk 3-4) | Exercise library (seed 100+ exercises from pillar data), exercise detail, search + filters |
| Sprint 3 (Wk 5-6) | AI Workout Generator (Claude integration), chat interface, workout output cards |
| Sprint 4 (Wk 7-8) | Active Workout Mode (timer, set logging, video playback, PR detection) |
| Sprint 5 (Wk 9-10) | Dashboard, Progress & History, basic charts |
| Sprint 6 (Wk 11-12) | Settings, Onboarding, Landing page, Stripe integration, launch prep |

### Phase 2: Marketplace + Social (Months 4-6) — 6 Screens

| Sprint | Deliverables |
|--------|-------------|
| Sprint 7 | Trainer profiles, program structure, marketplace directory |
| Sprint 8 | Social feed, user profiles, follow system |
| Sprint 9 | Program purchasing (Stripe), advanced analytics, data export |

### Phase 3: Scale (Months 7-12)

- Mobile app (React Native)
- Wearable integrations (Apple Health, Google Fit, Garmin)
- AI form check (video upload analysis)
- Nutrition tracking integration
- White-label option for gyms
- API for third-party integrations

---

## SUCCESS METRICS

| Category | Metric | Target |
|----------|--------|--------|
| Engagement | DAU/MAU ratio | >20% |
| Engagement | Workouts logged per user/week | >3 |
| Engagement | Workout completion rate | >80% |
| Retention | D7 retention | >40% |
| Retention | D30 retention | >25% |
| Revenue | Free→Premium conversion | >10% |
| Revenue | Monthly churn (Premium) | <5% |
| Revenue | LTV:CAC ratio | >3:1 |
| Content | Exercise library size | 500+ by Month 6 |
| AI | Workout generation satisfaction | >4/5 stars |

---

*This specification provides full endpoint fidelity for every screen. Feed into UI Assembly Pipeline for component matching and development sprints.*
