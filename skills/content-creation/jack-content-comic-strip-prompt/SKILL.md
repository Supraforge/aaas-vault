---
name: jack-content-comic-strip-prompt
description: >-
  Generates a prompt for creating a 4-panel comic strip lead magnet, tailored to
  a specific brand using website analysis and logo integration.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - comic strip
  - lead magnet
  - AI automation
  - cartoon
  - cold outreach
triggers:
  - When creating a personalized comic strip for lead generation
  - When automating content creation with brand-specific visuals
allowed-tools: []
compatibility: 'OpenAI, n8n'
metadata:
  source: jack-school
  lesson: 82
  lesson_title: How to Automate UNSTOPPABLE Lead Magnets
  difficulty: medium
  category: content
  tools_required:
    - OpenAI
    - n8n
  estimated_setup_time: 30min
  extracted_from:
    - "\U0001F3A8 Comic Outreach Lead Magnet (4-Panel).txt"
---

# Content Comic Strip Prompt

## When to Use

Use this skill when you need to:
- When creating a personalized comic strip for lead generation
- When automating content creation with brand-specific visuals

## What This Does

Generates a prompt for creating a 4-panel comic strip lead magnet, tailored to a specific brand using website analysis and logo integration.

## Workflow

Create a 4-panel comic strip in a vibrant, cartoon style reminiscent of classic animated sitcoms: bold outlines, exaggerated facial expressions, and a bright, playful color palette. The characters should have yellow skin tones, expressive eyes, and a slightly caricatured look.

The main character is a tech-savvy, confident professional with either a clean haircut or a scruffy beard (Character A). Character A wears a T-shirt featuring the attached logo. Character B appears in the last strip (part 4) looks different, and has a different t-shirt on with the word INSERT YOUR NAME; written on it.

This comic will be used as a creative cold outreach for an AI automation consultant.


✅ Visual Style Notes:
* Yellow-toned skin, cartoonish proportions
* Thick black outlines, bright colors
* Exaggerated facial expressions
* Clean, punchy composition
* Every single panel MUST have a speech bubble as explain below.


Accent colors and props reflecting the brand. The brand colours and description of the homepage to include are: 
{{ $('Website Analysis').item.json.content }}
Keep the design visually beautiful with contrasting colours.
Include a website screenshot on the laptop screen in panel 1. 


✅ Text & Structure:
* Max 5 words per panel, in speech bubbles or notes only
* Style and tone: humorous, insightful, friendly



🟨 Panel Breakdown
Panel 1 – Admiration
 Scene: Character A is looking at his open laptop and the attached screenshot is clearly visible.
The business website clearly visible. He looks intrigued
Speech bubble: 
""{{ $json.message.content }}""


Panel 2 – Opportunity Thought
 Scene: Character A wonders longingly looking out of the window as he considers. He looks sad.
 Speech bubble:
 "Imagine more customers here..."


Panel 3 – Insight
 Scene: A lightbulb appears above Character A's head. In the background, helpful cartoon robots tidy tabs, auto-sort messages, or serve digital forms. He looks hopeful.
 Speech bubble:
 "AI Automation could help."


Panel 4 – CTA
 Scene: A New character (Character B) in the fourth panel, visibly different then the others with a plain shirt with the word Jack on it. He smiles, writing on a sticky note or messaging box.

 Message:
 "Want me to show you how?"

## Configuration

**Required tools/platforms:**
- OpenAI
- n8n

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
