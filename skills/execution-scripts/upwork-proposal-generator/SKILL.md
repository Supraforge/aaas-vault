---
name: "upwork-proposal-generator"
description: "Generates customized cover letters and project proposals for Upwork jobs using Opus 4.5 for high-quality personalization."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["upwork","proposal","cover letter","automation","AI"]
triggers:
  - "when I need to generate an upwork proposal"
  - "when I want to quickly create a cover letter for an upwork job"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "upwork_proposal_generator.py"
---

# Upwork Proposal Generator

## When to Use

- when I need to generate an upwork proposal
- when I want to quickly create a cover letter for an upwork job

## What This Does

Generates customized cover letters and project proposals for Upwork jobs using Opus 4.5 for high-quality personalization.

## Execution

```bash
python execution/upwork_proposal_generator.py --input .tmp/upwork_jobs_batch.json
```

### Parameters

--input <path_to_upwork_jobs_batch.json>: Path to the JSON file containing the Upwork job descriptions.

### Dependencies

- python3
- anthropic
- google-api-python-client
- google-auth-httplib2
- google-auth-oauthlib
- python-dotenv
