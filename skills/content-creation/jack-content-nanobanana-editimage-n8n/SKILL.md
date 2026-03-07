---
name: jack-content-nanobanana-editimage-n8n
description: >-
  Automates image editing with Nano Banana API in n8n, uploading a logo,
  generating a hyperrealistic image with notifications for new leads, and
  storing the result.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - image editing
  - automation
  - nano banana
  - n8n
  - lead magnet
  - api
triggers:
  - When a new form is submitted with a brand and logo.
  - When you want to generate a lead magnet image
allowed-tools: []
compatibility: 'n8n, Nano Banana API, ImgBB API, Google Drive'
metadata:
  source: jack-school
  lesson: 113
  lesson_title: How to Automate UNSTOPPABLE Lead Magnets
  difficulty: hard
  category: content
  tools_required:
    - n8n
    - Nano Banana API
    - ImgBB API
    - Google Drive
  estimated_setup_time: 1hr
  extracted_from:
    - "\U0001F34CNano Banana (BLUEPRINT).json"
---

# Content Nanobanana Editimage N8n

## When to Use

Use this skill when you need to:
- When a new form is submitted with a brand and logo.
- When you want to generate a lead magnet image

## What This Does

Automates image editing with Nano Banana API in n8n, uploading a logo, generating a hyperrealistic image with notifications for new leads, and storing the result.

## Workflow

The provided n8n workflow `🍌Nano Banana (BLUEPRINT).json`  contains the full automation logic. Configure the `API_KEY` variables in the HTTP Request nodes.

## Configuration

**Required tools/platforms:**
- n8n
- Nano Banana API
- ImgBB API
- Google Drive

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
