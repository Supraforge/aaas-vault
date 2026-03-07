# Salesforce MCP Skill

Enterprise CRM automation with Salesforce API integration.

## Features

### Core CRM Operations
- Lead management (create, update, qualify)
- Opportunity tracking and pipeline management
- Contact and account synchronization
- Sales forecasting and reporting

### Business Intelligence
- Sales velocity calculation
- Conversion rate analysis
- Forecast accuracy tracking
- Executive dashboard generation

### Integration Capabilities
- Sync with marketing platforms (Mailchimp, HubSpot)
- CSV import/export for data migration
- Real-time pipeline monitoring
- Automated workflow triggers

## Quick Start

1. **Install dependencies**:
   ```bash
   bash install.sh
   ```

2. **Configure credentials**:
   ```bash
   cp .env.template .env
   # Edit .env with your Salesforce credentials
   ```

3. **Test connection**:
   ```bash
   python3 scripts/salesforce_operations.py --test
   ```

4. **Get sales pipeline**:
   ```bash
   python3 scripts/salesforce_operations.py --pipeline
   ```

## API Reference

### Python Scripts
- `salesforce_operations.py` - Core CRM operations
- `salesforce_analytics.py` - Business intelligence
- `salesforce_sync.py` - Data synchronization

### Node.js MCP Server
- `nodejs/server.js` - MCP protocol implementation
- Tools: get_sales_pipeline, create_lead, update_opportunity, get_sales_analytics

## Use Cases

### Sales Teams
- Real-time pipeline visibility
- Automated lead qualification
- Forecast reporting
- Territory management

### Marketing Teams
- Lead synchronization
- Campaign performance tracking
- Customer segmentation
- ROI analysis

### Executives
- Executive dashboards
- KPI tracking
- Revenue forecasting
- Performance analytics

## Security Notes

- Store credentials in `.env` file (never commit to version control)
- Use Salesforce Connected App with appropriate permissions
- Implement OAuth 2.0 for production deployments
- Regularly rotate API credentials
