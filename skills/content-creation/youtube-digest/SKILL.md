---
name: youtube-digest
version: "1.0.0"
description: "YouTube video processing: transcript extraction, summarization, and skill generation. Extracted from GravityClaw."
dependencies:
  - youtube-transcript (pip)
  - yt-dlp (optional, for audio fallback)
tags: [youtube, video, transcription, summarization, learning]
---

# YouTube Digest — Video Intelligence Extraction

> Extracted from GravityClaw's YouTube processing pipeline. Turns video content into structured knowledge.

## Pipeline

```
YouTube URL → Transcript → Chunking → Summarization → Output
                                          │
                              ┌───────────┼───────────┐
                              ▼           ▼           ▼
                          Summary    Key Points    Skill.md
                        (1-page)   (actionable)   (if tutorial)
```

## Transcript Extraction (3-Tier Fallback)

```python
async def get_transcript(video_id: str) -> str:
    """Extract transcript with 3-tier fallback strategy."""

    # Tier 1: Official YouTube captions (fastest, most accurate)
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([t["text"] for t in transcript])
    except Exception:
        pass

    # Tier 2: Auto-generated captions (still fast)
    try:
        transcript = YouTubeTranscriptApi.get_transcript(
            video_id, languages=["en-US", "en"]
        )
        return " ".join([t["text"] for t in transcript])
    except Exception:
        pass

    # Tier 3: Download audio + Whisper transcription (slowest, most robust)
    try:
        audio_path = await download_audio(video_id)  # yt-dlp
        transcript = await whisper_transcribe(audio_path)  # OpenAI Whisper
        return transcript
    except Exception:
        raise TranscriptUnavailableError(video_id)
```

## Chunking Strategy

Long transcripts are split into semantic chunks:

```python
def chunk_transcript(text: str, max_tokens: int = 4000, overlap: int = 200) -> list:
    """Split transcript into overlapping chunks at sentence boundaries."""
    sentences = split_into_sentences(text)
    chunks = []
    current = []
    current_tokens = 0

    for sentence in sentences:
        tokens = count_tokens(sentence)
        if current_tokens + tokens > max_tokens and current:
            chunks.append(" ".join(current))
            # Keep last N tokens as overlap
            overlap_sentences = get_overlap(current, overlap)
            current = overlap_sentences
            current_tokens = count_tokens(" ".join(current))
        current.append(sentence)
        current_tokens += tokens

    if current:
        chunks.append(" ".join(current))

    return chunks
```

## Output Formats

### 1. Executive Summary
```markdown
# [Video Title] — Summary

**Channel:** [Channel Name]
**Duration:** [HH:MM:SS]
**Published:** [Date]

## TL;DR (1 paragraph)
[Concise summary of the entire video]

## Key Takeaways
1. [Most important point]
2. [Second most important]
3. [Third most important]

## Detailed Notes
### [Topic 1] (timestamp: MM:SS)
[Notes...]

### [Topic 2] (timestamp: MM:SS)
[Notes...]
```

### 2. Actionable Key Points
```json
{
    "video_id": "...",
    "title": "...",
    "key_points": [
        {
            "point": "Use semantic search for memory, not keyword matching",
            "timestamp": "05:23",
            "category": "technical",
            "actionable": true,
            "action": "Implement Pinecone-based memory in agent system"
        }
    ],
    "tools_mentioned": ["Pinecone", "LangChain", "OpenAI"],
    "people_mentioned": ["Sam Altman", "Andrej Karpathy"]
}
```

### 3. Auto-Generated SKILL.md (for tutorials)
When a video is detected as a tutorial or how-to:

```markdown
---
name: [derived-from-title]
version: "1.0.0"
description: "[Auto-generated from YouTube: video title]"
source: "https://youtube.com/watch?v=[id]"
---

# [Skill Name]

> Auto-generated from: [Video Title] by [Channel]

## Prerequisites
[Extracted from video intro]

## Steps
1. [Step extracted from tutorial flow]
2. [Step 2]
3. [Step 3]

## Code Examples
[Code blocks extracted from video]
```

## Usage

```bash
# Summarize a single video
python3 skills/youtube-digest/scripts/process.py "https://youtube.com/watch?v=VIDEO_ID"

# Batch process a playlist
python3 skills/youtube-digest/scripts/process.py --playlist="PLAYLIST_ID"

# Generate skill from tutorial
python3 skills/youtube-digest/scripts/process.py "URL" --output=skill

# Process and add to knowledge graph
python3 skills/youtube-digest/scripts/process.py "URL" --kg
```

## Integration

```
YouTube URL
    → youtube-digest (extract + summarize)
        → knowledge-graph (entities from video)
        → content-pipeline/forge (enrich metadata)
        → skills/ (auto-generate if tutorial)
```
