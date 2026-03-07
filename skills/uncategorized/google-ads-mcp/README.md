# Google Ads MCP Skill

## Overview
This skill provides integration with Google Ads API for advertising automation, campaign management, and performance optimization.

## Features
- Campaign creation and management
- Bid optimization and automation
- Performance reporting and analytics
- Budget management
- Conversion tracking
- Audience targeting
- A/B testing setup

## Setup
1. Copy `.env.template` to `.env`
2. Add your Google Ads API credentials
3. Run `./install.sh` to install dependencies
4. Run `./test.sh` to verify setup

## Usage
### Python
```bash
python3 scripts/google_ads_manager.py --list-campaigns
python3 scripts/google_ads_manager.py --report json
python3 scripts/google_ads_manager.py --optimize
```

### Node.js
```bash
cd scripts && npm install
node google_ads_api.js --list-campaigns
node google_ads_api.js --report csv
```

## API Requirements
- Google Ads API access
- OAuth 2.0 credentials
- Developer token
- Customer ID

## License
MIT
