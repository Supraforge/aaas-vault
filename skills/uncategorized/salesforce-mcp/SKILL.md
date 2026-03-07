---
name: salesforce-mcp
description: >-
  Integrates with Salesforce API for CRM automation, sales pipeline management,
  lead tracking, and business intelligence
version: 1.0.0
dependencies:
  - python3
  - node
  - npm
  - jq
inputs:
  - name: salesforce_client_id
    description: Salesforce Connected App Client ID
  - name: salesforce_client_secret
    description: Salesforce Connected App Client Secret
  - name: salesforce_username
    description: Salesforce username for authentication
  - name: salesforce_password
    description: Salesforce password with security token
  - name: salesforce_instance_url
    description: 'Salesforce instance URL (e.g., https://yourdomain.my.salesforce.com)'
outputs:
  - type: file
    description: Salesforce data exports in JSON/CSV format
  - type: stdout
    description: Real-time sales metrics and pipeline reports
compatibility: 'agent-zero, claude-code, cursor'
---

# Salesforce MCP

## 🎯 Triggers
- "Connect to Salesforce and get my sales pipeline"
- "Create a new lead in Salesforce from this contact information"
- "Update opportunity stage and generate forecast report"
- "Sync Salesforce contacts with our marketing platform"
- "Analyze sales performance and generate quarterly reports"

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/salesforce-mcp/test.sh`.
- [ ] Check `.env` contains required Salesforce credentials.
- [ ] Ensure Python dependencies are installed: `pip install simple-salesforce pandas`

## 📋 Workflow
1. **Authentication**: Connect to Salesforce using OAuth 2.0 JWT Bearer or Username-Password flow
2. **Data Operations**: Query, create, update, delete Salesforce records (Leads, Contacts, Accounts, Opportunities)
3. **Pipeline Management**: Track sales stages, forecast revenue, identify bottlenecks
4. **Reporting**: Generate sales dashboards, performance metrics, and business intelligence
5. **Automation**: Trigger workflows, send notifications, sync with other platforms

## 🛠️ Script Reference
- Use `scripts/salesforce_operations.py` for core CRM operations
- Use `scripts/salesforce_analytics.py` for reporting and dashboards
- Use `scripts/salesforce_sync.py` for data synchronization
- Use `nodejs/server.js` for MCP server implementation

## 🔧 Configuration
Create `.env` file with:
```
SALESFORCE_CLIENT_ID=your_client_id
SALESFORCE_CLIENT_SECRET=your_client_secret
SALESFORCE_USERNAME=your_username
SALESFORCE_PASSWORD=your_password_with_token
SALESFORCE_INSTANCE_URL=https://yourdomain.my.salesforce.com
SALESFORCE_API_VERSION=59.0
```

## 📚 API Reference
- **SOQL Queries**: Salesforce Object Query Language for data retrieval
- **REST API**: CRUD operations on Salesforce objects
- **Bulk API**: Large data operations
- **Streaming API**: Real-time notifications

## 🚀 Advanced Features
- **Sales Forecasting**: Predictive analytics on pipeline
- **Lead Scoring**: Automated lead qualification
- **Territory Management**: Sales team assignment
- **Einstein Analytics**: AI-powered insights
