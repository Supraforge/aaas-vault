---
name: jack-voice-telegram-transcribe
description: >-
  Transcribes Telegram voice messages using OpenAI's audio transcription
  service.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - telegram
  - voice
  - transcription
  - openai
  - n8n
triggers:
  - when a new voice message is sent to a Telegram bot
allowed-tools: []
compatibility: 'n8n, telegram, openai'
metadata:
  source: jack-school
  lesson: 67
  lesson_title: Automate Anything with AI Agents... Zero Code
  difficulty: medium
  category: voice
  tools_required:
    - n8n
    - telegram
    - openai
  estimated_setup_time: 30min
  extracted_from:
    - AI_Agent_Workflow (2).json
---

# Voice Telegram Transcribe

## When to Use

Use this skill when you need to:
- when a new voice message is sent to a Telegram bot

## What This Does

Transcribes Telegram voice messages using OpenAI's audio transcription service.

## Workflow

This n8n workflow triggers on a new Telegram voice message, retrieves the audio file, and transcribes it using OpenAI.

## Configuration

**Required tools/platforms:**
- n8n
- telegram
- openai

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
