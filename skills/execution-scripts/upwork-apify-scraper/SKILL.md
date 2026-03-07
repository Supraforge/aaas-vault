---
name: "upwork-job-scraper"
description: "Scrapes Upwork job listings using Apify and filters by budget, experience, and keywords. Useful for finding freelance opportunities based on specific criteria."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["upwork","scraper","freelance","apify","jobs"]
triggers:
  - "when I need to find Upwork jobs"
  - "when I want to filter Upwork jobs by budget"
  - "when I am looking for freelance opportunities"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "upwork_apify_scraper.py"
---

# Upwork Job Scraper

## When to Use

- when I need to find Upwork jobs
- when I want to filter Upwork jobs by budget
- when I am looking for freelance opportunities

## What This Does

Scrapes Upwork job listings using Apify and filters by budget, experience, and keywords. Useful for finding freelance opportunities based on specific criteria.

## Execution

```bash
python execution/upwork_apify_scraper.py --limit 50
```

### Parameters

--limit [int] (max jobs to fetch, default 50), --days [int] (jobs from last N days), --from-date [YYYY-MM-DD], --to-date [YYYY-MM-DD], --keyword [str], --min-hourly [float], --max-hourly [float], --min-fixed [float], --max-fixed [float], --experience [str, comma-separated], --verified-payment [bool], --min-spent [float], --min-hires [int], --output [filepath], APIFY_API_TOKEN (required)

### Dependencies

- python3
- requests
- dotenv
- apify-client
