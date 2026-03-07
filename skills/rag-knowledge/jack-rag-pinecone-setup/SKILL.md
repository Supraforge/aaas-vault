---
name: jack-rag-pinecone-setup
description: >-
  Initialize a Pinecone vector database to store and retrieve business context
  for AI co-pilots, enabling long-term memory and improved decision-making.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - rag
  - vector database
  - pinecone
  - ai copilot
triggers:
  - when setting up long-term memory for an AI agent
  - when building a RAG application
allowed-tools: []
compatibility: pinecone
metadata:
  source: jack-school
  lesson: 122
  lesson_title: How to Use AntiGravity Better than 99% of People
  difficulty: medium
  category: rag
  tools_required:
    - pinecone
  estimated_setup_time: 30min
---

# Rag Pinecone Setup

## When to Use

Use this skill when you need to:
- when setting up long-term memory for an AI agent
- when building a RAG application

## What This Does

Initialize a Pinecone vector database to store and retrieve business context for AI co-pilots, enabling long-term memory and improved decision-making.

## Workflow

1. Create a Pinecone account.
2. Create a new Pinecone index with dimensions appropriate for your embeddings.
3. Configure your application to connect to Pinecone using your API key and environment.

## Configuration

**Required tools/platforms:**
- pinecone

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
