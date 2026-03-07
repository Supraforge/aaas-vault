---
name: get-focus-mode
description: Get the current macOS Focus mode
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---

# Get Focus Mode

Returns the name of the currently active macOS Focus mode.

## Usage

```bash
~/clawd/skills/get-focus-mode/get-focus-mode.sh
```

## Output

Prints the Focus mode name to stdout:
- "No Focus" - Focus mode is off
- "Office" - Office focus is active
- "Sleep" - Sleep focus is active  
- "Do Not Disturb" - DND is active

## Requirements

- macOS
- `jq` installed
