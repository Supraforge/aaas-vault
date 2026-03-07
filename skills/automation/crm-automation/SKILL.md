---
name: crm-automation
description: >-
  Automates customer relationship management across multiple CRM platforms with
  lead tracking, sales pipeline management, and automated follow-ups
version: 1.0.0
dependencies:
  - python3
  - pip
  - curl
  - jq
inputs:
  - name: crm_platform
    description: 'CRM platform to use (hubspot, salesforce, zoho, freshworks, pipedrive)'
  - name: operation
    description: >-
      Operation to perform (sync_contacts, create_lead, update_pipeline,
      send_followup, generate_report)
  - name: data_file
    description: Path to JSON/CSV file containing contact or lead data
outputs:
  - type: file
    description: CRM operation results and analytics report
  - type: stdout
    description: Status updates and error messages
compatibility: 'agent-zero, claude-code, cursor'
---

# CRM Automation Skill

## 🎯 Triggers
- "Sync my contacts with HubSpot"
- "Create a new lead in Salesforce"
- "Update sales pipeline status"
- "Send automated follow-up emails"
- "Generate CRM analytics report"

## ⚡ Quick Start (Self-Check)
Before running CRM automation:
- [ ] Run `bash ~/.gemini/skills/crm-automation/test.sh`
- [ ] Check `.env` contains required API keys for your CRM platforms
- [ ] Verify you have proper CRM API access permissions

## 📋 Workflow

### 1. Platform Selection & Authentication
- Detect which CRM platform to use
- Load appropriate API credentials from `.env`
- Test connection to CRM API

### 2. Data Preparation
- Parse input data (CSV, JSON, or manual entry)
- Validate contact/lead information
- Format data according to CRM API requirements

### 3. Operation Execution
- **Contact Sync**: Import/export contacts between systems
- **Lead Creation**: Create new leads with scoring and assignment
- **Pipeline Management**: Update deal stages and values
- **Follow-up Automation**: Schedule and send personalized emails
- **Reporting**: Generate sales metrics and performance analytics

### 4. Verification & Error Handling
- Confirm successful operations
- Log errors and retry failed operations
- Generate summary report

## 🛠️ Script Reference

### Main Scripts:
- `scripts/crm_manager.py` - Main CRM orchestration script
- `scripts/hubspot_integration.py` - HubSpot API integration
- `scripts/salesforce_integration.py` - Salesforce API integration
- `scripts/data_processor.py` - Data formatting and validation
- `scripts/report_generator.py` - Analytics and reporting

### Utility Scripts:
- `scripts/auth_tester.py` - Test CRM API connections
- `scripts/backup_contacts.py` - Backup CRM data locally
- `scripts/migration_tool.py` - Migrate between CRM platforms

## 🔧 Configuration

### Supported CRM Platforms:
1. **HubSpot** - Marketing-focused CRM with strong automation
2. **Salesforce** - Enterprise sales and service platform
3. **Zoho CRM** - Affordable all-in-one solution
4. **Freshworks** - User-friendly sales automation
5. **Pipedrive** - Visual pipeline management
6. **Nimble** - Social CRM with relationship intelligence

### API Rate Limits & Best Practices:
- Respect API rate limits (typically 100-1000 calls/minute)
- Implement exponential backoff for retries
- Cache frequently accessed data
- Use webhooks for real-time updates when available

## 📊 Data Models

### Contact Schema:
```json
{
  "email": "required",
  "first_name": "optional",
  "last_name": "optional",
  "company": "optional",
  "phone": "optional",
  "tags": ["lead", "customer", "prospect"],
  "custom_fields": {}
}
```

### Lead Schema:
```json
{
  "source": "website",
  "status": "new",
  "score": 85,
  "owner": "sales_team",
  "expected_value": 5000,
  "timeline": {
    "created": "2025-01-20",
    "next_followup": "2025-01-25"
  }
}
```

## 🔄 Automation Rules

### Lead Scoring Rules:
- +10 points for company email domain
- +20 points for job title containing "director" or "manager"
- +15 points for company size > 100 employees
- +25 points for previous engagement (email opens, website visits)

### Follow-up Triggers:
- New lead created → Send welcome email within 1 hour
- Lead score > 75 → Assign to sales team immediately
- No response in 3 days → Send follow-up email
- Deal stage changed → Notify account manager

## 📈 Reporting & Analytics

### Key Metrics Tracked:
- Lead conversion rate
- Sales pipeline velocity
- Customer acquisition cost
- Customer lifetime value
- Email engagement rates
- Team performance metrics

### Automated Reports:
- Daily sales summary
- Weekly pipeline review
- Monthly performance dashboard
- Quarterly trend analysis

## 🚨 Error Handling

### Common Issues:
1. **API Authentication Failures** - Check token expiration
2. **Rate Limit Exceeded** - Implement backoff and retry
3. **Data Validation Errors** - Clean input data before sending
4. **Network Timeouts** - Increase timeout settings

### Recovery Procedures:
- Log detailed error information
- Retry with exponential backoff
- Fallback to alternative endpoints
- Notify administrators of persistent issues

## 🔐 Security Considerations

### Data Protection:
- Encrypt sensitive contact information
- Secure API keys in environment variables
- Implement access controls for different user roles
- Regular security audits of integration points

### Compliance:
- GDPR compliance for EU contacts
- CCPA compliance for California residents
- Industry-specific regulations (HIPAA, FINRA)
- Data retention and deletion policies

## 🧪 Testing

### Test Scenarios:
1. **Unit Tests** - Individual function testing
2. **Integration Tests** - CRM API connection testing
3. **End-to-End Tests** - Complete workflow testing
4. **Load Tests** - Performance under high volume

### Test Data:
- Use sandbox/test environments when available
- Create mock CRM responses for development
- Test with sample datasets of various sizes

## 📚 Resources

### Documentation:
- [HubSpot API Docs](https://developers.hubspot.com/docs/api/overview)
- [Salesforce REST API Guide](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/)
- [Zoho CRM API](https://www.zoho.com/crm/developer/docs/api/v2/)

### Community & Support:
- CRM platform developer forums
- Stack Overflow tags for each platform
- Official platform support channels

---

*Last Updated: 2025-01-20*
*Version: 1.0.0*
