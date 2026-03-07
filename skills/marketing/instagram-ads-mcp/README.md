# Instagram Ads MCP Skill

Automated Instagram Advertising and social commerce management through Model Context Protocol integration.

## Features

- **Campaign Management**: Create, update, and manage Instagram campaigns
- **Ad Creation**: Generate and optimize Instagram ads (feed, stories, reels, explore)
- **Audience Targeting**: Configure detailed targeting options for Instagram
- **Performance Analytics**: Track reach, engagement, conversions, and ROAS
- **Creative Optimization**: A/B test creatives and optimize visual content
- **Influencer Partnerships**: Manage sponsored content and influencer campaigns
- **Shopping Automation**: Sync product catalogs and enable Instagram shopping
- **Content Management**: Schedule and publish Instagram content

## Setup

1. **Get Facebook/Instagram API Credentials**:
   - Create a Facebook Developer account
   - Create a Facebook App with Marketing API access
   - Generate access token with required permissions
   - Connect Instagram Business account to Facebook Page
   - Note your Ad Account ID and Instagram Business Account ID

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

### Create Instagram Campaign
```bash
python3 scripts/instagram_ads_manager.py --action create_campaign \
  --name "Summer Sale Campaign" \
  --objective "OUTCOME_TRAFFIC"
```

### Get Campaign Insights
```bash
python3 scripts/instagram_insights.py \
  --start-date 2024-06-01 \
  --end-date 2024-06-30 \
  --format csv \
  --output june_report.csv
```

### Optimize Creative
```bash
python3 scripts/instagram_creative_optimizer.py \
  --creative-data '{"image_url": "https://example.com/image.jpg"}' \
  --output recommendations.json
```

### Manage Instagram Shopping
```bash
python3 scripts/instagram_shopping.py \
  --action get_catalog \
  --output products.json
```

## API Reference

### Campaign Objectives
- BRAND_AWARENESS: Increase brand awareness
- REACH: Maximize reach
- TRAFFIC: Drive traffic to website
- ENGAGEMENT: Increase post engagement
- APP_INSTALLS: Drive app installs
- VIDEO_VIEWS: Increase video views
- LEAD_GENERATION: Generate leads
- CONVERSIONS: Drive conversions
- PRODUCT_CATALOG_SALES: Drive catalog sales
- STORE_VISITS: Drive store visits

### Ad Formats
- Image ads
- Video ads
- Carousel ads
- Collection ads
- Stories ads
- Reels ads
- Explore ads
- Shopping ads

### Placement Options
- Instagram feed
- Instagram stories
- Instagram explore
- Instagram reels
- Instagram shopping

## Best Practices

1. **Creative Guidelines**:
   - Use high-quality, visually appealing content
   - Optimize for mobile viewing
   - Include clear call-to-action
   - Test different formats (stories, reels, feed)
   - Use user-generated content when possible

2. **Audience Strategy**:
   - Start with broad targeting, then refine
   - Use lookalike audiences based on best customers
   - Create custom audiences from website visitors
   - Test interest-based vs. behavior-based targeting

3. **Budget Optimization**:
   - Start with test budgets ($5-20/day)
   - Use automatic placements initially
   - Implement dayparting for optimal timing
   - Scale winning campaigns gradually

4. **Shopping Best Practices**:
   - Use high-quality product images
   - Include clear pricing and descriptions
   - Enable checkout on Instagram
   - Use collection ads for product groups
   - Retarget abandoned carts

## Support

For issues and questions:
- Check Facebook Marketing API documentation
- Review Instagram Business Help Center
- Test with small budgets first
- Monitor API rate limits and costs
