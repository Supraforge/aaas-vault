---
name: remotion-best-practices
description: Provides expert guidance on creating videos with Remotion (React for Video).
version: 1.0.0
dependencies: []
inputs:
  - name: topic
    description: >-
      The video implementation detail to query (e.g., 'composition',
      'rendering').
outputs:
  - type: stdout
    description: Best practices and code snippets.
compatibility: 'agent-zero, claude-code, cursor'
---

# Remotion Best Practices

**PURPOSE:**
This skill acts as a knowledge base for "Remotion", the framework for creating videos in React.

## 🎯 Best Practices

### 1. Composition
- Always define video metadata (width, height, fps) in `remotion.config.ts`.
- Use `<AbsoluteFill>` for layering components.

### 2. Rendering
- Prefer server-side rendering for production.
- Use `npx remotion render` for CLI output.

## 🛠️ Performance
- Use `useVideoConfig()` to access frame data.
- Optimize images using `remotion`'s built-in `Img` tag.
