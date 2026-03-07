# TUI Style Presets

> Ready-to-use aesthetic systems for terminal interfaces

## Style Index

| Style | Vibe | Best For |
|-------|------|----------|
| [Corporate](#corporate) | Clean, professional, trustworthy | Enterprise tools, B2B |
| [Hacker](#hacker) | Matrix-style, technical, edgy | Dev tools, security |
| [Retro/DOS](#retro-dos) | 80s computing, nostalgic | Games, novelty apps |
| [Cyberpunk](#cyberpunk) | Neon, high-tech, futuristic | Monitoring, dashboards |
| [Minimal](#minimal) | Clean, zen, focused | Productivity, writing |
| [Pip-Boy](#pip-boy) | Fallout-inspired, amber CRT | Games, themed apps |
| [Synthwave](#synthwave) | 80s neon, vaporwave | Music apps, creative tools |
| [Nord](#nord) | Arctic, calm, muted | Code editors, everyday use |
| [Dracula](#dracula) | Dark, purple-accented | Dev environments |
| [Gruvbox](#gruvbox) | Warm, earthy, retro | Text-heavy apps |

---

## Corporate

> Clean lines, professional blues, enterprise-grade trust

### Philosophy
Corporate design prioritizes clarity, accessibility, and professionalism. It should feel like enterprise software—reliable, not flashy.

### Color Palette

```
┌─────────────────────────────────────────────────────────────┐
│  CORPORATE PALETTE                                          │
├─────────────────────────────────────────────────────────────┤
│  Background    #1a1a2e    ████  Deep navy                  │
│  Surface       #16213e    ████  Slightly lighter           │
│  Primary       #0f4c75    ████  Corporate blue             │
│  Accent        #3282b8    ████  Bright blue                │
│  Text          #e8e8e8    ████  Light gray                 │
│  Muted         #6b7280    ████  Gray                       │
│  Success       #10b981    ████  Green                      │
│  Warning       #f59e0b    ████  Amber                      │
│  Error         #ef4444    ████  Red                        │
└─────────────────────────────────────────────────────────────┘
```

### Visual Language

```
BORDERS: Single line, rounded corners
╭──────────────────────────────────────────────────────────────╮
│                                                              │
│   ACME CORP DASHBOARD                                        │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   Quarterly Report                                           │
│   ────────────────                                           │
│                                                              │
│   Revenue     $1,234,567    ▲ 12.5%                         │
│   Users       45,678        ▲ 8.3%                          │
│   Churn       2.1%          ▼ 0.5%                          │
│                                                              │
│   ┌─────────────────────────────────────────────────────┐   │
│   │ ████████████████████████████████░░░░░░░░░░  78%     │   │
│   │ Q4 Target Progress                                  │   │
│   └─────────────────────────────────────────────────────┘   │
│                                                              │
│                              [ View Details ]  [ Export ]   │
│                                                              │
╰──────────────────────────────────────────────────────────────╯
```

### Lipgloss (Go)

```go
var CorporateStyle = struct {
    Background lipgloss.Color
    Surface    lipgloss.Color
    Primary    lipgloss.Color
    Accent     lipgloss.Color
    Text       lipgloss.Color
    Muted      lipgloss.Color
}{
    Background: lipgloss.Color("#1a1a2e"),
    Surface:    lipgloss.Color("#16213e"),
    Primary:    lipgloss.Color("#0f4c75"),
    Accent:     lipgloss.Color("#3282b8"),
    Text:       lipgloss.Color("#e8e8e8"),
    Muted:      lipgloss.Color("#6b7280"),
}

headerStyle := lipgloss.NewStyle().
    Background(CorporateStyle.Primary).
    Foreground(lipgloss.Color("#ffffff")).
    Bold(true).
    Padding(0, 2)

boxStyle := lipgloss.NewStyle().
    Border(lipgloss.RoundedBorder()).
    BorderForeground(CorporateStyle.Accent).
    Padding(1, 2)
```

---

## Hacker

> Green-on-black Matrix aesthetic, technical and edgy

### Philosophy
Channel the feeling of being inside the machine. Dense information, scrolling text, the aesthetic of power users and security researchers.

### Color Palette

```
┌─────────────────────────────────────────────────────────────┐
│  HACKER PALETTE                                             │
├─────────────────────────────────────────────────────────────┤
│  Background    #0a0a0a    ████  Near black                 │
│  Surface       #111111    ████  Slightly lighter           │
│  Primary       #00ff00    ████  Matrix green               │
│  Accent        #00cc00    ████  Darker green               │
│  Text          #00ff00    ████  Green text                 │
│  Muted         #006600    ████  Dim green                  │
│  Highlight     #00ff00    ████  Bright green (inverted)    │
│  Error         #ff0000    ████  Red alert                  │
│  Warning       #ffff00    ████  Yellow                     │
└─────────────────────────────────────────────────────────────┘
```

### Visual Language

```
BORDERS: ASCII or single line, sharp corners
+==============================================================+
|                                                              |
|  > SYSTEM ACCESS GRANTED                                     |
|  > USER: root@mainframe                                      |
|  > SESSION: 0x7F3A2B1C                                       |
|                                                              |
+--------------------------------------------------------------+
|                                                              |
|  [SCANNING NETWORK...]                                       |
|                                                              |
|  192.168.1.1    ████████████████████  ONLINE   [ANALYZE]    |
|  192.168.1.24   ████████████░░░░░░░░  PARTIAL  [ANALYZE]    |
|  192.168.1.105  ░░░░░░░░░░░░░░░░░░░░  OFFLINE  [  SKIP ]    |
|                                                              |
|  > Found 2 active nodes                                      |
|  > Scanning ports...                                         |
|  > ████████████████░░░░░░░░  67% [PORT 443]                 |
|                                                              |
|  [ABORT]  [PAUSE]  [EXPORT LOG]                             |
|                                                              |
+==============================================================+
```

### Animation Style

```
TYPEWRITER EFFECT:
> Initializing connection...
> Handshake complete
> Decrypting payload█

MATRIX RAIN:
  ア イ ウ エ オ カ キ ク ケ コ
   ワ ヰ ヱ ヲ ン ヴ ヵ ヶ
    タ チ ツ テ ト ナ ニ
     サ シ ス セ ソ

SCAN LINE:
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
```

---

## Retro DOS

> 80s computing nostalgia, CGA colors, blocky aesthetic

### Philosophy
Transport users back to the DOS era. Limited color palette, blocky UI elements, that distinctive early PC feel.

### Color Palette (CGA)

```
┌─────────────────────────────────────────────────────────────┐
│  DOS/CGA PALETTE                                            │
├─────────────────────────────────────────────────────────────┤
│  Background    #0000aa    ████  DOS Blue                   │
│  Surface       #000000    ████  Black                      │
│  Primary       #ffff55    ████  Yellow                     │
│  Accent        #55ffff    ████  Cyan                       │
│  Text          #ffffff    ████  White                      │
│  Muted         #aaaaaa    ████  Gray                       │
│  Highlight     #ff55ff    ████  Magenta                    │
│  Border        #ffffff    ████  White                      │
└─────────────────────────────────────────────────────────────┘
```

### Visual Language

```
BORDERS: Double line, blocky
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║    ██████╗  ██████╗ ███████╗    ████████╗██╗   ██╗██╗       ║
║    ██╔══██╗██╔═══██╗██╔════╝    ╚══██╔══╝██║   ██║██║       ║
║    ██║  ██║██║   ██║███████╗       ██║   ██║   ██║██║       ║
║    ██║  ██║██║   ██║╚════██║       ██║   ██║   ██║██║       ║
║    ██████╔╝╚██████╔╝███████║       ██║   ╚██████╔╝██║       ║
║    ╚═════╝  ╚═════╝ ╚══════╝       ╚═╝    ╚═════╝ ╚═╝       ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║   C:\> dir                                                   ║
║                                                              ║
║   Volume in drive C is MAIN                                  ║
║   Directory of C:\                                           ║
║                                                              ║
║   COMMAND  COM     47,845  01-15-24   10:30a                ║
║   CONFIG   SYS        256  01-15-24   10:30a                ║
║   AUTOEXEC BAT        128  01-15-24   10:30a                ║
║                                                              ║
║          3 file(s)     48,229 bytes                          ║
║          0 dir(s)   1,234,567 bytes free                     ║
║                                                              ║
║   C:\> █                                                     ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

BUTTONS: Block style
┌────────────────┐   ┌────────────────┐   ┌────────────────┐
│   < Yes  >     │   │   < No   >     │   │   < Cancel >   │
└────────────────┘   └────────────────┘   └────────────────┘

MENUS: Highlighted bar
┌─ File ─────────────────┐
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │  ← New        Ctrl+N
│   Open...    Ctrl+O    │
│   Save       Ctrl+S    │
│ ─────────────────────  │
│   Exit       Alt+X     │
└────────────────────────┘
```

---

## Cyberpunk

> Neon-drenched, high-tech dystopia, glitch aesthetic

### Philosophy
Maximum visual intensity. Neon colors against dark backgrounds, glitch effects, the feeling of a rain-soaked neon cityscape.

### Color Palette

```
┌─────────────────────────────────────────────────────────────┐
│  CYBERPUNK PALETTE                                          │
├─────────────────────────────────────────────────────────────┤
│  Background    #0d0d0d    ████  Near black                 │
│  Surface       #1a1a2e    ████  Dark purple-black          │
│  Primary       #ff00ff    ████  Hot magenta                │
│  Secondary     #00ffff    ████  Electric cyan              │
│  Accent        #ff6b6b    ████  Neon coral                 │
│  Text          #ffffff    ████  White                      │
│  Muted         #4a4a6a    ████  Purple-gray                │
│  Warning       #ffff00    ████  Yellow                     │
│  Glow          #ff00ff    ████  Magenta glow               │
└─────────────────────────────────────────────────────────────┘
```

### Visual Language

```
BORDERS: Heavy, with glow effect (double colors)
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                              ┃
┃   ░█▀▀░█░█░█▀▄░█▀▀░█▀▄░█▀█░█░█░█▀█░█░█                      ┃
┃   ░█░░░░█░░█▀▄░█▀▀░█▀▄░█▀▀░█░█░█░█░█▀▄                      ┃
┃   ░▀▀▀░░▀░░▀▀░░▀▀▀░▀░▀░▀░░░▀▀▀░▀░▀░▀░▀                      ┃
┃                                                              ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃                                                              ┃
┃   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                 ┃
┃   NEURAL LINK ACTIVE        ║ SYNC: 98.7%                   ┃
┃   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                 ┃
┃                                                              ┃
┃   ┌─────────────────┐  ┌─────────────────┐                  ┃
┃   │ ◢◤ UPLOAD ◢◤    │  │ ◢◤ DOWNLOAD ◢◤  │                  ┃
┃   │     2.4 GB/s    │  │     1.8 GB/s    │                  ┃
┃   └─────────────────┘  └─────────────────┘                  ┃
┃                                                              ┃
┃   [ JACK IN ]  [ DISCONNECT ]  [ TRACE ]                    ┃
┃                                                              ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

GLITCH TEXT EFFECT:
N̷E̵U̴R̷A̸L̶ ̵L̶I̵N̴K̵ ̶A̵C̸T̵I̵V̸E̴

SCAN LINES:
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
```

---

## Minimal

> Clean, zen-like, maximum focus on content

### Philosophy
Strip away everything unnecessary. Let content breathe. Minimal borders, subtle colors, pure function.

### Color Palette

```
┌─────────────────────────────────────────────────────────────┐
│  MINIMAL PALETTE                                            │
├─────────────────────────────────────────────────────────────┤
│  Background    #1a1a1a    ████  Soft black                 │
│  Surface       #2d2d2d    ████  Dark gray                  │
│  Primary       #ffffff    ████  White                      │
│  Accent        #888888    ████  Medium gray                │
│  Text          #e0e0e0    ████  Light gray                 │
│  Muted         #666666    ████  Dim gray                   │
│  Subtle        #333333    ████  Barely visible             │
└─────────────────────────────────────────────────────────────┘
```

### Visual Language

```
BORDERS: None or very subtle

  Tasks

  ○ Buy groceries
  ○ Finish report
  ● Call mom                    ← Selected (filled)
  ○ Exercise

  ─────────────────────────────

  Press Enter to complete, Tab to edit


NO BOXES, JUST SPACE:

  Welcome back.

  You have 3 tasks remaining.
  2 hours of focus time logged.



  What would you like to do?

  > Start focus session
    View tasks
    Settings




  ↑↓ navigate    enter select    q quit
```

---

## Pip-Boy

> Fallout-inspired, amber CRT, post-apocalyptic retro

### Philosophy
Channel the Fallout Pip-Boy device. Amber/green phosphor CRT aesthetic, rounded edges, that distinctive vault-tec feel.

### Color Palette

```
┌─────────────────────────────────────────────────────────────┐
│  PIP-BOY PALETTE                                            │
├─────────────────────────────────────────────────────────────┤
│  Background    #0a0a08    ████  CRT black                  │
│  Scanline      #0f0f0d    ████  Scanline overlay           │
│  Primary       #18ff6d    ████  Pip-Boy green              │
│  Alt Primary   #ffb000    ████  Amber variant              │
│  Dim           #0a5528    ████  Dark green                 │
│  Text          #18ff6d    ████  Green text                 │
│  Highlight     #0a0a08    ████  Inverted (green bg)        │
│  Warning       #ff6600    ████  Orange                     │
└─────────────────────────────────────────────────────────────┘
```

### Visual Language

```
BORDERS: Rounded, technical
╭──────────────────────────────────────────────────────────────╮
│ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ │
│ █ VAULT-TEC PIP-BOY 3000 █████████████████████████████████ │
│ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ │
├──────────────────────────────────────────────────────────────┤
│  ┌─ STAT ─┬─ INV ─┬─ DATA ─┬─ MAP ─┬─ RADIO ─┐              │
│  └────────┴───────┴────────┴───────┴─────────┘              │
│                                                              │
│  HP  ████████████████░░░░░░░░  175/250                      │
│  AP  ██████████░░░░░░░░░░░░░░   85/200                      │
│  XP  ████████████████████░░░░  Level 24                     │
│                                                              │
│  ┌─ SPECIAL ──────────────────────────────────────────────┐ │
│  │ S:6  P:7  E:5  C:4  I:8  A:6  L:5                      │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  [ STATUS ]  [ EFFECTS ]  [ PERKS ]                         │
│                                                              │
│  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ │
╰──────────────────────────────────────────────────────────────╯

CRT SCANLINE EFFECT (Apply with alternating dim lines):
████████████████████████████████████████████████████
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
████████████████████████████████████████████████████
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
```

---

## Nord

> Arctic, calm, muted palette inspired by the Nord color scheme

### Color Palette

```
┌─────────────────────────────────────────────────────────────┐
│  NORD PALETTE                                               │
├─────────────────────────────────────────────────────────────┤
│  Polar Night                                                │
│  nord0         #2e3440    ████  Background                 │
│  nord1         #3b4252    ████  Elevated surface           │
│  nord2         #434c5e    ████  Selection                  │
│  nord3         #4c566a    ████  Comments                   │
│                                                             │
│  Snow Storm                                                 │
│  nord4         #d8dee9    ████  Text                       │
│  nord5         #e5e9f0    ████  Light text                 │
│  nord6         #eceff4    ████  Bright text                │
│                                                             │
│  Frost                                                      │
│  nord7         #8fbcbb    ████  Teal                       │
│  nord8         #88c0d0    ████  Cyan                       │
│  nord9         #81a1c1    ████  Blue                       │
│  nord10        #5e81ac    ████  Dark blue                  │
│                                                             │
│  Aurora                                                     │
│  nord11        #bf616a    ████  Red                        │
│  nord12        #d08770    ████  Orange                     │
│  nord13        #ebcb8b    ████  Yellow                     │
│  nord14        #a3be8c    ████  Green                      │
│  nord15        #b48ead    ████  Purple                     │
└─────────────────────────────────────────────────────────────┘
```

---

## Dracula

> Dark theme with purple accents, popular in dev tools

### Color Palette

```
┌─────────────────────────────────────────────────────────────┐
│  DRACULA PALETTE                                            │
├─────────────────────────────────────────────────────────────┤
│  Background    #282a36    ████                             │
│  Current Line  #44475a    ████                             │
│  Foreground    #f8f8f2    ████                             │
│  Comment       #6272a4    ████                             │
│  Cyan          #8be9fd    ████                             │
│  Green         #50fa7b    ████                             │
│  Orange        #ffb86c    ████                             │
│  Pink          #ff79c6    ████                             │
│  Purple        #bd93f9    ████                             │
│  Red           #ff5555    ████                             │
│  Yellow        #f1fa8c    ████                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Gruvbox

> Retro groove, warm earthy colors

### Color Palette

```
┌─────────────────────────────────────────────────────────────┐
│  GRUVBOX DARK PALETTE                                       │
├─────────────────────────────────────────────────────────────┤
│  bg            #282828    ████                             │
│  bg1           #3c3836    ████                             │
│  bg2           #504945    ████                             │
│  fg            #ebdbb2    ████                             │
│  fg1           #d5c4a1    ████                             │
│  red           #fb4934    ████                             │
│  green         #b8bb26    ████                             │
│  yellow        #fabd2f    ████                             │
│  blue          #83a598    ████                             │
│  purple        #d3869b    ████                             │
│  aqua          #8ec07c    ████                             │
│  orange        #fe8019    ████                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Synthwave

> 80s neon, vaporwave aesthetic, retro-futurism

### Color Palette

```
┌─────────────────────────────────────────────────────────────┐
│  SYNTHWAVE PALETTE                                          │
├─────────────────────────────────────────────────────────────┤
│  Background    #241b2f    ████  Dark purple               │
│  Surface       #2d1f3d    ████  Purple                    │
│  Primary       #ff7edb    ████  Hot pink                  │
│  Secondary     #72f1b8    ████  Mint                      │
│  Accent        #36f9f6    ████  Cyan                      │
│  Text          #f4eeff    ████  Light purple-white        │
│  Yellow        #fede5d    ████  Gold                      │
│  Orange        #ff8b39    ████  Orange                    │
│  Red           #fe4450    ████  Red                       │
└─────────────────────────────────────────────────────────────┘
```

### Visual Language

```
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║  ███████╗██╗   ██╗███╗   ██╗████████╗██╗  ██╗              ║
║  ██╔════╝╚██╗ ██╔╝████╗  ██║╚══██╔══╝██║  ██║              ║
║  ███████╗ ╚████╔╝ ██╔██╗ ██║   ██║   ███████║              ║
║  ╚════██║  ╚██╔╝  ██║╚██╗██║   ██║   ██╔══██║              ║
║  ███████║   ██║   ██║ ╚████║   ██║   ██║  ██║              ║
║  ╚══════╝   ╚═╝   ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝              ║
║                                                            ║
║  ▁▂▃▄▅▆▇█▇▆▅▄▃▂▁▂▃▄▅▆▇█▇▆▅▄▃▂▁▂▃▄▅▆▇█▇▆▅▄▃▂▁              ║
║                                                            ║
║  ┌─────────────────────────────────────────────────────┐   ║
║  │  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │   ║
║  │  ████████████████████████████████████░░░░░░░░░░░░░ │   ║
║  │  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │   ║
║  └─────────────────────────────────────────────────────┘   ║
║                                                            ║
║               [ PLAY ]  [ STOP ]  [ NEXT ]                 ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
```

---

## Quick Style Selector

When implementing, use this guide:

| Need | Recommended Style |
|------|-------------------|
| Enterprise SaaS | Corporate |
| Developer tool | Hacker or Dracula |
| Nostalgic/fun app | Retro DOS or Pip-Boy |
| Monitoring dashboard | Cyberpunk |
| Writing/productivity | Minimal or Nord |
| Music/creative | Synthwave |
| Code editor | Dracula or Gruvbox |
| General purpose | Nord |

---

## Implementation Tips

### Lipgloss Theme System (Go)

```go
type Theme struct {
    Background    lipgloss.Color
    Surface       lipgloss.Color
    Primary       lipgloss.Color
    Secondary     lipgloss.Color
    Accent        lipgloss.Color
    Text          lipgloss.Color
    Muted         lipgloss.Color
    Success       lipgloss.Color
    Warning       lipgloss.Color
    Error         lipgloss.Color
    BorderStyle   lipgloss.Border
}

var Themes = map[string]Theme{
    "corporate": {
        Background:   lipgloss.Color("#1a1a2e"),
        Primary:      lipgloss.Color("#0f4c75"),
        // ...
        BorderStyle:  lipgloss.RoundedBorder(),
    },
    "hacker": {
        Background:   lipgloss.Color("#0a0a0a"),
        Primary:      lipgloss.Color("#00ff00"),
        // ...
        BorderStyle:  lipgloss.NormalBorder(),
    },
}

func ApplyTheme(theme Theme) {
    // Apply to all styles
}
```

### Textual CSS Variables (Python)

```css
/* themes/corporate.tcss */
$background: #1a1a2e;
$surface: #16213e;
$primary: #0f4c75;
$accent: #3282b8;
$text: #e8e8e8;

/* themes/hacker.tcss */
$background: #0a0a0a;
$surface: #111111;
$primary: #00ff00;
$text: #00ff00;
```

### Ink Theme Context (React)

```tsx
const themes = {
  corporate: {
    background: '#1a1a2e',
    primary: '#0f4c75',
    text: '#e8e8e8',
  },
  hacker: {
    background: '#0a0a0a',
    primary: '#00ff00',
    text: '#00ff00',
  },
};

const ThemeContext = React.createContext(themes.corporate);

const ThemedBox = ({ children }) => {
  const theme = useContext(ThemeContext);
  return (
    <Box borderStyle="round" borderColor={theme.primary}>
      <Text color={theme.text}>{children}</Text>
    </Box>
  );
};
```
