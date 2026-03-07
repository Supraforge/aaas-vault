---
name: "vault-sync"
description: "Syncs skills, execution scripts, and directives from a project to the central vault, automatically de-branding project-specific content."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["vault","sync","skills","execution","directives","utility","internal"]
triggers:
  - "when I want to update the central vault with project assets"
  - "when I need to de-brand project-specific content"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "vault_sync.py"
---

# Vault Sync

## When to Use

- when I want to update the central vault with project assets
- when I need to de-brand project-specific content

## What This Does

Syncs skills, execution scripts, and directives from a project to the central vault, automatically de-branding project-specific content.

## Execution

```bash
python3 vault_sync.py [--all | <asset_type> | --diff | --from-vault]
```

### Parameters

None - Configuration managed in the script itself. Uses current working directory to determine project.

### Dependencies

- python3
- pyyaml
- filecmp
