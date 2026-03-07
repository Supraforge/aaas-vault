---
name: jack-content-rag-client-intelligence
description: >-
  Create a client intelligence system that retrieves data from websites, emails,
  and meetings, vectorizing it into a RAG-powered knowledge base.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - rag
  - client intelligence
  - automation
  - knowledge base
triggers:
  - When a new email is received
  - On a schedule
allowed-tools: []
compatibility: 'n8n, airtable, pinecone, firecrawl, fireflies.ai, openai'
metadata:
  source: jack-school
  lesson: 85
  lesson_title: What it does
  difficulty: hard
  category: content
  tools_required:
    - n8n
    - airtable
    - pinecone
    - firecrawl
    - fireflies.ai
    - openai
  estimated_setup_time: 1hr
  extracted_from:
    - ___n8n__Client_Intelligence_System.json
    - "\U0001F52E subagent magic.json"
---

# Content Rag Client Intelligence

## When to Use

Use this skill when you need to:
- When a new email is received
- On a schedule

## What This Does

Create a client intelligence system that retrieves data from websites, emails, and meetings, vectorizing it into a RAG-powered knowledge base.

## Workflow

See source files for full workflow.

## Configuration

**Required tools/platforms:**
- n8n
- airtable
- pinecone
- firecrawl
- fireflies.ai
- openai

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
