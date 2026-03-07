---
name: jack-social-post-creator
description: >-
  Creates social media posts for platforms like Instagram, X, LinkedIn, Skool,
  and YouTube summaries.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - social media
  - content creation
  - AI
  - post generation
triggers:
  - when the user asks to generate social media content for a specific platform
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

# Social Post Creator

## When to Use

Use this skill when you need to:
- when the user asks to generate social media content for a specific platform

## What This Does

Creates social media posts for platforms like Instagram, X, LinkedIn, Skool, and YouTube summaries.

## Workflow

Use the Post Creator agent when asked to create social content. Supported outputs: Twitter/X (short, sharp, ≤280 chars, 1–2 hashtags max), LinkedIn (professional, insight-driven, 2–5 sentences), Instagram (engaging, casual, may use emojis and hashtags), Skool (conversational, community-focused), YouTube summaries (concise, highlight key takeaways). Tailor tone + length for the platform and output final post ready to publish (no JSON, no extra wrapping).

## Configuration

**Required tools/platforms:**
- n8n
- openai

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
