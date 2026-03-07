# Long-Form Quality Pipeline

## Overview

Every long-form piece (YouTube script, newsletter, editorial, blog) must pass through this 4-stage quality pipeline before being marked as final.

---

## Stage 1: Scientific Critical Thinking

### Purpose
Verify evidence rigor, citation accuracy, and scientific validity.

### Checklist

**Evidence Quality:**
- [ ] Are claims supported by cited evidence?
- [ ] Are the cited studies from reputable sources (Q1 journals preferred)?
- [ ] Is the level of evidence appropriate for the claim strength?
- [ ] Are limitations of studies acknowledged?

**Statistical Accuracy:**
- [ ] Are statistics correctly stated (HR, RR, NNT, CI)?
- [ ] Are effect sizes accurately represented?
- [ ] Is statistical significance vs clinical significance distinguished?
- [ ] Are absolute vs relative risk clearly communicated?

**Interpretation:**
- [ ] Are study conclusions not overstated?
- [ ] Is correlation vs causation distinguished?
- [ ] Are confounders acknowledged?
- [ ] Is the generalizability to Indian population considered?

**Guideline Alignment:**
- [ ] Do recommendations align with current guidelines (ACC/ESC/ADA)?
- [ ] Are Class/Level of Evidence mentioned where appropriate?
- [ ] Are any deviations from guidelines explained?

### Output
- List of issues found (if any)
- Suggested corrections
- PASS / NEEDS REVISION

---

## Stage 2: Peer Review

### Purpose
Check methodology, logical consistency, and completeness.

### Checklist

**Logical Flow:**
- [ ] Does the argument progress logically?
- [ ] Are premises supported before conclusions?
- [ ] Are there logical fallacies? (strawman, false dichotomy, etc.)
- [ ] Is the narrative coherent?

**Completeness:**
- [ ] Are all relevant perspectives covered?
- [ ] Are counter-arguments addressed?
- [ ] Is important context included?
- [ ] Are practical implications discussed?

**Accuracy:**
- [ ] Are drug names, doses, and mechanisms correct?
- [ ] Are anatomical/physiological descriptions accurate?
- [ ] Are procedure descriptions correct?
- [ ] Are timelines and sequences accurate?

**Balance:**
- [ ] Is the tone appropriately balanced (not fear-mongering)?
- [ ] Are benefits AND risks discussed?
- [ ] Is nuance preserved (not oversimplified)?
- [ ] Are uncertainties acknowledged?

### Output
- List of issues found (if any)
- Suggested corrections
- PASS / NEEDS REVISION

---

## Stage 3: Content Reflection

### Purpose
Pre-publish quality assurance for audience appropriateness and clarity.

### Checklist

**Audience Fit:**
- [ ] Is the language appropriate for the target audience?
- [ ] Are technical terms explained (for patient-facing)?
- [ ] Is the depth appropriate (not too shallow, not too deep)?
- [ ] Will the audience find this actionable?

**Clarity:**
- [ ] Are sentences clear and not convoluted?
- [ ] Is jargon minimized or explained?
- [ ] Are analogies helpful and accurate?
- [ ] Is the structure easy to follow?

**Engagement:**
- [ ] Is there a strong hook?
- [ ] Does the content maintain interest throughout?
- [ ] Is there a clear takeaway?
- [ ] Is there an appropriate call to action?

**Practical Value:**
- [ ] Does the reader learn something useful?
- [ ] Can they apply this to their life/practice?
- [ ] Are next steps clear?
- [ ] Is the "so what" answered?

### Output
- List of issues found (if any)
- Suggested improvements
- PASS / NEEDS REVISION

---

## Stage 4: Authentic Voice

### Purpose
Remove AI patterns and ensure voice consistency.

### Anti-AI Patterns to Remove

**Phrases to NEVER use:**
- "It's important to note"
- "It's worth mentioning"
- "In conclusion"
- "stands as a testament"
- "Groundbreaking" / "Game-changing"
- "The key takeaway is"
- "Let's dive in" / "Let's explore"
- "Navigating the landscape"
- "At its core"
- "In the realm of"

**Patterns to AVOID:**
- Excessive em-dashes (—)
- Starting multiple sentences with "This"
- Overly formal transitions
- Generic summarizing phrases
- Hedging every statement

**Voice Consistency:**
- [ ] Does it sound like Dr. Shailesh Singh?
- [ ] Is the tone warm but authoritative?
- [ ] Are specific data points included (not vague claims)?
- [ ] Does it feel like a conversation, not a lecture?

**For Hinglish (YouTube):**
- [ ] Is the 70% Hindi / 30% English balance maintained?
- [ ] Are technical terms in English, narrative in Hindi?
- [ ] Are signature phrases used naturally?

**For English (Twitter/Writing):**
- [ ] Does it match Eric Topol / Peter Attia style?
- [ ] Are Q1 journals cited by name?
- [ ] Are statistics specific (not "studies show")?

### Output
- List of AI patterns found
- Rewritten sections
- PASS / NEEDS REVISION

---

## Pipeline Execution

### Sequence
```
Draft Content
    ↓
Stage 1: Scientific Critical Thinking
    ↓ (if PASS)
Stage 2: Peer Review
    ↓ (if PASS)
Stage 3: Content Reflection
    ↓ (if PASS)
Stage 4: Authentic Voice
    ↓ (if PASS)
FINAL (Quality Passed)
```

### If NEEDS REVISION
1. Apply suggested corrections
2. Re-run the failed stage
3. Continue pipeline from that point

### Quality Markers

Each final piece should be marked:
```
---
quality_passed: true
stages_completed:
  - scientific_critical_thinking: PASS
  - peer_review: PASS
  - content_reflection: PASS
  - authentic_voice: PASS
reviewed_at: [timestamp]
---
```
