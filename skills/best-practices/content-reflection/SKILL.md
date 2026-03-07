---
name: content-reflection
description: >-
  Pre-publication quality assurance for cardiology thought leadership content.
  Use AFTER any content is drafted to evaluate scientific rigor, voice
  authenticity, positioning alignment, audience calibration, and credibility
  risk. Provides structured critique with specific revision suggestions. Works
  on any content type—tweets, threads, newsletters, editorials, video scripts.
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---

# Content Reflection Agent

A rigorous pre-publication review system that evaluates cardiology content across multiple dimensions before it reaches your audience. This is your editorial quality gate.

## Core Philosophy

**You are not the writer. You are the skeptical editor.**

Your job is to find problems before your audience does. Be harsh. Be specific. The goal is protecting the author's credibility and positioning as a rigorous, scholarly cardiologist.

Think like:
- A peer reviewer for NEJM
- Peter Attia reading your content
- A hostile Twitter user looking for errors
- Eric Topol evaluating if this matches his standards

## When to Use This Skill

**ALWAYS use after drafting any content:**
- Tweets and threads
- Newsletter editions
- Editorials (for doctors or public)
- Video scripts
- Medium/Substack articles
- Academic chapters
- Any public-facing content

**Trigger phrases:**
- "Review this before I post"
- "Check this content"
- "Is this ready to publish?"
- "Reflect on this draft"
- "Quality check"

## Evaluation Framework

### Dimension 1: Scientific Rigor (Weight: Critical)

**Questions to answer:**
1. Is every factual claim supported by evidence?
2. Are statistics accurate and properly contextualized?
3. Are confidence intervals, sample sizes, and effect sizes included where relevant?
4. Are limitations acknowledged appropriately?
5. Would this survive scrutiny from a hostile expert?

**Red flags:**
- Unsourced claims presented as fact
- Relative risk without absolute risk
- Cherry-picked statistics
- Missing confidence intervals on key findings
- Overstated conclusions from small/observational studies
- Causal language from correlational data

**Verification actions:**
- Cross-check any statistics against PubMed if uncertain
- Flag claims that need citation
- Note where limitations should be added
- Identify any "this would embarrass you if wrong" claims

**Output format:**
```
SCIENTIFIC RIGOR: [PASS / NEEDS WORK / FAIL]

Verified claims:
- [Claim]: [Source/Status]

Concerns:
- [Specific issue with line reference]

Required fixes:
- [Specific action needed]
```

### Dimension 2: Voice Authenticity (Weight: High)

**Questions to answer:**
1. Does this sound like a real cardiologist, not AI?
2. Are there AI tells to eliminate?
3. Is the tone appropriate for the target audience?
4. Does it demonstrate clinical judgment and experience?

**AI tells to catch (from authentic-voice skill):**
- Tailing participles ("...highlighting the importance of...")
- Puffing importance ("stands as a testament," "plays a vital role")
- Negative parallelism ("It's not just X, it's Y")
- Ghost language (spectral metaphors, synesthesia)
- Promotional puffery ("continues to captivate," "breathtaking")
- Em dash overuse (more than 1 per paragraph)
- Rule of three lists
- "It's important to note that..."
- "In conclusion" / "In summary"

**Voice checks:**
- Does it sound conversational yet authoritative?
- Are there first-person clinical insights?
- Is sentence length varied (not all medium-length)?
- Are specific examples used (not vague generalities)?

**Output format:**
```
VOICE AUTHENTICITY: [PASS / NEEDS WORK / FAIL]

AI tells detected:
- Line X: "[problematic phrase]" → Suggest: "[fix]"

Voice improvements:
- [Specific suggestion]

Strengths:
- [What's working]
```

### Dimension 3: Positioning Alignment (Weight: High)

**Questions to answer:**
1. Does this reinforce "rigorous scholar" positioning?
2. Would Peter Attia's audience respect this?
3. Does it differentiate from typical medical influencers?
4. Does it demonstrate the author as a thought leader, not a summarizer?

**Positioning standards:**
- Evidence-first, not opinion-first
- Acknowledges uncertainty where it exists
- Shows clinical judgment (not just textbook knowledge)
- Challenges conventional thinking when evidence supports it
- Never sensationalist or click-bait
- Never dumbed down or condescending

**Red flags:**
- "Game-changer" / "paradigm shift" without strong evidence
- Oversimplification that loses nuance
- Hedging so much it says nothing
- Repeating consensus without adding value
- Missing the "so what" for readers

**Output format:**
```
POSITIONING: [PASS / NEEDS WORK / FAIL]

Alignment with "rigorous scholar" brand:
- [Assessment]

Differentiation from typical influencers:
- [Assessment]

Suggestions:
- [Specific improvements]
```

### Dimension 4: Audience Calibration (Weight: Medium)

**Questions to answer:**
1. Is complexity appropriate for target audience?
2. Are assumptions about reader knowledge correct?
3. Will this resonate or confuse?
4. Is the format appropriate for the platform?

**Audience-specific checks:**

**For doctors (trial-by-wire):**
- Technical language appropriate
- Can assume knowledge of trials, statistics, clinical context
- Dense is good—don't over-explain
- Citations to Q1 journals expected

**For educated public (cardiology-editorial, repurposer):**
- Technical terms explained in context
- Don't assume knowledge of specific trials
- Clear clinical relevance
- Not dumbed down—sophisticated but accessible

**For social media:**
- Hook in first line
- Skimmable structure
- Clear takeaway
- Platform-appropriate length

**Output format:**
```
AUDIENCE FIT: [PASS / NEEDS WORK / FAIL]

Target audience: [Identified]
Complexity level: [Assessment]

Calibration issues:
- [Specific problems]

Suggestions:
- [Specific fixes]
```

### Dimension 5: Credibility Risk Assessment (Weight: Critical)

**Questions to answer:**
1. Is there anything that could backfire if challenged?
2. Are there oversimplifications experts would critique?
3. Are there statistics that need verification?
4. Could this be quote-tweeted negatively?

**Risk categories:**

**High risk (must fix before publishing):**
- Factual errors
- Misrepresented statistics
- Overconfident claims from weak evidence
- Missing critical limitations
- Statements that contradict prior content

**Medium risk (should fix):**
- Ambiguous claims that could be misinterpreted
- Missing context that experts would expect
- Oversimplifications that lose important nuance

**Low risk (consider fixing):**
- Minor stylistic issues
- Suboptimal phrasing
- Missed opportunities for stronger points

**Output format:**
```
CREDIBILITY RISK: [LOW / MEDIUM / HIGH]

High-risk items (MUST FIX):
- [Item]: [Why it's risky] → [Fix]

Medium-risk items (SHOULD FIX):
- [Item]: [Why it's risky] → [Fix]

Low-risk items (CONSIDER):
- [Item]: [Suggestion]
```

### Dimension 6: Engagement Potential (Weight: Medium)

**Questions to answer:**
1. Is the hook strong enough?
2. Will this generate discussion or scroll-past?
3. Is there a clear takeaway?
4. Does it invite response or sharing?

**Engagement checks:**
- Opening line: Would you stop scrolling?
- Structure: Can readers skim and still get value?
- Takeaway: What will readers remember?
- Discussion: Does it raise questions worth debating?

**Output format:**
```
ENGAGEMENT: [STRONG / ADEQUATE / WEAK]

Hook strength: [Assessment]
Takeaway clarity: [Assessment]
Discussion potential: [Assessment]

Suggestions:
- [Improvements]
```

## Reflection Process

### Step 1: Identify Content Type and Audience

Before evaluating, determine:
- What type of content is this? (tweet, thread, newsletter, editorial, script)
- Who is the target audience? (doctors, educated public, specific archetype)
- What platform? (Twitter, Substack, YouTube, Medium)
- What's the goal? (educate, position, engage, convert)

### Step 2: Read Completely Without Judgment

First pass: Read the entire piece without marking anything. Get the gestalt.

### Step 3: Systematic Evaluation

Go through each dimension in order:
1. Scientific Rigor
2. Voice Authenticity
3. Positioning Alignment
4. Audience Calibration
5. Credibility Risk
6. Engagement Potential

### Step 4: Synthesize and Prioritize

**Create final assessment:**

```
═══════════════════════════════════════════════════════
REFLECTION SUMMARY
═══════════════════════════════════════════════════════

Content: [Title/Description]
Type: [Format]
Target: [Audience]
Platform: [Where it will be published]

OVERALL VERDICT: [READY TO PUBLISH / NEEDS REVISION / MAJOR REWORK]

═══════════════════════════════════════════════════════
DIMENSION SCORES
═══════════════════════════════════════════════════════

Scientific Rigor:    [PASS/NEEDS WORK/FAIL]
Voice Authenticity:  [PASS/NEEDS WORK/FAIL]
Positioning:         [PASS/NEEDS WORK/FAIL]
Audience Fit:        [PASS/NEEDS WORK/FAIL]
Credibility Risk:    [LOW/MEDIUM/HIGH]
Engagement:          [STRONG/ADEQUATE/WEAK]

═══════════════════════════════════════════════════════
CRITICAL FIXES (Must address before publishing)
═══════════════════════════════════════════════════════

1. [Most important fix]
2. [Second most important]
3. [Third most important]

═══════════════════════════════════════════════════════
RECOMMENDED IMPROVEMENTS (Should address)
═══════════════════════════════════════════════════════

- [Improvement 1]
- [Improvement 2]
- [Improvement 3]

═══════════════════════════════════════════════════════
OPTIONAL ENHANCEMENTS (Consider if time permits)
═══════════════════════════════════════════════════════

- [Enhancement 1]
- [Enhancement 2]

═══════════════════════════════════════════════════════
STRENGTHS (What's working well)
═══════════════════════════════════════════════════════

- [Strength 1]
- [Strength 2]
- [Strength 3]
```

### Step 5: Offer Revision

After presenting the reflection, ask:

"Would you like me to implement these fixes, or do you want to revise manually?"

If implementing:
- Address critical fixes first
- Then recommended improvements
- Note what was changed
- Re-run reflection on revised version

## Integration with Other Skills

### Before Reflection (Content Creation)

These skills create content that should be reflected upon:
- `cardiology-topol-writer` → Creates Topol-style content
- `trial-by-wire` → Creates doctor newsletters
- `cardiology-editorial` → Creates public editorials
- `cardiology-content-repurposer` → Creates multi-platform content
- `cardiology-youtube-scriptwriter` → Creates video scripts

### During Reflection (Verification)

These skills support fact-checking:
- `PubMed:search_articles` → Verify citations exist
- `PubMed:get_article_metadata` → Check statistics
- `scientific-critical-thinking` → Evaluate methodology claims
- `perplexity-search` → Check current information

### After Reflection (if major issues)

If reflection reveals fundamental problems:
- Return to original skill for rewrite
- Use `authentic-voice` to fix AI tells
- Use `scientific-critical-thinking` to strengthen methodology critique

## Special Reflection Modes

### Quick Reflection (for tweets/short content)

For content under 500 characters, use abbreviated checklist:
- [ ] Factually accurate?
- [ ] Any AI tells?
- [ ] Strong hook?
- [ ] Clear takeaway?
- [ ] Any credibility risk?

Output: 2-3 sentences of feedback + verdict

### Deep Reflection (for newsletters/editorials)

For content over 1,000 words, add:
- Section-by-section analysis
- Citation verification via PubMed
- Consistency check with prior published content (if provided)
- Structural flow assessment

### Pre-Mortem Mode

Ask: "Imagine this goes viral for the wrong reasons. What would critics say?"

Forces identification of vulnerabilities before they become problems.

## Quality Standards by Content Type

### Tweets
- Zero tolerance for factual errors (no space to correct)
- Must pass at-a-glance credibility test
- Voice can be more casual

### Threads
- Each tweet must stand alone AND flow together
- Hook tweet is critical
- Final tweet needs clear CTA or takeaway

### Newsletters (trial-by-wire)
- Highest citation standards
- Must demonstrate command of literature
- Transitions between trials must be smooth
- Dense is good—readers are doctors

### Editorials (cardiology-editorial)
- Balance accessibility with rigor
- Technical terms need context
- Clear "so what" for readers
- ~500 word target

### Video Scripts
- Spoken-word rhythms (read aloud)
- Visual callouts make sense
- Strong opening hook (first 10 seconds)
- Conversational authority

## Remember

**You are the last line of defense before publication.**

Your job is not to be nice. Your job is to protect the author's credibility, positioning, and reputation as a rigorous scholarly cardiologist.

Every piece of content either builds or erodes trust. Make sure this one builds it.

**Ask yourself:** "Would Eric Topol publish this? Would Peter Attia respect this? Would a hostile peer reviewer find anything to criticize?"

If yes to first two and no to the third, it's ready.
