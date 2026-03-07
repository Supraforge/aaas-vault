---
name: pinterest-mcp
description: Integrates with Pinterest API for visual discovery, content curation, and e-commerce marketing automation
version: 1.0.0
dependencies: ["nodejs", "npm", "python3", "curl"]
inputs:
  - name: access_token
    description: Pinterest OAuth 2.0 access token
  - name: board_id
    description: Pinterest board ID for pin operations
  - name: image_url
    description: URL of image to pin
  - name: description
    description: Pin description text
outputs:
  - type: stdout
    description: JSON response from Pinterest API
  - type: file
    description: Analytics reports in CSV format
---

# Pinterest API MCP Integration

## 🎯 Triggers
- "Create a Pinterest pin for our new product"
- "Analyze Pinterest engagement metrics"
- "Schedule pins to multiple boards"
- "Extract trending topics from Pinterest"
- "Monitor competitor Pinterest activity"

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/pinterest-mcp/test.sh`.
- [ ] Check `.env` contains `PINTEREST_ACCESS_TOKEN`.
- [ ] Ensure Pinterest Developer App is created at https://developers.pinterest.com/

## 📋 Workflow
1. **Authentication**: Obtain OAuth 2.0 token from Pinterest Developer Portal
2. **Board Management**: Create, list, or update Pinterest boards
3. **Pin Operations**: Create pins, schedule posts, analyze performance
4. **Analytics**: Extract engagement metrics, follower growth, click-through rates
5. **Automation**: Schedule recurring pin creation based on content calendar

## 🛠️ Script Reference
- Use `scripts/pinterest_api.js` for direct API calls
- Use `scripts/analytics.js` for data analysis
- Use `scripts/scheduler.js` for automated posting

## 🔌 MCP Server Implementation
This skill includes a Model Context Protocol (MCP) server that exposes:
- `pinterest.create_pin`: Create new pins with images
- `pinterest.get_analytics`: Retrieve board and pin analytics
- `pinterest.search_pins`: Search for trending content
- `pinterest.manage_boards`: Create and organize boards

## 📊 API Endpoints Covered
- Pins: Create, Get, Update, Delete
- Boards: List, Create, Update
- Analytics: Get board analytics, Get pin analytics
- User Account: Get user info, Get followers

## 🔐 Security Notes
- Store `PINTEREST_ACCESS_TOKEN` in `.env` file
- Never commit `.env` to version control
- Use environment-specific tokens for dev/prod
