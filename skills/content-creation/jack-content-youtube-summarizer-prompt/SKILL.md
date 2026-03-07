---
name: jack-content-youtube-summarizer-prompt
description: >-
  ChatGPT prompt to summarize YouTube transcripts, format the output, and
  extract key takeaways.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - youtube
  - summarization
  - prompt engineering
  - chatgpt
  - takeaways
triggers:
  - >-
    When creating a prompt for summarizing YouTube transcripts in a consistent
    and structured way.
  - >-
    When you need to extract both a summary and key takeaways from transcript
    data.
allowed-tools: []
compatibility: openai
metadata:
  source: jack-school
  lesson: 40
  lesson_title: AI-Powered Chrome Extensions Change Everything
  difficulty: medium
  category: content
  tools_required:
    - openai
  estimated_setup_time: 5min
---

# Content Youtube Summarizer Prompt

## When to Use

Use this skill when you need to:
- When creating a prompt for summarizing YouTube transcripts in a consistent and structured way.
- When you need to extract both a summary and key takeaways from transcript data.

## What This Does

ChatGPT prompt to summarize YouTube transcripts, format the output, and extract key takeaways.

## Workflow

"Summarize this YouTube transcript in 80 words or less. After the summary, create a list of key takeaways with each item starting with an emoji. Format the summary and the list with line breaks so that the summary is separated from the list. The summary is on its own separate lines. Each bullet point is on its own line. The summary should have one line break above and below it, and each bullet point should follow a similar spacing as shown in this example: Each bullet point should be on its own line, like this:

The video discusses a controversy involving Mr. Beast hiring an individual with a criminal history and addresses reactions from various parties, including Mr. Beast's ex-girlfriend and YouTuber Rosanna Pansino.

The video critiques the hiring decision and reflects on the lack of transparency and accountability.

🤐 Allegations of Mr. Beast knowingly hiring an offender.
🕵️‍♀️ Expose release sparks social media reactions
💔 Mr. Beast's ex-girlfriend criticizes trending pages
🛑 Rosanna Pansino talks about potential investigations
🤔 Questions about nicknaming conventions to hide identity
🗣️ Heated exchanges highlighting hypocrisy
📈 Debate on accountability and ethical hiring practices

Now, please use this format with the following transcript: {{1.transcript}}"

## Configuration

**Required tools/platforms:**
- openai

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
