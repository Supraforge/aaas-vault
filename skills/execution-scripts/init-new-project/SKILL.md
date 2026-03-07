---
name: "init-new-project"
description: "Resets a project by clearing context, .tmp/, and infrastructure configs. Use when starting a new project based on a template."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["project setup","reset","initialization","cleanup","utility","internal"]
triggers:
  - "when starting a new project"
  - "when resetting a project"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "init_new_project.py"
---

# Init New Project

## When to Use

- when starting a new project
- when resetting a project

## What This Does

Resets a project by clearing context, .tmp/, and infrastructure configs. Use when starting a new project based on a template.

## Execution

```bash
python3 execution/init_new_project.py
```

### Parameters

No CLI arguments or env vars are required.

### Dependencies

- python3
