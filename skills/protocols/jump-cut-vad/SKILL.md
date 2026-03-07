---
name: "jump-cut-editor"
description: "Removes silences from talking-head videos using neural voice activity detection (Silero VAD). Offers restart phrase detection, audio enhancement, and color grading."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["video editing","silence removal","voice activity detection","audio enhancement","color grading"]
triggers:
  - "when I need to remove silences from a video"
  - "when I want to edit talking-head videos"
  - "when I need more accurate silence detection"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "directive"
  original_file: "jump_cut_vad.md"
---

# Jump Cut Editor

## When to Use

To remove long pauses in talking-head videos,To automatically edit out mistakes marked with a 'cut cut' phrase,When FFmpeg's silence detection is inaccurate due to background noise,To enhance audio quality with EQ, compression, and loudness normalization,To apply color grading using LUT files

## What This Does

Removes silences from talking-head videos using neural voice activity detection (Silero VAD). Offers restart phrase detection, audio enhancement, and color grading.

## Workflow

Extract audio from the input video.,Run Silero VAD to identify speech segments.,(Optional) Detect 'cut cut' restart phrases using Whisper.,(Optional) Remove the segment containing 'cut cut' and the preceding mistake segment.,Concatenate speech segments with specified padding.,(Optional) Apply audio enhancement chain (highpass, lowpass, EQ, compression, loudness normalization).,(Optional) Apply color grading using a LUT file.,Encode and save the edited video to the specified output path.

## Constraints

Requires Python 3 and FFmpeg to be installed.,Requires the `torch` package for Silero VAD.,Requires the `whisper` package for restart detection (optional).,Input video must have an audio track.,LUT files must be in a supported format (.cube, .3dl, .dat, .m3d, .csp).,Hardware encoding is automatically used on macOS if available; otherwise, software encoding is used.
