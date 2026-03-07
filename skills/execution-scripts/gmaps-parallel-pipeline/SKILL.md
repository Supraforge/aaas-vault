---
name: "gmaps-lead-pipeline"
description: "Scrapes Google Maps for business leads, extracts contact info, and saves them incrementally to a Google Sheet."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["google maps","lead generation","web scraping","data enrichment","google sheets"]
triggers:
  - "when I need to scrape Google Maps for leads"
  - "when I want to incrementally save leads to a Google Sheet"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "gmaps_parallel_pipeline.py"
---

# Gmaps Lead Pipeline

## When to Use

- when I need to scrape Google Maps for leads
- when I want to incrementally save leads to a Google Sheet

## What This Does

Scrapes Google Maps for business leads, extracts contact info, and saves them incrementally to a Google Sheet.

## Execution

```bash
gmaps-lead-pipeline.py --search <search_query> [--limit <max_results>] [--location <location>] [--sheet-url <sheet_url>] [--sheet-name <sheet_name>] [--workers <num_workers>]
```

### Parameters

--search: The Google Maps search query (required)
--limit: Max results to scrape (default: 100)
--location: Location to filter search results
--sheet-url: URL of an existing Google Sheet
--sheet-name: Name for a new Google Sheet
--workers: Number of parallel workers (default: 10)

Requires GOOGLE_API_KEY and GOOGLE_SHEET_ID or GOOGLE_CREDENTIALS environment variables.

### Dependencies

- Python 3
- google-api-python-client
- google-auth-httplib2
- google-auth-oauthlib
- requests
- beautifulsoup4
- python-dotenv
