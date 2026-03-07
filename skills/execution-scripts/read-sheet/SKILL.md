---
name: "google-sheet-to-json"
description: "Reads data from a Google Sheet and exports it as a JSON file. Useful when you need to process spreadsheet data with other tools."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["google sheets","data extraction","json","data conversion"]
triggers:
  - "when I need to extract Google Sheet data to JSON"
  - "when I want to process a spreadsheet as JSON"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "read_sheet.py"
---

# Google Sheet To Json

## When to Use

- when I need to extract Google Sheet data to JSON
- when I want to process a spreadsheet as JSON

## What This Does

Reads data from a Google Sheet and exports it as a JSON file. Useful when you need to process spreadsheet data with other tools.

## Execution

```bash
google-sheet-to-json.py --url <sheet_url> --worksheet <worksheet_name> --output_prefix <prefix>
```

### Parameters

--url (required): Google Sheets URL or ID.  --worksheet: Name of the worksheet (default: first sheet).  --output_prefix: Prefix for the output filename (default: leads_input).  GOOGLE_APPLICATION_CREDENTIALS environment variable: Path to Google service account credentials JSON file.

### Dependencies

- python3
- gspread
- google-auth
- google-auth-oauthlib
- python-dotenv
