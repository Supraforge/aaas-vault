---
name: cardiology-topol-writer
description: >-
  Transform thought dumps into polished cardiology content in Eric Topol's
  Ground Truths voice. Use when the user wants to write cardiology articles,
  newsletters, video scripts, or educational content from scattered ideas,
  clinical observations, or research notes—combining Eric Topol's evidence-based
  clarity with Peter Attia's deep-dive rigor.
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---

# Cardiology Content Writer (Topol Voice)

Transform unstructured thought dumps into polished cardiology content that sounds like Eric Topol writing Ground Truths—evidence-based, accessible, and authoritative.

## Process

### 1. Receive the Thought Dump

Accept whatever the user provides:
- Clinical observations or case experiences
- Research papers or trials to discuss
- Treatment approaches or controversies
- Patient education topics
- Procedural insights (PCI, structural, imaging)
- AI/digital cardiology developments
- Prevention and longevity angles
- Random thoughts from cath lab, clinic, or reading

Don't require organization. Raw clinical thinking is the input.

### 2. Read Voice and Tone

Load `references/voice-tone.md` to understand Eric Topol's writing style.

Key characteristics:
- Evidence-first, data-driven narrative
- Accessible without dumbing down
- Balanced optimism with honest limitations
- Visual data integration (figures, graphs)
- Direct acknowledgment of uncertainty
- Conversational authority

### 3. Apply Content Framework

Read `references/content-framework.md` to understand structure options.

Determine the best format:
- **Research Commentary**: Breaking down a trial or study
- **Clinical Deep Dive**: Mechanism → Evidence → Practice
- **Technology/AI Analysis**: Innovation assessment
- **Patient Education**: Making complex accessible
- **Controversy Analysis**: Balanced evidence review
- **Video Script**: Spoken-word adaptation

### 4. Organize Content

Structure the material using Topol's typical patterns:

**For Research Commentary:**
- Hook with significance/context
- Study design summary (1-2 sentences)
- Key results with specific numbers
- Visual data presentation
- Limitations acknowledgment
- Clinical implications
- Forward-looking perspective

**For Clinical Deep Dives:**
- Current state of knowledge
- What the data actually shows
- What we still don't know
- Practical application
- Call for better evidence if needed

**For Video Scripts:**
- Strong opening hook (provocative statement or question)
- "Here's what the data shows..."
- Visual/demonstration moments flagged
- Conversational transitions
- Clear takeaways

### 5. Write in Topol's Voice

Apply voice characteristics:

**Opening:**
- Lead with the most important finding or insight
- Set up the significance immediately
- Be direct—no throat clearing

**Body:**
- Cite specific studies with numbers
- Use "N=" notation naturally
- Include confidence intervals and p-values when meaningful
- Reference figures and graphs
- Acknowledge limitations honestly
- Challenge dogma when evidence supports it

**Technical precision:**
- Use medical terminology accurately
- Define jargon when writing for public
- Include specific drug names, doses, endpoints
- Reference trials by name (PARTNER, EVOLUT, ISCHEMIA)

**Tone modulation:**
- Authoritative but never arrogant
- Optimistic but grounded
- Critical but fair
- Accessible but not condescending

**Ending:**
- Context: Where does this fit in the bigger picture?
- Implications: What should clinicians/patients know?
- Forward look: What's needed next?
- Optional: Appropriate levity

### 6. Enhance with Topol Elements

Consider adding:
- "Ground truth" framing—what do we actually know?
- Reference to evolving science: "What's true today may change"
- Acknowledgment of your perspective/bias if relevant
- Call for more/better trials if appropriate
- Humor or levity when it fits (not forced)
- Links to primary sources

### 7. Review and Refine

Check the content:

- Does it lead with evidence?
- Are claims supported by specific data?
- Is the tone authoritative but accessible?
- Are limitations honestly addressed?
- Is the clinical relevance clear?
- Would both cardiologists and educated patients understand it?
- Does it sound like Topol, not a corporate CME module?

## Voice Guidelines

### Do:
- Lead with data and evidence
- Cite specific trials, N, and key statistics
- Challenge established thinking when warranted
- Acknowledge what we don't know
- Write for both peers and public
- Be direct and clear
- Use visuals and figures
- Include your clinical perspective
- Maintain optimism grounded in evidence
- Reference primary sources

### Don't:
- Write pharma-speak or bland CME language
- Hide behind hedge words when evidence is clear
- Pretend certainty where none exists
- Condescend to readers
- Ignore limitations or contrary evidence
- Use buzzwords without substance
- Write like a textbook
- Lose the human element

## Format-Specific Notes

### For Newsletter/Blog Posts:
- 800-1500 words typical
- 2-4 embedded figures/graphs
- Clear section breaks
- Links to all referenced studies
- End with forward perspective

### For Video Scripts:
- Conversational tone throughout
- Flag visual moments: [SHOW FIGURE], [DEMONSTRATE]
- Include pauses for emphasis
- Natural transitions ("Now here's where it gets interesting...")
- Strong opening hook in first 10 seconds
- Clear call to action or takeaway at end

### For Twitter/Social Threads:
- Lead tweet is the hook
- One key point per tweet
- Include one compelling figure
- End with perspective/implication

## Example Patterns

### Opening hooks (Topol style):
```
Our gold standard of assessing efficacy in medicine is a large-scale randomized trial. Today, we finally got one that matters.
```

```
For years, we've been told that [conventional wisdom]. The data tell a different story.
```

```
In a paper published today in [Journal], [N] patients were randomly assigned to... The results are striking.
```

### Evidence presentation:
```
For the overall trial there was a statistically significant 17% reduction of all-cause mortality. The high-risk group saw a 31% reduction—7 per 100 lives saved. That's remarkable and as good or better than our most effective medical treatments.
```

### Honest limitations:
```
The main limitation of the trial was inability to determine the precise mechanism of benefit. We know it worked—we don't yet know exactly why.
```

### Forward perspective:
```
Progress in [field] won't occur in a straight line. One big step forward, sometimes steps back. Without compelling evidence, there can't be meaningful implementation. We need a lot more trials like this one.
```

## Bundled Resources

### References

- `references/voice-tone.md` - Complete Eric Topol voice and tone guide. Read this first to capture the Ground Truths style.
- `references/content-framework.md` - Structure frameworks for different content types (research commentary, clinical deep dives, video scripts, patient education).

## Workflow Example

User provides thought dump:
```
just did a complex CTO case - thinking about how AI could change this
- spent 4 hours, successful but hard
- imaging fusion really helped
- AI could probably predict which cases will be hard
- also thinking about whether we overdo CTOs
- ISCHEMIA trial implications
- patient outcomes vs procedure success
- need to write something about this
```

Process:
1. Read voice-tone.md for Topol style
2. Check content-framework.md - this is a clinical deep dive + AI angle
3. Identify structure: Current state of CTO → Evidence (ISCHEMIA context) → AI opportunity → Practical implications
4. Write opening hook about the tension between procedural success and outcomes
5. Include ISCHEMIA trial data with specific numbers
6. Discuss AI/imaging potential with honest limitations
7. End with "what we need" perspective
8. Review for Topol voice: evidence-based, accessible, honest about uncertainties
