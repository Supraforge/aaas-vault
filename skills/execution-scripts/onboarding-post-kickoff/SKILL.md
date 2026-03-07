---
name: "post-kickoff-onboarding"
description: "Orchestrates client onboarding after kickoff: lead generation, campaign creation, knowledge base setup, summary email."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["onboarding","automation","lead generation","email marketing","google sheets"]
triggers:
  - "when a client kickoff call is complete"
  - "when onboarding is triggered"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "onboarding_post_kickoff.py"
---

# Post Kickoff Onboarding

## When to Use

- when a client kickoff call is complete
- when onboarding is triggered

## What This Does

Orchestrates client onboarding after kickoff: lead generation, campaign creation, knowledge base setup, summary email.

## Execution

```bash
python3 path/to/onboarding_script.py --payload '{"client_name": "Example Inc.", "client_email": "test@example.com", "service_type": "Accounting", "target_location": "New York", "offers": "Offer 1 | Offer 2 | Offer 3"}' --token_data '{"token": "...", "refresh_token": "...", "token_uri": "...", "client_id": "...", "client_secret": "...", "scopes": ["..."]}'
```

### Parameters

Requires a JSON payload containing client_name, client_email, service_type, target_location, offers (pipe-separated), target_audience, social_proof, lead_limit. Also requires Google OAuth token data.

### Dependencies

- Python 3
- google-api-python-client
- google-auth-httplib2
- google-auth-oauthlib
- subprocess
- datetime
- pathlib
