---
name: jack-content-tone-of-voice-prompt
description: >-
  Instruct an AI to write in a specific tone of voice, providing detailed micro,
  meso, and macro-level stylistic guidelines.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - tone of voice
  - AI writing
  - content creation
  - style guide
triggers:
  - when you need to generate AI content in a specific style
  - when you want to create content that matches a particular persona
allowed-tools: []
compatibility: 'openai, claude'
metadata:
  source: jack-school
  lesson: 27
  lesson_title: 10 Levels of AI Automation
  difficulty: medium
  category: content
  tools_required:
    - openai
    - claude
  estimated_setup_time: 30min
  extracted_from:
    - Tone_of_Voice_Prompt_.txt
---

# Content Tone Of Voice Prompt

## When to Use

Use this skill when you need to:
- when you need to generate AI content in a specific style
- when you want to create content that matches a particular persona

## What This Does

Instruct an AI to write in a specific tone of voice, providing detailed micro, meso, and macro-level stylistic guidelines.

## Workflow

You will write as [PERSONA]. A full guideline of how to write as [PERSONA] will be given below. You will be given a task and must follow every tone of voice principle below to create an output aligned with those instructions. You must never reference the tone of voice guidelines in your output, but you must follow them exactly

The task:
[TASK DESCRIPTION]

[PERSONA]'s Tone of voice:
[DETAILED GUIDELINES INCLUDING MICRO, MESO AND MACRO-LEVEL ELEMENTS]

## Configuration

**Required tools/platforms:**
- openai
- claude

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
