---
name: business-intelligence-automation
description: >-
  Automates business intelligence workflows across multiple BI platforms with
  data visualization, dashboard creation, and automated reporting
version: 1.0.0
dependencies:
  - python3
  - pip
  - jq
  - curl
inputs:
  - name: data_source
    description: 'Path to data source file (CSV, JSON, Excel) or database connection string'
  - name: report_type
    description: 'Type of report to generate (sales, marketing, financial, operational)'
  - name: output_format
    description: 'Output format (pdf, html, excel, powerpoint)'
outputs:
  - type: file
    description: Generated BI report or dashboard
  - type: stdout
    description: Analysis summary and insights
compatibility: 'agent-zero, claude-code, cursor'
---

# Business Intelligence Automation

## 🎯 Triggers
- "Create a sales dashboard from our Q3 data"
- "Generate automated marketing analytics report"
- "Set up weekly financial reporting automation"
- "Visualize customer behavior patterns from our database"

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/business-intelligence-automation/test.sh`.
- [ ] Check `.env` contains required API keys for BI platforms.
- [ ] Ensure data sources are accessible (CSV files, database connections).

## 📋 Workflow
1. **Data Ingestion**: Connect to data sources (CSV, JSON, Excel, SQL databases)
2. **Data Transformation**: Clean, normalize, and prepare data for analysis
3. **Analysis & Visualization**: Apply statistical analysis and create visualizations
4. **Dashboard Creation**: Build interactive dashboards for different BI platforms
5. **Automated Reporting**: Schedule and distribute reports to stakeholders
6. **Insight Generation**: Extract actionable insights from data patterns

## 🛠️ Script Reference
- Use `scripts/bi_manager.py` for main BI automation workflows
- Use `scripts/data_processor.py` for data cleaning and transformation
- Use `scripts/report_generator.py` for automated report generation
- Use `scripts/dashboard_builder.py` for creating interactive dashboards

## 🔌 Supported BI Platforms
- **Microsoft Power BI**: REST API integration for datasets and reports
- **Tableau**: Tableau Server REST API for workbook management
- **Qlik Sense**: Qlik Sense APIs for app management and data loading
- **Zoho Analytics**: Zoho Analytics API for reports and dashboards
- **Google Data Studio**: Data source configuration and report automation
- **Looker Studio**: Looker API for exploring and managing content

## 📊 Data Source Support
- CSV/Excel files
- JSON data
- SQL databases (PostgreSQL, MySQL, SQL Server)
- REST APIs
- Cloud storage (Google Drive, Dropbox, S3)

## 🔄 Automation Features
- **Scheduled Reporting**: Cron-based report generation and distribution
- **Real-time Dashboards**: Live data updates and refresh automation
- **Alert System**: Threshold-based alerts for key metrics
- **Data Pipeline**: End-to-end data processing automation
- **Multi-tenant Support**: Manage multiple client BI environments

## 📈 Use Cases
1. **Sales Analytics**: Track sales performance, pipeline health, and forecasting
2. **Marketing ROI**: Measure campaign effectiveness and attribution
3. **Financial Reporting**: Automated P&L, balance sheets, and cash flow
4. **Operational Metrics**: Monitor KPIs for operations and supply chain
5. **Customer Analytics**: Customer segmentation, churn prediction, LTV

## 🚀 Getting Started
1. Install dependencies: `bash install.sh`
2. Configure API keys in `.env` file
3. Test connection: `bash test.sh`
4. Run sample: `python scripts/bi_manager.py --sample`
5. Customize templates for your specific use case

## 📝 Notes
- This skill requires API access to respective BI platforms
- Data privacy and compliance should be considered when handling sensitive data
- Large datasets may require optimization for performance
- Regular maintenance of API keys and connections is recommended
