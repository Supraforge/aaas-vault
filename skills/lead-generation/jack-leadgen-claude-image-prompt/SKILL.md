---
name: jack-leadgen-claude-image-prompt
description: >-
  Generates a JSON payload with an image prompt based on a website's content,
  business name and setting.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - image generation
  - claude
  - lead generation
  - prompt engineering
triggers:
  - >-
    When you need to generate an image prompt based on a website's content to
    create personalized visuals.
  - >-
    When you want to automate the creation of image prompts for different
    businesses.
allowed-tools: []
compatibility: claude
metadata:
  source: jack-school
  lesson: 43
  lesson_title: Tools
  difficulty: medium
  category: leadgen
  tools_required:
    - claude
  estimated_setup_time: 15min
---

# Leadgen Claude Image Prompt

## When to Use

Use this skill when you need to:
- When you need to generate an image prompt based on a website's content to create personalized visuals.
- When you want to automate the creation of image prompts for different businesses.

## What This Does

Generates a JSON payload with an image prompt based on a website's content, business name and setting.

## Workflow

You will receive the contents of a homepage from a prospective client. Based on that information, you must do two things:

1) Determine an appropriate setting or background that relates to the client's business or industry.
2) Extract the client's business name from the homepage content.

Your output MUST be in the following JSON format only:

{
  "version": "a738942df15c8c788b076ddd052256ba7923aade687b12109ccc64b2c3483aa1",
  "input": {
    "prompt": "A photo of Jack in a professional, yet stylish suit looking at the camera, [BACKGROUND DESCRIPTION] holding up a sign that says '[BUSINESS NAME]'",
    "hf_loras": [
      "itsssssjack/KingJack-lora"
    ],
    "num_outputs": 4,
    "aspect_ratio": "16:9",
    "output_format": "png",
    "guidance_scale": 3.5,
    "output_quality": 100,
    "num_inference_steps": 28
  }
}

Replace [BACKGROUND DESCRIPTION], and [BUSINESS NAME] with the appropriate information based on the client's homepage content.

Do not include any explanations or additional text outside of this JSON structure. The output should be valid JSON that can be parsed directly.

THE TEXT: {{21.text}}

## Configuration

**Required tools/platforms:**
- claude

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
