---
name: linkedin-content-intelligence
description: Create data-driven, high-performing LinkedIn content with integrated posting, visual design, and content intelligence. Combines brand voice, SEO optimization, visual mockups, and direct LinkedIn posting capabilities. Use when creating LinkedIn posts, analyzing LinkedIn content strategy, designing LinkedIn visuals, or posting to LinkedIn.
license: MIT
metadata:
  version: 1.0.0
  author: [PROJECT_NAME] AI
  category: marketing
  domain: linkedin-marketing
  updated: 2026-02-12
  integrations: linkedin-mcp-server, content-creator, visual-designer
  tech-stack: LinkedIn-API, Node.js, Sharp, Puppeteer
---

# LinkedIn Content Intelligence

Professional-grade LinkedIn content creation system combining content intelligence, visual design, and direct posting capabilities.

## Keywords

linkedin, linkedin posting, linkedin content, linkedin strategy, b2b marketing, thought leadership, professional networking, linkedin analytics, linkedin carousel, linkedin engagement, content intelligence, viral content, linkedin algorithm, linkedin optimization, social selling

## Quick Start

### Prerequisites

1. **LinkedIn MCP Server** (for posting)

   ```bash
   cd mcp-servers/linkedin
   npm install
   npm run setup  # Authenticate with LinkedIn
   npm run build
   ```

2. **Content Creation Tools**

   ```bash
   npm install sharp puppeteer dotenv
   ```

### Create Your First Post

```bash
# 1. Generate content brief
node skills/linkedin-content-intelligence/scripts/generate_content_brief.js "topic"

# 2. Create visual mockup
node skills/linkedin-content-intelligence/scripts/create_linkedin_visual.js "input.png" "output.png"

# 3. Post to LinkedIn (via MCP)
# Use the linkedin_post_text or linkedin_post_image tools
```

## Core Workflows

### 1. Thought Leadership Post Creation

**Goal**: Create engaging thought leadership content that drives engagement

**Process**:

1. **Research & Intelligence**
   - Review `references/linkedin_content_intelligence.md` for current trends
   - Analyze competitor content patterns
   - Identify trending topics in your industry

2. **Content Development**
   - Use `references/content_frameworks.md` for post structure
   - Apply brand voice from `references/brand_voice_guidelines.md`
   - Optimize for LinkedIn algorithm (see Algorithm Factors below)

3. **Visual Creation** (Optional)
   - Generate mockups using `scripts/create_linkedin_visual.js`
   - Create carousels using `scripts/create_carousel.js`
   - Add branding with `scripts/composite_logo.js`

4. **Publishing**
   - Use LinkedIn MCP tools to post
   - Schedule for optimal times (Tue-Thu, 8-10 AM)
   - Monitor early engagement (first hour critical)

### 2. Data-Driven Content Strategy

**Goal**: Build a content strategy based on performance data

**Process**:

1. **Quarterly Intelligence Review**
   - Analyze top-performing posts
   - Identify content patterns that drive engagement
   - Document insights in `data/quarterly_intelligence.md`

2. **Content Pillar Development**
   - Define 3-5 content pillars
   - Create templates for each pillar
   - Plan content calendar (40/25/25/10 ratio)

3. **Performance Tracking**
   - Track engagement rate, dwell time, comments
   - Document what works in `data/performance_insights.md`
   - Iterate based on data

### 3. Visual Content Creation

**Goal**: Create premium LinkedIn visuals that stand out

**Process**:

1. **Screenshot Capture**

   ```bash
   node scripts/screenshot_sections.js "https://your-site.com" "./screenshots" "dark"
   ```

2. **Mockup Generation**

   ```bash
   # Browser mockup
   node scripts/create_browser_mockup.js "screenshot.png" "output.png" "dark"
   
   # Device mockup
   node scripts/create_mac_iphone_mockup.js "desktop.png" "mobile.png" "output.png" "dark"
   
   # Gradient background
   node scripts/create_gradient_mockup.js "screenshot.png" "output.png" "gold"
   ```

3. **Branding**

   ```bash
   node scripts/composite_logo.js "input.png" "logo.svg" "output.png" "bottom-left" "0.16"
   ```

4. **Carousel Creation**

   ```bash
   node scripts/create_carousel.js "content_brief.md"
   ```

## LinkedIn Algorithm Optimization

### Critical Success Factors

1. **Dwell Time** (Most Important)
   - Keep readers engaged for 30+ seconds
   - Use line breaks, emojis, formatting
   - Hook in first 2 lines (shown in preview)

2. **Early Engagement** (First Hour)
   - Post at optimal times (Tue-Thu, 8-10 AM)
   - Engage with early commenters immediately
   - Seed engagement with close network

3. **Comment Quality**
   - Comments valued 10x more than likes
   - Reply to every comment within 2 hours
   - Ask questions to drive discussion

4. **Content Format Preferences**
   - Native video: 5x more engagement
   - PDF carousels: High dwell time
   - Text posts: Best for thought leadership
   - Polls: Drive engagement but lower reach

### Content Optimization Checklist

- [ ] First 2 lines hook the reader
- [ ] 1,300-2,000 characters (optimal length)
- [ ] Line breaks every 2-3 lines
- [ ] 3-5 relevant hashtags
- [ ] Clear value proposition
- [ ] Question or CTA at end
- [ ] Native content (no external links in first hour)
- [ ] Relevant tags (people/companies)
- [ ] Posted at optimal time
- [ ] Ready to engage with comments

## Content Intelligence Framework

### ViralBrain.ai Insights Integration

**Key Metrics to Track**:

- **Engagement Rate**: (Likes + Comments + Shares) / Impressions × 100
- **Dwell Time**: Average time spent reading
- **Comment Ratio**: Comments / Total Engagement
- **Share Rate**: Shares / Impressions × 100
- **Profile Visits**: Clicks to profile from post

**High-Performing Content Patterns**:

1. **Contrarian Takes**
   - Challenge industry "natural laws"
   - Example: "Tesla doesn't do ASPICE. Here's why that matters..."
   - Hook: Bold statement that creates tension

2. **Pain Agitation**
   - Identify specific pain point
   - Quantify the cost (time, money, opportunity)
   - Example: "40% of engineering time lost to documentation"

3. **Before/After Transformation**
   - Show the problem state
   - Reveal the solution state
   - Bridge with your approach

4. **Data-Driven Insights**
   - Lead with surprising statistic
   - Explain why it matters
   - Provide actionable takeaway

5. **Personal Stories**
   - Vulnerable, authentic experiences
   - Lessons learned
   - Universal application

### Content Frameworks

#### The "Tesla vs. Germany" Pattern (High Tension)

```
Hook: [Contrarian statement about industry leaders]

Context: [Explain the conventional wisdom]

Insight: [Why the conventional wisdom is wrong]

The Real Question: [Reframe the problem]

Solution: [Your approach/perspective]

CTA: [Question to drive discussion]
```

#### The "Late Visibility" Pattern (Pain Agitation)

```
The Problem: [Specific pain point]

The Cost: [Quantify impact - time, money, opportunity]

Why This Happens: [Root cause analysis]

The Better Way: [Your solution approach]

The Result: [Transformation outcome]

Question: [Engage readers with their experience]
```

#### The "Overlay Strategy" Pattern (Technical Authority)

```
The Misconception: [Common wrong assumption]

The Reality: [How it actually works]

Technical Approach: [Your methodology]

Integration Point: [How it fits existing systems]

Business Impact: [ROI/value proposition]

Learn More: [Soft CTA]
```

## Brand Voice Guidelines

### Tone Attributes

- **Engineering-Authoritative**: Speak from technical expertise
- **Provocative**: Challenge assumptions, create tension
- **ROI-Focused**: Always tie back to business value
- **Authentic**: Share real experiences and insights

### Key Lexicon

- "Systemic failure" (not "problem")
- "Neural quality layer" (not "AI tool")
- "Late visibility" (not "delayed feedback")
- "Golden thread" (for traceability)
- "By-product of development" (not "automated output")
- "Compliance at the speed of code"

### Voice Fingerprint

- Use short, punchy sentences for emphasis
- Ask rhetorical questions to create tension
- Quantify everything (40%, 3 months, 10x)
- Challenge "natural laws" and conventional wisdom
- End with thought-provoking questions

## Script Reference

### generate_content_brief.js

Creates a structured content brief for LinkedIn posts.

**Usage**: `node scripts/generate_content_brief.js "topic" [output_file]`

**Generates**:

- Content hook and structure
- Visual specifications
- Hashtag recommendations
- Posting schedule

### create_linkedin_visual.js

Creates premium LinkedIn post visuals with brand styling.

**Usage**: `node scripts/create_linkedin_visual.js "input.png" "output.png" [theme]`

**Features**:

- Dark/light theme support
- Brand gradient backgrounds
- Floating card effects
- Logo compositing

### create_carousel.js

Generates multi-slide LinkedIn carousel PDFs.

**Usage**: `node scripts/create_carousel.js "content_brief.md" [output_dir]`

**Output**: 10-15 slide PDF carousel optimized for LinkedIn

### screenshot_sections.js

Captures website sections for LinkedIn mockups.

**Usage**: `node scripts/screenshot_sections.js "url" "output_dir" [theme]`

**Captures**:

- Hero section
- Feature sections
- Mobile views
- Full page

### analyze_post_performance.js

Analyzes LinkedIn post performance and extracts insights.

**Usage**: `node scripts/analyze_post_performance.js "post_url"`

**Returns**:

- Engagement metrics
- Content pattern analysis
- Optimization recommendations

## LinkedIn MCP Integration

### Available Tools

#### linkedin_post_text

Post text-only content to LinkedIn.

```javascript
// Parameters
{
  text: "Your post content (max 3000 chars)"
}
```

#### linkedin_post_image

Post content with an image.

```javascript
// Parameters
{
  text: "Your commentary",
  imageUrl: "path/to/image.png"
}
```

#### linkedin_post_article

Share an article with preview card.

```javascript
// Parameters
{
  text: "Your commentary",
  articleUrl: "https://article-url.com",
  title: "Custom title (optional)",
  description: "Custom description (optional)"
}
```

#### linkedin_get_profile

Get authenticated user's profile information.

#### linkedin_check_auth

Verify LinkedIn authentication status.

### Authentication

LinkedIn access tokens expire after 60 days. To refresh:

```bash
cd mcp-servers/linkedin
npm run setup
# Follow browser authentication flow
```

## Content Calendar Planning

### Weekly Posting Schedule

**Monday**: Industry Insight

- Share data-driven observation
- Challenge conventional wisdom
- Drive discussion

**Tuesday**: Thought Leadership

- Long-form perspective piece
- Personal experience/story
- Establish authority

**Wednesday**: Product/Solution

- Soft product mention
- Focus on problem-solving
- Educational angle

**Thursday**: Engagement Post

- Poll or question
- Community discussion
- Relationship building

**Friday**: Behind-the-Scenes

- Team/culture content
- Humanize the brand
- Build connection

### Monthly Content Pillars

**40%**: Educational Content

- How-to guides
- Industry insights
- Best practices

**25%**: Thought Leadership

- Opinion pieces
- Trend analysis
- Future predictions

**25%**: Engagement Content

- Questions and polls
- Community discussions
- User stories

**10%**: Promotional

- Product updates
- Case studies
- Company news

## Performance Metrics

### Track These KPIs

**Engagement Metrics**:

- Engagement rate (target: 3-5%)
- Comment rate (target: 1-2%)
- Share rate (target: 0.5-1%)
- Click-through rate (target: 2-4%)

**Reach Metrics**:

- Impressions
- Unique viewers
- Follower growth
- Profile visits

**Business Metrics**:

- Lead generation
- Website traffic
- Demo requests
- Sales conversations

### Quarterly Intelligence Review

Every quarter, analyze:

1. Top 10 performing posts
2. Content patterns that worked
3. Audience engagement trends
4. Competitive landscape shifts
5. Algorithm changes

Document findings in `data/quarterly_intelligence.md`

## Best Practices

### Do's

✅ Post consistently (3-5x per week)
✅ Engage with comments within 2 hours
✅ Use native content (no external links initially)
✅ Hook readers in first 2 lines
✅ Ask questions to drive discussion
✅ Share authentic experiences
✅ Use data to support claims
✅ Tag relevant people/companies
✅ Optimize for dwell time
✅ Reply to every comment

### Don'ts

❌ Post external links in first hour
❌ Use generic stock photos
❌ Write walls of text without breaks
❌ Ignore comments
❌ Over-promote products
❌ Use excessive hashtags (max 5)
❌ Post at random times
❌ Copy-paste from other platforms
❌ Use clickbait without substance
❌ Neglect visual formatting

## Integration Points

This skill integrates with:

- **content-creator**: Brand voice and SEO optimization
- **visual-designer**: Mockup and visual asset creation
- **linkedin-mcp-server**: Direct posting to LinkedIn
- **notebooklm-intelligence**: Content research and insights

## Troubleshooting

### LinkedIn MCP Issues

- **"LinkedIn not configured"**: Run `npm run setup` in `mcp-servers/linkedin`
- **"Token expired"**: Tokens last 60 days, re-run setup
- **Posts not appearing**: Check app has "Share on LinkedIn" product enabled

### Visual Generation Issues

- **Low quality images**: Ensure input images are 1080px+ width
- **Logo not appearing**: Check SVG path and permissions
- **Mockup errors**: Verify Sharp.js is installed (`npm install sharp`)

### Content Performance Issues

- **Low engagement**: Review first 2 lines hook, post at optimal times
- **No comments**: End with question, engage with early commenters
- **Low reach**: Avoid external links in first hour, use native content

## Quick Commands

```bash
# Setup LinkedIn posting
cd mcp-servers/linkedin && npm run setup

# Create content brief
node skills/linkedin-content-intelligence/scripts/generate_content_brief.js "AI in automotive"

# Generate LinkedIn visual
node skills/linkedin-content-intelligence/scripts/create_linkedin_visual.js "input.png" "output.png"

# Create carousel
node skills/linkedin-content-intelligence/scripts/create_carousel.js "brief.md"

# Analyze performance
node skills/linkedin-content-intelligence/scripts/analyze_post_performance.js "post_url"
```

## Related Skills

- `content-creator` - Brand voice and content frameworks
- `visual-designer` - Visual asset generation
- `notebooklm-intelligence` - Research and insights
- `brand-designer` - Brand identity and guidelines
