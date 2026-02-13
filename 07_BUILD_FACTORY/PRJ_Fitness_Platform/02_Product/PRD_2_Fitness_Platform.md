# PRD 2: Fitness Platform & App

**Version:** 2.0  
**Date:** 2025-11-04  
**Priority:** HIGH  

---

## Vision

Create a comprehensive fitness platform that leverages YouTube content to provide personalized workout programs, progress tracking, and community features while building personal fitness knowledge and routine.

---

## Target Audience

### Primary
- Individuals seeking structured workout programs
- Home fitness enthusiasts
- Gym-goers wanting guided workouts
- People building fitness habits

### Secondary
- Personal trainers seeking content library
- Fitness content creators
- Rehabilitation patients (with medical guidance)

---

## Core Features

### 1. YouTube Content Library
- **Integration:** YouTube API for exercise video management
- **Categorization:** Exercise type, muscle group, difficulty, equipment
- **Curation:** Vetted channels and quality content
- **Playback:** In-app video player with controls
- **Offline:** Downloaded videos for offline access

### 2. Workout Programs
- **Pre-built Programs:** Beginner to advanced
- **Custom Programs:** User-created routines
- **Smart Scheduling:** Weekly workout calendar
- **Progression:** Automatic difficulty adjustment
- **Variety:** Strength, cardio, flexibility, mobility, HIIT

### 3. Exercise Database
- **Comprehensive Library:** 500+ exercises
- **Details per Exercise:**
  - Primary/secondary muscle groups
  - Equipment required
  - Difficulty level
  - Multiple video demonstrations
  - Form cues and tips
  - Common mistakes
  - Variations and progressions
  - Alternative exercises

### 4. Progress Tracking
- **Workout Logging:** 
  - Sets, reps, weight
  - Time, distance
  - Rest periods
  - Perceived exertion
- **Body Metrics:**
  - Weight tracking
  - Body measurements
  - Progress photos
  - Body composition
- **Performance Metrics:**
  - Volume (total weight lifted)
  - Workout frequency
  - Personal records
  - Streak tracking
- **Visualization:**
  - Charts and graphs
  - Trend analysis
  - Achievement badges
  - Comparison over time

### 5. Workout Experience
- **Active Workout Mode:**
  - Exercise-by-exercise guidance
  - Video playback for current exercise
  - Timer for sets/rest
  - Quick logging interface
  - Previous performance display
- **Smart Features:**
  - Rest timer with notifications
  - Auto-advance to next exercise
  - Plate calculator (weight loading)
  - Superset/circuit support
  - Notes per exercise

### 6. Knowledge Base
- **Learning Content:**
  - Exercise technique guides
  - Program design principles
  - Nutrition basics
  - Recovery strategies
  - Injury prevention
- **Personal Notes:**
  - Observations and learnings
  - Form improvements
  - What works/doesn't work
  - Modification needs

---

## Technical Architecture

### Platform Components
- **Web App:** Desktop experience
- **Mobile App:** iOS & Android (React Native)
- **Backend:** Node.js or Python
- **Database:** PostgreSQL
- **Media:** YouTube API + S3 for custom content

### Key Integrations
- **YouTube Data API v3:** Content discovery and playback
- **Health APIs:** Apple Health, Google Fit (optional)
- **Wearables:** Future integration (Garmin, Fitbit, etc.)

---

## Database Schema

### Core Tables

```sql
-- Users & Profiles
users
user_profiles (fitness goals, experience level, preferences)
user_measurements (body metrics over time)

-- Exercise Library
exercises (name, description, muscle_groups, equipment, difficulty)
exercise_videos (youtube_video_id, exercise_id, quality_rating)
muscle_groups
equipment_types

-- Workouts & Programs
programs (name, description, duration, difficulty)
program_weeks (week number within program)
program_workouts (workouts within program week)
workout_templates (reusable workout designs)
workout_exercises (exercises within workout, order, sets, reps)

-- User Activity
user_workouts (completed workouts)
workout_sets (logged sets: weight, reps, rpe)
workout_notes
personal_records

-- Progress Tracking
body_measurements (weight, measurements, date)
progress_photos
achievements

-- Content Management
youtube_channels (curated fitness channels)
youtube_playlists (organized collections)
content_tags (categorization)

-- Knowledge Base
learning_articles
personal_notes
form_feedback
```

---

## Content Strategy

### YouTube Channel Curation
**Vetted Channels by Category:**

**Strength Training:**
- Jeff Nippard (science-based)
- AthleanX (form and injury prevention)
- Renaissance Periodization (program design)
- Stronger by Science
- Jeff Cavaliere

**Bodyweight/Calisthenics:**
- FitnessFAQs
- Calisthenicmovement
- Chris Heria
- Austin Dunham

**Olympic Lifting:**
- Catalyst Athletics
- Torokhtiy Weightlifting
- ATG (Knees Over Toes Guy)

**Cardio/Conditioning:**
- The Running Channel
- Global Triathlon Network
- GCN (cycling)

**Flexibility/Mobility:**
- Tom Merrick (bodyweight training)
- Yoga with Adriene
- GMB Fitness

**Exercise-Specific Tutorials:**
- Squat University (form checks)
- Brian Alsruhe (conditioning)
- Alexander Bromley (program design)

### Content Organization
- **By Muscle Group:** Chest, back, legs, shoulders, arms, core
- **By Equipment:** Barbell, dumbbell, bodyweight, machines, resistance bands
- **By Goal:** Strength, hypertrophy, endurance, mobility, fat loss
- **By Difficulty:** Beginner, intermediate, advanced
- **By Duration:** <10min, 10-20min, 20-30min, 30-45min, 45-60min, 60min+

---

## User Experience Flow

### Onboarding
1. Fitness goal selection
2. Experience level assessment
3. Equipment availability
4. Schedule preferences
5. Program recommendation

### Daily Usage
1. View today's workout
2. Start workout (active mode)
3. Follow exercise videos
4. Log sets/reps in real-time
5. Complete workout summary
6. Review progress

### Workout Creation
1. Select exercise category
2. Browse exercise library (with videos)
3. Add exercises to workout
4. Define sets/reps/rest
5. Order exercises
6. Save as template

---

## Pre-built Programs

### Beginner Programs
- **Starting Strength Adaptation:** Basic barbell program
- **Bodyweight Foundation:** No equipment required
- **Dumbbell Only:** Home gym setup
- **Machine Based:** Gym beginners

### Intermediate Programs
- **Upper/Lower Split:** 4 days/week
- **Push/Pull/Legs:** 6 days/week or 3 days/week
- **Full Body:** 3-4 days/week
- **5/3/1 Adaptation:** Strength focus

### Advanced Programs
- **Olympic Lifting:** Snatch, clean & jerk progressions
- **Powerlifting:** Squat, bench, deadlift focus
- **Bodybuilding:** Hypertrophy phases
- **Athlete Training:** Sport-specific

### Specialty Programs
- **Home Workouts:** Minimal equipment
- **Hotel/Travel:** Bodyweight focus
- **Time-Efficient:** <30 minute sessions
- **Rehabilitation:** Low-impact progressions

---

## Progress & Analytics Features

### Workout Analytics
- Total volume per session
- Volume per muscle group
- Workout duration trends
- Frequency analysis
- Intensity distribution

### Performance Tracking
- 1RM estimations and tracking
- Rep PR tracking per exercise
- Volume PR tracking
- Workout density (volume/time)

### Body Composition
- Weight trend line
- Measurement changes (chest, waist, arms, legs, etc.)
- Progress photo timeline
- Body composition estimates (if scale integration)

### Goal Management
- Target weight/composition
- Performance goals (e.g., "bench 225lbs")
- Habit goals (e.g., "workout 4x/week")
- Progress toward goals visualization

---

## Monetization Strategy

### Freemium Model
**Free Tier:**
- Access to exercise library (limited videos)
- Basic workout logging
- Pre-built beginner programs (1-2)
- Basic progress tracking

**Premium Tier (£9.99/mo or £79/year):**
- Full exercise video library
- All pre-built programs
- Custom program creation
- Advanced analytics
- Progress photos
- Personal records tracking
- Workout templates
- No ads

**Coach/Trainer Tier (£29/mo):**
- Multiple client profiles
- Program assignment to clients
- Client progress monitoring
- Custom branding
- Exercise library management

---

## Technical Requirements

### YouTube API Integration
- Video search and discovery
- Playlist management
- Video metadata retrieval
- Embed player implementation
- Quota management (10,000 units/day free)

### Mobile App Features
- Offline workout mode
- Camera integration (progress photos)
- Notification/reminders
- Background timer
- Apple Health/Google Fit sync

### Performance Requirements
- Fast video loading (<2 seconds)
- Smooth workout logging (no lag)
- Offline data sync when reconnected
- Battery efficiency during workouts

---

## Phase 1 Development (Months 1-3)

### Critical Features
1. User authentication
2. Exercise library (100+ exercises)
3. YouTube video integration
4. Basic workout logging
5. Simple progress tracking (weight, measurements)
6. 2-3 pre-built programs
7. Workout timer

### High Priority
1. Mobile app (iOS/Android)
2. Active workout mode
3. Rest timer
4. Personal records tracking
5. Program calendar view
6. Exercise filtering/search

---

## Phase 2 Development (Months 4-6)

### Features
1. Custom program builder
2. Advanced analytics
3. Progress photos
4. Workout templates
5. Social features (share workouts)
6. Achievement system
7. Expanded exercise library (500+)
8. More pre-built programs (10+)

---

## Phase 3 Development (Months 7-12)

### Features
1. AI-powered program recommendations
2. Form check video upload
3. Community features
4. Nutrition tracking integration
5. Wearable device integration
6. Coach/trainer dashboard
7. White-label options
8. API for third-party integrations

---

## Key Metrics

### User Engagement
- Daily active users (DAU)
- Monthly active users (MAU)
- Workouts logged per week
- Session duration
- Workout completion rate

### Content Metrics
- Exercise video views
- Program starts vs completions
- Most popular exercises
- Video quality ratings

### Business Metrics
- Free-to-paid conversion rate
- Churn rate
- LTV:CAC ratio
- MRR growth

---

## Dependencies

### Internal
- **Copy Platform:** Marketing content, in-app copy
- **Branding Platform:** Visual identity, app design
- **UI Library:** Component designs
- **Database:** Schema and RAG integration
- **Agent OS:** Task orchestration

### External
- YouTube Data API access
- Mobile app store accounts
- Cloud hosting (AWS/GCP)
- Payment processing (Stripe)
- Analytics platform

---

## Success Criteria

### Month 3
- MVP launched (web + mobile)
- 100+ exercises with videos
- 3 pre-built programs
- Basic workout logging functional
- 500 users

### Month 6
- 500+ exercises
- 10+ programs
- Advanced tracking features
- 5,000 users
- 5% conversion to premium

### Month 12
- Full feature set
- 50,000 users
- 10% conversion to premium
- £50K MRR
- 4+ star rating on app stores

---

## Risk Mitigation

### YouTube API Risks
- **Risk:** Quota limits or API changes
- **Mitigation:** Cache video metadata, diversify to Vimeo, host critical content

### Content Quality Risks
- **Risk:** Poor quality or incorrect form in videos
- **Mitigation:** Vetted channels only, user rating system, expert review

### User Retention Risks
- **Risk:** Users abandon after initial enthusiasm
- **Mitigation:** Habit-building features, streak tracking, reminders, progress visualization

---

## Next Steps

1. Finalize exercise database structure
2. Curate initial 100 YouTube videos
3. Design mobile app UI/UX
4. Build MVP workout logging
5. Implement YouTube API integration
6. Create first 3 programs
7. Launch beta testing

---

**Status:** Ready for Phase 1 development
**Owner:** [Your Name]
**Last Updated:** 2025-11-04
