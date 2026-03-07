---
name: "google-serp-lead-scraper"
description: "Scrapes Google search results for local businesses, extracts contact info, and stores structured leads in Google Sheets. Useful for lead generation."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["lead generation","web scraping","local business","google serp","contact extraction"]
triggers:
  - "when building lead lists"
  - "when prospecting for local businesses"
  - "when populating CRM with enriched data"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "directive"
  original_file: "google_serp_lead_scraper.md"
---

# Google Serp Lead Scraper

## When to Use

Building lead lists for local service businesses,Prospecting for outreach campaigns targeting specific geographic areas,Populating CRM with enriched contact data

## What This Does

Scrapes Google search results for local businesses, extracts contact info, and stores structured leads in Google Sheets. Useful for lead generation.

## Workflow

Apify's `google-search-scraper` scrapes Google SERP using a hardcoded query.,Results are limited to a test set of 2; remove the Limit node for full runs.,Each result URL is fetched and converted to markdown.,GPT-5 extracts 100+ fields (company info, emails, phones, social profiles, etc.).,Data is appended to the Google Sheets database.

## Constraints

Hardcoded query: Currently set to 'calgary plumber'.,Test limit: Only processes 2 results by default.,No deduplication: Repeated runs may create duplicates.,Apify rate limits: Large batches may require pagination or scheduling.
