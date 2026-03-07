---
name: jack-guidance-openai-data-formatting
description: Formats user information for a vector database search using OpenAI.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - openai
  - prompt
  - data formatting
  - vector database
  - client search
triggers:
  - When you need to format client data for a vector database search.
allowed-tools: []
compatibility: openai
metadata:
  source: jack-school
  lesson: 61
  lesson_title: Steal This AI Client Intelligence System... WOW
  difficulty: medium
  category: guidance
  tools_required:
    - openai
  estimated_setup_time: 15min
  extracted_from:
    - "[3_3] Personal Delivery System \U0001F4C8.json"
---

# Guidance Openai Data Formatting

## When to Use

Use this skill when you need to:
- When you need to format client data for a vector database search.

## What This Does

Formats user information for a vector database search using OpenAI.

## Workflow

You will be given a user's information, you will format this for a search on a vector database. in json format.

**Please respond in JSON format as shown below:**

{
  "search_term": ""
}

**Guidelines:**
- simply provide the user information, name and email
---

**Example Response:**

{
  "search_term": "Johnathon Singh, jonniboy3737@outlook.com"
}

---

This is the user name: {{3.`Name 👋`}} 
This it he user's email: {{3.`Email 📧`}}

## Configuration

**Required tools/platforms:**
- openai

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
