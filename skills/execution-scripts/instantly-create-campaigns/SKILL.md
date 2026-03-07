---
name: "instantly-campaign-creator"
description: "Creates 3 Instantly email campaigns, each targeting a unique offer, with A/B tested first steps. Uses client details and Claude AI to generate compelling sequences."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["email marketing","cold outreach","AI","campaign creation","instantly.ai"]
triggers:
  - "when I need to create multiple email campaigns quickly"
  - "when I want to use AI to generate email sequences for Instantly"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "instantly_create_campaigns.py"
---

# Instantly Campaign Creator

## When to Use

- when I need to create multiple email campaigns quickly
- when I want to use AI to generate email sequences for Instantly

## What This Does

Creates 3 Instantly email campaigns, each targeting a unique offer, with A/B tested first steps. Uses client details and Claude AI to generate compelling sequences.

## Execution

```bash
python3 execution/instantly_create_campaigns.py --client_name "Your Client Name" --client_description "Your client description here" --offers "Offer 1|Offer 2|Offer 3" --target_audience "Describe who you are targeting" --social_proof "Mention your credentials"
```

### Parameters

--client_name: Name of the client. Required.
--client_description: Detailed description of the client's business. Required.
--offers: Pipe-separated list of offers (e.g., 'Offer1|Offer2|Offer3'). Optional; if missing, offers will be generated.
--target_audience: Description of the target audience. Required.
--social_proof: Credentials to mention in emails. Required.

Env vars:
ANTHROPIC_API_KEY: API key for Anthropic.
INSTANTLY_API_KEY: API key for Instantly.

### Dependencies

- python3
- requests
- anthropic
- python-dotenv
