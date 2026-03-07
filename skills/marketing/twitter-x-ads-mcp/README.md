# Twitter/X Ads MCP Skill

Automated Twitter/X Advertising and real-time engagement management through Model Context Protocol integration.

## Features

- **Campaign Management**: Create, update, and manage Twitter/X campaigns
- **Promoted Tweet Creation**: Generate and optimize promoted tweets
- **Audience Targeting**: Configure detailed targeting options for Twitter/X
- **Performance Analytics**: Track impressions, engagements, conversions, and ROAS
- **Real-time Engagement**: Monitor mentions, replies, and conversations
- **Community Building**: Manage followers, lists, and Twitter Spaces
- **Sentiment Analysis**: Analyze conversation sentiment and brand perception
- **Crisis Management**: Monitor and respond to brand mentions in real-time

## Setup

1. **Get Twitter/X API Credentials**:
   - Apply for Twitter Developer access
   - Create a Twitter App with required permissions
   - Generate API keys and access tokens
   - Apply for Twitter Ads API access (separate application)
   - Note your Ads Account ID

2. **Configure Environment**:
   ```bash
   cp .env.template .env
   # Edit .env with your credentials
   ```

3. **Install Dependencies**:
   ```bash
   ./install.sh
   ```

4. **Test Setup**:
   ```bash
   ./test.sh
   ```

## Usage Examples

### Create Twitter/X Campaign
```bash
python3 scripts/twitter_ads_manager.py --action create_campaign \
  --name "Product Launch Campaign" \
  --objective "WEBSITE_CLICKS" \
  --daily-budget 50.0
```

### Get Campaign Analytics
```bash
python3 scripts/twitter_analytics.py \
  --start-date 2024-06-01 \
  --end-date 2024-06-30 \
  --format csv \
  --output june_report.csv
```

### Monitor Mentions in Real-time
```bash
python3 scripts/twitter_engagement.py \
  --action monitor \
  --keywords "yourbrand,productname" \
  --duration 10 \
  --output mentions.json
```

### Analyze Conversation Sentiment
```bash
python3 scripts/twitter_engagement.py \
  --action analyze_sentiment \
  --text "Love the new product features! Great work!" \
  --output sentiment.json
```

## API Reference

### Campaign Objectives
- AWARENESS: Increase brand awareness
- FOLLOWERS: Gain followers
- ENGAGEMENT: Increase tweet engagements
- WEBSITE_CLICKS: Drive traffic to website
- APP_INSTALLS: Drive app installs
- VIDEO_VIEWS: Increase video views
- LEAD_GENERATION: Generate leads
- CONVERSIONS: Drive conversions

### Ad Formats
- Promoted Tweets
- Promoted Accounts
- Promoted Trends
- In-Stream Video Ads
- Takeover Products
- Amplify Pre-roll

### Targeting Options
- Keywords
- Interests
- Followers
- Devices
- Locations
- Languages
- Behaviors
- Custom audiences
- Lookalike audiences

## Best Practices

1. **Content Strategy**:
   - Keep tweets concise and engaging
   - Use relevant hashtags and mentions
   - Include visual content (images, videos, GIFs)
   - Create tweet threads for longer content
   - Use polls and interactive content

2. **Engagement Strategy**:
   - Monitor mentions in real-time
   - Respond promptly to customer inquiries
   - Participate in relevant conversations
   - Use Twitter Spaces for live audio
   - Create Twitter Chats for community building

3. **Advertising Strategy**:
   - Start with small test budgets
   - A/B test different creatives
   - Use dayparting for optimal timing
   - Retarget website visitors
   - Use conversion tracking

4. **Community Management**:
   - Curate Twitter Lists
   - Engage with influencers
   - Monitor brand sentiment
   - Handle crises proactively
   - Foster community discussions

## Support

For issues and questions:
- Check Twitter Ads API documentation
- Review Twitter Developer Platform
- Test with small budgets first
- Monitor API rate limits and costs
