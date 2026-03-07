---
name: pinterest-ads-mcp
description: Manages Pinterest Advertising campaigns, audience targeting, creative optimization, and performance analytics through MCP integration
version: 1.0.0
dependencies: ["python3", "pip", "node", "npm", "jq", "curl"]
inputs:
  - name: action
    description: The Pinterest Ads operation to perform (create_campaign, get_analytics, update_ad, etc.)
  - name: account_id
    description: Pinterest Ads account ID
  - name: campaign_data
    description: JSON string containing campaign parameters
  - name: ad_group_id
    description: Ad group identifier for ad operations
  - name: creative_data
    description: JSON string containing creative assets and specifications
outputs:
  - type: file
    description: Campaign performance report in CSV format
  - type: stdout
    description: Operation status and results
---

# Pinterest Ads MCP Skill

## 🎯 Triggers
- User wants to create or manage Pinterest Advertising campaigns
- User needs Pinterest Ads performance analytics and reporting
- User wants to optimize Pinterest ad creatives and targeting
- User needs to automate Pinterest Ads management workflows

## ⚡ Quick Start (Self-Check)
Before running Pinterest Ads operations:
- [ ] Run `bash ~/.gemini/skills/pinterest-ads-mcp/test.sh`.
- [ ] Ensure `.env` contains `PINTEREST_ACCESS_TOKEN` and `PINTEREST_AD_ACCOUNT_ID`.
- [ ] Install dependencies with `./install.sh`.

## 📋 Workflow
1. **Authentication Setup**: Configure Pinterest API credentials in `.env`
2. **Campaign Creation**: Define campaign objectives, budget, and schedule
3. **Ad Group Setup**: Configure targeting, placements, and bidding
4. **Creative Management**: Upload pins, create ads, and A/B test creatives
5. **Performance Monitoring**: Track impressions, clicks, conversions, and ROI
6. **Optimization**: Adjust bids, targeting, and creatives based on performance

## 🛠️ Script Reference
- Use `scripts/pinterest_ads_manager.py` for core campaign operations
- Use `scripts/pinterest_ads_analytics.py` for performance reporting
- Use `scripts/pinterest_ads_optimizer.py` for automated optimization

## 🔧 API Integration
This skill integrates with Pinterest Marketing API v5:
- Campaign Management
- Ad Creation and Management
- Audience Targeting
- Conversion Tracking
- Analytics and Reporting
- Creative Library Management

## 📊 Key Metrics
- Impressions
- Clicks and CTR
- Conversions and Conversion Rate
- Cost per Click (CPC)
- Return on Ad Spend (ROAS)
- Engagement Metrics (Saves, Closeups)

## 🎨 Creative Best Practices
- Vertical images (2:3 aspect ratio)
- Clear call-to-action
- Brand consistency
- Mobile-optimized designs
- Rich Pins for product information

## 🎯 Targeting Options
- Interest-based targeting
- Keyword targeting
- Demographic targeting
- Lookalike audiences
- Retargeting campaigns
- Device and placement targeting

## 📈 Optimization Strategies
- Bid optimization for conversions
- Audience expansion
- Creative rotation
- Dayparting
- Budget pacing
- Performance-based scaling

## 🔐 Security Notes
- Store API tokens securely in `.env`
- Implement rate limiting
- Monitor API usage costs
- Regular token rotation

## 📚 Resources
- [Pinterest Marketing API Documentation](https://developers.pinterest.com/docs/api/v5/)
- [Pinterest Business Help Center](https://help.pinterest.com/business)
- [Pinterest Ads Best Practices](https://business.pinterest.com/advertising/)

## License
MIT License
