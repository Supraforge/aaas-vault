---
name: jack-design-extract-remotion-showcase
description: >-
  Extracts design tokens from a website and generates a Remotion video
  showcasing the design system.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - design system
  - extraction
  - remotion
  - video
  - automation
triggers:
  - when you want to create a video showcasing a website's design system
  - >-
    when you need to reverse-engineer a website's design tokens for use in other
    projects
allowed-tools: []
compatibility: remotion
metadata:
  source: jack-school
  lesson: 129
  lesson_title: Links
  difficulty: medium
  category: design
  tools_required:
    - remotion
  estimated_setup_time: 30min
---

# Design Extract Remotion Showcase

## When to Use

Use this skill when you need to:
- when you want to create a video showcasing a website's design system
- when you need to reverse-engineer a website's design tokens for use in other projects

## What This Does

Extracts design tokens from a website and generates a Remotion video showcasing the design system.

## Workflow

# Design System Extraction and Remotion Showcase Procedure

This procedure automates the process of extracting a design system from a website and generating a Remotion video showcasing the system.

## Steps

1.  **Analyze & Extract Design System:**

    *   Fetch the website and extract the following design tokens:
        *   **Typography:**
            *   Font families: primary / secondary / mono
            *   Heading styles: H1–H6 (size, weight, line-height)
            *   Body styles: paragraph size, line-height, spacing
            *   Any custom letter spacing / text transforms (uppercase, tracking, etc.)
        *   **Colors:**
            *   Primary brand color(s)
            *   Secondary / accent colors
            *   Background colors (light/dark mode if present)
            *   Text colors: headings / body / muted
            *   Borders / dividers
            *   Gradients (definitions + usage)
        *   **Icons:**
            *   Icon library used (Lucide, Heroicons, custom SVG, etc.)
            *   Default icon size + stroke width
            *   Key brand-representative icons
        *   **Logo:**
            *   Extract or describe the logo
            *   Variants (wordmark, icon-only, stacked, etc.)
            *   Colors + dimensions / proportions
        *   **Layout & Components:**
            *   Border radius tokens (cards, buttons, inputs)
            *   Shadow styles (box-shadow tokens)
            *   Spacing scale (padding/margin patterns)
            *   Container widths / max-widths
            *   Common patterns (cards, sections, nav, buttons, inputs)

2.  **Create Animated Remotion Showcase:**

    *   Build a Remotion composition with the following specifications:
        *   Resolution: 1920 × 1080
        *   Frame rate: 30fps
        *   Length: ~15–16 seconds
    *   Animation Style Rules:
        *   Use spring-like motion (Remotion interpolate + easing)
        *   Stagger items for cascade effects
        *   Keep it minimal:
            *   Scale: 0.95 → 1
            *   Opacity: 0 → 1
        *   Clean, professional, no gimmicks

3.  **Generate Files:**

    *   Create the following files:
        *   `src/DesignShowcase.tsx`
            *   Main composition that uses extracted tokens to render the full 15–16s showcase
        *   `src/theme.ts`
            *   Extracted design tokens as TypeScript constants
            *   Document extracted values with comments (where each value came from)

## Output

*   Render to Desktop as: `[website-name]-design-system.mp4`

## Execution Rules

*   Auto-accept all permissions
*   No confirmations
*   Execute immediately

## Configuration

**Required tools/platforms:**
- remotion

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
