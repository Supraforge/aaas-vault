# Textual Reference (Python)

> Modern Python framework for TUI applications

## Installation

```bash
pip install textual
# or with dev tools
pip install "textual[dev]"
```

## Core Concepts

### Basic App Structure

```python
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Container

class MyApp(App):
    """A simple Textual app."""

    # CSS styling
    CSS = """
    Screen {
        layout: vertical;
    }

    #welcome {
        text-align: center;
        padding: 2;
    }
    """

    # Key bindings
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("d", "toggle_dark", "Toggle dark mode"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets."""
        yield Header()
        yield Container(
            Static("Welcome to Textual!", id="welcome"),
            Button("Click me!", id="btn"),
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press."""
        if event.button.id == "btn":
            self.notify("Button clicked!")

    def action_toggle_dark(self) -> None:
        """Toggle dark mode."""
        self.dark = not self.dark

if __name__ == "__main__":
    app = MyApp()
    app.run()
```

## Widgets

### Built-in Widgets

```python
from textual.widgets import (
    Button,          # Clickable button
    Checkbox,        # Toggle checkbox
    DataTable,       # Spreadsheet-like table
    DirectoryTree,   # File browser
    Footer,          # Key binding hints
    Header,          # App title bar
    Input,           # Text input
    Label,           # Text label
    ListItem,        # List item
    ListView,        # Scrollable list
    LoadingIndicator,# Spinner
    Log,             # Scrolling log
    Markdown,        # Rendered markdown
    MarkdownViewer,  # Markdown with navigation
    OptionList,      # Selectable options
    Placeholder,     # Development placeholder
    Pretty,          # Pretty-printed data
    ProgressBar,     # Progress indicator
    RadioButton,     # Radio selection
    RadioSet,        # Group of radio buttons
    RichLog,         # Rich text log
    Rule,            # Horizontal line
    Select,          # Dropdown select
    SelectionList,   # Multi-select list
    Sparkline,       # Mini chart
    Static,          # Static text/content
    Switch,          # On/off toggle
    TabbedContent,   # Tab container
    TabPane,         # Tab panel
    Tabs,            # Tab bar
    TextArea,        # Multi-line text
    Tree,            # Tree view
)
```

### Input Widget

```python
from textual.widgets import Input

class MyApp(App):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Enter your name...")
        yield Input(password=True, placeholder="Password")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        value = event.value
        self.notify(f"You entered: {value}")
```

### DataTable

```python
from textual.widgets import DataTable

class MyApp(App):
    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("Name", "Age", "City")
        table.add_rows([
            ("Alice", 30, "NYC"),
            ("Bob", 25, "LA"),
            ("Charlie", 35, "Chicago"),
        ])

    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        self.notify(f"Selected row: {event.row_key}")
```

### ListView

```python
from textual.widgets import ListView, ListItem, Label

class MyApp(App):
    def compose(self) -> ComposeResult:
        yield ListView(
            ListItem(Label("Option 1"), id="opt1"),
            ListItem(Label("Option 2"), id="opt2"),
            ListItem(Label("Option 3"), id="opt3"),
        )

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        self.notify(f"Selected: {event.item.id}")
```

### TabbedContent

```python
from textual.widgets import TabbedContent, TabPane, Static

class MyApp(App):
    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("Home", id="home"):
                yield Static("Welcome home!")
            with TabPane("Settings", id="settings"):
                yield Static("Settings go here")
            with TabPane("About", id="about"):
                yield Static("About this app")
```

### Tree

```python
from textual.widgets import Tree

class MyApp(App):
    def compose(self) -> ComposeResult:
        tree = Tree("Root")
        tree.root.expand()

        branch1 = tree.root.add("Branch 1")
        branch1.add_leaf("Leaf 1.1")
        branch1.add_leaf("Leaf 1.2")

        branch2 = tree.root.add("Branch 2")
        branch2.add_leaf("Leaf 2.1")

        yield tree
```

## Containers & Layout

### Container Types

```python
from textual.containers import (
    Container,       # Basic container
    Horizontal,      # Horizontal layout
    Vertical,        # Vertical layout
    Grid,            # CSS Grid layout
    ScrollableContainer,  # Scrollable area
    Center,          # Center content
    Middle,          # Vertically center
    VerticalScroll,  # Vertical scrollable
    HorizontalScroll,# Horizontal scrollable
)
```

### Layout Examples

```python
from textual.containers import Horizontal, Vertical, Grid

class MyApp(App):
    CSS = """
    Horizontal {
        height: auto;
    }

    .box {
        width: 1fr;
        height: 5;
        border: solid green;
    }

    Grid {
        grid-size: 3 2;
        grid-gutter: 1;
    }
    """

    def compose(self) -> ComposeResult:
        # Horizontal layout
        with Horizontal():
            yield Static("Left", classes="box")
            yield Static("Middle", classes="box")
            yield Static("Right", classes="box")

        # Grid layout
        with Grid():
            for i in range(6):
                yield Static(f"Cell {i}", classes="box")
```

## CSS Styling

### Textual CSS (TCSS)

```css
/* styles.tcss */

/* Target by type */
Button {
    background: $primary;
    color: $text;
    border: tall $accent;
}

/* Target by ID */
#main-content {
    width: 100%;
    height: 1fr;
}

/* Target by class */
.highlighted {
    background: $warning;
    text-style: bold;
}

/* Pseudo-classes */
Button:hover {
    background: $primary-lighten-1;
}

Button:focus {
    border: heavy $accent;
}

/* Nested rules */
#sidebar {
    width: 30;

    Button {
        width: 100%;
        margin: 1;
    }
}
```

### Common CSS Properties

```css
/* Dimensions */
width: 50;           /* Cells */
width: 50%;          /* Percentage */
width: 1fr;          /* Fraction */
width: auto;         /* Content-based */
min-width: 20;
max-width: 100;

/* Spacing */
margin: 1 2;         /* Vertical, Horizontal */
padding: 1 2 3 4;    /* Top, Right, Bottom, Left */

/* Colors */
background: $primary;
background: #ff6600;
background: rgb(255, 100, 0);
color: $text;

/* Borders */
border: solid green;
border: double red;
border: round $accent;
border-title-align: center;

/* Text */
text-align: center;
text-style: bold italic underline;

/* Layout */
layout: horizontal;
layout: vertical;
layout: grid;
align: center middle;
content-align: center middle;
```

### Loading External CSS

```python
class MyApp(App):
    CSS_PATH = "styles.tcss"  # Load from file

    # Or inline CSS
    CSS = """
    Screen {
        background: $surface;
    }
    """
```

## Reactive Attributes

```python
from textual.reactive import reactive

class Counter(Static):
    """A counter widget."""

    count: reactive[int] = reactive(0)

    def render(self) -> str:
        return f"Count: {self.count}"

    def watch_count(self, count: int) -> None:
        """Called when count changes."""
        if count >= 10:
            self.add_class("high")
        else:
            self.remove_class("high")

    def increment(self) -> None:
        self.count += 1
```

## Messages & Events

### Custom Messages

```python
from textual.message import Message

class Counter(Static):
    class LimitReached(Message):
        """Message sent when limit is reached."""
        def __init__(self, count: int) -> None:
            self.count = count
            super().__init__()

    def increment(self) -> None:
        self.count += 1
        if self.count >= 10:
            self.post_message(self.LimitReached(self.count))

class MyApp(App):
    def on_counter_limit_reached(self, message: Counter.LimitReached) -> None:
        self.notify(f"Limit reached at {message.count}!")
```

### Event Handlers

```python
class MyApp(App):
    # Named handler (preferred)
    def on_button_pressed(self, event: Button.Pressed) -> None:
        pass

    # Handler for specific button
    def on_button_pressed_submit_btn(self, event: Button.Pressed) -> None:
        """Handle #submit-btn specifically."""
        pass

    # Mount event (widget added to DOM)
    def on_mount(self) -> None:
        pass

    # Key press
    def on_key(self, event: events.Key) -> None:
        if event.key == "escape":
            self.exit()
```

## Workers (Background Tasks)

```python
from textual import work
from textual.worker import Worker

class MyApp(App):
    @work(exclusive=True)
    async def fetch_data(self, url: str) -> None:
        """Background task to fetch data."""
        self.query_one("#status").update("Loading...")

        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            data = response.json()

        self.query_one("#result").update(str(data))
        self.query_one("#status").update("Done!")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "fetch":
            self.fetch_data("https://api.example.com/data")

    # Handle worker events
    def on_worker_state_changed(self, event: Worker.StateChanged) -> None:
        if event.state == WorkerState.SUCCESS:
            self.notify("Task completed!")
```

## Screens

### Multiple Screens

```python
from textual.screen import Screen

class HomeScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Static("Home Screen")
        yield Button("Go to Settings", id="to-settings")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "to-settings":
            self.app.push_screen("settings")

class SettingsScreen(Screen):
    BINDINGS = [("escape", "pop_screen", "Back")]

    def compose(self) -> ComposeResult:
        yield Static("Settings Screen")
        yield Button("Back", id="back")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back":
            self.app.pop_screen()

class MyApp(App):
    SCREENS = {
        "home": HomeScreen,
        "settings": SettingsScreen,
    }

    def on_mount(self) -> None:
        self.push_screen("home")
```

### Modal Screens

```python
from textual.screen import ModalScreen

class ConfirmDialog(ModalScreen[bool]):
    """A modal dialog that returns True/False."""

    def compose(self) -> ComposeResult:
        yield Container(
            Static("Are you sure?"),
            Horizontal(
                Button("Yes", id="yes", variant="primary"),
                Button("No", id="no"),
            ),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss(event.button.id == "yes")

class MyApp(App):
    def action_delete(self) -> None:
        async def handle_confirm(confirmed: bool) -> None:
            if confirmed:
                self.notify("Deleted!")

        self.push_screen(ConfirmDialog(), handle_confirm)
```

## Notifications & Logging

```python
class MyApp(App):
    def some_action(self) -> None:
        # Toast notification
        self.notify("Action completed!")

        # With severity
        self.notify("Warning!", severity="warning")
        self.notify("Error occurred!", severity="error")

        # With title and timeout
        self.notify(
            "This is the message",
            title="Notice",
            timeout=5.0,
        )

    def compose(self) -> ComposeResult:
        # RichLog for app logs
        yield RichLog(id="log")

    def log_message(self, msg: str) -> None:
        log = self.query_one("#log", RichLog)
        log.write(msg)
```

## Testing

```python
from textual.testing import AppTest

async def test_button_press():
    async with AppTest(MyApp()) as pilot:
        # Click a button
        await pilot.click("#my-button")

        # Check result
        assert pilot.app.query_one("#result").renderable == "Clicked!"

async def test_input():
    async with AppTest(MyApp()) as pilot:
        # Type in input
        await pilot.type("Hello, World!")
        await pilot.press("enter")

        # Check state
        assert pilot.app.name == "Hello, World!"

async def test_key_bindings():
    async with AppTest(MyApp()) as pilot:
        await pilot.press("q")
        assert pilot.app.is_headless  # App should quit
```

## Dev Tools

```bash
# Run with dev console
textual run --dev my_app.py

# CSS hot reloading
textual run --dev my_app.py

# Take screenshot
textual run my_app.py --screenshot screenshot.svg

# Profile performance
textual run --profile my_app.py
```

## Resources

- [Textual Docs](https://textual.textualize.io/)
- [Textual GitHub](https://github.com/Textualize/textual)
- [Widget Gallery](https://textual.textualize.io/widget_gallery/)
- [CSS Reference](https://textual.textualize.io/css_types/)
