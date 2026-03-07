---
name: youtube-comment-analyzer
description: >-
  **Trigger phrases:** - "Analyze comments for [URL]" - "Analyze this video:
  [URL]" - "What are people asking about [URL]" - "Comment analysis for
  [VIDEO_ID]" - "YouTube comment insights for [URL]"
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---
# YouTube Comment Analyzer

**Trigger phrases:**
- "Analyze comments for [URL]"
- "Analyze this video: [URL]"
- "What are people asking about [URL]"
- "Comment analysis for [VIDEO_ID]"
- "YouTube comment insights for [URL]"

**Source:** Based on https://github.com/drshailesh88/youtube-analyzer

---

## What This Does

Analyzes YouTube video comments to extract audience insights:
- **Top Questions** people are asking (with urgency ratings)
- **Top Myths** and misconceptions (with danger ratings)
- **Pain Points** and frustrations
- **Content Recommendations** (must address, gaps, viral potential)
- **Sentiment Analysis** (positive/negative/neutral breakdown)
- **Recurring Themes** in discussions

---

## How to Use (Claude Instructions)

### Step 1: Extract Video ID

From URL patterns:
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://youtube.com/watch?v=VIDEO_ID&...`
- Just `VIDEO_ID` (11 characters, alphanumeric with - and _)

### Step 2: Run the Analyzer

```bash
python skills/cardiology/youtube-comment-analyzer/scripts/analyze_comments.py VIDEO_URL_OR_ID
```

**Options:**
- `--max-comments 500` — Limit comments scraped (default: 500)
- `--output path/to/file.json` — Custom output location
- `--json` — Output raw JSON instead of formatted report

**Examples:**
```bash
# Analyze by URL
python skills/cardiology/youtube-comment-analyzer/scripts/analyze_comments.py "https://youtube.com/watch?v=abc123xyz"

# Analyze by ID with limited comments
python skills/cardiology/youtube-comment-analyzer/scripts/analyze_comments.py abc123xyz --max-comments 200

# Get JSON output
python skills/cardiology/youtube-comment-analyzer/scripts/analyze_comments.py abc123xyz --json
```

### Step 3: Read the Output

The script outputs a formatted report directly. Full JSON is saved to:
```
skills/cardiology/youtube-comment-analyzer/output/analysis_VIDEO_ID_TIMESTAMP.json
```

---

## Output Format

```
## Comment Analysis: [Video Title]

**Analyzed:** 1,847 comments | **Time:** 45 seconds

### Top Questions (What viewers want to know)
1. [Question] — HIGH urgency
2. [Question] — MEDIUM urgency
3. ...

### Top Myths (Misconceptions to address)
1. [Myth] — HIGH danger
2. [Myth] — MEDIUM danger
3. ...

### Pain Points (Viewer frustrations)
1. [Pain point]
2. [Pain point]
3. ...

### Content Recommendations
- **Must Address:** [topics]
- **Content Gaps:** [topics]
- **Viral Potential:** [topics]

### Sentiment
Positive: X | Negative: Y | Neutral: Z
Summary: [one line]

### Recurring Themes
theme1, theme2, theme3, ...
```

---

## API Keys Required

Set one of these in `.env`:
- `YOUTUBE_API_KEY` or `GOOGLE_API_KEY` — For fetching comments via YouTube Data API v3
- `ANTHROPIC_API_KEY` — For AI analysis (preferred)
- `OPENROUTER_API_KEY` — Fallback for AI analysis (uses free Gemini model)

---

## Error Handling

- **No comments found:** Video may have comments disabled
- **API error:** Check API key validity
- **Rate limited:** Wait and retry, or reduce --max-comments

---

## Technical Details

- Uses **YouTube Data API v3** for comment fetching
- Uses **Claude** or **OpenRouter (Gemini)** for AI analysis
- Handles **500+ comments** via map-reduce chunking
- Output saved to JSON for future reference
- Works with any YouTube video with comments enabled
