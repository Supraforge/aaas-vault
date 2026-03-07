---
name: "insert-swivel-teaser"
description: "Inserts a swivel teaser (fast-forward preview with 3D rotation) into a video at a specified point while preserving original audio."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["video editing","ffmpeg","3D transition","video effects"]
triggers:
  - "when I want to add a dynamic teaser to a video"
  - "when I need to create a fast-forward preview with 3D effects"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "insert_3d_transition.py"
---

# Insert Swivel Teaser

## When to Use

- when I want to add a dynamic teaser to a video
- when I need to create a fast-forward preview with 3D effects

## What This Does

Inserts a swivel teaser (fast-forward preview with 3D rotation) into a video at a specified point while preserving original audio.

## Execution

```bash
python execution/insert_3d_transition.py input.mp4 output.mp4 [--bg-image path/to/bg.png]
```

### Parameters

input_path (required): Path to the input video file.
output_path (required): Path to save the output video.
--bg-image (optional): Path to a background image for the transition.

### Dependencies

- ffmpeg
- remotion
- python3
- npx
