---
name: instagram-ads-mcp
description: >-
  Manages Instagram Advertising campaigns, influencer partnerships, visual
  content optimization, and social commerce through MCP integration
version: 1.0.0
dependencies:
  - python3
  - pip
  - node
  - npm
  - jq
  - curl
  - graphql
inputs:
  - name: action
    description: >-
      The Instagram Ads operation to perform (create_campaign, get_insights,
      create_ad, etc.)
  - name: account_id
    description: Facebook/Instagram Ads account ID
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
    description: Creative assets and media files
compatibility: 'agent-zero, claude-code, cursor'
---

# Instagram Ads MCP Skill

## 🎯 Triggers
- User wants to create or manage Instagram Advertising campaigns
- User needs Instagram Ads performance analytics and reporting
- User wants to optimize Instagram ad creatives and visual content
- User needs to manage influencer partnerships and sponsored content
- User wants to automate Instagram shopping and social commerce

## ⚡ Quick Start (Self-Check)
Before running Instagram Ads operations:
- [ ] Run `bash ~/.gemini/skills/instagram-ads-mcp/test.sh`.
- [ ] Ensure `.env` contains `FACEBOOK_ACCESS_TOKEN`, `FACEBOOK_AD_ACCOUNT_ID`, and `INSTAGRAM_BUSINESS_ACCOUNT_ID`.
- [ ] Install dependencies with `./install.sh`.

## 📋 Workflow
1. **Authentication Setup**: Configure Facebook Marketing API credentials in `.env`
2. **Account Linking**: Connect Instagram Business account to Facebook Ads account
3. **Campaign Creation**: Define campaign objectives (awareness, consideration, conversions)
4. **Ad Set Configuration**: Configure targeting, placements, and budgeting
5. **Creative Management**: Create carousels, stories, reels, and feed ads
6. **Performance Monitoring**: Track reach, engagement, conversions, and ROAS
7. **Influencer Integration**: Manage sponsored content and influencer partnerships
8. **Shopping Automation**: Sync product catalogs and enable Instagram shopping

## 🛠️ Script Reference
- Use `scripts/instagram_ads_manager.py` for core campaign operations
- Use `scripts/instagram_insights.py` for performance reporting
- Use `scripts/instagram_creative_optimizer.py` for visual content optimization
- Use `scripts/instagram_shopping.py` for social commerce automation

## 🔧 API Integration
This skill integrates with Facebook Marketing API (Graph API v18+):
- Campaign Management
- Ad Creation and Management
- Instagram Graph API for business accounts
- Instagram Basic Display API for content
- Instagram Shopping API for e-commerce
- Instagram Insights API for analytics

## 📊 Key Metrics
- Reach and Impressions
- Engagement Rate (likes, comments, shares)
- Click-Through Rate (CTR)
- Conversion Rate
- Cost per Result (CPR)
- Return on Ad Spend (ROAS)
- Story Completions and Swipe-ups
- Reels Views and Engagement

## 🎨 Creative Best Practices
- Square (1:1) and vertical (4:5) formats
- High-quality visual content
- Clear call-to-action buttons
- Instagram Stories and Reels optimization
- Carousel ads for multiple products
- User-generated content integration

## 🎯 Targeting Options
- Demographic targeting (age, gender, location)
- Interest-based targeting
- Behavior targeting
- Custom audiences (website visitors, email lists)
- Lookalike audiences
- Engagement audiences
- Placement optimization (feed, stories, explore, reels)

## 📈 Optimization Strategies
- Automatic placements optimization
- Bid strategies for conversions
- Dynamic creative optimization
- Audience expansion
- Dayparting and scheduling
- Budget pacing
- Creative fatigue management

## 👥 Influencer Partnership Features
- Influencer discovery and vetting
- Campaign brief creation
- Content approval workflows
- Performance tracking for sponsored posts
- Payment and compliance management
- Relationship management

## 🛍️ Social Commerce Features
- Product catalog synchronization
- Shopping tag automation
- Checkout optimization
- Abandoned cart recovery
- Product launch campaigns
- Collection ads

## 🔐 Security Notes
- Store API tokens securely in `.env`
- Implement proper rate limiting
- Monitor API usage and costs
- Regular token rotation
- Compliance with Instagram platform policies

## 📚 Resources
- [Facebook Marketing API Documentation](https://developers.facebook.com/docs/marketing-apis/)
- [Instagram Graph API Documentation](https://developers.facebook.com/docs/instagram-api/)
- [Instagram Business Help Center](https://business.instagram.com/)
- [Instagram Ads Best Practices](https://www.facebook.com/business/ads-guide/instagram/)

## License
MIT License
