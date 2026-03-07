---
name: jack-rag-perplexity-fact-check-prompt
description: >-
  Prompt for Perplexity AI to fact-check a statement, providing a verdict,
  confidence score, findings, and source summaries from reputable sources.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - fact-checking
  - perplexity
  - verification
  - ai
triggers:
  - When you need to fact-check a statement from a URL.
  - To verify the accuracy of a claim with supporting evidence.
allowed-tools: []
compatibility: perplexity
metadata:
  source: jack-school
  lesson: 41
  lesson_title: This AI Co-Pilot Will Fact Check ANYTHING
  difficulty: medium
  category: rag
  tools_required:
    - perplexity
  estimated_setup_time: 5min
---

# Rag Perplexity Fact Check Prompt

## When to Use

Use this skill when you need to:
- When you need to fact-check a statement from a URL.
- To verify the accuracy of a claim with supporting evidence.

## What This Does

Prompt for Perplexity AI to fact-check a statement, providing a verdict, confidence score, findings, and source summaries from reputable sources.

## Workflow

I found a statement on {{1.url}} that claims '{{1.text}}.' I need a detailed fact-check report on this claim, and I would like you to source up to three additional examples that either support or refute this information. The report should include:

1. **Claim:**  
   Restate the specific fact or statement being checked.

2. **Verdict:**  
   Provide one of the following verdicts based on your findings: 🟢 True, 🔴 False, ⚫️ Misleading, or 🟣 Unverifiable.

3. **Confidence Score:**  
   Assign a confidence score between 1-10, where 10 indicates high confidence in the verdict and 1 indicates low confidence. include a brief explainatiof on why in brackets next to the number (no more than 12 words).

4. **Findings:**  
   Offer further context or information about the claim, including its origin, any reasons it might be misunderstood, and how experts view it. Limit this section to a maximum of 200 words.

5. **Source Summary:**  
   Identify up to three new credible sources that verify the claim. Provide a brief summary of the findings from each source, ensuring that they are distinct from the original link provided. Include:
   - The name of each source (e.g., a scientific journal, reputable news outlet, expert organization). This cannot be reddit
- You must not use the same website you are provided here: {{1.url}}
- You must search the claim on the internet and find reputatable sources to assess the veracity of the claim.
   - A brief description of what the source says about the claim.
   - A direct, clickable hyperlink to the full article.

Please ensure the output follows this format:
- **Numbered headers** are bold, like '1. **Claim:**'
- **Links** are provided as **clickable hyperlinks**.

## Configuration

**Required tools/platforms:**
- perplexity

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
