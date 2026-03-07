# Gettr Transcript & Summary

Download audio from a GETTR post, transcribe it locally with MLX Whisper on Apple Silicon, and produce a clean summary or timestamped outline.

## What it does
- Extracts audio from a GETTR post (via og:video → 16kHz mono WAV)
- Transcribes locally with MLX Whisper (no API keys required)
- Outputs VTT with timestamps for precise outline generation
- Summarizes into bullets or a timestamped outline

## Quick start
```bash
bash scripts/run_pipeline.sh "<GETTR_POST_URL>"
```

Outputs to `./out/gettr-transcribe-summarize/<slug>/`:
- `audio.wav` – extracted audio
- `audio.vtt` – timestamped transcript

## Prerequisites
- `mlx_whisper` (`pip install mlx-whisper`)
- `ffmpeg` (`brew install ffmpeg`)

## Features
- Auto-detects non-video posts (image/text) with helpful error messages
- Retries network requests with exponential backoff
- Transcribes in original language (auto-detected)
- Prevents hallucination propagation with `--condition_on_previous_text False`
