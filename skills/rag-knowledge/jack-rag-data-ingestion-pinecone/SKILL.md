---
name: jack-rag-data-ingestion-pinecone
description: >-
  Create a data ingestion pipeline to store meeting transcripts, emails, and
  documents in Pinecone for chat-based querying.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - rag
  - data ingestion
  - pinecone
  - n8n
  - chatbots
triggers:
  - Need to query across multiple data sources
  - Want a chat interface to access company knowledge
allowed-tools: []
compatibility: 'n8n, Pinecone, Fireflies.ai'
metadata:
  source: jack-school
  lesson: 104
  lesson_title: Tools
  difficulty: hard
  category: rag
  tools_required:
    - n8n
    - Pinecone
    - Fireflies.ai
  estimated_setup_time: 1hr
---

# Rag Data Ingestion Pinecone

## When to Use

Use this skill when you need to:
- Need to query across multiple data sources
- Want a chat interface to access company knowledge

## What This Does

Create a data ingestion pipeline to store meeting transcripts, emails, and documents in Pinecone for chat-based querying.

## Workflow

1. Connect Fireflies.ai (or similar) for meeting transcripts.
2. Connect Google Drive/Outlook to n8n for document access.
3. Connect Pinecone to n8n for vector storage.
4. Upload the provided n8n blueprint.
5. Grab Fireflies API key and configure.
6. Expose a public URL to enable chat interface.

## Configuration

**Required tools/platforms:**
- n8n
- Pinecone
- Fireflies.ai

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
