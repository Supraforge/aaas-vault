# CLI UX Guidelines

> Best practices from clig.dev and industry standards

## Philosophy

### Human-First Design
Modern CLIs are used directly by humans, not just scripts. Design for human interaction first.

```
OLD THINKING: CLIs are for power users who read man pages
NEW THINKING: CLIs should be discoverable, forgiving, and helpful
```

### The Conversation Model
CLI interaction is a dialogue:
1. User issues command
2. Tool provides feedback
3. User adjusts and retries
4. Success (or helpful failure)

Design for this iterative process.

---

## Output Principles

### 1. Show Progress Always

| Duration | Indicator |
|----------|-----------|
| < 100ms | Nothing needed |
| 100ms - 1s | Spinner |
| 1s - 10s | Progress bar |
| > 10s | Progress bar + ETA |

```bash
# Bad: Silent hang
$ mytool deploy
[...user wonders if it's working...]

# Good: Immediate feedback
$ mytool deploy
⠋ Connecting to server...
████████████████░░░░░░░░ 67% | ETA: 12s
✓ Deployed successfully!
```

### 2. Respect the Terminal

```bash
# Detect if running in a terminal
if [ -t 1 ]; then
    # Human-friendly output with colors
else
    # Machine-friendly plain text
fi
```

- Use colors sparingly and meaningfully
- Respect `NO_COLOR` environment variable
- Provide `--no-color` flag
- Use ANSI codes only when stdout is a TTY

### 3. Appropriate Information Density

```bash
# Bad: Too verbose
$ mytool status
Checking connection to server at https://api.example.com...
Connection established successfully.
Fetching project metadata from database...
Project metadata retrieved.
Current status: active
Last deployment: 2024-01-15T10:30:00Z
...50 more lines...

# Good: Scannable, with detail available
$ mytool status
✓ Connected | Project: my-app | Status: active
  Last deploy: 2 hours ago

$ mytool status --verbose  # For when you need more
```

### 4. Structure Output for Humans AND Machines

```bash
# Default: Human-readable
$ mytool list
NAME        STATUS    CREATED
my-app      active    2 hours ago
other-app   stopped   5 days ago

# Flag: Machine-readable
$ mytool list --json
[{"name": "my-app", "status": "active", "created": "2024-01-15T10:30:00Z"}]

# Pipe-friendly: Plain text
$ mytool list | grep active
my-app      active    2 hours ago
```

---

## Error Handling

### The Golden Rule
Every error message should answer:
1. What went wrong?
2. Why did it happen?
3. How do I fix it?

### Good vs Bad Errors

```bash
# Bad
$ mytool deploy
Error: ECONNREFUSED

# Better
$ mytool deploy
Error: Could not connect to server

# Best
$ mytool deploy
✗ Could not connect to api.example.com:443

  The server refused the connection. This usually means:
  • The server is down
  • Your network is blocking the connection
  • The URL is incorrect

  Try:
  1. Check if the server is running: curl https://api.example.com/health
  2. Verify your network connection
  3. Check your config: mytool config show

  Docs: https://docs.example.com/troubleshooting#connection-refused
```

### Error Output Location

```bash
# Errors go to stderr (so they don't break pipes)
echo "Error: something failed" >&2

# Exit codes matter
exit 0  # Success
exit 1  # General error
exit 2  # Misuse (bad arguments)
```

---

## Arguments & Flags

### Flag Conventions

| Flag | Meaning |
|------|---------|
| `-h`, `--help` | Show help |
| `-V`, `--version` | Show version |
| `-v`, `--verbose` | More output |
| `-q`, `--quiet` | Less output |
| `-f`, `--force` | Skip confirmations |
| `-n`, `--dry-run` | Preview without executing |
| `-o`, `--output FILE` | Output file |
| `-c`, `--config FILE` | Config file |
| `--json` | JSON output |
| `--no-color` | Disable colors |

### Naming Conventions

```bash
# Use full words for clarity
--output not --out
--recursive not --rec
--verbose not --verb

# Use kebab-case
--dry-run not --dryRun
--no-color not --nocolor

# Negative flags
--no-cache not --skip-cache
--no-verify not --unsafe
```

### Positional vs Flags

```bash
# Positional: For the primary target
mytool deploy my-app

# Flags: For options/modifiers
mytool deploy my-app --env production --force

# Rule: If you'd need to remember order, use flags
# Bad: mytool copy source dest staging true
# Good: mytool copy source dest --env staging --force
```

---

## Help & Documentation

### Help Output Structure

```
mytool - One-line description

USAGE
    mytool <command> [options]

COMMANDS
    init        Create a new project
    deploy      Deploy to production
    status      Check current status

OPTIONS
    -h, --help      Show this help
    -V, --version   Show version
    -v, --verbose   Increase verbosity

EXAMPLES
    mytool init my-project
    mytool deploy --env staging
    mytool status --json

DOCS
    https://docs.example.com
```

### Key Principles

1. **Lead with examples** - Most users scan for patterns
2. **Keep it scannable** - Use columns, grouping, whitespace
3. **Link to full docs** - Help is a summary, not a manual
4. **Show common workflows** - Not just individual commands

### Smart Defaults

```bash
# No args? Show help, not an error
$ mytool
Usage: mytool <command> [options]

Run 'mytool --help' for more information.

# Suggest corrections
$ mytool dploy
Unknown command: dploy

Did you mean: deploy?
```

---

## Interactivity

### When to Prompt

```bash
# DO prompt for:
- Dangerous/destructive actions
- Missing required information
- Ambiguous situations

# DON'T prompt for:
- Non-interactive environments (CI/CD)
- When all info is available
- Confirmations that can use --force
```

### Prompt Best Practices

```bash
# Provide defaults
Enter project name [my-project]:

# Show current value when editing
Enter API key [***hidden***]:

# Validate inline
Email: not-an-email
  ↳ Invalid email format. Try: user@example.com

# Support escape
Press Ctrl+C to cancel
```

### Respect --no-input

```bash
# In scripts, prompts should fail gracefully
if [ "$NO_INPUT" = "1" ]; then
    echo "Error: Cannot prompt in non-interactive mode"
    echo "Provide --name flag or set NAME env var"
    exit 1
fi
```

---

## Configuration

### Precedence (highest to lowest)

1. Command-line flags
2. Environment variables
3. Project config (`./.myapp.yaml`)
4. User config (`~/.config/myapp/config.yaml`)
5. System config (`/etc/myapp/config.yaml`)
6. Built-in defaults

### Environment Variables

```bash
# Naming convention
MYAPP_API_KEY
MYAPP_CONFIG_PATH
MYAPP_VERBOSE

# Boolean flags
MYAPP_DEBUG=1    # truthy
MYAPP_DEBUG=     # falsy
```

### Config Files

```yaml
# Use XDG Base Directory
# Linux: ~/.config/myapp/
# macOS: ~/Library/Application Support/myapp/

# Support multiple formats
config.yaml
config.json
config.toml
```

---

## Composability

### Work with Pipes

```bash
# Read from stdin
echo "input" | mytool process

# Write to stdout
mytool generate > output.txt

# Chain commands
mytool list --json | jq '.[] | .name' | xargs mytool delete
```

### Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | General error |
| 2 | Misuse (bad args) |
| 126 | Permission denied |
| 127 | Command not found |
| 130 | Ctrl+C (SIGINT) |

### Signals

```bash
# Handle Ctrl+C gracefully
trap cleanup SIGINT SIGTERM

cleanup() {
    echo "Interrupted. Cleaning up..."
    # Cleanup code
    exit 130
}
```

---

## Performance & Responsiveness

### Startup Time

```
< 100ms: Excellent
100-250ms: Acceptable
250-500ms: Noticeable lag
> 500ms: Too slow
```

Tips:
- Lazy-load dependencies
- Cache expensive operations
- Show spinner immediately

### Feedback Timing

```
0-100ms: No feedback needed
100ms-1s: Show spinner
1s-10s: Show progress
>10s: Show ETA
```

---

## Subcommands

### Verb-Noun Pattern

```bash
# Good: verb-noun
git commit
docker run
kubectl get pods

# Avoid: noun-verb
git-commit  # harder to discover
```

### Hierarchy

```bash
# Two levels max
mytool project create
mytool project list
mytool project delete

# Not
mytool project settings advanced security enable  # too deep
```

### Aliases

```bash
# Common abbreviations
mytool ls    # list
mytool rm    # remove
mytool i     # install

# Document in help
ALIASES
    ls → list
    rm → remove
```

---

## Versioning & Updates

### Version Output

```bash
$ mytool --version
mytool 1.2.3

# Or with more detail
$ mytool --version --verbose
mytool 1.2.3
  Built: 2024-01-15
  Commit: abc123
  Go: 1.21
```

### Update Notifications

```bash
# Non-intrusive notice
$ mytool deploy
✓ Deployed successfully

A new version is available: 1.3.0 (you have 1.2.3)
Run 'mytool update' to upgrade.
```

---

## Security

### Sensitive Data

```bash
# Never accept passwords as flags (visible in ps, history)
# Bad
mytool login --password secret123

# Good
mytool login
Password: ████████

# Or
MYAPP_PASSWORD=secret mytool login
mytool login < password.txt
```

### Confirmations

```bash
# Destructive actions require confirmation
$ mytool delete --all
This will delete 47 items. Type 'delete all' to confirm:
> delete all
Deleting...

# Or use --force to skip
$ mytool delete --all --force
Deleting 47 items...
```

---

## Resources

- [Command Line Interface Guidelines](https://clig.dev/)
- [12 Factor CLI Apps](https://medium.com/@jdxcode/12-factor-cli-apps-dd3c227a0e46)
- [Heroku CLI Style Guide](https://devcenter.heroku.com/articles/cli-style-guide)
- [GNU Standards for CLIs](https://www.gnu.org/prep/standards/html_node/Command_002dLine-Interfaces.html)
