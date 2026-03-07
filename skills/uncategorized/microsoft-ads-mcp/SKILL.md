---
name: microsoft-ads-mcp
description: >-
  Automates Microsoft Advertising (Bing Ads) management, campaign optimization,
  keyword research, and performance reporting through MCP integration
version: 1.0.0
dependencies:
  - python3
  - pip
  - node
  - npm
  - jq
  - curl
inputs:
  - name: action
    description: 'Action to perform (create_campaign, get_reports, optimize_keywords, etc.)'
  - name: config_file
    description: Path to configuration JSON file (optional)
  - name: output_format
    description: 'Output format (json, csv, html)'
outputs:
  - type: file
    description: Campaign performance report or optimization recommendations
  - type: stdout
    description: Status messages and operation results
compatibility: 'agent-zero, claude-code, cursor'
---

# Microsoft Ads MCP

## 🎯 Triggers
- "Create Microsoft Ads campaign for B2B lead generation"
- "Get Microsoft Ads performance report for last 30 days"
- "Optimize Microsoft Ads keywords for better ROI"
- "Analyze Microsoft Ads competitor performance"
- "Set up Microsoft Ads budget alerts"

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/microsoft-ads-mcp/test.sh`.
- [ ] Check `.env` contains required Microsoft Advertising API credentials.
- [ ] Run `./install.sh` to install Python and Node.js dependencies.

## 📋 Workflow
1. **Authentication**: Connect to Microsoft Advertising API using OAuth 2.0
2. **Campaign Management**: Create, update, pause, or delete campaigns
3. **Keyword Research**: Analyze search volume and competition data
4. **Performance Reporting**: Generate detailed reports on clicks, impressions, conversions
5. **Budget Optimization**: Adjust bids and budgets based on performance
6. **Competitor Analysis**: Monitor competitor ad positions and strategies

## 🛠️ Script Reference
- Use `scripts/microsoft_ads_manager.py` for Python-based campaign management
- Use `scripts/microsoft_ads_api.js` for Node.js API interactions
- Use `scripts/microsoft_ads_reporter.py` for performance reporting
- Use `scripts/microsoft_ads_optimizer.py` for bid and keyword optimization

## 🔧 Configuration
### Environment Variables (.env)
```bash
MICROSOFT_ADS_CLIENT_ID=your_client_id
MICROSOFT_ADS_CLIENT_SECRET=your_client_secret
MICROSOFT_ADS_REFRESH_TOKEN=your_refresh_token
MICROSOFT_ADS_DEVELOPER_TOKEN=your_developer_token
MICROSOFT_ADS_CUSTOMER_ID=your_customer_id
MICROSOFT_ADS_ACCOUNT_ID=your_account_id
```

### API Endpoints
- **Campaign Management**: Create, update, delete campaigns
- **Reporting**: Get performance metrics and analytics
- **Keyword Suggestions**: Get keyword ideas and search volume
- **Bid Management**: Adjust bids for optimal performance

## 📊 Example Usage
```bash
# Create a new search campaign
python scripts/microsoft_ads_manager.py --action create_campaign --name "B2B Software Campaign" --budget 1000

# Get performance report
python scripts/microsoft_ads_reporter.py --report-type performance --days 30 --output-format csv

# Optimize keywords
python scripts/microsoft_ads_optimizer.py --action optimize --campaign-id 12345 --max-cpc 5.00

# Analyze competitors
node scripts/microsoft_ads_api.js --action competitor_analysis --keywords "cloud software,saas"
```

## 🔍 Monitoring & Alerts
- **Budget Alerts**: Get notified when campaigns approach budget limits
- **Performance Alerts**: Monitor CTR, conversion rate, and ROI thresholds
- **Competitor Alerts**: Track competitor ad position changes

## 📈 Best Practices
1. **B2B Focus**: Target business hours and professional demographics
2. **Keyword Strategy**: Use exact match for high-intent B2B keywords
3. **Ad Extensions**: Utilize sitelinks, callouts, and structured snippets
4. **A/B Testing**: Continuously test ad copy and landing pages
5. **Remarketing**: Implement audience targeting for previous visitors

## 🔗 Integration Points
- **CRM Integration**: Sync leads with Salesforce, HubSpot
- **Analytics Integration**: Connect with Google Analytics, Power BI
- **Marketing Automation**: Integrate with Marketo, Pardot
- **Reporting Tools**: Export to Excel, Tableau, Looker

## 🚨 Error Handling
- **API Rate Limits**: Implement exponential backoff for API calls
- **Authentication Errors**: Automatic token refresh when expired
- **Data Validation**: Validate campaign settings before submission
- **Network Issues**: Retry logic for transient failures

## 📚 Resources
- [Microsoft Advertising API Documentation](https://docs.microsoft.com/en-us/advertising/)
- [Bing Ads SDK for Python](https://github.com/BingAds/BingAds-Python-SDK)
- [Microsoft Advertising Developer Portal](https://developers.ads.microsoft.com/)
- [API Best Practices Guide](https://docs.microsoft.com/en-us/advertising/guides/)

## License
MIT
