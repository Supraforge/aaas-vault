---
name: jack-content-midjourney-prompt-generation
description: >-
  Generates a Midjourney prompt from input text describing a scene or concept,
  adhering to a specific style and aspect ratio.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - midjourney
  - prompt engineering
  - image generation
  - content creation
triggers:
  - When you need to create a Midjourney prompt from descriptive text.
  - When you want to generate images with a specific style.
allowed-tools: []
compatibility: 'midjourney, text analysis tool'
metadata:
  source: jack-school
  lesson: 11
  lesson_title: Heads-up
  difficulty: medium
  category: content
  tools_required:
    - midjourney
    - text analysis tool
  estimated_setup_time: 5min
  extracted_from:
    - Midjourney_Prompt_.txt
---

# Content Midjourney Prompt Generation

## When to Use

Use this skill when you need to:
- When you need to create a Midjourney prompt from descriptive text.
- When you want to generate images with a specific style.

## What This Does

Generates a Midjourney prompt from input text describing a scene or concept, adhering to a specific style and aspect ratio.

## Workflow

1. Analyze the input text to identify the subject, action, setting, and details.
2. Use the information to fill the template: [subject], [action], [setting], [additional details]. The image must be natural, realistic, in 2018, style raw, 8K, taken on iPhone, --ar 16:9
3.  Ensure the final prompt is well-formatted and complete.

## Configuration

**Required tools/platforms:**
- midjourney
- text analysis tool

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
