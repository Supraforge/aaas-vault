---
name: jack-nocode-string-replacement
description: >-
  String replace function to clean text from various special characters in
  Make.com
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - make.com
  - string manipulation
  - text cleaning
  - automation
triggers:
  - when cleaning text data in make.com
  - when special characters are interfering with workflow
allowed-tools: []
compatibility: make.com
metadata:
  source: jack-school
  lesson: 65
  lesson_title: Automate Anything with AI Agents... Zero Code
  difficulty: easy
  category: nocode
  tools_required:
    - make.com
  estimated_setup_time: 5min
---

# Nocode String Replacement

## When to Use

Use this skill when you need to:
- when cleaning text data in make.com
- when special characters are interfering with workflow

## What This Does

String replace function to clean text from various special characters in Make.com

## Workflow

{{replace(replace(replace(replace(replace(replace(replace(32.text; "/\n/g"; space); "/\r/g"; space); "/\t/g"; space); "/\f/g"; space); "/\//g"; "/"); "/\\/g"; "\\"); "/\"/g"; "\"")}}

## Configuration

**Required tools/platforms:**
- make.com

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
