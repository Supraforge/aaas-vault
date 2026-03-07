---
name: "instantly-autoreply"
description: "Automatically replies to emails in Instantly using a knowledge base and Claude for reply generation.  Useful for automating sales outreach and customer support."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["email automation","sales outreach","AI","Claude","Instantly"]
triggers:
  - "when a new email is received in Instantly"
  - "when an Instantly webhook is triggered"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "instantly_autoreply.py"
---

# Instantly Autoreply

## When to Use

- when a new email is received in Instantly
- when an Instantly webhook is triggered

## What This Does

Automatically replies to emails in Instantly using a knowledge base and Claude for reply generation.  Useful for automating sales outreach and customer support.

## Execution

```bash
python instantly_autoreply.py --payload <payload.json> --token_data <token_data.json>
```

### Parameters

Requires Instantly API key (INSTANTLY_API_KEY), Anthropic API Key (ANTHROPIC_API_KEY) and Google OAuth token data passed as a JSON object

### Dependencies

- requests
- google-api-python-client
- google-auth-httplib2
- google-auth-oauthlib
- anthropic
