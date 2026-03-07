---
name: jack-openai-embedding-format
description: >-
  JSON format for generating embeddings with OpenAI's API. Configures input,
  model, and encoding format for vectorizing text.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - openai
  - embeddings
  - text-embedding-3-small
  - vectorization
triggers:
  - when generating embeddings with OpenAI
  - when preparing data for vector databases
allowed-tools: []
compatibility: openai
metadata:
  source: jack-school
  lesson: 65
  lesson_title: Automate Anything with AI Agents... Zero Code
  difficulty: easy
  category: content
  tools_required:
    - openai
  estimated_setup_time: 5min
---

# Openai Embedding Format

## When to Use

Use this skill when you need to:
- when generating embeddings with OpenAI
- when preparing data for vector databases

## What This Does

JSON format for generating embeddings with OpenAI's API. Configures input, model, and encoding format for vectorizing text.

## Workflow

{
  "input": "{{33.`JSON String`}}",
  "model": "text-embedding-3-small",
  "encoding_format": "float"
}

## Configuration

**Required tools/platforms:**
- openai

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
