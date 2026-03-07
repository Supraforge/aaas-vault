---
name: jack-workflow-lead-magnet-generation
description: >-
  Automates lead magnet creation by capturing form data, generating a plan using
  AI, and delivering it as HTML.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - lead magnet
  - automation
  - ai
  - paperform
  - make.com
triggers:
  - When a user submits a lead magnet request form
  - To automate the creation and delivery of lead magnets
allowed-tools: []
compatibility: 'make.com, paperform, openai'
metadata:
  source: jack-school
  lesson: 56
  lesson_title: This AI System Creates UNIQUE Lead Magnets (100% Automated)
  difficulty: hard
  category: leadgen
  tools_required:
    - make.com
    - paperform
    - openai
  estimated_setup_time: 1hr
  extracted_from:
    - Lead Magnet System (B2G).json
---

# Workflow Lead Magnet Generation

## When to Use

Use this skill when you need to:
- When a user submits a lead magnet request form
- To automate the creation and delivery of lead magnets

## What This Does

Automates lead magnet creation by capturing form data, generating a plan using AI, and delivering it as HTML.

## Workflow

This workflow automates the lead magnet generation process.
1. **Paperform Submission:** Triggers when a new submission is received from a Paperform form.
2. **Basic Router:**  Routes the data to the AI module.
3. **Anthropic Claude:** Creates a personalized 90-day business plan using the AI model based on the form data.


## Configuration

**Required tools/platforms:**
- make.com
- paperform
- openai

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
