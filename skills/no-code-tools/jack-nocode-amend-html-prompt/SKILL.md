---
name: jack-nocode-amend-html-prompt
description: >-
  Instructs to rewrite HTML with webhook integration and refined chat display
  for responses from multiple experts.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - HTML
  - Webhooks
  - chat interface
triggers:
  - When integrating webhooks into existing HTML code
  - Improving the display of chat responses from multiple sources
allowed-tools: []
compatibility: 'OpenAI, Claude'
metadata:
  source: jack-school
  lesson: 36
  lesson_title: This AI Meeting Automation 100Xs Your Productivity
  difficulty: medium
  category: nocode
  tools_required:
    - OpenAI
    - Claude
  estimated_setup_time: 30min
  extracted_from:
    - PROMPTS_FROM_VIDEO.txt
---

# Nocode Amend Html Prompt

## When to Use

Use this skill when you need to:
- When integrating webhooks into existing HTML code
- Improving the display of chat responses from multiple sources

## What This Does

Instructs to rewrite HTML with webhook integration and refined chat display for responses from multiple experts.

## Workflow

i would you like you to re-write the html in full with the following upgrades:
* include this webhook: [insert webhook]
* we want the chats to be visible above the part where you enter the question
* you will be given 9 responses from 3 people in turn, show them with their title.
* make it look more like this:

## Configuration

**Required tools/platforms:**
- OpenAI
- Claude

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
