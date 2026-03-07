---
name: jack-social-instagram-post-agent
description: Generates Instagram posts by researching news and crafting engaging captions.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - instagram
  - content
  - ai
  - social media
  - captions
triggers:
  - when the user asks to generate content for Instagram
allowed-tools: []
compatibility: 'n8n, openai'
metadata:
  source: jack-school
  lesson: 107
  lesson_title: This NEW AI System Will Blow up Your Socials (INSANE)
  difficulty: medium
  category: social
  tools_required:
    - n8n
    - openai
  estimated_setup_time: 15min
---

# Social Instagram Post Agent

## When to Use

Use this skill when you need to:
- when the user asks to generate content for Instagram

## What This Does

Generates Instagram posts by researching news and crafting engaging captions.

## Workflow

Research 2–3 recent, high-quality news updates relevant to my avatar in the UK within the last 7 days, focusing on how they connect to the problem i solve
Select the strongest story or angle for Instagram.

Do not output JSON or extra structure.
Do not explain your reasoning.
Output must be only the Instagram caption, ready to copy-paste into Instagram.

## Configuration

**Required tools/platforms:**
- n8n
- openai

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
