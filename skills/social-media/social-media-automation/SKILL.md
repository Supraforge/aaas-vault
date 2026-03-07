---
name: social-media-automation
description: >-
  Automates social media management across multiple platforms with AI-powered
  content creation, scheduling, and analytics
version: 1.0.0
dependencies:
  - python3
  - pip
  - jq
  - curl
inputs:
  - name: platforms
    description: >-
      List of social media platforms to manage (twitter, linkedin, facebook,
      instagram, tiktok)
  - name: content_strategy
    description: >-
      Content strategy file or JSON defining posting themes, frequency, and
      goals
  - name: schedule_config
    description: 'Scheduling configuration (timezone, optimal posting times, frequency)'
outputs:
  - type: file
    description: Social media calendar CSV/JSON for the next 30 days
  - type: file
    description: Content library with generated posts and media
  - type: file
    description: Analytics report with engagement metrics and recommendations
compatibility: 'agent-zero, claude-code, cursor'
---

# Social Media Automation

## 🎯 Triggers
- "Schedule social media posts for next week"
- "Generate content ideas for our product launch"
- "Analyze social media performance and suggest improvements"
- "Automate posting across all our social channels"

## ⚡ Quick Start (Self-Check)
Before running automation, verify readiness:
- [ ] Run `bash ~/.gemini/skills/social-media-automation/test.sh`.
- [ ] Check `.env` contains required API keys for selected platforms.
- [ ] Ensure content strategy file exists or create one using templates.

## 📋 Workflow
1. **Platform Setup**: Configure API access for each social media platform
2. **Content Generation**: Use AI to create posts, images, and videos based on strategy
3. **Scheduling Optimization**: Determine best posting times based on audience analytics
4. **Automated Posting**: Schedule and publish content across all platforms
5. **Performance Monitoring**: Track engagement and adjust strategy
6. **Reporting**: Generate weekly/monthly analytics reports

## 🛠️ Script Reference
- Use `scripts/social_scheduler.py` for scheduling and posting
- Use `scripts/content_generator.py` for AI-powered content creation
- Use `scripts/analytics_dashboard.py` for performance tracking
- Use `scripts/platform_integration.py` for API connections

## 📊 Supported Platforms

### Tier 1 (Full Automation)
- **Twitter/X**: Posting, threading, media uploads, analytics
- **LinkedIn**: Company pages, personal profiles, articles
- **Facebook**: Pages, groups, stories, reels
- **Instagram**: Posts, stories, reels, carousels

### Tier 2 (Scheduled Posting)
- **TikTok**: Video uploads with captions and hashtags
- **Pinterest**: Pins, boards, rich pins
- **YouTube**: Video descriptions, community posts
- **Reddit**: Subreddit posts (with rate limiting)

### Tier 3 (Analytics Only)
- **Threads**: Analytics and monitoring
- **Bluesky**: Analytics and monitoring
- **Mastodon**: Analytics and monitoring

## 🤖 AI Content Generation

The system uses multiple AI models for different content types:

### Text Generation
- **Short-form**: Tweets, captions, comments (GPT-4, Claude)
- **Long-form**: Articles, blog posts, LinkedIn posts
- **Hashtag Research**: Trending and relevant hashtags

### Visual Content
- **Image Generation**: DALL-E 3, Midjourney, Stable Diffusion
- **Video Creation**: Short clips, animations, text-to-video
- **Design Templates**: Canva integration for branded content

## ⏰ Smart Scheduling

### Optimal Posting Times
- Calculates based on:
  - Platform-specific peak hours
  - Audience timezone analysis
  - Historical engagement data
  - Competitor posting patterns

### Content Calendar
- 30-day rolling calendar
- Theme-based content planning
- Holiday and event integration
- Campaign tracking

## 📈 Analytics & Optimization

### Key Metrics
- Engagement rate (likes, comments, shares)
- Reach and impressions
- Follower growth
- Click-through rate
- Conversion tracking

### AI Recommendations
- Content type optimization
- Posting time adjustments
- Hashtag effectiveness
- Audience targeting improvements

## 🔐 Security & Compliance

### Data Protection
- API keys encrypted at rest
- No personal data storage
- GDPR/CCPA compliant data handling

### Platform Compliance
- Respects rate limits
- Follows platform TOS
- Proper disclosure for AI-generated content
- Copyright compliance for media

## 🚀 Advanced Features

### 1. Competitor Analysis
- Monitor competitor social activity
- Benchmark performance
- Identify content gaps

### 2. Sentiment Analysis
- Brand sentiment tracking
- Crisis detection and alerts
- Customer feedback analysis

### 3. Influencer Collaboration
- Identify relevant influencers
- Outreach automation
- Campaign tracking

### 4. Social Listening
- Brand mentions monitoring
- Industry trend detection
- Customer service integration

## 📁 File Structure

```
social-media-automation/
├── scripts/
│   ├── social_scheduler.py     # Main scheduling logic
│   ├── content_generator.py    # AI content creation
│   ├── analytics_dashboard.py  # Performance tracking
│   ├── platform_integration.py # API connections
│   └── utils.py               # Helper functions
├── templates/
│   ├── content_strategy.json   # Strategy template
│   ├── posting_schedule.json   # Schedule template
│   ├── brand_voice.md         # Brand guidelines
│   └── hashtag_libraries.json  # Categorized hashtags
├── config/
│   ├── platform_configs/      # Platform-specific settings
│   └── ai_models.json         # AI model configurations
└── data/
    ├── content_library/       # Generated content
    ├── analytics/            # Performance data
    └── exports/              # Report exports
```

## 🔧 Configuration

### Environment Variables
See `.env.template` for all required API keys:
- Social platform API keys (Twitter, LinkedIn, Facebook, etc.)
- AI service keys (OpenAI, Anthropic, etc.)
- Analytics services (Google Analytics, etc.)

### Content Strategy
Define your strategy in JSON format:
```json
{
  "brand_voice": "professional yet approachable",
  "target_audience": "tech professionals, ages 25-45",
  "content_themes": ["industry insights", "product updates", "team culture"],
  "posting_frequency": {
    "twitter": "3/day",
    "linkedin": "1/day",
    "instagram": "1/day"
  },
  "campaigns": [
    {
      "name": "Product Launch",
      "duration": "2 weeks",
      "themes": ["announcement", "features", "testimonials"]
    }
  ]
}
```

## 🧪 Testing

Run the test suite:
```bash
cd ~/.gemini/skills/social-media-automation
bash test.sh
```

Tests verify:
- API connectivity
- Content generation
- Scheduling logic
- File permissions
- Dependency availability

## 🚨 Troubleshooting

### Common Issues
1. **API Rate Limits**: Implement exponential backoff
2. **Content Rejection**: Review platform guidelines
3. **Authentication Errors**: Refresh tokens regularly
4. **Analytics Discrepancies**: Platform API limitations

### Support
- Check logs in `logs/` directory
- Review platform status pages
- Consult API documentation

## 📚 Resources

### Documentation
- Platform API docs (Twitter, LinkedIn, Facebook, etc.)
- AI model documentation (OpenAI, Anthropic, etc.)
- Social media best practices guides

### Learning
- Social media marketing courses
- Content strategy frameworks
- Analytics interpretation guides

---

*Last updated: 2025-01-20*
*Version: 1.0.0*
