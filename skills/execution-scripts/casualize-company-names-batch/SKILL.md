---
name: "casualize-company-names"
description: "Casualizes company names in a Google Sheet using Claude AI for cold emails. Removes legal suffixes and generic terms."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["google sheets","automation","cold email","company names","Claude AI"]
triggers:
  - "when a Google Sheet URL is provided"
  - "when you need to clean up business names for cold email"
  - "when you want to use AI to casualize company names"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "casualize_company_names_batch.py"
---

# Casualize Company Names

## When to Use

- when a Google Sheet URL is provided
- when you need to clean up business names for cold email
- when you want to use AI to casualize company names

## What This Does

Casualizes company names in a Google Sheet using Claude AI for cold emails. Removes legal suffixes and generic terms.

## Execution

```bash
python your_script_name.py <sheet_url> [--overwrite]
```

### Parameters

sheet_url: Google Sheet URL, --overwrite: Overwrite existing casual names

### Dependencies

- python
- gspread
- anthropic
- python-dotenv
