---
name: jack-sales-whatsapp-agent
description: >-
  Automates WhatsApp customer service and sales conversations using an AI agent
  connected to Unipile and n8n.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - whatsapp
  - sales
  - customer service
  - automation
  - n8n
  - unipile
  - ai agent
triggers:
  - When a new WhatsApp message is received via Unipile
  - To provide automated customer service or sales assistance on WhatsApp
allowed-tools: []
compatibility: 'n8n, Unipile, OpenAI API Key'
metadata:
  source: jack-school
  lesson: 105
  lesson_title: 99% are STILL Ignoring WhatsApp Agents
  difficulty: hard
  category: sales
  tools_required:
    - n8n
    - Unipile
    - OpenAI API Key
  estimated_setup_time: 1hr
  extracted_from:
    - "\U0001F525 WhatsApp Operating System.json"
---

# Sales Whatsapp Agent

## When to Use

Use this skill when you need to:
- When a new WhatsApp message is received via Unipile
- To provide automated customer service or sales assistance on WhatsApp

## What This Does

Automates WhatsApp customer service and sales conversations using an AI agent connected to Unipile and n8n.

## Workflow

This n8n workflow manages customer service in WhatsApp and automates sales conversations using an AI agent. It uses a webhook to receive messages from Unipile, extracts chat ID and message content, then feeds this information to an AI agent. The AI agent, configured with a system message for a WhatsApp agent role, formulates a response. Finally, the AI agent's response is sent back to the user via Unipile.

## Configuration

**Required tools/platforms:**
- n8n
- Unipile
- OpenAI API Key

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
