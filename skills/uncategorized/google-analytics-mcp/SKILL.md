---
name: google-analytics-mcp
description: Integrates with Google Analytics API for web analytics, traffic analysis, user behavior tracking, and marketing optimization
version: 1.0.0
dependencies: ["python3", "node", "npm", "jq", "google-auth-library"]
inputs:
  - name: google_client_id
    description: Google Cloud OAuth Client ID
  - name: google_client_secret
    description: Google Cloud OAuth Client Secret
  - name: google_analytics_property_id
    description: Google Analytics Property ID (format: GA4-XXXXXXX)
  - name: google_analytics_view_id
    description: Google Analytics View ID (for Universal Analytics)
outputs:
  - type: file
    description: Analytics reports in CSV/JSON format
  - type: stdout
    description: Summary insights and recommendations
---

# Google Analytics MCP

## 🎯 Triggers
- "Analyze website traffic for the last 30 days"
- "Get conversion rate report for e-commerce"
- "Track user engagement metrics"
- "Generate marketing performance dashboard"
- "Monitor real-time website visitors"

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/google-analytics-mcp/test.sh`.
- [ ] Check `.env` contains required Google Cloud credentials.
- [ ] Ensure Google Analytics API is enabled in Google Cloud Console.

## 📋 Workflow
1. **Authentication**: OAuth2 flow with Google Cloud credentials
2. **Data Extraction**: Query GA4 or Universal Analytics APIs
3. **Processing**: Transform raw data into actionable insights
4. **Reporting**: Generate visualizations and recommendations
5. **Automation**: Schedule regular analytics reports

## 🛠️ Script Reference
- Use `scripts/python/analytics.py` for Python-based analytics
- Use `scripts/node/analytics.js` for Node.js implementations
- Use `scripts/export_reports.sh` for batch export operations

## 🔧 API Endpoints Covered
- Google Analytics Data API (GA4)
- Google Analytics Reporting API (v4)
- Google Analytics Admin API
- Real-time Reporting API

## 📊 Key Metrics Tracked
- Users, Sessions, Pageviews
- Bounce Rate, Session Duration
- Conversion Rates, Goal Completions
- Traffic Sources, Channels
- User Demographics, Geography
- E-commerce Performance
- Custom Events and Conversions
