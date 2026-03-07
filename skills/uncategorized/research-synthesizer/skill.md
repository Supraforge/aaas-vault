# Skill: Research Synthesizer

## Metadata
- **Name**: research-synthesizer
- **Version**: 1.0
- **Purpose**: Analyze YouTube research data and identify content opportunities
- **Token Budget**: Medium (Sonnet recommended)

---

## When to Use This Skill

Invoke when:
- Processing research engine output
- Analyzing competitor videos
- Identifying content gaps
- Creating idea briefs from raw data

---

## Input Data Expected

This skill processes output from the research engine:

```json
{
  "idea_id": "seed_001_mod_003",
  "seed_idea": "Statin side effects myths",
  "modifier": "myth-busting + data",
  "youtube_research": {
    "top_videos": [...],
    "total_views": 2500000,
    "avg_views": 250000,
    "comment_themes": [...],
    "transcript_insights": [...]
  }
}
```

---

## Analysis Framework

### 1. Demand Analysis
**Question**: Is there audience interest in this topic?

**Signals to check:**
- Total views across top 10 videos
- View velocity (views per day since publish)
- Search volume indicators
- Comment volume and engagement

**Scoring:**
| Signal | Low (1-3) | Medium (4-6) | High (7-10) |
|--------|-----------|--------------|-------------|
| Total views (top 10) | <500K | 500K-2M | >2M |
| Avg views per video | <50K | 50K-200K | >200K |
| Comments per video | <100 | 100-500 | >500 |

### 2. Gap Analysis
**Question**: What's missing in existing content?

**Gaps to identify:**
- **Angle gaps**: Topics covered but not from this perspective
- **Depth gaps**: Surface-level only, no deep-dives
- **Format gaps**: No Hinglish, no Indian context
- **Recency gaps**: Outdated information, no recent videos
- **Authority gaps**: No credentialed experts

**Gap Detection Process:**
1. List what existing videos cover
2. Identify what they DON'T cover
3. Find questions in comments that aren't answered
4. Check publish dates (>2 years = recency gap)
5. Check creator credentials

### 3. Competition Assessment
**Question**: Can we compete/win?

**Factors:**
- Channel size of top performers
- Production quality required
- Content depth of existing videos
- Engagement rates

**Competitive Positioning:**
| Their Strength | Our Counter |
|----------------|-------------|
| High production | Authenticity + expertise |
| English content | Hinglish accessibility |
| Generic health | Specialist cardiology |
| Western context | Indian-specific |
| Clickbait | Evidence-based trust |

### 4. Alignment Scoring
**Question**: How well does this fit our channel?

**Check against:**
- Content pillars (1-5 score)
- Target archetypes (which ones?)
- Expertise match (can we add value?)
- Hinglish potential (natural or forced?)

---

## Comment Theme Analysis

### Process:
1. Sample 50-100 comments from top videos
2. Categorize by type:
   - Questions (what they want to know)
   - Objections (what they doubt)
   - Stories (what they've experienced)
   - Requests (what they want more of)

### Theme Template:
```
## Comment Themes for: [Topic]

### Top Questions (Content Opportunities)
1. [Question theme] - [Frequency: X comments]
2. [Question theme] - [Frequency: X comments]

### Common Objections (Must Address)
1. [Objection] - "But what about..."
2. [Objection] - "This doesn't work because..."

### Personal Stories (Connection Points)
1. [Story pattern] - "My father had..."
2. [Story pattern] - "I experienced..."

### Explicit Requests
1. "[Request]" - X viewers asked for this
```

---

## Transcript Insight Extraction

### What to Extract:
- Key points covered
- Examples/analogies used
- Questions posed to audience
- Calls to action used
- What's missing/weak

### Transcript Analysis Template:
```
## Video: [Title]
**Channel**: [Name] | **Views**: [X] | **Length**: [X min]

### Content Covered:
- Point 1
- Point 2
- Point 3

### Effective Elements:
- Hook used: [describe]
- Best analogy: [quote]
- Engagement technique: [describe]

### Weaknesses/Gaps:
- Missing: [what wasn't covered]
- Weak: [what was poorly explained]
- Outdated: [what needs updating]

### Our Opportunity:
[How we can do this better]
```

---

## Output: Idea Brief

After analysis, generate an idea brief:

```markdown
# Idea Brief: [Title]

## Opportunity Score: [X/10]
- Demand: [X/10]
- Gap: [X/10]
- Competition: [X/10]
- Alignment: [X/10]

## The Opportunity
[2-3 sentence summary of why this is worth making]

## Target Audience
**Primary archetype**: [Name]
**Awareness level**: [Level]
**Key pain point addressed**: [Pain point]

## Content Angle
[How we'll approach this differently than existing content]

## Key Points to Cover
1. [Point 1]
2. [Point 2]
3. [Point 3]

## Must Address (from comments)
- [Question/objection 1]
- [Question/objection 2]

## Suggested Hook
[Hook concept based on research]

## Recommended Format
- **Length**: [X minutes]
- **Style**: [Educational/Story/Myth-bust/etc.]
- **Visuals**: [Any specific suggestions]

## Research Sources
- [Source 1]
- [Source 2]
- [Competitor video to reference]

## Priority: [HIGH/MEDIUM/LOW]
**Reason**: [Why this priority]
```

---

## Batch Processing Mode

When processing multiple ideas:

1. **Quick filter** (eliminate obvious low-potential)
2. **Score remaining** (all criteria)
3. **Rank by total score**
4. **Generate briefs** for top 20-30
5. **Final selection** to 100-day calendar

---

## Integration Points

- **Input from**: Research engine (YouTube API data)
- **Output to**: Content calendar, Script skill
- **Feeds into**: Hook generator, Script writer

---

*This skill transforms raw research into actionable content opportunities.*
