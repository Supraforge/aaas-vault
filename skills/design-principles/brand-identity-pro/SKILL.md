---
name: applying-brand-identity
description: Provides the single source of truth for brand guidelines, design tokens, technology choices, and voice/tone. Use this skill whenever generating UI components, styling applications, writing copy, or creating user-facing assets to ensure brand consistency.
version: 1.0.0
dependencies: []
---

# Brand Identity & Guidelines

**Brand Name:** AaaS (Agents as a Service)
**Canonical Reference:** https://aaas-platform.web.app/aaas-brand-reference.html

This skill defines the core constraints for visual design and technical implementation for the brand. You must adhere to these guidelines strictly to maintain consistency.

## 🎯 Triggers
- "Create a UI component for..."
- "Style this application..."
- "Write copy for..."
- "Generate a landing page..."
- "Build a form with brand styling..."

## ⚡ Quick Start (Self-Check)
Before applying brand guidelines, verify readiness:
- [ ] Run `bash ~/.gemini/skills/brand-identity/test.sh` to check all resource files exist.

## Reference Documentation

Depending on the task you are performing, consult the specific resource files below. Do not guess brand elements; always read the corresponding file.

### For Visual Design & UI Styling
If you need exact colors, fonts, border radii, or spacing values, read:
👉 **[`resources/design-tokens.json`](resources/design-tokens.json)**

### For Coding & Component Implementation
If you are generating code, choosing libraries, or structuring UI components, read the technical constraints here:
👉 **[`resources/tech-stack.md`](resources/tech-stack.md)**

### For Copywriting & Content Generation
If you are writing marketing copy, error messages, documentation, or user-facing text, read the persona guidelines here:
👉 **[`resources/voice-tone.md`](resources/voice-tone.md)**

## 📋 Workflow

1. **Ingest**: Analyze the user's request. Determine if the task involves UI design, code generation, or copywriting.
2. **Load Context**: Read the appropriate resource file(s) for the task type.
3. **Execute**: Generate the output strictly adhering to the loaded guidelines.
4. **Verify**: Confirm the output uses correct tokens, tech stack, and voice/tone.

## 🤖 System Instructions

When applying this skill:
- **Never hardcode** hex colors or font names; always reference `design-tokens.json`
- **Never deviate** from the tech stack defined in `tech-stack.md`
- **Always match** the brand voice defined in `voice-tone.md`
- If a guideline is unclear, ask the user rather than guessing
