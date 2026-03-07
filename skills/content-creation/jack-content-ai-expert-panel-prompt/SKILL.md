---
name: jack-content-ai-expert-panel-prompt
description: >-
  Defines prompt structure to build an AI web app with functionalities to submit
  questions and display different voices in chat.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - AI
  - Expert Panel
  - HTML
triggers:
  - Generating code for a web app
  - Creating interface for user submissions
allowed-tools: []
compatibility: 'OpenAI, Claude'
metadata:
  source: jack-school
  lesson: 36
  lesson_title: This AI Meeting Automation 100Xs Your Productivity
  difficulty: medium
  category: content
  tools_required:
    - OpenAI
    - Claude
  estimated_setup_time: 30min
  extracted_from:
    - PROMPTS_FROM_VIDEO.txt
---

# Content Ai Expert Panel Prompt

## When to Use

Use this skill when you need to:
- Generating code for a web app
- Creating interface for user submissions

## What This Does

Defines prompt structure to build an AI web app with functionalities to submit questions and display different voices in chat.

## Workflow

I would like you to create html only code for a web application. Functionalities:
* user submits question
* webhook fires with question (webhook address: )
* It will display 3 different voices in a whatsapp style chat with different colours
* once submitted do a confetti animation & add a 70 second timer
* font avenir
* use the below designs for the html

## Configuration

**Required tools/platforms:**
- OpenAI
- Claude

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
