---
name: instagram-mcp
description: >-
  Integrates with Instagram Graph API for business account management, content
  scheduling, and engagement analytics
version: 1.0.0
dependencies:
  - nodejs
  - npm
  - instagram-graph-api
inputs:
  - name: access_token
    description: Instagram Graph API access token with required permissions
  - name: business_account_id
    description: Instagram Business Account ID
  - name: content_path
    description: Path to image/video content for posting
outputs:
  - type: file
    description: Analytics report in JSON format
  - type: stdout
    description: Post status and engagement metrics
compatibility: 'agent-zero, claude-code, cursor'
---

# Instagram API MCP Skill

## 🎯 Triggers
- "Schedule Instagram posts for this week"
- "Analyze Instagram engagement metrics"
- "Post new product images to Instagram"
- "Monitor Instagram comments and respond"
- "Generate Instagram content calendar"

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/instagram-mcp/test.sh`.
- [ ] Check `.env` contains required Instagram API credentials.
- [ ] Ensure Instagram Business Account is connected.

## 📋 Workflow
1. **Authentication**: Validate Instagram Graph API credentials
2. **Content Preparation**: Process images/videos with optimal sizing
3. **Scheduling**: Queue posts based on optimal engagement times
4. **Publishing**: Post to Instagram with captions and hashtags
5. **Analytics**: Track performance and generate reports

## 🛠️ Script Reference
- Use `scripts/schedule_post.js` for content scheduling
- Use `scripts/analytics_report.js` for engagement analysis
- Use `scripts/media_upload.js` for image/video posting

## 🔌 MCP Server Capabilities
- **instagram.query_insights**: Get account insights and metrics
- **instagram.schedule_post**: Schedule content for future posting
- **instagram.upload_media**: Upload images/videos to Instagram
- **instagram.get_comments**: Retrieve and manage comments
- **instagram.analyze_hashtags**: Analyze hashtag performance

## 📊 API Integration Details
- **Base URL**: https://graph.facebook.com/v18.0/
- **Required Permissions**: instagram_basic, instagram_manage_insights, instagram_content_publish
- **Rate Limits**: 200 calls/hour per access token

## 🚀 Example Usage
```bash
# Set up environment
cp .env.template .env
# Edit .env with your credentials

# Test the skill
bash test.sh

# Run analytics report
node scripts/analytics_report.js
```
