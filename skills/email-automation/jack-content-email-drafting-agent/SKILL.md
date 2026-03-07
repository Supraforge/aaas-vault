---
name: jack-content-email-drafting-agent
description: >-
  Generates draft email replies using an AI agent, considering context from past
  emails and a knowledge base.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - email
  - drafting
  - ai agent
  - automation
triggers:
  - when needing to quickly respond to emails
  - to automate email replies
allowed-tools: []
compatibility: 'n8n, openai, airtable'
metadata:
  source: jack-school
  lesson: 99
  lesson_title: TLDR
  difficulty: medium
  category: email
  tools_required:
    - n8n
    - openai
    - airtable
  estimated_setup_time: 1hr
  extracted_from:
    - "\U0001F525 Replace Your $4k_mo Secretary (1).json"
---

# Content Email Drafting Agent

## When to Use

Use this skill when you need to:
- when needing to quickly respond to emails
- to automate email replies

## What This Does

Generates draft email replies using an AI agent, considering context from past emails and a knowledge base.

## Workflow

Core Requirement:
For every incoming email (non-negotiable):
You must always produce a complete reply text that can be sent as a draft email using the Gmail draft reply tool.
Create the draft reply using this tool without exception.
Even if the message is spam, irrelevant, or unclear — still produce a draft that:
Answers appropriately
Politely declines
Or asks for clarification.
Never skip producing a draft.

## Configuration

**Required tools/platforms:**
- n8n
- openai
- airtable

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
