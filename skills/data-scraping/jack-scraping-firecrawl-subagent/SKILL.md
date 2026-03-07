---
name: jack-scraping-firecrawl-subagent
description: >-
  Create a sub-agent to scrape and retrieve specific data from websites using
  Firecrawl, given a URL, prompt, and property to extract.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - scraping
  - firecrawl
  - sub-agent
  - automation
triggers:
  - When executed by another workflow
allowed-tools: []
compatibility: 'n8n, firecrawl'
metadata:
  source: jack-school
  lesson: 85
  lesson_title: What it does
  difficulty: medium
  category: scraping
  tools_required:
    - n8n
    - firecrawl
  estimated_setup_time: 30min
  extracted_from:
    - "\U0001F52E subagent magic.json"
---

# Scraping Firecrawl Subagent

## When to Use

Use this skill when you need to:
- When executed by another workflow

## What This Does

Create a sub-agent to scrape and retrieve specific data from websites using Firecrawl, given a URL, prompt, and property to extract.

## Workflow

See source file for full workflow.

## Configuration

**Required tools/platforms:**
- n8n
- firecrawl

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
