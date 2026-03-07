# Pinterest Ads MCP Skill

Automated Pinterest Advertising management through Model Context Protocol integration.

## Features

- **Campaign Management**: Create, update, and manage Pinterest campaigns
- **Ad Creation**: Generate and optimize Pinterest ads
- **Audience Targeting**: Configure detailed targeting options
- **Performance Analytics**: Track impressions, clicks, conversions, and ROI
- **Creative Optimization**: A/B test creatives and optimize based on performance
- **Budget Management**: Monitor and adjust campaign budgets
- **Reporting**: Generate detailed performance reports

## Setup

1. **Get Pinterest API Credentials**:
   - Create a Pinterest Business account
   - Generate access token from Pinterest Developer Portal
   - Note your Ad Account ID

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

### Create Campaign
```bash
python3 scripts/pinterest_ads_manager.py --action create_campaign \
  --name "Spring Collection Launch" \
  --objective "CONVERSIONS" \
  --budget 5000
```

### Get Analytics
```bash
python3 scripts/pinterest_ads_analytics.py \
  --start-date 2024-01-01 \
  --end-date 2024-01-31 \
  --format csv \
  --output campaign_report.csv
```

### Optimize Campaign
```bash
python3 scripts/pinterest_ads_optimizer.py \
  --campaign-id "1234567890" \
  --target-cpc 1.50
```

## API Reference

### Campaign Objectives
- AWARENESS: Brand awareness
- CONSIDERATION: Website traffic, video views, engagement
- CONVERSIONS: Conversions, catalog sales, lead generation

### Targeting Options
- Interests and keywords
- Demographics (age, gender, location)
- Device and placement
- Custom audiences
- Lookalike audiences

## Best Practices

1. **Creative Guidelines**:
   - Use vertical images (2:3 aspect ratio)
   - Include clear call-to-action
   - Maintain brand consistency
   - Optimize for mobile viewing

2. **Budget Strategy**:
   - Start with test budgets
   - Scale winning campaigns
   - Use dayparting for optimal timing

3. **Optimization Tips**:
   - Monitor performance daily
   - Adjust bids based on conversion data
   - Refresh creatives regularly
   - Expand successful audiences

## Support

For issues and questions:
- Check Pinterest API documentation
- Review skill logs
- Test with smaller budgets first
