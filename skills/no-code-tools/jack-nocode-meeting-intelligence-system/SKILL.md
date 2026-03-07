---
name: jack-nocode-meeting-intelligence-system
description: >-
  Procedure to make every meeting actionable using AI to extract key decisions
  and action items.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - meeting
  - automation
  - task management
  - AI
triggers:
  - when analyzing meeting recordings
  - to automate task creation from meetings
allowed-tools: []
compatibility: 'notebooklm, antigravity'
metadata:
  source: jack-school
  lesson: 128
  lesson_title: NotebookLM just got 10X better (AntiGravity)
  difficulty: medium
  category: nocode
  tools_required:
    - notebooklm
    - antigravity
  estimated_setup_time: 1hr
  extracted_from:
    - NotebookLMjustgot10Xbetter.txt
---

# Nocode Meeting Intelligence System

## When to Use

Use this skill when you need to:
- when analyzing meeting recordings
- to automate task creation from meetings

## What This Does

Procedure to make every meeting actionable using AI to extract key decisions and action items.

## Workflow

Meeting recording uploaded
        ↓
NotebookLM extracts:
  → Key decisions
  → Action items
  → Follow-up questions
        ↓
Generates:
  → Meeting summary (briefing doc)
  → Task list (data table)
  → Visual recap (infographic)
        ↓
AntiGravity:
  → Creates tasks in project manager
  → Sends summary to attendees
  → Schedules follow-ups

## Configuration

**Required tools/platforms:**
- notebooklm
- antigravity

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
