# Fitness App — Screen Inventory
## All Screens Needed for MVP + Full Build

**Date:** 2026-02-14
**Based on:** PRD_2, 90-Day Goal Intake, exercise_library.json (4,630 exercises), video_library (3,857 videos)

---

## MVP SCREENS (Build First — You Are User #1)

### Core Navigation
| Screen | Route | Key Components |
|--------|-------|----------------|
| App Shell | `/` | Sidebar nav, header, user avatar |
| Dashboard Home | `/dashboard` | Today's routine, quick stats, streak, next session |

### Daily Training View
| Screen | Route | Key Components |
|--------|-------|----------------|
| Today's Routine | `/today` | Full day view: morning session + GST breaks + hypertrophy + yoga |
| Weekly Calendar | `/calendar` | 7-day grid showing all training layers per day |
| Session Detail | `/session/:id` | Exercise list, video player, timer, log inputs |
| Active Workout | `/workout/:id` | Exercise-by-exercise mode: video, timer, set logging, next exercise |

### Exercise Library
| Screen | Route | Key Components |
|--------|-------|----------------|
| Exercise Browse | `/exercises` | Grid/list of 4,630 exercises, filter by category/muscle/equipment/plane |
| Exercise Detail | `/exercises/:id` | Video player, cues, muscles, variations, progressions, notes |
| Video Library | `/videos` | Browse 3,857 videos, search, filter by exercise/category |

### AI Chat
| Screen | Route | Key Components |
|--------|-------|----------------|
| AI Chat | `/chat` | Chat interface, message history, context-aware (knows your routine/progress) |
| Chat Thread List | `/chat/threads` | Previous conversations |

### Progress & Logging
| Screen | Route | Key Components |
|--------|-------|----------------|
| Progress Dashboard | `/progress` | Charts: volume, frequency, body metrics, streaks |
| Workout Log | `/log` | Chronological log of all completed sessions |
| Session Log Detail | `/log/:id` | What was done: exercises, sets, reps, weight, RPE, notes |
| Body Metrics | `/progress/body` | Weight chart, measurements, progress photos |
| Personal Records | `/progress/records` | PRs by exercise (1RM, rep PRs, volume PRs) |

### Settings & Profile
| Screen | Route | Key Components |
|--------|-------|----------------|
| Profile | `/profile` | Goals, experience level, preferences, equipment |
| Settings | `/settings` | App settings, notifications, integrations |

**MVP TOTAL: 16 screens**

---

## FULL BUILD SCREENS (After MVP)

### Program Builder
| Screen | Route | Key Components |
|--------|-------|----------------|
| Programs Browse | `/programs` | Pre-built + custom programs |
| Program Detail | `/programs/:id` | Week-by-week breakdown, exercises, progression |
| Program Builder | `/programs/build` | Drag-and-drop program creation |
| Workout Template Builder | `/programs/templates` | Reusable workout templates |

### Knowledge Base
| Screen | Route | Key Components |
|--------|-------|----------------|
| Learning Hub | `/learn` | Articles, guides, technique videos |
| Article Detail | `/learn/:slug` | Long-form content |
| Movement Library | `/learn/movements` | Movement pattern education (push, pull, hinge, squat, carry, rotate) |

### Nutrition (Future)
| Screen | Route | Key Components |
|--------|-------|----------------|
| Nutrition Dashboard | `/nutrition` | Daily intake, macros, meal log |
| Meal Logger | `/nutrition/log` | Quick food entry, barcode scan |
| Recipes | `/nutrition/recipes` | High-protein recipe library |

### Social/Community (Future)
| Screen | Route | Key Components |
|--------|-------|----------------|
| Community | `/community` | Feed, shared workouts |
| Coach View | `/coach` | Multi-client dashboard |

**FULL BUILD TOTAL: 11 additional screens**
**GRAND TOTAL: 27 screens**

---

## SCREEN-TO-KIT MAPPING

### MVP Kit Sources

| Screen | Primary Kit | Secondary Kit | What To Pull |
|--------|------------|---------------|-------------|
| App Shell / Sidebar | Brainwave 2.0 | Aitentico (collapsed sidebar) | Sidebar nav, header bar |
| Dashboard Home | Brainwave 2.0 | Befit | Stat cards, activity feed, calendar widget |
| Today's Routine | Befit | Brainwave 2.0 | Workout card layout, exercise list |
| Weekly Calendar | Brainwave 2.0 | Tendly | Calendar grid component |
| Active Workout | Befit | Social Dashboards UI | Timer, video player, set logging form |
| Exercise Browse | Brainwave 2.0 | — | Data table/grid, filters, search |
| Exercise Detail | Social Dashboards UI | Befit | Video player, detail cards, muscle diagram |
| Video Library | Social Dashboards UI | Unity | Video grid, player, categories |
| AI Chat | Source AI / Aimate | Triply | Chat interface, message bubbles, input |
| Progress Dashboard | Brainwave 2.0 | Zipformat | Charts, graphs, stat cards |
| Workout Log | Brainwave 2.0 | Trakr | Data table, timeline view |
| Body Metrics | Brainwave 2.0 | — | Charts, photo grid |
| Profile / Settings | Brainwave 2.0 | Strivo (onboarding) | Form layouts, preference toggles |

### Boilerplate Layouts (Reusable Across Screens)

| Layout | Used On | Base Kit |
|--------|---------|----------|
| **Dashboard Layout** (sidebar + header + content area) | All logged-in screens | Brainwave 2.0 |
| **List/Grid Layout** (filters + search + card grid) | Exercise Browse, Video Library, Programs, Workout Log | Brainwave 2.0 |
| **Detail Layout** (hero/media + info panels + related items) | Exercise Detail, Session Detail, Program Detail | Social Dashboards UI |
| **Form Layout** (stepped or single-page form) | Profile, Settings, Program Builder, Meal Logger | Brainwave 2.0 |
| **Active Mode Layout** (video + controls + logging) | Active Workout, Session in Progress | Befit |
| **Chat Layout** (message thread + input) | AI Chat | Source AI |
| **Analytics Layout** (stat cards + charts + tables) | Progress Dashboard, Body Metrics, Personal Records | Brainwave 2.0 |

---

## COMPONENT INVENTORY (Fitness App Specific)

### Training Components
- [ ] WorkoutCard (exercise list, duration, difficulty)
- [ ] ExerciseRow (name, sets/reps, video thumbnail, expand)
- [ ] SetLogger (weight, reps, RPE inputs — inline)
- [ ] RestTimer (countdown, customizable)
- [ ] ExerciseVideoPlayer (YouTube embed + controls)
- [ ] DailyRoutineTimeline (morning → GST → hypertrophy → yoga)
- [ ] TrainingLayerBadge (cardio/plyo/strength/hypertrophy/GST/yoga)
- [ ] StreakCounter (daily streak visualization)

### Body/Muscle Components
- [ ] MuscleGroupSelector (visual body map)
- [ ] MovementPatternFilter (push/pull/hinge/squat/carry/rotate)
- [ ] PlaneOfMotionFilter (sagittal/frontal/transverse)

### Progress Components
- [ ] VolumeChart (line/bar chart — total volume over time)
- [ ] FrequencyHeatmap (calendar heatmap — training consistency)
- [ ] PRCard (exercise name, current PR, date set)
- [ ] BodyMetricChart (weight/measurements trend line)
- [ ] ProgressPhotoTimeline (before/after grid)

---

## NEXT STEPS

1. Review Befit + Fitness Pro Figma kits for component availability
2. Set up React app shell using Brainwave dashboard layout
3. Import exercise_library.json as seed data
4. Connect exercise_video_lookup.json for video integration
5. Build Daily Routine view first (this is what you use every morning)
