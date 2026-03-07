---
name: "lead-scraping-and-verification"
description: "Scrapes leads, verifies industry relevance, and saves to a Google Sheet, using parallel scraping for large datasets when appropriate."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["lead generation","data scraping","google sheets","apify"]
triggers:
  - "when I need to scrape leads and save them to Google Sheets"
  - "when the user asks me to find leads in a specific industry"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "directive"
  original_file: "scrape_leads.md"
---

# Lead Scraping And Verification

## When to Use

When the user provides an industry and location for lead generation.,When the desired number of leads is known.,When the task requires verifying lead relevance (industry match).

## What This Does

Scrapes leads, verifies industry relevance, and saves to a Google Sheet, using parallel scraping for large datasets when appropriate.

## Workflow

Determine if a small scrape (<1000 leads) or large scrape (1000+ leads) is needed based on the total count.,For small scrapes: Test scrape with `max_items=25`, verify industry match > 80%. If it fails, ask user to refine search terms. Proceed to full scrape, upload to Google Sheet, and enrich emails.,For large scrapes: Test scrape with `max_items=25`, verify industry match > 80%. If it fails, ask user to refine search terms. Proceed to parallel full scrape, upload to Google Sheet, and enrich emails.,Optionally use LLM classification for complex industry distinctions when simple keyword matching isn't sufficient.,Always enrich missing emails in the google sheet and return the URL as the ONLY deliverable.,Handle potential errors such as no leads found, API errors, or low-quality classifications.

## Constraints

The final deliverable is ALWAYS a Google Sheet URL.,Use parallel scraping (`scrape_apify_parallel.py`) when Total Count exceeds 1000 leads.,The APIFY_API_TOKEN and GOOGLE_APPLICATION_CREDENTIALS must be correctly configured.,Always enrich emails after scraping.
