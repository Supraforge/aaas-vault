---
name: jack-content-segmentation-prompt
description: >-
  Analyze text for micro, meso, and macro-level stylistic elements to create a
  segmentation guideline for AI content generation.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - style analysis
  - AI persona
  - content style
  - language model
triggers:
  - when you need to analyze existing content for stylistic patterns
  - when creating a detailed profile to guide AI content generation
allowed-tools: []
compatibility: 'openai, claude'
metadata:
  source: jack-school
  lesson: 27
  lesson_title: 10 Levels of AI Automation
  difficulty: hard
  category: content
  tools_required:
    - openai
    - claude
  estimated_setup_time: 1hr
  extracted_from:
    - Segmentation_Prompt_.txt
---

# Content Segmentation Prompt

## When to Use

Use this skill when you need to:
- when you need to analyze existing content for stylistic patterns
- when creating a detailed profile to guide AI content generation

## What This Does

Analyze text for micro, meso, and macro-level stylistic elements to create a segmentation guideline for AI content generation.

## Workflow

Analyze the given text focusing on the following micro-level elements:
[MICRO-LEVEL ELEMENTS]
Please provide a detailed guideline for each element, including relevant examples from the given text. It is imperative that your guidelines read as instructions to a language model to emulate this style exactly.

Analyze the given text focusing on the following meso-level elements:
[MESO-LEVEL ELEMENTS]
Please provide a detailed guideline for each element, including relevant examples from the given text. It is imperative that your guidelines read as instructions to a language model to emulate this style exactly.

Analyze the given text focusing on the following macro-level elements and additional considerations:
[MACRO-LEVEL ELEMENTS]
Please provide a detailed guideline for each element, including relevant examples from the given text. It is imperative that your guidelines read as instructions to a language model to emulate this style exactly.

## Configuration

**Required tools/platforms:**
- openai
- claude

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
