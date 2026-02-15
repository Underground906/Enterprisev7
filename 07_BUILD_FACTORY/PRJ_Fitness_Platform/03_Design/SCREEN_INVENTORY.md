# Fitness Platform — Page Inventory
## AI-Driven Workout Generator + Marketplace + Social

**Date:** 2026-02-14 (Corrected)
**Based on:** PRD_2_Fitness_Platform.md, user corrections (AI-first architecture, marketplace model, social layer)
**Sources:** See SESSION_SOURCES.md

---

## Design Philosophy

This is NOT a program browser. The core function is an **AI workout generator** that learns the user and creates workouts on the fly from any combination of exercises. The user's circumstances change — equipment access, time, energy, goals — and the AI adapts instantly.

**Core loop:** Tell the AI what you've got → Get a workout → Do it → Track it → AI gets smarter about you.

---

## MVP SCREENS (10 Screens)

### Onboarding

| # | Screen | Route | Purpose |
|---|--------|-------|---------|
| 1 | Landing / Marketing | `/` | Presell + conversion. Explain the AI-first approach |
| 2 | Auth (Sign Up / Sign In) | `/auth` | Authentication |
| 3 | Onboarding Intake | `/onboarding` | Preliminary info only — goals, experience level, equipment access, injuries, preferences. Light touch. Circumstances change so this is a starting point, not a permanent profile |

### Core AI Experience

| # | Screen | Route | Purpose |
|---|--------|-------|---------|
| 4 | **AI Workout Generator** | `/generate` | **THE CORE SCREEN.** Chat/conversational interface where the AI knows the user and generates workouts on the fly from any exercise combo. "I've got 30 mins and dumbbells" → instant personalised workout. AI remembers preferences, adapts to circumstances, pulls from the full exercise database. This is the product |
| 5 | **Active Workout Mode** | `/workout/:id` | Execute the generated workout. Exercise-by-exercise guidance: video playback, timer, set/rep/weight logging, rest periods, form cues. Previous performance shown. Auto-advance |
| 6 | Exercise Library | `/exercises` | Browse/search the full exercise database. AI pulls from this but users can explore independently. Filter by muscle group, equipment, difficulty, movement pattern |
| 7 | Exercise Detail | `/exercises/:id` | Video demonstrations, muscle groups targeted, form tips, common mistakes, variations, progressions. This feeds the AI's options |

### Tracking & Home

| # | Screen | Route | Purpose |
|---|--------|-------|---------|
| 8 | Dashboard / Home | `/dashboard` | Today's AI suggestion, recent activity, streaks, quick stats. Entry point after login |
| 9 | Progress & History | `/progress` | Workout log, charts (volume, frequency, body metrics), PRs, trends over time. Body measurements, progress photos |

### Settings

| # | Screen | Route | Purpose |
|---|--------|-------|---------|
| 10 | Settings / Profile | `/settings` | Preferences, subscription, notifications. Update circumstances (new gym, equipment changes, injury) — feeds back to AI |

---

## PHASE 2 SCREENS: MARKETPLACE (Plan Now, Build Later)

The platform becomes a marketplace connecting people with trainers and influencers. Trainers create programs, influencers build audiences, clients find guidance.

| # | Screen | Route | Purpose |
|---|--------|-------|---------|
| 11 | Trainer/Influencer Profiles | `/trainers` | Marketplace directory. Browse trainers and influencers. Ratings, specialties, content. Connect with potential clients |
| 12 | Trainer Detail | `/trainers/:id` | Individual trainer page. Bio, certifications, programs offered, reviews, pricing, contact/booking |
| 13 | Pre-built Programs | `/programs` | Trainer-made and curated programs. The marketplace content layer. Buy/subscribe to structured programs |
| 14 | Program Detail / Flow | `/programs/:id` | Follow a structured program with weekly schedule, progressive overload, rest days. Trainer-designed |

---

## PHASE 2 SCREENS: SOCIAL (Plan Now, Build Later)

Social area for fitness enthusiasts to post routines and journeys and interact with others on the platform.

| # | Screen | Route | Purpose |
|---|--------|-------|---------|
| 15 | Social Feed | `/social` | Fitness enthusiasts post routines, progress updates, journey milestones. Comment, like, share. Community interaction |
| 16 | User Profile (Public) | `/users/:id` | Public profile showing achievements, shared routines, followers/following. Social identity on the platform |

---

## SUBSCRIPTION MODEL

| Tier | Access | Price |
|------|--------|-------|
| Free | Limited AI generations/day, basic exercise library, basic logging | Free |
| Premium | Unlimited AI workouts, full library, advanced analytics, progress photos, no ads | £9.99/mo or £79/yr |
| Trainer | Everything Premium + multi-client management, program creation, marketplace listing, custom branding | £29/mo |

---

## SCREEN-TO-KIT MAPPING

| Screen | Primary Kit | Secondary Kit | What To Pull |
|--------|------------|---------------|-------------|
| Landing / Marketing | Briefberry | Multi-concept Landing | Hero sections, feature blocks, CTA, pricing |
| Auth | Briefberry | Strivo (onboarding) | Auth forms, social login |
| Onboarding Intake | Strivo | Brainwave 2.0 | Multi-step form, progress bar |
| **AI Workout Generator** | **Source Fusion AI** | **Aimate / Triply AI** | **Chat interface, AI response cards, workout output cards** |
| Active Workout Mode | Befit | Fitness Pro | Timer, video player, set logging form, exercise cards |
| Exercise Library | Brainwave 2.0 | Fitness Pro | Data grid, filters, search, cards |
| Exercise Detail | Social Dashboards UI | Befit | Video player, detail panels, muscle group tags |
| Dashboard / Home | Brainwave 2.0 | Befit | Stat cards, activity feed, streak counter |
| Progress & History | Brainwave 2.0 | Zipformat | Charts, graphs, timeline, photo grid |
| Settings / Profile | Brainwave 2.0 | — | Form layouts, toggle switches |
| Trainer Profiles (P2) | Finder (Directory) | Adify (Job Finding) | Directory listing, filter sidebar, profile cards |
| Social Feed (P2) | Social Dashboards UI | Nexus | Post cards, feed layout, interactions |

---

## BOILERPLATE LAYOUTS

| Layout | Screens Using It | Base Kit |
|--------|-----------------|----------|
| **Marketing Layout** (hero + features + CTA + pricing) | Landing | Briefberry / Multi-concept |
| **Auth Layout** (centered form) | Auth, Onboarding | Briefberry / Strivo |
| **Chat Layout** (AI conversation + output panel) | AI Workout Generator | Source Fusion AI |
| **Active Mode Layout** (video + controls + logging) | Active Workout | Befit / Fitness Pro |
| **Dashboard Layout** (sidebar + header + content) | Home, Progress, Settings, Exercise Library | Brainwave 2.0 |
| **Detail Layout** (hero/media + info panels) | Exercise Detail, Trainer Detail, Program Detail | Social Dashboards UI |
| **Directory Layout** (search + filters + card grid) | Trainer Profiles, Programs | Finder / Adify |
| **Social Layout** (feed + interactions) | Social Feed, User Profile | Social Dashboards UI / Nexus |

---

## KEY COMPONENTS (Fitness-Specific)

### AI Components
- [ ] AIWorkoutChat — Conversational interface for workout generation
- [ ] WorkoutOutputCard — AI-generated workout displayed as structured card (exercises, sets, reps, rest)
- [ ] CircumstanceInput — Quick input for "what have you got?" (time, equipment, energy level)
- [ ] ExerciseSwapSuggestion — AI offers alternatives during workout

### Training Components
- [ ] ExerciseRow — Name, sets/reps, video thumbnail, expand
- [ ] SetLogger — Weight, reps, RPE inputs (inline during workout)
- [ ] RestTimer — Countdown with customisable duration
- [ ] ExerciseVideoPlayer — YouTube embed + controls
- [ ] StreakCounter — Daily streak visualisation

### Body/Muscle Components
- [ ] MuscleGroupSelector — Visual body map
- [ ] EquipmentFilter — What equipment is available

### Progress Components
- [ ] VolumeChart — Total volume over time
- [ ] FrequencyHeatmap — Training consistency calendar
- [ ] PRCard — Exercise name, current PR, date set
- [ ] BodyMetricChart — Weight/measurements trend line
- [ ] ProgressPhotoTimeline — Before/after grid

---

## SUMMARY

| Phase | Screens | Status |
|-------|---------|--------|
| MVP | 10 | Build now |
| Marketplace | 4 | Plan now, build Phase 2 |
| Social | 2 | Plan now, build Phase 2 |
| **Total** | **16** | |

+ Common ancillary pages shared across all builds (404, Terms, Privacy, Cookie, Contact)
