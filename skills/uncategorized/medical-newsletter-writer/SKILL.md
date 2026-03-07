---
name: medical-newsletter-writer
description: >
  Create evidence-based medical newsletters for interventional cardiologists in
  Eric Topol's authoritative Ground Truths style. Use when the user wants to
  analyze trending medical topics with engagement predictions, conduct
  data-driven topic selection, research medical literature using PubMed, or
  write comprehensive well-referenced newsletters that build professional
  authority. Handles complete workflow from trend analysis to final draft.
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---

# Medical Newsletter Writer

Create high-quality, evidence-based medical newsletters in the style of Eric Topol's Ground Truths. This skill guides the complete newsletter creation process: from analyzing your PDF of topic ideas, to deep PubMed research, to writing in Topol's distinctive authoritative-yet-accessible voice.

## Quick Start

**Simple 3-Step Process:**

1. **Upload PDF** - Upload your PDF with topic ideas in the chat
2. **Select Topic** - Review engagement predictions and pick one topic
3. **Get Newsletter** - Receive complete, publication-ready newsletter (~3,000 words with 20-30 PubMed citations)

The skill handles everything: PDF extraction, trend analysis, PubMed research, and writing in Eric Topol's exact voice.

## Complete Workflow

The newsletter creation process has 5 phases:

1. **Extract Topics from PDF** - Read user's uploaded PDF of topic ideas
2. **Trend Analysis** - Analyze each topic for engagement potential
3. **Topic Selection** - User approves topics based on data-driven predictions  
4. **Deep Research** - Comprehensive PubMed literature review
5. **Newsletter Writing** - Write complete newsletter in Topol's style

## Phase 1: Extract Topics from PDF

### PDF Upload
User will upload a PDF containing potential newsletter topic ideas in the chat.

### Extract Topics
- Read the PDF using available tools
- Extract all topic ideas mentioned
- Clean and organize the list
- If PDF contains notes/context about topics, capture that too

## Phase 2: Trend Analysis & Engagement Prediction

### Analyze Each Topic (Automatically)

For each topic extracted from the PDF, conduct comprehensive trend analysis:

**1. News Coverage (Google News, medical news sites)**
- Search past 30 days
- Note which outlets covering
- Identify breaking developments
- Count article frequency

**2. Search Interest**
- Use web_search to assess current discussion
- Look for rising interest signals
- Note if topic is trending

**3. Social Media Signals**
- YouTube: Search for videos, note view counts
- Check if medical professionals are discussing
- Assess virality potential

**4. Academic Momentum (PubMed)**
- Count recent publications (6 months)
- Check for major journal coverage
- Identify ongoing trials
- Note if field is active

### Engagement Prediction Scoring

For each topic, score 1-10 on:

1. **Readability**: Can this be explained clearly to physicians?
2. **Controversy**: Is there debate/opposing views?
3. **Clinical Relevance**: Will this affect patient care?
4. **Timeliness**: How current is this? Breaking news?
5. **Share Potential**: Will physicians share with colleagues?

**Overall Engagement Score** = Average of 5 metrics

### Present Analysis

Create comparison table with:
- Topic name
- Brief trend summary (2-3 sentences)
- Individual scores (1-10)
- Overall engagement score
- Priority recommendation (High/Medium/Low)

Sort by overall score, present top 5-10 topics to user.

## Phase 3: Topic Selection

Present findings to user with:
- Top topics by engagement prediction
- Rationale for scores
- Notable timeliness factors

**User selects ONE topic** - then the skill automatically proceeds to research and writing.

## Phase 4: Deep Research (Automatic)

### PubMed Search Strategy

Before searching, read **workflow.md** for detailed research guidance.

**Initial searches:**
1. Broad topic overview
2. Recent findings (<1 year)  
3. Systematic reviews/meta-analyses
4. Major clinical trials

**Paper Prioritization:**
- Tier 1: Large RCTs in NEJM, Lancet, JAMA, Science, Nature
- Tier 2: Meta-analyses and systematic reviews
- Tier 3: Large observational studies
- Tier 4: Mechanistic studies in high-impact journals
- Tier 5: Pre-clinical (use sparingly)

**Target:** 15-30 highly relevant papers

### Extract Key Information

For each major paper:
- Study design and sample size
- Key findings (quantitative)
- Limitations
- How it fits the narrative
- Potential quotes/figures

### Find Related Work
- Use PubMed related articles
- Check major paper citations
- Look for responses/commentary
- Identify consensus vs. controversy

## Phase 5: Newsletter Writing (Automatic)

### Before Writing

**CRITICAL: Read topol-style-guide.md first** - This contains essential voice patterns, phrases, and stylistic requirements.

### Structure

**Opening (1-2 paragraphs)**
- Hook using Topol's opening patterns (see style guide)
- Why this matters NOW
- What will be covered

**Background/Context (optional)**
- Define key terms: "To review: [term] is..."
- Historical perspective if relevant
- Current state of field

**Main Content (3-5 sections with clear headers)**
- Each section = one major subtopic
- Build logically
- Include data/studies in each
- Use tables to compare studies/treatments
- Reference figures from papers

**Implications/Future Directions**
- What this means for practice
- Research gaps
- What's next

**Bottom Line (required)**
- Synthesize key takeaways
- Clear conclusions based on evidence
- Call for more evidence if needed

**Standard Closing (required)**
```
Thanks for reading and subscribing to Ground Truths.

If you found this interesting PLEASE share it!

That makes the work involved in putting these together especially worthwhile.

All content on Ground Truths—its newsletters, analyses, and podcasts, are free, open-access.

Paid subscriptions are voluntary and all proceeds from them go to support Scripps Research. They do allow for posting comments and questions, which I do my best to respond to. Please don't hesitate to post comments and give me feedback. Let me know topics that you would like to see covered.
```

### Writing Requirements

**Voice & Style:**
- First person engaged ("I recently fielded questions...")
- Authoritative but accessible
- Critical and evidence-based
- Use Topol's signature phrases (see style guide)

**Citations:**
- EVERY factual claim needs a PubMed citation with hyperlink
- Format: [link text](URL) embedded in prose
- Cite original studies, not news articles
- Include author names for major findings: "Professor X and colleagues at Y University published in Z..."

**Critical Analysis:**
- Always discuss study limitations
- Note conflicts of interest if relevant
- Present alternative interpretations
- Flag when evidence is preliminary
- Call out hype vs. data

**Length:** 2,000-3,500 words

**Visual Elements:**
- Create tables comparing studies/treatments
- Describe figures from papers
- Use clear section headers

### Quality Checks

Before finalizing:
- [ ] Engaging opening hook?
- [ ] Clear why-this-matters framing?
- [ ] Every claim cited?
- [ ] Limitations discussed?
- [ ] Topol's voice consistent?
- [ ] Tables/figures included?
- [ ] Logical flow?
- [ ] "Bottom Line" section?
- [ ] Standard closing?
- [ ] 2,000-3,500 words?

## Delivery

### Final Format
- Complete newsletter in Markdown
- All hyperlinked citations to PubMed
- 2,000-3,500 words
- Ready for user's newsletter platform

### Customization Note
User may want to change "Scripps Research" in the standard closing to their own institution/practice name.

## Essential References

**ALWAYS READ BEFORE WRITING:**
- **topol-style-guide.md** - Complete guide to Topol's voice, phrases, patterns
- **workflow.md** - Detailed research and writing process

## Key Success Factors

1. **Evidence-based**: Every claim must be cited
2. **Critical thinking**: Discuss limitations, not just positives
3. **Voice consistency**: Sound like Topol throughout
4. **Comprehensive**: Cover topic thoroughly with multiple studies
5. **Accessible**: Technical accuracy without excessive jargon
6. **Timely**: Focus on recent developments
7. **Visual**: Include tables/figures to enhance understanding
8. **Engaging**: Hook readers immediately, maintain interest

## Example Opening Lines (Topol Style)

- "In fielding questions recently from patients and colleagues about [topic], I was prompted to look into the field at more depth."
- "[Term] was coined in the late [year]. Now, about [X] years later, we've yet to achieve [goal]."
- "This week [major development] was published in [journal]. Several important reports have since been published. I've incorporated them in this updated version."
- "There's no question that the use of [intervention] has surged, in part because of [claims], along with endorsements by [influencers]."

## Common Pitfalls to Avoid

- Don't rely on single studies - use multiple sources
- Don't ignore study limitations - they're critical
- Don't cherry-pick data - present full picture
- Don't get too technical - stay accessible
- Don't use bullet points excessively - prefer prose
- Don't skip the critical analysis - it's essential
- Don't forget visual elements - tables enhance understanding
- Don't deviate from Topol's voice - consistency matters
