---
name: youtube-mcp
description: >-
  Integrates with YouTube Data API v3 for video management, analytics, and
  content automation
version: 1.0.0
dependencies:
  - nodejs
  - npm
  - googleapis
  - express
  - dotenv
inputs:
  - name: channel_id
    description: YouTube channel ID to manage
  - name: video_file
    description: Path to video file for upload
  - name: analytics_period
    description: 'Time period for analytics (7days, 30days, lifetime)'
outputs:
  - type: file
    description: Analytics reports in CSV format
  - type: stdout
    description: Video upload status and metrics
compatibility: 'agent-zero, claude-code, cursor'
---

# YouTube API MCP

## 🎯 Triggers
- "Upload this video to my YouTube channel"
- "Get analytics for my YouTube videos"
- "Schedule YouTube content for next week"
- "Find trending topics in my niche"
- "Optimize video titles and descriptions"

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/youtube-mcp/test.sh`.
- [ ] Check `.env` contains required Google API credentials.
- [ ] Ensure OAuth 2.0 is configured for YouTube Data API.

## 📋 Workflow
1. **Authentication**: Configure OAuth 2.0 with Google Cloud Console
2. **Channel Setup**: Connect to YouTube channel via API
3. **Content Management**: Upload, schedule, and manage videos
4. **Analytics**: Retrieve view counts, engagement metrics, demographics
5. **Optimization**: A/B test titles, thumbnails, descriptions

## 🛠️ Script Reference
- Use `scripts/upload_video.js` for video uploads
- Use `scripts/get_analytics.js` for performance metrics
- Use `scripts/schedule_content.js` for content calendar
- Use `scripts/trend_analysis.js` for topic research

## 🔧 API Configuration
1. Create project in Google Cloud Console
2. Enable YouTube Data API v3
3. Create OAuth 2.0 credentials
4. Set redirect URIs for your application
5. Configure scopes: youtube.upload, youtube.readonly, youtube.force-ssl

## 📊 Analytics Capabilities
- **View Analytics**: Track views, watch time, audience retention
- **Engagement Metrics**: Likes, comments, shares, subscribers gained
- **Demographics**: Age, gender, geographic distribution
- **Traffic Sources**: How viewers discover your content
- **Playback Locations**: Where videos are watched

## ⚙️ MCP Server Features
- **Video Management**: Upload, update, delete videos
- **Playlist Operations**: Create, manage, reorder playlists
- **Live Streaming**: Schedule and manage live broadcasts
- **Comment Moderation**: Filter, reply to, moderate comments
- **Caption Management**: Add, edit, sync closed captions

## 🚀 Advanced Features
- **Bulk Operations**: Process multiple videos simultaneously
- **Automated Publishing**: Schedule videos based on optimal times
- **A/B Testing**: Test different thumbnails and titles
- **Competitor Analysis**: Monitor competitor channel performance
- **Content Gap Analysis**: Identify missing content opportunities

## 🔐 Security Notes
- Store OAuth tokens securely
- Implement token refresh mechanisms
- Use environment variables for API keys
- Follow YouTube API quotas and limits

## 📈 Business Applications
- **Content Marketing**: Distribute branded video content
- **Product Demos**: Showcase products and features
- **Customer Education**: Create tutorial and how-to videos
- **Brand Building**: Establish thought leadership
- **Lead Generation**: Drive traffic to landing pages
