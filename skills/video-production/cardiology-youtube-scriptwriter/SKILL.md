---
name: cardiology-youtube-scriptwriter
description: >-
  End-to-end YouTube content creation for cardiology channels. Use when user
  wants to create YouTube videos about cardiology, heart health, or
  cardiovascular topics. Triggers on greetings with content intent, requests for
  video ideas or scripts, help with cardiology YouTube channels, heart health
  video content requests, or any cardiology content creation conversation.
  Handles complete workflow from ideation through social listening, topic
  selection, and full script delivery.
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---

# Cardiology YouTube Scriptwriter

Complete workflow from "Hello" to finished script. Combines social listening research with proven content frameworks to create engaging cardiology YouTube content.

---

## Workflow Overview

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  1. HELLO   │────▶│ 2. RESEARCH │────▶│ 3. IDEATE   │────▶│ 4. APPROVE  │────▶│ 5. SCRIPT   │
│  Discovery  │     │   Social    │     │   Generate  │     │   Select    │     │   Write     │
│             │     │   Listening │     │   Ideas     │     │   Idea      │     │   Full      │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

---

## Phase 1: Discovery

When user starts conversation, gather context:

**Ask (pick 2-3 most relevant):**
- What's your channel about / who's your audience?
- What topics have performed well / poorly for you?
- Any specific areas you want to focus on?
- Video length preference? (Shorts, 5-10 min, long-form)
- What's your content goal? (Grow subs, educate, build authority)
- Any topics you want to avoid?

**Keep it conversational** - don't interrogate. If user just wants to dive in, roll with it.

---

## Phase 2: Social Listening Research

**Use web search** to find what's trending and what people are asking about.

### Search Strategy

Execute 3-5 searches mixing these patterns:

```
1. Reddit: "site:reddit.com [topic] heart" OR "site:reddit.com cardiology"
2. Questions: "[cardiology topic] questions people ask"
3. Trends: "heart health trending 2024" OR "[topic] new research"
4. YouTube: "cardiology YouTube video ideas" (see what's working)
5. Forums: "[topic] patient questions forum"
```

### Extract & Synthesize

Look for:
- **Hot questions** people are asking
- **Misconceptions** that need correcting
- **Emotional language** (fear, confusion, hope)
- **Gaps** in existing content
- **Trending hooks** and angles

Reference: [social-listening.md](references/social-listening.md) for detailed research methodology.

---

## Phase 3: Generate Ideas

Combine social listening insights with seed topics and modifiers.

### Formula
```
[Seed Topic] + [Modifier(s)] + [Social Insight] = Targeted Video Concept
```

### Resources
- **Seeds:** [seeds.md](references/seeds.md) - 300 cardiology topics across 15 categories
- **Modifiers:** [modifiers.md](references/modifiers.md) - 200+ angles, audiences, and hooks

### Generate 3-5 Ideas

For each idea, provide:

```
### Idea [#]: [Working Title]

**Hook Angle:** [One-sentence hook]
**Target Audience:** [Who this is for]
**Why Now:** [Social listening insight that validates this]
**Format:** [Listicle / Explainer / Myth-Buster / Story / etc.]
**Length:** [Estimated minutes]
**Seed + Modifiers Used:** [Show the combination]
```

### Quality Filters

Each idea must pass:
- [ ] Addresses real question/concern from research
- [ ] Clear audience and intent
- [ ] Not fear-mongering without actionable advice
- [ ] Differentiated from obvious existing content
- [ ] Matches user's channel focus and style

---

## Phase 4: Approval

Present ideas and let user choose. Be ready to:
- **Refine:** Adjust angle, audience, or scope
- **Combine:** Merge elements from multiple ideas  
- **Regenerate:** Create fresh options if none fit
- **Clarify:** Explain why certain angles work

Get clear approval before moving to script.

---

## Phase 5: Script Writing

Reference: [script-templates.md](references/script-templates.md) for structures and retention techniques.

### Select Structure Based on Video Type

| Video Type | Use Template |
|------------|--------------|
| Educational explainer | Structure A |
| List/ranking | Structure B |
| Myth vs fact | Structure C |
| Case study / story | Structure D |
| Short-form (<60s) | Structure E |

### Script Sections

**Every script includes:**

1. **HOOK (0:00-0:30)**
   - Pattern interrupt or surprising fact
   - Clear promise of value
   - "Stay for..." tease (optional)

2. **INTRO (0:30-1:30)**
   - Brief credibility (don't over-explain)
   - Context: Why this matters now
   - Preview: What viewer will learn

3. **MAIN CONTENT**
   - Chunked into clear sections
   - Retention elements every 2-3 min
   - Evidence + stories + practical tips balanced

4. **WRAP-UP**
   - 3 key takeaways (numbered)
   - Clear CTA
   - Engagement prompt

### Script Format

Deliver scripts in this format:

```
# [VIDEO TITLE]
## [Subtitle / Hook Line]

**Target Length:** X minutes
**Style Notes:** [Tone, pacing, B-roll suggestions]

---

### HOOK [0:00-0:30]

[Script text with suggested delivery cues]

**[GRAPHIC: Key stat or visual]**

---

### INTRO [0:30-1:30]

[Script text]

---

### SECTION 1: [Title] [Timestamp]

[Script text]

**💡 RETENTION MOMENT:** [Pattern interrupt or question]

---

[Continue sections...]

---

### WRAP-UP + CTA [Timestamp]

**3 KEY TAKEAWAYS:**
1. [Takeaway]
2. [Takeaway]  
3. [Takeaway]

[CTA script]

---

## Production Notes

**Suggested B-Roll:**
- [Scene suggestions]

**Graphics/Text Overlays:**
- [Key stats or terms to display]

**Thumbnail Concept:**
- [Visual idea for thumbnail]
```

---

## Safety & Quality Guardrails

### Always Include:
- Medical disclaimer (education, not personal advice)
- "Talk to your doctor" for decision-making
- Balanced presentation of evidence
- Emergency warning signs when relevant

### Never Include:
- Guaranteed outcomes or cure claims
- Anti-doctor or anti-medicine rhetoric
- Unsubstantiated alternative treatments as fact
- Content that could delay emergency care
- Fear-mongering without actionable guidance

### Handle Carefully:
- Controversial topics: Present evidence fairly
- Supplements: Acknowledge evidence levels
- Medications: Side effects AND benefits
- Alternative approaches: Neither dismiss nor endorse without evidence

---

## Quick Reference

**For idea generation:** Read seeds.md + modifiers.md
**For script structures:** Read script-templates.md
**For research approach:** Read social-listening.md

---

## Example Workflow

```
User: "Hey, I want to create some YouTube content this week"

Claude: [Phase 1] "Great! Quick questions - what's your audience like, 
        and any topics you're excited about or want to avoid?"

User: "My audience is mostly 40-60, worried about heart disease. 
       Open to anything but want to stay positive."

Claude: [Phase 2] *Performs 4-5 web searches for trending topics, 
        Reddit discussions, recent news*

Claude: [Phase 3] "Based on what I found, here are 4 ideas..."
        *Presents structured ideas with hooks and validation*

User: "Love idea #2, but can we make it more for beginners?"

Claude: [Phase 4] "Absolutely, here's the refined version..."

User: "Perfect, let's do it!"

Claude: [Phase 5] *Delivers full script with hook, structure, 
        timestamps, and production notes*
```
