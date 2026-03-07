---
name: jack-content-expert-panel-json-structure
description: >-
  Defines the JSON structure for creating an AI expert panel, specifying roles
  and areas of expertise.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - AI
  - expert panel
  - JSON
  - data structure
triggers:
  - When designing an AI system that uses multiple experts
  - When structuring data for panel discussions
allowed-tools: []
compatibility: JSON editor
metadata:
  source: jack-school
  lesson: 36
  lesson_title: This AI Meeting Automation 100Xs Your Productivity
  difficulty: easy
  category: content
  tools_required:
    - JSON editor
  estimated_setup_time: 5min
---

# Content Expert Panel Json Structure

## When to Use

Use this skill when you need to:
- When designing an AI system that uses multiple experts
- When structuring data for panel discussions

## What This Does

Defines the JSON structure for creating an AI expert panel, specifying roles and areas of expertise.

## Workflow

```json
{
  "question": "[INSERT ORIGINAL QUESTION]",
  "role_1": "[INSERT ROLE 1]",
  "expertise_1": "[INSERT BRIEF, SPECIFIC DESCRIPTION OF EXPERTISE]",
  "role_2": "[INSERT ROLE 2]",
  "expertise_2": "[INSERT BRIEF, SPECIFIC DESCRIPTION OF EXPERTISE]",
  "role_3": "[INSERT ROLE 3]",
  "expertise_3": "[INSERT BRIEF, SPECIFIC DESCRIPTION OF EXPERTISE]"
}
```

## Configuration

**Required tools/platforms:**
- JSON editor

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
