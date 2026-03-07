---
name: hubspot-mcp
description: >-
  Integrates with HubSpot API for CRM management, marketing automation, sales
  pipelines, and customer service operations
version: 1.0.0
dependencies:
  - python3
  - node
  - npm
inputs:
  - name: hubspot_access_token
    description: HubSpot OAuth access token or private app access token
  - name: hubspot_portal_id
    description: HubSpot portal ID for API requests
outputs:
  - type: file
    description: 'CRM data exports, marketing analytics reports, contact lists'
  - type: stdout
    description: 'API responses, operation status, error messages'
compatibility: 'agent-zero, claude-code, cursor'
---

# HubSpot MCP Skill

## 🎯 Triggers
- "Connect to HubSpot CRM and sync contacts"
- "Create a marketing automation workflow"
- "Analyze sales pipeline performance"
- "Export customer data for reporting"
- "Manage deals and companies in HubSpot"

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/hubspot-mcp/test.sh`.
- [ ] Check `.env` contains required HubSpot API credentials.
- [ ] Ensure Python dependencies are installed via `install.sh`.

## 📋 Workflow
1. **Authentication Setup**: Configure HubSpot OAuth or private app tokens
2. **CRM Operations**: Create/update contacts, companies, deals, tickets
3. **Marketing Automation**: Manage workflows, email campaigns, forms
4. **Sales Pipeline**: Track deals, analyze pipeline, forecast revenue
5. **Analytics & Reporting**: Generate reports, export data, analyze performance

## 🛠️ Script Reference
- Use `scripts/hubspot_crm.py` for CRM operations (contacts, companies, deals)
- Use `scripts/hubspot_marketing.py` for marketing automation and campaigns
- Use `scripts/hubspot_mcp_server.js` for MCP server implementation
- Use `scripts/hubspot_analytics.py` for reporting and data analysis

## 🔧 Configuration
Create `.env` file with:
```
HUBSPOT_ACCESS_TOKEN=your_access_token_here
HUBSPOT_PORTAL_ID=your_portal_id_here
```

## 📚 API Reference
- **Contacts API**: Manage contact records and properties
- **Companies API**: Handle company records and associations
- **Deals API**: Track sales deals through pipeline stages
- **Marketing API**: Automate emails, workflows, and campaigns
- **Analytics API**: Generate reports and performance metrics

## 🚀 Deployment
```bash
# Install dependencies
bash install.sh

# Start MCP server
node scripts/hubspot_mcp_server.js

# Test CRM operations
python3 scripts/hubspot_crm.py
```
