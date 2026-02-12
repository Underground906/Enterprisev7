# CALAN BRAND SYSTEM

**Version:** 1.0
**Last Updated:** 2026-02-05
**Source:** CaLan Figma Kit (Tablet)

---

## COLOR PALETTE

### Primary Colors (YOUR CUSTOMIZATIONS)
| Role | Hex | Usage |
|------|-----|-------|
| Light Secondary | #A9D4FF | Accent, highlights, active states |
| Dark Navy | #0E1E47 | Dark backgrounds, primary text on light |

### Action Colors
| Role | Hex (estimated) | Usage |
|------|-----------------|-------|
| Action Light | #A9D4FF | Buttons, links, interactive elements |
| Action Dark | #0E1E47 | Primary buttons on light mode |

### Basic Colors
| Role | Hex (estimated) | Usage |
|------|-----------------|-------|
| Black | #0A0F29 | Darkest text |
| Purple Gray | #5C5470 | Secondary text, muted elements |
| White | #FFFFFF | Backgrounds, text on dark |
| Light Gray | #E8E8ED | Disabled states, subtle backgrounds |

### Background Colors
| Role | Hex | Usage |
|------|-----|-------|
| Dark BG | #0E1E47 | Dark mode background |
| Light BG | #FFFFFF | Light mode background |

### Accent/Other Colors
| Role | Hex (estimated) | Usage | CHECK THESE |
|------|-----------------|-------|-------------|
| Coral | #FF6B4A | Alerts, errors, CTAs | May clash with navy |
| Green | #6BC66B | Success states | Should work |
| Gold | #F5C16C | Warnings, highlights | Should work |
| Blue | #4A7BF7 | Links, info states | May compete with #A9D4FF |

### Border Colors
| Role | Hex (estimated) | Usage |
|------|-----------------|-------|
| Purple Border | #3D2F7C | Active borders, focus states |
| Light Border | #E0E0E6 | Default borders |
| Subtle Border | #F0F0F4 | Subtle separators |

---

## TYPOGRAPHY

### Font Family
**DM Sans** (Google Fonts)

### SPACING FIX NEEDED
- Current: -3.6% letter-spacing
- Target: 0% letter-spacing
- Action: Update all text styles in Figma

### Type Scale

| Style | Size | Line Height | Weight | Letter Spacing |
|-------|------|-------------|--------|----------------|
| Display 1 | 72px | 78px | Bold (700) | 0% |
| Display 2 | 64px | 72px | Bold (700) | 0% |
| Display 3 | 48px | 56px | Bold (700) | 0% |
| Headline 1 | 48px | 56px | Bold (700) | 0% |
| Headline 2 | 24px | 34px | Bold (700) | 0% |
| Headline 3 | 22px | 32px | Bold (700) | 0% |
| Headline 4 | 28px | 38px | Bold (700) | 0% |
| Headline 5 | 16px | 26px | Bold (700) | 0% |
| Headline 6 | 14px | 24px | Bold (700) | 0% |
| Paragraph 1 | 18px | 28px | Regular (400) | 0% |
| Paragraph 2 | 16px | 26px | Regular (400) | 0% |
| Paragraph 3 | 14px | 24px | Regular (400) | 0% |

---

## COLOR CONTRAST CHECK

Testing your primary colors against WCAG 2.1 AA:

| Combination | Contrast Ratio | Pass? |
|-------------|----------------|-------|
| #0E1E47 on #FFFFFF | ~15:1 | ✅ AAA |
| #FFFFFF on #0E1E47 | ~15:1 | ✅ AAA |
| #0E1E47 on #A9D4FF | ~8:1 | ✅ AAA |
| #A9D4FF on #0E1E47 | ~8:1 | ✅ AAA |

Your two primary colors work excellently together.

---

## COLORS TO CHECK/ADJUST

Based on your new #A9D4FF + #0E1E47 palette:

### Potentially Problematic:
1. **Coral #FF6B4A** - Warm color may feel disconnected from cool navy/blue palette
   - Consider: Softer coral or switch to a blue-based red

2. **Blue #4A7BF7** - Very close to your #A9D4FF, may cause confusion
   - Consider: Use only one blue, or make them more distinct

3. **Purple Border #3D2F7C** - Could work, but test against your navy
   - May look muddy next to #0E1E47

### Should Work Fine:
- Green #6BC66B - Universal success color
- Gold #F5C16C - Good contrast, warm accent
- Light grays - Neutral, won't clash

---

## FIGMA FIX: Letter Spacing

To fix the -3.6% spacing globally in Figma:

1. Open your file
2. Go to the **Text Styles** panel (right sidebar)
3. For each style:
   - Right-click → Edit Style
   - Change Letter Spacing from -3.6% to 0%
   - Click Update

Or use **Find and Replace Styles** plugin for bulk update.

---

## TAILWIND CONFIG (for development)

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        'calan': {
          'navy': '#0E1E47',
          'light-blue': '#A9D4FF',
          'black': '#0A0F29',
          'gray': '#5C5470',
          'light-gray': '#E8E8ED',
          'coral': '#FF6B4A',
          'green': '#6BC66B',
          'gold': '#F5C16C',
          'blue': '#4A7BF7',
          'purple': '#3D2F7C',
        }
      },
      fontFamily: {
        'sans': ['DM Sans', 'sans-serif'],
      },
      fontSize: {
        'display-1': ['72px', { lineHeight: '78px', fontWeight: '700' }],
        'display-2': ['64px', { lineHeight: '72px', fontWeight: '700' }],
        'display-3': ['48px', { lineHeight: '56px', fontWeight: '700' }],
        'h1': ['48px', { lineHeight: '56px', fontWeight: '700' }],
        'h2': ['24px', { lineHeight: '34px', fontWeight: '700' }],
        'h3': ['22px', { lineHeight: '32px', fontWeight: '700' }],
        'h4': ['28px', { lineHeight: '38px', fontWeight: '700' }],
        'h5': ['16px', { lineHeight: '26px', fontWeight: '700' }],
        'h6': ['14px', { lineHeight: '24px', fontWeight: '700' }],
        'body-lg': ['18px', { lineHeight: '28px', fontWeight: '400' }],
        'body': ['16px', { lineHeight: '26px', fontWeight: '400' }],
        'body-sm': ['14px', { lineHeight: '24px', fontWeight: '400' }],
      }
    }
  }
}
```

---

## CSS VARIABLES (for any framework)

```css
:root {
  /* Colors */
  --color-navy: #0E1E47;
  --color-light-blue: #A9D4FF;
  --color-black: #0A0F29;
  --color-gray: #5C5470;
  --color-light-gray: #E8E8ED;
  --color-coral: #FF6B4A;
  --color-green: #6BC66B;
  --color-gold: #F5C16C;
  --color-blue: #4A7BF7;
  --color-purple: #3D2F7C;
  --color-white: #FFFFFF;

  /* Typography */
  --font-family: 'DM Sans', sans-serif;
  --letter-spacing: 0;
}
```

---

## NEXT STEPS

1. **Fix letter spacing in Figma** - 5 minutes
2. **Decide on the questionable colors** (coral, secondary blue, purple)
3. **Export final tokens** from Figma using Tokens Studio
4. **Apply to your component library** - batch update

---

**This is your locked brand system. Any changes go through this document.**
