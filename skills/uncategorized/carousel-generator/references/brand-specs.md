# Brand Specifications

## Color Palette

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Deep Teal | #207178 | (32, 113, 120) | Titles, CTAs, primary branding |
| Mist Aqua | #E4F1EF | (228, 241, 239) | Slide backgrounds, soft elements |
| Warm Coral | #F28C81 | (242, 140, 129) | Accent highlights, bullet points |
| Off-White | #F8F9FA | (248, 249, 250) | Alternative backgrounds |
| Charcoal | #333333 | (51, 51, 51) | Body text, high contrast |
| Heart Red | #E63946 | (230, 57, 70) | Emphasis, danger alerts |

## Typography

### Font Family
- **Primary:** Inter (all weights)
- **Fallback 1:** Helvetica (macOS system font)
- **Fallback 2:** Arial (Windows/Linux)
- **Fallback 3:** System default

### Font Sizes
| Element | Size | Weight |
|---------|------|--------|
| Title (title slide) | 60px | Bold |
| Subtitle | 48px | SemiBold |
| Body text | 36px | Regular |
| Footer name | 28px | Medium |
| Footer handle | 24px | Regular |

## Image Specifications

### Instagram Carousel
- **Dimensions:** 1080 x 1080 px (square)
- **Margin:** 80px all sides
- **Content area:** 920 x 850 px
- **Footer height:** 150px
- **Max slides:** 10 (Instagram limit)

### Instagram Infographic (Future)
- **Dimensions:** 1080 x 1350 px (portrait)
- **Margin:** 80px all sides
- **Footer height:** 150px

## Footer Design

```
┌──────────────────────────────────────────┐
│                CONTENT                    │
│                                          │
├──────────────────────────────────────────┤
│ [Photo] Dr. Shailesh Singh               │
│         @heartdocshailesh                │
└──────────────────────────────────────────┘
```

- Subtle separator line (Mist Aqua, 2px)
- Profile photo: 100x100px circular
- Photo positioned left, text to the right
- Name in Charcoal
- Handle in Deep Teal

## Account Handles

| Account | Handle | Use Case |
|---------|--------|----------|
| 1 | @heartdocshailesh | Primary cardiology content |
| 2 | @dr.shailesh.singh | Professional/clinical |

## Title Slide Design

- Background: Deep Teal (#207178)
- Text: White (#FFFFFF)
- Centered vertically and horizontally
- Subtitle in Mist Aqua below title

## Content Slide Design

- Background: Off-White (#F8F9FA)
- Title: Deep Teal, top-aligned
- Body: Charcoal
- Bullet points: Warm Coral circles (10px diameter)
- Footer at bottom

## Accessibility

- Minimum contrast ratio: 4.5:1 for body text
- Title text on teal background: White (15.5:1 ratio)
- Body text on white: Charcoal (12.6:1 ratio)
- All text readable at mobile size

## File Naming

- Slides: `slide-01.png`, `slide-02.png`, etc.
- Output folder: `output/carousels/<topic>/account-<n>/`
