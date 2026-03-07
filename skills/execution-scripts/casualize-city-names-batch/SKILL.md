---
name: "casualize-city-names"
description: "Casualizes formal city names in a Google Sheet for cold emails using Claude. Improves deliverability with colloquial local names."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["google sheets","nlp","city names","cold email","data processing"]
triggers:
  - "when needing casual city names for emails"
  - "when spreadsheet requires city name cleaning"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "casualize_city_names_batch.py"
---

# Casualize City Names

## When to Use

- when needing casual city names for emails
- when spreadsheet requires city name cleaning

## What This Does

Casualizes formal city names in a Google Sheet for cold emails using Claude. Improves deliverability with colloquial local names.

## Execution

```bash
python script.py <sheet_url> [--overwrite]
```

### Parameters

sheet_url: Google Sheet URL. --overwrite: Overwrite existing casual names (optional). ANTHROPIC_API_KEY env var must be set.

### Dependencies

- python3
- gspread
- anthropic
- python-dotenv
