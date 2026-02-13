# Property Connect London — Brand Identity Brief

**Purpose:** Define the complete visual identity system for PCL before any page design begins.
**Date:** 2026-02-13

---

## 1. Brand Positioning

**Tagline concept:** "London Property Intelligence"

**Position:** Bloomberg Terminal + Forbes + LinkedIn for London property.
Not a portal (Rightmove). Not an agency (Savills). Not a media site (Property Week).
All three fused — data intelligence + editorial authority + professional community.

**Brand DNA (from PRD):**
- **Authoritative** — Data-driven, expert-backed
- **Accessible** — Complex topics made simple
- **Premium** — High-quality production values
- **Connected** — Community-focused
- **Forward-thinking** — Anticipating trends

**Tone:** Professional but approachable. Confident and knowledgeable. Educational, not condescending. Market-focused and practical.

---

## 2. Logo

**Existing mark:** Geometric cube/hexagon icon (mycubelogo.jpg)
- Construction grid shows intentional geometric design
- Currently shown white on blue (#0099FF approx)
- Suggests: layers, data stacking, building blocks, intelligence

**Needed:**
- [ ] Logo with "Property Connect London" wordmark
- [ ] Horizontal lockup (icon + wordmark)
- [ ] Stacked lockup (icon above wordmark)
- [ ] Icon only (for favicons, app icons, social avatars)
- [ ] Mono versions (black, white, single-color)
- [ ] Clear space and minimum size rules

---

## 3. Color Palette

### Approach
PCL needs to feel: premium, trustworthy, data-driven, London. Not estate agent generic (navy blue + gold). Not startup frivolous. Think Bloomberg meets Savills.

### Proposed Palette (to be finalized)

**Primary:**
- PCL Blue (from logo) — trust, intelligence, data
- Deep Navy — authority, premium

**Secondary:**
- Warm accent (gold/amber?) — premium, London heritage
- Success Green — positive data, growth indicators

**Functional:**
- Error Red — alerts, negative data
- Warning Amber — caution states
- Info Blue — informational

**Neutrals:**
- Rich Black (not pure #000)
- Dark Grey (body text)
- Medium Grey (secondary text)
- Light Grey (borders, dividers)
- Off White (backgrounds)
- Pure White (cards, modals)

### Design Token Structure (from Untitled UI)
```
primitives/    → Raw color values (blue-50 through blue-900)
semantic/      → brand-primary, brand-secondary, text-primary, bg-surface
component/     → button-primary-bg, card-border, nav-bg
```

---

## 4. Typography

### Strategy (from BUILD_NOTES.md)
- **Website/Landing pages:** DM Sans (from Real Estate SaaS Kit)
- **Dashboard/App:** Inter (from Brainwave 2.0 kit)
- **Size compensation:** DM Sans needs ~6-8% size increase vs Plus Jakarta Sans

### Type Scale
| Use | Font | Weight | Size |
|-----|------|--------|------|
| H1 (Hero) | DM Sans | Bold (700) | 56-64px |
| H2 (Section) | DM Sans | SemiBold (600) | 40-48px |
| H3 (Subsection) | DM Sans | SemiBold (600) | 28-32px |
| H4 (Card title) | DM Sans | Medium (500) | 20-24px |
| Body Large | DM Sans | Regular (400) | 18px |
| Body | DM Sans | Regular (400) | 16px |
| Body Small | DM Sans | Regular (400) | 14px |
| Caption | DM Sans | Regular (400) | 12px |
| Dashboard Body | Inter | Regular (400) | 14-16px |
| Dashboard Label | Inter | Medium (500) | 12-14px |
| Data/Numbers | Inter | SemiBold (600) | 14-32px |

---

## 5. Visual Style

### Photography
- London architectural photography (premium, editorial quality)
- Aerial/drone shots of London skyline and neighborhoods
- Property interiors (aspirational but realistic)
- Professional headshots for directory/team
- Data visualization overlays on property imagery

### Iconography
- Line icons (consistent stroke width, rounded corners)
- Dual-tone for feature callouts
- Consistent 24px grid

### Data Visualization
- Clean, minimal chart styling
- Brand color palette applied to all charts
- Interactive hover states
- Responsive scaling
- Source attribution on all data

### Shadows & Elevation (from Untitled UI tokens)
| Level | Use | Shadow |
|-------|-----|--------|
| xs | Subtle cards | 0 1px 2px rgba(0,0,0,0.05) |
| sm | Hover states | 0 1px 3px rgba(0,0,0,0.1) |
| md | Cards, dropdowns | 0 4px 8px rgba(0,0,0,0.1) |
| lg | Modals, popovers | 0 12px 24px rgba(0,0,0,0.1) |
| xl | Floating elements | 0 24px 48px rgba(0,0,0,0.1) |

### Border Radius
| Use | Radius |
|-----|--------|
| Buttons | 8px |
| Cards | 12px |
| Modals | 16px |
| Avatars | Full (50%) |
| Input fields | 8px |

---

## 6. Component Source Mapping (from BUILD_NOTES.md)

| Need | Source Kit | What To Pull |
|------|-----------|-------------|
| Dashboard base | Brainwave 2.0 | Sidebar, header, cards, charts, tables |
| Website pages | Real Estate SaaS Kit | Hero sections, pricing cards, feature grids |
| Design tokens | Untitled UI | Full color scales, typography, shadows |
| Sidebar menu | Aitentico | Collapsed sidebar pattern |
| Sidebar menu (alt) | Trakr | Sidebar menu variant |
| Project components | Strivo | Onboarding flow, project cards |
| Social/content | Social Dashboards UI | Events cards, video player, feeds |
| Property cards | Huose Property | Lead cards, 4 circular action icons |
| Accent colors | Zipformat | Niche pastels for data viz |
| Design system | Caresync SAAS | Green-toned system reference |

---

## 7. Pages Requiring Unique Design vs Template

### Unique Design Needed (12 pages)
1. Homepage — hero + multi-pathway entry
2. Pricing page — complex tier comparison
3. Property Search — map integration
4. Area Explorer — interactive London map
5. Pro Dashboard Home — custom widget grid
6. Consumer Dashboard Home — personalized feed
7. Magazine Home — editorial layout
8. Podcast Home — player + episodes
9. Register/Onboarding — multi-step flow
10. Free Video Landing — funnel page
11. Blog Index — content grid
12. Professional Directory — search + categories

### Template-Based (69+ pages)
- All service pages (same layout, different content) — 5 pages
- All spoke sub-pages (same structure) — 7 pages
- All dashboard list/detail pages — 30+ pages
- All settings pages — 6 pages
- All create/edit forms — 8 pages
- Auth pages (login, forgot, reset) — 3 pages
- Legal pages — 2 pages
- Blog post template — 1 template for many posts

---

## 8. Immediate Next Steps

1. **Finalize PCL color palette** — pick exact hex values
2. **Create logo lockups** — wordmark + icon combinations
3. **Design 12 unique pages** in Figma using kit components
4. **Apply templates** to remaining 69+ pages
5. **Export all visuals** for launch material

---

**This brief drives all design decisions. Lock it before touching Figma.**
