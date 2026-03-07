---
name: jack-content-meeting-transcript-formatter
description: >-
  Format Fireflies.ai meeting transcripts by combining speaker names and
  sentence text into a single transcript.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - meeting
  - transcription
  - fireflies.ai
  - formatting
triggers:
  - When processing a Fireflies.ai transcript
allowed-tools: []
compatibility: 'n8n, fireflies.ai'
metadata:
  source: jack-school
  lesson: 85
  lesson_title: What it does
  difficulty: easy
  category: content
  tools_required:
    - n8n
    - fireflies.ai
  estimated_setup_time: 15min
---

# Content Meeting Transcript Formatter

## When to Use

Use this skill when you need to:
- When processing a Fireflies.ai transcript

## What This Does

Format Fireflies.ai meeting transcripts by combining speaker names and sentence text into a single transcript.

## Workflow

// Get the transcript block from the current item
const transcript = $json.data.transcript;

// Safely extract title and sentence list
const title = transcript.title;
const sentences = transcript.sentences || [];

// Combine all sentence texts into a single transcript
const fullTranscriptText = sentences.map(s => `${s.speaker_name}: ${s.text}`).join('\n');

// Add final formatted values to item
item.json.meetingTitle = title;
item.json.fullTranscript = fullTranscriptText;

return item;

## Configuration

**Required tools/platforms:**
- n8n
- fireflies.ai

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
