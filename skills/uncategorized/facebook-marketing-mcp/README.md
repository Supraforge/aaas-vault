# Facebook Marketing API MCP Skill

This skill provides MCP (Model Context Protocol) integration with Facebook Marketing API for automated advertising, audience management, and performance analytics.

## Features

### Campaign Management
- Create, update, pause, and delete ad campaigns
- Automated budget allocation and optimization
- A/B testing setup and analysis

### Audience Management
- Custom audience creation from CRM data
- Lookalike audience generation
- Audience insights and segmentation

### Creative Management
- Ad creative upload and management
- Dynamic creative optimization
- Creative performance analytics

### Analytics & Reporting
- Real-time performance monitoring
- ROAS (Return on Ad Spend) calculation
- Automated reporting and alerts

### Automation
- Rule-based campaign optimization
- Budget pacing and alerts
- Performance-based audience expansion

## Business Use Cases

### E-commerce
- Dynamic product ads
- Retargeting campaigns
- Abandoned cart recovery

### Lead Generation
- Form ads and lead capture
- Lead quality scoring
- CRM integration

### Brand Awareness
- Reach and frequency campaigns
- Brand lift measurement
- Competitor analysis

### App Promotion
- App install campaigns
- App engagement ads
- App event optimization

## Getting Started

1. **Set up Facebook App**: Create app at https://developers.facebook.com/apps/
2. **Get API Credentials**: Obtain App ID, App Secret, and Access Token
3. **Configure .env**: Copy .env.template to .env and add credentials
4. **Install Dependencies**: Run `bash install.sh`
5. **Test Installation**: Run `bash test.sh`
6. **Start MCP Server**: Run `npm start`
7. **Connect Client**: Use any MCP-compatible client to connect

## API Rate Limits

Facebook Marketing API has rate limits:
- 200 calls per hour per user
- 50 concurrent requests
- Implement retry logic with exponential backoff

## Security Best Practices

- Store credentials in .env (never commit to version control)
- Use long-lived access tokens with appropriate permissions
- Implement token rotation
- Monitor API usage and errors
- Regular security audits

## Support

For issues and questions:
- Check Facebook Marketing API documentation
- Review skill logs in `logs/` directory
- Test with `bash test.sh` for diagnostics

## License

MIT License - See LICENSE file for details
