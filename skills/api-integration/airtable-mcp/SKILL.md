---
name: airtable-mcp
description: >-
  Integrates with Airtable API for database automation, CRM management, and
  business data workflows
version: 1.0.0
dependencies:
  - python3
  - node
  - npm
inputs:
  - name: airtable_token
    description: Airtable API personal access token
  - name: base_id
    description: Airtable base ID
  - name: table_name
    description: Airtable table name
outputs:
  - type: stdout
    description: JSON response from Airtable API operations
  - type: file
    description: Exported Airtable data as CSV or JSON
compatibility: 'agent-zero, claude-code, cursor'
---

# Airtable API MCP Skill

## 🎯 Triggers
- "Connect to Airtable and fetch customer data"
- "Automate CRM updates in Airtable"
- "Sync business data between Airtable and other platforms"
- "Generate reports from Airtable data"
- "Create automated workflows with Airtable"

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/airtable-mcp/test.sh`.
- [ ] Check `.env` contains `AIRTABLE_TOKEN`, `AIRTABLE_BASE_ID`.
- [ ] Ensure Node.js and Python dependencies are installed.

## 📋 Workflow
1. **Authentication**: Load Airtable credentials from `.env`
2. **Connection**: Initialize Airtable client with base ID
3. **Operation**: Perform requested CRUD operations
4. **Export**: Format and output results

## 🛠️ Script Reference
- Use `scripts/airtable_mcp_server.js` for MCP server operations
- Use `scripts/airtable_api_client.py` for Python-based operations
- Use `scripts/airtable_workflow.js` for complex automations

## 🔌 MCP Server Features
- **List Resources**: Browse Airtable bases, tables, views
- **Read Resources**: Fetch records from tables
- **Create Resources**: Add new records to tables
- **Update Resources**: Modify existing records
- **Delete Resources**: Remove records from tables
- **Search Resources**: Query records with filters

## 📊 Use Cases
1. **CRM Automation**: Sync customer data between platforms
2. **Lead Management**: Track and update lead status
3. **Inventory Tracking**: Manage product inventory
4. **Project Management**: Track tasks and deadlines
5. **Marketing Campaigns**: Manage campaign data
6. **Financial Tracking**: Record expenses and revenues

## 🔐 Security Notes
- Store Airtable tokens securely in `.env`
- Use environment variables for sensitive data
- Implement rate limiting for API calls
- Validate all inputs before processing
