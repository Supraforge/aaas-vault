# Content OS Orchestrator Instructions

## When User Says "Content OS: [input]"

Follow these instructions exactly.

---

## Step 0: Detect Mode

### Forward Mode
If input is a **topic/idea** (short phrase, question, concept, < 500 words):
→ Go to **Forward Mode Pipeline**

### Backward Mode
If input is **existing content** (long text, > 500 words, article/script/newsletter):
→ Go to **Backward Mode Pipeline**

---

## FORWARD MODE PIPELINE

### Phase 1: Research

**1.1 Create output directory**
```
/output/content-os/[topic-slug]/
├── research/
├── long-form/
├── short-form/
└── visual/
```

**1.2 Research with PubMed MCP**
- Use `pubmed_search_articles` to find relevant papers
- Focus on: trials, meta-analyses, guidelines
- Get 10-20 most relevant results

**1.3 Research with knowledge-pipeline**
- Query AstraDB for guidelines (ACC/ESC/ADA)
- Get textbook context if relevant
- Synthesize with PubMed findings

**1.4 Save research brief**
- Write comprehensive research-brief.md to `/research/`
- Include: key findings, statistics, citations, guidelines
- This is the foundation for ALL content

### Phase 2: Long-Form Content (Full Quality Pipeline)

For EACH long-form piece:

**2.1 YouTube Script**
- Invoke `youtube-script-master` skill patterns
- Write Hinglish script (70% Hindi / 30% English)
- Run through quality pipeline:
  1. Scientific critical thinking pass
  2. Peer review pass
  3. Content reflection pass
  4. Authentic voice pass
- Save to `/long-form/youtube-script.md`

**2.2 Newsletter B2C (Patient-facing)**
- Invoke `cardiology-newsletter-writer` skill patterns
- Write accessible patient newsletter
- Run through quality pipeline (all 4 stages)
- Save to `/long-form/newsletter-b2c.md`

**2.3 Newsletter B2B (Doctor-facing)**
- Invoke `medical-newsletter-writer` skill patterns
- Write clinical/evidence-focused newsletter
- Run through quality pipeline (all 4 stages)
- Save to `/long-form/newsletter-b2b.md`

**2.4 Editorial**
- Invoke `cardiology-editorial` skill patterns
- Write Eric Topol-style editorial
- Run through quality pipeline (all 4 stages)
- Save to `/long-form/editorial.md`

**2.5 Blog Post**
- Invoke `cardiology-writer` skill patterns
- Write SEO-optimized blog
- Run through quality pipeline (all 4 stages)
- Save to `/long-form/blog.md`

### Phase 3: Short-Form Content (Quick Accuracy Pass)

**3.1 Tweets**
- Invoke `x-post-creator-skill` patterns
- Generate 5-10 tweets from different angles
- Run quick accuracy pass (data interpretation check)
- Save to `/short-form/tweets.md`

**3.2 Thread**
- Invoke `twitter-longform-medical` patterns
- Generate thread (condensed version of topic)
- Run quick accuracy pass
- Save to `/short-form/thread.md`

**3.3 Carousel Content**
- Extract key points for slides
- Format for carousel-generator input
- Save to `/short-form/carousel-content.md`

### Phase 4: Visual Content

**4.1 Generate Carousel**
- Use `/short-form/carousel-content.md` as input
- Invoke `carousel-generator` tool
- Generate slides to `/visual/carousel/`

**4.2 Infographic Concepts (if data-heavy)**
- If topic has significant data/charts
- Write infographic concepts
- Save to `/visual/infographic-concepts.md`

### Phase 5: Summary

Create `/summary.md`:
```markdown
# Content OS Output: [Topic]

## Generated: [timestamp]

## Long-Form (Quality Passed)
- [ ] YouTube Script: `/long-form/youtube-script.md`
- [ ] Newsletter B2C: `/long-form/newsletter-b2c.md`
- [ ] Newsletter B2B: `/long-form/newsletter-b2b.md`
- [ ] Editorial: `/long-form/editorial.md`
- [ ] Blog: `/long-form/blog.md`

## Short-Form (Accuracy Checked)
- [ ] Tweets (X): `/short-form/tweets.md`
- [ ] Thread: `/short-form/thread.md`
- [ ] Carousel content: `/short-form/carousel-content.md`

## Visual
- [ ] Carousel slides: `/visual/carousel/`
- [ ] Infographic concepts: `/visual/infographic-concepts.md`

## Research Foundation
- Research brief: `/research/research-brief.md`
```

---

## BACKWARD MODE PIPELINE

### Phase 1: Analyze Input

**1.1 Parse long-form content**
- Identify content type (script/newsletter/blog/etc.)
- Extract main topic/theme
- Note key data points, statistics, claims
- Identify quotable sections

**1.2 Create output directory**
```
/output/content-os/repurposed-[slug]/
├── analysis/
├── short-form/
└── visual/
```

**1.3 Save analysis**
- Write content analysis to `/analysis/`
- Include: key points, data extracted, structure

### Phase 2: Generate Short-Form

**2.1 Tweets**
- Extract 5-10 key points
- One insight per tweet
- Run quick accuracy pass
- Save to `/short-form/tweets.md`

**2.2 Thread**
- Condense narrative to 5-10 tweet thread
- Maintain logical flow
- Run quick accuracy pass
- Save to `/short-form/thread.md`

**2.3 Snippets**
- Extract quotable sections
- Format as standalone insights
- Save to `/short-form/snippets.md`

**2.4 Carousel Content**
- Extract visual-friendly points
- Format for slides
- Save to `/short-form/carousel-content.md`

### Phase 3: Visual

**3.1 Generate Carousel**
- Use extracted content
- Generate slides
- Save to `/visual/carousel/`

### Phase 4: Summary

Create summary of all repurposed content.

---

## Quality Pipeline Execution

### For Long-Form (MUST DO ALL 4 STAGES)

```
STAGE 1: Scientific Critical Thinking
├── Check evidence quality
├── Verify statistics
├── Confirm guideline alignment
└── Output: PASS or list issues

STAGE 2: Peer Review
├── Check logical flow
├── Verify completeness
├── Confirm accuracy
└── Output: PASS or list issues

STAGE 3: Content Reflection
├── Check audience fit
├── Verify clarity
├── Confirm engagement
└── Output: PASS or list issues

STAGE 4: Authentic Voice
├── Remove AI patterns
├── Check voice consistency
├── Apply style guide
└── Output: PASS or list issues
```

If any stage fails: Fix issues, re-run that stage.

### For Short-Form (QUICK PASS ONLY)

```
ACCURACY CHECK
├── Identify data claims
├── Verify against research brief
├── Flag any misinterpretations
└── Output: ACCURATE or list corrections
```

---

## Customization Handling

If user specifies constraints:

| User Says | Action |
|-----------|--------|
| "only YouTube and tweets" | Skip newsletter, editorial, blog |
| "skip editorial" | Skip editorial only |
| "long-form only" | Skip tweets, thread, carousel |
| "short-form only" | Skip YouTube, newsletters, editorial, blog |

---

## Progress Updates

Keep user informed:
- "Starting research phase..."
- "Research complete. Beginning long-form content..."
- "YouTube script drafted. Running quality pipeline..."
- "Quality passed. Moving to newsletter..."
- "Long-form complete. Generating short-form..."
- "All content generated. Creating summary..."

---

## Error Handling

If a skill fails:
1. Note the error
2. Continue with other content
3. Report in summary what couldn't be generated
4. Suggest manual intervention if needed

---

## Final Checklist

Before marking complete:

- [ ] All requested content types generated
- [ ] Long-form passed quality pipeline
- [ ] Short-form passed accuracy check
- [ ] Visual content generated
- [ ] Summary file created
- [ ] User notified of completion
