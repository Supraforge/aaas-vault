---
name: jack-research-perplexity-summary
description: >-
  Use Perplexity AI to summarize content from a URL, extract key insights, and
  gather additional research data points.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - research
  - summarization
  - perplexity
  - url analysis
triggers:
  - When you need to quickly understand the key points of a web page or document
  - >-
    When you need to gather additional research insights related to the content
    of a URL
allowed-tools: []
compatibility: perplexity.ai
metadata:
  source: jack-school
  lesson: 1
  lesson_title: How to Create FULLY Autonomous AI Research Agents
  difficulty: medium
  category: research
  tools_required:
    - perplexity.ai
  estimated_setup_time: 15min
  extracted_from:
    - Perplexity_Prompt_.txt
---

# Research Perplexity Summary

## When to Use

Use this skill when you need to:
- When you need to quickly understand the key points of a web page or document
- When you need to gather additional research insights related to the content of a URL

## What This Does

Use Perplexity AI to summarize content from a URL, extract key insights, and gather additional research data points.

## Workflow

Context: You are a summarization expert who identifies salient aspects of content from URLs. You will summarize the URL and complete further research on the topic to provide data points.
Actions: Read through the post. Improve clarity, language, and grammar; if not in first person, make it so. Keep the interesting parts. Summarize comments including reactions and advice (max 100 words), labeled 'perspective'. Provide 3 insights/data points, labeled 'data' (list your sources).

## Configuration

**Required tools/platforms:**
- perplexity.ai

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
