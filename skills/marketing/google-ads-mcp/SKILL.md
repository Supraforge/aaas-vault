---
name: google-ads-mcp
description: >-
  Integrates with Google Ads API for advertising automation, campaign
  management, bid optimization, performance tracking, and ad creation
version: 1.0.0
dependencies:
  - python3
  - node
  - npm
  - jq
  - google-ads-api
inputs:
  - name: google_ads_client_id
    description: Google Ads OAuth Client ID
  - name: google_ads_client_secret
    description: Google Ads OAuth Client Secret
  - name: google_ads_refresh_token
    description: Google Ads OAuth Refresh Token
  - name: google_ads_developer_token
    description: Google Ads Developer Token
  - name: google_ads_customer_id
    description: Google Ads Customer ID (10-digit number)
outputs:
  - type: file
    description: Campaign performance reports in CSV/JSON format
  - type: stdout
    description: Real-time campaign metrics and optimization recommendations
compatibility: 'agent-zero, claude-code, cursor'
---

# Google Ads MCP

## 🎯 Triggers
- "Set up Google Ads campaigns for my product launch"
- "Optimize my Google Ads bids for better ROI"
- "Generate performance report for my ad campaigns"
- "Create new search ads for my keywords"
- "Analyze competitor ad strategies"

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/google-ads-mcp/test.sh`.
- [ ] Check `.env` contains required Google Ads API credentials.
- [ ] Ensure Python dependencies are installed: `pip install google-ads`

## 📋 Workflow
1. **Authentication**: Connect to Google Ads API using OAuth 2.0
2. **Campaign Setup**: Create/manage search, display, shopping campaigns
3. **Bid Management**: Automated bid adjustments based on performance
4. **Performance Analysis**: Generate detailed reports and insights
5. **Optimization**: Provide actionable recommendations

## 🛠️ Script Reference
- Use `scripts/google_ads_manager.py` for campaign management
- Use `scripts/google_ads_reporter.py` for performance reporting
- Use `scripts/google_ads_optimizer.py` for bid optimization

## 🔧 API Capabilities
- Campaign creation and management
- Ad group and keyword management
- Bid strategy optimization
- Performance reporting and analytics
- Conversion tracking
- Audience targeting
- Budget management
- A/B testing setup

## 📊 Key Metrics Tracked
- Click-through Rate (CTR)
- Cost Per Click (CPC)
- Conversion Rate
- Return on Ad Spend (ROAS)
- Quality Score
- Impression Share
- Cost Per Acquisition (CPA)

## 🚀 Advanced Features
- Automated bid adjustments based on time of day
- Competitor ad copy analysis
- Keyword expansion suggestions
- Negative keyword management
- Performance forecasting
- Budget pacing alerts

## 🔐 Security Notes
- Store API credentials in `.env` file
- Use OAuth 2.0 with refresh tokens
- Implement rate limiting for API calls
- Log all changes for audit trail
