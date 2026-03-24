---
name: content-pipeline
version: "1.0.0"
description: "End-to-end content automation: Scout → Intake → Forge → Digest → Publish. Extracted from GravityClaw."
dependencies:
  - scout-research
  - knowledge-graph (optional)
tags: [content, automation, pipeline, publishing, curation]
---

# Content Pipeline — Scout to Publish

> Extracted from GravityClaw's production content automation system. Defines the 5-stage pipeline for turning raw research into published content.

## The Pipeline

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│  SCOUT   │───▶│  INTAKE  │───▶│  FORGE   │───▶│  DIGEST  │───▶│ PUBLISH  │
│ Discover │    │ Validate │    │ Enrich   │    │ Curate   │    │ Deliver  │
└──────────┘    └──────────┘    └──────────┘    └──────────┘    └──────────┘
```

### Stage 1: SCOUT (Discovery)
**Input:** Keywords, topics, configured scanners
**Output:** Raw items (URLs, titles, metadata)
**See:** `skills/scout-research/SKILL.md`

### Stage 2: INTAKE (Validation & Extraction)
**Input:** Raw items from Scout
**Output:** Validated, deduplicated, extracted content

Steps:
1. **Detect** — Classify source type (article, repo, paper, video, tweet)
2. **Extract** — Pull full content (Firecrawl, YouTube transcript, API)
3. **Analyze** — Score quality (readability, depth, originality)
4. **Vet** — Check against blocklist, spam detection, duplicate check
5. **Store** — Save to `.tmp/intake/` with standardized schema
6. **Activate** — Mark as ready for enrichment

```json
{
    "id": "intake-abc123",
    "source_type": "article",
    "url": "https://example.com/article",
    "title": "...",
    "content": "...(full text)...",
    "quality_score": 78.5,
    "word_count": 2340,
    "readability": "intermediate",
    "tags_auto": ["AI", "agents", "framework"],
    "status": "activated",
    "intake_timestamp": "2026-03-18T10:05:00Z"
}
```

### Stage 3: FORGE (Enrichment)
**Input:** Activated intake items
**Output:** Enriched items with metadata, summaries, classifications

Steps:
1. **Categorize** — Assign to content taxonomy (industry, topic, subtopic)
2. **Summarize** — LLM-generated 2-sentence summary
3. **Extract entities** — People, companies, tools, concepts → knowledge graph
4. **Tag** — Auto-generate semantic tags
5. **Score relevance** — How well does this match project goals?
6. **Normalize** — Standardize format, fix encoding, clean HTML

```python
def forge_enrich(item: IntakeItem) -> EnrichedItem:
    """Enrich an intake item with LLM-assisted metadata."""
    prompt = f"""Analyze this content and provide:
    1. Category (from taxonomy)
    2. 2-sentence summary
    3. Key entities (people, companies, tools)
    4. Semantic tags (5-10)
    5. Relevance score (0-100) to: {project_goals}

    Content: {item.content[:3000]}
    """
    enrichment = await llm.generate(prompt)
    return merge(item, enrichment)
```

### Stage 4: DIGEST (Curation)
**Input:** Enriched items
**Output:** Curated digest (selected, ordered, formatted)

Steps:
1. **Filter** — Remove items below relevance threshold
2. **Rank** — Sort by composite score (relevance × quality × recency)
3. **Group** — Cluster related items by topic
4. **Select** — Pick top N items per category
5. **Format** — Generate digest in target format (markdown, HTML, JSON)
6. **Review gate** — Optional human review before publishing

```markdown
# Weekly AI Digest — March 18, 2026

## 🔥 Top Stories
1. **Show HN: New agent framework** (Score: 92)
   Summary: ...
   Source: Hacker News | [Link](...)

2. **OpenAI announces GPT-5.4** (Score: 88)
   Summary: ...
   Source: Tech Blog | [Link](...)

## 📊 Trending Repos
- **project/repo** ⭐ 2.3k (+500 this week)
  Description: ...

## 📚 Research Papers
- **"Attention Is Still All You Need"** (arXiv)
  Summary: ...
```

### Stage 5: PUBLISH (Delivery)
**Input:** Curated digest
**Output:** Published content across channels

Delivery channels:
- **Email** — Resend API, formatted HTML digest
- **Notion** — Auto-create page in workspace
- **Slack** — Post to configured channel
- **LinkedIn** — Format as article or post
- **Twitter/X** — Thread from digest highlights
- **Google Docs** — Create shareable document
- **Custom webhook** — POST JSON to any endpoint

```python
PUBLISH_CONFIG = {
    "email": {
        "enabled": True,
        "recipients": ["team@company.com"],
        "template": "weekly_digest",
        "schedule": "monday 9:00",
    },
    "notion": {
        "enabled": True,
        "database_id": "...",
        "auto_tag": True,
    },
    "slack": {
        "enabled": False,
        "channel": "#research",
        "webhook_url": "...",
    },
}
```

## Pipeline Orchestration

Run the full pipeline:
```bash
# Full pipeline (all stages)
python3 skills/content-pipeline/scripts/run_pipeline.py --all --topic="AI agents"

# Single stage
python3 skills/content-pipeline/scripts/run_pipeline.py --stage=intake --input=.tmp/scout_results.json

# Dry run (no publishing)
python3 skills/content-pipeline/scripts/run_pipeline.py --all --dry-run
```

## Quality Scoring

Multi-dimensional quality assessment:

| Dimension | Weight | Measurement |
|-----------|--------|-------------|
| Relevance | 30% | Embedding similarity to project goals |
| Quality | 25% | Readability, depth, originality |
| Recency | 20% | Exponential decay (half-life: 7 days) |
| Authority | 15% | Source domain reputation |
| Engagement | 10% | Social signals (upvotes, shares) |

## Integration Map

```
research-protocol → scout-research → content-pipeline
                                        ├── intake (validate)
                                        ├── forge (enrich) → knowledge-graph
                                        ├── digest (curate)
                                        └── publish (deliver)
```
