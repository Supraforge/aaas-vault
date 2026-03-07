---
name: "validate-skills"
description: "Validates skills by checking the directory structure and SKILL.md metadata against defined conventions. Use when developing or maintaining skills to ensure quality and consistency."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["skill validation","metadata","quality assurance","skill development","utility","internal"]
triggers:
  - "when skill is created"
  - "when skill is modified"
  - "when needing to check all skills"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "validate_skills.py"
---

# Validate Skills

## When to Use

- when skill is created
- when skill is modified
- when needing to check all skills

## What This Does

Validates skills by checking the directory structure and SKILL.md metadata against defined conventions. Use when developing or maintaining skills to ensure quality and consistency.

## Execution

```bash
python3 validate_skills.py [SKILL_NAME] [--vault] [--all]
```

### Parameters

SKILL_NAME (optional): Specific skill to validate. --vault: Validate skills in the vault. --all: Validate both project and vault skills.

### Dependencies

- python3
- pyyaml
