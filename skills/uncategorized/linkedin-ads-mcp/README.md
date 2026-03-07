# LinkedIn Ads MCP Skill

## Overview
This skill provides comprehensive LinkedIn Advertising automation through MCP (Model Context Protocol) integration. It enables AI assistants to manage LinkedIn campaigns, optimize budgets, target professional audiences, and generate performance reports.

## Features
- **Campaign Management**: Create, update, pause, and delete LinkedIn campaigns
- **Audience Targeting**: Target by job title, company, industry, skills, and seniority
- **Budget Optimization**: AI-driven bid and budget optimization
- **Performance Analytics**: Detailed reporting and insights
- **MCP Integration**: Seamless integration with AI assistants
- **Multi-format Reports**: JSON, CSV, and executive summaries

## Installation
1. Clone or copy this skill to `~/.gemini/skills/linkedin-ads-mcp/`
2. Run `./install.sh` to install dependencies
3. Copy `.env.template` to `.env` and add your LinkedIn Marketing API credentials
4. Run `./test.sh` to verify setup

## LinkedIn API Setup
1. Create a LinkedIn Developer App at https://www.linkedin.com/developers/apps
2. Request access to Marketing API
3. Generate OAuth 2.0 credentials
4. Add credentials to `.env` file

## Usage Examples

### Python Script
```bash
python3 scripts/linkedin_ads_manager.py --create-campaign "B2B Product Launch" --budget 100
python3 scripts/linkedin_ads_manager.py --list-campaigns
python3 scripts/linkedin_ads_manager.py --get-analytics "campaign_id_here"
```

### Node.js Script
```bash
node scripts/linkedin_ads_api.js --test
node scripts/linkedin_ads_api.js --list-campaigns
```

### Optimization
```bash
python3 scripts/linkedin_ads_optimizer.py --analyze "campaign_id_here"
python3 scripts/linkedin_ads_optimizer.py --optimize-bids "campaign_id_here"
```

### Reporting
```bash
python3 scripts/linkedin_ads_reporter.py --performance-report --format csv
python3 scripts/linkedin_ads_reporter.py --executive-summary
python3 scripts/linkedin_ads_reporter.py --compare-campaigns id1 id2 id3
```

## MCP Integration
This skill implements MCP for AI assistant integration:
- Campaign creation and management
- Real-time analytics
- Budget optimization recommendations
- Automated reporting

## Supported Campaign Types
- Sponsored Content
- Sponsored InMail
- Text Ads
- Dynamic Ads
- Video Ads
- Carousel Ads

## Target Audience Parameters
- Job Titles (specific roles)
- Company Names/Industries
- Company Size
- Seniority Levels
- Skills and Interests
- LinkedIn Groups
- Geographic Location

## Performance Metrics
- Impressions and Reach
- Click-through Rate (CTR)
- Cost Per Click (CPC)
- Conversion Rate
- Cost Per Acquisition (CPA)
- Return on Ad Spend (ROAS)
- Engagement Metrics

## License
MIT License
