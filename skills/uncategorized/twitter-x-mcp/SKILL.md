---
name: twitter-x-mcp
description: >-
  Integrates with Twitter/X API for social media management, content scheduling,
  and engagement analytics
version: 1.0.0
dependencies:
  - nodejs
  - npm
  - python3
  - jq
inputs:
  - name: tweet_content
    description: 'Text content for tweets, threads, or replies'
  - name: schedule_data
    description: JSON file with posting schedule and content
  - name: analytics_params
    description: 'Parameters for analytics (date range, metrics)'
outputs:
  - type: stdout
    description: API response or operation confirmation
  - type: file
    description: Analytics reports in JSON/CSV format
compatibility: 'agent-zero, claude-code, cursor'
---

# Twitter/X API MCP Integration

## 🎯 Triggers
- "Schedule tweets for our product launch"
- "Analyze Twitter engagement for our brand"
- "Monitor mentions and respond to customers"
- "Create Twitter thread about our new feature"
- "Track competitor activity on Twitter"

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/twitter-x-mcp/test.sh`.
- [ ] Check `.env` contains Twitter API credentials.
- [ ] Ensure Node.js and npm are installed.

## 📋 Workflow
1. **Authentication**: Load Twitter API credentials from `.env`
2. **Content Creation**: Compose tweets, threads, or replies
3. **Scheduling**: Schedule posts for optimal engagement times
4. **Engagement**: Monitor mentions, replies, and direct messages
5. **Analytics**: Track impressions, engagements, and follower growth
6. **Reporting**: Generate performance reports for marketing teams

## 🛠️ Script Reference
- Use `scripts/schedule-tweet.js` for automated posting
- Use `scripts/analyze-engagement.js` for performance metrics
- Use `scripts/monitor-mentions.js` for real-time engagement
- Use `scripts/create-thread.js` for multi-tweet content

## 🔧 API Endpoints Covered
- Tweet creation and management
- User lookup and profile management
- Search and stream APIs
- Analytics and metrics
- Direct messaging
- Lists and spaces

## 📊 Business Applications
- **Marketing**: Product launches, brand awareness campaigns
- **Sales**: Lead generation through social listening
- **Support**: Customer service via direct messages
- **Growth**: Follower acquisition and engagement optimization
- **Competitive Intelligence**: Monitor competitor activities

## 🔐 Security Notes
- Store API keys securely in `.env` file
- Implement rate limiting to avoid API bans
- Use OAuth 2.0 for user authentication
- Regularly rotate access tokens
