---
name: jack-rag-create-openai-embedding
description: >-
  Creates an OpenAI embedding for a given text using the
  'text-embedding-3-small' model.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - openai
  - embedding
  - text-embedding-3-small
  - automation
  - vector database
triggers:
  - >-
    When you need to create a vector embedding for text to store in a vector
    database.
allowed-tools: []
compatibility: 'make.com, openai'
metadata:
  source: jack-school
  lesson: 61
  lesson_title: Steal This AI Client Intelligence System... WOW
  difficulty: medium
  category: rag
  tools_required:
    - make.com
    - openai
  estimated_setup_time: 15min
  extracted_from:
    - "[1_3] Company Information\U0001F4A1.json"
    - "[2_3] Onboarding \U0001F525.json"
---

# Rag Create Openai Embedding

## When to Use

Use this skill when you need to:
- When you need to create a vector embedding for text to store in a vector database.

## What This Does

Creates an OpenAI embedding for a given text using the 'text-embedding-3-small' model.

## Workflow

This Make.com module takes a JSON string as input, creates an OpenAI embedding using the specified model and encoding format.

## Configuration

**Required tools/platforms:**
- make.com
- openai

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
