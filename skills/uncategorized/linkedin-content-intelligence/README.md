# LinkedIn Content Intelligence Skill - Summary

## What We've Created

A comprehensive **LinkedIn Content Intelligence** skill that integrates:

1. **Content Strategy & Intelligence** - Data-driven insights from ViralBrain.ai patterns
2. **Brand Voice Guidelines** - SupraForge/[PROJECT_NAME]-specific voice and lexicon
3. **Content Frameworks** - 10 proven post structures with templates
4. **Visual Design Integration** - Mockup and carousel creation
5. **Direct LinkedIn Posting** - Via LinkedIn MCP server integration

---

## Skill Location

```
/Users/user/.gemini/[PROJECT_NAME]/skills/linkedin-content-intelligence/
├── SKILL.md (main skill documentation)
└── references/
    ├── linkedin_content_intelligence.md
    ├── brand_voice_guidelines.md
    └── content_frameworks.md
```

---

## Key Intelligence Integrated

### From ViralBrain.ai Context

**High-Performing Content Patterns**:

1. **Contrarian Takes** - Challenge industry "natural laws" (5-8% engagement)
2. **Pain Agitation** - Quantify business impact (4-6% engagement)
3. **Technical Authority** - Demonstrate expertise (3-5% engagement)
4. **Personal Stories** - Vulnerable transformation (6-9% engagement)
5. **Data-Driven Insights** - Lead with statistics (4-6% engagement)

**Algorithm Optimization**:

- **Dwell Time** is most critical (40% weight)
- **Early Engagement** (first hour) drives reach (30% weight)
- **Comments** valued 10x more than likes
- Optimal posting: Tue-Thu, 8-10 AM

**Content Format Performance**:

- Text posts: 3-5% engagement, 30-60s dwell time
- Image posts: 4-6% engagement, 20-40s dwell time
- Video posts: 5-10% engagement (5x text posts)
- PDF Carousels: 6-8% engagement, 90-180s dwell time (highest)
- Polls: 8-12% engagement, 10-20s dwell time

### From Existing Brand Context

**SupraForge/[PROJECT_NAME] Voice Fingerprint**:

- Engineering-authoritative
- Provocative (challenges assumptions)
- ROI-focused (quantifies everything)
- Authentic (shares real experiences)

**Key Lexicon**:

- "Systemic failure" (not "problem")
- "Neural quality layer" (not "AI tool")
- "Late visibility" (not "delayed feedback")
- "Golden thread" (for traceability)
- "By-product of development"
- "Compliance at the speed of code"

**Content Patterns from LinkedIn Intel**:

1. **Tesla vs. Germany** - High tension contrarian positioning
2. **Late Visibility** - Pain agitation with economic argument
3. **Overlay Strategy** - Technical integration approach

---

## How to Use This Skill

### 1. Creating a Thought Leadership Post

```bash
# Step 1: Choose framework
# Use: Contrarian Take or Pain Agitation

# Step 2: Apply brand voice
# Reference: references/brand_voice_guidelines.md

# Step 3: Optimize for algorithm
# Reference: references/linkedin_content_intelligence.md

# Step 4: Post via LinkedIn MCP
# Use: linkedin_post_text tool
```

### 2. Creating Visual Content

```bash
# Step 1: Generate mockup
node skills/visual-designer/scripts/create_linkedin_visual.js input.png output.png

# Step 2: Add branding
node skills/visual-designer/scripts/composite_logo.js output.png logo.svg branded.png

# Step 3: Post with image
# Use: linkedin_post_image tool
```

### 3. Creating a Carousel

```bash
# Step 1: Create content brief
# Use: Framework 10 (Carousel) from content_frameworks.md

# Step 2: Generate slides
node skills/visual-designer/scripts/create_carousel.js brief.md

# Step 3: Export as PDF
# Upload to LinkedIn as document post
```

---

## Integration Points

### Existing Skills

- **content-creator** - SEO optimization, brand voice analysis
- **visual-designer** - Mockup generation, carousel creation
- **notebooklm-intelligence** - Research and insights

### MCP Servers

- **linkedin-mcp-server** - Direct posting to LinkedIn
  - Location: `/Users/user/.gemini/[PROJECT_NAME]/mcp-servers/linkedin`
  - Tools: `linkedin_post_text`, `linkedin_post_image`, `linkedin_post_article`

### Scripts

- **create_linkedin_post.js** - Premium visual generation
- **screenshot_sections.js** - Website capture for mockups
- **composite_logo.js** - Brand logo overlay

---

## Quick Start Guide

### Setup (One-Time)

```bash
# 1. Setup LinkedIn MCP
cd /Users/user/.gemini/[PROJECT_NAME]/mcp-servers/linkedin
npm install
npm run setup  # Authenticate with LinkedIn
npm run build

# 2. Install dependencies
cd /Users/user/.gemini/[PROJECT_NAME]
npm install sharp puppeteer dotenv
```

### Create Your First Post

```bash
# 1. Read the frameworks
cat skills/linkedin-content-intelligence/references/content_frameworks.md

# 2. Choose a pattern (e.g., Contrarian Take)

# 3. Apply brand voice
cat skills/linkedin-content-intelligence/references/brand_voice_guidelines.md

# 4. Write your post (1,300-2,000 characters)

# 5. Post to LinkedIn
# Use linkedin_post_text MCP tool
```

---

## Content Calendar Template

### Weekly Schedule

**Monday**: Industry Insight (Contrarian Take)
**Tuesday**: Thought Leadership (Personal Story)
**Wednesday**: Product/Solution (Technical Deep Dive)
**Thursday**: Engagement (Question Post)
**Friday**: Behind-the-Scenes (Authentic Story)

### Monthly Content Pillars

- 40% Educational (How-to, Best Practices)
- 25% Thought Leadership (Opinion, Trends)
- 25% Engagement (Questions, Community)
- 10% Promotional (Product, Case Studies)

---

## Performance Benchmarks

### Target Metrics

**Engagement Rate**: 3-5% (good), 5-8% (excellent)
**Comment Ratio**: 10-15% of total engagement
**Share Rate**: 1-3%
**Dwell Time**: 30-60 seconds
**Profile Visit Rate**: 3-5%

### Track These KPIs

- Engagement rate: (Likes + Comments + Shares) / Impressions × 100
- Comment rate: Comments / Total Engagement × 100
- Share rate: Shares / Impressions × 100
- Save rate: Saves / Impressions × 100
- Click-through rate: Clicks / Impressions × 100

---

## Best Practices Checklist

### Before Posting

- [ ] Hook in first 2 lines
- [ ] 1,300-2,000 characters
- [ ] Line breaks every 2-3 lines
- [ ] 3-5 relevant hashtags
- [ ] Specific metrics or examples
- [ ] Question or CTA at end
- [ ] Brand voice consistent
- [ ] Optimal posting time (Tue-Thu, 8-10 AM)
- [ ] Engagement plan ready

### After Posting

- [ ] Monitor first hour engagement
- [ ] Reply to all comments within 2 hours
- [ ] Ask follow-up questions in replies
- [ ] Share insights from discussion
- [ ] Document performance metrics
- [ ] Note patterns for future posts

---

## Quarterly Intelligence Review

Every 3 months, analyze:

1. **Top 10 Performing Posts**
   - What patterns worked?
   - Which frameworks drove best engagement?
   - What voice elements resonated?

2. **Audience Insights**
   - Follower growth rate
   - Engagement rate trends
   - Top engaging segments

3. **Content Insights**
   - Best performing formats
   - Optimal posting times (refined)
   - Hashtag performance
   - Topic resonance

4. **Competitive Landscape**
   - New competitors
   - Industry trend shifts
   - Algorithm updates

5. **Action Items**
   - Content adjustments
   - Format experiments
   - New content pillars
   - Skills to develop

Document findings in: `skills/linkedin-content-intelligence/data/quarterly_intelligence.md`

---

## Troubleshooting

### LinkedIn MCP Issues

**"LinkedIn not configured"**

```bash
cd /Users/user/.gemini/[PROJECT_NAME]/mcp-servers/linkedin
npm run setup
```

**"Token expired"** (tokens last 60 days)

```bash
cd /Users/user/.gemini/[PROJECT_NAME]/mcp-servers/linkedin
npm run setup  # Re-authenticate
```

**Posts not appearing**

- Ensure LinkedIn app has "Share on LinkedIn" product enabled
- Check token has `w_member_social` scope

### Content Performance Issues

**Low engagement**

- Review first 2 lines hook
- Post at optimal times (Tue-Thu, 8-10 AM)
- Avoid external links in first hour

**No comments**

- End with question
- Engage with early commenters
- Reply within 2 hours

**Low reach**

- Use native content (no external links initially)
- Increase dwell time (line breaks, formatting)
- Engage with comments to boost algorithm

---

## Next Steps

### Immediate Actions

1. **Review the skill documentation**

   ```bash
   cat /Users/user/.gemini/[PROJECT_NAME]/skills/linkedin-content-intelligence/SKILL.md
   ```

2. **Study the content frameworks**

   ```bash
   cat /Users/user/.gemini/[PROJECT_NAME]/skills/linkedin-content-intelligence/references/content_frameworks.md
   ```

3. **Understand brand voice**

   ```bash
   cat /Users/user/.gemini/[PROJECT_NAME]/skills/linkedin-content-intelligence/references/brand_voice_guidelines.md
   ```

4. **Setup LinkedIn posting**

   ```bash
   cd /Users/user/.gemini/[PROJECT_NAME]/mcp-servers/linkedin
   npm run setup
   ```

### Future Enhancements

1. **Create automation scripts**
   - `generate_content_brief.js` - Auto-generate post briefs
   - `analyze_post_performance.js` - Track and analyze metrics
   - `create_carousel.js` - Auto-generate carousel PDFs

2. **Build data tracking**
   - Performance metrics database
   - A/B testing framework
   - Quarterly intelligence reports

3. **Expand integrations**
   - NotebookLM for research
   - Tavily for competitive intelligence
   - Analytics dashboards

---

## Resources

### Documentation

- Main Skill: `skills/linkedin-content-intelligence/SKILL.md`
- Intelligence: `skills/linkedin-content-intelligence/references/linkedin_content_intelligence.md`
- Brand Voice: `skills/linkedin-content-intelligence/references/brand_voice_guidelines.md`
- Frameworks: `skills/linkedin-content-intelligence/references/content_frameworks.md`

### Existing Assets

- LinkedIn Intel: `docs/strategy/supraforge_linkedin_intel_v1.md`
- Social Media Guide: `skills/content-creator/references/social_media_optimization.md`
- LinkedIn MCP: `mcp-servers/linkedin/README.md`
- Visual Scripts: `skills/visual-designer/scripts/`

### External Resources

- LinkedIn Marketing Labs (free courses)
- Richard van der Blom (algorithm insights)
- Justin Welsh (personal brand building)
- Jasmin Alić (LinkedIn growth)

---

## Summary

You now have a **complete LinkedIn content intelligence system** that combines:

✅ **Data-driven insights** from ViralBrain.ai patterns
✅ **Brand-specific voice** from SupraForge/[PROJECT_NAME] context
✅ **10 proven frameworks** for different content goals
✅ **Algorithm optimization** strategies
✅ **Visual design** integration
✅ **Direct posting** capabilities via MCP

**Start creating high-performing LinkedIn content today!**
