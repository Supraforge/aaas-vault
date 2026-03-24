---
name: scout-research
version: "1.0.0"
description: "Multi-source research automation with 12 scanner patterns. Extracted from GravityClaw."
dependencies:
  - tavily (optional)
  - firecrawl (optional)
  - brave-search (optional)
tags: [research, automation, scanning, discovery]
---

# Scout Research — Multi-Source Intelligence Scanner

> Extracted from GravityClaw's production scout system. Provides 12 scanner patterns for automated research across the web.

## Philosophy

**Don't search randomly — scan systematically.** Each scanner targets a specific source with tailored extraction logic. Results are scored, deduplicated, and enriched before being presented.

## The 12 Scanner Patterns

### Tier 1: Tech & Innovation (run first)

| Scanner | Source | What It Finds | Frequency |
|---------|--------|---------------|-----------|
| **hacker-news** | news.ycombinator.com | Top stories, Show HN, Ask HN by keyword | Daily |
| **github-trending** | github.com/trending | Repos by language/timeframe, stars velocity | Daily |
| **product-hunt** | producthunt.com | New launches, upvote velocity, maker info | Daily |
| **arxiv** | arxiv.org | Research papers by category (cs.AI, cs.CL, etc.) | Weekly |

### Tier 2: Industry & Market

| Scanner | Source | What It Finds | Frequency |
|---------|--------|---------------|-----------|
| **tech-blogs** | Major tech blogs (list below) | Articles matching topic keywords | Daily |
| **newsletters** | Configured newsletter feeds | Curated industry content | Weekly |
| **reddit** | Targeted subreddits | Discussions, trends, sentiment | Daily |
| **twitter-lists** | X/Twitter lists | Real-time signals from experts | Daily |

### Tier 3: Academic & Deep

| Scanner | Source | What It Finds | Frequency |
|---------|--------|---------------|-----------|
| **google-scholar** | scholar.google.com | Citations, h-index, research trends | Weekly |
| **patents** | patents.google.com | Filed patents by company/keyword | Monthly |
| **crunchbase** | crunchbase.com | Funding rounds, acquisitions | Weekly |
| **custom-feeds** | User-defined RSS/URLs | Any structured feed | Configurable |

## Scanner Configuration

Each scanner is defined as a config object:

```python
SCANNER_CONFIG = {
    "hacker_news": {
        "enabled": True,
        "source_url": "https://hacker-news.firebaseio.com/v0",
        "endpoints": {
            "top": "/topstories.json",
            "new": "/newstories.json",
            "best": "/beststories.json",
            "show": "/showstories.json",
            "ask": "/askstories.json",
        },
        "max_items": 30,
        "keywords": [],  # Empty = all; or ["AI", "startup", "SaaS"]
        "scoring": {
            "min_score": 10,
            "weight_score": 0.4,
            "weight_comments": 0.3,
            "weight_recency": 0.3,
        },
    },
    "github_trending": {
        "enabled": True,
        "source_url": "https://api.github.com",
        "languages": ["python", "typescript", "rust"],
        "timeframes": ["daily", "weekly"],
        "min_stars": 50,
        "scoring": {
            "weight_stars": 0.3,
            "weight_forks": 0.2,
            "weight_recency": 0.3,
            "weight_description_match": 0.2,
        },
    },
    "product_hunt": {
        "enabled": True,
        "source_url": "https://api.producthunt.com/v2/api/graphql",
        "categories": ["ARTIFICIAL_INTELLIGENCE", "DEVELOPER_TOOLS", "SAAS"],
        "min_votes": 20,
    },
    "arxiv": {
        "enabled": True,
        "source_url": "http://export.arxiv.org/api/query",
        "categories": ["cs.AI", "cs.CL", "cs.LG"],
        "max_results": 20,
        "sort_by": "submittedDate",
    },
}
```

## Scoring Algorithm

Every discovered item gets a composite score (0-100):

```
score = (
    relevance_weight * keyword_match_score +
    authority_weight * source_authority_score +
    recency_weight * time_decay_score +
    engagement_weight * social_signal_score
)
```

Where:
- `keyword_match_score` — How well the title/description matches search terms (TF-IDF or embedding similarity)
- `source_authority_score` — Domain reputation (HN front page = 90, random blog = 30)
- `time_decay_score` — Exponential decay from publish date (half-life: 7 days)
- `social_signal_score` — Upvotes, stars, comments normalized to 0-100

## Deduplication

Before storing results, deduplicate by:
1. **URL normalization** — strip tracking params, normalize protocol
2. **Title similarity** — fuzzy match (>0.85 = duplicate)
3. **Content hash** — SHA-256 of first 500 chars of body

## Output Format

Each scan produces a structured result:

```json
{
    "scanner": "hacker_news",
    "timestamp": "2026-03-18T10:00:00Z",
    "items": [
        {
            "id": "hn-12345678",
            "title": "Show HN: AI agent framework",
            "url": "https://example.com/project",
            "source": "hacker_news",
            "score": 87.5,
            "metadata": {
                "hn_score": 342,
                "comments": 89,
                "author": "user123",
                "published": "2026-03-17T15:30:00Z"
            },
            "tags": ["AI", "agents", "framework"],
            "summary": null
        }
    ],
    "total_found": 30,
    "after_dedup": 28,
    "above_threshold": 12
}
```

## Usage

### Quick scan (single source)
```bash
python3 skills/scout-research/scripts/scan.py --source=hacker_news --keywords="AI agent"
```

### Full sweep (all enabled scanners)
```bash
python3 skills/scout-research/scripts/scan.py --all --keywords="AI,SaaS,automation"
```

### Custom config
```bash
python3 skills/scout-research/scripts/scan.py --config=.tmp/scout_config.json
```

## Integration with Research Protocol

Scout feeds into Phase 2 (Proposal Research) of the research-protocol skill:

```
research-protocol Phase 2
    └── scout-research (automated discovery)
        ├── hacker_news scanner
        ├── github_trending scanner
        ├── product_hunt scanner
        └── ... (all enabled scanners)
    └── research-tavily (deep-dive on top results)
    └── manual research (agent-guided)
```

## Tech Blog Sources (Default)

- https://blog.google/technology/ai/
- https://openai.com/blog
- https://www.anthropic.com/research
- https://engineering.fb.com/
- https://netflixtechblog.com/
- https://blog.cloudflare.com/
- https://aws.amazon.com/blogs/machine-learning/
- https://techcrunch.com/category/artificial-intelligence/

## Adding Custom Scanners

Create a new scanner by implementing:

```python
class CustomScanner:
    name: str = "my_scanner"
    source_url: str = "https://..."

    async def scan(self, keywords: list[str]) -> list[ScanResult]:
        """Fetch, filter, score, and return results."""
        raw = await self.fetch()
        filtered = self.filter(raw, keywords)
        scored = self.score(filtered)
        return scored

    def score(self, items) -> list[ScanResult]:
        """Apply composite scoring algorithm."""
        ...
```

Register in `SCANNER_CONFIG` and it's automatically included in full sweeps.
