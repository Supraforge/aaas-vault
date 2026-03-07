---
name: jack-rag-customer-query-chatbot
description: >-
  Build a chatbot that answers customer queries by leveraging uploaded documents
  and Pinecone for knowledge retrieval.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - rag
  - customer support
  - chatbot
  - n8n
  - pinecone
  - hugging face
  - loveable
triggers:
  - Need to automate customer support
  - Want to provide instant answers to customer queries
allowed-tools: []
compatibility: 'n8n, Pinecone, Hugging Face, Loveable'
metadata:
  source: jack-school
  lesson: 104
  lesson_title: Tools
  difficulty: hard
  category: rag
  tools_required:
    - n8n
    - Pinecone
    - Hugging Face
    - Loveable
  estimated_setup_time: 1hr
---

# Rag Customer Query Chatbot

## When to Use

Use this skill when you need to:
- Need to automate customer support
- Want to provide instant answers to customer queries

## What This Does

Build a chatbot that answers customer queries by leveraging uploaded documents and Pinecone for knowledge retrieval.

## Workflow

1. Upload n8n blueprint.
2. Gather relevant documents.
3. Connect Pinecone to n8n.
4. Obtain a Hugging Face API token.
5. Follow the tutorial for setup.
6. Create a chat interface on Loveable using the provided prompt.
7. Connect the Loveable webhook to the n8n scenario.

## Configuration

**Required tools/platforms:**
- n8n
- Pinecone
- Hugging Face
- Loveable

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
