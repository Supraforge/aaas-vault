# TUI Design System

> Senior-level terminal UI design principles, patterns, and aesthetics

## Design Philosophy

### The Terminal is a Canvas
The terminal isn't a limitation—it's a medium with its own aesthetic language. Great TUI design embraces constraints: monospace fonts, limited colors, character-based drawing. These aren't bugs, they're features that create a distinct visual identity impossible in GUIs.

### Core Principles

1. **Information Hierarchy** - Guide the eye through visual weight
2. **Breathing Room** - Whitespace is your friend, even in terminals
3. **Consistent Rhythm** - Establish patterns, then maintain them
4. **Purposeful Color** - Every color should communicate meaning
5. **Typography as Structure** - Monospace is your only font; use it wisely

---

## Visual Building Blocks

### Box-Drawing Characters

```
┌─────────────────────────────────────────────────────────────┐
│  SINGLE LINE                                                │
│  ┌──────┐  Corners: ┌ ┐ └ ┘                                │
│  │      │  Lines:   ─ │                                    │
│  │      │  T-junctions: ┬ ┴ ├ ┤                            │
│  └──────┘  Cross: ┼                                        │
├─────────────────────────────────────────────────────────────┤
│  DOUBLE LINE                                                │
│  ╔══════╗  Corners: ╔ ╗ ╚ ╝                                │
│  ║      ║  Lines:   ═ ║                                    │
│  ║      ║  T-junctions: ╦ ╩ ╠ ╣                            │
│  ╚══════╝  Cross: ╬                                        │
├─────────────────────────────────────────────────────────────┤
│  ROUNDED                                                    │
│  ╭──────╮  Corners: ╭ ╮ ╰ ╯                                │
│  │      │  (Combine with single line characters)           │
│  │      │                                                  │
│  ╰──────╯                                                  │
├─────────────────────────────────────────────────────────────┤
│  HEAVY/BOLD                                                 │
│  ┏━━━━━━┓  Corners: ┏ ┓ ┗ ┛                                │
│  ┃      ┃  Lines:   ━ ┃                                    │
│  ┃      ┃  T-junctions: ┳ ┻ ┣ ┫                            │
│  ┗━━━━━━┛  Cross: ╋                                        │
├─────────────────────────────────────────────────────────────┤
│  ASCII (Maximum Compatibility)                              │
│  +------+  Corners: +                                      │
│  |      |  Lines:   - |                                    │
│  |      |  Cross: +                                        │
│  +------+                                                  │
└─────────────────────────────────────────────────────────────┘
```

### Block Characters (For Graphs & Progress)

```
FULL BLOCKS     ████████████████████████████████
LIGHT SHADE     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
MEDIUM SHADE    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
DARK SHADE      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

PARTIAL BLOCKS  ▏▎▍▌▋▊▉█  (1/8 to full)

QUADRANTS       ▖ ▗ ▘ ▙ ▚ ▛ ▜ ▝ ▞ ▟

BRAILLE         ⠁⠂⠃⠄⠅⠆⠇⡀⡁⡂⡃⡄⡅⡆⡇  (For high-res graphs)
```

### Symbols & Icons

```
STATUS          ✓ ✗ ● ○ ◉ ◎ ■ □ ▪ ▫ ★ ☆ ♦ ♢
ARROWS          ← → ↑ ↓ ↔ ↕ ⇐ ⇒ ⇑ ⇓ ➜ ➤ ▶ ◀ ▲ ▼
MATH            × ÷ ± ≤ ≥ ≠ ≈ ∞ √ ∑ ∏ ∫
MISC            … · • ¦ § ¶ © ® ™ ° ′ ″
SPINNERS        ⠋ ⠙ ⠹ ⠸ ⠼ ⠴ ⠦ ⠧ ⠇ ⠏  (Braille)
                ◐ ◓ ◑ ◒  (Quarter circles)
                ◴ ◷ ◶ ◵  (Quarter squares)
                ▁ ▂ ▃ ▄ ▅ ▆ ▇ █  (Growing bar)
```

---

## Color Theory for Terminals

### The 16-Color Base Palette

Most terminals support at least 16 colors. Design for this first, enhance for 256/truecolor.

```
Standard 8:
  0 Black     1 Red       2 Green     3 Yellow
  4 Blue      5 Magenta   6 Cyan      7 White

Bright 8:
  8 Bright Black (Gray)   9 Bright Red
 10 Bright Green         11 Bright Yellow
 12 Bright Blue          13 Bright Magenta
 14 Bright Cyan          15 Bright White
```

### Color Semantics (Consistent Meaning)

| Color | Primary Use | Secondary Use |
|-------|-------------|---------------|
| **Red** | Errors, danger, deletion | Urgent alerts |
| **Green** | Success, addition, positive | Active/online status |
| **Yellow** | Warnings, caution | In-progress, pending |
| **Blue** | Information, links | Primary actions |
| **Magenta** | Special, unique | Syntax highlighting |
| **Cyan** | Secondary info | Commands, paths |
| **White** | Primary text | - |
| **Gray** | Disabled, hints, dimmed | Comments, metadata |

### Contrast Rules

```
GOOD CONTRAST (AAA):
  White on Black       ████████  High contrast, easy to read
  Black on White       ████████  Inverted, good for headers
  Yellow on Black      ████████  Attention-grabbing
  Cyan on Black        ████████  Good for secondary text

POOR CONTRAST (Avoid):
  Red on Blue          ████████  Vibrates, hard to read
  Green on Red         ████████  Colorblind-unfriendly
  Yellow on White      ████████  Nearly invisible
  Blue on Black        ████████  Too dark
```

### Dark vs Light Mode

```
DARK MODE (Default):
  Background: Black/Dark Gray (#0d1117)
  Primary Text: White/Light Gray (#c9d1d9)
  Secondary Text: Gray (#8b949e)
  Accent: Bright colors pop

LIGHT MODE:
  Background: White/Light (#ffffff)
  Primary Text: Dark Gray (#24292f)
  Secondary Text: Gray (#57606a)
  Accent: Muted colors work better
```

---

## Typography in Monospace

### Hierarchy Through Style

Since you can't change font size, use these techniques:

```
═══════════════════════════════════════════════════════════════
                        TITLE (CENTERED, CAPS)
═══════════════════════════════════════════════════════════════

## SECTION HEADER (CAPS, UNDERLINED)
───────────────────────────────────────────────────────────────

### Subsection (Title Case)

Body text uses normal case. Keep lines readable—aim for 60-80
characters per line maximum.

**Bold Text** for emphasis (using ANSI bold)
*Italic Text* for subtle emphasis (using ANSI italic)
`Code` for commands, paths, values (using different color)

> Blockquotes for callouts (indent + different color)

• Bullet points for lists
  ◦ Sub-bullets indented
    ‣ Third level

1. Numbered lists for sequences
   a. Sub-items
   b. Continue pattern
```

### Alignment Patterns

```
LEFT ALIGNED (Default)
Name:        Value
Status:      Active
Created:     2024-01-15

RIGHT ALIGNED (Numbers, Dates)
        Name: Project Alpha
      Status: Active
     Created: 2024-01-15

CENTERED (Titles, Headers)
        ╔══════════════════════╗
        ║    SYSTEM STATUS     ║
        ╚══════════════════════╝

JUSTIFIED (Tables)
┌────────────┬────────┬────────────┐
│ Name       │ Status │ Created    │
├────────────┼────────┼────────────┤
│ Alpha      │ Active │ 2024-01-15 │
│ Beta       │ Idle   │ 2024-01-10 │
└────────────┴────────┴────────────┘
```

---

## Layout Patterns

### The Grid System

Think in character cells. Common terminal widths:

| Width | Use Case |
|-------|----------|
| 80 | Classic terminal, maximum compatibility |
| 120 | Modern wide terminal |
| Full-width | Responsive, fills available space |

### Spacing Standards

```
PADDING (Inside borders):
  Minimal:  1 character
  Normal:   2 characters
  Generous: 3-4 characters

MARGIN (Between elements):
  Tight:    1 line
  Normal:   2 lines
  Spacious: 3+ lines

EXAMPLE:
┌──────────────────────────────────────┐
│                                      │  ← 1 char top padding
│  Content here with 2-char padding    │
│                                      │  ← 1 char bottom padding
└──────────────────────────────────────┘

                                          ← 2 lines between elements

┌──────────────────────────────────────┐
│  Next element                        │
└──────────────────────────────────────┘
```

### Common Layout Templates

```
SINGLE COLUMN (Simple)
┌────────────────────────────────────────────────────────────────────┐
│  Header                                                            │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  Main Content Area                                                 │
│                                                                    │
├────────────────────────────────────────────────────────────────────┤
│  Footer                                                            │
└────────────────────────────────────────────────────────────────────┘

SIDEBAR + MAIN (Dashboard)
┌────────────────┬───────────────────────────────────────────────────┐
│  Sidebar       │  Main Content                                     │
│                │                                                   │
│  • Item 1      │                                                   │
│  • Item 2      │                                                   │
│  • Item 3      │                                                   │
│                │                                                   │
└────────────────┴───────────────────────────────────────────────────┘

SPLIT PANES (Comparison)
┌─────────────────────────────────┬─────────────────────────────────┐
│  Left Pane                      │  Right Pane                     │
│                                 │                                 │
│                                 │                                 │
└─────────────────────────────────┴─────────────────────────────────┘

QUADRANT (Monitoring)
┌─────────────────────────────────┬─────────────────────────────────┐
│  Panel 1                        │  Panel 2                        │
│                                 │                                 │
├─────────────────────────────────┼─────────────────────────────────┤
│  Panel 3                        │  Panel 4                        │
│                                 │                                 │
└─────────────────────────────────┴─────────────────────────────────┘

MODAL/DIALOG (Overlay)
┌────────────────────────────────────────────────────────────────────┐
│  Background content (dimmed)                                       │
│                     ┌─────────────────────────┐                    │
│                     │  Modal Title            │                    │
│                     ├─────────────────────────┤                    │
│                     │  Modal content here     │                    │
│                     │                         │                    │
│                     │  [Cancel]  [Confirm]    │                    │
│                     └─────────────────────────┘                    │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

---

## Animation & Motion

### Principles

1. **Purposeful** - Animation should communicate, not decorate
2. **Fast** - Terminal users expect speed; keep animations under 300ms
3. **Interruptible** - User input should always take priority

### Common Animations

```
SPINNER (Continuous)
  Dots:     ⠋ ⠙ ⠹ ⠸ ⠼ ⠴ ⠦ ⠧ ⠇ ⠏
  Line:     - \ | /
  Bounce:   ⠁ ⠂ ⠄ ⠂
  Pulse:    ◐ ◓ ◑ ◒

PROGRESS (Linear)
  Bar:      ░░░░░░░░░░ → █████░░░░░ → ██████████
  Dots:     ...        → ......     → ..........
  Blocks:   ▏▎▍▌▋▊▉█

TRANSITION (State Change)
  Fade in:  (dim) → (normal) → (bright)
  Slide:    Move content left/right/up/down
  Expand:   Small box → Large box

FEEDBACK (User Action)
  Flash:    Briefly invert colors on selection
  Highlight: Brighten then fade
  Shake:    Horizontal jitter on error
```

### Implementation Tips

```go
// Smooth spinner (Bubbletea)
spinner.Spinner = spinner.Spinner{
    Frames: []string{"⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"},
    FPS:    time.Second / 10,
}

// Progress animation
for i := 0; i <= 100; i++ {
    filled := i * width / 100
    bar := strings.Repeat("█", filled) + strings.Repeat("░", width-filled)
    fmt.Printf("\r%s %d%%", bar, i)
    time.Sleep(20 * time.Millisecond)
}
```

---

## Accessibility

### Color Blindness Considerations

```
PROBLEMATIC COMBINATIONS:
  Red + Green    (8% of males affected)
  Blue + Purple
  Green + Brown

SOLUTIONS:
  1. Don't rely solely on color—add symbols
     ✓ Success (green)    ✗ Error (red)    ⚠ Warning (yellow)

  2. Use patterns/textures for graphs
     █████  vs  ▓▓▓▓▓  vs  ░░░░░

  3. Ensure sufficient contrast
     High contrast mode: White on black only
```

### Screen Reader Support

```
1. Provide text alternatives for visual elements
   Progress: "50% complete" not just "██████░░░░░░"

2. Announce state changes
   "Loading started" → "Loading complete"

3. Use semantic structure
   Headers, lists, regions

4. Support reduced motion
   if (prefersReducedMotion) {
       disableAnimations()
   }
```

---

## Responsive Design

### Width Breakpoints

```go
switch {
case width < 40:
    // Compact mode: Stack everything vertically
    // Hide non-essential elements
    // Use abbreviations

case width < 80:
    // Standard mode: Single column
    // Full labels
    // Basic formatting

case width < 120:
    // Wide mode: Two columns possible
    // Sidebar + main content
    // More whitespace

default:
    // Ultra-wide: Three columns
    // Full dashboard layouts
    // Maximum information density
}
```

### Graceful Degradation

```
FULL WIDTH (120+):
┌─ Status ──────────────────┬─ Details ─────────────────────────────┐
│ ● Server: Online          │ Last checked: 2024-01-15 10:30:00     │
│ ● Database: Connected     │ Response time: 45ms                   │
│ ● Cache: Active           │ Memory usage: 67%                     │
└───────────────────────────┴───────────────────────────────────────┘

MEDIUM WIDTH (80):
┌─ Status ──────────────────────────────────────────┐
│ ● Server: Online    │ Last check: 10:30          │
│ ● Database: OK      │ Response: 45ms             │
│ ● Cache: Active     │ Memory: 67%                │
└───────────────────────────────────────────────────┘

NARROW WIDTH (40):
┌─ Status ───────────────┐
│ ● Server    Online     │
│ ● Database  OK         │
│ ● Cache     Active     │
│ Mem: 67%  Resp: 45ms   │
└────────────────────────┘

MINIMAL WIDTH (<40):
Status: All OK
Mem: 67% | 45ms
```

---

## Component Library

### Buttons

```
STANDARD:
  [ Submit ]  [ Cancel ]

WITH ICONS:
  [ ✓ Save ]  [ ✗ Cancel ]  [ ↻ Refresh ]

STATES:
  [ Normal  ]     Default state
  [ FOCUSED ]     Bold/highlighted when selected
  [ Disabled]     Dimmed, no interaction

VARIANTS:
  ┌──────────┐
  │  Primary │     Filled background
  └──────────┘

  [ Secondary ]    Outlined

  ⟨ Minimal ⟩      No border
```

### Inputs

```
TEXT INPUT:
  Label: █                              Empty
  Label: John Doe█                      With value
  Label: ████████ (hidden)              Password

  ┌─ Name ────────────────────────────┐
  │ John Doe█                         │  Boxed variant
  └───────────────────────────────────┘

SELECT/DROPDOWN:
  Option: [  Option 1          ▼]

  ┌─ Select Option ───────────────────┐
  │ > Option 1                        │
  │   Option 2                        │
  │   Option 3                        │
  └───────────────────────────────────┘

CHECKBOX/RADIO:
  [✓] Option A                          Checkbox
  [ ] Option B

  (●) Choice A                          Radio
  ( ) Choice B
  ( ) Choice C
```

### Lists

```
SIMPLE LIST:
  • Item one
  • Item two
  • Item three

SELECTABLE LIST:
  > Item one     ← Selected (highlighted)
    Item two
    Item three

HIERARCHICAL:
  ▼ Parent
    ├── Child 1
    ├── Child 2
    └── Child 3

NUMBERED:
  1. First step
  2. Second step
  3. Third step
```

### Tables

```
SIMPLE:
  Name          Status    Created
  ─────────────────────────────────
  Project A     Active    Jan 15
  Project B     Pending   Jan 10

BORDERED:
  ┌─────────────┬──────────┬───────────┐
  │ Name        │ Status   │ Created   │
  ├─────────────┼──────────┼───────────┤
  │ Project A   │ Active   │ Jan 15    │
  │ Project B   │ Pending  │ Jan 10    │
  └─────────────┴──────────┴───────────┘

WITH SELECTION:
  ┌─────────────┬──────────┬───────────┐
  │ Name        │ Status   │ Created   │
  ├─────────────┼──────────┼───────────┤
  │ > Project A │ Active   │ Jan 15    │  ← Selected row
  │   Project B │ Pending  │ Jan 10    │
  └─────────────┴──────────┴───────────┘
```

### Status Indicators

```
BADGES:
  [SUCCESS]  [WARNING]  [ERROR]  [INFO]

DOTS:
  ● Online   ● Degraded   ● Offline
  (green)    (yellow)     (red)

ICONS:
  ✓ Passed   ⚠ Warning   ✗ Failed   ○ Pending   ⋯ Running

PROGRESS:
  ████████████████░░░░░░░░  67%

  Step 1 ── Step 2 ── Step 3 ── Step 4
    ✓         ✓         ●         ○
```

---

## Design Checklist

### Before Shipping

- [ ] Works in 80-column terminals
- [ ] Readable without color (symbols backup color)
- [ ] Clear information hierarchy
- [ ] Consistent spacing and alignment
- [ ] Keyboard fully navigable
- [ ] Error states are helpful
- [ ] Loading states provide feedback
- [ ] Respects NO_COLOR environment variable
- [ ] Works in both dark and light terminals
