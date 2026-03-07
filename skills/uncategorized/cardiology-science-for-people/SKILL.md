---
name: cardiology-science-for-people
description: >-
  Write rigorous, accurate cardiology science for general audiences—not doctors.
  Use when the user wants to: (1) Explain clinical trials or research in plain
  English, (2) Write science content an 8th grader can understand WITHOUT
  dumbing it down, (3) Create thought leadership for the intelligent public
  rather than medical peers, (4) Transform complex cardiology findings into
  stories and narratives, (5) Write pieces where readers DON'T need another LLM
  to understand the explanation. Maintains full scientific rigor with PubMed
  citations for verification while avoiding academic language, trial acronyms,
  and intimidating statistics.
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---

# Cardiology Science for People

Write rigorous cardiology science that real people actually want to read. Same accuracy as an academic editorial. Zero intimidation.

## Core Philosophy

**The problem you're solving**: Academic writing says correct things in ways that require a medical degree to understand. Dumbed-down content oversimplifies to the point of being wrong. 

**The solution**: Write scientifically accurate content in the language people actually use. An 8th grader should understand it. A cardiologist should find no errors.

**What "for people" means**:
- Stories, not statistics
- What it means for them, not what the trial showed
- Names of conditions, not trial acronyms
- Explanations that stand alone, not explanations requiring explanations

## The Three Golden Rules

### 1. Lead with the Human Story

**Never start with**: "The STEP-HFpEF trial randomized 529 patients..."

**Always start with**: "If you have heart failure and struggle to walk up stairs, there's finally a drug that might help you do more of what you love."

The trial is evidence. The story is why anyone should care.

### 2. Translate Statistics to Meaning

**Never write**: "The hazard ratio was 0.65 (95% CI 0.51-0.82), representing a 35% relative risk reduction."

**Instead write**: "For every 100 people who took the drug, about 8 fewer had heart attacks compared to those who didn't. That's a meaningful difference—roughly 1 in 12 people benefited."

Always convert to:
- "X out of 100 people..." (absolute terms)
- "About 1 in Y people benefited"
- Real-world comparisons: "roughly the same benefit as..."
- Time frames that matter: "over the next 5 years..."

### 3. Background the Evidence, Foreground the Understanding

**Academic style**: "The DAPA-HF trial (McMurray et al., NEJM 2019) demonstrated that dapagliflozin reduced the composite of worsening heart failure or cardiovascular death by 26% (HR 0.74, 95% CI 0.65-0.85)."

**People style**: "A diabetes drug called dapagliflozin turns out to help hearts too—even in people without diabetes. In a large study, people taking this drug were about a quarter less likely to end up in the hospital for heart failure or die from heart problems. Scientists aren't entirely sure why it works, but the evidence is strong enough that cardiologists now prescribe it regularly."

The citation goes in your references section. The reader gets the understanding.

## Writing Process

### Step 1: Research (Same Rigor as Editorial Skill)

Use PubMed MCP exactly as you would for academic writing:
- `PubMed:search_articles` for finding trials and evidence
- `PubMed:get_article_metadata` for details
- `PubMed:get_full_text_article` when available

**Target**: 5-8 solid references from major journals (NEJM, JAMA, Lancet, JACC, Circulation, EHJ).

**Purpose of citations**: YOUR verification that you got the science right, and the user's ability to check your work. NOT to impress readers.

### Step 2: Extract the Core Story

Before writing, answer:

1. **What's the one thing readers need to understand?**
   - Not what the trial showed. What it MEANS.

2. **Why should someone care?**
   - Not "this is important because..." 
   - What changes in their life, their risk, their choices?

3. **What's the story arc?**
   - What was the problem before?
   - What did we discover?
   - What's different now?

4. **What's the "so what" for a reader's life?**
   - Should they ask their doctor about something?
   - Should they change a behavior?
   - Should they feel relieved or concerned?

### Step 3: Write for Understanding

#### Structure (Flexible—Narrative Flow Over Sections)

Unlike the rigid 7-section editorial, structure should serve the story:

**Option A: Problem → Discovery → Meaning**
- Start with a relatable problem ("Many people with heart failure can barely walk to the mailbox")
- Introduce the discovery as a story ("Then scientists tried something unexpected...")
- Land on what it means for the reader ("For you, this means...")

**Option B: Surprising Fact → Explanation → Implications**
- Hook with something unexpected ("A diabetes drug is now one of the best heart failure treatments")
- Explain how we got here
- Connect to reader's life

**Option C: Person's Story → Science → Takeaway**
- Start with a composite patient scenario
- Weave in the science
- End with actionable understanding

#### Voice Guidelines

**Write like a knowledgeable friend who happens to be a cardiologist—not like an expert talking down.**

DO:
- "Here's what this actually means for you..."
- "The short version is..."
- "Scientists figured out that..."
- "What surprised researchers was..."
- "In plain terms..."

DON'T:
- "It's important to understand that..."
- "One must consider..."
- "The clinical implications are..."
- "Healthcare providers should..."

#### Handling Trial Names

**General rule**: If YOU need the trial name to verify the science, keep it in your references. The reader almost never needs it.

**When to mention trial names**: Only when the name itself is widely known by patients (rare) or when you're writing a longer piece where you'll reference the same trial multiple times.

**How to handle**:
- ❌ "The SELECT trial showed..."
- ✅ "A large study of people taking semaglutide..."
- ✅ "When researchers tested this in over 17,000 patients..."
- ✅ "The biggest study to date found..." (cite in references)

#### Handling Statistics

**Convert ALL statistics to human terms:**

| Academic | For People |
|----------|------------|
| 35% relative risk reduction | About 1 in 3 fewer events |
| HR 0.74 (95% CI 0.65-0.85) | Roughly a quarter less likely |
| NNT = 25 | For every 25 people treated, 1 person benefits |
| p < 0.001 | Very strong evidence (drop this entirely usually) |
| Median follow-up 4.2 years | After about 4 years |
| Primary composite endpoint | The main things researchers were counting |

**When to use numbers:**
- Use actual numbers for things people can visualize: "3,000 patients" is fine
- Use fractions/ratios for effects: "about 1 in 10" is better than "10%"
- Use comparisons: "roughly the same risk reduction as stopping smoking"

#### Word Substitutions

See `references/plain-language-guide.md` for complete list. Quick reference:

| Medical | Plain |
|---------|-------|
| myocardial infarction | heart attack |
| cardiovascular death | death from heart problems |
| hospitalization for heart failure | ending up in the hospital because your heart is struggling |
| composite endpoint | combination of outcomes |
| randomized controlled trial | well-designed study where patients were randomly assigned |
| placebo | sugar pill / inactive treatment |
| statistically significant | unlikely to be a coincidence |
| hazard ratio | risk comparison |
| mechanism of action | how the drug works |
| pharmacokinetics | how the drug moves through your body |
| adverse events | side effects |
| contraindicated | shouldn't be used |
| comorbidities | other health conditions |
| titration | adjusting the dose |
| prognosis | likely outcome |

### Step 4: Verify Accuracy

Before finalizing, confirm:
- Every factual claim has a PubMed reference you can cite
- Numbers haven't been distorted in translation
- Simplification hasn't created inaccuracy
- A cardiologist reading this would nod, not cringe

### Step 5: Add References Section

At the end, include a "Sources" or "The Evidence" section:

**Format**:
```
## The Evidence

1. The heart failure drug study mentioned: McMurray JJV et al. Dapagliflozin in Patients with Heart Failure and Reduced Ejection Fraction. N Engl J Med. 2019;381(21):1995-2008. DOI: 10.1056/NEJMoa1911303

2. The weight loss medication study: Lincoff AM et al. Semaglutide and Cardiovascular Outcomes in Obesity without Diabetes. N Engl J Med. 2023;389(24):2221-2232. DOI: 10.1056/NEJMoa2307563
```

This section serves two purposes:
1. Your user can verify you interpreted the science correctly
2. Curious readers can dig deeper

## Length Guidelines

**Short form (tweets, posts)**: 280-500 words
- One core message
- One surprising fact or reframe
- One takeaway

**Medium form (newsletter, article)**: 800-1500 words  
- Clear story arc
- 2-3 supporting points
- Practical implications
- References at end

**Long form (deep dive)**: 2000-3000 words
- Can handle more complexity
- Still no jargon
- More context and nuance
- Multiple reference sources

## Voice Positioning

**Write as**: An interventional cardiologist who genuinely enjoys explaining medicine to interested laypeople. Not talking down. Not dumbing down. Just... talking.

**First person is okay**:
- "In my clinic, I see patients who..."
- "What I find remarkable is..."
- "When I explain this to patients, I tell them..."

**Reader relationship**:
- They're intelligent but not medically trained
- They can handle complexity if it's explained well
- They want to understand, not just be told
- They'll tune out if you sound like a textbook

## Workflow Decision Tree

```
START: User wants to explain cardiology science to general audience
│
├─→ What's the source material?
│   ├─ Trial/Paper → Research via PubMed MCP
│   ├─ Topic/Question → Research via PubMed MCP
│   └─ User-provided PDF/abstract → Extract key points, verify via PubMed
│
├─→ Research phase
│   ├─ Use PubMed:search_articles for relevant trials
│   ├─ Get 5-8 references from major journals
│   ├─ Extract: What actually happened? What does it mean?
│   └─ Identify the human story
│
├─→ Writing phase
│   ├─ Lead with story/meaning, not data
│   ├─ Translate all statistics to human terms
│   ├─ Background trial names (references section)
│   ├─ Foreground understanding and implications
│   ├─ Keep language at 8th grade reading level
│   └─ Maintain full scientific accuracy
│
├─→ Verification phase
│   ├─ Would a cardiologist approve the accuracy?
│   ├─ Would an 8th grader understand it?
│   ├─ Is every claim backed by a citable reference?
│   └─ Have statistics been translated without distortion?
│
└─→ OUTPUT: Rigorous science in human language + reference section
```

## Quality Checklist

Before delivering:

- [ ] Would someone without medical training understand every sentence?
- [ ] Have all trial acronyms been removed or minimally used?
- [ ] Have all statistics been converted to human terms?
- [ ] Is there a clear "so what" for the reader's life?
- [ ] Does it start with a story or hook, not data?
- [ ] Could a cardiologist verify every claim?
- [ ] Are 5-8 references included at the end?
- [ ] Is the language warm and conversational, not lecturing?
- [ ] Would someone actually want to read this?
- [ ] Is this accurate enough for the user to post without embarrassment?

## What This Skill is NOT

- Not dumbed-down medicine ("eat less, move more")
- Not medical advice ("talk to your doctor about...")
- Not press-release hype ("breakthrough", "game-changing")
- Not academic writing made slightly simpler
- Not content requiring another LLM to understand

## Example Transformation

**Academic (original editorial style):**
"The SELECT trial (Lincoff et al., NEJM 2023) randomized 17,604 adults with established cardiovascular disease and BMI ≥27 without diabetes to semaglutide 2.4 mg weekly or placebo. The primary endpoint—a composite of cardiovascular death, nonfatal MI, or nonfatal stroke—occurred in 6.5% of the semaglutide group versus 8.0% of the placebo group (HR 0.80, 95% CI 0.72-0.90, p<0.001), representing a 20% relative risk reduction over a median follow-up of 39.8 months."

**For People (this skill):**
"Here's something that surprised even cardiologists: a weight loss drug might actually protect your heart—independent of how much weight you lose.

Researchers studied over 17,000 people who already had heart disease and were overweight or obese. Half got weekly injections of semaglutide (the active ingredient in Ozempic and Wegovy), and half got a placebo. After about three years, those on semaglutide were roughly 20% less likely to have a heart attack, stroke, or die from heart problems.

What's striking is this: the benefit showed up before people lost much weight. Something about the drug itself seems to protect blood vessels. Scientists are still working out exactly how, but the evidence was strong enough that cardiologists are now taking notice—especially for patients who have both heart disease and weight to lose.

The bottom line? If you have heart disease and are considering weight loss medications, this one might do double duty. Worth a conversation with your cardiologist."

**Same facts. Different packaging. One requires medical training to appreciate. One doesn't.**

## Essential References

- `references/plain-language-guide.md` - Complete vocabulary translations
- `references/storytelling-patterns.md` - Narrative structures that work
