---
name: "json-to-google-sheets"
description: "Uploads JSON data to a Google Sheet, handling authentication and sheet creation. Use when needing to import data from JSON files into a spreadsheet."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["google sheets","json","data import","automation","spreadsheet"]
triggers:
  - "when I need to import a JSON file into Google Sheets"
  - "when I have JSON data for a spreadsheet"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "update_sheet.py"
---

# Json To Google Sheets

## When to Use

- when I need to import a JSON file into Google Sheets
- when I have JSON data for a spreadsheet

## What This Does

Uploads JSON data to a Google Sheet, handling authentication and sheet creation. Use when needing to import data from JSON files into a spreadsheet.

## Execution

```bash
json-to-google-sheets <path_to_json_file> [--sheet_name <sheet_name>]
```

### Parameters

json_file: Path to the JSON file. sheet_name: (optional) Name of the Google Sheet. Uses 'GOOGLE_APPLICATION_CREDENTIALS' or 'token.json' for authentication. 'USER_EMAIL' env var for sharing (optional)

### Dependencies

- python3
- gspread
- google-auth
- google-auth-oauthlib
- pandas
- python-dotenv
