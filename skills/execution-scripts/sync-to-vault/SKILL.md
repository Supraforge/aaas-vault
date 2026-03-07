---
name: "skill-vault-sync"
description: "Syncs skills from a project to the central vault, making them available for future projects. Use to update the vault with improved skills."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["skill management","vault synchronization","project skills","skill sharing","utility","internal"]
triggers:
  - "when a skill is updated in a project"
  - "when skills should be shared with the vault"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "sync_to_vault.py"
---

# Skill Vault Sync

## When to Use

- when a skill is updated in a project
- when skills should be shared with the vault

## What This Does

Syncs skills from a project to the central vault, making them available for future projects. Use to update the vault with improved skills.

## Execution

```bash
python3 sync_to_vault.py [skill_name | --all | --diff | --list]
```

### Parameters

Optional skill name to sync, --all to sync all, --diff to show changes, --list to list skills.  No required environment variables.
