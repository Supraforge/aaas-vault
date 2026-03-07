---
name: jack-leadgen-website-summary-gpt
description: >-
  Generates a concise website summary (35 words) and lists 5 core features using
  GPT for lead qualification.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - lead qualification
  - website analysis
  - gpt
  - summary generation
triggers:
  - when you need a quick website overview
  - when qualifying leads based on website content
allowed-tools: []
compatibility: 'openai, chatgpt'
metadata:
  source: jack-school
  lesson: 33
  lesson_title: Tools
  difficulty: medium
  category: leadgen
  tools_required:
    - openai
    - chatgpt
  estimated_setup_time: 5min
  extracted_from:
    - Snappy_Website_Summary_.txt
---

# Leadgen Website Summary Gpt

## When to Use

Use this skill when you need to:
- when you need a quick website overview
- when qualifying leads based on website content

## What This Does

Generates a concise website summary (35 words) and lists 5 core features using GPT for lead qualification.

## Workflow

You will be provided with the copy of a website. Your task is to carefully read and comprehend the content of the website. After analyzing the text, generate a concise summary of the key points and main ideas discussed in the website. The summary should be informative, helpful, and to the point, with a maximum length of 35 words.

When creating the summary, focus on the following aspects:

- Identify the core message or theme of the website.
- Highlight the most important facts, statistics, or examples that support the main points.
- If applicable, briefly mention any significant conclusions or recommendations made in the website.

Avoid using unnecessary fluff or filler phrases, and do not include introductory phrases like "this website is about." Instead, concentrate on directly communicating the essential information in a clear and efficient manner.

To ensure your summary is effective, consider the following tips:

- Use concise and precise language to convey the key ideas.
- Prioritize information based on its relevance to the main message.
- Ensure that the summary can be easily understood by someone who hasn't seen the website.
- Read through your summary to check for clarity, coherence, and adherence to the 35-word limit.

Remember, your goal is to provide a comprehensive yet succinct overview of the website's content, enabling readers to quickly grasp the core message and main takeaways. Do not repeat the title.

Then, write 5 core features about the website in bullets

* 📝 fact 1
* 🔍 fact 2
* 📊 fact 3
* 💡 fact 4
* ⚡ fact 5

The website copy: {{website_content}}

## Configuration

**Required tools/platforms:**
- openai
- chatgpt

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
