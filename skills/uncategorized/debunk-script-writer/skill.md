# DEPRECATED - Use youtube-script-master instead

> **This skill has been merged into `youtube-script-master`.**
> Location: `/.claude/skills/youtube-script-master/SKILL.md`
> Please use the unified skill for all YouTube script writing, including debunk content.

---

# Skill: Debunk Script Writer

## Metadata
- **Name**: debunk-script-writer
- **Version**: 1.1
- **Status**: DEPRECATED - merged into youtube-script-master
- **Purpose**: Write evidence-based correction videos that address patient misinformation without humiliation
- **Token Budget**: High (use with Opus for nuanced tone)
- **Inherits From**: `youtube-script-hinglish` (for Hinglish rules, voice, transitions)

---

## Relationship to youtube-script-hinglish

This skill **extends** the base youtube-script-hinglish skill. It inherits:
- Hinglish word choice matrix (70% Hindi, 30% English technical)
- Voice DNA and transitions
- Basic script quality standards
- Engagement beat patterns

It **adds** specialized capabilities for:
- Steelman-then-correct methodology
- Tone calibration for sensitive corrections
- Narrative-specific hooks and structures
- Evidence citation protocol for debunking

**When to use which:**
| Scenario | Use |
|----------|-----|
| Explaining a concept (What is ApoB?) | youtube-script-hinglish |
| Lifestyle advice (Walking vs Gym) | youtube-script-hinglish |
| Patient stories/cases | youtube-script-hinglish |
| Correcting a popular myth | **debunk-script-writer** |
| Responding to Berg/Ekberg/SAAOL | **debunk-script-writer** |
| "YouTube says X, is it true?" | **debunk-script-writer** |

---

## The Core Philosophy

**"Be the cardiologist who speaks their language without surrendering rigor."**

Patients arrive having watched 50+ hours of Dr. Eric Berg, SAAOL, and fasting evangelists. They have absorbed:
- LDL skepticism
- Statin fear
- Insulin-as-sole-cause framing
- Fasting-cures-everything belief
- Supplements-over-medications preference

Your job is NOT to mock, dismiss, or humiliate. Your job is to:
1. Acknowledge what they got RIGHT
2. Gently show where the wheels come off
3. Provide the nuanced truth with evidence
4. Give them a new, more accurate mental model

---

## When to Use This Skill

Invoke this skill when:
- Creating "response to" videos addressing popular misinformation
- Writing myth-busting content about cardiology topics
- Correcting beliefs seeded by high-influence channels
- Addressing common patient concerns about statins, LDL, fasting, etc.

---

## Required Context

Before using:
1. Know which narrative you're correcting (from narrative_monitor.py output)
2. Know which channel(s) promoted this narrative
3. Have specific claims to address (not vague generalizations)
4. Have evidence ready (studies, guidelines, clinical experience)

---

## Debunk Formats

### Format A: Direct Response (Use sparingly, for high-stakes misinformation)

**When to use:** Only for dangerous misinformation from high-influence channels.

**Structure:**
```
[HOOK] - The claim that needs correcting
[STEELMAN] - What they got RIGHT, give credit
[PIVOT] - "Lekin yahan problem hai..."
[EVIDENCE] - What studies actually show
[NUANCE] - The complete picture
[TAKEAWAY] - What to actually do
```

**Example title:** "Cardiologist Reacts: What Dr. Eric Berg Gets Wrong About LDL"

**Tone rules:**
- Never use "destroy," "debunk," "expose" language
- Always acknowledge partial truths
- Be respectful even in disagreement
- Your authority comes from evidence, not ridicule

---

### Format B: Gentle Correction (Default format)

**When to use:** Most misinformation that doesn't require naming sources.

**Structure:**
```
[HOOK] - "Aapne yeh suna hoga..." (you've probably heard this)
[VALIDATE] - Why this belief makes sense / is appealing
[COMPLICATE] - "Lekin story itni simple nahi hai..."
[EVIDENCE] - Walk through what we actually know
[CONTEXT] - Indian-specific considerations
[ACTIONABLE] - What to do with this information
```

**Example title:** "Kya LDL Really Matters? The Full Truth"

**Tone rules:**
- Never name specific channels unless absolutely necessary
- Frame as "common misconceptions" not "lies"
- Validate the underlying concern (fear of medications, desire for natural solutions)
- Show you understand why they believed this

---

### Format C: Evidence Synthesis (For complex, nuanced topics)

**When to use:** When the truth is genuinely complex and both "sides" have partial truths.

**Structure:**
```
[HOOK] - The debate/controversy
[SIDES] - What each side claims
[EVIDENCE WALK] - Study by study breakdown
[SYNTHESIS] - What the totality of evidence suggests
[CLINICAL REALITY] - What I see in practice
[FRAMEWORK] - How to think about this
```

**Example title:** "The LDL Controversy: 50 Studies Reviewed"

---

### Format D: Indian Context Correction

**When to use:** When Western advice doesn't translate to Indian population.

**Structure:**
```
[HOOK] - Popular advice that doesn't work for Indians
[GLOBAL vs LOCAL] - Why generic advice fails
[INDIAN DATA] - Studies on Indian populations
[RISK FACTORS] - India-specific considerations
[ADAPTED ADVICE] - What Indians should actually do
```

**Example title:** "Why American Heart Advice Doesn't Work for Indians"

---

## Steelman-Then-Correct Protocol

This is the most important technique. Before criticizing ANY belief, you MUST:

### Step 1: Find the Kernel of Truth
Every popular health belief contains something true or appealing. Find it.

| Belief | Kernel of Truth |
|--------|-----------------|
| "LDL doesn't matter" | LDL alone isn't the full picture; particle count, inflammation matter |
| "Statins are poison" | Statins do have side effects; not everyone needs them |
| "Fasting cures everything" | Fasting has metabolic benefits; caloric restriction helps |
| "Insulin is the real problem" | Insulin resistance IS important; metabolic health matters |
| "Seed oils cause heart disease" | Diet quality matters; ultra-processed foods are problematic |

### Step 2: Acknowledge It Explicitly

**Wrong approach:**
> "Yeh log galat hain. LDL clearly causes heart disease."

**Right approach:**
> "Yeh belief kahan se aayi? Actually, ek valid point hai. LDL alone se poori picture nahi milti. ApoB, particle count, inflammation - sab matter karta hai. Lekin iska matlab yeh nahi ki LDL matter hi nahi karta..."

### Step 3: Show the Logical Error

Common logical errors to expose:
- **Oversimplification**: "It's not that simple..."
- **Cherry-picking studies**: "Jab hum ALL studies dekhte hain..."
- **Correlation vs causation**: "Yeh saath-saath hota hai, iska matlab yeh nahi ki..."
- **Anecdote vs evidence**: "Kuch logon ka experience aisa hai, but population level pe..."
- **False dichotomy**: "Yeh either-or nahi hai..."

---

## Evidence Citation Protocol

### For Studies
> "2023 mein European Heart Journal mein ek meta-analysis aayi - 200 studies, 20 lakh logon pe. Finding? [specific finding]..."

### For Guidelines
> "ESC guidelines - Europe ke top cardiologists - recommend karte hain ki [specific recommendation]. Kyun? Because evidence shows..."

### For Clinical Experience
> "Mere practice mein pichhle 15 saal mein, maine [X] cases dekhe hain jahan [observation]..."

### For Opposing Evidence
> "Ab kuch log kehte hain ki [study name] ne opposite dikhaaya. Sahi baat hai. Lekin us study mein [limitation]..."

---

## Hinglish Hooks for Debunk Content

### For LDL Skepticism
- "YouTube pe dekha ki LDL kharab nahi hai? Ek cardiologist ki sachai suniye..."
- "High LDL but 'I feel fine' - yeh kyun khatarnak soch hai..."
- "LDL myth ya reality? 50 studies dekhne ke baad mera jawab..."

### For Statin Fear
- "Statin se darr lagta hai? Main aapka darr samajhta hoon. Ab evidence dekhte hain..."
- "Statin ke side effects - kitna real, kitna exaggerated..."
- "Maine statin leni chahiye ya nahi? Honest answer..."

### For Insulin Primacy
- "Sirf insulin fix karo, sab theek? Kaash itna simple hota..."
- "Insulin resistance important hai - but story yahan khatam nahi hoti..."
- "Cholesterol vs Insulin - yeh ladai fake hai. Real picture alag hai..."

### For Fasting Absolutism
- "Fasting se heart disease reverse? Kuch sach hai, kuch myth..."
- "Autophagy ka magic ya marketing? Evidence check karte hain..."
- "Fasting achha hai - but kiske liye? Yeh important hai..."

---

## Tone Calibration

### Never Say:
- "Yeh log galat hain" (These people are wrong)
- "Bakwaas" (Nonsense)
- "Unhe medical degree nahi hai" (They don't have a medical degree)
- "Aap fool ban rahe ho" (You're being fooled)
- "Yeh dangerous misinformation hai" (This is dangerous misinformation)

### Instead Say:
- "Is approach mein ek problem hai" (There's a problem with this approach)
- "Story itni simple nahi hai" (The story isn't that simple)
- "Partial truth hai, but..." (There's partial truth, but...)
- "Main samajhta hoon kyun yeh appealing hai" (I understand why this is appealing)
- "Evidence kuch aur kehti hai" (Evidence says something different)

---

## Script Template: Gentle Correction

```
[HOOK - 0:00]
{Surprising statement that challenges common belief}
"Aapne suna hoga ki {common belief}. Lakhs of people believe this. Aur honestly? Unki baat mein thoda point bhi hai. Lekin poori story alag hai..."

[VALIDATE - 0:30]
{Acknowledge why this belief exists}
"Yeh belief kahan se aayi? {Name source or trend}. Aur dekho, {what they got right}. Yeh sach hai."

[PIVOT - 1:30]
{Introduce the complication}
"Lekin yahan story mein twist hai. {The piece they're missing}. Aur yeh miss karna aapke liye expensive ho sakta hai..."

[EVIDENCE - 2:30]
{Walk through evidence}
"Chalo evidence dekhte hain. {Study 1}. Phir {Study 2}. Aur {meta-analysis or guideline}. Pattern dikh raha hai?"

[NUANCE - 5:30]
{The complete picture}
"Toh sachai kya hai? {Nuanced truth}. Na sirf {extreme A}, na sirf {extreme B}. Reality is..."

[INDIAN CONTEXT - 7:00]
{India-specific considerations}
"Aur specifically Indians ke liye? {India-specific data or risk factors}. Generic advice se kaam nahi chalega..."

[ACTIONABLE - 8:30]
{What to actually do}
"Toh aap kya karein? Simple steps:
1. {Action 1}
2. {Action 2}
3. {Action 3}
Apne doctor se is basis pe baat karein..."

[CLOSE - 9:30]
{Empowering close}
"Ab aapke paas complete picture hai. Na darr, na complacency. Sirf evidence. Apna decision informed lein..."
```

---

## Response Video Template

For direct "Cardiologist Reacts" format:

```
[HOOK - 0:00]
"[Channel name] ki yeh video [X million] logon ne dekhi. Aur [specific claim]. Main as a cardiologist, 15 saal ka experience, aapko batata hoon - kya sahi hai, kya galat..."

[CLIP 1 + REACTION]
"{Show claim}"
"Yahan [name] sahi keh rahe hain ki {partial truth}. Credit where due..."

[CLIP 2 + CORRECTION]
"{Show problematic claim}"
"Ab yahan problem hai. {Why this is incomplete/wrong}. Studies show {evidence}..."

[CLIP 3 + NUANCE]
"{Show oversimplification}"
"Yeh oversimplification hai. Real picture? {Nuanced truth}..."

[SUMMARY]
"Toh kya main keh raha hoon ki [channel] galat hai? Nahi. Main keh raha hoon ki {nuanced position}. Aapka health too important hai for incomplete information..."
```

---

## Quality Checklist

Before finalizing debunk script:

### Steelman Check
- [ ] Did I acknowledge what they got RIGHT?
- [ ] Did I explain why this belief is appealing?
- [ ] Did I avoid strawmanning their position?

### Evidence Check
- [ ] Did I cite specific studies/guidelines?
- [ ] Did I address counter-evidence fairly?
- [ ] Did I show my reasoning, not just conclusions?

### Tone Check
- [ ] Would I be comfortable saying this to a patient's face?
- [ ] Is this educational, not confrontational?
- [ ] Does this build trust or defensiveness?

### Actionable Check
- [ ] Does viewer know what to DO with this information?
- [ ] Is advice realistic for Indian context?
- [ ] Does it empower, not just correct?

---

## Narratives Quick Reference

| Narrative | Steelman | Key Correction |
|-----------|----------|----------------|
| LDL skepticism | LDL alone isn't everything; metabolic health matters | Mendelian randomization proves LDL causality |
| Statin fear | Statins have real side effects; not everyone needs them | For high-risk patients, benefits far outweigh risks |
| Insulin primacy | Insulin resistance is genuinely important | It's one factor among many; LDL still independent |
| Fasting absolutism | Fasting has metabolic benefits | Not magical; doesn't reverse established plaque |
| Seed oil villain | Diet quality matters; ultra-processed bad | Seed oils not uniquely harmful; overall pattern matters |

---

*This skill ensures debunk content corrects with authority but without arrogance.*
