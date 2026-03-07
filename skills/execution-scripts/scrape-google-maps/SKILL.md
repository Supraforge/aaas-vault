---
name: "google-maps-scraper"
description: "Scrapes business listings from Google Maps using Apify, useful for lead generation and market research."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["google maps","scraper","apify","lead generation","business data"]
triggers:
  - "when I need to extract business data from Google Maps"
  - "when I want to generate leads based on location and keywords"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "scrape_google_maps.py"
---

# Google Maps Scraper

## When to Use

- when I need to extract business data from Google Maps
- when I want to generate leads based on location and keywords

## What This Does

Scrapes business listings from Google Maps using Apify, useful for lead generation and market research.

## Execution

```bash
python3 execution/scrape_google_maps.py --search 'your search query' --limit 20
```

### Parameters

--search (required): Search query (e.g., 'plumbers in Austin TX').  --limit (optional): Maximum number of results (default: 10).  --location (optional): Location to focus search.  --language (optional): Language code (default: en).  --output (optional): Output file prefix (default: gmaps).  --json (optional): Output results as JSON to stdout.  APIFY_API_TOKEN environment variable must be set.

### Dependencies

- python3
- apify-client
- python-dotenv
