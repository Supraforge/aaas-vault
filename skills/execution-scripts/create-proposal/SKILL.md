---
name: "pandadoc-proposal-creator"
description: "Creates a PandaDoc proposal document from a JSON input, populating it with client and project-specific details."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["pandadoc","proposal","document generation","automation","api"]
triggers:
  - "when a proposal document needs to be created in PandaDoc"
  - "when client and project details are available in JSON format"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "create_proposal.py"
---

# Pandadoc Proposal Creator

## When to Use

- when a proposal document needs to be created in PandaDoc
- when client and project details are available in JSON format

## What This Does

Creates a PandaDoc proposal document from a JSON input, populating it with client and project-specific details.

## Execution

```bash
python pandadoc_proposal_creator.py [optional: path/to/input.json] (or pass JSON via stdin)
```

### Parameters

Expects a JSON payload via stdin or a path to a JSON file as a CLI argument. Requires PANDADOC_API_KEY and PANDADOC_TEMPLATE_UUID env vars.

### Dependencies

- python3
- requests
- dotenv (optional)
