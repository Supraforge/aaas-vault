# Ratatui Reference (Rust)

> Build rich terminal UIs in Rust

## Installation

```bash
cargo add ratatui crossterm
```

Or in `Cargo.toml`:
```toml
[dependencies]
ratatui = "0.28"
crossterm = "0.28"
```

## Core Concepts

### Basic App Structure

```rust
use std::io;
use crossterm::{
    event::{self, Event, KeyCode, KeyEventKind},
    terminal::{disable_raw_mode, enable_raw_mode, EnterAlternateScreen, LeaveAlternateScreen},
    ExecutableCommand,
};
use ratatui::{
    prelude::*,
    widgets::{Block, Borders, Paragraph},
};

fn main() -> io::Result<()> {
    // Setup terminal
    enable_raw_mode()?;
    io::stdout().execute(EnterAlternateScreen)?;
    let mut terminal = Terminal::new(CrosstermBackend::new(io::stdout()))?;

    // Run app
    let result = run(&mut terminal);

    // Cleanup
    disable_raw_mode()?;
    io::stdout().execute(LeaveAlternateScreen)?;

    result
}

fn run(terminal: &mut Terminal<impl Backend>) -> io::Result<()> {
    loop {
        // Draw UI
        terminal.draw(|frame| {
            let area = frame.area();
            frame.render_widget(
                Paragraph::new("Hello, Ratatui! Press 'q' to quit.")
                    .block(Block::default().title("My App").borders(Borders::ALL)),
                area,
            );
        })?;

        // Handle input
        if let Event::Key(key) = event::read()? {
            if key.kind == KeyEventKind::Press && key.code == KeyCode::Char('q') {
                break;
            }
        }
    }
    Ok(())
}
```

## Widgets

### Paragraph (Text)

```rust
use ratatui::widgets::{Paragraph, Block, Borders, Wrap};
use ratatui::text::{Line, Span};
use ratatui::style::{Style, Color, Modifier};

// Simple text
let para = Paragraph::new("Hello, World!");

// With styling
let para = Paragraph::new("Styled text")
    .style(Style::default().fg(Color::Yellow).add_modifier(Modifier::BOLD))
    .block(Block::default().title("Title").borders(Borders::ALL))
    .wrap(Wrap { trim: true })
    .alignment(Alignment::Center);

// Rich text with spans
let text = vec![
    Line::from(vec![
        Span::raw("Hello, "),
        Span::styled("World", Style::default().fg(Color::Green).add_modifier(Modifier::BOLD)),
        Span::raw("!"),
    ]),
    Line::from("Second line"),
];
let para = Paragraph::new(text);
```

### List

```rust
use ratatui::widgets::{List, ListItem, ListState, Block, Borders};

struct App {
    items: Vec<String>,
    state: ListState,
}

impl App {
    fn new() -> Self {
        let mut state = ListState::default();
        state.select(Some(0));
        Self {
            items: vec!["Item 1".into(), "Item 2".into(), "Item 3".into()],
            state,
        }
    }

    fn next(&mut self) {
        let i = match self.state.selected() {
            Some(i) => (i + 1) % self.items.len(),
            None => 0,
        };
        self.state.select(Some(i));
    }

    fn previous(&mut self) {
        let i = match self.state.selected() {
            Some(i) => (i + self.items.len() - 1) % self.items.len(),
            None => 0,
        };
        self.state.select(Some(i));
    }
}

// Render
fn render(frame: &mut Frame, app: &mut App) {
    let items: Vec<ListItem> = app.items
        .iter()
        .map(|i| ListItem::new(i.as_str()))
        .collect();

    let list = List::new(items)
        .block(Block::default().title("Items").borders(Borders::ALL))
        .highlight_style(Style::default().add_modifier(Modifier::REVERSED))
        .highlight_symbol("> ");

    frame.render_stateful_widget(list, frame.area(), &mut app.state);
}
```

### Table

```rust
use ratatui::widgets::{Table, Row, Cell, Block, Borders, TableState};

let rows = vec![
    Row::new(vec!["Alice", "30", "Developer"]),
    Row::new(vec!["Bob", "25", "Designer"]),
    Row::new(vec!["Charlie", "35", "Manager"]),
];

let widths = [
    Constraint::Length(15),
    Constraint::Length(5),
    Constraint::Fill(1),
];

let table = Table::new(rows, widths)
    .header(Row::new(vec!["Name", "Age", "Role"]).style(Style::default().add_modifier(Modifier::BOLD)))
    .block(Block::default().title("Employees").borders(Borders::ALL))
    .highlight_style(Style::default().add_modifier(Modifier::REVERSED))
    .highlight_symbol("> ");

// Stateful rendering
let mut state = TableState::default();
state.select(Some(0));
frame.render_stateful_widget(table, area, &mut state);
```

### Gauge (Progress)

```rust
use ratatui::widgets::{Gauge, Block, Borders};

let gauge = Gauge::default()
    .block(Block::default().title("Progress").borders(Borders::ALL))
    .gauge_style(Style::default().fg(Color::Green))
    .percent(67)
    .label("67/100");

// Line gauge (simpler)
let line_gauge = LineGauge::default()
    .block(Block::default().title("Download"))
    .gauge_style(Style::default().fg(Color::Blue))
    .ratio(0.67);
```

### Sparkline

```rust
use ratatui::widgets::Sparkline;

let data = vec![0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0];
let sparkline = Sparkline::default()
    .block(Block::default().title("Activity"))
    .data(&data)
    .style(Style::default().fg(Color::Yellow));
```

### Tabs

```rust
use ratatui::widgets::Tabs;

let titles = vec!["Tab1", "Tab2", "Tab3"];
let tabs = Tabs::new(titles)
    .block(Block::default().title("Navigation").borders(Borders::ALL))
    .select(1) // Select second tab
    .style(Style::default().fg(Color::White))
    .highlight_style(Style::default().fg(Color::Yellow).add_modifier(Modifier::BOLD))
    .divider("|");
```

### Block (Container)

```rust
use ratatui::widgets::{Block, Borders, BorderType};

let block = Block::default()
    .title("Title")
    .title_alignment(Alignment::Center)
    .borders(Borders::ALL)
    .border_type(BorderType::Rounded)
    .border_style(Style::default().fg(Color::Cyan));
```

### Chart

```rust
use ratatui::widgets::{Chart, Dataset, Axis, GraphType};
use ratatui::symbols::Marker;

let datasets = vec![
    Dataset::default()
        .name("data1")
        .marker(Marker::Braille)
        .graph_type(GraphType::Line)
        .style(Style::default().fg(Color::Cyan))
        .data(&[(0.0, 0.0), (1.0, 1.0), (2.0, 3.0), (3.0, 2.0)]),
];

let chart = Chart::new(datasets)
    .block(Block::default().title("Chart").borders(Borders::ALL))
    .x_axis(Axis::default()
        .title("X")
        .bounds([0.0, 4.0])
        .labels(vec!["0", "2", "4"]))
    .y_axis(Axis::default()
        .title("Y")
        .bounds([0.0, 4.0])
        .labels(vec!["0", "2", "4"]));
```

## Layout

### Constraints

```rust
use ratatui::layout::{Layout, Constraint, Direction};

let chunks = Layout::default()
    .direction(Direction::Vertical)
    .margin(1)
    .constraints([
        Constraint::Length(3),    // Fixed height
        Constraint::Min(5),       // Minimum height
        Constraint::Percentage(50), // 50% of remaining
        Constraint::Fill(1),      // Fill remaining space
    ])
    .split(frame.area());

// Horizontal layout
let horizontal = Layout::default()
    .direction(Direction::Horizontal)
    .constraints([
        Constraint::Percentage(30),
        Constraint::Percentage(70),
    ])
    .split(area);
```

### Nested Layouts

```rust
fn render(frame: &mut Frame) {
    // Main vertical split
    let main_chunks = Layout::default()
        .direction(Direction::Vertical)
        .constraints([
            Constraint::Length(3),  // Header
            Constraint::Min(0),     // Body
            Constraint::Length(1),  // Footer
        ])
        .split(frame.area());

    // Body horizontal split
    let body_chunks = Layout::default()
        .direction(Direction::Horizontal)
        .constraints([
            Constraint::Percentage(30),  // Sidebar
            Constraint::Percentage(70),  // Content
        ])
        .split(main_chunks[1]);

    // Render widgets
    frame.render_widget(header(), main_chunks[0]);
    frame.render_widget(sidebar(), body_chunks[0]);
    frame.render_widget(content(), body_chunks[1]);
    frame.render_widget(footer(), main_chunks[2]);
}
```

## Styling

### Colors

```rust
use ratatui::style::{Color, Style};

// Named colors
Color::Black
Color::Red
Color::Green
Color::Yellow
Color::Blue
Color::Magenta
Color::Cyan
Color::Gray
Color::DarkGray
Color::LightRed
Color::White
Color::Reset

// RGB
Color::Rgb(255, 100, 0)

// 256-color palette
Color::Indexed(208)
```

### Modifiers

```rust
use ratatui::style::Modifier;

Style::default()
    .fg(Color::Yellow)
    .bg(Color::Black)
    .add_modifier(Modifier::BOLD)
    .add_modifier(Modifier::ITALIC)
    .add_modifier(Modifier::UNDERLINED)
    .add_modifier(Modifier::REVERSED)
    .add_modifier(Modifier::DIM)
    .add_modifier(Modifier::CROSSED_OUT);
```

## Event Handling

### Crossterm Events

```rust
use crossterm::event::{self, Event, KeyCode, KeyModifiers, KeyEventKind};
use std::time::Duration;

fn handle_events(app: &mut App) -> io::Result<()> {
    // Poll with timeout (non-blocking)
    if event::poll(Duration::from_millis(100))? {
        match event::read()? {
            Event::Key(key) => {
                if key.kind == KeyEventKind::Press {
                    match key.code {
                        KeyCode::Char('q') => app.quit = true,
                        KeyCode::Char('c') if key.modifiers.contains(KeyModifiers::CONTROL) => {
                            app.quit = true;
                        }
                        KeyCode::Up | KeyCode::Char('k') => app.previous(),
                        KeyCode::Down | KeyCode::Char('j') => app.next(),
                        KeyCode::Enter => app.select(),
                        KeyCode::Esc => app.back(),
                        _ => {}
                    }
                }
            }
            Event::Resize(width, height) => {
                app.width = width;
                app.height = height;
            }
            Event::Mouse(mouse) => {
                // Handle mouse events if enabled
            }
            _ => {}
        }
    }
    Ok(())
}
```

### Enable Mouse Support

```rust
use crossterm::event::{EnableMouseCapture, DisableMouseCapture};

// In setup
io::stdout().execute(EnableMouseCapture)?;

// In cleanup
io::stdout().execute(DisableMouseCapture)?;
```

## App Architecture

### Recommended Structure

```rust
// app.rs
pub struct App {
    pub running: bool,
    pub items: Vec<String>,
    pub selected: usize,
    pub mode: Mode,
}

pub enum Mode {
    Normal,
    Editing,
    Selecting,
}

impl App {
    pub fn new() -> Self {
        Self {
            running: true,
            items: vec!["Item 1".into(), "Item 2".into()],
            selected: 0,
            mode: Mode::Normal,
        }
    }

    pub fn tick(&mut self) {
        // Update state on each tick
    }

    pub fn quit(&mut self) {
        self.running = false;
    }
}

// ui.rs
pub fn render(frame: &mut Frame, app: &App) {
    match app.mode {
        Mode::Normal => render_normal(frame, app),
        Mode::Editing => render_editing(frame, app),
        Mode::Selecting => render_selecting(frame, app),
    }
}

// event.rs
pub fn handle_event(app: &mut App, event: Event) {
    match app.mode {
        Mode::Normal => handle_normal(app, event),
        Mode::Editing => handle_editing(app, event),
        Mode::Selecting => handle_selecting(app, event),
    }
}

// main.rs
fn main() -> io::Result<()> {
    let mut terminal = setup_terminal()?;
    let mut app = App::new();

    while app.running {
        terminal.draw(|frame| ui::render(frame, &app))?;

        if event::poll(Duration::from_millis(16))? {
            event::handle_event(&mut app, event::read()?);
        }

        app.tick();
    }

    restore_terminal()?;
    Ok(())
}
```

## Async with Tokio

```rust
use tokio::sync::mpsc;

enum Message {
    Tick,
    Key(KeyEvent),
    DataLoaded(Vec<String>),
}

#[tokio::main]
async fn main() -> io::Result<()> {
    let (tx, mut rx) = mpsc::unbounded_channel();

    // Spawn tick task
    let tx_tick = tx.clone();
    tokio::spawn(async move {
        loop {
            tx_tick.send(Message::Tick).unwrap();
            tokio::time::sleep(Duration::from_millis(100)).await;
        }
    });

    // Spawn input task
    let tx_input = tx.clone();
    tokio::spawn(async move {
        loop {
            if let Event::Key(key) = event::read().unwrap() {
                tx_input.send(Message::Key(key)).unwrap();
            }
        }
    });

    // Main loop
    let mut app = App::new();
    while app.running {
        terminal.draw(|f| ui::render(f, &app))?;

        match rx.recv().await {
            Some(Message::Tick) => app.tick(),
            Some(Message::Key(key)) => handle_key(&mut app, key),
            Some(Message::DataLoaded(data)) => app.data = data,
            None => break,
        }
    }

    Ok(())
}
```

## Testing

```rust
#[cfg(test)]
mod tests {
    use super::*;
    use ratatui::backend::TestBackend;

    #[test]
    fn test_app_navigation() {
        let mut app = App::new();
        assert_eq!(app.selected, 0);

        app.next();
        assert_eq!(app.selected, 1);

        app.previous();
        assert_eq!(app.selected, 0);
    }

    #[test]
    fn test_render() {
        let backend = TestBackend::new(80, 24);
        let mut terminal = Terminal::new(backend).unwrap();
        let app = App::new();

        terminal.draw(|frame| render(frame, &app)).unwrap();

        let buffer = terminal.backend().buffer();
        // Assert buffer contents
        assert!(buffer.get(0, 0).symbol() == "┌");
    }
}
```

## Templates

### Quick Start Template

```bash
cargo generate ratatui/templates simple
```

## Resources

- [Ratatui Docs](https://ratatui.rs/)
- [Ratatui GitHub](https://github.com/ratatui/ratatui)
- [Examples](https://github.com/ratatui/ratatui/tree/main/examples)
- [Templates](https://github.com/ratatui/templates)
- [Awesome Ratatui](https://github.com/ratatui/awesome-ratatui)
