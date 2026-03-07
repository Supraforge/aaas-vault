# Brand QA Validation Criteria

## Scoring Components

### Voice Alignment (40% of total score)

| Dimension | Weight | What It Measures |
|-----------|--------|------------------|
| Tone Match | 40% | Keywords matching brand tone attributes |
| Formality | 20% | Appropriate level for brand |
| Style | 25% | Sentence variety, engagement elements |
| Readability | 15% | Appropriate complexity for audience |

**Tone Attributes by Brand:**

| Brand | Tone Attributes |
|-------|-----------------|
| [PROJECT_NAME] | Innovative, Precise, Empowering |
| SUPRA FORGE | Vitreous (transparent), Authoritative, Calm |

### Terminology Compliance (35% of total score)

| Check | Points | Criteria |
|-------|--------|----------|
| Required Terms | 50 max | Meeting minimum (2) required terms |
| Preferred Phrases | 30 max | 10 points per phrase (max 3) |
| Anti-Pattern Penalty | -15 each | Per violation found |

**Required Minimum Terms:** 2

### Readability (25% of total score)

Based on Flesch Reading Ease:

| Score | Level | Target Audience |
|-------|-------|-----------------|
| 80-100 | Easy | General public |
| 60-79 | Standard | Business professionals |
| 40-59 | Moderately difficult | Technical audience |
| 0-39 | Difficult | Specialists only |

**Target for [PROJECT_NAME]/SUPRA FORGE:** 50-70 (technical but accessible)

---

## Grade Thresholds

| Score | Grade | Label | Action |
|-------|-------|-------|--------|
| 90-100 | A | Excellent | Ready to publish |
| 80-89 | B | Good | Minor tweaks optional |
| 70-79 | C | Acceptable | Review recommendations |
| 60-69 | D | Needs Work | Address issues before publishing |
| 0-59 | F | Significant Revision | Major rewrite needed |

**Default Pass Threshold:** 80

---

## Required Terms Checklist

### [PROJECT_NAME] Brand

At minimum, content should include 2 of:

- [ ] Neural Quality Layer
- [ ] Golden Thread
- [ ] See the Risk Before It Sees You
- [ ] Audit Blindness
- [ ] Manual Compliance Tax
- [ ] Real-Time Audit Companion

### SUPRA FORGE Brand

All [PROJECT_NAME] terms plus:

- [ ] Waze for Compliance
- [ ] Benevolent Omniscience
- [ ] Quality. Engineered. Not Administered.

---

## Anti-Pattern Severity Levels

### High Severity (Always Fix)

| Avoid | Use Instead |
|-------|-------------|
| "AI tool" | "Neural Quality Layer" |
| "AI magic" | "evidence-based analysis" |
| "audit the engineers" | "audit the artifacts" |
| "replaces" | "empowers" |

### Medium Severity (Fix When Possible)

| Avoid | Use Instead |
|-------|-------------|
| "compliance tool" | "Real-Time Audit Companion" |
| "machine learning solution" | "Neuro-Symbolic architecture" |
| "checks your code" | "scans for architecture erosion" |
| "helps you manage" | "ensures continuous visibility" |

### Low Severity (Consider Context)

| Avoid | Use Instead |
|-------|-------------|
| "delayed feedback" | "late visibility" |
| "fast compliance" | "compliance at the speed of code" |
| "simple" | "streamlined" |
| "easy" | "efficient" |

---

## Voice Fingerprint Guidelines

### Sentence Patterns

1. **Bold Statement**: [Contrarian claim]. [Reframe]. [Question].
2. **Quantified Problem**: [Metric] of [audience] [problem]. [Why it matters].
3. **Reframe**: The problem isn't [obvious thing]. The problem is [root cause].
4. **Before/After**: [Before state]. [After state]. [Bridge].

### Engagement Elements

- Use rhetorical questions (adds +10 points per question, max +20)
- Quantify everything (40%, 3 months, 10x)
- Challenge conventional wisdom
- End with thought-provoking question

### What to Avoid

- Walls of text without breaks
- Generic marketing speak
- Buzzwords without substance
- Passive voice (prefer active)
- Hedging language ("might", "could", "possibly")

---

## Content-Specific Thresholds

| Content Type | Recommended Threshold |
|--------------|----------------------|
| LinkedIn Post | 80 |
| Press Release | 85 |
| Email Sequence | 75 |
| Website Copy | 85 |
| Internal Docs | 60 |
| Ad Copy | 80 |
| Investor Update | 80 |

---

## Validation Workflow

```
1. Write content
   ↓
2. Run consistency_scorer.py
   ↓
3. Review score and grade
   ↓
4. If score < threshold:
   a. Address high-priority recommendations first
   b. Fix anti-pattern violations
   c. Add required terminology naturally
   d. Re-run validation
   ↓
5. If score >= threshold:
   → Ready for publishing/review
```
