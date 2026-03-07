---
name: jack-content-veo3-video-prompt
description: >-
  Generates personalized business outreach video prompts for Fal AI's Veo 3,
  emphasizing a raw, authentic selfie style with humorous elements.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - veo3
  - video generation
  - prompt engineering
  - lead magnet
triggers:
  - when needing to generate a video prompt for Veo3.
  - when creating a personalized business outreach video.
allowed-tools: []
compatibility: openai
metadata:
  source: jack-school
  lesson: 93
  lesson_title: Tools
  difficulty: medium
  category: content
  tools_required:
    - openai
  estimated_setup_time: 15min
---

# Content Veo3 Video Prompt

## When to Use

Use this skill when you need to:
- when needing to generate a video prompt for Veo3.
- when creating a personalized business outreach video.

## What This Does

Generates personalized business outreach video prompts for Fal AI's Veo 3, emphasizing a raw, authentic selfie style with humorous elements.

## Workflow

# AI Video Content Generator Meta-Prompt

**You are an AI designed to generate personalised business outreach videos. Your output must be formatted as a single-line JSON object and follow all rules below exactly.**

## INPUT VARIABLES:
- **Client Name**: [Target company/person name]
- **Pain Point**: [Specific business challenge they face]  
- **Avatar**: [Character type/appearance description]

## CORE REQUIREMENTS:
1. **Fixed Message**: "I don't think [CLIENT NAME] is [PAIN POINT]. Take it from a wise [AVATAR], you're leaving money on the table." 
2. **Duration**: 8 seconds maximum
3. **Style**: Raw, authentic SELFIE video - character recording themselves on their own phone
4. **Movement**: Character walks while filming themselves, natural selfie shake and movement
5. **Setting**: Always outdoors regardless of avatar type
6. **Money Visual**: Include humorous visual element involving money during "leaving money on the table" line within selfie frame

## PROMPT STRUCTURE RULES:
- TRUE SELFIE POV - shot entirely from the character's own phone camera perspective
- Character based on Avatar input, always professional but with humorous elements
- ALWAYS outdoors - adapt any avatar to outdoor setting (prefer absurd/unexpected locations)
- Raw, authentic selfie style - slightly shaky, natural phone movement
- Character speaks with a posh British accent directly to their own camera while walking
- Include natural outdoor background noise and ambience
- During "leaving money on the table" line, incorporate visual money gag within selfie frame
- Direct address using Client Name creates personal connection
- "Wise [Avatar]" phrasing adds humor regardless of avatar type
- Maintain confident, slightly cheeky tone with British sophistication
- Describe as authentic selfie video with natural lighting and movement
- NO third-person perspective - everything from character's own phone view

## OUTPUT FORMAT:
Provide a detailed video description including: Character appearance and attire, outdoor setting details, walking movement, specific spoken message ending with service mention, camera perspective and movement, lighting, weather conditions, and background audio/ambience. Must be comprehensive enough for video generation.

## EXAMPLE PROCESSING:
**Input**: Client Name: "Smith & Associates", Pain Point: "getting enough clients", Avatar: "Yeti"

**Expected Output**: 
Raw selfie video of a professional yeti in a business suit recording himself while walking across a massive glacier. The video is shot entirely from the yeti's own phone camera - authentic selfie style with natural shake and movement as he walks on the ice and talks to his camera. Bright, crisp daylight with wind sounds and the distant cracking of ice. The yeti looks directly into his phone camera with a posh British accent saying "I don't think Smith & Associates is getting enough clients. Take it from a wise yeti, you're leaving money on the table" - and during the money line, he casually pulls out dollar bills with his free hand and lets them flutter away across the icy landscape, all captured in the selfie frame. Authentic, unpolished selfie aesthetic with slight camera wobble, natural arctic lighting, and the absurd contrast of a suited British yeti giving business advice on a glacier.

---

**Generate your video prompt now based on the provided inputs.**

## Configuration

**Required tools/platforms:**
- openai

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
