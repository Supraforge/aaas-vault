---
name: jack-nocode-vercel-mcp-config
description: >-
  Add Vercel Model Context Protocol (MCP) to Antigravity config to manage Vercel
  deployments from within Antigravity.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - vercel
  - mcp
  - antigravity
  - deployment
triggers:
  - when wanting to integrate Vercel deployments with Antigravity
  - when setting up Model Context Protocol for Vercel
allowed-tools: []
compatibility: 'vercel, antigravity'
metadata:
  source: jack-school
  lesson: 131
  lesson_title: Tools
  difficulty: medium
  category: nocode
  tools_required:
    - vercel
    - antigravity
  estimated_setup_time: 15min
  extracted_from:
    - HowIbuildBeautiful10000WebsiteswithAI.txt
---

# Nocode Vercel Mcp Config

## When to Use

Use this skill when you need to:
- when wanting to integrate Vercel deployments with Antigravity
- when setting up Model Context Protocol for Vercel

## What This Does

Add Vercel Model Context Protocol (MCP) to Antigravity config to manage Vercel deployments from within Antigravity.

## Workflow

```json
"vercel": {
  "command": "npx",
  "args": [
    "-y",
    "@robinson_ai_systems/vercel-mcp"
  ],
  "env": {
    "VERCEL_TOKEN": "INSERT_VERCEL_API_KEY"
  }
}
```
Replace INSERT_VERCEL_API_KEY with your Vercel token.

## Configuration

**Required tools/platforms:**
- vercel
- antigravity

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
