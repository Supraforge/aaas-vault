---
name: "append-google-sheet-rows"
description: "Append rows from a JSON file to a Google Sheet, matching columns to existing headers.  Useful when you have data in JSON that needs to be added to a spreadsheet."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["google sheets","automation","data import","spreadsheet","append"]
triggers:
  - "when I want to add data to a Google Sheet from a JSON file"
  - "when I need to update a Google Sheet programmatically"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "append_to_sheet.py"
---

# Append Google Sheet Rows

## When to Use

- when I want to add data to a Google Sheet from a JSON file
- when I need to update a Google Sheet programmatically

## What This Does

Append rows from a JSON file to a Google Sheet, matching columns to existing headers.  Useful when you have data in JSON that needs to be added to a spreadsheet.

## Execution

```bash
append-google-sheet-rows.py --url <sheet_url> --json_file <json_file> [--worksheet <worksheet_name>]
```

### Parameters

--url (required): Google Sheets URL or ID
--json_file (required): Path to JSON file
--worksheet: (optional) Name of the worksheet (default: first sheet)
GOOGLE_APPLICATION_CREDENTIALS: Path to the credentials.json file (or set as env var). If missing, will attempt to authenticate via token.json or interactive login.

### Dependencies

- python3
- gspread
- google-auth
- google-auth-oauthlib
- python-dotenv
