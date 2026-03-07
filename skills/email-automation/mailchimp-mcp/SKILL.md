---
name: mailchimp-mcp
description: >-
  Integrates with Mailchimp API for email marketing automation, audience
  management, campaign creation, and analytics
version: 1.0.0
dependencies:
  - python3
  - node
  - npm
inputs:
  - name: mailchimp_api_key
    description: Mailchimp API key for authentication
  - name: mailchimp_server_prefix
    description: 'Mailchimp server prefix (e.g., ''us1'', ''us2'')'
outputs:
  - type: file
    description: Campaign performance reports and analytics
  - type: stdout
    description: Audience statistics and campaign status
compatibility: 'agent-zero, claude-code, cursor'
---

# Mailchimp MCP Skill

## 🎯 Triggers
- "Set up Mailchimp email marketing automation"
- "Create email campaign in Mailchimp"
- "Segment Mailchimp audience based on behavior"
- "Analyze Mailchimp campaign performance"
- "Sync contacts to Mailchimp from CRM"
- "Automate Mailchimp welcome sequences"

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/mailchimp-mcp/test.sh`.
- [ ] Check `.env` contains `MAILCHIMP_API_KEY` and `MAILCHIMP_SERVER_PREFIX`.

## 📋 Workflow
1. **Authentication Setup**: Configure Mailchimp API credentials
2. **Audience Management**: Create/update audience lists and segments
3. **Campaign Creation**: Design and schedule email campaigns
4. **Automation Setup**: Configure automated email sequences
5. **Analytics**: Track opens, clicks, conversions, and ROI

## 🛠️ Script Reference
- Use `scripts/mailchimp_mcp_server.js` for MCP server
- Use `scripts/mailchimp_automation.py` for Python automation
- Use `scripts/mailchimp_analytics.py` for campaign analytics

## 🔌 MCP Tools
- `mailchimp_list_audiences` - List all audiences
- `mailchimp_create_campaign` - Create new email campaign
- `mailchimp_get_analytics` - Get campaign performance data
- `mailchimp_add_subscriber` - Add subscriber to audience
- `mailchimp_create_segment` - Create audience segment
- `mailchimp_send_test_email` - Send test email

## 📊 API Reference
- Base URL: `https://{server_prefix}.api.mailchimp.com/3.0/`
- Authentication: API key in Authorization header
