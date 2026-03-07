---
name: jack-social-image-improvement-agent
description: >-
  Improves image quality based on user prompts using file IDs and new file
  names.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - image editing
  - ai
  - workflow
  - google drive
triggers:
  - when the user asks to edit or improve an image
allowed-tools: []
compatibility: 'n8n, replicate, google drive'
metadata:
  source: jack-school
  lesson: 107
  lesson_title: This NEW AI System Will Blow up Your Socials (INSANE)
  difficulty: medium
  category: social
  tools_required:
    - n8n
    - replicate
    - google drive
  estimated_setup_time: 30min
---

# Social Image Improvement Agent

## When to Use

Use this skill when you need to:
- when the user asks to edit or improve an image

## What This Does

Improves image quality based on user prompts using file IDs and new file names.

## Workflow

Call Improve workflow once only if: You have a valid file_id of the source image. The user gave a clear edit instruction (e.g., “make the jumper blue,” “replace background with modern office,” “increase saturation”). You have computed the next new_file_name.

## Configuration

**Required tools/platforms:**
- n8n
- replicate
- google drive

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
