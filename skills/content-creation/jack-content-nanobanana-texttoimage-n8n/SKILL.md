---
name: jack-content-nanobanana-texttoimage-n8n
description: >-
  Automates image creation with Nano Banana API, generating images from Airtable
  prompts and storing them back in Airtable.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - image generation
  - automation
  - nano banana
  - n8n
  - text-to-image
  - api
  - airtable
triggers:
  - When a workflow is manually triggered.
  - When you want to create images from a set of prompts
allowed-tools: []
compatibility: 'n8n, Nano Banana API, Airtable'
metadata:
  source: jack-school
  lesson: 113
  lesson_title: How to Automate UNSTOPPABLE Lead Magnets
  difficulty: hard
  category: content
  tools_required:
    - n8n
    - Nano Banana API
    - Airtable
  estimated_setup_time: 1hr
  extracted_from:
    - "\U0001F34CNano Banana (BLUEPRINT).json"
---

# Content Nanobanana Texttoimage N8n

## When to Use

Use this skill when you need to:
- When a workflow is manually triggered.
- When you want to create images from a set of prompts

## What This Does

Automates image creation with Nano Banana API, generating images from Airtable prompts and storing them back in Airtable.

## Workflow

The provided n8n workflow `🍌Nano Banana (BLUEPRINT).json`  contains the full automation logic. Configure the `API_KEY` variables in the HTTP Request nodes.

## Configuration

**Required tools/platforms:**
- n8n
- Nano Banana API
- Airtable

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
