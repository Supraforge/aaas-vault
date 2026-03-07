---
name: "casualize-names-google-sheets"
description: "Casualizes first names in a Google Sheet using Claude AI to generate friendly nicknames, updating the sheet with the results."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["google sheets","ai","name generation","automation","cold email"]
triggers:
  - "when I need to generate casual nicknames for cold emails"
  - "when I want to automate name casualization in a spreadsheet"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "casualize_first_names_batch.py"
---

# Casualize Names Google Sheets

## When to Use

- when I need to generate casual nicknames for cold emails
- when I want to automate name casualization in a spreadsheet

## What This Does

Casualizes first names in a Google Sheet using Claude AI to generate friendly nicknames, updating the sheet with the results.

## Execution

```bash
python casualize_names.py "<google_sheet_url>" [--overwrite]
```

### Parameters

sheet_url (required): URL of the Google Sheet.  --overwrite (optional): Overwrite existing 'casual_first_name' column. Requires ANTHROPIC_API_KEY env var.

### Dependencies

- python
- gspread
- anthropic
- python-dotenv
