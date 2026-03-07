---
name: "casualize-google-sheets"
description: "Casualizes first names, company names, and cities in a Google Sheet using Claude to improve cold email personalization."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["google sheets","nlp","casualize","anthropic","data processing"]
triggers:
  - "when I want to casualize data in a Google Sheet"
  - "when I need to prep data for cold emails"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "casualize_batch.py"
---

# Casualize Google Sheets

## When to Use

- when I want to casualize data in a Google Sheet
- when I need to prep data for cold emails

## What This Does

Casualizes first names, company names, and cities in a Google Sheet using Claude to improve cold email personalization.

## Execution

```bash
python your_script_name.py <sheet_url> [--overwrite] [--workers <num_workers>]
```

### Parameters

sheet_url: URL of the Google Sheet. --overwrite: Overwrite existing values. --workers: Number of parallel workers (default: 5). ANTHROPIC_API_KEY: API key set in .env

### Dependencies

- python
- gspread
- anthropic
- python-dotenv
