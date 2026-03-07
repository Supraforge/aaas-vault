---
name: gettr-transcribe-summarize
description: >-
  Download audio from a GETTR post (via HTML og:video), transcribe it locally
  with MLX Whisper on Apple Silicon (with timestamps via VTT), and summarize the
  transcript into bullet points and/or a timestamped outline. Use when given a
  GETTR post URL and asked to produce a transcript or summary.
homepage: 'https://gettr.com'
metadata:
  clawdbot:
    emoji: "\U0001F4FA"
    requires:
      bins:
        - mlx_whisper
        - ffmpeg
    install:
      - id: mlx-whisper
        kind: pip
        package: mlx-whisper
        bins:
          - mlx_whisper
        label: Install mlx-whisper (pip)
      - id: ffmpeg
        kind: brew
        formula: ffmpeg
        bins:
          - ffmpeg
        label: Install ffmpeg (brew)
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---

# Gettr Transcribe + Summarize (MLX Whisper)

## Quick start (single command)

Run the full pipeline (Steps 1–3) with one command:
```bash
bash scripts/run_pipeline.sh "<GETTR_POST_URL>"
```

To explicitly set the transcription language (recommended for non-English content):
```bash
bash scripts/run_pipeline.sh --language zh "<GETTR_POST_URL>"
```

Common language codes: `zh` (Chinese), `en` (English), `ja` (Japanese), `ko` (Korean), `es` (Spanish), `fr` (French), `de` (German), `ru` (Russian).

This outputs:
- `./out/gettr-transcribe-summarize/<slug>/audio.wav`
- `./out/gettr-transcribe-summarize/<slug>/audio.vtt`

Then proceed to Step 4 (Summarize) to generate the final deliverable.

---

## Workflow (GETTR URL → transcript → summary)

### Inputs to confirm
Ask for:
- GETTR post URL
- Output format: **bullets only** or **bullets + timestamped outline**
- Summary size: **short**, **medium** (default), or **detailed**
- Language (optional): if the video is non-English and auto-detection fails, ask for the language code (e.g., `zh` for Chinese)

Notes:
- This skill does **not** handle authentication-gated GETTR posts.
- This skill does **not** translate; outputs stay in the video's original language.
- If transcription quality is poor or mixed with English, re-run with explicit `--language` flag.

### Prereqs (local)
- `mlx_whisper` installed and on PATH
- `ffmpeg` installed (recommended: `brew install ffmpeg`)

### Step 0 — Pick an output directory
Recommended convention: `./out/gettr-transcribe-summarize/<slug>/`

Extract the slug from the GETTR post URL (e.g., `https://gettr.com/post/p1abc2def` → slug = `p1abc2def`).

Directory structure:
- `./out/gettr-transcribe-summarize/<slug>/audio.wav`
- `./out/gettr-transcribe-summarize/<slug>/audio.vtt`
- `./out/gettr-transcribe-summarize/<slug>/summary.md`

### Step 1 — Extract the media URL and slug
Preferred: fetch the post HTML and read `og:video*`.

```bash
python3 scripts/extract_gettr_og_video.py "<GETTR_POST_URL>"
```
This prints the best candidate video URL (often an HLS `.m3u8`) and the post slug.

Extract the slug from the URL path (e.g., `/post/p1abc2def` → `p1abc2def`) to create the output directory.

**Important: Streaming URLs require browser extraction**

For streaming URLs (`gettr.com/streaming/<slug>`), the Python script may return a stale/invalid `og:video` URL that fails with HTTP 412. This is because GETTR dynamically generates signed stream URLs via JavaScript.

If the URL is a streaming link OR if download fails with HTTP 412:
1. Open the streaming URL in a browser and wait for the page to fully load (JavaScript must execute)
2. Extract the `og:video` meta tag content from the rendered DOM:
   ```javascript
   document.querySelector('meta[property="og:video"]').getAttribute('content')
   ```
3. Use that fresh URL for the download step

The browser-extracted URL will have a valid signature and work with ffmpeg.

If extraction fails, ask the user to provide the `.m3u8`/MP4 URL directly (common if the post is private/gated or the HTML is dynamic).

### Step 2 — Download audio with ffmpeg
Extract audio-only (16kHz mono WAV) for faster and more stable transcription:
```bash
bash scripts/download_audio.sh "<M3U8_OR_MP4_URL>" "./out/gettr-transcribe-summarize/<slug>/audio.wav"
```

This directly extracts audio without intermediate video, reducing disk I/O and processing time.

### Step 3 — Transcribe with MLX Whisper
Generate VTT output with timestamps:
```bash
mlx_whisper "./out/gettr-transcribe-summarize/<slug>/audio.wav" \
  -f vtt \
  -o "./out/gettr-transcribe-summarize/<slug>" \
  --model mlx-community/whisper-large-v3-turbo \
  --condition-on-previous-text False \
  --word-timestamps True
```

To explicitly set the language (recommended when auto-detection fails):
```bash
mlx_whisper "./out/gettr-transcribe-summarize/<slug>/audio.wav" \
  -f vtt \
  -o "./out/gettr-transcribe-summarize/<slug>" \
  --model mlx-community/whisper-large-v3-turbo \
  --condition-on-previous-text False \
  --word-timestamps True \
  --language zh
```

Flags explained:
- `-f vtt`: VTT format provides timestamps for building the outline.
- `--condition-on-previous-text False`: prevents hallucination errors from propagating across segments.
- `--word-timestamps True`: more precise timing for section boundaries.
- `--language <code>`: explicit language code (e.g., `zh`, `en`, `ja`, `ko`). Use when auto-detection fails.

Notes:
- By default, language is auto-detected. For non-English content where detection fails, use `--language`.
- Common language codes: `zh` (Chinese), `en` (English), `ja` (Japanese), `ko` (Korean), `es` (Spanish), `fr` (French), `de` (German), `ru` (Russian).
- If too slow or memory-heavy, try smaller models: `mlx-community/whisper-medium` or `mlx-community/whisper-small`.
- If quality is poor, try the full model: `mlx-community/whisper-large-v3` (slower but more accurate).
- If `--word-timestamps` causes issues, omit it (the pipeline script handles this automatically).

### Step 4 — Summarize
Write the final deliverable to `./out/gettr-transcribe-summarize/<slug>/summary.md`.

Pick a **summary size** (user-selectable):
- **Short:** 5–8 bullets; (if outline) 4–6 sections
- **Medium (default):** 8–20 bullets; (if outline) 6–15 sections
- **Detailed:** 20–40 bullets; (if outline) 15–30 sections

Include:
- **Bullets** (per size above)
- Optional **timestamped outline** (per size above)

Timestamped outline format (default heading style):
```
[00:00 - 02:15] Section heading
- 1–3 sub-bullets
```

When building the outline from VTT cues:
- Group adjacent cues into coherent sections.
- Use the start time of the first cue and end time of the last cue in the section.

## Bundled scripts
- `scripts/run_pipeline.sh`: full pipeline wrapper (Steps 1–3 in one command)
- `scripts/extract_gettr_og_video.py`: fetch GETTR HTML and extract `og:video*` URL + post slug (with retry/backoff)
- `scripts/download_audio.sh`: download/extract audio from HLS or MP4 URL to 16kHz mono WAV

### Error handling
- **Non-video posts**: The extraction script detects image/text posts and provides a helpful error message.
- **Network errors**: Automatic retry with exponential backoff (up to 3 attempts).
- **No audio track**: The download script validates output and reports if the source has no audio.
- **HTTP 412 errors**: The extracted `og:video` URL has an expired/invalid signature. Use browser extraction to get a fresh URL (see Step 1 and `references/troubleshooting.md`).

## Troubleshooting
See `references/troubleshooting.md` for detailed solutions to common issues including:
- HTTP 412 errors (stale signed URLs)
- Extraction failures
- Download errors
- Transcription quality issues
