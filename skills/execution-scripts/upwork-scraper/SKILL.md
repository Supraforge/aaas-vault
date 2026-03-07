---
name: "upwork-job-scraper"
description: "Scrapes job postings from Upwork based on a search query and saves them to a JSON file. Useful for monitoring specific job categories on Upwork."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["web scraping","upwork","jobs","automation","playwright"]
triggers:
  - "when I need to monitor Upwork for specific job types"
  - "when I want to automate job searching on Upwork"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "upwork_scraper.py"
---

# Upwork Job Scraper

## When to Use

- when I need to monitor Upwork for specific job types
- when I want to automate job searching on Upwork

## What This Does

Scrapes job postings from Upwork based on a search query and saves them to a JSON file. Useful for monitoring specific job categories on Upwork.

## Execution

```bash
python3 <script_name>.py --query <search_query> --pages <num_pages> --output <output_file.json>
```

### Parameters

query: Search query for jobs (default: 'automation'). pages: Number of pages to scrape (default: 1). output: Output JSON file path (optional).

### Dependencies

- python3
- playwright
- beautifulsoup4
