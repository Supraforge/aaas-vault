---
name: jack-rag-claude-vision-browser-assistance
description: >-
  Uses Claude Vision to analyze browser screenshots, extracts text, and provides
  user assistance based on conversation history.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - claude vision
  - browser automation
  - make.com
  - ai assistance
triggers:
  - when a user needs help navigating a web page
  - when visual context is required for AI assistance
allowed-tools: []
compatibility: 'make.com, claude'
metadata:
  source: jack-school
  lesson: 50
  lesson_title: Claude Vision in Your Browser is INSANE
  difficulty: hard
  category: rag
  tools_required:
    - make.com
    - claude
  estimated_setup_time: 1hr
  extracted_from:
    - "Claude Vision \U0001F440.json"
---

# Rag Claude Vision Browser Assistance

## When to Use

Use this skill when you need to:
- when a user needs help navigating a web page
- when visual context is required for AI assistance

## What This Does

Uses Claude Vision to analyze browser screenshots, extracts text, and provides user assistance based on conversation history.

## Workflow

The workflow takes a screenshot and text from a browser page, sends it to Claude Vision with conversation history, and receives helpful instructions.

## Configuration

**Required tools/platforms:**
- make.com
- claude

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
