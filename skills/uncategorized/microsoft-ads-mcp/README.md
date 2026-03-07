# Microsoft Ads MCP Skill

Automated Microsoft Advertising (Bing Ads) management and optimization through MCP integration.

## Features

- **Campaign Management**: Create, update, pause, and delete campaigns
- **Keyword Optimization**: Smart keyword research and bid management
- **Performance Reporting**: Detailed analytics and visualization
- **Competitor Analysis**: Monitor competitor strategies and positioning
- **Budget Optimization**: Automated bid adjustments and budget allocation
- **A/B Testing**: Test ad copy, landing pages, and targeting options

## Quick Start

1. **Install dependencies**:
   ```bash
   ./install.sh
   ```

2. **Configure credentials**:
   ```bash
   cp .env.template .env
   # Edit .env with your Microsoft Advertising API credentials
   ```

3. **Test setup**:
   ```bash
   ./test.sh
   ```

4. **Run optimization**:
   ```bash
   python scripts/microsoft_ads_optimizer.py --action analyze --campaign-id YOUR_CAMPAIGN_ID
   ```

## API Credentials

Get your Microsoft Advertising API credentials:
1. Register at [Microsoft Advertising Developer Portal](https://developers.ads.microsoft.com/)
2. Create an app to get Client ID and Client Secret
3. Generate Developer Token
4. Get Customer ID and Account ID from your Microsoft Advertising account

## Usage Examples

### Create a Campaign
```bash
python scripts/microsoft_ads_manager.py --action create_campaign \
  --name "B2B Software Campaign" \
  --budget 1000 \
  --output json
```

### Get Performance Report
```bash
python scripts/microsoft_ads_reporter.py \
  --campaign-id YOUR_CAMPAIGN_ID \
  --days 30 \
  --output-format html
```

### Optimize Keywords
```bash
python scripts/microsoft_ads_optimizer.py \
  --action apply \
  --campaign-id YOUR_CAMPAIGN_ID
```

### Competitor Analysis
```bash
node scripts/microsoft_ads_api.js \
  competitor-analysis \
  "enterprise software" "cloud solutions" "saas platform"
```

## Integration

This skill integrates with:
- **CRM Systems**: Salesforce, HubSpot, Dynamics 365
- **Analytics**: Google Analytics, Power BI, Tableau
- **Marketing Automation**: Marketo, Pardot, Eloqua
- **Reporting**: Excel, Google Sheets, Data Studio

## Best Practices for B2B Advertising

1. **Target Business Hours**: Focus on 9 AM - 5 PM in target timezones
2. **Use Exact Match**: Prioritize exact match keywords for high intent
3. **Leverage Ad Extensions**: Use sitelinks, callouts, and structured snippets
4. **Implement Remarketing**: Target previous visitors with specific offers
5. **Monitor Competitors**: Regularly analyze competitor ad positions and strategies

## Support

- [Microsoft Advertising API Documentation](https://docs.microsoft.com/en-us/advertising/)
- [Bing Ads SDK for Python](https://github.com/BingAds/BingAds-Python-SDK)
- [API Best Practices Guide](https://docs.microsoft.com/en-us/advertising/guides/)

## License

MIT License
