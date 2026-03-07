---
name: tiktok-mcp
description: >-
  Integrates with TikTok Marketing API for video content management, analytics,
  and advertising
dependencies:
  - node
  - npm
  - axios
  - tiktok-api
inputs:
  - name: access_token
    description: TikTok Marketing API access token
  - name: advertiser_id
    description: TikTok Advertiser ID
outputs:
  - type: stdout
    description: API response data
  - type: file
    description: Performance analytics in CSV format
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---

# TikTok Marketing API MCP

## 🎯 Triggers
- Schedule TikTok video posts
- Analyze video performance metrics
- Manage TikTok advertising campaigns
- Generate content recommendations

## ⚡ Quick Start
1. Run `bash test.sh` to check dependencies
2. Copy `.env.template` to `.env` and add TikTok API credentials
3. Run `npm install` via `install.sh`

## 📋 Workflow
1. Authenticate with TikTok Marketing API
2. Upload and schedule video content
3. Monitor engagement and virality metrics
4. Optimize posting times based on analytics

## 🛠️ Script Reference
- Use `scripts/upload_video.js` for video content
- Use `scripts/analytics.js` for performance tracking
- Use `scripts/ad_campaign.js` for advertising management
