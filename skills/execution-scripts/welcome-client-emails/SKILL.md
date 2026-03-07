---
name: "welcome-client-emails"
description: "Sends a 3-email welcome sequence (Nick, Peter, Sam) when a new client signs an agreement.  Uses the Gmail API."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["email","gmail","welcome sequence","automation","onboarding"]
triggers:
  - "when a new client signs"
  - "when onboarding a client"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "welcome_client_emails.py"
---

# Welcome Client Emails

## When to Use

- when a new client signs
- when onboarding a client

## What This Does

Sends a 3-email welcome sequence (Nick, Peter, Sam) when a new client signs an agreement.  Uses the Gmail API.

## Execution

```bash
python welcome_emails.py
```

### Parameters

Requires 'client_name', 'client_email', and 'company_name' in the payload. Requires a valid 'token.json' file for Google API authentication (see script comments for location).

### Dependencies

- google-api-python-client
- google-auth-httplib2
- google-auth-oauthlib
