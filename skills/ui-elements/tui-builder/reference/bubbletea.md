# Bubbletea Reference (Go)

> The Elm Architecture for terminal UIs

## Installation

```bash
go get github.com/charmbracelet/bubbletea
go get github.com/charmbracelet/lipgloss   # Styling
go get github.com/charmbracelet/bubbles    # Pre-built components
```

## Core Concepts

### The Elm Architecture (MVU)

```
Model  → The application state
Update → Handle messages, return new state
View   → Render state to string
```

### Basic Structure

```go
package main

import (
    "fmt"
    "os"
    tea "github.com/charmbracelet/bubbletea"
)

// MODEL - Application state
type model struct {
    cursor   int
    choices  []string
    selected map[int]struct{}
    quitting bool
}

func initialModel() model {
    return model{
        choices:  []string{"Buy milk", "Wash dishes", "Learn Bubbletea"},
        selected: make(map[int]struct{}),
    }
}

// INIT - Initial command (side effect)
func (m model) Init() tea.Cmd {
    return nil // No initial command
}

// UPDATE - Handle messages
func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
    switch msg := msg.(type) {
    case tea.KeyMsg:
        switch msg.String() {
        case "ctrl+c", "q":
            m.quitting = true
            return m, tea.Quit
        case "up", "k":
            if m.cursor > 0 {
                m.cursor--
            }
        case "down", "j":
            if m.cursor < len(m.choices)-1 {
                m.cursor++
            }
        case "enter", " ":
            if _, ok := m.selected[m.cursor]; ok {
                delete(m.selected, m.cursor)
            } else {
                m.selected[m.cursor] = struct{}{}
            }
        }
    }
    return m, nil
}

// VIEW - Render to string
func (m model) View() string {
    if m.quitting {
        return "Goodbye!\n"
    }

    s := "What needs to be done?\n\n"

    for i, choice := range m.choices {
        cursor := " "
        if m.cursor == i {
            cursor = ">"
        }

        checked := " "
        if _, ok := m.selected[i]; ok {
            checked = "x"
        }

        s += fmt.Sprintf("%s [%s] %s\n", cursor, checked, choice)
    }

    s += "\nPress q to quit.\n"
    return s
}

func main() {
    p := tea.NewProgram(initialModel())
    if _, err := p.Run(); err != nil {
        fmt.Printf("Error: %v", err)
        os.Exit(1)
    }
}
```

## Messages & Commands

### Built-in Messages

```go
// Key press
case tea.KeyMsg:
    switch msg.String() {
    case "ctrl+c": // Ctrl+C
    case "enter":  // Enter key
    case "up":     // Arrow up
    case "a":      // Letter a
    }

// Window resize
case tea.WindowSizeMsg:
    width := msg.Width
    height := msg.Height

// Mouse events (if enabled)
case tea.MouseMsg:
    x, y := msg.X, msg.Y
    button := msg.Button
```

### Custom Messages

```go
// Define custom message types
type statusMsg string
type errMsg struct{ err error }

// Command that returns a message
func fetchStatus() tea.Msg {
    // Simulate API call
    time.Sleep(time.Second)
    return statusMsg("Ready!")
}

// Use in Update
func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
    switch msg := msg.(type) {
    case statusMsg:
        m.status = string(msg)
    case errMsg:
        m.err = msg.err
    }
    return m, nil
}

// Trigger command from Init or Update
func (m model) Init() tea.Cmd {
    return fetchStatus // Note: no parentheses!
}
```

### Commands

```go
// Return multiple commands
return m, tea.Batch(cmd1, cmd2, cmd3)

// Quit the program
return m, tea.Quit

// Do nothing
return m, nil

// Tick (for animations)
func tickCmd() tea.Cmd {
    return tea.Tick(time.Second, func(t time.Time) tea.Msg {
        return tickMsg(t)
    })
}
```

## Styling with Lipgloss

```go
import "github.com/charmbracelet/lipgloss"

var (
    // Colors
    subtle    = lipgloss.AdaptiveColor{Light: "#D9DCCF", Dark: "#383838"}
    highlight = lipgloss.AdaptiveColor{Light: "#874BFD", Dark: "#7D56F4"}
    special   = lipgloss.AdaptiveColor{Light: "#43BF6D", Dark: "#73F59F"}

    // Styles
    titleStyle = lipgloss.NewStyle().
        Bold(true).
        Foreground(lipgloss.Color("#FAFAFA")).
        Background(lipgloss.Color("#7D56F4")).
        Padding(0, 1)

    itemStyle = lipgloss.NewStyle().
        PaddingLeft(2)

    selectedStyle = lipgloss.NewStyle().
        PaddingLeft(2).
        Foreground(lipgloss.Color("#7D56F4")).
        Bold(true)

    boxStyle = lipgloss.NewStyle().
        Border(lipgloss.RoundedBorder()).
        BorderForeground(lipgloss.Color("#874BFD")).
        Padding(1, 2)
)

func (m model) View() string {
    title := titleStyle.Render("My App")

    var items string
    for i, item := range m.items {
        if i == m.cursor {
            items += selectedStyle.Render("> " + item) + "\n"
        } else {
            items += itemStyle.Render("  " + item) + "\n"
        }
    }

    return boxStyle.Render(title + "\n\n" + items)
}
```

## Bubbles Components

### Spinner

```go
import "github.com/charmbracelet/bubbles/spinner"

type model struct {
    spinner  spinner.Model
    loading  bool
}

func initialModel() model {
    s := spinner.New()
    s.Spinner = spinner.Dot
    s.Style = lipgloss.NewStyle().Foreground(lipgloss.Color("205"))
    return model{spinner: s, loading: true}
}

func (m model) Init() tea.Cmd {
    return m.spinner.Tick
}

func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
    switch msg := msg.(type) {
    case spinner.TickMsg:
        var cmd tea.Cmd
        m.spinner, cmd = m.spinner.Update(msg)
        return m, cmd
    }
    return m, nil
}

func (m model) View() string {
    if m.loading {
        return m.spinner.View() + " Loading..."
    }
    return "Done!"
}
```

### Text Input

```go
import "github.com/charmbracelet/bubbles/textinput"

type model struct {
    input textinput.Model
}

func initialModel() model {
    ti := textinput.New()
    ti.Placeholder = "Enter your name"
    ti.Focus()
    ti.CharLimit = 50
    ti.Width = 30
    return model{input: ti}
}

func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
    var cmd tea.Cmd
    m.input, cmd = m.input.Update(msg)

    switch msg := msg.(type) {
    case tea.KeyMsg:
        if msg.Type == tea.KeyEnter {
            // Handle submission
            value := m.input.Value()
        }
    }
    return m, cmd
}

func (m model) View() string {
    return fmt.Sprintf("Name:\n%s\n\nPress Enter to submit", m.input.View())
}
```

### List

```go
import "github.com/charmbracelet/bubbles/list"

type item struct {
    title, desc string
}

func (i item) Title() string       { return i.title }
func (i item) Description() string { return i.desc }
func (i item) FilterValue() string { return i.title }

type model struct {
    list list.Model
}

func initialModel() model {
    items := []list.Item{
        item{title: "Raspberry Pi", desc: "A tiny computer"},
        item{title: "Arduino", desc: "A microcontroller"},
    }

    l := list.New(items, list.NewDefaultDelegate(), 0, 0)
    l.Title = "My Hardware"

    return model{list: l}
}
```

### Progress Bar

```go
import "github.com/charmbracelet/bubbles/progress"

type model struct {
    progress progress.Model
    percent  float64
}

func initialModel() model {
    return model{
        progress: progress.New(progress.WithDefaultGradient()),
    }
}

func (m model) View() string {
    return m.progress.ViewAs(m.percent)
}
```

### Table

```go
import "github.com/charmbracelet/bubbles/table"

columns := []table.Column{
    {Title: "ID", Width: 4},
    {Title: "Name", Width: 20},
    {Title: "Status", Width: 10},
}

rows := []table.Row{
    {"1", "Project Alpha", "Active"},
    {"2", "Project Beta", "Pending"},
}

t := table.New(
    table.WithColumns(columns),
    table.WithRows(rows),
    table.WithFocused(true),
    table.WithHeight(7),
)
```

## Advanced Patterns

### Sub-models (Component Composition)

```go
type model struct {
    tabs     []string
    activeTab int

    // Sub-models for each tab
    homeModel    homeModel
    settingsModel settingsModel
}

func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
    var cmd tea.Cmd

    // Route to active tab's model
    switch m.activeTab {
    case 0:
        m.homeModel, cmd = m.homeModel.Update(msg)
    case 1:
        m.settingsModel, cmd = m.settingsModel.Update(msg)
    }

    return m, cmd
}
```

### Full-screen vs Inline

```go
// Full-screen (default)
p := tea.NewProgram(model{})

// Inline (within existing terminal output)
p := tea.NewProgram(model{}, tea.WithAltScreen())

// With mouse support
p := tea.NewProgram(model{}, tea.WithMouseCellMotion())
```

### Async Operations

```go
// HTTP request command
func fetchData(url string) tea.Cmd {
    return func() tea.Msg {
        resp, err := http.Get(url)
        if err != nil {
            return errMsg{err}
        }
        defer resp.Body.Close()

        body, _ := io.ReadAll(resp.Body)
        return dataMsg(body)
    }
}

// Use in Update
case tea.KeyMsg:
    if msg.String() == "f" {
        return m, fetchData("https://api.example.com/data")
    }
```

## Testing

```go
func TestUpdate(t *testing.T) {
    m := initialModel()

    // Simulate key press
    m, _ = m.Update(tea.KeyMsg{Type: tea.KeyDown})

    if m.cursor != 1 {
        t.Errorf("expected cursor 1, got %d", m.cursor)
    }
}

func TestView(t *testing.T) {
    m := initialModel()
    view := m.View()

    if !strings.Contains(view, "What needs to be done?") {
        t.Error("expected title in view")
    }
}
```

## Resources

- [Bubbletea GitHub](https://github.com/charmbracelet/bubbletea)
- [Bubbles Components](https://github.com/charmbracelet/bubbles)
- [Lipgloss Styling](https://github.com/charmbracelet/lipgloss)
- [Charm Examples](https://github.com/charmbracelet/bubbletea/tree/master/examples)
