---
name: "apify-leads-scraper"
description: "Scrapes leads using Apify's leads-finder actor based on a query, location, and optional filters. Saves results to a JSON file."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["web scraping","lead generation","Apify","data extraction"]
triggers:
  - "when I need to find leads for a specific query in a location"
  - "when I want to scrape contact information from the web using Apify"
  - "when I need to generate a list of leads with job titles or company keywords"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "scrape_apify.py"
---

# Apify Leads Scraper

## When to Use

- when I need to find leads for a specific query in a location
- when I want to scrape contact information from the web using Apify
- when I need to generate a list of leads with job titles or company keywords

## What This Does

Scrapes leads using Apify's leads-finder actor based on a query, location, and optional filters. Saves results to a JSON file.

## Execution

```bash
apify-leads-scraper.py --query <query> --location <location> [--max_items <max_items>] [--output_prefix <output_prefix>] [--job_titles <job_titles>] [--company_keywords <company_keywords>] [--no-email-filter]
```

### Parameters

query (string, required): Search query (e.g., 'Plumbers').
location (string, required): Location (e.g., 'New York').
max_items (integer, optional): Maximum number of items to scrape (default: 25).
output_prefix (string, optional): Prefix for the output file (default: 'leads').
job_titles (list of strings, optional): Specific job titles to target (e.g., 'CEO' 'Founder').
company_keywords (list of strings, optional): Company keywords to filter (e.g., 'software' 'SaaS').
no-email-filter (boolean, optional): Don't filter by validated emails (faster, larger results). APIFY_API_TOKEN environment variable is required.

### Dependencies

- python3
- python3-dotenv
- apify-client
- os
- sys
- json
- argparse
- datetime
