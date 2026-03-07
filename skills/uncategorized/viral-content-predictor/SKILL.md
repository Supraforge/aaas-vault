---
name: viral-content-predictor
description: >
  Analyzes medical education content ideas from PDFs/DOCX files to predict viral
  potential (views, likes, shares, AVD) and provides actionable insights. Use
  when the user needs to evaluate content ideas for engagement potential, get
  predictive analytics on video performance, research trending topics in
  medical/health niches, analyze YouTube comments and audience sentiment,
  identify knowledge gaps and myths, or prioritize content ideas based on viral
  likelihood.
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---

# Viral Content Predictor for Medical Education

This skill analyzes healthcare/medical education content ideas and predicts their viral potential using multi-factor analysis, trend research, and YouTube audience insights.

## Core Capabilities

1. **Content Idea Analysis**: Extract and score content ideas from uploaded documents
2. **Viral Potential Prediction**: Estimate views, engagement, and AVD based on multiple factors
3. **Trend Research**: Identify hot topics and emerging trends in medical education
4. **Audience Intelligence**: Analyze YouTube comments to understand knowledge gaps and concerns
5. **Content Optimization**: Provide subtopics, myths to address, and structural recommendations

## Workflow

### Phase 1: Content Extraction & Initial Scoring

When the user provides PDF/DOCX files with content ideas:

1. **Extract all content ideas** from the document
2. **Initial categorization** by topic, complexity, and format
3. **Preliminary viral score** (0-100) based on:
   - Topic relevance and timeliness
   - Emotional appeal (fear, hope, relief, empowerment)
   - Searchability and SEO potential
   - Educational value vs entertainment balance
   - Novelty factor

### Phase 2: Deep Research & Validation

For top-scoring ideas (score >70) or user-selected ideas:

1. **Search current trends**: Use web_search to find:
   - Recent high-performing videos on the topic
   - News articles and medical publications
   - Reddit/forum discussions
   - Trending searches related to the topic

2. **Competitive analysis**:
   - Identify top-performing videos in the niche
   - Analyze view counts, engagement ratios, and video length
   - Note common patterns and differentiators

3. **Knowledge gap identification**:
   - What questions are people asking?
   - What misconceptions exist?
   - What information is missing from existing content?

### Phase 3: Predictive Analytics

For each analyzed idea, calculate:

1. **Predicted View Range**: Based on:
   - Search volume data (estimated from trends)
   - Similar video performance benchmarks
   - Topic saturation level
   - Seasonal/temporal relevance
   - Channel authority factor (assumed moderate for interventional cardiology niche)

2. **Engagement Prediction**:
   - Estimated likes, shares, comments
   - Expected like-to-view ratio
   - Share potential score

3. **AVD (Average View Duration) Optimization Score**:
   - Topic retention potential (inherent interest)
   - Complexity level (optimal: moderate complexity for patient education)
   - Hook strength assessment
   - Pacing recommendations

### Phase 4: Content Blueprint

For prioritized ideas, provide:

1. **Video Structure Recommendation**:
   - Optimal video length
   - Hook suggestions (first 10 seconds)
   - Chapter breakdown with timestamps
   - Pacing guidance for high retention

2. **Subtopics to Include** (in priority order):
   - Core information (must-have)
   - High-interest tangents (AVD boosters)
   - Myth-busting segments (engagement drivers)
   - Practical takeaways (satisfaction & shareability)

3. **Psychological Triggers to Address**:
   - Common fears related to the topic
   - Misconceptions to debunk
   - Hope/empowerment angles
   - Trust-building elements

4. **SEO & Discoverability**:
   - Title suggestions (tested patterns)
   - Thumbnail concepts
   - Keyword recommendations
   - Description template

## Scoring Methodology

### Viral Potential Score (0-100)

**Topic Factors (40 points)**:
- Search demand: 15 pts (estimated from trend data)
- Emotional resonance: 10 pts (fear, hope, curiosity)
- Timeliness: 10 pts (recent news, seasonal relevance)
- Novelty: 5 pts (unique angle or new information)

**Engagement Factors (30 points)**:
- Shareability: 10 pts (will people send to family/friends?)
- Comment-worthiness: 10 pts (controversial or discussion-inducing?)
- Practical value: 10 pts (actionable information)

**Retention Factors (30 points)**:
- Hook potential: 10 pts (compelling opening)
- Information density: 10 pts (value per minute)
- Narrative flow: 10 pts (story or logical progression)

### View Prediction Formula

```
Estimated Views = Base_Audience × Topic_Multiplier × Quality_Factor × Trend_Factor

Where:
- Base_Audience: 5,000-15,000 (typical for established medical education channel)
- Topic_Multiplier: 0.5-10.0 (based on search volume and competition)
- Quality_Factor: 0.8-1.5 (based on production quality, assumed 1.0)
- Trend_Factor: 0.5-3.0 (based on current trending status)

Range Output: 
- Minimum (conservative): Lower quartile estimate
- Expected (median): Most likely scenario
- Maximum (optimistic): Upper quartile with viral potential
```

## Research Tools & Techniques

### Web Search Strategies

When researching topics, use these search patterns:

1. **Trend identification**:
   - "[topic] latest research 2024"
   - "most common questions about [topic]"
   - "[topic] myths debunked"

2. **Audience analysis**:
   - "reddit [topic] patient experience"
   - "[topic] what to expect forum"
   - "[topic] success stories"

3. **Competition analysis**:
   - "[topic] youtube popular"
   - "how to explain [topic] to patients"
   - "[topic] doctor explains"

### YouTube Comment Analysis Strategy

When the user provides a topic or video URL:

1. Search for top 5-10 videos on the topic
2. Analyze comment patterns for:
   - Most frequently asked questions
   - Common confusions or misconceptions
   - Emotional reactions (fear, gratitude, skepticism)
   - Requests for specific information
   - Demographic clues (age, situation)

3. Categorize insights into:
   - **Knowledge gaps**: What people don't understand
   - **Fears**: What worries them
   - **Desires**: What they hope to learn
   - **Trust signals**: What builds credibility

## Output Format

### Content Idea Report

For each analyzed idea, provide:

```markdown
## [Content Idea Title]

### 🎯 Viral Potential Score: [X/100]

**Predicted Performance**:
- Views: [min - expected - max]
- Like Ratio: [X%]
- AVD: [X:XX - Y:YY minutes]
- Shareability: [Low/Medium/High]

### 📊 Analysis

**Strengths**:
- [Key strength 1]
- [Key strength 2]

**Opportunities**:
- [Improvement area 1]
- [Improvement area 2]

**Market Insights**:
- Current search trends: [summary]
- Competition level: [Low/Medium/High]
- Audience demand: [description]

### 🎬 Content Blueprint

**Optimal Length**: [X-Y minutes]

**Video Structure**:
1. Hook (0:00-0:10): [specific suggestion]
2. Problem Setup (0:10-1:00): [what to cover]
3. Core Education (1:00-[X]:00): [main content]
4. Myth-Busting ([X]:00-[Y]:00): [misconceptions to address]
5. Practical Takeaways ([Y]:00-end): [actionable advice]

**Essential Subtopics** (in order of priority):
1. [Subtopic 1] - [why it matters for AVD]
2. [Subtopic 2] - [why it matters for AVD]
3. [Subtopic 3] - [why it matters for AVD]

**Knowledge Gaps to Address**:
- [Gap 1] - [source: YouTube comments/Reddit/forums]
- [Gap 2] - [source]

**Myths & Misconceptions**:
- [Myth 1] - [prevalence & why it persists]
- [Myth 2] - [prevalence & why it persists]

**Emotional Hooks**:
- Fear to address: [specific patient fear]
- Hope to provide: [specific positive outcome]
- Empowerment angle: [how viewers take control]

**SEO Recommendations**:
- Primary keyword: [keyword]
- Title suggestions:
  1. [Title option 1]
  2. [Title option 2]
  3. [Title option 3]
- Thumbnail concept: [description]

### 🔥 Hot Take / Unique Angle

[One compelling angle that differentiates this from existing content]
```

### Trend Report

When analyzing current trends:

```markdown
## 🚀 Trending Topics in [Niche]

### High Priority (Create ASAP)
1. **[Topic]** - Viral Score: [X/100]
   - Why now: [reason for timeliness]
   - Quick summary: [one-liner]
   
### Medium Priority (Plan for Next Month)
[Similar format]

### Emerging Trends (Watch Closely)
[Similar format]

### Seasonal Opportunities
[Upcoming events/seasons that create content opportunities]
```

## Best Practices

### For Medical Education Content

1. **Balance authority with accessibility**: Use simple language but demonstrate expertise
2. **Lead with empathy**: Acknowledge fears and concerns first
3. **Provide hope**: Always include positive outcomes or management strategies
4. **Be specific**: Concrete examples outperform abstractions
5. **Use visual analogies**: Help patients visualize complex concepts
6. **Address "why"**: Explain mechanisms, not just recommendations
7. **Anticipate objections**: Address common pushback or skepticism
8. **Include patient stories**: Anonymized cases increase retention
9. **End with empowerment**: Clear next steps or takeaways

### AVD Optimization Tactics

1. **Pattern interrupt every 60-90 seconds**: Change visual, topic, or energy
2. **Open loops**: Tease information that comes later
3. **Progress indicators**: "Three things you need to know..."
4. **Highlight surprising facts**: "Most people don't know..."
5. **Use conversational pacing**: Speak as if to one person
6. **Strategic repetition**: Reinforce key points without being boring
7. **Maintain momentum**: Cut dead air and unnecessary transitions

## Reference Files

- **references/medical-content-patterns.md**: Analysis of high-performing medical YouTube content patterns
- **references/cardiology-keywords.md**: SEO-optimized keywords for cardiology topics
- **references/avd-tactics.md**: Advanced retention strategies specific to educational content

## When to Use Multiple Research Iterations

For content ideas scoring 85+:
1. Run initial analysis
2. Conduct deep competitive research
3. Search for recent medical publications
4. Analyze comment sections of top 5 competing videos
5. Check Reddit/forums for patient perspectives
6. Synthesize into comprehensive blueprint

This ensures the highest-potential ideas get the deepest analysis.
