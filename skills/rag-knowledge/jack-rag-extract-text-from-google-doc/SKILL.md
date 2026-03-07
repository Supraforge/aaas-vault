---
name: jack-rag-extract-text-from-google-doc
description: >-
  Extracts text content from a Google Docs file using DumplingAI and returns it
  as plain text.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - google docs
  - dumplingai
  - text extraction
  - automation
triggers:
  - When you need to extract text from a Google Docs file automatically.
allowed-tools: []
compatibility: 'make.com, google drive, dumplingai'
metadata:
  source: jack-school
  lesson: 61
  lesson_title: Steal This AI Client Intelligence System... WOW
  difficulty: medium
  category: rag
  tools_required:
    - make.com
    - google drive
    - dumplingai
  estimated_setup_time: 30min
  extracted_from:
    - "[1_3] Company Information\U0001F4A1.json"
---

# Rag Extract Text From Google Doc

## When to Use

Use this skill when you need to:
- When you need to extract text from a Google Docs file automatically.

## What This Does

Extracts text content from a Google Docs file using DumplingAI and returns it as plain text.

## Workflow

This Make.com module watches a Google Drive folder, gets the file, converts it to text using DumplingAI, and sets the extracted text as a variable.

## Configuration

**Required tools/platforms:**
- make.com
- google drive
- dumplingai

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
