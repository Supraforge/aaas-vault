---
name: hubspot-mcp-integration
description: >-
  Connects to HubSpot CRM via MCP to access contacts, companies, deals, and
  marketing analytics
version: 1.0.0
dependencies:
  - nodejs
  - npm
  - mcp-client
inputs:
  - name: hubspot_account_id
    description: Your HubSpot account ID or portal ID
  - name: query_type
    description: 'Type of data to query (contacts, companies, deals, analytics)'
  - name: query_parameters
    description: JSON string of query parameters for filtering
outputs:
  - type: stdout
    description: JSON formatted HubSpot data or analysis results
  - type: file
    description: CSV export of HubSpot data when requested
compatibility: 'agent-zero, claude-code, cursor'
---

# HubSpot MCP Integration

## 🎯 Triggers
- "Connect to my HubSpot CRM and get recent contacts"
- "Analyze deal pipeline from HubSpot"
- "Export marketing analytics from HubSpot"
- "Sync HubSpot contacts with other systems"

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/hubspot-mcp-integration/test.sh`.
- [ ] Check `.env` contains required keys (HUBSPOT_ACCESS_TOKEN).
- [ ] Ensure MCP client is installed and configured.

## 📋 Workflow
1. **Authentication**: Load HubSpot access token from `.env` file
2. **MCP Connection**: Connect to HubSpot MCP server using account credentials
3. **Data Query**: Execute queries for contacts, companies, deals, or analytics
4. **Processing**: Transform and analyze the data as needed
5. **Output**: Return structured data or generate reports

## 🛠️ Script Reference
- Use `scripts/query_hubspot.js` for basic data queries
- Use `scripts/export_contacts.js` for CSV exports
- Use `scripts/analyze_deals.js` for pipeline analysis

## 🔗 MCP Server Setup
To use this skill, you need to set up the HubSpot MCP server:
1. Install the HubSpot MCP server: `npm install -g @hubspot/mcp-server`
2. Configure with your HubSpot access token
3. Start the MCP server in the background

## 📊 Example Queries
- "Get all contacts created in the last 30 days"
- "Show deal pipeline by stage"
- "Export company data for sales outreach"
- "Analyze email campaign performance"
