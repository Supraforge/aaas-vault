#!/usr/bin/env python3
"""
Textual TUI Starter Template

Features:
- Multi-screen navigation
- Data table display
- Form input
- Progress indicators
- Modal dialogs

Usage:
    python src/app.py
"""

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.screen import Screen, ModalScreen
from textual.widgets import (
    Header,
    Footer,
    Static,
    Button,
    Input,
    Label,
    DataTable,
    ProgressBar,
    LoadingIndicator,
)
from textual.binding import Binding
from textual import work
import asyncio


# ============================================
# Styles
# ============================================

CSS = """
Screen {
    background: $surface;
}

#main-menu {
    layout: vertical;
    padding: 2;
    width: 100%;
    height: auto;
}

.menu-button {
    width: 100%;
    margin: 1 0;
}

#form-container {
    layout: vertical;
    padding: 2;
    border: solid $primary;
    width: 60;
    height: auto;
    margin: 2 auto;
}

.form-field {
    margin: 1 0;
}

.form-label {
    margin-bottom: 1;
}

#progress-container {
    layout: vertical;
    padding: 2;
    width: 60;
    height: auto;
    margin: 2 auto;
    align: center middle;
}

#result-container {
    layout: vertical;
    padding: 2;
    border: solid $success;
    width: 60;
    height: auto;
    margin: 2 auto;
}

.success-text {
    color: $success;
    text-style: bold;
}

ConfirmDialog {
    align: center middle;
}

#dialog-container {
    width: 50;
    height: auto;
    border: solid $primary;
    background: $surface;
    padding: 2;
}

#dialog-buttons {
    margin-top: 2;
    align: center middle;
}

#dialog-buttons Button {
    margin: 0 1;
}
"""


# ============================================
# Screens
# ============================================

class MenuScreen(Screen):
    """Main menu screen."""

    BINDINGS = [
        Binding("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Static("What would you like to do?", classes="form-label"),
            Button("Start New Task", id="btn-new", classes="menu-button"),
            Button("View Data", id="btn-data", classes="menu-button"),
            Button("Settings", id="btn-settings", classes="menu-button"),
            Button("Exit", id="btn-exit", classes="menu-button", variant="error"),
            id="main-menu",
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-new":
            self.app.push_screen("form")
        elif event.button.id == "btn-data":
            self.app.push_screen("data")
        elif event.button.id == "btn-exit":
            self.app.push_screen(ConfirmDialog("Are you sure you want to exit?"), self.handle_exit)

    def handle_exit(self, confirmed: bool) -> None:
        if confirmed:
            self.app.exit()


class FormScreen(Screen):
    """Form input screen."""

    BINDINGS = [
        Binding("escape", "go_back", "Back"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Static("Enter your details:", classes="form-label"),
            Container(
                Label("Name:"),
                Input(placeholder="John Doe", id="input-name"),
                classes="form-field",
            ),
            Container(
                Label("Email:"),
                Input(placeholder="john@example.com", id="input-email"),
                classes="form-field",
            ),
            Horizontal(
                Button("Cancel", id="btn-cancel"),
                Button("Submit", id="btn-submit", variant="primary"),
            ),
            id="form-container",
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-cancel":
            self.app.pop_screen()
        elif event.button.id == "btn-submit":
            name = self.query_one("#input-name", Input).value
            email = self.query_one("#input-email", Input).value
            if name and email:
                self.app.form_data = {"name": name, "email": email}
                self.app.push_screen("progress")
            else:
                self.notify("Please fill in all fields", severity="warning")

    def action_go_back(self) -> None:
        self.app.pop_screen()


class ProgressScreen(Screen):
    """Progress/loading screen."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            LoadingIndicator(),
            Static("Processing...", id="progress-status"),
            ProgressBar(id="progress-bar", total=100),
            id="progress-container",
        )
        yield Footer()

    def on_mount(self) -> None:
        self.run_task()

    @work(exclusive=True)
    async def run_task(self) -> None:
        """Simulate a long-running task."""
        progress_bar = self.query_one("#progress-bar", ProgressBar)
        status = self.query_one("#progress-status", Static)

        steps = [
            (20, "Connecting..."),
            (40, "Fetching data..."),
            (60, "Processing..."),
            (80, "Validating..."),
            (100, "Complete!"),
        ]

        for progress, text in steps:
            await asyncio.sleep(0.5)
            progress_bar.update(progress=progress)
            status.update(text)

        await asyncio.sleep(0.5)
        self.app.switch_screen("result")


class DataScreen(Screen):
    """Data table screen."""

    BINDINGS = [
        Binding("escape", "go_back", "Back"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield DataTable(id="data-table")
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one("#data-table", DataTable)
        table.add_columns("ID", "Name", "Status", "Created")
        table.add_rows([
            ("1", "Project Alpha", "Active", "2024-01-15"),
            ("2", "Project Beta", "Pending", "2024-01-10"),
            ("3", "Project Gamma", "Complete", "2024-01-05"),
            ("4", "Project Delta", "Active", "2024-01-01"),
        ])

    def action_go_back(self) -> None:
        self.app.pop_screen()


class ResultScreen(Screen):
    """Result/success screen."""

    BINDINGS = [
        Binding("b", "go_back", "Back to Menu"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Static("✓ Task Complete!", classes="success-text"),
            Static(id="result-name"),
            Static(id="result-email"),
            Button("Back to Menu", id="btn-back"),
            id="result-container",
        )
        yield Footer()

    def on_mount(self) -> None:
        data = getattr(self.app, "form_data", {})
        self.query_one("#result-name", Static).update(f"Name: {data.get('name', 'N/A')}")
        self.query_one("#result-email", Static).update(f"Email: {data.get('email', 'N/A')}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-back":
            self.app.switch_screen("menu")

    def action_go_back(self) -> None:
        self.app.switch_screen("menu")


class ConfirmDialog(ModalScreen[bool]):
    """A modal confirmation dialog."""

    def __init__(self, message: str) -> None:
        super().__init__()
        self.message = message

    def compose(self) -> ComposeResult:
        yield Container(
            Static(self.message),
            Horizontal(
                Button("Cancel", id="btn-cancel"),
                Button("Confirm", id="btn-confirm", variant="primary"),
                id="dialog-buttons",
            ),
            id="dialog-container",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss(event.button.id == "btn-confirm")


# ============================================
# Main App
# ============================================

class MyApp(App):
    """Main application."""

    CSS = CSS
    TITLE = "My TUI App"

    SCREENS = {
        "menu": MenuScreen,
        "form": FormScreen,
        "progress": ProgressScreen,
        "data": DataScreen,
        "result": ResultScreen,
    }

    BINDINGS = [
        Binding("ctrl+c", "quit", "Quit", show=False),
        Binding("d", "toggle_dark", "Toggle Dark Mode"),
    ]

    def __init__(self) -> None:
        super().__init__()
        self.form_data: dict = {}

    def on_mount(self) -> None:
        self.push_screen("menu")

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark


# ============================================
# Entry Point
# ============================================

if __name__ == "__main__":
    app = MyApp()
    app.run()
