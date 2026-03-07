---
name: jack-workflow-automate-content-midjourney-google-docs
description: >-
  Automates content creation by fetching RSS feed, generating images with
  Midjourney, and adding content to Google Docs.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - automation
  - midjourney
  - content creation
  - google docs
  - rss
  - openai
triggers:
  - When you need to automate content creation from RSS feeds.
  - When you want to generate images and add them to Google Docs automatically.
allowed-tools: []
compatibility: 'make.com, openai, userapi.ai, google docs'
metadata:
  source: jack-school
  lesson: 11
  lesson_title: Heads-up
  difficulty: hard
  category: content
  tools_required:
    - make.com
    - openai
    - userapi.ai
    - google docs
  estimated_setup_time: 1hr
  extracted_from:
    - 1_3 midjourney .json
    - 2_3 midjourney .json
    - 3_3 midjourney .json
---

# Workflow Automate Content Midjourney Google Docs

## When to Use

Use this skill when you need to:
- When you need to automate content creation from RSS feeds.
- When you want to generate images and add them to Google Docs automatically.

## What This Does

Automates content creation by fetching RSS feed, generating images with Midjourney, and adding content to Google Docs.

## Workflow

This bundles three Make.com scenarios:
1. **Create (1_3 midjourney .json):** Reads RSS, extracts HTML, uses OpenAI to generate LinkedIn post and Midjourney prompt, adds the post to Google Docs, and calls UserAPI to imagine the image.
2. **Generate (2_3 midjourney .json):** Receives webhook with 4 images, upscales the image selected by user.
3. **Upscaler (3_3 midjourney .json):**  Receives webhook, adds upscaled image to Google Docs.

## Configuration

**Required tools/platforms:**
- make.com
- openai
- userapi.ai
- google docs

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
