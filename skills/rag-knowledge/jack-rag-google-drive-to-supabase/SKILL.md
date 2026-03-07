---
name: jack-rag-google-drive-to-supabase
description: >-
  Loads Google Drive files into Supabase vector store for RAG applications using
  n8n.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - n8n
  - rag
  - google drive
  - supabase
  - vector store
  - automation
triggers:
  - when a new file is created in a Google Drive folder
  - when building a RAG system with Google Drive documents
allowed-tools: []
compatibility: 'n8n, google drive, supabase, openai'
metadata:
  source: jack-school
  lesson: 102
  lesson_title: Tools
  difficulty: hard
  category: rag
  tools_required:
    - n8n
    - google drive
    - supabase
    - openai
  estimated_setup_time: 1hr
  extracted_from:
    - "\U0001F4B8 $100M Money Models.json"
---

# Rag Google Drive To Supabase

## When to Use

Use this skill when you need to:
- when a new file is created in a Google Drive folder
- when building a RAG system with Google Drive documents

## What This Does

Loads Google Drive files into Supabase vector store for RAG applications using n8n.

## Workflow

See the provided JSON file for the full n8n workflow.

## Configuration

**Required tools/platforms:**
- n8n
- google drive
- supabase
- openai

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
