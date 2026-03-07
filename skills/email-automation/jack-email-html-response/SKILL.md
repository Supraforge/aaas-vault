---
name: jack-email-html-response
description: >-
  Generates an HTML-formatted email response that mirrors the tone of voice and
  style of the incoming email.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - email
  - automation
  - html
  - deepseek
  - openrouter
triggers:
  - When a new email is received
  - When you need to automatically reply to emails with a consistent tone
allowed-tools: []
compatibility: 'make.com, openrouter, deepseek, microsoft email'
metadata:
  source: jack-school
  lesson: 64
  lesson_title: Steal This AI Client Intelligence System... WOW
  difficulty: medium
  category: email
  tools_required:
    - make.com
    - openrouter
    - deepseek
    - microsoft email
  estimated_setup_time: 30min
  extracted_from:
    - "\U0001F433 DeepSeek V3.json"
---

# Email Html Response

## When to Use

Use this skill when you need to:
- When a new email is received
- When you need to automatically reply to emails with a consistent tone

## What This Does

Generates an HTML-formatted email response that mirrors the tone of voice and style of the incoming email.

## Workflow

This Make.com workflow uses OpenRouter and DeepSeek to generate an HTML email reply that matches the tone of the original email.

1.  **Trigger:** Custom Mail Hook to receive emails.
2.  **AI Processing:** OpenRouter module calls DeepSeek with a prompt to generate an HTML email based on the received email.
3.  **Email Sending:** Microsoft Email module sends the generated HTML content as an email reply.

## Configuration

**Required tools/platforms:**
- make.com
- openrouter
- deepseek
- microsoft email

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
