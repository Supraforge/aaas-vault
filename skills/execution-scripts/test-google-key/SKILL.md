---
name: "test-gemini-api-key"
description: "Tests a Google Gemini API key by listing available models. Useful for verifying API key validity and connectivity."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["gemini","api","google","test","verification","utility","internal"]
triggers:
  - "when I need to test my gemini key"
  - "when I want to verify a google ai api key"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "test_google_key.py"
---

# Test Gemini Api Key

## When to Use

- when I need to test my gemini key
- when I want to verify a google ai api key

## What This Does

Tests a Google Gemini API key by listing available models. Useful for verifying API key validity and connectivity.

## Execution

```bash
python3 test_gemini.py
```

### Parameters

Requires the GOOGLE_API_KEY environment variable to be set.

### Dependencies

- requests
