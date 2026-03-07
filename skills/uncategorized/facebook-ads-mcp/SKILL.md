---
name: facebook-ads-mcp
description: >-
  Automates Facebook Ads management, campaign creation, performance reporting,
  and budget optimization through MCP integration
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
    description: >-
      The Facebook Ads operation to perform (create-campaign, get-report,
      optimize-bids, etc.)
  - name: campaign_name
    description: Name for new campaign (required for create-campaign)
  - name: budget_amount
    description: Daily budget amount in currency (required for create-campaign)
  - name: target_audience
    description: JSON string of targeting parameters
  - name: ad_creative
    description: JSON string of ad creative elements
  - name: report_type
    description: 'Type of report to generate (performance, demographics, conversions)'
  - name: date_range
    description: 'Date range for reporting (today, yesterday, last_7_days, etc.)'
outputs:
  - type: file
    description: Campaign performance report in CSV/JSON format
  - type: stdout
    description: Operation results and campaign details
  - type: file
    description: Optimized bid recommendations
compatibility: 'agent-zero, claude-code, cursor'
---

# Facebook Ads MCP

## 🎯 Triggers
- "Create a Facebook Ads campaign for our new product launch"
- "Generate performance report for our Facebook Ads campaigns"
- "Optimize Facebook Ads bids based on conversion data"
- "Analyze audience demographics for our Facebook Ads"
- "Automate A/B testing for Facebook ad creatives"

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/facebook-ads-mcp/test.sh`.
- [ ] Check `.env` contains required Facebook Ads API credentials.
- [ ] Ensure Python dependencies are installed: `pip install facebook-business`

## 📋 Workflow
1. **Authentication**: Load Facebook Ads API credentials from `.env`
2. **Campaign Management**: Create, update, pause, or delete campaigns
3. **Ad Creation**: Generate ad sets and ads with targeting parameters
4. **Reporting**: Pull performance metrics and generate insights
5. **Optimization**: Adjust bids, budgets, and targeting based on performance

## 🛠️ Script Reference
- Use `scripts/facebook_ads_manager.py` for campaign management
- Use `scripts/facebook_ads_reporter.py` for performance reporting
- Use `scripts/facebook_ads_optimizer.py` for bid optimization
- Use `scripts/facebook_ads_api.js` for Node.js integration

## 🔧 API Integration

### Python SDK
```bash
# Install Facebook Business SDK
pip install facebook-business

# Set up environment variables
export FACEBOOK_ADS_ACCESS_TOKEN=your_token
export FACEBOOK_ADS_ACCOUNT_ID=your_account_id
export FACEBOOK_ADS_APP_ID=your_app_id
export FACEBOOK_ADS_APP_SECRET=your_app_secret

# Run campaign manager
python3 scripts/facebook_ads_manager.py --action create-campaign --name "Summer Sale" --budget 100
```

### Node.js
```bash
cd scripts && npm install
node facebook_ads_api.js --list-campaigns
node facebook_ads_api.js --report csv
```

## API Requirements
- Facebook Ads API access
- Access token with ads_management permission
- Ad account ID
- App ID and App Secret

## License
MIT
