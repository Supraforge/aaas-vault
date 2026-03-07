---
name: "skills-manager"
description: "Manage skills across a project and central vault, enabling/disabling and importing skills."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["skills","management","vault","enable","disable","import","utility","internal"]
triggers:
  - "when I want to manage project skills"
  - "when I need to import skills from the vault"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "skills_manager.py"
---

# Skills Manager

## When to Use

- when I want to manage project skills
- when I need to import skills from the vault

## What This Does

Manage skills across a project and central vault, enabling/disabling and importing skills.

## Execution

```bash
python3 skills_manager.py <command> [SKILL]
```

### Parameters

SKILL (required for enable, disable, import): The name of the skill.

### Dependencies

- python3
- shutil
- os
- pathlib
