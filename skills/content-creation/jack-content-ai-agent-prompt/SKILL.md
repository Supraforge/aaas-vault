---
name: jack-content-ai-agent-prompt
description: >-
  Provides a structured template for prompting AI agents, covering role,
  context, task, collaboration, and output format, enabling better AI agent
  performance.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - AI
  - prompting
  - automation
  - agent
triggers:
  - when building an AI agent
  - when defining an AI role
allowed-tools: []
compatibility: openai
metadata:
  source: jack-school
  lesson: 68
  lesson_title: Automate Anything with AI Agents... Zero Code
  difficulty: medium
  category: content
  tools_required:
    - openai
  estimated_setup_time: 15min
  extracted_from:
    - "AI Agent Prompting Template \U0001F916.txt"
    - AI_Agent_Prompting_Template_-_Google_Docs.txt
---

# Content Ai Agent Prompt

## When to Use

Use this skill when you need to:
- when building an AI agent
- when defining an AI role

## What This Does

Provides a structured template for prompting AI agents, covering role, context, task, collaboration, and output format, enabling better AI agent performance.

## Workflow

AI Agent Prompting Template 🤖

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

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
