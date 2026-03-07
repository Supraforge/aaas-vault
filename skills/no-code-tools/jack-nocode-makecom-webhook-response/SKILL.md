---
name: jack-nocode-makecom-webhook-response
description: >-
  Generates HTML code for webhook responses in Make.com to display expert
  responses in a chat format.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - Make.com
  - Webhooks
  - HTML
triggers:
  - Automating responses in Make.com
  - Generating dynamic content based on received data
allowed-tools: []
compatibility: 'Make.com, OpenAI, Claude'
metadata:
  source: jack-school
  lesson: 36
  lesson_title: This AI Meeting Automation 100Xs Your Productivity
  difficulty: medium
  category: nocode
  tools_required:
    - Make.com
    - OpenAI
    - Claude
  estimated_setup_time: 30min
  extracted_from:
    - PROMPTS_FROM_VIDEO.txt
---

# Nocode Makecom Webhook Response

## When to Use

Use this skill when you need to:
- Automating responses in Make.com
- Generating dynamic content based on received data

## What This Does

Generates HTML code for webhook responses in Make.com to display expert responses in a chat format.

## Workflow

I am using make.com and webhooks to send and receive data.
I have recieved the data from the website sucessfully. I know need to send the data back to the website with the responses for the chat.
Please do three things:
1) Create html code for the webhook response in make.com
Here are the inputs: 
Expert 1: {{29.role_1}}
Expert 2: {{29.role_2}}
Expert 3:{{29.role_3}}
Expert 1's response:{{30.textResponse}}
Expert 2's response: {{31.result}}
Expert 3's response{{32.choices[].message.content}}
2) Amend the html code and paste it in full, so that it can recieve the data from make and then present those answers in the whatsapp style chat. please include the expert's name
3)  clarify if we need any headers for key and value in make

## Configuration

**Required tools/platforms:**
- Make.com
- OpenAI
- Claude

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
