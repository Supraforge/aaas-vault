---
name: jack-sales-proposal-from-meeting
description: >-
  Generate a client proposal draft from meeting notes, including discussed
  points, desired outcomes, and pricing, ready for customization.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - sales
  - proposal
  - automation
  - client communication
triggers:
  - >-
    After a client meeting to summarize the key discussion points and proposed
    solutions
  - When creating a proposal based on client conversation
allowed-tools: []
metadata:
  source: jack-school
  lesson: 63
  lesson_title: Tools
  difficulty: easy
  category: sales
  estimated_setup_time: 5min
  extracted_from:
    - "\U0001F525 Meeting to PDF Bonus Resources.txt"
compatibility: 'agent-zero, claude-code, cursor'
---

# Sales Proposal From Meeting

## When to Use

Use this skill when you need to:
- After a client meeting to summarize the key discussion points and proposed solutions
- When creating a proposal based on client conversation

## What This Does

Generate a client proposal draft from meeting notes, including discussed points, desired outcomes, and pricing, ready for customization.

## Workflow

```
{{CLIENT NAME}} ({{CLIENT BUSINESS}})

Hey {{CLIENT NAME}}
Please see our below proposal, following our conversation.

💬 What we Discussed
{{WhatWeDiscussed}}

💎 What you’d like
{{ProjectOutcomes}}

📆 When for
{{WhenFor}}

🤩 Pricing
The quarterly fee is £20,000, paid in advance. This covers unlimited automation projects during each quarter. We don't limit the number or size of projects you can request. The fee includes all development work, testing, and implementation support needed to complete your automation initiatives. Our typical delivery capacity is one medium-sized automation project per month.

🔥 What next
Purchase here to secure your spot. Once your payment is processed, we'll schedule a kick-off call within 2 business days to discuss your first automation project. 

Yours Faithfully,
Jack Roberts
07498 XXX XXX
```

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
