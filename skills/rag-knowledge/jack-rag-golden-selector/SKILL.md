---
name: jack-rag-golden-selector
description: >-
  Uses a 'golden selector' to identify relevant workflows from a data source
  (e.g. Airtable) based on descriptions.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - rag
  - airtable
  - workflow selection
triggers:
  - >-
    when you need to dynamically select an automation workflow based on user
    description
allowed-tools: []
compatibility: airtable
metadata:
  source: jack-school
  lesson: 87
  lesson_title: This AI Agent Builds Automations (Chrome Extension)
  difficulty: medium
  category: rag
  tools_required:
    - airtable
  estimated_setup_time: 30min
---

# Rag Golden Selector

## When to Use

Use this skill when you need to:
- when you need to dynamically select an automation workflow based on user description

## What This Does

Uses a 'golden selector' to identify relevant workflows from a data source (e.g. Airtable) based on descriptions.

## Workflow

1.  Store workflow data (name, description, steps) in a structured format like Airtable.
2.  When a user describes a desired automation, use the description as a query.
3.  Use semantic search or keyword matching to identify workflows in the data store that best match the description.
4.  Return the matched workflow ID and details.

## Configuration

**Required tools/platforms:**
- airtable

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
