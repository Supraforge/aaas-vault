---
name: jack-rag-airtable-client-search
description: >-
  Searches for client information in Airtable and formats the data for a vector
  database search using OpenAI.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - airtable
  - openai
  - vector database
  - client search
  - automation
triggers:
  - When client data is updated in Airtable.
allowed-tools: []
compatibility: 'make.com, airtable, openai'
metadata:
  source: jack-school
  lesson: 61
  lesson_title: Steal This AI Client Intelligence System... WOW
  difficulty: hard
  category: rag
  tools_required:
    - make.com
    - airtable
    - openai
  estimated_setup_time: 1hr
  extracted_from:
    - "[3_3] Personal Delivery System \U0001F4C8.json"
---

# Rag Airtable Client Search

## When to Use

Use this skill when you need to:
- When client data is updated in Airtable.

## What This Does

Searches for client information in Airtable and formats the data for a vector database search using OpenAI.

## Workflow

This Make.com module watches for changes in Airtable, searches for client details, and uses OpenAI to format the info as a search term for a vector database.

## Configuration

**Required tools/platforms:**
- make.com
- airtable
- openai

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
