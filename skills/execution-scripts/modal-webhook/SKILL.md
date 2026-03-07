---
name: "claude-orchestrator"
description: "Orchestrates event-driven Claude interactions via webhooks for various tasks like email sending, data manipulation, and document generation."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["claude","webhook","automation","llm","orchestration","utility","internal"]
triggers:
  - "when a webhook is triggered"
  - "when a POST request is received"
  - "when data needs to be processed"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "modal_webhook.py"
---

# Claude Orchestrator

## When to Use

- when a webhook is triggered
- when a POST request is received
- when data needs to be processed

## What This Does

Orchestrates event-driven Claude interactions via webhooks for various tasks like email sending, data manipulation, and document generation.

## Execution

```bash
modal deploy execution/modal_webhook.py
```

### Parameters

The script relies on webhooks.json for configuration and expects a 'slug' parameter in the POST request to determine which directive to execute. It also depends on several environment variables and secrets (defined in Modal secrets) for API keys and authentication.

### Dependencies

- modal
- anthropic
- fastapi
- google-auth
- google-auth-oauthlib
- google-api-python-client
- requests
- apify-client
- gspread
- pandas
- python-dotenv
- yt-dlp
