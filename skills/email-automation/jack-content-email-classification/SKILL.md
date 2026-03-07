---
name: jack-content-email-classification
description: >-
  Classifies incoming emails into predefined categories (e.g., sponsorships,
  customer queries, spam) using an LLM.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - email
  - classification
  - automation
  - langchain
triggers:
  - when a new email arrives
  - to automatically sort emails
allowed-tools: []
compatibility: 'n8n, langchain'
metadata:
  source: jack-school
  lesson: 99
  lesson_title: TLDR
  difficulty: medium
  category: email
  tools_required:
    - n8n
    - langchain
  estimated_setup_time: 30min
  extracted_from:
    - "\U0001F525 Replace Your $4k_mo Secretary (1).json"
---

# Content Email Classification

## When to Use

Use this skill when you need to:
- when a new email arrives
- to automatically sort emails

## What This Does

Classifies incoming emails into predefined categories (e.g., sponsorships, customer queries, spam) using an LLM.

## Workflow

This N8N workflow node uses a Langchain Text Classifier to categorize emails based on their content. Input the email text, and define categories with descriptions for accurate classification.

## Configuration

**Required tools/platforms:**
- n8n
- langchain

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
