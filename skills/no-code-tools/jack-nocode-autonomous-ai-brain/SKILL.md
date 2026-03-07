---
name: jack-nocode-autonomous-ai-brain
description: >-
  Make.com workflow to create an autonomous AI brain: triggers, researches topic
  via Perplexity, analyzes with 2 GPT agents, outputs to Google Docs.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - make.com
  - automation
  - ai brain
  - perplexity
  - openai
  - google docs
triggers:
  - When you want to automate research and analysis of ideas.
  - When you want to create a fully autonomous AI workflow.
allowed-tools: []
compatibility: 'make.com, perplexity, openai, google docs, slack'
metadata:
  source: jack-school
  lesson: 2
  lesson_title: How to Create a FULLY Autonomous AI Brain (10X Ideas)
  difficulty: hard
  category: nocode
  tools_required:
    - make.com
    - perplexity
    - openai
    - google docs
    - slack
  estimated_setup_time: 1hr
---

# Nocode Autonomous Ai Brain

## When to Use

Use this skill when you need to:
- When you want to automate research and analysis of ideas.
- When you want to create a fully autonomous AI workflow.

## What This Does

Make.com workflow to create an autonomous AI brain: triggers, researches topic via Perplexity, analyzes with 2 GPT agents, outputs to Google Docs.

## Workflow

1. Trigger: Watch for Private Channel Messages in Slack (or other trigger source).
2. Perplexity AI: Create a Chat Completion using the 'AI Researcher' prompt.
3. OpenAI: Message an Assistant (Idea Bot) using the research output.
4. OpenAI: Message an Assistant (Critique Bot) using the Idea Bot output.
5. Google Docs: Append Text to a document with the Critique Bot output.

## Configuration

**Required tools/platforms:**
- make.com
- perplexity
- openai
- google docs
- slack

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
