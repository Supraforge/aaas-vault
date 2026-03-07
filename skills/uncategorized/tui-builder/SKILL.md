---
name: tui-builder
description: >-
  > Master-level terminal interface design and development across all languages
  and aesthetics.
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---
# TUI Builder - Senior Terminal UI Designer & Developer

> Master-level terminal interface design and development across all languages and aesthetics.

## Role

You are a **Senior TUI Designer & Developer** with expertise in:
- **Visual Design** - Typography, color theory, layout, animation
- **Multiple Aesthetics** - Corporate, Hacker, Retro/DOS, Cyberpunk, Minimal, and more
- **Framework Mastery** - Bubbletea, Ink, Textual, Ratatui
- **UX Excellence** - clig.dev best practices, accessibility, responsive design

When building TUIs, you don't just code—you **design**. Every interface should have intentional visual hierarchy, consistent styling, and a cohesive aesthetic.

## Reference Documents

| Document | Purpose |
|----------|---------|
| `reference/design-system.md` | Typography, color theory, layout patterns, components |
| `reference/style-presets.md` | 10+ style presets (Corporate, Hacker, Cyberpunk, etc.) |
| `reference/cli-ux-guidelines.md` | clig.dev UX best practices |
| `reference/bubbletea.md` | Go framework deep-dive |
| `reference/ink.md` | JavaScript/TypeScript framework |
| `reference/textual.md` | Python framework |
| `reference/ratatui.md` | Rust framework |

## Trigger Keywords

- `tui`, `terminal ui`, `terminal interface`
- `cli app`, `command line application`, `cli tool`
- `bubbletea`, `textual`, `ink`, `ratatui`, `charm`
- `terminal dashboard`, `terminal form`, `terminal menu`
- `progress bar`, `spinner`, `interactive cli`
- `retro`, `hacker style`, `cyberpunk`, `minimal`, `corporate`
- `pip-boy`, `dos style`, `synthwave`, `nord`, `dracula`

## Quick Start

When user wants to build a TUI:

1. **Clarify the aesthetic** - What style/vibe? (See style presets)
2. **Detect project context** - Check for existing language/framework
3. **Recommend framework** - Based on language and use case
4. **Design first** - Sketch the layout, choose colors, plan hierarchy
5. **Scaffold structure** - Generate boilerplate with styling baked in
6. **Implement features** - Build components following framework patterns

## Style Selection

Ask the user early: **"What aesthetic are you going for?"**

| Style | Vibe | Best For |
|-------|------|----------|
| Corporate | Clean, professional, trustworthy | Enterprise tools, B2B |
| Hacker | Matrix-style, green-on-black | Dev tools, security |
| Retro/DOS | 80s computing, CGA colors | Games, novelty |
| Cyberpunk | Neon, glitch, high-tech | Monitoring, dashboards |
| Minimal | Zen, focused, clean | Productivity, writing |
| Pip-Boy | Fallout amber CRT | Games, themed apps |
| Synthwave | 80s neon, vaporwave | Music, creative tools |
| Nord | Arctic, calm, muted | Code editors, everyday |
| Dracula | Dark, purple accents | Dev environments |
| Gruvbox | Warm, earthy, retro | Text-heavy apps |

See `reference/style-presets.md` for full palettes and implementation guides.

---

## Framework Selection Matrix

| If Project Has... | Recommend | Why |
|-------------------|-----------|-----|
| `go.mod` | **Bubbletea** | Best Go TUI, Elm architecture, huge ecosystem |
| `package.json` | **Ink** | React patterns, familiar to JS devs |
| `pyproject.toml` / `requirements.txt` | **Textual** | Modern Python TUI, CSS-like styling |
| `Cargo.toml` | **Ratatui** | Fast, low-level control, Rust safety |
| No existing project | Ask user preference, default to **Ink** for quick prototypes |

### Framework Comparison

```
┌─────────────┬────────────┬─────────────────┬──────────────────┐
│ Framework   │ Language   │ Architecture    │ Best For         │
├─────────────┼────────────┼─────────────────┼──────────────────┤
│ Bubbletea   │ Go         │ Elm MVU         │ Production CLIs  │
│ Ink         │ JS/TS      │ React           │ Quick prototypes │
│ Textual     │ Python     │ Reactive/CSS    │ Dashboards       │
│ Ratatui     │ Rust       │ Immediate mode  │ Performance      │
└─────────────┴────────────┴─────────────────┴──────────────────┘
```

---

## Core Principles (from clig.dev)

### 1. Human-First Design
```
DO: Design for humans interacting directly
DON'T: Assume machine-to-machine only
```

### 2. Show Progress Always
```
< 100ms  → No indicator needed
100ms-1s → Spinner
> 1s     → Progress bar with ETA
```

### 3. Helpful Error Messages
```
BAD:  "Error: ENOENT"
GOOD: "File not found: config.yaml

      To fix this, either:
      • Create the file: touch config.yaml
      • Specify a different path: --config /path/to/file"
```

### 4. Standard Flag Conventions
```
-h, --help      Show help
-v, --verbose   Verbose output
-q, --quiet     Suppress output
-V, --version   Show version
--json          Machine-readable output
--no-color      Disable colors
--dry-run       Preview without executing
--force         Skip confirmations
```

### 5. TTY Awareness
```go
// Detect if running interactively
if isatty.IsTerminal(os.Stdout.Fd()) {
    // Human-friendly output with colors
} else {
    // Machine-friendly JSON/plain text
}
```

### 6. Composability
```bash
# Your TUI should work in pipelines
mytool list --json | jq '.[] | select(.status == "active")'
mytool process < input.txt > output.txt
```

---

## Architecture Patterns

### Pattern 1: Model-View-Update (Elm Architecture)
Used by: **Bubbletea**, **Ratatui**

```
┌──────────────────────────────────────────┐
│                                          │
│  ┌─────────┐    ┌─────────┐    ┌──────┐ │
│  │  Model  │───▶│  View   │───▶│ UI   │ │
│  └─────────┘    └─────────┘    └──────┘ │
│       ▲                            │     │
│       │         ┌─────────┐        │     │
│       └─────────│ Update  │◀───────┘     │
│                 └─────────┘              │
│                 (Messages)               │
└──────────────────────────────────────────┘
```

### Pattern 2: Component Model (React-style)
Used by: **Ink**, **Textual**

```
┌──────────────────────────────────────────┐
│  App                                     │
│  ├── Header                              │
│  ├── MainContent                         │
│  │   ├── Sidebar                         │
│  │   └── ContentArea                     │
│  │       ├── List                        │
│  │       └── Detail                      │
│  └── Footer                              │
└──────────────────────────────────────────┘
```

---

## Common UI Patterns

### 1. Interactive List/Menu
```
┌─ Select an option ────────────────────┐
│                                       │
│   ● Create new project                │
│   ○ Open existing                     │
│   ○ Import from GitHub                │
│   ○ Settings                          │
│   ○ Exit                              │
│                                       │
│   ↑/↓: Navigate  Enter: Select  q: Quit
└───────────────────────────────────────┘
```

### 2. Form Input
```
┌─ New Project ─────────────────────────┐
│                                       │
│  Name: █my-awesome-app                │
│  Template: [Next.js v14      ▼]       │
│  Include tests: [✓]                   │
│  Git init: [✓]                        │
│                                       │
│        [Cancel]  [Create Project]     │
└───────────────────────────────────────┘
```

### 3. Progress Display
```
┌─ Installing dependencies ─────────────┐
│                                       │
│  ████████████████░░░░░░░░  67%        │
│  Installing: @types/react             │
│                                       │
│  Elapsed: 12s  Remaining: ~6s         │
└───────────────────────────────────────┘
```

### 4. Split Pane / Dashboard
```
┌─ System Monitor ──────────────────────────────────┐
│ ┌─ Processes ──────────┐ ┌─ Resources ─────────┐ │
│ │ PID   NAME     CPU   │ │ CPU  ████████░░ 80% │ │
│ │ 1234  node     45%   │ │ MEM  ██████░░░░ 60% │ │
│ │ 5678  chrome   23%   │ │ DISK █████░░░░░ 50% │ │
│ │ 9012  code     12%   │ │ NET  ██░░░░░░░░ 20% │ │
│ └──────────────────────┘ └─────────────────────┘ │
│ ┌─ Logs ───────────────────────────────────────┐ │
│ │ [INFO] Server started on port 3000           │ │
│ │ [WARN] Memory usage above 75%                │ │
│ └──────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────┘
```

### 5. Confirmation Dialog
```
┌─ Confirm ─────────────────────────────┐
│                                       │
│  ⚠️  Delete all files in /tmp?        │
│                                       │
│  This action cannot be undone.        │
│                                       │
│        [Cancel]  [Delete]             │
└───────────────────────────────────────┘
```

---

## Framework Quick References

### Bubbletea (Go)
See: `reference/bubbletea.md`

```go
package main

import (
    "fmt"
    tea "github.com/charmbracelet/bubbletea"
)

type model struct {
    choices  []string
    cursor   int
    selected map[int]struct{}
}

func (m model) Init() tea.Cmd { return nil }

func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
    switch msg := msg.(type) {
    case tea.KeyMsg:
        switch msg.String() {
        case "q": return m, tea.Quit
        case "up": if m.cursor > 0 { m.cursor-- }
        case "down": if m.cursor < len(m.choices)-1 { m.cursor++ }
        case "enter": m.selected[m.cursor] = struct{}{}
        }
    }
    return m, nil
}

func (m model) View() string {
    s := "Select items:\n\n"
    for i, choice := range m.choices {
        cursor := " "
        if m.cursor == i { cursor = ">" }
        checked := " "
        if _, ok := m.selected[i]; ok { checked = "x" }
        s += fmt.Sprintf("%s [%s] %s\n", cursor, checked, choice)
    }
    return s + "\nPress q to quit.\n"
}

func main() {
    m := model{choices: []string{"Option 1", "Option 2", "Option 3"}, selected: make(map[int]struct{})}
    tea.NewProgram(m).Run()
}
```

### Ink (JavaScript/TypeScript)
See: `reference/ink.md`

```tsx
import React, { useState } from 'react';
import { render, Box, Text, useInput } from 'ink';

const App = () => {
  const [selected, setSelected] = useState(0);
  const items = ['Create project', 'Open existing', 'Settings', 'Exit'];

  useInput((input, key) => {
    if (key.upArrow) setSelected(s => Math.max(0, s - 1));
    if (key.downArrow) setSelected(s => Math.min(items.length - 1, s + 1));
    if (input === 'q') process.exit(0);
  });

  return (
    <Box flexDirection="column" padding={1}>
      <Text bold>Select an option:</Text>
      {items.map((item, i) => (
        <Text key={i} color={i === selected ? 'green' : 'white'}>
          {i === selected ? '> ' : '  '}{item}
        </Text>
      ))}
      <Text dimColor>↑/↓: Navigate  q: Quit</Text>
    </Box>
  );
};

render(<App />);
```

### Textual (Python)
See: `reference/textual.md`

```python
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Container

class MyApp(App):
    CSS = """
    Screen {
        layout: vertical;
    }
    #main {
        height: 1fr;
        border: solid green;
    }
    """

    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Static("Welcome to My TUI App!", id="welcome"),
            Button("Get Started", id="start"),
            id="main"
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "start":
            self.notify("Let's go!")

if __name__ == "__main__":
    MyApp().run()
```

### Ratatui (Rust)
See: `reference/ratatui.md`

```rust
use ratatui::{
    backend::CrosstermBackend,
    widgets::{Block, Borders, Paragraph},
    Terminal,
};
use crossterm::{
    event::{self, Event, KeyCode},
    terminal::{disable_raw_mode, enable_raw_mode},
};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    enable_raw_mode()?;
    let mut terminal = Terminal::new(CrosstermBackend::new(std::io::stdout()))?;

    loop {
        terminal.draw(|frame| {
            let block = Block::default()
                .title("My TUI")
                .borders(Borders::ALL);
            let paragraph = Paragraph::new("Press 'q' to quit")
                .block(block);
            frame.render_widget(paragraph, frame.area());
        })?;

        if let Event::Key(key) = event::read()? {
            if key.code == KeyCode::Char('q') { break; }
        }
    }

    disable_raw_mode()?;
    Ok(())
}
```

---

## Project Scaffolding

When starting a new TUI project, create this structure:

### Go (Bubbletea)
```
my-tui/
├── main.go           # Entry point
├── model.go          # App state
├── update.go         # Message handlers
├── view.go           # UI rendering
├── commands.go       # Side effects (API calls, file IO)
├── styles.go         # Lipgloss styles
└── go.mod
```

### JavaScript (Ink)
```
my-tui/
├── src/
│   ├── index.tsx     # Entry point
│   ├── App.tsx       # Main component
│   ├── components/   # UI components
│   │   ├── Menu.tsx
│   │   ├── Form.tsx
│   │   └── Progress.tsx
│   └── hooks/        # Custom hooks
├── package.json
└── tsconfig.json
```

### Python (Textual)
```
my-tui/
├── src/
│   ├── __main__.py   # Entry point
│   ├── app.py        # Main app class
│   ├── screens/      # Different screens
│   │   ├── main.py
│   │   └── settings.py
│   ├── widgets/      # Custom widgets
│   └── styles.tcss   # Textual CSS
├── pyproject.toml
└── tests/
```

### Rust (Ratatui)
```
my-tui/
├── src/
│   ├── main.rs       # Entry point
│   ├── app.rs        # App state
│   ├── ui.rs         # UI rendering
│   ├── event.rs      # Event handling
│   └── widgets/      # Custom widgets
├── Cargo.toml
└── tests/
```

---

## Testing TUI Applications

### Snapshot Testing (Ink)
```tsx
import { render } from 'ink-testing-library';
import App from './App';

test('renders menu correctly', () => {
  const { lastFrame } = render(<App />);
  expect(lastFrame()).toMatchSnapshot();
});
```

### Textual Testing
```python
async def test_app():
    app = MyApp()
    async with app.run_test() as pilot:
        await pilot.click("#start-button")
        assert app.query_one("#status").renderable == "Started"
```

### Bubbletea Testing
```go
func TestModel(t *testing.T) {
    m := initialModel()
    m, _ = m.Update(tea.KeyMsg{Type: tea.KeyDown})
    if m.cursor != 1 {
        t.Errorf("expected cursor 1, got %d", m.cursor)
    }
}
```

---

## Ecosystem Tools

### Charm Suite (Go)
- **Lipgloss** - Styling and layout
- **Bubbles** - Pre-built components (spinners, text inputs, tables)
- **Glamour** - Markdown rendering
- **Wish** - SSH server for TUIs
- **VHS** - Record terminal GIFs

### Ink Ecosystem (JS)
- **ink-select-input** - Selection menus
- **ink-text-input** - Text inputs
- **ink-spinner** - Loading spinners
- **ink-table** - Tables
- **ink-gradient** - Gradient text

### Textual Ecosystem (Python)
- Built-in widgets: DataTable, Tree, Markdown, RichLog
- CSS-like styling with `.tcss` files
- DevTools for debugging

---

## Accessibility Considerations

1. **Screen reader support** - Provide text alternatives
2. **Color contrast** - Don't rely solely on color
3. **Keyboard navigation** - Everything must be keyboard-accessible
4. **Reduce motion** - Respect `REDUCE_MOTION` preference
5. **Clear focus indicators** - Show which element is selected

---

## Performance Tips

1. **Debounce rapid updates** - Don't redraw on every keystroke
2. **Virtual scrolling** - For long lists, only render visible items
3. **Lazy loading** - Load data as needed
4. **Efficient diffing** - Only update changed parts of the screen
5. **Background workers** - Don't block the UI thread

---

## Deployment

### Single Binary (Recommended)
```bash
# Go
go build -o mytui .

# Rust
cargo build --release

# Node (with pkg)
npx pkg . -o mytui

# Python (with PyInstaller)
pyinstaller --onefile src/__main__.py
```

### Distribution
- GitHub Releases with binaries for each platform
- Homebrew tap for macOS
- AUR package for Arch Linux
- npm publish for Node.js tools
- PyPI for Python tools
- crates.io for Rust tools

---

## Resources

- [Command Line Interface Guidelines](https://clig.dev/) - The bible of CLI UX
- [Charm](https://charm.sh/) - Go TUI ecosystem
- [Textual Docs](https://textual.textualize.io/) - Python TUI framework
- [Ink Docs](https://github.com/vadimdemedes/ink) - React for CLIs
- [Ratatui](https://ratatui.rs/) - Rust TUI library
- [Terminal Trove](https://terminaltrove.com/) - TUI inspiration gallery
