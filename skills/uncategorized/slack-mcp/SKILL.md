---
name: slack-mcp
description: >-
  Integrates with Slack API for team communication, channel management, message
  automation, and workflow orchestration
version: 1.0.0
dependencies:
  - nodejs
  - npm
  - python3
  - curl
inputs:
  - name: slack_token
    description: Slack Bot User OAuth Token
  - name: channel_id
    description: Target Slack channel ID
  - name: message_text
    description: Message content to send
  - name: user_id
    description: Slack user ID for direct messages
outputs:
  - type: stdout
    description: API response or success confirmation
  - type: file
    description: JSON response files in .tmp/
compatibility: 'agent-zero, claude-code, cursor'
---

# Slack API MCP Integration

## 🎯 Triggers
- "Send a message to the team Slack channel"
- "Schedule daily standup reminders in Slack"
- "Monitor Slack channels for specific keywords"
- "Create automated workflows with Slack webhooks"
- "Manage Slack user groups and permissions"

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/slack-mcp/test.sh`.
- [ ] Check `.env` contains `SLACK_BOT_TOKEN`.
- [ ] Ensure Node.js and npm are installed.

## 📋 Workflow
1. **Authentication Setup**: Configure Slack app and obtain OAuth tokens
2. **Channel Discovery**: List available channels and identify targets
3. **Message Operations**: Send, schedule, and manage messages
4. **Webhook Integration**: Set up incoming/outgoing webhooks
5. **Workflow Automation**: Create automated responses and notifications

## 🛠️ Script Reference
- Use `scripts/slack_send_message.js` for sending messages
- Use `scripts/slack_list_channels.js` for channel discovery
- Use `scripts/slack_webhook_server.js` for webhook handling
- Use `scripts/slack_scheduled_messages.py` for scheduled tasks

## 🔧 MCP Server Implementation

The Slack MCP server provides:
- **Real-time messaging**: Send and receive Slack messages
- **Channel management**: Create, archive, and manage channels
- **User operations**: Get user info, send DMs, manage profiles
- **File sharing**: Upload and share files in channels
- **Workflow triggers**: Connect Slack events to business processes

## 📚 API Reference
- **Slack API Documentation**: https://api.slack.com/
- **Bot Token Scopes**: chat:write, channels:read, users:read, files:write
- **Rate Limits**: Tier 3 (50+ requests per minute)
- **Webhook Types**: Incoming, Outgoing, Events API, Socket Mode

## 🚀 Advanced Features
1. **Standup Automation**: Daily reminder collection and reporting
2. **Incident Management**: Alert routing and escalation policies
3. **CRM Integration**: Sync Slack conversations with customer records
4. **Analytics Dashboard**: Message volume and engagement metrics
5. **Multi-workspace Management**: Coordinate across multiple Slack instances
