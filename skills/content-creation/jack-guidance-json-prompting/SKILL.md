---
name: jack-guidance-json-prompting
description: >-
  Instruct an LLM to return data ONLY in JSON format, emphasizing structure,
  constraints, and providing examples for accurate JSON output.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - llm
  - json
  - prompting
  - data extraction
  - format constraints
triggers:
  - When you need LLMs to return structured data in JSON format
  - When you require precise and consistent JSON output from an LLM
allowed-tools: []
compatibility: 'openai, anthropic'
metadata:
  source: jack-school
  lesson: 55
  lesson_title: Tools
  difficulty: medium
  category: content
  tools_required:
    - openai
    - anthropic
  estimated_setup_time: 15min
---

# Guidance Json Prompting

## When to Use

Use this skill when you need to:
- When you need LLMs to return structured data in JSON format
- When you require precise and consistent JSON output from an LLM

## What This Does

Instruct an LLM to return data ONLY in JSON format, emphasizing structure, constraints, and providing examples for accurate JSON output.

## Workflow

When using LLMs, provide clear instructions for JSON output:

1.  Specify NO additional information, explanations, or text outside the JSON.
2.  Highlight requirements like starting/ending with `{}` and double quotes.
3.  Provide an example JSON to guide the format and structure.
4. Emphasize the importance of adhering to JSON syntax rules and structure.


## Configuration

**Required tools/platforms:**
- openai
- anthropic

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
