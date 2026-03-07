# Short-Form Accuracy Pass

## Overview

A quick sanity check for tweets, threads, and carousel content to ensure data is not misinterpreted. This is NOT a full review - just accuracy verification.

---

## What This Checks

### Data Interpretation Accuracy

**Trial Results:**
- [ ] Is the primary endpoint correctly stated?
- [ ] Is the effect size accurate (HR, RR, ARR)?
- [ ] Is the confidence interval correct if mentioned?
- [ ] Is the study population correctly described?
- [ ] Is the conclusion not overstated beyond what the trial showed?

**Statistics:**
- [ ] Are numbers accurate (not rounded incorrectly)?
- [ ] Is NNT/NNH correctly calculated if stated?
- [ ] Are percentages accurately represented?
- [ ] Is the direction of effect correct (increase vs decrease)?

**Study Findings:**
- [ ] Is the study design correctly described (RCT vs observational)?
- [ ] Are findings not misattributed to the wrong study?
- [ ] Is the follow-up duration correct if mentioned?
- [ ] Are limitations not hidden if making strong claims?

**Guideline References:**
- [ ] Is the guideline year/version correct?
- [ ] Is the recommendation class/level correct if stated?
- [ ] Is the guideline correctly attributed (ACC vs ESC vs ADA)?

---

## What This Does NOT Check

- Writing quality (user can iterate)
- Voice consistency (quick pass only)
- Engagement optimization
- Full scientific rigor
- Complete citation verification

---

## Quick Pass Protocol

### For Each Short-Form Piece

1. **Identify Data Claims**
   - Find any statistics, trial results, study findings
   - Flag specific numbers, percentages, effect sizes

2. **Verify Against Source**
   - Check against research brief
   - Confirm accuracy of key claims

3. **Mark Result**
   - ✓ ACCURATE: Data correctly represented
   - ⚠ CHECK: Potential issue, needs verification
   - ✗ ERROR: Misinterpretation found, must fix

### Output Format

```markdown
## Accuracy Check: [Tweet/Thread/Carousel]

### Claims Verified:
1. "Statins reduce LDL by 50%" → ✓ ACCURATE (source: research brief)
2. "JUPITER trial showed 44% reduction" → ✓ ACCURATE
3. "NNT of 25" → ⚠ CHECK (research brief says NNT 95)

### Status: NEEDS CORRECTION

### Corrections:
- Tweet 3: Change "NNT of 25" to "NNT of 95 over 2 years"
```

---

## Examples

### ACCURATE (No Changes Needed)
```
Tweet: "SGLT2 inhibitors reduce heart failure hospitalizations by 25-35% in patients with HFrEF. That's an NNT of about 21 over 2 years. (DAPA-HF, EMPEROR-Reduced)"

Check:
- HF hospitalization reduction: ✓ ACCURATE (range correct)
- NNT: ✓ ACCURATE (matches trial data)
- Trial names: ✓ ACCURATE

Status: ✓ PASS
```

### NEEDS CORRECTION
```
Tweet: "Statins cause muscle pain in 50% of patients. That's why so many people stop taking them."

Check:
- 50% muscle pain: ✗ ERROR (actual rate 5-10%, nocebo effect significant)
- Causation claim: ⚠ CHECK (many symptoms are nocebo)

Status: NEEDS CORRECTION

Fix: "Muscle symptoms reported in 5-10% of statin users, though studies suggest nocebo effect accounts for many cases."
```

---

## Speed Guidelines

| Content Type | Time Limit | Focus |
|--------------|------------|-------|
| Single Tweet | 30 seconds | Key data point only |
| Thread (5-10 tweets) | 2 minutes | Main statistics |
| Carousel | 1 minute | Title claims, key numbers |

This is a QUICK pass. Don't overthink. Check the numbers, move on.

---

## Integration with Content OS

When Content OS generates short-form content:

1. **Generate** tweets/thread/carousel content
2. **Run** quick accuracy pass
3. **Flag** any issues found
4. **Correct** errors before marking as done
5. **Output** with accuracy status

```
short-form/
├── tweets.md           ✓ Accuracy checked
├── thread.md           ✓ Accuracy checked
└── accuracy-log.md     # Record of checks performed
```
