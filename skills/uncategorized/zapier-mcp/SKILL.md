---
name: zapier-mcp
description: >-
  Integrates with Zapier API for workflow automation, multi-app connections, and
  business process orchestration
version: 1.0.0
dependencies:
  - python3
  - node
  - npm
inputs:
  - name: zapier_token
    description: Zapier API personal access token
  - name: zap_id
    description: Zap ID for specific workflow
  - name: trigger_data
    description: JSON data to trigger a zap
outputs:
  - type: stdout
    description: JSON response from Zapier API operations
  - type: file
    description: Workflow execution logs and results
compatibility: 'agent-zero, claude-code, cursor'
---

# Zapier MCP Integration

## 🎯 Triggers
- "Connect my apps with Zapier"
- "Automate workflow between [App1] and [App2]"
- "Trigger a zap with this data"
- "Monitor my zap executions"
- "Create a new zap workflow"

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/zapier-mcp/test.sh`.
- [ ] Check `.env` contains `ZAPIER_API_KEY`.
- [ ] Ensure Node.js v18+ is installed.

## 📋 Workflow
1. **Authentication**: Load Zapier API credentials from `.env`
2. **Zap Discovery**: List available zaps and workflows
3. **Trigger Execution**: Run zaps with provided data
4. **Monitoring**: Check execution status and results
5. **Webhook Setup**: Create webhook endpoints for real-time triggers

## 🛠️ Script Reference
- Use `scripts/zapier_mcp_server.js` for Node.js MCP server
- Use `scripts/zapier_workflow.py` for Python automation
- Use `scripts/zapier_webhook.py` for webhook management

## 🔌 API Capabilities
- **Zap Management**: List, create, update, delete zaps
- **Execution Control**: Trigger, pause, resume zaps
- **History**: Retrieve execution logs and results
- **Webhooks**: Create and manage webhook endpoints
- **App Connections**: Manage connected app accounts

## 📊 Use Cases
1. **Marketing Automation**: Trigger email campaigns from form submissions
2. **Sales Pipeline**: Update CRM when deals progress
3. **Support Tickets**: Create tickets from social media mentions
4. **Data Sync**: Keep databases in sync across platforms
5. **Notifications**: Send alerts based on business events
