// Bubbletea TUI Starter Template
//
// Features:
// - Interactive list with selection
// - Spinner for loading states
// - Text input form
// - Styled output with Lipgloss
//
// Usage:
//   go run main.go

package main

import (
	"fmt"
	"os"
	"strings"
	"time"

	"github.com/charmbracelet/bubbles/list"
	"github.com/charmbracelet/bubbles/spinner"
	"github.com/charmbracelet/bubbles/textinput"
	tea "github.com/charmbracelet/bubbletea"
	"github.com/charmbracelet/lipgloss"
)

// ============================================
// Styles
// ============================================

var (
	titleStyle = lipgloss.NewStyle().
			Bold(true).
			Foreground(lipgloss.Color("#FAFAFA")).
			Background(lipgloss.Color("#7D56F4")).
			Padding(0, 1)

	boxStyle = lipgloss.NewStyle().
			Border(lipgloss.RoundedBorder()).
			BorderForeground(lipgloss.Color("#7D56F4")).
			Padding(1, 2)

	successStyle = lipgloss.NewStyle().
			Foreground(lipgloss.Color("#73F59F")).
			Bold(true)

	dimStyle = lipgloss.NewStyle().
			Foreground(lipgloss.Color("#666666"))
)

// ============================================
// Types
// ============================================

type screen int

const (
	menuScreen screen = iota
	formScreen
	loadingScreen
	resultScreen
)

type formData struct {
	name  string
	email string
}

// Messages
type loadingDoneMsg struct{}

// ============================================
// Model
// ============================================

type model struct {
	screen      screen
	menuList    list.Model
	nameInput   textinput.Model
	emailInput  textinput.Model
	formStep    int
	spinner     spinner.Model
	formData    formData
	width       int
	height      int
	quitting    bool
}

// List item implementation
type menuItem struct {
	title, desc string
}

func (i menuItem) Title() string       { return i.title }
func (i menuItem) Description() string { return i.desc }
func (i menuItem) FilterValue() string { return i.title }

func initialModel() model {
	// Menu list
	items := []list.Item{
		menuItem{title: "Start New Task", desc: "Begin a new workflow"},
		menuItem{title: "View Status", desc: "Check current progress"},
		menuItem{title: "Settings", desc: "Configure options"},
		menuItem{title: "Exit", desc: "Quit the application"},
	}

	l := list.New(items, list.NewDefaultDelegate(), 0, 0)
	l.Title = "What would you like to do?"
	l.SetShowStatusBar(false)
	l.SetFilteringEnabled(false)

	// Text inputs
	nameInput := textinput.New()
	nameInput.Placeholder = "John Doe"
	nameInput.Focus()
	nameInput.CharLimit = 50
	nameInput.Width = 30

	emailInput := textinput.New()
	emailInput.Placeholder = "john@example.com"
	emailInput.CharLimit = 50
	emailInput.Width = 30

	// Spinner
	s := spinner.New()
	s.Spinner = spinner.Dot
	s.Style = lipgloss.NewStyle().Foreground(lipgloss.Color("205"))

	return model{
		screen:     menuScreen,
		menuList:   l,
		nameInput:  nameInput,
		emailInput: emailInput,
		spinner:    s,
	}
}

// ============================================
// Bubbletea Interface
// ============================================

func (m model) Init() tea.Cmd {
	return nil
}

func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	switch msg := msg.(type) {
	case tea.WindowSizeMsg:
		m.width = msg.Width
		m.height = msg.Height
		m.menuList.SetSize(msg.Width-4, msg.Height-8)
		return m, nil

	case tea.KeyMsg:
		switch msg.String() {
		case "ctrl+c":
			m.quitting = true
			return m, tea.Quit
		case "q":
			if m.screen == menuScreen {
				m.quitting = true
				return m, tea.Quit
			}
		case "esc":
			if m.screen != menuScreen {
				m.screen = menuScreen
				return m, nil
			}
		}

	case loadingDoneMsg:
		m.screen = resultScreen
		return m, nil

	case spinner.TickMsg:
		if m.screen == loadingScreen {
			var cmd tea.Cmd
			m.spinner, cmd = m.spinner.Update(msg)
			return m, cmd
		}
	}

	// Route to screen-specific update
	switch m.screen {
	case menuScreen:
		return m.updateMenu(msg)
	case formScreen:
		return m.updateForm(msg)
	case resultScreen:
		return m.updateResult(msg)
	}

	return m, nil
}

func (m model) updateMenu(msg tea.Msg) (tea.Model, tea.Cmd) {
	switch msg := msg.(type) {
	case tea.KeyMsg:
		if msg.String() == "enter" {
			i, ok := m.menuList.SelectedItem().(menuItem)
			if ok {
				switch i.title {
				case "Start New Task":
					m.screen = formScreen
					m.formStep = 0
					m.nameInput.Focus()
					return m, textinput.Blink
				case "View Status":
					m.screen = loadingScreen
					return m, tea.Batch(m.spinner.Tick, simulateLoading())
				case "Exit":
					m.quitting = true
					return m, tea.Quit
				}
			}
		}
	}

	var cmd tea.Cmd
	m.menuList, cmd = m.menuList.Update(msg)
	return m, cmd
}

func (m model) updateForm(msg tea.Msg) (tea.Model, tea.Cmd) {
	switch msg := msg.(type) {
	case tea.KeyMsg:
		if msg.String() == "enter" {
			if m.formStep == 0 {
				m.formData.name = m.nameInput.Value()
				m.formStep = 1
				m.nameInput.Blur()
				m.emailInput.Focus()
				return m, textinput.Blink
			} else {
				m.formData.email = m.emailInput.Value()
				m.screen = loadingScreen
				return m, tea.Batch(m.spinner.Tick, simulateLoading())
			}
		}
	}

	var cmd tea.Cmd
	if m.formStep == 0 {
		m.nameInput, cmd = m.nameInput.Update(msg)
	} else {
		m.emailInput, cmd = m.emailInput.Update(msg)
	}
	return m, cmd
}

func (m model) updateResult(msg tea.Msg) (tea.Model, tea.Cmd) {
	switch msg := msg.(type) {
	case tea.KeyMsg:
		if msg.String() == "b" || msg.String() == "enter" {
			m.screen = menuScreen
			m.nameInput.Reset()
			m.emailInput.Reset()
			return m, nil
		}
	}
	return m, nil
}

func (m model) View() string {
	if m.quitting {
		return "Goodbye!\n"
	}

	var content string

	switch m.screen {
	case menuScreen:
		content = m.menuList.View()
	case formScreen:
		content = m.viewForm()
	case loadingScreen:
		content = m.viewLoading()
	case resultScreen:
		content = m.viewResult()
	}

	title := titleStyle.Render("My TUI App")
	footer := dimStyle.Render("Press q to quit, esc to go back")

	return fmt.Sprintf("%s\n\n%s\n\n%s", title, content, footer)
}

func (m model) viewForm() string {
	var b strings.Builder

	if m.formStep == 0 {
		b.WriteString("Enter your name:\n\n")
		b.WriteString(m.nameInput.View())
	} else {
		b.WriteString("Enter your email:\n\n")
		b.WriteString(m.emailInput.View())
	}

	b.WriteString(fmt.Sprintf("\n\n%s", dimStyle.Render(fmt.Sprintf("Step %d of 2", m.formStep+1))))

	return boxStyle.Render(b.String())
}

func (m model) viewLoading() string {
	return boxStyle.Render(fmt.Sprintf("%s Processing...", m.spinner.View()))
}

func (m model) viewResult() string {
	var b strings.Builder

	b.WriteString(successStyle.Render("✓ Task Complete!"))
	b.WriteString("\n\n")
	b.WriteString(fmt.Sprintf("Name: %s\n", m.formData.name))
	b.WriteString(fmt.Sprintf("Email: %s\n", m.formData.email))
	b.WriteString("\n")
	b.WriteString(dimStyle.Render("Press 'b' to go back"))

	return boxStyle.Render(b.String())
}

// ============================================
// Commands
// ============================================

func simulateLoading() tea.Cmd {
	return func() tea.Msg {
		time.Sleep(2 * time.Second)
		return loadingDoneMsg{}
	}
}

// ============================================
// Main
// ============================================

func main() {
	p := tea.NewProgram(initialModel(), tea.WithAltScreen())
	if _, err := p.Run(); err != nil {
		fmt.Printf("Error: %v", err)
		os.Exit(1)
	}
}
