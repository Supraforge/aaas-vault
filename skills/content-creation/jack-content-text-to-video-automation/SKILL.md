---
name: jack-content-text-to-video-automation
description: >-
  Automate viral video creation by using Airtable, Anthropic Claude, and
  Replicate in a Make.com workflow to generate images from stoic quotes.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - make.com
  - airtable
  - anthropic
  - replicate
  - automation
  - image generation
  - stoic quotes
  - video creation
triggers:
  - When you want to automatically generate images from text
  - When you need to create viral video content based on stoic philosophy
allowed-tools: []
compatibility: 'make.com, airtable, anthropic claude, replicate'
metadata:
  source: jack-school
  lesson: 55
  lesson_title: Tools
  difficulty: hard
  category: content
  tools_required:
    - make.com
    - airtable
    - anthropic claude
    - replicate
  estimated_setup_time: 1hr
  extracted_from:
    - "Text to Video Generation \U0001F4C8.json"
---

# Content Text To Video Automation

## When to Use

Use this skill when you need to:
- When you want to automatically generate images from text
- When you need to create viral video content based on stoic philosophy

## What This Does

Automate viral video creation by using Airtable, Anthropic Claude, and Replicate in a Make.com workflow to generate images from stoic quotes.

## Workflow

The provided JSON file 'Text to Video Generation 📈.json' contains the blueprint for a Make.com automation scenario that generates images from stoic quotes sourced from an Airtable base.  It increments a counter, retrieves the quote from Airtable, uses Anthropic Claude to generate a prompt, and then sends the prompt to Replicate for image generation.

## Configuration

**Required tools/platforms:**
- make.com
- airtable
- anthropic claude
- replicate

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
