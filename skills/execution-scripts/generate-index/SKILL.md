---
name: "generate-skills-index"
description: "Generates a JSON index of skills by parsing SKILL.md files in a directory. Useful for skill discovery and documentation."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["skill-management","index-generation","documentation","automation","utility","internal"]
triggers:
  - "when skills directory changes"
  - "when updating skill documentation"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "generate_index.py"
---

# Generate Skills Index

## When to Use

- when skills directory changes
- when updating skill documentation

## What This Does

Generates a JSON index of skills by parsing SKILL.md files in a directory. Useful for skill discovery and documentation.

## Execution

```bash
python scripts/generate_skills_index.py
```

### Parameters

No CLI parameters. Reads from `skills` directory and writes to `skills_index.json` in the project root.

### Dependencies

- Python 3.6+
