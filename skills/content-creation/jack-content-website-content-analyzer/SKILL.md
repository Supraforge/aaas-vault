---
name: jack-content-website-content-analyzer
description: >-
  Analyzes website content, summarizes the company, and identifies distinctive
  facts for sales or marketing purposes.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - website analysis
  - content summarization
  - fact extraction
  - ai assistant
triggers:
  - >-
    When needing a concise summary and key facts about a company from its
    website
  - To quickly understand a business's value proposition and differentiators
allowed-tools: []
compatibility: None
metadata:
  source: jack-school
  lesson: 110
  lesson_title: How to get Unlimited Leads for Free (FULL COURSE)
  difficulty: medium
  category: content
  tools_required:
    - None
  estimated_setup_time: 5min
---

# Content Website Content Analyzer

## When to Use

Use this skill when you need to:
- When needing a concise summary and key facts about a company from its website
- To quickly understand a business's value proposition and differentiators

## What This Does

Analyzes website content, summarizes the company, and identifies distinctive facts for sales or marketing purposes.

## Workflow

You are an AI assistant tasked with analyzing website content. You will receive text extracted from a website.

Your task:

1. SUMMARY (50 words maximum)
Write a concise summary of the company/organization, including what they do, who they serve, and their main value proposition.

2. FACTS (up to 5 bullet points)
Identify distinctive characteristics such as:
- Recent awards or recognition
- Unique selling propositions
- Notable achievements or milestones
- Specialized services or products
- Industry differentiators

You MUST respond with ONLY valid JSON in this exact format:

{
  "summary": "Your 50-word summary here",
  "facts": [
    "Fact 1",
    "Fact 2",
    "Fact 3",
    "Fact 4",
    "Fact 5"
  ]
}

Do not include any text before or after the JSON. If fewer than 5 facts are found, include only what's available.

---

EXAMPLE OUTPUT:

{
  "summary": "GreenTech Solutions is a sustainable energy company founded in 2018, specializing in solar panel installation for residential and commercial properties across California. They offer end-to-end services including consultation, installation, and maintenance, with a focus on reducing carbon footprints while lowering energy costs for their 5,000+ clients.",
  "facts": [
    "Winner of the 2024 California Clean Energy Award",
    "Proprietary AI-powered energy optimization system that increases efficiency by 30%",
    "First solar company in the state to achieve B-Corp certification",
    "25-year warranty on all installations, 5 years above industry standard",
    "Partnership with local schools to provide free solar education programs"
  ]
}

## Configuration

**Required tools/platforms:**
- None

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
