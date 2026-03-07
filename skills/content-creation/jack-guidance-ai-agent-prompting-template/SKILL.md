---
name: jack-guidance-ai-agent-prompting-template
description: >-
  Provides a structured template for creating effective AI agent prompts,
  including role definition, context, task, constraints, collaboration, and
  examples.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - ai agent
  - prompting
  - template
  - role definition
  - context
  - task
triggers:
  - when creating prompts for AI agents
  - when needing a structured approach to prompt design
allowed-tools: []
compatibility: 'openai, any LLM'
metadata:
  source: jack-school
  lesson: 69
  lesson_title: How DeepSeek AI Automates my work Effortlessly
  difficulty: easy
  category: content
  tools_required:
    - openai
    - any LLM
  estimated_setup_time: 15min
  extracted_from:
    - "AI Agent Prompting Template \U0001F916.txt"
    - AI_Agent_Prompting_Template_-_Google_Docs.txt
    - _DeepSeek_Integration_Brain.txt
---

# Guidance Ai Agent Prompting Template

## When to Use

Use this skill when you need to:
- when creating prompts for AI agents
- when needing a structured approach to prompt design

## What This Does

Provides a structured template for creating effective AI agent prompts, including role definition, context, task, constraints, collaboration, and examples.

## Workflow

## AI Agent Prompting Template

[ROLE]
- You are the [Name of Agent / Role].
- Your main responsibility is to [Primary Objective].

[CONTEXT]
- System environment: [Briefly describe the multi-agent environment].
- Known details: [Facts, references, previous conversation context].

[TASK]
- Goal: [Specific outcome you want].
- Constraints: [Time limit, length limit, etc.].
- Style: [Tone, formatting guidelines].
- Output format: [Plain text, HTML, JSON, etc.].

[COLLABORATION]
- Other agents: [Who they are, what they provide].
- Interaction: [How and when this agent should interact with them].

[EXAMPLES]
- Good response example: [...]
- Bad response example: [...]

[FINAL REQUIREMENTS]
- QA checks: [Spelling, grammar, factual accuracy].
- Ethical guidelines: [Allowed/Disallowed content].
- Error handling: [Instructions if something goes wrong].

## Configuration

**Required tools/platforms:**
- openai
- any LLM

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
