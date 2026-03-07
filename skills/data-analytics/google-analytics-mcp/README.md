# Google Analytics MCP

Enterprise-grade web analytics automation for business growth and marketing optimization.

## Features

### 📊 Comprehensive Analytics
- GA4 and Universal Analytics support
- Real-time and historical data
- Custom dimensions and metrics
- Multi-channel attribution

### 🤖 Automation Capabilities
- Scheduled reporting
- Automated insights generation
- Data export to CSV/JSON
- Integration with other MCP skills

### 🛠️ Dual Implementation
- Python implementation with pandas for data analysis
- Node.js implementation for JavaScript ecosystems
- Bash scripts for automation workflows

## Quick Start

1. **Setup Google Cloud Project**
   - Enable Google Analytics API
   - Create OAuth 2.0 credentials
   - Add authorized redirect URIs

2. **Configure Skill**
   ```bash
   cd ~/.gemini/skills/google-analytics-mcp
   cp .env.template .env
   # Edit .env with your credentials
   ```

3. **Install Dependencies**
   ```bash
   ./install.sh
   ```

4. **Authenticate**
   ```bash
   python3 scripts/python/analytics.py
   # Follow OAuth flow
   ```

5. **Run Tests**
   ```bash
   ./test.sh
   ```

## Use Cases

### Marketing Optimization
- Track campaign performance
- Analyze traffic sources
- Measure conversion rates
- Optimize ad spend

### Content Strategy
- Identify top-performing content
- Analyze user engagement
- Track bounce rates
- Measure time on page

### Business Intelligence
- User behavior analysis
- Demographic insights
- Geographic performance
- Device usage patterns

### E-commerce Analytics
- Sales funnel analysis
- Product performance
- Shopping behavior
- Revenue attribution

## Integration Examples

### With Mailchimp MCP
```bash
# Analyze email campaign traffic
# Export to Mailchimp for segmentation
```

### With Salesforce MCP
```bash
# Sync lead conversion data
# Update CRM with web analytics
```

### With Slack MCP
```bash
# Send daily analytics reports
# Alert on traffic anomalies
```

## API Coverage

- Google Analytics Data API (GA4)
- Google Analytics Reporting API (v4)
- Google Analytics Admin API
- Real-time Reporting API
- Management API

## Support

For issues or questions:
1. Check the test.sh output
2. Verify Google Cloud API permissions
3. Ensure OAuth credentials are valid
4. Check network connectivity to Google APIs

## License

MIT License - See included LICENSE file
