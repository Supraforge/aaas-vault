---
name: lead-generation-automation
description: >-
  Automates lead generation across multiple platforms including LinkedIn, email,
  and CRM systems
version: 1.0.0
dependencies:
  - python3
  - pip
  - curl
inputs:
  - name: target_audience
    description: Target audience description or keywords
  - name: platform
    description: 'Platform to generate leads from (linkedin, email, website)'
  - name: output_format
    description: 'Output format (csv, json, crm_import)'
outputs:
  - type: file
    description: Generated leads in specified format
  - type: stdout
    description: Summary of lead generation results
compatibility: 'agent-zero, claude-code, cursor'
---

# Lead Generation Automation

## 🎯 Triggers
- User needs to generate business leads
- User wants to automate prospecting
- User needs to integrate leads into CRM
- User wants to scale lead generation efforts

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/lead-generation-automation/test.sh`.
- [ ] Check `.env` contains required API keys.
- [ ] Ensure you have necessary platform accounts (LinkedIn, email service, CRM).

## 📋 Workflow
1. **Audience Definition**: Define target audience using keywords, industries, or job titles
2. **Platform Selection**: Choose lead source (LinkedIn, email lists, website forms)
3. **Lead Extraction**: Use APIs or web scraping to extract contact information
4. **Data Enrichment**: Enhance leads with additional data (company info, social profiles)
5. **Validation**: Verify contact information and filter out invalid leads
6. **Export**: Format leads for CRM import or direct use

## 🛠️ Script Reference
- Use `scripts/lead_generator.py` for automated lead generation
- Use `scripts/crm_integration.py` for CRM import/export
- Use `scripts/email_finder.py` for finding email addresses
- Use `scripts/linkedin_scraper.py` for LinkedIn prospecting

## 🔌 Supported Platforms

### LinkedIn Automation
- **Tools**: Sales Navigator, LinkedIn API, browser automation
- **Capabilities**: Profile scraping, connection requests, message automation
- **Limitations**: Respect LinkedIn rate limits and terms of service

### Email Prospecting
- **Tools**: Hunter.io, Clearbit, email verification APIs
- **Capabilities**: Email finding, verification, enrichment
- **Best Practices**: Use verified emails only, respect anti-spam laws

### CRM Integration
- **Supported CRMs**: Salesforce, HubSpot, Pipedrive, Zoho
- **Capabilities**: Lead import/export, field mapping, automation triggers

### Website Lead Capture
- **Tools**: Form builders, analytics, tracking pixels
- **Capabilities**: Visitor tracking, form submission capture, lead scoring

## ⚠️ Compliance & Best Practices
1. **GDPR/CCPA Compliance**: Ensure proper consent for data collection
2. **Anti-Spam Laws**: Follow CAN-SPAM, CASL regulations
3. **Platform Terms**: Respect LinkedIn, Google, and other platform terms
4. **Data Privacy**: Securely store and handle personal information
5. **Ethical Sourcing**: Focus on quality over quantity, build relationships

## 📊 Performance Metrics
- **Lead Quality Score**: Based on engagement and conversion potential
- **Conversion Rate**: Percentage of leads that become customers
- **Cost Per Lead**: Total cost divided by number of qualified leads
- **Time to Conversion**: Average time from lead capture to conversion

## 🔄 Continuous Improvement
1. **A/B Testing**: Test different messaging and targeting approaches
2. **Feedback Loop**: Incorporate sales team feedback on lead quality
3. **Tool Optimization**: Regularly update and optimize automation tools
4. **Market Adaptation**: Adjust strategies based on market changes
