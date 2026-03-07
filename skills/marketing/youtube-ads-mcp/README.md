# YouTube Ads MCP Skill

Automated YouTube Advertising and video marketing management through Model Context Protocol integration.

## Features

- **Campaign Management**: Create, update, and manage YouTube campaigns
- **Video Ad Creation**: Generate and optimize YouTube video ads
- **Audience Targeting**: Configure detailed targeting options for YouTube
- **Performance Analytics**: Track views, watch time, engagement, and conversions
- **Content Optimization**: Optimize videos for YouTube search and recommendations
- **Channel Management**: Manage YouTube channel settings and branding
- **Audience Development**: Grow subscribers and build community
- **Trend Analysis**: Monitor YouTube trends and optimize content strategy

## Setup

1. **Get Google API Credentials**:
   - Create a Google Cloud Project
   - Enable YouTube Data API v3 and Google Ads API
   - Create OAuth 2.0 credentials
   - Generate API keys and access tokens
   - Set up Google Ads API access
   - Note your Google Ads Account ID

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

### Create YouTube Campaign
```bash
python3 scripts/youtube_ads_manager.py --action create_campaign \
  --name "Product Launch Video Campaign" \
  --campaign-type "VIDEO_ACTION" \
  --budget-amount 500.0
```

### Get Campaign Analytics
```bash
python3 scripts/youtube_ads_manager.py --action get_insights \
  --start-date 2024-06-01 \
  --end-date 2024-06-30 \
  --output june_insights.json
```

### Analyze Channel Performance
```bash
python3 scripts/youtube_analytics.py --action channel_analytics \
  --channel-id YOUR_CHANNEL_ID \
  --output channel_stats.json
```

### Optimize Video Metadata
```bash
python3 scripts/youtube_content_optimizer.py --action analyze_metadata \
  --title "How to Optimize YouTube Videos for SEO" \
  --description "Learn the best practices for YouTube SEO in this comprehensive tutorial..." \
  --tags "youtube,seo,optimization,tutorial,marketing" \
  --category-id "27" \
  --output optimization.json
```

### Get Trending Keywords
```bash
python3 scripts/youtube_content_optimizer.py --action trending_keywords \
  --region-code "US" \
  --max-results 15 \
  --output trending.json
```

## API Reference

### Campaign Types
- VIDEO_ACTION: Drive actions like website visits or conversions
- VIDEO_NON_SKIPPABLE_IN_STREAM: Non-skippable in-stream ads
- VIDEO_TRUE_VIEW_IN_STREAM: TrueView in-stream ads
- VIDEO_TRUE_VIEW_IN_DISPLAY: TrueView in-display ads
- VIDEO_BUMPER: Short, non-skippable bumper ads

### Ad Formats
- In-stream ads (skippable and non-skippable)
- Video discovery ads (in-search and in-display)
- Bumper ads (6-second non-skippable)
- Outstream ads (mobile-only)
- Masthead ads (homepage takeover)

### Targeting Options
- Demographic targeting (age, gender, parental status)
- Interest and affinity audiences
- Custom intent audiences
- Remarketing audiences
- Life events targeting
- In-market audiences
- Topic and keyword targeting
- Placement targeting (specific channels/videos)
- Device and connection targeting

## Best Practices

1. **Content Strategy**:
   - Create compelling thumbnails and titles
   - Structure videos with clear chapters
   - Ensure high-quality audio and visuals
   - Hook viewers in first 15 seconds
   - Include clear calls-to-action
   - Add end screens and cards
   - Provide subtitles and closed captions
   - Organize content into playlists

2. **Advertising Strategy**:
   - Start with TrueView for maximum reach
   - Use bumper ads for brand awareness
   - Test different video lengths and formats
   - Optimize for mobile viewing
   - Use dayparting for optimal posting times
   - Retarget engaged viewers
   - A/B test different creatives

3. **Channel Strategy**:
   - Maintain consistent branding
   - Create compelling channel trailer
   - Organize videos into playlists
   - Engage with community in comments
   - Use Community tab for updates
   - Collaborate with other creators
   - Analyze analytics regularly
   - Respond to audience feedback

4. **SEO Strategy**:
   - Research trending keywords
   - Optimize titles and descriptions
   - Use relevant tags strategically
   - Create compelling thumbnails
   - Add chapters with timestamps
   - Transcribe videos for search
   - Build backlinks to videos
   - Promote across social media

## Support

For issues and questions:
- Check YouTube Data API documentation
- Review Google Ads API documentation
- Test with small budgets first
- Monitor API usage and quotas
- Join YouTube Creator Community
- Follow YouTube Creator Academy
