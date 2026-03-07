---
name: youtube-ads-mcp
description: >-
  Manages YouTube Advertising campaigns, video content optimization, channel
  growth, and audience engagement through MCP integration
version: 1.0.0
dependencies:
  - python3
  - pip
  - node
  - npm
  - jq
  - curl
  - google-api-python-client
  - oauth2client
inputs:
  - name: action
    description: >-
      The YouTube Ads operation to perform (create_campaign, get_analytics,
      upload_video, etc.)
  - name: account_id
    description: Google Ads account ID
  - name: campaign_data
    description: JSON string containing campaign parameters
  - name: video_data
    description: JSON string containing video metadata and specifications
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

# YouTube Ads MCP Skill

## 🎯 Triggers
- User wants to create or manage YouTube Advertising campaigns
- User needs YouTube Ads performance analytics and reporting
- User wants to optimize YouTube video content for search and engagement
- User needs to manage YouTube channel growth and audience development
- User wants to automate YouTube marketing and video content strategy

## ⚡ Quick Start (Self-Check)
Before running YouTube Ads operations:
- [ ] Run `bash ~/.gemini/skills/youtube-ads-mcp/test.sh`.
- [ ] Ensure `.env` contains `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `GOOGLE_REFRESH_TOKEN`, and `GOOGLE_ADS_ACCOUNT_ID`.
- [ ] Install dependencies with `./install.sh`.

## 📋 Workflow
1. **Authentication Setup**: Configure Google API credentials in `.env`
2. **Campaign Creation**: Define campaign objectives (awareness, consideration, conversions)
3. **Ad Group Configuration**: Configure targeting, placements, and budgeting
4. **Video Management**: Upload, optimize, and manage YouTube video content
5. **Content Optimization**: Optimize videos for YouTube search and recommendations
6. **Performance Monitoring**: Track views, watch time, engagement, and conversions
7. **Channel Management**: Manage YouTube channel settings and branding
8. **Audience Development**: Grow subscribers and build community

## 🛠️ Script Reference
- Use `scripts/youtube_ads_manager.py` for core campaign operations
- Use `scripts/youtube_analytics.py` for performance reporting
- Use `scripts/youtube_content_optimizer.py` for video content optimization
- Use `scripts/youtube_channel_manager.py` for channel management

## 🔧 API Integration
This skill integrates with multiple Google APIs:
- Google Ads API (campaign management)
- YouTube Data API v3 (video and channel management)
- YouTube Analytics API (performance reporting)
- YouTube Reporting API (detailed analytics)
- Google OAuth2 (authentication)

## 📊 Key Metrics
- Views and Watch Time
- Average View Duration
- Click-Through Rate (CTR)
- Engagement Rate (likes, comments, shares)
- Subscriber Growth
- Audience Retention
- Impressions and Impression Share
- Cost per View (CPV)
- Return on Ad Spend (ROAS)
- Video SEO Performance

## 🎨 Creative Best Practices
- Compelling thumbnails and titles
- Clear video structure with chapters
- High-quality audio and visuals
- Engaging introductions (first 15 seconds)
- Clear call-to-action
- End screens and cards
- Subtitles and closed captions
- Playlist organization

## 🎯 Targeting Options
- Demographic targeting (age, gender, location)
- Interest and affinity audiences
- Custom intent audiences
- Remarketing audiences
- Life events targeting
- In-market audiences
- Topic and keyword targeting
- Placement targeting (specific channels/videos)
- Device and connection targeting

## 📈 Optimization Strategies
- Bid optimization for conversions
- Dayparting for optimal posting times
- Audience expansion
- Creative rotation and A/B testing
- Video SEO optimization
- Playlist optimization
- Channel trailer optimization
- Community tab engagement

## 🎬 Content Creation Features
- Video upload and management
- Thumbnail generation
- Title and description optimization
- Tag research and optimization
- Chapter marker creation
- End screen and card creation
- Playlist creation and management
- Community post creation

## 👥 Channel Management Features
- Channel branding updates
- About section optimization
- Channel trailer setup
- Featured sections management
- Playlist organization
- Video organization
- Analytics dashboard
- Monetization management

## 🔐 Security Notes
- Store API tokens securely in `.env`
- Implement proper OAuth2 flow
- Monitor API usage and quotas
- Regular token refresh
- Compliance with YouTube policies
- Copyright and content guidelines
- Data privacy compliance (GDPR, CCPA)

## 📚 Resources
- [YouTube Data API Documentation](https://developers.google.com/youtube/v3)
- [Google Ads API Documentation](https://developers.google.com/google-ads/api)
- [YouTube Analytics API Documentation](https://developers.google.com/youtube/analytics)
- [YouTube Creator Academy](https://creatoracademy.youtube.com/)
- [YouTube Studio](https://studio.youtube.com/)

## License
MIT License
