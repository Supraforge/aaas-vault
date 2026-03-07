---
name: jack-content-midjourney-prompt
description: >-
  Generates Midjourney prompts from text by identifying the subject, action,
  setting, and details, then formatting them into a specific prompt structure.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - midjourney
  - prompt engineering
  - image generation
triggers:
  - when generating image prompts from descriptive text
  - when needing a structured Midjourney prompt
allowed-tools: []
compatibility: openai
metadata:
  source: jack-school
  lesson: 13
  lesson_title: Heads-up
  difficulty: medium
  category: content
  tools_required:
    - openai
  estimated_setup_time: 15min
  extracted_from:
    - Midjourney_Prompt_.txt
---

# Content Midjourney Prompt

## When to Use

Use this skill when you need to:
- when generating image prompts from descriptive text
- when needing a structured Midjourney prompt

## What This Does

Generates Midjourney prompts from text by identifying the subject, action, setting, and details, then formatting them into a specific prompt structure.

## Workflow

1. You will receive text data about a topic or post. Analyze this text to identify key elements such as the subject, action, setting, and additional details.
2. Use the information extracted from the text to fill in the following Midjourney prompt template:
[subject], [action], [setting], [additional details]. The image must be natural, realistic, in 2018, style raw, 8K, taken on iPhone, --ar 16:9
- [subject] should be the main focus of the image, like a person, object, creature, or concept. Be as specific as possible.
- [action] should describe what the subject is doing using active, descriptive verbs.
- [setting] should paint a vivid picture of the location, background, or environment surrounding the subject.
- [additional details] can include extra elements to enhance the image, such as clothing, colors, lighting, composition, or artistic references.
3. Always end the generated prompt with the exact phrase: "The image must be natural, realistic, in 2018, style raw, 8K, taken on iPhone, --ar 16:9"
4. Ensure that the final prompt is well-formatted and includes all the necessary components. Avoid incomplete or poorly structured prompts.
5. Output the complete Midjourney prompt, ready for use.

Example input text:
"In the heart of a dense forest, a majestic stag stands alert, its antlers glistening in the dappled sunlight filtering through the canopy. The rich earthy hues of the foliage create a vivid backdrop for the striking creature."

Example output prompt:
A majestic stag standing alert in the heart of a dense forest, antlers glistening in dappled sunlight, rich earthy hues of foliage creating a vivid backdrop. The image must be natural, realistic, in 2018, style raw, 8K, taken on iPhone, --ar 16:9

## Configuration

**Required tools/platforms:**
- openai

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
