---
name: linkedin-mcp
description: >-
  Integrates with LinkedIn API for professional networking, B2B marketing, lead
  generation, content publishing, and business development
version: 1.0.0
dependencies:
  - python3
  - node
  - npm
  - jq
  - linkedin-api-client
inputs:
  - name: linkedin_client_id
    description: LinkedIn OAuth Client ID
  - name: linkedin_client_secret
    description: LinkedIn OAuth Client Secret
  - name: linkedin_access_token
    description: LinkedIn OAuth Access Token
  - name: linkedin_refresh_token
    description: LinkedIn OAuth Refresh Token
outputs:
  - type: file
    description: LinkedIn analytics reports and exported connections
  - type: stdout
    description: API response data and operation results
compatibility: 'agent-zero, claude-code, cursor'
---

# LinkedIn MCP

## 🎯 Triggers
- "Post company updates to LinkedIn"
- "Analyze LinkedIn company page performance"
- "Find and connect with industry professionals"
- "Extract LinkedIn profile data for lead generation"
- "Schedule LinkedIn content calendar"
- "Monitor LinkedIn mentions and engagement"
- "Generate LinkedIn analytics reports"
- "Automate LinkedIn connection requests"

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/linkedin-mcp/test.sh`.
- [ ] Check `.env` contains required LinkedIn API credentials.
- [ ] Ensure Python 3.8+ and Node.js 16+ are installed.

## 📋 Workflow
1. **Authentication Setup**: Configure LinkedIn OAuth credentials in `.env`
2. **API Initialization**: Initialize LinkedIn API client with tokens
3. **Profile Analysis**: Extract and analyze professional profiles
4. **Content Publishing**: Schedule and publish posts/articles
5. **Network Management**: Manage connections and messages
6. **Analytics Generation**: Create performance reports
7. **Lead Generation**: Identify and qualify business prospects

## 🛠️ Script Reference
- Use `scripts/linkedin_api.py` for Python-based LinkedIn operations
- Use `scripts/linkedin_api.js` for Node.js-based LinkedIn operations
- Use `scripts/analytics_generator.py` for creating LinkedIn analytics reports
- Use `scripts/lead_scraper.py` for extracting LinkedIn profile data

## 🔐 Authentication
LinkedIn uses OAuth 2.0 with these scopes:
- `r_liteprofile` - Basic profile information
- `r_emailaddress` - Email address
- `w_member_social` - Post, comment, and like content
- `rw_organization_admin` - Manage organization pages
- `r_organization_social` - Read organization social data

## 📊 API Rate Limits
- Profile API: 100 requests/day (free tier)
- Share API: 25 posts/day (free tier)
- Search API: 100 requests/day (free tier)
- Organization API: 50 requests/day (free tier)

## 🚀 Advanced Features
- **Smart Post Scheduling**: Optimal posting times based on audience activity
- **Connection Scoring**: Prioritize connections by relevance and engagement
- **Content Performance Prediction**: AI-powered content optimization
- **Competitor Analysis**: Monitor competitor LinkedIn activity
- **Employee Advocacy**: Coordinate team LinkedIn activity

## 🔧 Troubleshooting
- **Authentication Errors**: Verify OAuth tokens and refresh if expired
- **Rate Limit Exceeded**: Implement exponential backoff
- **API Changes**: LinkedIn API frequently updates - check changelog
- **Content Rejection**: Ensure posts comply with LinkedIn Professional Community Policies
