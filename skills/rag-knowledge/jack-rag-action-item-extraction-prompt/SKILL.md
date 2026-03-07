---
name: jack-rag-action-item-extraction-prompt
description: >-
  Extracts action items, meeting name, and date from a meeting transcript using
  a specified format, listing action items per participant.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - meeting
  - action items
  - transcription
  - claude
  - summary
triggers:
  - >-
    when you need to create a clear, concise summary of action items from a
    meeting
  - when analyzing meeting transcripts
allowed-tools: []
compatibility: claude
metadata:
  source: jack-school
  lesson: 34
  lesson_title: This AI Meeting Automation 100Xs Your Productivity
  difficulty: medium
  category: rag
  tools_required:
    - claude
  estimated_setup_time: 5min
  extracted_from:
    - Action_Item_Extraction.txt
---

# Rag Action Item Extraction Prompt

## When to Use

Use this skill when you need to:
- when you need to create a clear, concise summary of action items from a meeting
- when analyzing meeting transcripts

## What This Does

Extracts action items, meeting name, and date from a meeting transcript using a specified format, listing action items per participant.

## Workflow

Analyze the provided meeting transcript and extract the meeting name, date, and action items for each participant. Format the output as follows:

💎 Meeting: [Meeting Name]
📆 Date: [Meeting Date]

[Participant's Name] Actions
• [Emoji] [Action description] (by [Deadline if specified])
• [Different Emoji] [Action description] (by [Deadline if specified])

Notes:
1. Start with the meeting name and date.
2. Use a different emoji for each action item.
3. Include deadlines in parentheses only if they are explicitly mentioned.
4. List all actions for one person before moving to the next.
5. Do not provide any additional output or explanations.

Example format:

💎 Meeting: Q4 Planning Session
📆 Date: October 15, 2024

Jack's Actions
• 👑 Complete project proposal (by Friday)
• 🌟 Schedule team meeting

Sarah's Actions
• 🚀 Research market trends
• 🔍 Present findings to leadership (by next Wednesday)

## Configuration

**Required tools/platforms:**
- claude

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
