---
name: notion-mcp
description: >-
  Integrates with Notion API for knowledge management, database automation, and
  content organization
version: 1.0.0
dependencies:
  - python3
  - node
  - npm
inputs:
  - name: notion_token
    description: Notion API integration token
  - name: database_id
    description: Notion database ID to work with
outputs:
  - type: stdout
    description: JSON response from Notion API operations
  - type: file
    description: Exported Notion pages as markdown
compatibility: 'agent-zero, claude-code, cursor'
---

# Notion API MCP Skill

## 🎯 Triggers
- User wants to automate Notion database operations
- User needs to sync content between Notion and other platforms
- User wants to create automated knowledge management workflows
- User needs to extract data from Notion for analysis

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/notion-mcp/test.sh`.
- [ ] Check `.env` contains `NOTION_API_TOKEN`.
- [ ] Ensure Node.js and npm are installed.

## 📋 Workflow
1. **Authentication**: Configure Notion API token in `.env`
2. **Database Setup**: Identify target database ID
3. **Operation Selection**: Choose between read, write, update, or query operations
4. **Execution**: Run MCP server or direct API calls
5. **Verification**: Check response status and data integrity

## 🛠️ Script Reference
- Use `scripts/notion_mcp_server.js` for MCP server implementation
- Use `scripts/notion_api_client.py` for Python API operations
- Use `scripts/export_pages.js` for exporting Notion pages to markdown

## 🔌 MCP Server Features
- **Database Query**: Query Notion databases with filters
- **Page Creation**: Create new pages with rich content
- **Page Update**: Update existing pages with new content
- **Content Export**: Export pages to markdown format
- **Block Operations**: Manipulate page blocks programmatically

## 📊 API Rate Limits
- Notion API has rate limits (3 requests per second)
- Implement retry logic with exponential backoff
- Batch operations when possible

## 🔐 Security Notes
- Store `NOTION_API_TOKEN` securely in `.env`
- Never commit `.env` files to version control
- Use database IDs not full URLs in public code
