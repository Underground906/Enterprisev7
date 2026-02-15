# VIDEO PRODUCTION SPEC — Motion Lexicon & Storyboard Reference
> Created: 2026-02-15 | Tool: Remotion + Claude
> Use this to describe what you want. Claude writes the Remotion code.

---

## HOW TO USE THIS

When writing a storyboard, pick terms from each section:

> "Logo **fades in** center with **spring** easing. After 1s, headline **typewriters** in below. Stats **count up** with **stagger**. **Crossfade** to dashboard screenshot which **Ken Burns** slowly. Cursor **glides** to the nav, **clicks** with **ripple**, sidebar **slides in from left** with **overshoot**."

That's enough for Claude to write the full Remotion composition.

---

## 1. ENTRY ANIMATIONS (How things appear)

| Term | What It Looks Like |
|------|-------------------|
| **Fade in** | Opacity 0→1. Simple, clean, professional. |
| **Slide in (from left/right/top/bottom)** | Element moves in from off-screen in the specified direction. |
| **Scale in** | Starts small (or invisible), grows to full size. |
| **Scale up** | Same as scale in — 0→100% size. |
| **Scale down in** | Starts oversized, shrinks to final size. Feels impactful. |
| **Pop in** | Quick scale 0→110%→100%. Bouncy, attention-grabbing. |
| **Spring in** | Physics-based — overshoots then settles. Feels organic. |
| **Bounce in** | Like spring but with multiple bounces before settling. |
| **Drop in** | Falls from above with slight bounce at landing. Gravity feel. |
| **Rise up** | Slides up from below + fades in simultaneously. Very common in SaaS. |
| **Fly in** | Fast slide from off-screen. More dramatic than slide. |
| **Zoom in** | Camera zooms toward the element (background scales up). |
| **Expand** | Element grows from a point (like expanding from a click). |
| **Unfold** | Element reveals height/width progressively, like unfolding paper. |
| **Clip reveal** | A mask wipes across, revealing the element behind it. |
| **Draw on** | SVG path draws itself stroke by stroke. Great for icons/illustrations. |
| **Blur in** | Starts blurred, sharpens into focus. Cinematic feel. |
| **Rotate in** | Spins while entering. Subtle rotation (5-15°) looks good, full spin is playful. |
| **Flip in** | 3D flip along X or Y axis to reveal. Card-flip effect. |
| **Glitch in** | Brief RGB split / distortion before settling. Tech/hacker aesthetic. |
| **Morph in** | Transforms from one shape into the final shape. |
| **Typewriter** | Characters appear one by one, left to right, with cursor. |
| **Materialize** | Particles/dots converge to form the element. |

---

## 2. EXIT ANIMATIONS (How things disappear)

| Term | What It Looks Like |
|------|-------------------|
| **Fade out** | Opacity 1→0. |
| **Slide out** | Moves off-screen in a direction. |
| **Scale out** | Shrinks to nothing. |
| **Shrink away** | Scales down to a point and vanishes. |
| **Fly away** | Fast exit off-screen. |
| **Zoom out** | Camera pulls back, element recedes. |
| **Collapse** | Height/width shrinks to zero. Like folding shut. |
| **Dissolve** | Breaks into particles that scatter. |
| **Blur out** | Goes out of focus then disappears. |
| **Drop off** | Falls downward with gravity. |
| **Wipe away** | A mask slides across, hiding the element. |

---

## 3. TRANSITIONS (Between scenes/sections)

| Term | What It Looks Like |
|------|-------------------|
| **Cut** | Instant switch. No animation. Punchy, fast-paced. |
| **Crossfade** | Old fades out while new fades in. Overlapping opacity. Smooth, professional. |
| **Dissolve** | Same as crossfade but often implies a longer, softer blend. |
| **Slide transition** | New scene slides in pushing the old one out. Direction matters (left, right, up, down). |
| **Push** | New content pushes old content off screen. Like swiping pages. |
| **Wipe** | A line/edge sweeps across revealing the new scene. Can be horizontal, vertical, diagonal, circular. |
| **Zoom through** | Camera zooms into old scene, emerges into new scene. Seamless depth effect. |
| **Morph transition** | Elements from scene A transform into elements of scene B. Shared element animation. |
| **Iris** | Circular reveal from center outward (or inward). Classic cinematic. |
| **Split** | Screen splits (horizontal/vertical) revealing new content. |
| **Curtain** | Two halves slide apart like curtains opening. |
| **Flip** | 3D page flip to new scene. |
| **Swipe** | Quick directional wipe with motion blur. |
| **Ripple** | Distortion wave emanates from center, revealing new scene. |
| **Glitch transition** | Brief digital distortion/noise between scenes. |
| **Match cut** | A shape/element in scene A matches position/shape in scene B for seamless switch. |

---

## 4. TEXT ANIMATIONS

| Term | What It Looks Like |
|------|-------------------|
| **Typewriter** | Characters appear one at a time with blinking cursor. |
| **Word by word** | Each word appears sequentially (fade or pop). |
| **Line by line** | Each line of text appears in sequence. |
| **Letter stagger** | All letters animate in simultaneously but with slight delay between each. Creates a wave. |
| **Split text** | Text splits apart (by letter or word) before reassembling. |
| **Highlight sweep** | A colour bar sweeps behind text from left to right, highlighting it. |
| **Underline draw** | An underline draws itself from left to right under the text. |
| **Colour shift** | Text colour changes word by word or all at once. |
| **Kinetic typography** | Text moves, scales, rotates dynamically to music/beats. Very energetic. |
| **Counter / Count up** | Number ticks from 0 to final value. Great for stats ("+340% conversion"). |
| **Scramble** | Random characters cycle before settling on the real text. Matrix-style. |
| **Blur reveal** | Text starts blurred, sharpens into readability. |
| **Gradient text** | Text fills with a moving gradient. Eye-catching for headlines. |
| **Mask reveal** | Text revealed by a shape/line passing over it. |
| **Bounce letters** | Each letter drops in with a bounce. Playful. |
| **Slide up replace** | Old text slides up and out, new text slides up into place. Good for changing stats. |
| **Fade swap** | Old text fades out, new text fades in same position. Subtle replacement. |

---

## 5. CURSOR & INTERACTION EFFECTS

| Term | What It Looks Like |
|------|-------------------|
| **Glide** | Cursor moves along a smooth bezier curve. No sharp corners. Professional. |
| **Click** | Cursor presses down slightly (scale 1→0.9→1). |
| **Click ripple** | Circular ripple expands from click point. Material Design style. |
| **Click highlight** | Brief colour flash at click point. |
| **Click pulse** | A ring pulses outward from click point then fades. |
| **Double click** | Two quick clicks in succession. |
| **Hover** | Cursor pauses over an element, element reacts (colour change, lift, glow). |
| **Drag** | Cursor grabs and moves an element from A to B. |
| **Scroll** | Scroll indicator or visible scrolling of content. |
| **Select text** | Cursor drags across text, leaving a selection highlight. |
| **Type** | Cursor in text field, characters appear as if typed. |
| **Tooltip appear** | Cursor hovers, a tooltip fades/pops in nearby. |
| **Right click** | Context menu appears. |
| **Cursor trail** | Subtle motion trail behind cursor. Sleek. |

---

## 6. LAYOUT & COMPONENT ANIMATIONS

| Term | What It Looks Like |
|------|-------------------|
| **Stagger** | Multiple elements animate in sequence with a delay between each (e.g., 0.1s apart). Cards appearing one after another. |
| **Cascade** | Like stagger but implies top-to-bottom flow. |
| **Fan out** | Elements spread from a central point outward. |
| **Grid populate** | Grid cells fill in one by one or row by row. |
| **Accordion** | Section expands/collapses vertically. Content reveals/hides. |
| **Tab switch** | Active tab indicator slides to new tab, content swaps. |
| **Sidebar slide** | Side panel slides in/out from edge. |
| **Modal pop** | Overlay fades in, modal card scales up from center. Background dims. |
| **Notification toast** | Small card slides in from corner, pauses, slides out. |
| **Drawer** | Panel slides up from bottom (mobile) or side (desktop). |
| **Card flip** | Card rotates 180° on Y axis, revealing back side. |
| **Card hover lift** | Card raises with shadow growing. Depth effect. |
| **List reorder** | Items animate to new positions. Smooth rearrangement. |
| **Progress fill** | A bar fills from left to right. Loading/progress indicator. |
| **Chart animate** | Bar chart bars grow upward, line chart draws left to right, pie chart segments expand. |
| **Counter tick** | Numbers rapidly increment to final value. |
| **Toggle switch** | Switch slides from off to on, colour changes. |
| **Skeleton load** | Grey placeholder shapes pulse, then real content fades in. |
| **Infinite scroll** | Content continuously scrolls (good for showing feeds/lists). |
| **Parallax** | Background and foreground move at different speeds. Depth illusion. |
| **Masonry fill** | Items drop into a masonry grid layout, finding their positions. |
| **Carousel slide** | Cards/images slide horizontally, one becomes center focus. |

---

## 7. BACKGROUND & AMBIENT EFFECTS

| Term | What It Looks Like |
|------|-------------------|
| **Gradient shift** | Background gradient colours slowly rotate or morph. Subtle, premium. |
| **Gradient sweep** | Gradient moves across the background like a slow wave. |
| **Particles** | Small dots/shapes floating with gentle movement. Ambient tech feel. |
| **Grain / Film grain** | Subtle noise overlay. Adds texture, feels analog/premium. |
| **Bokeh** | Soft blurred circles of light in background. Warm, cinematic. |
| **Grid lines** | Subtle grid pattern in background. Tech/blueprint aesthetic. |
| **Dot grid** | Regular pattern of dots. Clean, modern. |
| **Noise texture** | Static subtle noise. Adds depth to flat colours. |
| **Vignette** | Edges of frame darken. Draws focus to center. |
| **Light leak** | Soft coloured light bleeds from edges. Warm, film-like. |
| **Glow** | Soft light emanation around an element. Neon/tech feel. |
| **Shadow grow** | Drop shadow increases. Element appears to rise/float. |
| **Blur background** | Background goes out of focus. Draws attention to foreground. |
| **Spotlight** | Bright area follows a point, rest is darker. Dramatic focus. |
| **Pulse glow** | Element gently pulses with a glow. Draws attention. |
| **Aurora** | Slow-moving colour waves in background. Premium, ethereal. |
| **Mesh gradient** | Multi-point gradient that slowly morphs. Modern, Apple-style. |

---

## 8. TIMING & EASING (How fast and with what feel)

### Duration Terms
| Term | Typical Duration | Use For |
|------|:---:|-----------|
| **Instant** | 0ms | Cuts, state swaps |
| **Snappy** | 100-150ms | Micro-interactions, button clicks |
| **Quick** | 200-300ms | Standard UI transitions |
| **Normal** | 400-600ms | Content reveals, slides |
| **Slow** | 800-1200ms | Dramatic reveals, hero animations |
| **Cinematic** | 1500-3000ms | Slow zooms, atmospheric |
| **Leisurely** | 3000ms+ | Ken Burns, background drift |

### Easing Terms (The "feel" of the motion)
| Term | What It Feels Like |
|------|-------------------|
| **Linear** | Constant speed. Robotic. Rarely what you want. |
| **Ease in** | Starts slow, accelerates. Feels like it's gaining momentum. |
| **Ease out** | Starts fast, decelerates. Feels natural, like coming to rest. Most common. |
| **Ease in-out** | Slow start, fast middle, slow end. Smooth and balanced. |
| **Spring** | Overshoots target then bounces back. Feels lively, organic. |
| **Bounce** | Hits target, bounces several times. Playful, attention-grabbing. |
| **Elastic** | Like spring but more exaggerated oscillation. |
| **Snap** | Very fast with hard stop. Decisive, punchy. |
| **Overshoot** | Goes past target slightly, then settles back. Subtle energy. |
| **Smooth** | Gentle ease in-out. No sharp acceleration. Calm. |

### Timing Terms
| Term | What It Means |
|------|--------------|
| **Delay** | Wait X seconds before starting. |
| **Stagger** | Each element starts X ms after the previous one. |
| **Sequence** | Animations play one after another (A finishes, then B starts). |
| **Simultaneous** | Multiple things animate at the same time. |
| **Overlap** | B starts before A finishes. Creates flow. |
| **Hold** | Pause on screen for X seconds before next animation. |
| **Loop** | Animation repeats continuously. |
| **Ping pong** | Animation plays forward then reverse, repeating. |

---

## 9. CAMERA & FRAMING

| Term | What It Looks Like |
|------|-------------------|
| **Zoom in** | Camera moves closer. Focuses attention, builds intensity. |
| **Zoom out** | Camera pulls back. Reveals context, establishes scene. |
| **Pan** | Camera moves horizontally. Scanning across content. |
| **Tilt** | Camera moves vertically. Scrolling down a page. |
| **Ken Burns** | Very slow zoom + slight pan on a static image. Documentary/premium feel. |
| **Dolly** | Camera moves forward/back on a track. Smooth depth movement. |
| **Tracking shot** | Camera follows an element as it moves. |
| **Crane** | Camera lifts up or descends. Dramatic reveal. |
| **Shake** | Brief camera vibration. Impact, notification, error. |
| **Rack focus** | Shift focus from foreground to background (or vice versa). Cinematic. |
| **Perspective shift** | Slight 3D rotation of the scene. Adds depth to flat UI. |

---

## 10. MOCKUP & DEVICE FRAMING

| Term | What It Looks Like |
|------|-------------------|
| **Browser mockup** | UI displayed inside a browser chrome (address bar, tabs, buttons). |
| **Laptop mockup** | UI shown on a laptop screen, slight 3D angle. |
| **Phone mockup** | UI inside a phone frame. For mobile views. |
| **Tablet mockup** | UI inside tablet frame. |
| **Floating mockup** | Screen floating in space with shadow. No device frame. Clean. |
| **Clay mockup** | Matte, textureless device frame. Neutral, design-focused. |
| **Isometric view** | 3D angled view of the screen (typically 45°). |
| **Multi-device** | Same product shown on laptop, tablet, and phone simultaneously. |
| **Screen scroll** | Content scrolls inside the mockup frame. Shows full page. |
| **Split screen** | Two states shown side by side (before/after, mobile/desktop). |

---

## 11. BRAND & STYLE MODIFIERS

| Term | Effect |
|------|--------|
| **Dark mode** | Dark background (#0a0a0a to #1a1a1a), light text. |
| **Light mode** | White/light grey background, dark text. |
| **Glassmorphism** | Frosted glass effect — semi-transparent with blur. |
| **Neumorphism** | Soft shadows creating pressed/raised illusion. |
| **Flat** | No shadows, no gradients. Clean blocks of colour. |
| **Gradient accent** | Key elements use gradient fills. |
| **Monochrome** | Single colour palette. Elegant, focused. |
| **High contrast** | Bold darks and lights. Impactful, accessible. |
| **Neon glow** | Bright saturated colours with glow effects. |
| **Minimal** | Maximum whitespace, few elements, clean typography. |
| **Editorial** | Magazine-style layout with strong typography hierarchy. |

---

## STORYBOARD TEMPLATE

Use this format when describing a video to Claude:

```
VIDEO: [Name]
DURATION: [Total seconds]
RESOLUTION: [1920x1080 / 1080x1920 / 1080x1080]
STYLE: [dark mode, minimal, brand green #0B8C00]
FONT: [Inter / DM Sans]
ASSETS: [logo.svg, dashboard-screenshot.png, etc.]

SCENE 1 (0-3s): INTRO
- Background: dark gradient shift
- Logo: scale in with spring, center screen
- Tagline: fade in below logo, 0.5s delay
- Sound: subtle whoosh

SCENE 2 (3-8s): PROBLEM
- Transition: slide left
- Text "95% of visitors leave": typewriter
- Stat "£47,000/month lost": count up with highlight sweep
- Background: subtle particles

SCENE 3 (8-15s): PRODUCT DEMO
- Transition: zoom through
- Browser mockup: slide in from bottom with overshoot
- Cursor: glide to "Live Visitors" tab
- Click: ripple effect
- Dashboard content: stagger in (cards cascade)
- Lead card: pop in with glow
- Hold 2s

SCENE 4 (15-20s): FEATURES
- Transition: crossfade
- 6 feature icons: grid populate with stagger 0.15s
- Each icon: draw on (SVG)
- Labels: fade in below each, 0.2s delay after icon

SCENE 5 (20-25s): SOCIAL PROOF
- Transition: push up
- Stat cards: rise up with stagger
- Numbers: count up
- Client logos: fade in row, stagger 0.3s

SCENE 6 (25-30s): CTA
- Transition: crossfade
- Headline: word by word, spring
- CTA button: scale in with pulse glow
- URL: typewriter
- Logo: fade in corner
```

Give that to Claude, Claude writes the Remotion code, you render.

---

## TOTAL TERM COUNT

| Category | Terms |
|----------|:---:|
| Entry animations | 23 |
| Exit animations | 11 |
| Transitions | 16 |
| Text animations | 17 |
| Cursor & interaction | 14 |
| Layout & component | 22 |
| Background & ambient | 17 |
| Timing & easing | 19 |
| Camera & framing | 11 |
| Mockup & device | 10 |
| Brand & style | 11 |
| **TOTAL** | **171** |

You don't need to memorise all 171. The most commonly used ~30 terms will cover 90% of your videos:

**The Essential 30:**
fade in, slide in, scale in, spring, pop in, rise up, typewriter, stagger, crossfade, cut, zoom through, slide transition, count up, highlight sweep, word by word, click ripple, glide, hover, tab switch, modal pop, notification toast, chart animate, gradient shift, particles, grain, ease out, spring easing, Ken Burns, browser mockup, dark mode

---

## VIDEOS NEEDED FOR LEADENGINE LAUNCH

| # | Video | Duration | Style | Priority |
|---|-------|:---:|-------|:---:|
| 1 | Hero product demo | 30s | Dark, polished, browser mockup | Day 7 |
| 2 | "What you're missing" problem video | 15s | Dark, stat-heavy, dramatic | Day 7 |
| 3 | AI Concierge feature spotlight | 15s | Dark, chat interface, typewriter | Week 2 |
| 4 | Funnel leak detection spotlight | 15s | Dark, dashboard, chart animate | Week 2 |
| 5 | Lead routing spotlight | 15s | Dark, notification toast, stagger | Week 2 |
| 6 | Real-time visitors spotlight | 15s | Dark, live counter, pulse glow | Week 2 |
| 7 | Webinar intro | 10s | Dark, logo spring, gradient shift | Week 2 |
| 8 | Webinar outro + CTA | 10s | Dark, CTA pulse, typewriter URL | Week 2 |
| 9 | LinkedIn carousel video | 30s | Dark, stat count ups, social proof | Week 2 |
| 10 | TikTok/Reels vertical clip | 15s | Dark, fast cuts, pop text | Week 2 |
