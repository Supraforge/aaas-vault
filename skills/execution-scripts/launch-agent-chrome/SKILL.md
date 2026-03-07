---
name: "launch-agent-chrome"
description: "Launches Google Chrome in 'Agent-Ready' mode with remote debugging enabled. Useful for automated browser testing and tooling when you need a specific Chrome profile."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["chrome","debugging","automation","browser","agent","utility","internal"]
triggers:
  - "when I need a Chrome instance with remote debugging"
  - "when I want to launch Chrome for automated testing"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "launch_agent_chrome.sh"
---

# Launch Agent Chrome

## When to Use

- when I need a Chrome instance with remote debugging
- when I want to launch Chrome for automated testing

## What This Does

Launches Google Chrome in 'Agent-Ready' mode with remote debugging enabled. Useful for automated browser testing and tooling when you need a specific Chrome profile.

## Execution

```bash
launch_agent_chrome.sh
```

### Parameters

None

### Dependencies

- Google Chrome
