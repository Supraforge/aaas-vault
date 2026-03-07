---
name: infographic-copy
description: >-
  Transform research and knowledge base material into information-dense
  infographic copy—clear, scannable, authoritative, reference-worthy.
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---
# Infographic Copy Skill

Transform research and knowledge base material into information-dense infographic copy—clear, scannable, authoritative, reference-worthy.

---

## When to Use This Skill

Use when you have:
- Clinical algorithms or decision trees to visualize
- Comparison data (drug vs drug, treatment options)
- Patient preparation guides or checklists
- Trial results that need single-image presentation
- Myth vs truth content
- Process workflows (how to start a medication, what happens during a procedure)

---

## How Infographics Differ from Carousels

| Aspect | Carousel | Infographic |
|--------|----------|-------------|
| Consumption | Swipe through, narrative flow | Single image, scan and absorb |
| Density | One idea per slide | Multiple ideas, organized visually |
| Save behavior | Save whole carousel | Screenshot, reference later |
| Purpose | Engagement, education journey | Quick reference, decision support |
| Copy length | ≤15 words per slide | Tighter—≤8 words per bullet |

**Key insight:** Infographics are saved, screenshotted, and returned to. Write for the second and third viewing, not just the first.

---

## Voice Calibration for Infographics

### More Compressed, Same Authority

Infographic copy is even tighter than carousel copy. Every word must earn its place.

**Target:**
```
"SGLT2i: 26% reduction in HF hospitalization. Start if EF ≤40%."
```

**Not:**
```
"SGLT2 inhibitors have been shown to reduce heart failure hospitalization 
by 26% and should be considered in patients with EF ≤40%."
```

### Noun-heavy, Verb-light

Infographics favor noun phrases over full sentences:

| Full Sentence | Infographic Style |
|---------------|-------------------|
| "You should avoid caffeine before the test" | "Avoid caffeine 24h before" |
| "The medication reduces cholesterol levels" | "LDL reduction: 30-50%" |
| "Patients often experience muscle pain" | "Muscle pain: 5-10% of patients" |

### Authority Through Precision

In infographics, authority comes from precision, not from "I" statements:

- Specific numbers > general claims
- Trial names > "studies show"
- Dosing details > "as prescribed"

---

## Knowledge Base → Infographic Copy Transformation

### Step 1: Identify the Infographic Type

| Your Content | Best Template |
|--------------|---------------|
| Single striking statistic | `infographic-hero` |
| Multiple related facts/sections | `infographic-dense` |
| Two options to compare | `infographic-comparison` |
| Misconception to correct | `infographic-myth` |
| Sequential steps | `infographic-process` |
| Patient prep or to-do list | `infographic-checklist` |

### Step 2: Extract and Compress

**For each piece of information, ask:**
1. What is the core fact? (3-5 words)
2. What context is essential? (3-5 words)
3. What can be cut without losing meaning?

**Compression Examples:**

| Original | Compressed |
|----------|------------|
| "Patients should discontinue aspirin 7 days before the procedure if instructed by their physician" | "Stop aspirin 7 days before (if advised)" |
| "Blood pressure should be measured in a seated position after 5 minutes of rest" | "BP: seated, after 5 min rest" |
| "The PARADIGM-HF trial demonstrated a 20% relative risk reduction in cardiovascular mortality" | "CV mortality: ↓20% (PARADIGM-HF)" |

### Step 3: Organize for Scanning

Readers scan infographics in predictable patterns:
- Top to bottom (hierarchy)
- Left to right (comparisons)
- Center outward (hero stats)

Place the most important information where eyes land first.

---

## Copy Patterns by Infographic Type

### HERO (Single Stat)

**Purpose:** One memorable number that tells the story.

**Copy Elements:**
```
STAT:     [Number + unit]     →  "26%"
LABEL:    [What it measures]  →  "Mortality Reduction"
CONTEXT:  [Technical detail]  →  "HR 0.74 (95% CI 0.65-0.85)"
SOURCE:   [Trial/study]       →  "PARADIGM-HF Trial"
TAG:      [Category label]    →  "LANDMARK TRIAL"
```

**Writing the label:**
- Outcome-focused: "Mortality Reduction" not "Primary Endpoint Result"
- Patient-relevant: "Fewer Hospitalizations" not "Reduced Hospitalization Rate"
- Active when possible: "Risk Reduction" not "Reduced Risk"

**Context line options:**
- Hazard ratio with CI: `HR 0.74 (95% CI 0.65-0.85)`
- NNT: `NNT: 21 over 18 months`
- Absolute risk: `ARR: 4.7%`
- vs comparator: `vs placebo`

### DENSE (Multi-Section)

**Purpose:** Multiple related points, organized by theme.

**Copy Elements:**
```
TAG:      [Category]          →  "PATIENT GUIDE"
TITLE:    [Main topic]        →  "SGLT2 Inhibitor Initiation"
SUBTITLE: [Scope/audience]    →  "For HFrEF patients"

SECTION 1:
  TITLE:  [Section name]      →  "Who qualifies"
  BULLETS: [2-4 short items]  →  • EF ≤40%
                                 • Stable on current therapy
                                 • eGFR ≥20

SECTION 2:
  TITLE:  [Section name]      →  "Red flags to monitor"
  BULLETS: [2-4 short items]  →  • Volume depletion
                                 • Acute kidney injury
                                 • Ketoacidosis (rare)

CALLOUT:  [Key takeaway]      →  "Start low, monitor at 2 weeks"
```

**Bullet writing rules:**
- Start with noun or verb
- ≤8 words per bullet
- Parallel structure (all start same way)
- No periods at end

**Section title patterns:**
- Question format: "Who qualifies?"
- Category format: "Monitoring Parameters"
- Action format: "Before Starting"

### COMPARISON

**Purpose:** Side-by-side evaluation of two options.

**Copy Elements:**
```
TAG:      [Category]          →  "TREATMENT CHOICE"
TITLE:    [What's being compared] →  "ACE-I vs ARB in Heart Failure"

LEFT SIDE:
  LABEL:      [Option name]   →  "ACE Inhibitors"
  STAT:       [Key number]    →  "31%"
  STAT LABEL: [What stat means] → "Mortality Reduction"
  BULLETS:    [Differentiators] → • First-line therapy
                                  • More cough (10-15%)
                                  • Proven in CONSENSUS, SOLVD

RIGHT SIDE:
  LABEL:      [Option name]   →  "ARBs"
  STAT:       [Key number]    →  "Similar"
  STAT LABEL: [What stat means] → "Mortality Reduction"
  BULLETS:    [Differentiators] → • ACE-I intolerant patients
                                  • Better tolerated
                                  • Val-HeFT, CHARM trials

SOURCE:   [Evidence base]     →  "ESC Guidelines 2023"
```

**Comparison writing rules:**
- Keep sides parallel (same number of bullets)
- Lead with differentiators, not similarities
- Be fair—don't strawman one side
- Include when to choose each

### MYTH

**Purpose:** Correct a specific misconception with evidence.

**Copy Elements:**
```
TAG:      [Category]          →  "MYTH BUSTED"
TITLE:    [The misconception] →  "Statins cause permanent muscle damage"

MYTH:
  TEXT:   [State belief as held] → "Taking statins will give you 
                                    severe muscle problems"

TRUTH:
  TEXT:   [Direct correction]    → "Muscle symptoms affect 5-10%. 
                                    Reversible. Most continue therapy."

EVIDENCE: [Supporting data]      → "Meta-analysis of 19 RCTs, n=71,000"
SOURCE:   [Citation]             → "Lancet 2022"
```

**Myth statement rules:**
- Write the myth as believers state it
- Don't strawman or exaggerate the myth
- Use quotation marks to signal "this is what people think"

**Truth statement rules:**
- Lead with the correction
- Include the key number
- End with reassurance or action

### PROCESS (Steps/Flow)

**Purpose:** Sequential actions or algorithm.

**Copy Elements:**
```
TAG:      [Category]          →  "CLINICAL ALGORITHM"
TITLE:    [Process name]      →  "Starting Beta-Blockers in HF"
SUBTITLE: [Context]           →  "Initiation and uptitration"

STEP 1:
  TITLE:       [Action verb]  →  "Confirm stability"
  DESCRIPTION: [Details]      →  "No IV diuretics in 48h, no recent 
                                  decompensation"

STEP 2:
  TITLE:       [Action verb]  →  "Start low"
  DESCRIPTION: [Details]      →  "Carvedilol 3.125mg BID or 
                                  Metoprolol succinate 12.5-25mg daily"

STEP 3:
  TITLE:       [Action verb]  →  "Uptitrate slowly"
  DESCRIPTION: [Details]      →  "Double dose every 2 weeks as tolerated"

NOTE:     [Important caveat]  →  "Hold uptitration if: HR <55, SBP <90, 
                                  worsening symptoms"
```

**Step title rules:**
- Start with verb
- 2-4 words max
- Action-oriented: "Check", "Start", "Monitor", "Adjust"

**Description rules:**
- Include the specific (dose, timing, threshold)
- One sentence or phrase fragments
- No fluff words

### CHECKLIST

**Purpose:** Actionable to-do list, often for patients.

**Copy Elements:**
```
TAG:      [Category]          →  "PATIENT CHECKLIST"
TITLE:    [What it's for]     →  "Before Your Angiogram"
SUBTITLE: [Additional context] → "Day-of preparation"

CATEGORY 1:
  TITLE:  [Timeframe/theme]   →  "24 Hours Before"
  ITEMS:
    - "Stop blood thinners (if instructed)"
    - "No food after midnight"
    - "Continue BP and heart medications"

CATEGORY 2:
  TITLE:  [Timeframe/theme]   →  "Morning Of"
  ITEMS:
    - "Bring medication list"
    - "Arrange transport home"
    - "Wear comfortable clothing"

CALLOUT:  [Critical warning]  →  "⚠ Tell staff immediately if: 
                                  chest pain, allergies, or recent illness"
```

**Checklist item rules:**
- Start with verb
- Specific and actionable
- Order by importance or timeline
- Include exceptions in parentheses

---

## Citation Placement in Infographics

### Bottom Source Line (Default)

For most infographics, a single source line at the bottom:
```
Source: ACC/AHA Guidelines 2023
```

### Inline After Stats

When multiple sources, cite inline:
```
Mortality: ↓26% (DAPA-HF)
Hospitalization: ↓25% (EMPEROR-Reduced)
```

### Abbreviated Formats

Use standard abbreviations to save space:
- `NEJM 2019` not `New England Journal of Medicine, 2019`
- `ACC/AHA 2023` not `American College of Cardiology/American Heart Association Guidelines 2023`
- `n=8,000` not `in a study of 8,000 patients`

---

## Archetype Adaptation for Infographics

### Same Information, Different Framing

**Example: Beta-Blocker Initiation Process**

**For Clinicians/Biohackers (technical):**
```
Title: Beta-Blocker Initiation in HFrEF
Steps: 
1. Confirm euvolemia (no IV diuretics 48h)
2. Start: Carvedilol 3.125mg BID or Metoprolol XL 12.5mg
3. Uptitrate q2 weeks to target dose
Note: Target HR 60-70, hold if SBP <90
```

**For Heart Patients (practical):**
```
Title: Starting Your Beta-Blocker
Steps:
1. Your doctor confirms you're stable
2. You start at a very low dose
3. Dose increases slowly over weeks
Note: Tell your doctor if you feel dizzy or too tired
```

**For Caregivers (watchpoints):**
```
Title: Beta-Blocker Monitoring Checklist
Categories:
Watch For:
  - Dizziness when standing
  - Unusual fatigue
  - Very slow pulse (<50)
What's Normal:
  - Some initial tiredness (improves)
  - Slightly lower energy at first
When to Call Doctor:
  - Shortness of breath worsens
  - Fainting or near-fainting
```

---

## Quality Checklist for Infographic Copy

- [ ] Title is scannable in 2 seconds
- [ ] Most important information is visually prominent
- [ ] Each bullet ≤8 words
- [ ] Parallel structure throughout
- [ ] Numbers are specific (not "significant" or "many")
- [ ] Source is clear and abbreviated
- [ ] No orphan information (everything belongs to a section)
- [ ] A patient could understand this without medical training
- [ ] A doctor would find this accurate and useful

---

## Common Infographic Copy Mistakes

| Mistake | Example | Fix |
|---------|---------|-----|
| Too wordy | "Patients should make sure to avoid eating..." | "No food after midnight" |
| Vague numbers | "Significant reduction" | "26% reduction" |
| Missing context | "Take with food" | "Take with food (reduces GI upset)" |
| Inconsistent format | Mix of sentences and fragments | Pick one style, stick to it |
| Buried key info | Important point in middle of list | Lead with most critical item |
| No hierarchy | All bullets same importance | Use callout for key point |
| Missing source | Stats without attribution | Add trial name or guideline |

---

## Positioning in Infographic Copy

Unlike carousels (where "I" statements work), infographics signal expertise through:

### Precision Markers
- Exact doses: "Carvedilol 3.125mg BID"
- Specific thresholds: "eGFR ≥20"
- Clinical ranges: "HR 0.74 (95% CI 0.65-0.85)"

### Guideline Awareness
- "Per ESC 2023"
- "ACC/AHA Class I"
- "Guideline-directed"

### Clinical Nuance
- "(if not contraindicated)"
- "in stable patients"
- "unless recent decompensation"

These signal "written by someone who actually prescribes this" without saying it.

---

## Example Transformation

### Input: Knowledge Base Excerpt

```
Angiography Patient Preparation:

Pre-procedure:
- NPO after midnight for morning procedures
- Hold metformin 48h before if using contrast
- Continue aspirin unless directed otherwise
- Stop warfarin 5 days before, bridge with heparin if high-risk
- Arrive 2h before scheduled time

Day of:
- Wear comfortable, loose clothing
- Bring list of current medications
- Arrange transportation home (no driving for 24h)
- Inform staff of allergies, especially contrast or iodine

Post-procedure:
- Bed rest 2-6h depending on access site
- Monitor puncture site for bleeding
- Resume normal diet unless instructed otherwise
- Drink plenty of fluids to clear contrast
```

### Output: Infographic Copy (Checklist Template)

```
TAG: PATIENT GUIDE

TITLE: Before Your Angiogram

SUBTITLE: Complete preparation checklist

CATEGORY 1: "48 Hours Before"
ITEMS:
  - "Stop metformin (if using)"
  - "Stop warfarin (if instructed)"
  - "Continue aspirin and BP meds"

CATEGORY 2: "Night Before"
ITEMS:
  - "No food after midnight"
  - "Water OK until 2h before"
  - "Confirm ride home arranged"

CATEGORY 3: "Morning Of"
ITEMS:
  - "Arrive 2 hours early"
  - "Bring medication list"
  - "Wear comfortable clothing"

CALLOUT: 
  ICON: warning
  TEXT: "Tell staff about: contrast allergies, kidney problems, 
         recent bleeding, or if you might be pregnant"

FOOTER: "Educational guide. Follow your doctor's specific instructions."
```

---

## Integration with Infographic Generator

This skill provides the copy. The infographic-generator skill handles visuals.

**Workflow:**
1. Research → Knowledge base
2. **This skill:** Knowledge base → Structured copy
3. Infographic generator: Structured copy → Visual output

**Output format for handoff:**
```json
{
  "template": "infographic-checklist",
  "data": {
    "tag": "PATIENT GUIDE",
    "title": "Before Your Angiogram",
    "subtitle": "Complete preparation checklist",
    "categories": [
      {
        "title": "48 Hours Before",
        "items": [
          {"text": "Stop metformin (if using)"},
          {"text": "Stop warfarin (if instructed)"},
          {"text": "Continue aspirin and BP meds"}
        ]
      }
    ],
    "callout": {
      "icon": "warning",
      "text": "Tell staff about: contrast allergies, kidney problems, recent bleeding"
    }
  }
}
```

---

*Part of Dr. Shailesh Singh's Integrated Content OS*
