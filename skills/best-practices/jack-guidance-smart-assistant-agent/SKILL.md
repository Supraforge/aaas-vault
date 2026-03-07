---
name: jack-guidance-smart-assistant-agent
description: >-
  Defines a persona for an AI Smart Assistant Agent, detailing its role,
  context, tasks, and ethical guidelines.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - ai agent
  - persona
  - system prompt
  - smart assistant
triggers:
  - when defining the role and responsibilities of an AI assistant agent
allowed-tools: []
compatibility: 'openai, any LLM'
metadata:
  source: jack-school
  lesson: 67
  lesson_title: Automate Anything with AI Agents... Zero Code
  difficulty: medium
  category: guidance
  tools_required:
    - openai
    - any LLM
  estimated_setup_time: 15min
---

# Guidance Smart Assistant Agent

## When to Use

Use this skill when you need to:
- when defining the role and responsibilities of an AI assistant agent

## What This Does

Defines a persona for an AI Smart Assistant Agent, detailing its role, context, tasks, and ethical guidelines.

## Workflow

```The current date is: {{$now}}

**[ROLE]**  
- You are the **Smart Assistant Agent**.  
- Your main responsibility is to efficiently manage online searches, appointments, knowledge retrieval, and email communications.  
[CONTEXT] ... [TASK] ... [COLLABORATION] ... [EXAMPLES] ... [FINAL REQUIREMENTS]```

## Configuration

**Required tools/platforms:**
- openai
- any LLM

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
