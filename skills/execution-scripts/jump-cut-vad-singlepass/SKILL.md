---
name: "jump-cut-editor"
description: "Edits videos by automatically removing silence using Silero VAD and FFmpeg for single-pass processing, enhancing editing efficiency."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["video editing","ffmpeg","silero vad","automation","audio processing"]
triggers:
  - "when editing a video and need to remove silences"
  - "when preparing videos for social media"
  - "when wanting to quickly shorten a video"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "jump_cut_vad_singlepass.py"
---

# Jump Cut Editor

## When to Use

- when editing a video and need to remove silences
- when preparing videos for social media
- when wanting to quickly shorten a video

## What This Does

Edits videos by automatically removing silence using Silero VAD and FFmpeg for single-pass processing, enhancing editing efficiency.

## Execution

```bash
jump-cut-editor input.mp4 output.mp4 --min-silence 0.6 --padding 200
```

### Parameters

input (path): Input video file path.
output (path): Output video file path.
--min-silence (float): Minimum silence duration to cut in seconds (default: 0.5).
--min-speech (float): Minimum speech duration to keep in seconds (default: 0.25).
--padding (int): Padding around speech segments in milliseconds (default: 100).
--merge-gap (float): Merge segments closer than this gap in seconds (default: 0.3).
--keep-start/--no-keep-start (bool): Whether to always start from 0:00 (default: True).

### Dependencies

- ffmpeg
- python3
- torch
- silero-vad (pytorch hub)
