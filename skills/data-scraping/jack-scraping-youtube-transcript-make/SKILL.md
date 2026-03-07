---
name: jack-scraping-youtube-transcript-make
description: >-
  Scrape YouTube video transcripts using Make.com by extracting the transcript
  link from the HTML source.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - youtube
  - scraping
  - transcript
  - automation
triggers:
  - when you need to automatically extract transcript data from a YouTube video
  - when 0CodeKit is not working
allowed-tools: []
compatibility: make.com
metadata:
  source: jack-school
  lesson: 27
  lesson_title: 10 Levels of AI Automation
  difficulty: medium
  category: scraping
  tools_required:
    - make.com
  estimated_setup_time: 30min
  extracted_from:
    - blueprint(2).json
---

# Scraping Youtube Transcript Make

## When to Use

Use this skill when you need to:
- when you need to automatically extract transcript data from a YouTube video
- when 0CodeKit is not working

## What This Does

Scrape YouTube video transcripts using Make.com by extracting the transcript link from the HTML source.

## Workflow

Make.com blueprint to retrieve YouTube transcripts by scraping the video page HTML, finding the transcript link, and fetching the transcript data.

## Configuration

**Required tools/platforms:**
- make.com

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
