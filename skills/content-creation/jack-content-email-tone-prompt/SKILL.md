---
name: jack-content-email-tone-prompt
description: >-
  Instructs an LLM to create an HTML email response that matches the tone of
  voice from an incoming email.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - prompt
  - email
  - tone of voice
  - html
triggers:
  - When generating an automated email response using an LLM
  - >-
    When you need to ensure the email aligns with the sender's communication
    style
allowed-tools: []
compatibility: 'openai, gemini, any LLM provider'
metadata:
  source: jack-school
  lesson: 64
  lesson_title: Steal This AI Client Intelligence System... WOW
  difficulty: easy
  category: content
  tools_required:
    - openai
    - gemini
    - any LLM provider
  estimated_setup_time: 5min
---

# Content Email Tone Prompt

## When to Use

Use this skill when you need to:
- When generating an automated email response using an LLM
- When you need to ensure the email aligns with the sender's communication style

## What This Does

Instructs an LLM to create an HTML email response that matches the tone of voice from an incoming email.

## Workflow

You will receive an email and a set of instructions from the user. Your task is to craft a response to the email in HTML format. The response must match the user's tone of voice, as inferred from their instructions and provided context. Do not add any additional content beyond the email response requested by the user. Focus solely on delivering a concise, HTML-structured reply that adheres to their style and requirements.

## Configuration

**Required tools/platforms:**
- openai
- gemini
- any LLM provider

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
