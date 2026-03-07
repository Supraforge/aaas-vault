---
name: twitter-x-ads-mcp
description: >-
  Manages Twitter/X Advertising campaigns, real-time engagement, community
  building, and brand conversations through MCP integration
version: 1.0.0
dependencies:
  - python3
  - pip
  - node
  - npm
  - jq
  - curl
  - tweepy
inputs:
  - name: action
    description: >-
      The Twitter/X Ads operation to perform (create_campaign, get_analytics,
      create_promoted_tweet, etc.)
  - name: account_id
    description: Twitter/X Ads account ID
  - name: campaign_data
    description: JSON string containing campaign parameters
  - name: tweet_data
    description: JSON string containing tweet content and specifications
  - name: audience_data
    description: JSON string containing audience targeting parameters
outputs:
  - type: file
    description: Campaign performance report in CSV format
  - type: stdout
    description: Operation status and results
  - type: file
    description: Engagement analytics and conversation metrics
compatibility: 'agent-zero, claude-code, cursor'
---

# Twitter/X Ads MCP Skill

## 🎯 Triggers
- User wants to create or manage Twitter/X Advertising campaigns
- User needs Twitter/X Ads performance analytics and reporting
- User wants to optimize promoted tweets and real-time engagement
- User needs to manage brand conversations and community building
- User wants to automate Twitter/X marketing and audience growth

## ⚡ Quick Start (Self-Check)
Before running Twitter/X Ads operations:
- [ ] Run `bash ~/.gemini/skills/twitter-x-ads-mcp/test.sh`.
- [ ] Ensure `.env` contains `TWITTER_API_KEY`, `TWITTER_API_SECRET`, `TWITTER_ACCESS_TOKEN`, `TWITTER_ACCESS_SECRET`, and `TWITTER_ADS_ACCOUNT_ID`.
- [ ] Install dependencies with `./install.sh`.

## 📋 Workflow
1. **Authentication Setup**: Configure Twitter/X API credentials in `.env`
2. **Campaign Creation**: Define campaign objectives (awareness, consideration, conversions)
3. **Ad Group Configuration**: Configure targeting, placements, and budgeting
4. **Creative Management**: Create promoted tweets, trends, and accounts
5. **Real-time Engagement**: Monitor mentions, replies, and conversations
6. **Performance Monitoring**: Track impressions, engagements, conversions, and ROAS
7. **Community Building**: Manage followers, lists, and Twitter Spaces
8. **Analytics Reporting**: Generate performance insights and optimization recommendations

## 🛠️ Script Reference
- Use `scripts/twitter_ads_manager.py` for core campaign operations
- Use `scripts/twitter_analytics.py` for performance reporting
- Use `scripts/twitter_engagement.py` for real-time conversation management
- Use `scripts/twitter_community.py` for audience growth and community building

## 🔧 API Integration
This skill integrates with Twitter Ads API v12 and Twitter API v2:
- Campaign Management
- Promoted Tweet Creation
- Audience Targeting
- Conversion Tracking
- Analytics and Reporting
- Real-time Engagement
- Community Management
- Twitter Spaces Integration

## 📊 Key Metrics
- Impressions and Reach
- Engagement Rate (likes, retweets, replies, clicks)
- Click-Through Rate (CTR)
- Conversion Rate
- Cost per Engagement (CPE)
- Return on Ad Spend (ROAS)
- Follower Growth
- Conversation Sentiment
- Hashtag Performance

## 🎨 Creative Best Practices
- Concise, compelling copy (280 characters)
- Relevant hashtags and mentions
- Visual content (images, GIFs, videos)
- Clear call-to-action
- Thread optimization for longer content
- Polls and interactive content
- Twitter Cards for rich media

## 🎯 Targeting Options
- Keyword targeting
- Interest targeting
- Follower targeting
- Device targeting
- Location targeting
- Language targeting
- Behavior targeting
- Custom audiences (website visitors, email lists)
- Lookalike audiences

## 📈 Optimization Strategies
- Bid optimization for engagements
- Dayparting for optimal timing
- Audience expansion
- Creative rotation
- Hashtag optimization
- Conversation monitoring
- Competitor analysis
- Trend jacking

## 💬 Real-time Engagement Features
- Mention monitoring and response
- Conversation tracking
- Sentiment analysis
- Crisis management
- Customer support automation
- Influencer engagement
- Trend participation
- Twitter Spaces management

## 👥 Community Building Features
- Follower growth strategies
- List management
- Twitter Chat organization
- Community moderation
- Content curation
- Cross-promotion
- Partnership development
- Event promotion

## 🔐 Security Notes
- Store API tokens securely in `.env`
- Implement proper rate limiting
- Monitor API usage and costs
- Regular token rotation
- Compliance with Twitter/X platform policies

## 📚 Resources
- [Twitter Ads API Documentation](https://developer.twitter.com/en/docs/twitter-ads-api)
- [Twitter API v2 Documentation](https://developer.twitter.com/en/docs/twitter-api)
- [Twitter Business Help Center](https://business.twitter.com/)
- [Twitter Ads Best Practices](https://business.twitter.com/en/advertising/ads-best-practices.html)

## License
MIT License
