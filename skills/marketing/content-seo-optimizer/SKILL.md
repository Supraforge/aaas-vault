---
name: content-seo-optimizer
description: >-
  Three-agent SEO audit pipeline. Scrapes your content → analyzes SERP
  competitors → generates prioritized optimization report with P0/P1/P2
  recommendations. Use BEFORE and AFTER publishing to maximize organic reach.
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---

# Content SEO Optimizer

**Your content, discovered.** This skill audits your published content against SERP competitors and generates a prioritized optimization roadmap.

---

## When to Use

| Scenario | Use This Skill? |
|----------|-----------------|
| Before publishing a blog post | Yes - optimize before going live |
| After publishing, low traffic | Yes - diagnose and fix |
| YouTube video optimization | Yes - title, description, tags |
| Newsletter landing page | Yes - improve discoverability |
| Academic/medical content | Yes - with medical keyword focus |

---

## How It Works

```
YOUR CONTENT URL
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│ AGENT 1: PAGE AUDITOR                                        │
│                                                              │
│ • Scrapes your page (Firecrawl/WebFetch)                    │
│ • Extracts: title, meta, headings, word count, links        │
│ • Identifies: primary keyword, secondary keywords           │
│ • Flags: technical issues, content gaps                     │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│ AGENT 2: SERP ANALYST                                        │
│                                                              │
│ • Searches Google/Perplexity for your primary keyword       │
│ • Analyzes top 10 competitors                               │
│ • Extracts: title patterns, content formats, themes         │
│ • Identifies: differentiation opportunities                 │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│ AGENT 3: OPTIMIZATION ADVISOR                                │
│                                                              │
│ • Synthesizes audit + SERP data                             │
│ • Generates McKinsey-style recommendations                  │
│ • Prioritizes: P0 (critical), P1 (important), P2 (nice)     │
│ • Outputs: actionable report with expected impact           │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
SEO AUDIT REPORT (Markdown)
```

---

## Usage

### In Claude Code (Recommended)

```
Audit SEO for https://yoursite.com/article-about-statins
```

or

```
Use content-seo-optimizer for my blog post: [URL]
```

### For YouTube Content

```
Optimize SEO for my YouTube video: https://youtube.com/watch?v=xxxxx
```

Claude will:
1. Fetch the video page
2. Analyze title, description, tags
3. Research competing videos
4. Suggest optimizations

### CLI Mode

```bash
python skills/cardiology/content-seo-optimizer/scripts/seo_audit.py \
    --url "https://yoursite.com/article" \
    --keyword "statins cardiovascular risk"  # Optional override
```

---

## Output: SEO Audit Report

```markdown
# SEO Audit Report

**URL:** https://yoursite.com/statin-myths-debunked
**Audit Date:** 2026-01-01
**Primary Keyword:** statin myths

---

## Executive Summary

Your article targets "statin myths" with moderate optimization.
The title is strong but meta description is missing key terms.
Competitors are using listicle formats (5 myths, 7 facts) which
you should consider adopting. Word count (1,200) is below
competitor average (2,100).

**Overall Score:** 65/100
**Quick Wins Available:** 3 changes could boost score to 80+

---

## Technical & On-Page Findings

### Title Tag
**Current:** "Debunking Statin Myths - Dr. Singh"
**Length:** 38 characters (optimal: 50-60)
**Recommendation:** "7 Statin Myths Exposed: Cardiologist Reveals Truth [2026]"
**Rationale:** Add number, year, and authority signal

### Meta Description
**Current:** [MISSING]
**Recommendation:** "Interventional cardiologist debunks the 7 most
dangerous statin myths. Evidence-based analysis of side effects,
muscle pain, and who really needs statins."
**Length:** 158 characters (optimal)

### Heading Structure
- H1: ✅ Present ("Debunking Statin Myths")
- H2s: ⚠️ Only 2 (competitors average 7)
- H3s: ❌ None (add for each myth)

### Content Depth
- **Your word count:** 1,200
- **Competitor average:** 2,100
- **Gap:** 900 words
- **Recommendation:** Expand with clinical evidence, patient stories

### Link Profile
- Internal links: 3 (low - aim for 8-10)
- External links: 2 (good - both to journals)
- Suggested internal links:
  - Your article on LDL targets
  - Your cholesterol video
  - Your cardiovascular risk calculator

---

## Keyword Analysis

### Primary Keyword
**Target:** "statin myths"
**Search Volume:** ~2,400/month
**Competition:** Medium
**Your Current Ranking:** Not in top 100

### Secondary Keywords (add to content)
- statin side effects myths (1,200/mo)
- do statins cause muscle pain (800/mo)
- statin benefits vs risks (600/mo)
- should I take statins (1,500/mo)

### Search Intent
**Dominant:** Informational
**User Need:** Reassurance, evidence-based answers
**Content Angle:** Counter misinformation with authority

---

## Competitive SERP Analysis

### Top 5 Competitors

| Rank | Title | Word Count | Format |
|------|-------|------------|--------|
| 1 | "5 Statin Myths That Could Kill You" | 2,400 | Listicle |
| 2 | "The Truth About Statins: What You Need to Know" | 1,800 | Guide |
| 3 | "Statin Myths and Facts - Harvard Health" | 2,100 | FAQ |
| 4 | "7 Common Statin Myths Exposed" | 1,900 | Listicle |
| 5 | "Statins: Benefits, Risks, and Myths" | 2,500 | Comprehensive |

### Patterns in Top Results
- **Titles:** Numbers (5, 7), emotional words (truth, exposed, kill)
- **Formats:** Listicles dominate (4 of 5)
- **Authority:** Medical credentials mentioned (Harvard, MD)
- **Length:** All 1,800+ words

### People Also Ask
- Are statin side effects exaggerated?
- What are the real risks of statins?
- Do statins cause memory loss?
- Should everyone over 50 take statins?

### Your Differentiation Opportunity
- **Angle:** Active interventional cardiologist perspective
- **Unique:** Real cath lab stories, patient outcomes
- **Voice:** Hinglish content not available in English SERP

---

## Prioritized Recommendations

### P0 - Critical (Do This Week)

| Action | Rationale | Impact | Effort |
|--------|-----------|--------|--------|
| Add meta description | Missing entirely - major SEO gap | High | Low |
| Restructure as listicle (7 myths) | Top 4 competitors use this format | High | Medium |
| Add year to title [2026] | Freshness signal, higher CTR | Medium | Low |

### P1 - Important (Do This Month)

| Action | Rationale | Impact | Effort |
|--------|-----------|--------|--------|
| Expand to 2,000+ words | Below competitor average by 900 | High | Medium |
| Add FAQ schema | Capture People Also Ask | Medium | Low |
| Add 5+ internal links | Low link density hurting authority | Medium | Low |
| Include patient stories | Differentiation + engagement | Medium | Medium |

### P2 - Nice to Have

| Action | Rationale | Impact | Effort |
|--------|-----------|--------|--------|
| Add video embed | Mixed media boosts dwell time | Low | Low |
| Create infographic | Shareable, backlink potential | Medium | High |
| Hindi/Hinglish version | Capture India market gap | Medium | High |

---

## Next Steps

1. **Immediate:** Add meta description (5 minutes)
2. **This week:** Restructure as "7 Statin Myths" listicle
3. **This month:** Expand content with evidence + FAQ schema
4. **Measure:** Check ranking in 2-4 weeks
5. **Iterate:** Re-audit after changes

---

## Measurement Plan

| Metric | Current | Target | Timeline |
|--------|---------|--------|----------|
| Google ranking (primary KW) | 100+ | Top 20 | 4 weeks |
| Organic traffic | 0/month | 200/month | 8 weeks |
| CTR from search | N/A | 5%+ | 4 weeks |
| Avg. time on page | Unknown | 3+ min | 4 weeks |
```

---

## Medical Content Specific Features

### Pre-configured Medical Keywords

The skill understands medical/cardiology context:

| Your Topic | Suggested Keywords |
|------------|-------------------|
| Statins | statin myths, statin side effects, cholesterol medication |
| SGLT2 | SGLT2 inhibitors, diabetes heart medication, Jardiance benefits |
| Heart failure | heart failure treatment, ejection fraction, HFpEF |
| CAC scoring | coronary calcium score, heart scan, cardiac CT |
| Blood pressure | hypertension treatment, high blood pressure medication |

### Medical Authority Signals

Recommendations include:
- Adding MD/cardiologist credentials to title/bio
- Citing PubMed studies (with PMIDs)
- Referencing guidelines (ACC/AHA/ESC)
- Medical schema markup

---

## Integration with Other Skills

### Pre-Publish Workflow
```
1. Write content with cardiology-newsletter-writer
2. Research with quick-topic-researcher (PMIDs)
3. Check with viral-content-predictor (engagement score)
4. Audit with content-seo-optimizer (SEO score)  ← This skill
5. Refine based on recommendations
6. Publish
```

### Post-Publish Workflow
```
1. Publish content
2. Wait 2-4 weeks for indexing
3. Audit with content-seo-optimizer
4. Implement P0/P1 recommendations
5. Re-audit in 4 weeks
```

---

## Technical Architecture

### Tools Used

| Tool | Purpose | Fallback |
|------|---------|----------|
| **Firecrawl MCP** | Page scraping | WebFetch |
| **Perplexity MCP** | SERP research | WebSearch |
| **Claude** | Analysis & report | - |

### Dependencies

```bash
# Optional - for CLI mode with Firecrawl
pip install firecrawl-py

# For Google ADK version (advanced)
pip install google-adk pydantic>=2.7.0
```

### API Keys

| Key | Purpose | Required? |
|-----|---------|-----------|
| FIRECRAWL_API_KEY | Page scraping | Optional (use WebFetch fallback) |
| GOOGLE_API_KEY | SERP research | Already have |
| PERPLEXITY_API_KEY | Alternative SERP | Already have |

---

## Comparison with Paid Tools

| Feature | This Skill | Ahrefs ($99/mo) | Semrush ($119/mo) |
|---------|------------|-----------------|-------------------|
| Page audit | ✅ | ✅ | ✅ |
| SERP analysis | ✅ | ✅ | ✅ |
| Keyword suggestions | ✅ | ✅ | ✅ |
| Competitor analysis | ✅ | ✅ | ✅ |
| Medical context | ✅ | ❌ | ❌ |
| Integrated with your content system | ✅ | ❌ | ❌ |
| Cost | $0 | $99/mo | $119/mo |

---

## Example Session

**User:** Audit SEO for https://drshailesh.com/statin-myths

**Claude:**

I'll perform a comprehensive SEO audit using the 3-agent pipeline.

**Agent 1: Page Auditor**
[Fetches page, extracts structure, identifies keywords]

**Agent 2: SERP Analyst**
[Researches "statin myths", analyzes top 10 competitors]

**Agent 3: Optimization Advisor**
[Synthesizes findings into prioritized report]

---

# SEO Audit Report

[Full report as shown above]

---

**Quick Wins You Can Do Right Now:**
1. Add meta description (copy from report)
2. Add [2026] to title
3. Change H1 to "7 Statin Myths..."

Would you like me to help implement any of these changes?

---

*This skill turns your great content into discoverable content.*
