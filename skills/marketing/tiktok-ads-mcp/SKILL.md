---
name: tiktok-ads-mcp
description: >-
  Manages TikTok Advertising campaigns, viral content creation, influencer
  partnerships, and short-form video marketing through MCP integration
version: 1.0.0
dependencies:
  - python3
  - pip
  - node
  - npm
  - jq
  - curl
  - tiktok-api-python
inputs:
  - name: action
    description: >-
      The TikTok Ads operation to perform (create_campaign, get_insights,
      create_video_ad, etc.)
  - name: account_id
    description: TikTok Ads account ID
  - name: campaign_data
    description: JSON string containing campaign parameters
  - name: creative_data
    description: JSON string containing creative assets and specifications
  - name: audience_data
    description: JSON string containing audience targeting parameters
outputs:
  - type: file
    description: Campaign performance report in CSV format
  - type: stdout
    description: Operation status and results
  - type: file
    description: Video analytics and engagement metrics
compatibility: 'agent-zero, claude-code, cursor'
---

# TikTok Ads MCP Skill

## 🎯 Triggers
- User wants to create or manage TikTok Advertising campaigns
- User needs TikTok Ads performance analytics and reporting
- User wants to optimize TikTok video creatives for viral potential
- User needs to manage influencer partnerships and creator collaborations
- User wants to automate TikTok marketing and audience growth

## ⚡ Quick Start (Self-Check)
Before running TikTok Ads operations:
- [ ] Run `bash ~/.gemini/skills/tiktok-ads-mcp/test.sh`.
- [ ] Ensure `.env` contains `TIKTOK_ACCESS_TOKEN`, `TIKTOK_APP_ID`, `TIKTOK_SECRET`, and `TIKTOK_ADVERTISER_ID`.
- [ ] Install dependencies with `./install.sh`.

## 📋 Workflow
1. **Authentication Setup**: Configure TikTok Marketing API credentials in `.env`
2. **Campaign Creation**: Define campaign objectives (awareness, consideration, conversions)
3. **Ad Group Configuration**: Configure targeting, placements, and budgeting
4. **Creative Management**: Create video ads, carousels, and Spark Ads
5. **Content Optimization**: Analyze viral potential and optimize for TikTok algorithm
6. **Performance Monitoring**: Track views, engagement, conversions, and ROAS
7. **Influencer Integration**: Manage creator partnerships and branded content
8. **Trend Analysis**: Monitor TikTok trends and participate in challenges

## 🛠️ Script Reference
- Use `scripts/tiktok_ads_manager.py` for core campaign operations
- Use `scripts/tiktok_analytics.py` for performance reporting
- Use `scripts/tiktok_content_optimizer.py` for video content optimization
- Use `scripts/tiktok_influencer.py` for creator partnership management

## 🔧 API Integration
This skill integrates with TikTok Marketing API v3:
- Campaign Management
- Ad Creation and Management
- Creative Tools API for video processing
- TikTok Business Center API
- TikTok Creator Marketplace API
- TikTok Insights API for analytics
- TikTok Pixel API for conversion tracking

## 📊 Key Metrics
- Video Views and Completion Rate
- Engagement Rate (likes, comments, shares, follows)
- Click-Through Rate (CTR)
- Conversion Rate
- Cost per Result (CPR)
- Return on Ad Spend (ROAS)
- Sound Usage and Trend Participation
- Hashtag Performance
- Creator Performance Score

## 🎨 Creative Best Practices
- Short, engaging videos (15-60 seconds)
- Vertical format (9:16 aspect ratio)
- High-quality visuals and audio
- Clear call-to-action
- Trending sounds and hashtags
- Authentic, relatable content
- Text overlays and captions
- Interactive elements (polls, questions)

## 🎯 Targeting Options
- Demographic targeting (age, gender, location)
- Interest and behavior targeting
- Device and connection targeting
- Custom audiences (website visitors, app users)
- Lookalike audiences
- Keyword targeting
- Hashtag targeting
- Creator targeting

## 📈 Optimization Strategies
- Bid optimization for conversions
- Dayparting for optimal posting times
- Audience expansion
- Creative rotation and A/B testing
- Sound and trend optimization
- Influencer collaboration scaling
- UGC (User Generated Content) amplification
- Retargeting strategies

## 🎬 Content Creation Features
- Video template generation
- Text-to-speech and caption generation
- Trend analysis and prediction
- Hashtag research and optimization
- Sound selection and licensing
- Video editing and optimization
- Thumbnail generation
- Duet and Stitch creation

## 👥 Influencer Partnership Features
- Creator discovery and vetting
- Campaign brief creation
- Content approval workflow
- Performance tracking
- Payment and contract management
- Relationship management
- Brand safety monitoring
- Compliance verification

## 🔐 Security Notes
- Store API tokens securely in `.env`
- Implement proper rate limiting
- Monitor API usage and costs
- Regular token rotation
- Compliance with TikTok platform policies
- Data privacy compliance (GDPR, CCPA)

## 📚 Resources
- [TikTok Marketing API Documentation](https://ads.tiktok.com/marketing_api/docs)
- [TikTok Business Help Center](https://www.tiktok.com/business)
- [TikTok Creator Marketplace](https://creatormarketplace.tiktok.com/)
- [TikTok Creative Center](https://ads.tiktok.com/creativecenter/)
- [TikTok Trends](https://www.tiktok.com/tag/trending)

## License
MIT License
