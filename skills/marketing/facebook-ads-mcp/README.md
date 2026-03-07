# Facebook Ads MCP Skill

Automated Facebook Ads management, campaign creation, performance reporting, and optimization through MCP integration.

## Features

- **Campaign Management**: Create, update, pause, and delete Facebook Ads campaigns
- **Performance Reporting**: Generate detailed performance reports with ROI analysis
- **Bid Optimization**: Automated bid adjustments based on performance metrics
- **Audience Analysis**: Demographic and behavioral audience insights
- **A/B Testing**: Automated creative testing and optimization
- **Budget Management**: Smart budget allocation and optimization

## Quick Start

1. Install dependencies:
   ```bash
   ./install.sh
   ```

2. Configure environment:
   ```bash
   cp .env.template .env
   # Edit .env with your Facebook Ads credentials
   ```

3. Test setup:
   ```bash
   ./test.sh
   ```

4. Run a sample command:
   ```bash
   python3 scripts/facebook_ads_manager.py --action list --limit 5
   ```

## API Credentials

You need:
1. Facebook Developer Account
2. Facebook App with ads_management permission
3. Ad Account ID
4. Access Token with ads_read, ads_management permissions

## Usage Examples

### List campaigns
```bash
python3 scripts/facebook_ads_manager.py --action list --limit 10
```

### Create campaign
```bash
python3 scripts/facebook_ads_manager.py --action create --name "Summer Sale" --budget 5000 --objective OUTCOME_CONVERSIONS
```

### Generate performance report
```bash
python3 scripts/facebook_ads_reporter.py --date-range last_30_days --level campaign --export csv
```

### Optimize campaign bids
```bash
python3 scripts/facebook_ads_optimizer.py --campaign-id <CAMPAIGN_ID> --days 7 --analyze-only
```

## License
MIT
