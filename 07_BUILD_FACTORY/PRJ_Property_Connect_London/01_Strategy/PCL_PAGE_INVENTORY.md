# PCL PAGE INVENTORY
## Complete List of Pages to Build (Sorted by Priority)

---

## BUILD PHASE 1: MARKETING SITE MVP (17 pages)

### Priority 1A: Lead Generation (Week 1)
| Page | URL | Type | Key Components |
|------|-----|------|----------------|
| Homepage | `/` | Marketing | Hero, Problem/Solution, Channels, Pricing preview, CTA |
| Free Video Landing | `/free-video` | Funnel | Hero, Benefits, Form, FAQ |
| Free Video Apply | `/free-video/apply` | Funnel | Multi-step form |
| Free Video Thank You | `/free-video/thank-you` | Funnel | Confirmation, Upsell CTA |
| Contact | `/contact` | Marketing | Form, Map, Details |

### Priority 1B: Service Pages (Week 2)
| Page | URL | Type | Key Components |
|------|-----|------|----------------|
| Video Production | `/services/video-production` | Service | Hero, Packages, Portfolio, Process, CTA |
| Magazine Advertising | `/services/magazine-advertising` | Service | Hero, Formats, Pricing, Distribution map |
| Sponsorship | `/services/sponsorship` | Service | Hero, Tiers, ROI calculator, Application |
| Content Creation | `/services/content-creation` | Service | Hero, Services grid, Process |
| Platform Marketing | `/services/platform-marketing` | Service | Hero, Features, CTA |

### Priority 1C: Core Pages (Week 3)
| Page | URL | Type | Key Components |
|------|-----|------|----------------|
| About | `/about` | Marketing | Story, Team, Mission, Values |
| Pricing | `/pricing` | Marketing | Toggle (Pro/Consumer), Tier cards, Comparison table |
| Platform Pros | `/platform/professionals` | Landing | Dashboard preview, Features, Pricing, Trial CTA |
| Platform Consumers | `/platform/consumers` | Landing | Feed preview, Features, Signup CTA |
| Blog Index | `/blog` | Content | Post grid, Categories, Search |
| Blog Post | `/blog/[slug]` | Content | Article layout, Author, Related |
| Privacy/Terms | `/privacy`, `/terms` | Legal | Text content |

---

## BUILD PHASE 2: SPOKES (12 pages)

### Magazine Section
| Page | URL | Type | Key Components |
|------|-----|------|----------------|
| Magazine Home | `/magazine` | Spoke | Current issue, Highlights, Subscribe CTA |
| Current Issue | `/magazine/current-issue` | Spoke | Flipbook embed, Articles |
| Archive | `/magazine/archive` | Spoke | Issue grid, Filters |
| Subscribe | `/magazine/subscribe` | Spoke | Plans, Checkout |
| Advertise | `/magazine/advertise` | Spoke | → Redirect to service page |
| Contribute | `/magazine/contribute` | Spoke | Application form |

### Podcast Section
| Page | URL | Type | Key Components |
|------|-----|------|----------------|
| Podcast Home | `/podcast` | Spoke | Latest episode, Player, Episodes grid |
| Episodes | `/podcast/episodes` | Spoke | Episode list, Filters, Search |
| Episode Detail | `/podcast/[slug]` | Spoke | Player, Show notes, Guest info |
| Guests | `/podcast/guests` | Spoke | Guest directory, Search |
| Sponsor | `/podcast/sponsor` | Spoke | Packages, Application |

### Video/CTV Section
| Page | URL | Type | Key Components |
|------|-----|------|----------------|
| Video Home | `/video` | Spoke | Featured tours, Gallery |
| CTV Home | `/tv` | Spoke | Channel preview, Features |
| CTV Subscribe | `/tv/subscribe` | Spoke | App links, Subscription |

---

## BUILD PHASE 3: PLATFORM PUBLIC (8 pages)

| Page | URL | Type | Key Components |
|------|-----|------|----------------|
| Login | `/login` | Auth | Form, Social login, Forgot password |
| Register | `/register` | Auth | User type selection, Form, Onboarding |
| Forgot Password | `/forgot-password` | Auth | Email form |
| Reset Password | `/reset-password` | Auth | New password form |
| Property Search | `/search` | Public | Map, Filters, Results grid |
| Area Explorer | `/areas` | Public | Interactive map, Area cards |
| Area Detail | `/areas/[borough]` | Public | Data sections, Compare CTA |
| Professional Directory | `/directory` | Public | Categories, Search, Filters |
| Professional Profile | `/directory/[slug]` | Public | Profile, Services, Reviews, Contact |
| Content Hub | `/content` | Public | Content grid, Filters by type |
| Content Detail | `/content/[type]/[slug]` | Public | Article/Video/Podcast layout |

---

## BUILD PHASE 4: PRO DASHBOARD (26 pages)

### Core Dashboard
| Page | URL | Parent | Key Components |
|------|-----|--------|----------------|
| Dashboard Home | `/pro/dashboard` | - | Stats, Activity, Alerts |
| Notifications | `/pro/notifications` | - | Notification list |

### Content Management Hub
| Page | URL | Parent | Key Components |
|------|-----|--------|----------------|
| Content Library | `/pro/content` | Content | All content, Filters, Actions |
| Create Article | `/pro/content/new/article` | Content | Rich text editor |
| Create Video | `/pro/content/new/video` | Content | Upload, Details form |
| Create Listing | `/pro/content/new/listing` | Content | Property form, Photos |
| Create Event | `/pro/content/new/event` | Content | Event form |
| Create Job | `/pro/content/new/job` | Content | Job form |
| Content Calendar | `/pro/content/calendar` | Content | Calendar view, Scheduler |
| Media Library | `/pro/content/media` | Content | File browser, Upload |
| Content Analytics | `/pro/content/analytics` | Content | Performance charts |

### Client Management
| Page | URL | Parent | Key Components |
|------|-----|--------|----------------|
| Client Database | `/pro/clients` | Clients | Contact list, Search |
| Client Detail | `/pro/clients/[id]` | Clients | Profile, History, Notes |
| Lead Inbox | `/pro/clients/leads` | Clients | Lead list, Qualification |
| Lead Detail | `/pro/clients/leads/[id]` | Clients | Lead profile, Actions |
| Client Journey | `/pro/clients/journey` | Clients | Pipeline view |

### Analytics
| Page | URL | Parent | Key Components |
|------|-----|--------|----------------|
| Analytics Dashboard | `/pro/analytics` | Analytics | Overview charts |
| Performance | `/pro/analytics/performance` | Analytics | Detailed metrics |
| Competitors | `/pro/analytics/competitors` | Analytics | Benchmarks |
| Reports | `/pro/analytics/reports` | Analytics | Custom report builder |

### Business Profile
| Page | URL | Parent | Key Components |
|------|-----|--------|----------------|
| Profile Editor | `/pro/profile` | Profile | All profile fields |
| Services | `/pro/profile/services` | Profile | Service packages |
| Team | `/pro/profile/team` | Profile | Team members |
| Portfolio | `/pro/profile/portfolio` | Profile | Work showcase |
| Reviews | `/pro/profile/reviews` | Profile | Review management |

### Marketing Tools
| Page | URL | Parent | Key Components |
|------|-----|--------|----------------|
| Campaigns | `/pro/marketing` | Marketing | Campaign list |
| Create Campaign | `/pro/marketing/new` | Marketing | Campaign builder |
| Email Marketing | `/pro/marketing/email` | Marketing | Templates, Sequences |
| Promotions | `/pro/marketing/promotions` | Marketing | Offers, Referrals |

### Learning
| Page | URL | Parent | Key Components |
|------|-----|--------|----------------|
| Learning Home | `/pro/learning` | Learning | Courses, Resources |
| Course Detail | `/pro/learning/[id]` | Learning | Video player, Progress |
| Research Library | `/pro/learning/research` | Learning | Reports, Studies |

### Community
| Page | URL | Parent | Key Components |
|------|-----|--------|----------------|
| Network | `/pro/community` | Community | Connections, Opportunities |
| Forums | `/pro/community/forums` | Community | Discussion threads |
| Events | `/pro/community/events` | Community | Event calendar |

### Settings
| Page | URL | Parent | Key Components |
|------|-----|--------|----------------|
| Account Settings | `/pro/settings` | Settings | Profile, Password |
| Subscription | `/pro/settings/subscription` | Settings | Plan, Billing |
| Notifications | `/pro/settings/notifications` | Settings | Preferences |
| Integrations | `/pro/settings/integrations` | Settings | Connected apps |

---

## BUILD PHASE 5: CONSUMER DASHBOARD (18 pages)

### Core Dashboard
| Page | URL | Parent | Key Components |
|------|-----|--------|----------------|
| Dashboard Home | `/user/dashboard` | - | Feed, Alerts, Saved |
| Notifications | `/user/notifications` | - | Notification list |

### Feed & Content
| Page | URL | Parent | Key Components |
|------|-----|--------|----------------|
| Personalized Feed | `/user/feed` | Feed | Content stream |
| Following | `/user/feed/following` | Feed | Followed experts' content |
| Saved Content | `/user/feed/saved` | Feed | Bookmarked items |

### Property Explorer
| Page | URL | Parent | Key Components |
|------|-----|--------|----------------|
| Property Search | `/user/explore` | Explore | Map search, Filters |
| Saved Properties | `/user/explore/saved` | Explore | Saved listings |
| Property Alerts | `/user/explore/alerts` | Explore | Alert management |
| Area Research | `/user/explore/areas` | Explore | Saved areas, Compare |

### Expert Finder
| Page | URL | Parent | Key Components |
|------|-----|--------|----------------|
| Find Experts | `/user/experts` | Experts | Directory, Search |
| Compare Experts | `/user/experts/compare` | Experts | Side-by-side |
| Consultations | `/user/experts/consultations` | Experts | Bookings, History |

### Tools
| Page | URL | Parent | Key Components |
|------|-----|--------|----------------|
| Tools Home | `/user/tools` | Tools | Tool cards grid |
| Mortgage Calculator | `/user/tools/mortgage` | Tools | Calculator |
| Stamp Duty Calculator | `/user/tools/stamp-duty` | Tools | Calculator |
| Budget Planner | `/user/tools/budget` | Tools | Planner form |

### Learning
| Page | URL | Parent | Key Components |
|------|-----|--------|----------------|
| Learning Hub | `/user/learning` | Learning | Guides, Resources |
| Guide Detail | `/user/learning/[slug]` | Learning | Content, Progress |

### Community
| Page | URL | Parent | Key Components |
|------|-----|--------|----------------|
| Community Home | `/user/community` | Community | Forums, Reviews |
| My Reviews | `/user/community/reviews` | Community | User's reviews |

### Settings
| Page | URL | Parent | Key Components |
|------|-----|--------|----------------|
| Account Settings | `/user/settings` | Settings | Profile, Password |
| Preferences | `/user/settings/preferences` | Settings | Interests, Notifications |
| Subscription | `/user/settings/subscription` | Settings | Plan, Billing |

---

## COMPONENT INVENTORY

### Navigation Components (7)
- [ ] MainNav (desktop mega menu)
- [ ] MobileNav (hamburger + drawer)
- [ ] DashboardSidebar (pro)
- [ ] DashboardSidebar (consumer)
- [ ] Breadcrumbs
- [ ] TabNav
- [ ] Footer

### Hero Components (5)
- [ ] HeroVideo (video background)
- [ ] HeroSplit (text + media)
- [ ] HeroCentered (centered text)
- [ ] HeroDashboard (stats header)
- [ ] HeroMinimal (page title only)

### Card Components (10)
- [ ] ServiceCard
- [ ] PricingCard
- [ ] PropertyCard
- [ ] ExpertCard
- [ ] ContentCard (article/video/podcast)
- [ ] TestimonialCard
- [ ] StatCard
- [ ] FeatureCard
- [ ] EventCard
- [ ] JobCard

### Form Components (8)
- [ ] ContactForm
- [ ] LeadCaptureForm
- [ ] MultiStepForm
- [ ] SearchFilters
- [ ] ProfileEditor
- [ ] ContentEditor (rich text)
- [ ] FileUploader
- [ ] DateTimePicker

### Data Display Components (10)
- [ ] StatsGrid
- [ ] ComparisonTable
- [ ] FeatureChecklist
- [ ] ProcessSteps
- [ ] Timeline
- [ ] LineChart
- [ ] BarChart
- [ ] PieChart
- [ ] InteractiveMap
- [ ] DataTable

### Feedback Components (6)
- [ ] Toast
- [ ] Modal
- [ ] EmptyState
- [ ] LoadingSkeleton
- [ ] ErrorState
- [ ] ConfirmDialog

### Content Components (8)
- [ ] ArticleLayout
- [ ] VideoPlayer
- [ ] PodcastPlayer
- [ ] FAQAccordion
- [ ] TabbedContent
- [ ] ImageGallery
- [ ] Flipbook (magazine)
- [ ] Calculator

---

## TOTAL PAGE COUNT

| Section | Pages |
|---------|-------|
| Marketing Site | 17 |
| Spokes | 12 |
| Platform Public | 8 |
| Pro Dashboard | 26 |
| Consumer Dashboard | 18 |
| **TOTAL** | **81 pages** |

---

## AUTOMATION OPPORTUNITIES

### Pages That Can Be Templated
- All service pages (same layout, different content)
- All spoke "home" pages (same structure)
- All dashboard "list" pages (same table/grid layout)
- All dashboard "detail" pages (same profile layout)
- All "create/edit" pages (same form layout)
- All "settings" pages (same form layout)

### Pages That Need Custom Design
- Homepage (unique layout)
- Pricing page (complex comparison)
- Property Search (map integration)
- Area Explorer (interactive map)
- Dashboard Homes (custom widgets)
- Analytics pages (custom charts)

### Content That Can Be AI-Generated
- Service page copy (from questionnaire answers)
- FAQ sections
- Feature descriptions
- CTA copy variations
- Meta descriptions
- Email sequences

---

## NEXT STEP: UI LIBRARY BUILD ORDER

1. **Design Tokens** — Colors, typography, spacing, shadows
2. **Base Components** — Button, Input, Select, Checkbox, etc.
3. **Navigation** — MainNav, MobileNav, Footer
4. **Cards** — All card types
5. **Heroes** — All hero types
6. **Forms** — All form types
7. **Data Display** — Tables, charts, stats
8. **Feedback** — Toasts, modals, states
9. **Content** — Article, video, podcast layouts
10. **Dashboard Shells** — Sidebar, header, layout wrappers
