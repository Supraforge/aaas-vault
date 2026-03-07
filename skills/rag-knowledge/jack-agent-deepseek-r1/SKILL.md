---
name: jack-agent-deepseek-r1
description: Creates an AI agent powered by DeepSeek R1 within n8n for chat interactions.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - ai agent
  - deepseek
  - openrouter
  - chat
  - n8n
triggers:
  - when a chat message is received
  - to enable a conversational AI agent
allowed-tools: []
compatibility: 'n8n, deepseek, openrouter'
metadata:
  source: jack-school
  lesson: 67
  lesson_title: Automate Anything with AI Agents... Zero Code
  difficulty: medium
  category: rag
  tools_required:
    - n8n
    - deepseek
    - openrouter
  estimated_setup_time: 30min
  extracted_from:
    - ___DeepSeek_r1_Agent.json
---

# Agent Deepseek R1

## When to Use

Use this skill when you need to:
- when a chat message is received
- to enable a conversational AI agent

## What This Does

Creates an AI agent powered by DeepSeek R1 within n8n for chat interactions.

## Workflow

This n8n workflow sets up a chat agent using the DeepSeek R1 model via OpenRouter, allowing for conversational interactions.

## Configuration

**Required tools/platforms:**
- n8n
- deepseek
- openrouter

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
