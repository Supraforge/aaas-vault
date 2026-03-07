---
name: facebook-marketing-mcp
description: >-
  Integrates with Facebook Marketing API for automated ad campaigns, audience
  targeting, and performance analytics
version: 1.0.0
dependencies:
  - nodejs
  - npm
  - python3
  - jq
inputs:
  - name: campaign_data
    description: >-
      JSON or YAML file containing campaign parameters (budget, targeting,
      creative)
  - name: audience_segment
    description: CSV file with audience data or segment criteria
outputs:
  - type: file
    description: Campaign performance report in JSON format
  - type: stdout
    description: Real-time campaign status and metrics
compatibility: 'agent-zero, claude-code, cursor'
---

# Facebook Marketing API MCP Integration

## 🎯 Triggers
- "Create Facebook ad campaign for product launch"
- "Analyze Facebook ad performance from last week"
- "Optimize Facebook ad targeting based on engagement"
- "Generate Facebook audience insights report"
- "Automate Facebook ad budget allocation"

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/facebook-marketing-mcp/test.sh`.
- [ ] Check `.env` contains Facebook API credentials.
- [ ] Ensure Node.js and npm are installed.

## 📋 Workflow
1. **Authentication**: Connect to Facebook Marketing API using OAuth 2.0
2. **Campaign Setup**: Create campaigns, ad sets, and ads from templates
3. **Audience Management**: Build custom audiences from CRM data or website visitors
4. **Creative Management**: Upload images/videos and generate ad variations
5. **Performance Monitoring**: Track impressions, clicks, conversions, ROAS
6. **Optimization**: Automated bid adjustments and audience refinement

## 🛠️ Script Reference
- Use `scripts/create-campaign.js` for new ad campaigns
- Use `scripts/analyze-performance.py` for performance analytics
- Use `scripts/audience-builder.sh` for audience segmentation
- Use `scripts/budget-optimizer.js` for automated budget allocation

## 🔌 MCP Server Features
- **Campaign Management**: Create, pause, update campaigns
- **Audience Insights**: Demographic and behavioral analysis
- **Creative Library**: Manage ad creatives and templates
- **Reporting**: Custom reports and dashboards
- **Automation**: Rule-based campaign optimization

## 📊 Business Applications
- **E-commerce**: Dynamic product ads and retargeting
- **Lead Generation**: Form ads and lead quality scoring
- **Brand Awareness**: Reach and frequency campaigns
- **App Installs**: Mobile app promotion and engagement
- **Local Business**: Location-based targeting and promotions

## 🔐 Security Notes
- Store Facebook API tokens securely in `.env`
- Implement rate limiting to avoid API throttling
- Use environment-specific configurations (dev/staging/prod)
- Regular token rotation and permission audits
