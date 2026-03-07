---
name: "enrich-missing-emails"
description: "Enriches missing email addresses in a Google Sheet using the AnyMailFinder API.  It's useful when you have incomplete contact information and need to find email addresses."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["email enrichment","google sheets","anymailfinder","data enrichment","sales"]
triggers:
  - "when a Google Sheet has missing email addresses"
  - "when you need to enrich contact data with email addresses"
  - "when you have first name, last name, and company domain in a sheet"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "enrich_emails.py"
---

# Enrich Missing Emails

## When to Use

- when a Google Sheet has missing email addresses
- when you need to enrich contact data with email addresses
- when you have first name, last name, and company domain in a sheet

## What This Does

Enriches missing email addresses in a Google Sheet using the AnyMailFinder API.  It's useful when you have incomplete contact information and need to find email addresses.

## Execution

```bash
enrich-missing-emails <google_sheet_url>
```

### Parameters

The Google Sheet URL is passed as a command line argument.  The ANYMAILFINDER_API_KEY and GOOGLE_APPLICATION_CREDENTIALS (or OAuth2 token.json) environment variables must be set.

### Dependencies

- python3
- gspread
- google-auth
- google-auth-oauthlib
- requests
- python-dotenv
