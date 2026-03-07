---
name: linkedin-ads-mcp
description: >-
  Automates LinkedIn Advertising management, campaign optimization, audience
  targeting, and B2B lead generation through MCP integration
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
      Action to perform (create_campaign, get_analytics, optimize_budget,
      target_audience, generate_report)
  - name: campaign_name
    description: Name of the LinkedIn campaign (required for create_campaign)
  - name: budget_amount
    description: Daily budget in USD (required for create_campaign)
  - name: target_audience
    description: Audience targeting parameters as JSON (optional)
  - name: report_format
    description: 'Output format for reports (json, csv, pdf) (optional)'
outputs:
  - type: file
    description: Campaign performance report in specified format
  - type: stdout
    description: Status messages and campaign analytics
compatibility: 'agent-zero, claude-code, cursor'
---

# LinkedIn Ads MCP Skill

## 🎯 Triggers
- "Create a LinkedIn Ads campaign for our B2B product launch"
- "Get analytics for our LinkedIn advertising performance"
- "Optimize LinkedIn Ads budget based on conversion data"
- "Target specific professional audiences on LinkedIn"
- "Generate LinkedIn Ads performance report for stakeholders"

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/linkedin-ads-mcp/test.sh`.
- [ ] Check `.env` contains LinkedIn Marketing API credentials.
- [ ] Run `./install.sh` to install Python and Node.js dependencies.

## 📋 Workflow
1. **Authentication**: Connect to LinkedIn Marketing API using OAuth 2.0
2. **Campaign Management**: Create, update, pause, or delete campaigns
3. **Audience Targeting**: Define professional demographics, job titles, industries
4. **Budget Optimization**: Adjust bids and budgets based on performance
5. **Analytics & Reporting**: Generate detailed performance reports

## 🛠️ Script Reference
- Use `scripts/linkedin_ads_manager.py` for Python-based campaign management
- Use `scripts/linkedin_ads_api.js` for Node.js API interactions
- Use `scripts/linkedin_ads_optimizer.py` for budget and bid optimization
- Use `scripts/linkedin_ads_reporter.py` for analytics and reporting

## 🔐 API Integration
This skill integrates with LinkedIn Marketing API v2:
- Campaign Management
- Audience Targeting
- Analytics & Reporting
- Lead Generation Forms
- Sponsored Content

## 📊 Supported Campaign Types
- Sponsored Content
- Sponsored InMail
- Text Ads
- Dynamic Ads
- Video Ads
- Carousel Ads

## 🎯 Target Audience Capabilities
- Job Title Targeting
- Company Size Targeting
- Industry Targeting
- Seniority Level Targeting
- Skills Targeting
- Groups Targeting
- Matched Audiences (Account Lists)

## 📈 Performance Metrics
- Impressions, Clicks, CTR
- Conversions, Conversion Rate
- Cost Per Click (CPC)
- Cost Per Conversion
- Return on Ad Spend (ROAS)
- Engagement Rate

## 🔄 MCP Integration
This skill implements MCP (Model Context Protocol) for seamless integration with AI assistants and automation workflows.
