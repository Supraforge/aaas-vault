---
name: "gmaps-lead-pipeline"
description: "Scrapes Google Maps for leads, enriches them with website data, and saves the leads in a Google Sheet."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["lead generation","web scraping","google maps","data enrichment"]
triggers:
  - "when I need to generate leads from Google Maps"
  - "when I want to enrich business data"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "gmaps_lead_pipeline.py"
---

# Gmaps Lead Pipeline

## When to Use

- when I need to generate leads from Google Maps
- when I want to enrich business data

## What This Does

Scrapes Google Maps for leads, enriches them with website data, and saves the leads in a Google Sheet.

## Execution

```bash
python3 execution/gmaps_lead_pipeline.py --search "your search query" --limit 25
```

### Parameters

--search: Google Maps search query (required). --location: Optional location to narrow the search. --limit: Max number of leads to scrape (default: 10). --sheet-url: URL of an existing Google Sheet. If not provided, a new sheet is created.

### Dependencies

- python3
- gspread
- google-auth-httplib2
- google-auth-oauthlib
- beautifulsoup4
- requests
- python-dotenv
