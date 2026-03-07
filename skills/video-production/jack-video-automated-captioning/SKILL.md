---
name: jack-video-automated-captioning
description: >-
  Automates video captioning with word-level timestamps, audio processing, and
  Remotion-based caption rendering.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - video
  - captioning
  - automation
  - remotion
  - whisper
  - auphonic
triggers:
  - when you need to automatically generate captions for a video
  - when you want to improve video accessibility with accurate captions
allowed-tools: []
compatibility: 'ffmpeg, auphonic, remotion, openai whisper'
metadata:
  source: jack-school
  lesson: 129
  lesson_title: Links
  difficulty: medium
  category: video
  tools_required:
    - ffmpeg
    - auphonic
    - remotion
    - openai whisper
  estimated_setup_time: 1hr
---

# Video Automated Captioning

## When to Use

Use this skill when you need to:
- when you need to automatically generate captions for a video
- when you want to improve video accessibility with accurate captions

## What This Does

Automates video captioning with word-level timestamps, audio processing, and Remotion-based caption rendering.

## Workflow

# Automated Video Captioning Procedure

This procedure automates the process of generating captions for videos using Whisper for transcription, Auphonic for audio processing, and Remotion for rendering the captions.

## Steps

1.  **Transcribe with Whisper:**

    *   Use Whisper to transcribe the video and obtain word-level timestamps.

        ```bash
        uvx --from openai-whisper whisper audio.wav \
          --model tiny \
          --output_format json \
          --word_timestamps True
        ```

2.  **Parse the Transcript:**

    *   Analyze the transcript to detect false starts, filler mistakes, and identify the clean take.
    *   Record precise start and end timestamps for the clean take.

3.  **Trim the Video:**

    *   Use ffmpeg with the identified timestamps to cut the video to the clean take.

4.  **Audio Processing (Auphonic API):**

    *   Process the audio using the Auphonic API for broadcast-grade, normalized, noise-reduced audio.
    *   Auphonic Settings:
        *   leveler: true
        *   normloudness: true (Target: 16 LUFS)
        *   denoise: true
        *   denoisemethod: "dynamic"
        *   Output: AAC – 192kbps
    *   Steps:
        *   Create a production via: <https://auphonic.com/api/productions.json>
        *   Upload the trimmed audio
        *   Start processing
        *   Poll until complete
        *   Download the processed result
    *   Store your API key in an environment variable.

5.  **Remotion Caption Engine:**

    *   Create a React component with the following caption system using Remotion:
        *   Typography:
            *   Font: Inter (via @remotion/google-fonts)
            *   Size: 72px
            *   Weight: 800
            *   Letter spacing: 0.02em
            *   Word gap: 24px
        *   Chunking: Display 4 words per chunk
        *   Styling Logic:
            *   Word State Styling:
                *   Current: #BFF549 (neon green) + glow 0 0 40px rgba(191,245,73,0.8) + scale(1.1)
                *   Past: #FFFFFF
                *   Future: rgba(255,255,255,0.5)
            *   Additional effects:
                *   Text shadow: 0 4px 20px rgba(0,0,0,0.8)
                *   Position: Bottom, 120px
                *   Gradient overlay: Height: 40%, Fade: transparent → rgba(0,0,0,0.85)
        *   Audio: Mute original video and overlay Auphonic-processed audio
        *   Cleanup Rules: Remove trailing punctuation (., ,) and preserve contractions (don't, it's, etc.)

6.  **Render:**

    *   Use Remotion to render the video with captions.

        ```bash
        npx remotion render [CompositionName] output.mp4 --codec h264
        ```

    *   Output location: Desktop

## Project Structure

```
/project-root
  /public
    video.mp4
    audio.aac
  Root.tsx
  index.ts
```

## Dependencies

*   remotion
*   @remotion/google-fonts

Root.tsx registers the composition and wires everything together.

## Execution Rules

*   Auto-accept all permissions
*   No prompts
*   No confirmations
*   Just execute

This is a hands-off, deterministic pipeline from raw footage → cinematic, captioned MP4.

## Configuration

**Required tools/platforms:**
- ffmpeg
- auphonic
- remotion
- openai whisper

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
