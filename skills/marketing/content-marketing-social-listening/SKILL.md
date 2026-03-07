---
name: content-marketing-social-listening
description: >-
  Comprehensive content marketing toolkit for discovering viral content
  opportunities, social listening, knowledge gap analysis, and content demand
  assessment across platforms. Use when researching trending topics in a niche,
  finding what's going viral, assessing content knowledge gaps, planning content
  calendars, or identifying high-demand content opportunities. Integrates with
  perplexity-search for real-time trend data and research-lookup for deep
  analysis.
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---

# Content Marketing & Social Listening

## Overview

End-to-end content marketing research system for identifying viral content opportunities, performing social listening, and assessing content demand in any niche. Designed for content creators, marketers, and thought leaders who need data-driven content strategies.

## Core Capabilities

### 1. Social Listening & Trend Discovery

Find what's currently trending and going viral in your niche.

**Workflow:**
```
1. Define niche keywords (e.g., "cardiology", "heart health", "interventional cardiology")
2. Use perplexity-search with recency filter for each platform
3. Aggregate and score by engagement signals
4. Identify patterns in viral content
```

**Query Templates for Social Listening:**

```python
# Twitter/X Trends
query = "What are the most discussed cardiology topics on Twitter/X this week? Include specific tweets and engagement metrics."

# YouTube Trending
query = "What cardiology and heart health videos are trending on YouTube right now? Include view counts and upload dates."

# Reddit Discussions
query = "What are the hot topics being discussed in cardiology and heart health subreddits this week?"

# LinkedIn Professional
query = "What cardiology topics are healthcare professionals discussing on LinkedIn this week?"

# News & Media
query = "What cardiology news stories are getting the most coverage this week?"
```

### 2. Knowledge Gap Analysis

Identify what your audience is asking that isn't being answered well.

**Workflow:**
```
1. Search for common questions in your niche
2. Analyze existing content quality on those topics
3. Identify gaps where demand exceeds supply
4. Score opportunities by search volume + competition
```

**Query Templates:**

```python
# Common Questions
query = "What are the most frequently asked questions about [TOPIC] that people struggle to find good answers for?"

# Content Gaps
query = "What aspects of [TOPIC] are underserved by existing content online?"

# Emerging Topics
query = "What are emerging topics in [NICHE] that don't have much content yet?"
```

### 3. Viral Content Pattern Analysis

Understand what makes content go viral in your niche.

**Analysis Framework:**

| Factor | Weight | Assessment |
|--------|--------|------------|
| Emotional Trigger | 25% | Fear, hope, surprise, anger, joy |
| Practical Value | 25% | Actionable, saves time/money, solves problem |
| Social Currency | 20% | Makes sharer look smart/informed |
| Novelty | 15% | New data, contrarian view, first-to-market |
| Timing | 15% | News hooks, seasonal, cultural moments |

**Query for Viral Analysis:**
```python
query = f"""Analyze the top 5 most viral {niche} content pieces from the past month.
For each piece, identify:
1. The emotional trigger used
2. The practical value offered
3. Why people shared it
4. What made it novel
5. Any timing factors that helped"""
```

### 4. Content Demand Assessment

Quantify demand for content topics before creating.

**Demand Signals (in order of strength):**
1. Search volume (Google Trends, keyword tools)
2. Question frequency (forums, Q&A sites)
3. Social engagement (likes, shares, comments)
4. Comment requests ("please make a video about...")
5. Competitor performance on topic

**Query Template:**
```python
query = f"""What is the content demand for "{topic}" in the {niche} space?
Include:
- Estimated search volume or interest level
- Common questions asked about this topic
- How existing content on this topic performs
- Competitor coverage of this topic"""
```

### 5. Platform-Specific Strategies

**YouTube (Long-form):**
- Search: "YouTube [niche] trending videos"
- Signals: Views in 24h, view-to-subscriber ratio, comment velocity
- Hooks: Title patterns, thumbnail analysis, intro hooks

**Twitter/X (Short-form):**
- Search: "[niche] viral tweets OR threads"
- Signals: Retweets, quote tweets, reply ratio
- Hooks: First line patterns, thread structures

**LinkedIn (Professional):**
- Search: "[niche] LinkedIn viral posts professionals"
- Signals: Engagement rate, comment quality, shares
- Hooks: Personal stories, contrarian takes, data reveals

**TikTok/Reels (Micro-content):**
- Search: "[niche] TikTok trends OR viral"
- Signals: View count velocity, duets, stitches
- Hooks: Pattern interrupts, surprising facts, storytelling

**Blog/SEO (Evergreen):**
- Search: "top [niche] blog posts OR articles"
- Signals: Backlinks, SERP position, organic traffic estimates
- Hooks: Comprehensive guides, data studies, how-tos

## Content Opportunity Scoring

Score each content opportunity using this framework:

```
OPPORTUNITY_SCORE = (Demand × 0.3) + (Gap × 0.25) + (Virality_Potential × 0.25) + (Alignment × 0.2)

Where:
- Demand (1-10): How much people are searching/asking
- Gap (1-10): How poorly existing content serves demand
- Virality_Potential (1-10): How shareable the topic is
- Alignment (1-10): How well it fits your expertise/brand
```

## Quick Start Workflow

### Finding Your Next Viral Topic

```
Step 1: Define your niche keywords (3-5 core terms)
Step 2: Run social listening queries for each platform
Step 3: Identify trending topics in last 7-14 days
Step 4: Score each topic using opportunity framework
Step 5: Validate with knowledge gap analysis
Step 6: Create content calendar with top opportunities
```

### Weekly Social Listening Routine

```
Monday: YouTube + Podcast trends
Tuesday: Twitter/X conversations
Wednesday: LinkedIn professional discussions
Thursday: Reddit + forum deep dive
Friday: News hooks + emerging stories
Weekend: Synthesis + content planning
```

## Integration with Other Skills

This skill works best when combined with:

- **perplexity-search**: Real-time trend data and research
- **research-lookup**: Deep analysis with citations
- **generate-image**: Create visuals for content
- **scientific-schematics**: Create infographics
- **cardiology-content-repurposer**: Turn findings into multi-platform content

## Output Templates

### Content Opportunity Report

```markdown
# Content Opportunity: [TOPIC]

## Demand Score: X/10
- Search interest: [HIGH/MEDIUM/LOW]
- Question frequency: [EXAMPLES]
- Social buzz: [METRICS]

## Gap Score: X/10
- Existing content quality: [ASSESSMENT]
- Unmet needs: [LIST]
- Our angle: [DIFFERENTIATOR]

## Virality Potential: X/10
- Emotional triggers: [LIST]
- Shareability factors: [LIST]
- Timing considerations: [NOTES]

## Recommendation
- Priority: [HIGH/MEDIUM/LOW]
- Format: [VIDEO/ARTICLE/THREAD/etc.]
- Platform: [YOUTUBE/TWITTER/etc.]
- Hook angle: [SUGGESTION]
```

### Weekly Trend Report

```markdown
# Weekly Trend Report: [NICHE]
Week of: [DATE]

## Hot Topics This Week
1. [TOPIC] - [PLATFORM] - [WHY TRENDING]
2. [TOPIC] - [PLATFORM] - [WHY TRENDING]
3. [TOPIC] - [PLATFORM] - [WHY TRENDING]

## Emerging Stories
- [STORY] - Virality potential: X/10

## Knowledge Gaps Identified
- [GAP 1]
- [GAP 2]

## Content Calendar Recommendations
| Day | Platform | Topic | Format |
|-----|----------|-------|--------|
| Mon | YouTube  | ...   | Video  |
| Wed | Twitter  | ...   | Thread |
| Fri | LinkedIn | ...   | Post   |

## Competitor Watch
- [COMPETITOR] published [CONTENT] - [PERFORMANCE]
```

## Best Practices

1. **Recency Matters**: Always filter for last 7-14 days for trend data
2. **Cross-Platform**: What's viral on one platform often translates
3. **Speed**: First-mover advantage is real - act on trends quickly
4. **Validation**: Validate gut feelings with data before committing
5. **Iteration**: Track what works and refine your pattern recognition
