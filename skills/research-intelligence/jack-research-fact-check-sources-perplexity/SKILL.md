---
name: jack-research-fact-check-sources-perplexity
description: >-
  Fact-checks and adds/corrects sources for a list of bullet points using
  Perplexity AI, ensuring accuracy and proper citation.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - fact-check
  - sources
  - research
  - perplexity
  - bullet points
triggers:
  - When you need to verify facts and add sources to a list.
  - To ensure the accuracy of information before using it.
allowed-tools: []
compatibility: perplexity
metadata:
  source: jack-school
  lesson: 30
  lesson_title: Tools
  difficulty: medium
  category: research
  tools_required:
    - perplexity
  estimated_setup_time: 5min
  extracted_from:
    - Research_B_.txt
---

# Research Fact Check Sources Perplexity

## When to Use

Use this skill when you need to:
- When you need to verify facts and add sources to a list.
- To ensure the accuracy of information before using it.

## What This Does

Fact-checks and adds/corrects sources for a list of bullet points using Perplexity AI, ensuring accuracy and proper citation.

## Workflow

Please analyze the following output from the previous model:

{{7.choices[].message.content}}

For each bullet point in the output, perform the following tasks:

1. Check if the bullet point has a source URL.
   - If a source URL is missing, attempt to find a relevant and reliable source that supports the information provided.
   - If a source URL is found, include it alongside the bullet point.
- You MUST include the naked url for every source
   - If no reliable source can be found, remove the bullet point from the list.

2. Fact-check the information in each bullet point.
   - Verify the accuracy of the claims made using reliable sources and fact-checking techniques.
   - If any information is found to be inaccurate, correct it or remove the bullet point if it cannot be corrected.

3. Maintain the original format of the output, including the emoji bullet points and headers.

4. For each bullet point that passes the fact-check, include the source URL(s) used to verify the information.

5. Do not include any further information in your answer than the list. You must use one emoji per number, do not use mark down by using '**' 

6. You can only provide the output an no further information, such as 'sure, here's the updated list you asked for'. Do not add aniy addtional copy before or after the 10 facts such as 'here are the facts you asked for'

You MUST include the naked url for every source

Please provide the updated output with fact-checked information, source URLs, and any necessary corrections, while keeping the emoji bullet points and headers intact.

## Configuration

**Required tools/platforms:**
- perplexity

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
