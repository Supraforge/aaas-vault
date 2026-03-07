---
name: ensemble-content-scorer
description: >-
  Multi-model consensus scoring for content ideas. Scores the same idea with
  Claude, GPT-4o, Gemini, and Grok in parallel, then aggregates for a balanced
  verdict. Reduces single-model bias and improves viral predictions.
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---
# Ensemble Content Scorer

**Wisdom of crowds, but for AI.** This skill scores your content ideas using multiple AI models, then aggregates for consensus. More reliable than single-model predictions.

---

## WHAT IT DOES

```
                Content Idea
                     │
    ┌────────────────┼────────────────┐
    │                │                │
    ▼                ▼                ▼
[Claude]        [GPT-4o]         [Gemini]
  Score            Score            Score
    │                │                │
    └────────────────┼────────────────┘
                     │
                     ▼
            [Aggregator (Claude)]
                     │
                     ▼
         Consensus Score + Verdict
```

---

## WHY MULTI-MODEL?

| Single Model | Ensemble |
|--------------|----------|
| May have biases | Biases cancel out |
| One perspective | Multiple perspectives |
| Black box score | Transparent reasoning |
| May miss nuances | Catches different angles |

---

## TRIGGERS

Use this skill when you say:
- "Score this content idea"
- "Is this topic worth pursuing?"
- "Rate my video concept"
- "Predict if this will go viral"
- "Ensemble score: [topic]"

---

## USAGE

### In Claude Code (Recommended)

```
"Ensemble score: Statins myth-busting for Indian audience"

"Score this video idea: Why your LDL target depends on your risk"

"Rate these ideas and rank them:
1. GLP-1 agonists explained
2. Heart attack warning signs
3. Is coconut oil heart-healthy?"
```

### CLI Mode

```bash
# Score single idea
python scripts/score_content.py --idea "Statins myth-busting for Indian audience"

# Score multiple ideas
python scripts/score_content.py --ideas "GLP-1 explained" "Statin myths" "CAC scoring"

# Use specific models
python scripts/score_content.py --idea "Topic" --models claude,gpt4o,gemini
```

---

## SCORING DIMENSIONS

Each model scores on these dimensions (1-10):

| Dimension | What It Measures |
|-----------|------------------|
| **Relevance** | How relevant to target audience (Indian patients/doctors) |
| **Novelty** | How fresh is the angle? Been covered before? |
| **Expertise Match** | Does it match your expertise as interventional cardiologist? |
| **Engagement Potential** | Will it capture and hold attention? |
| **Share-ability** | Will people share this? Controversy potential? |
| **Evergreen Factor** | Will this be relevant in 6 months? |

**Total Score: 0-60**

---

## OUTPUT FORMAT

```markdown
# ENSEMBLE CONTENT SCORE

**Idea:** Statins myth-busting for Indian audience - why most "side effects" aren't real

**Date:** 2025-01-01

---

## INDIVIDUAL MODEL SCORES

### Claude (Anthropic)
| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| Relevance | 9/10 | High - statins widely prescribed in India, misinformation common |
| Novelty | 7/10 | Topic covered before, but Indian-specific angle is fresher |
| Expertise | 9/10 | Perfect for interventional cardiologist |
| Engagement | 8/10 | Controversial enough to spark discussion |
| Shareability | 8/10 | Will trigger debates |
| Evergreen | 9/10 | Statin myths persist |
| **Total** | **50/60** | |

### GPT-4o (OpenAI)
| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| Relevance | 9/10 | Very relevant for Indian audience |
| Novelty | 6/10 | Many statin videos exist |
| Expertise | 10/10 | Perfect fit |
| Engagement | 9/10 | Myth-busting format works |
| Shareability | 8/10 | Good controversy factor |
| Evergreen | 8/10 | Will stay relevant |
| **Total** | **50/60** | |

### Gemini (Google)
| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| Relevance | 8/10 | Good for health-conscious Indians |
| Novelty | 7/10 | Indian angle adds freshness |
| Expertise | 9/10 | Great fit |
| Engagement | 7/10 | Educational more than viral |
| Shareability | 7/10 | Moderate share potential |
| Evergreen | 9/10 | Long-lasting relevance |
| **Total** | **47/60** | |

---

## CONSENSUS SCORE

| Model | Total Score |
|-------|-------------|
| Claude | 50/60 |
| GPT-4o | 50/60 |
| Gemini | 47/60 |
| **Average** | **49/60 (81.7%)** |
| **Std Dev** | 1.7 (High Consensus) |

---

## VERDICT

🟢 **STRONG PURSUE** (Score: 49/60, Consensus: High)

All models agree this is a strong content idea. The combination of:
- High relevance to your audience
- Perfect expertise match
- Good controversy factor
- Evergreen potential

Makes this a priority topic for your content calendar.

---

## RECOMMENDATIONS

1. **Angle Enhancement**: Focus on the "nocebo effect" - most statin "side effects" are psychosomatic
2. **Hook Suggestion**: "90% of statin side effects aren't real - here's the data"
3. **Format**: 12-15 minute deep dive with studies
4. **Hinglish Tip**: Use "side effect ka drama" for relatability

---

## DISSENT ANALYSIS

- **Gemini** scored lower on engagement (7 vs 8-9)
- Suggests: May need stronger hook to maximize viral potential
- Consider: Adding patient testimonial or counter-narrative
```

---

## SCORING TIERS

| Score Range | Verdict | Action |
|-------------|---------|--------|
| 50-60 | 🟢 STRONG PURSUE | High priority, create immediately |
| 40-49 | 🟡 WORTH PURSUING | Good idea, add to calendar |
| 30-39 | 🟠 NEEDS REFINEMENT | Has potential, needs angle work |
| 20-29 | 🔴 RECONSIDER | Weak idea, low priority |
| 0-19 | ⛔ SKIP | Not worth the effort |

---

## CONSENSUS INTERPRETATION

| Std Deviation | Interpretation |
|---------------|----------------|
| < 3 | High consensus - models agree |
| 3-5 | Moderate consensus - some disagreement |
| > 5 | Low consensus - divisive idea (may be worth exploring!) |

---

## INTEGRATION

### Enhances:
- `viral-content-predictor` - More reliable predictions
- `youtube-script-master` - Validate topics before scripting
- `content-repurposer` - Know which content to repurpose

### Workflow:
```
Idea Generation → Ensemble Score → [High Score?] → Create Content
                         ↓
                   [Low Score?] → Refine or Skip
```

---

## MODELS USED

| Model | Provider | Cost | Notes |
|-------|----------|------|-------|
| Claude Sonnet | Anthropic | Subscription | Your primary |
| GPT-4o | OpenAI | API | Strong analysis |
| Gemini Pro | Google | FREE | Good for fact-checking |
| Grok | xAI | API | Twitter trend awareness |

**Minimum required:** 2 models (Claude + one other)
**Recommended:** 3+ models for robust consensus

---

## DEPENDENCIES

```python
anthropic>=0.18.0
openai>=1.0.0           # For GPT-4o
google-generativeai>=0.3.0  # For Gemini
python-dotenv>=1.0.0
rich>=13.0.0
```

---

## API KEYS NEEDED

| Key | Purpose | Status |
|-----|---------|--------|
| ANTHROPIC_API_KEY | Claude | Already have |
| OPENAI_API_KEY | GPT-4o | Already have |
| GOOGLE_API_KEY | Gemini | Already have |
| XAI_API_KEY | Grok (optional) | Already have |

---

## BATCH SCORING

For scoring multiple ideas at once:

```bash
python scripts/score_content.py --batch \
    --ideas "GLP-1 for heart failure" \
            "Statin myth-busting" \
            "CAC scoring guide" \
            "Why LDL matters" \
            "Exercise for heart health"
```

Output:
```
| Rank | Idea | Score | Verdict |
|------|------|-------|---------|
| 1 | Statin myth-busting | 49/60 | 🟢 STRONG PURSUE |
| 2 | GLP-1 for heart failure | 45/60 | 🟡 WORTH PURSUING |
| 3 | CAC scoring guide | 42/60 | 🟡 WORTH PURSUING |
| 4 | Why LDL matters | 38/60 | 🟠 NEEDS REFINEMENT |
| 5 | Exercise for heart health | 35/60 | 🟠 NEEDS REFINEMENT |
```

---

## NOTES

- **Speed**: ~30 seconds for single idea (parallel API calls)
- **Cost**: Minimal - short prompts to each model
- **Reliability**: Consensus typically more accurate than single model
- **When to ignore**: If YOU have strong conviction, trust your expertise

---

*This skill helps you invest your time in content that's more likely to succeed.*
