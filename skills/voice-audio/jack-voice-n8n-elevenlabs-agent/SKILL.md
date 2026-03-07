---
name: jack-voice-n8n-elevenlabs-agent
description: >-
  Creates a voice agent using n8n and ElevenLabs to automate real-time
  interactions like appointment scheduling and email responses.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - n8n
  - elevenlabs
  - voice agent
  - automation
  - webhook
  - calendar
  - email
triggers:
  - when a voice command is received via webhook
  - when you need to automate appointment scheduling
allowed-tools: []
compatibility: 'n8n, elevenlabs'
metadata:
  source: jack-school
  lesson: 78
  lesson_title: How to Build Voice Agents with n8n + Elevenlabs
  difficulty: hard
  category: voice
  tools_required:
    - n8n
    - elevenlabs
  estimated_setup_time: 1hr
  extracted_from:
    - ____Build_Voice_Agents_with_n8n___Elevenlabs (2).json
---

# Voice N8n Elevenlabs Agent

## When to Use

Use this skill when you need to:
- when a voice command is received via webhook
- when you need to automate appointment scheduling

## What This Does

Creates a voice agent using n8n and ElevenLabs to automate real-time interactions like appointment scheduling and email responses.

## Workflow

The provided n8n workflow JSON configures an AI voice agent with webhook triggers, ElevenLabs voice synthesis, and calendar/email automation.

## Configuration

**Required tools/platforms:**
- n8n
- elevenlabs

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
