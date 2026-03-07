# TikTok Ads MCP Skill

Automated TikTok Advertising and short-form video marketing management through Model Context Protocol integration.

## Features

- **Campaign Management**: Create, update, and manage TikTok campaigns
- **Video Ad Creation**: Generate and optimize TikTok video ads
- **Audience Targeting**: Configure detailed targeting options for TikTok
- **Performance Analytics**: Track views, engagement, conversions, and ROAS
- **Content Optimization**: Analyze viral potential and optimize for TikTok algorithm
- **Influencer Management**: Discover and manage creator partnerships
- **Trend Analysis**: Monitor TikTok trends and participate in challenges
- **Creative Tools**: Video editing, caption generation, and thumbnail creation

## Setup

1. **Get TikTok API Credentials**:
   - Apply for TikTok Developer access
   - Create a TikTok App with Marketing API permissions
   - Generate API keys and access tokens
   - Apply for TikTok Ads API access (business verification required)
   - Note your Advertiser ID

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

### Create TikTok Campaign
```bash
python3 scripts/tiktok_ads_manager.py --action create_campaign \
  --name "Summer Viral Campaign" \
  --objective "CONVERSIONS" \
  --budget-mode "BUDGET_MODE_DAY"
```

### Get Campaign Analytics
```bash
python3 scripts/tiktok_analytics.py \
  --start-date 2024-06-01 \
  --end-date 2024-06-30 \
  --format csv \
  --output june_report.csv
```

### Optimize Video Metadata
```bash
python3 scripts/tiktok_content_optimizer.py \
  --action optimize_metadata \
  --title "My Amazing TikTok Video" \
  --description "Check out this amazing content! #fyp #viral" \
  --tags "fyp,viral,comedy,dance" \
  --output optimization.json
```

### Get Trending Hashtags
```bash
python3 scripts/tiktok_content_optimizer.py \
  --action trending_hashtags \
  --category "comedy" \
  --limit 10 \
  --output trending.json
```

## API Reference

### Campaign Objectives
- AWARENESS: Increase brand awareness
- TRAFFIC: Drive traffic to website
- CONVERSIONS: Drive conversions
- APP_INSTALLS: Drive app installs
- VIDEO_VIEWS: Increase video views
- LEAD_GENERATION: Generate leads
- COMMUNITY_INTERACTION: Increase community interaction
- PROFILE_VISITS: Drive profile visits

### Ad Formats
- In-Feed Ads
- TopView Ads
- Brand Takeover
- Branded Hashtag Challenge
- Branded Effects
- Spark Ads (organic content amplification)
- Collection Ads
- Dynamic Showcase Ads

### Targeting Options
- Demographic targeting (age, gender, location)
- Interest and behavior targeting
- Device and connection targeting
- Custom audiences (website visitors, app users)
- Lookalike audiences
- Keyword targeting
- Hashtag targeting
- Creator targeting
- Video targeting

## Best Practices

1. **Content Strategy**:
   - Keep videos short and engaging (15-60 seconds)
   - Use vertical format (9:16 aspect ratio)
   - Include trending sounds and hashtags
   - Add text overlays and captions
   - Create authentic, relatable content
   - Use interactive elements (polls, questions)

2. **Advertising Strategy**:
   - Start with Spark Ads for organic amplification
   - Use In-Feed Ads for maximum reach
   - Test different video lengths and formats
   - Optimize for sound-on experience
   - Use dayparting for optimal posting times
   - Retarget engaged users

3. **Influencer Strategy**:
   - Partner with micro-influencers (10K-100K followers)
   - Use Creator Marketplace for discovery
   - Create clear campaign briefs
   - Allow creative freedom
   - Track performance with unique codes
   - Build long-term relationships

4. **Trend Strategy**:
   - Monitor TikTok Trends page daily
   - Participate in relevant challenges
   - Create original sounds
   - Use trending hashtags strategically
   - Jump on trends early
   - Put unique spin on popular trends

## Support

For issues and questions:
- Check TikTok Marketing API documentation
- Review TikTok Business Help Center
- Test with small budgets first
- Monitor API rate limits and costs
- Join TikTok Creator Community
