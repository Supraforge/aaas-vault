# Trial Importance Scoring System

Hybrid rules + LLM approach to identify landmark cardiology trials worthy of editorial coverage.

## Two-Layer Approach

### Layer 1: Rules-Based Scoring (Transparent, Token-Efficient)

For each trial abstract, use an LLM call to extract structured metadata:

**Prompt Template:**
```
You are a cardiology trial methodologist.
You receive the title and abstract of a new cardiology article.
Output a JSON object with these fields only:

"design": one of ["large_RCT", "small_RCT", "observational", "registry", "meta_analysis", "case_series", "basic_science", "review", "editorial", "other"]
"sample_size": an integer estimate if clearly stated in the abstract, else null
"endpoints": one of ["hard_clinical", "surrogate", "procedural", "diagnostic", "other"]
"topic_class": one of ["coronary_intervention", "structural_intervention", "EP", "heart_failure", "prevention", "imaging", "other"]
"novelty": one of ["incremental", "moderate", "high"] based on whether the study seems to test a new strategy or device vs standard of care
"journal": the journal name from the article metadata

Do not hallucinate numbers or facts not clearly present in the abstract.
```

**Scoring Algorithm:**

```python
def calculate_importance_score(metadata):
    score = 0
    
    # Design weight (5 points max)
    if metadata["design"] == "large_RCT":
        score += 5
    elif metadata["design"] == "small_RCT":
        score += 3
    elif metadata["design"] == "meta_analysis":
        score += 3
    elif metadata["design"] in ["observational", "registry"]:
        score += 1
    
    # Sample size weight (3 points max)
    if metadata["sample_size"]:
        if metadata["sample_size"] >= 3000:
            score += 3
        elif metadata["sample_size"] >= 1000:
            score += 2
        elif metadata["sample_size"] >= 300:
            score += 1
    
    # Endpoints weight (3 points max)
    if metadata["endpoints"] == "hard_clinical":
        score += 3
    elif metadata["endpoints"] == "surrogate":
        score += 1
    
    # Topic relevance (2 points max)
    high_value_topics = ["coronary_intervention", "structural_intervention", "heart_failure"]
    if metadata["topic_class"] in high_value_topics:
        score += 2
    
    # Novelty weight (3 points max)
    if metadata["novelty"] == "high":
        score += 3
    elif metadata["novelty"] == "moderate":
        score += 1
    
    # Venue bonus (2 points max)
    journal_lower = metadata.get("journal", "").lower()
    top_journals = ["jacc", "circulation", "european heart journal", "nejm", "jama", "lancet"]
    if any(j in journal_lower for j in top_journals):
        score += 2
    
    return score
```

**Maximum possible score: 18 points**

### Layer 2: Practice-Change Likelihood (Optional, for Top Candidates)

After initial scoring, for the top 5-10 trials, add a second LLM assessment:

**Prompt Template:**
```
You are a senior cardiologist reviewing a new clinical trial.
Based only on the title and abstract, estimate how likely this study is to meaningfully influence clinical guidelines or everyday practice, if the results are confirmed.

Answer strictly in JSON with:
"practice_change_likelihood": one of ["low", "moderate", "high"]
"reason": one sentence explanation
```

**Additional Points:**
- "high" → +3 points
- "moderate" → +1 point
- "low" → 0 points

**Final score = Layer 1 score + Layer 2 points**

## Score Interpretation

**15+ points**: Likely landmark trial, strong editorial candidate
**10-14 points**: Important contribution, good editorial candidate
**7-9 points**: Moderate interest, editorial if slow news cycle
**< 7 points**: Usually skip unless special circumstances

## Special Considerations

### User Subspecialty Adjustment

If user specializes in specific area, adjust topic weights:

- **Interventional cardiologist**: coronary_intervention +3, structural_intervention +3
- **Heart failure specialist**: heart_failure +3
- **Electrophysiologist**: EP +3
- **Imaging specialist**: imaging +2

### Contextual Factors (Not in Score)

Consider but don't score:
- First-in-class device or therapy
- Reverses prior dogma
- Addresses FDA "black box" warning
- Major guideline timing (e.g., ACC/AHA update pending)
- Media buzz or social media traction
- Controversy or debate in the field

### Multi-Trial Synthesis

Sometimes no single trial scores high, but 3-4 moderate trials on same topic collectively matter:
- Meta-analysis opportunity
- "State of the field" editorial
- Trend analysis across studies

## Implementation Workflow

1. **Search PubMed** for recent articles (30-90 days) from target journals
2. **Extract abstracts** for all results
3. **Run Layer 1 LLM call** for each abstract → get structured JSON
4. **Calculate base scores** using algorithm above
5. **Sort by score**, take top 10
6. **Run Layer 2 LLM call** on top 10 → practice-change assessment
7. **Add Layer 2 points**, re-sort
8. **Present top 3-5** to user with score breakdown

## Quality Checks

- Verify sample sizes match abstract (no hallucination)
- Confirm design classification (RCT vs observational)
- Check endpoint classification against actual primary outcome
- Validate novelty assessment against clinical knowledge

## Edge Cases

**Negative trials**: High-quality null results can be landmark too
- If large RCT with hard endpoints shows no difference, still score high
- Novelty should account for "practice-changing negative result"

**Subset analyses**: Post-hoc or subgroup papers usually score lower
- Unless they fundamentally change interpretation of parent trial

**Device/procedural studies**: May have surrogate endpoints but high clinical relevance
- Consider pragmatic adjustment for interventional cardiology context

**Registry studies**: Can be landmark if massive scale or novel insights
- E.g., 100,000+ patients with real-world outcomes
