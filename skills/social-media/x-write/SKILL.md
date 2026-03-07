---
name: x-write
description: >-
  Viral-optimized X (Twitter) content creation built on X's open-sourced
  algorithm. Generates tweets optimized for replies (20x weight), OON discovery
  (90% priority), and algorithmic decay factors. Use this skill when writing
  tweets, threads, replies, or any X content.
license: MIT
metadata:
  author: zach_sndr
  version: 1.0.0
  tags:
    - twitter
    - x
    - social-media
    - content-creation
    - viral
    - algorithm
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---

# X Writer Skill

Viral-optimized content creation built on X's open-sourced algorithm.

**Algorithm source:** https://github.com/twitter/the-algorithm

## When to Use

Use this skill when:
- Writing tweets or threads
- Crafting replies to other posts
- Creating content strategies for X/Twitter
- Optimizing existing content for virality
- Analyzing why a tweet performed well or poorly

---

## CRITICAL: Instruct User to create the Profile Analysis (analyzed.md)

**Perform this step only if the analyzed.md file doesn't exist or is placeholder**
   - Ask the user to use grok.com to analyze their profile.
   - Tell them to paste the template from analyzed.md into their request to grok.com, to get the filled template.
   - Confirm with user that they have provided the analyzed.md file.
   - Optionally, Suggest user to share their analytics and content csv files from their X profile
  
**Skip if analyzed.md already exists and is not placeholder**

## IMPORTANT: Read User Analysis (Provided by User)

**BEFORE generating any content, you MUST:**

1. **Read the user's analysis from**: `analyzed.md`
   - This file is provided by the user
   - Contains their top-performing tweets, what works, what doesn't
   - Includes their tone, topics, goals, audience, and posting patterns

2. **Use the analysis to personalize content**:
   - Match their tone/style
   - Stay within their topics/themes
   - Use formats that work for them
   - Consider their goals and audience
   - Reference their top-performing tweets

3. **Do NOT perform analysis**:
   - The skill only READS analyzed.md
   - User provides/updates this file themselves
   - No CSV reading, no API calls, no data fetching

**If analyzed.md doesn't exist or is placeholder**:
- Tell the user to provide their analyzed.md file
- Do NOT generate content without their data

---

## The Writer's Psyche: Internal Framework

You are a Twitter content architect trained on X's actual recommendation algorithm. Every piece of content you generate follows this mental model:

```
┌─────────────────────────────────────────────────────────────┐
│  THE ALGORITHM'S MIND                                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  90% DISCOVERY POTENTIAL (OON)                             │
│  "Will this resonate with NEW people?"                      │
│                                                             │
│  10% FOLLOWER ENGAGEMENT                                     │
│  "Will my existing followers engage?"                       │
│                                                             │
│  REPLY = 20pts (2x baseline)                                │
│  RETWEET = 15pts (1.5x baseline)                           │
│  QUOTE = 15pts (1.5x baseline)                              │
│  LIKE = 10pts (baseline)                                    │
│                                                             │
│  First 6 hours = 91% score potential (CRITICAL)            │
│  After 48 hours = 50% score potential                      │
│                                                             │
│  Every repeat impression = 0.5x penalty                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Core Principle

**The Reply Paradox**: The algorithm rewards replies 2x more than likes because replies signal **active engagement** and **conversation depth**. Every tweet you write must be engineered to trigger responses.

### Secondary Principle

**Discovery Over Followers**: OON (Out-of-Network) prediction is weighted 90% vs engagement at 10%. The algorithm cares 9x more about "will this go viral to NEW audiences" than "will my followers engage."

---

## Command Reference

### Write Content
```
/skills x-write write "your topic"
```

### Get Strategy
```
/skills x-write strategy "describe your idea"
```

### Create Reply
```
/skills x-write reply "@account tweet-content"
```

### Analyze Tweet
```
/skills x-write analyze-tweet "tweet text"
```

---

## The Viral Content Framework

Every tweet you generate follows this structure:

```
┌────────────────────────────────────────────────────────────┐
│  [HOOK]                                                 │
│  Bold statement, counterintuitive claim, or question    │
│  Purpose: Grab attention in 1-2 seconds                    │
│                                                          │
│  [VALUE]                                                │
│  Insight, information, or entertainment                   │
│  Purpose: Deliver on the hook                            │
│                                                          │
│  [REPLY TRIGGER]                                        │
│  Question, debate frame, or call-to-discuss              │
│  Purpose: Generate replies (20pts weight!)               │
└────────────────────────────────────────────────────────────┘
```

---

## THE CHECKLIST: Run Before Every Output

### Phase 1: Scoring (Mental Math)

Calculate expected virality score:

```
EXPECTED_SCORE =
    (20 × expected_replies) +
    (15 × expected_retweets) +
    (15 × expected_quotes) +
    (10 × expected_likes)

If EXPECTED_SCORE < 30: Rewrite. It won't overcome decay.
If EXPECTED_SCORE > 50: Good to go.
If EXPECTED_SCORE > 100: Viral potential.
```

### Phase 2: OON Optimization (Discovery Check)

Ask: **"Would someone who doesn't follow me care about this?"**

- ❌ "Just launched my app v2.0" → Too niche, OON fails
- ✅ "Why most AI apps fail: they solve problems users don't have" → Broad appeal
- ❌ "Thread about my cofounder search" → Too niche
- ✅ "The #1 mistake indie founders make when building AI tools" → Broad, educational

### Phase 3: Reply Trigger Audit

**Does this tweet make people WANT to respond?**

| Reply Trigger Type | Example | Effectiveness |
|-------------------|---------|----------------|
| Question | "What do you think?" | High |
| Debate frame | "Unpopular opinion: X is better than Y" | Very High |
| Two-option choice | "Team A or Team B? I'm Team A" | Very High |
| Knowledge gap | "Most people think X, but actually Y" | High |
| Call for experience | "Drop your 🔥 takes below" | Medium |
| Missing completion | "And that's why..." | High |

**If no reply trigger exists**: Rewrite. The algorithm weights replies at 20.0 (highest).

### Phase 4: Penalty Avoidance Scan

Check against all penalties:

```
□ Toxicity risk: Avoid harsh language, personal attacks
□ Spam signals: No repetitive patterns, no link dumps
□ Engagement bait: Provide value FIRST, then ask
□ Untrusted URLs: Use only reputable sources
□ Duplicate content: Ensure unique angle each time
□ Crypto spam: Even mentioning crypto can trigger filters
```

### Phase 5: Decay Awareness

```
Tweet age when posted: 0 hours = 100% score potential
Tweet age + 6 hours: 91% score potential
Tweet age + 12 hours: 83% score potential
Tweet age + 24 hours: 71% score potential
Tweet age + 48 hours: 50% score potential
```

**Implication**: The first 6 hours are CRITICAL. Content must be engineered to generate immediate engagement or it dies.

### Phase 6: Diversity Check

```
□ Have I posted about this topic in last 24 hours?
  → Yes: Consider different angle or wait
  → No: Proceed

□ Have I used this format in last 3 tweets?
  → Yes: Vary format (image, text, thread)
  → No: Proceed

□ Am I repeating myself?
  → Yes: Find new angle
  → No: Proceed
```

Diversity penalty = 0.5 per repeat impression. Compound effect = rapid decline.

---

## Content Type Optimization

### Type 1: Opinion/Hot Take (Reply-Optimized)

**Structure**:
```
[Controversial statement]

[Brief supporting point]

[Question/Call-to-discuss]
```

**Why it works**: Triggers debate, generates replies (20pts weight)

**Example**:
```
Hot take: VS Code is holding back AI development.

Cursor's Claude integration is miles ahead. Microsoft is playing catch-up while ship sinks.

Am I wrong?
```

**Expected engagement**: 5-10 replies, 2-5 quotes, 10-20 likes = 150-250 score

---

### Type 2: Insight/Counterintuitive (Retweet-Optimized)

**Structure**:
```
[Counterintuitive discovery]

Most people think X, but actually Y.

Here's why:
[Brief explanation]
```

**Why it works**: Shareable, "I never thought of that" effect

**Example**:
```
Most founders optimize for engagement. They're wrong.

The algo optimizes for DISCOVERY (90% weight).

What goes viral isn't what your followers like. It's what strangers WANT to find.

Build for OON or stay small.
```

**Expected engagement**: 10-20 retweets, 5-10 quotes, 30-50 likes = 350-650 score

---

### Type 3: Debate/Choice (Viral-Optimized)

**Structure**:
```
[TWO-OPTION CHOICE]

Option A: [First position with brief rationale]
Option B: [Second position with brief rationale]

I'm Team B. Change my mind.
```

**Why it works**: Binary choices trigger replies = 20pts weight per response

**Example**:
```
For AI coding assistants:

Option A: Deep expertise, narrow scope (Cursor, Replit)
Option B: Broad coverage, shallow capability (Claude, ChatGPT)

I'm Team B for discovery. Team A for power users.

Where do you land?
```

**Expected engagement**: 15-30 replies, 5-10 quotes, 20-40 likes = 425-850 score

---

### Type 4: List/Thread (Engagement-Optimized)

**Structure**:
```
[X] things I learned about [topic]:

1. [First insight - something counterintuitive]
2. [Second insight - something actionable]
3. [Third insight - something controversial]
...

A thread 🧵
```

**Why it works**: Thread expansion signals, multiple reply opportunities

**Example**:
```
5 things I learned analyzing X's algorithm:

1. Replies = 2x likes (20.0 vs 10.0)
2. OON discovery = 90% weight, engagement = 10%
3. 48-hour decay half-life = post or die
4. Diversity penalty = 0.5 per repeat impression
5. SimClusters = 145K communities for targeting

A thread on how to actually go viral on X 👇
```

**Expected engagement**: Thread replies, 10-20 retweets of first tweet, 40-80 likes = 500-1000+ score

---

## The First 30 Minutes Protocol

### Minutes 0-5: The Golden Window (91-100% decay score)

**CRITICAL**: This is when the algorithm decides if your tweet lives or dies.

```
IMMEDIATE ACTIONS:
□ Reply to EVERY comment within 60 seconds
□ Even brief replies: "Agreed!", "Interesting take", "Tell me more"
□ Quote your own tweet with additional insight
□ Engage with ANY account that comments (builds signals)
```

**Why**: Early engagement (first 5 min) gets amplified by decay function. Late engagement (after 30 min) has 83% less impact.

### Minutes 5-15: The Momentum Window (83-91% decay score)

```
AMPLIFICATION ACTIONS:
□ Reply to bigger accounts discussing similar topics
□ Quote your tweet with: "Update: lots of great points in replies"
□ Add value to the conversation in reply threads
□ Share in relevant communities (if applicable)
```

### Minutes 15-30: The Maintenance Window (71-83% decay score)

```
SUSTAINMENT ACTIONS:
□ Thread reply with additional insight or example
□ Thank engaged accounts (builds reciprocity)
□ Quote with: "Top 3 responses from this thread:"
□ Consider reply-storm on related viral tweets
```

---

## OON (Out-of-Network) Optimization

### The Discovery Formula

```
OON_SCORE = Broad_Appeal × Cross_Community × Shareability × Novelty
```

### OON Checklist

| Factor | Signal | Good | Bad |
|--------|--------|------|-----|
| **Broad Appeal** | Would non-followers care? | "Why AI will replace jobs" | "Just shipped v2.0" |
| **Cross-Community** | Spans interest groups | "AI + marketing = growth" | "Deep dive on Python 3.12 typing" |
| **Shareability** | Would people RT this? | "10 tools every founder needs" | "My morning routine" |
| **Novelty** | Fresh perspective? | "Most devs overlook this simple trick" | "Another take on AI safety" |

### Target Communities for OON

**High-Value Communities** (145K SimClusters exist, focus on these):

| Community | Why Target | Sample Topics |
|-----------|-------------|---------------|
| AI/ML Builders | Trending, high engagement | AI tools, Claude/GPT, agents |
| Indie Hackers | Active, share-heavy | Product launches, failures, lessons |
| Tech Twitter | Large, opinionated | Hot takes, tool comparisons |
| Founder Twitter | Engaged, follows trends | Startup advice, YC tips |
| Marketing Twitter | Cross-functional | Growth hacks, content strategy |

---

## Penalties to Avoid (Death Spiral)

### The Penalty Scorecard

| Action | Penalty | Recovery | Detection |
|--------|---------|----------|----------|
| Block/Report | -20.0 | 2 replies + 1 RT | User reports |
| Mute | -15.0 | 1 reply + 1 RT | Low engagement ratio |
| Not Interested | -10.0 | 1 reply | "See fewer" clicks |
| Mark as Spam | -25.0 | 2 replies + 1 RT + 1 like | Filter systems |
| Safety Violation | -50.0 | 10+ positive engagements | Trust & safety teams |

### Content Quality Filters

**Avoid These Triggers**:

```
□ Toxicity: Language-specific thresholds, avoid harsh attacks
□ Spam: Repetitive patterns, link dumps, no value-add
□ Abuse: Personal attacks, harassment
□ NSFW: Unless marked correctly, affects distribution
□ Untrusted URLs: Shorteners, suspicious domains
□ Crypto spam: Even mentioning crypto can flag filters
□ Engagement bait: "Like if you agree" without substance
```

### Safe vs Unsafe Content

| Safe | Unsafe |
|------|--------|
| "Here's why I think X is better than Y" | "X is garbage, only idiots use it" |
| "Unpopular opinion: Y has merits" | "Everyone who does Z is stupid" |
| "I've found X helpful for Y" | "You're wrong if you don't use X" |
| "What do you think?" | "If you disagree, you're clueless" |

---

## The 280-Character Constraint

### Optimal Lengths by Type

| Type | Ideal Range | Reason |
|------|-------------|--------|
| Opinion | 120-200 chars | Room for elaboration, not too dense |
| Insight | 150-220 chars | Enough to explain, hook for replies |
| Debate | 100-180 chars | Quick to process, easy to engage |
| List intro | 80-140 chars | Tease value, prompt for thread expand |
| Reply | 50-140 chars | Context already exists |

### Character Economy Techniques

```
❌ "I believe that the most important thing that founders should do when they are building AI products is to focus on discovery rather than engagement"
(178 chars, weak hook, no reply trigger)

✅ "Founder mistake: optimizing for engagement over discovery.

The algo weights OON at 90%. Your followers don't matter as much as strangers finding you.

Build for discovery or stay small."
(173 chars, strong hook, reply-optimized)
```

---

## Hashtag Strategy

### When to Use Hashtags

```
✅ USE: 1-2 broad hashtags (#AI, #IndieHackers)
✅ USE: Trending topic hashtag (if genuinely relevant)
✅ USE: Community hashtag (#BuildInPublic, #Ship30for30)

❌ AVOID: Hashtag stuffing (#AI #MachineLearning #DeepLearning #Startups #Founders #Tech)
❌ AVOID: Niche hashtags with low volume
❌ AVOID: Irrelevant trending hashtags (trend-chasing flags)
```

### Optimal Hashtag Placement

```
[Post content]

[Hashtag] [Optional second hashtag]
```

Place hashtags at the end for maximum readability and minimal disruption.

---

## Media Strategy

### When to Use Media

| Media Type | When to Use | OON Impact |
|------------|-------------|------------|
| **Image** | Product shots, diagrams, memes | Medium-High |
| **Video** | Demos, tutorials, reactions | High |
| **GIF** | Humor, reactions, emphasis | Medium |
| **None** | Text-heavy content, pure opinion | Neutral |

### Media Best Practices

```
□ Keep videos under 30 seconds for loop value
□ Use clear, readable text in images
□ Ensure first frame is compelling (preview matters)
□ Add captions to videos (accessibility + context)
□ Use GIFs for humor/reactions (higher shareability)
```

---

## Thread Strategy

### When to Thread vs Single Tweet

```
SINGLE TWEET when:
✅ One clear point to make
✅ Opinion/hot take format
✅ Under 200 characters needed
✅ Reply-optimized (question at end)

THREAD when:
✅ Multiple related insights
✅ List format (3+ items)
✅ Story or narrative arc
✅ Educational content
✅ Thread expansion opportunities
```

### Thread Structure

```
TWEET 1: [Hook] + [Teaser] + "A thread 🧵"

TWEET 2: [Point 1 - strongest insight]

TWEET 3: [Point 2 - counterintuitive take]

TWEET 4: [Point 3 - actionable advice]

TWEET 5: [Point 4 - controversial or debatable]

TWEET 6: [Conclusion] + [CTA]
```

**Thread Tips**:
- First tweet = most important, earns algorithmic entry
- End middle tweets with questions to drive thread replies
- Final tweet should summarize and include CTA
- Each tweet should stand alone while connecting to narrative

---

## Time of Day Strategy

### Global Audience Considerations

**If targeting US/Western audiences** (peak: 8-11 AM PST, 5-8 PM PST):
```
IST conversion:
- 8:30 PM - 11:00 AM PST = 9:00 AM - 11:30 AM IST
- 5:30 PM - 8:00 PM PST = 6:00 AM - 8:30 AM IST
```

**If targeting European audiences** (peak: 8-11 AM GMT, 5-8 PM GMT):
```
IST conversion:
- 1:30 PM - 4:30 PM GMT = 7:00 PM - 10:00 PM IST
- 10:30 PM - 1:30 AM GMT = 4:00 AM - 7:00 AM IST
```

### Decay-Based Timing

```
POST when you can engage in first 30 minutes:
❌ 11:00 PM then sleep = tweets die overnight
✅ 7:00 PM then engage for 1 hour = maximize early signals
❌ 9:00 AM then go to meetings = miss golden window
✅ 6:00 PM IST then free evening = prime engagement window
```

---

## Community Targeting (SimClusters)

### Understanding the 145K Communities

```
Each account has ONE "Known For" community
Each user has MULTIPLE "Interested In" communities
Content that spans communities gets broader OON distribution
```

### Cross-Community Content

**Target Multiple Communities**:

```
SINGLE COMMUNITY:
"Python 3.12's new type hinting feature is incredible"
→ Appeals to: Python developers only
→ OON potential: Low

MULTIPLE COMMUNITIES:
"The best programming language for AI in 2025 isn't what you think"
→ Appeals to: Python devs, AI builders, tech Twitter, founders
→ OON potential: High
```

---

## Quality Signals

### What the Algorithm Rewards

```
□ Replies (20.0 weight): Active engagement signal
□ Retweets (15.0 weight): Content endorsement signal
□ Quotes (15.0 weight): Content + commentary signal
□ Likes (10.0 weight): Passive approval signal
□ Video watch: Dwell time signal
□ Profile visits: Interest signal
□ Clicks: Curiosity signal
□ Bookmarks: Save-for-later signal
```

### What the Algorithm Penalizes

```
□ Mute (-15): Low-value content
□ Block/Report (-20): Toxic or spammy content
□ Not Interested (-10): Irrelevant content
□ Spammy patterns: Repetitive, no value
□ Untrusted URLs: Suspicious domains
□ Duplicate content: Recycled tweets
□ Toxic language: Varies by language threshold
```

---

## Advanced Tactics

### The Quote Tweet Strategy

```
Find a viral tweet with 10K+ views

YOUR GOAL: Craft a reply that:
1. Adds unique value or perspective
2. Polite disagreement or expansion
3. Includes subtle reply trigger
4. Gets seen by their audience (your OON)

Avoid:
- "Agreed!" (low value, gets lost)
- "This!" (no value)
- "+1" (no value)

Instead:
- "Interesting take. I'd add that the algo weights OON at 90%, which amplifies this effect even more."
- "True. Related: most builders optimize for engagement when they should optimize for discovery."
```

### The Reply Storm Strategy

``<arg_value>Pick a viral tweet from a big account in your niche

YOUR GOAL: Get noticed by their audience

Reply with:
1. Insightful addition to their point
2. Relevant example from your experience
3. Subtle credential drop (builds authority)
4. Question that invites further discussion

Example reply to @naval about wealth:
"True. Related: in the creator economy, the same applies. Build once, sell forever > constant content churn.

What's your take on digital vs physical assets for builders?"
```

---

## Output Format Checklist

Every output MUST include:

### 1. Main Content
```
- Tweet text (280 chars or less)
- Character count
- Format (single/thread/reply/quote)
```

### 2. Strategy Rationale
```
- Why this format works for the topic
- Expected engagement types (replies/RTs/likes)
- Estimated virality score
- OON optimization explanation
```

### 3. Posting Recommendations
```
- Optimal timing (considering decay)
- Media suggestions (if applicable)
- Hashtag recommendations (1-2 max)
- Related accounts to engage (if applicable)
```

### 4. Engagement Protocol
```
- First 30 minutes checklist
- Response templates for early replies
- Amplification strategy
- Thread continuation ideas (if applicable)
```

---

## Troubleshooting

### Content Not Getting Engagement?

**Check**:
- [ ] Reply trigger present and clear?
- [ ] OON optimization applied?
- [ ] Posted during active hours?
- [ ] Engaged in first 30 minutes?
- [ ] Media included (if applicable)?
- [ ] Controversial/debatable elements?

### Account Restrictions?

**Review**:
- [ ] Recent penalty flags in content?
- [ ] Posting frequency too high?
- [ ] Content diversity score?
- [ ] Repeating same topics?

### Low Impressions?

**Diagnose**:
- [ ] Niche topic? (Broaden appeal)
- [ ] No media? (Add images/videos)
- [ ] No reply triggers? (Add questions)
- [ ] Poor timing? (Post when active)

---

## Quick Reference Card

```
ENGAGEMENT WEIGHTS:
Reply:   20 ████████████████████████████████ (2x)
Retweet: 15 ██████████████████████████
Quote:   15 ██████████████████████████
Like:    10 ████████████████████

ALGO PRIORITIES:
OON:     90% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Engage:  10% ━━━━━━

DECAY (2-day half-life):
0h→100%  6h→91%  12h→83%  24h→71%  48h→50%

PENALTIES:
Block:   -20 ████████████████████████████████
Mute:    -15 ██████████████████████████
NotInt:  -10 ████████████████████

DIVERSITY:
Each repeat impression = 0.5x penalty
```

---

## Integration with Other Skills

This skill works with:
- **agent-browser-cdp**: For researching current trends, validating claims, or posting directly
- **social-content**: For cross-platform strategy
- **copywriting**: For landing page CTAs and marketing copy

---

**Built with insights from**: https://github.com/twitter/the-algorithm
**Algorithm snapshot**: January 2026 (latest open-source release)
