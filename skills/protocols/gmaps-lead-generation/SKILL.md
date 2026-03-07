---
name: "google-maps-lead-gen"
description: "Generate and enrich B2B leads from Google Maps by scraping websites and using Claude to extract contact data, then deduplicate and save leads."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["lead generation","scraping","google maps","enrichment","claude"]
triggers:
  - "when I need to generate leads for local service businesses"
  - "when I want to research businesses in a specific geographic area"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "directive"
  original_file: "gmaps_lead_generation.md"
---

# Google Maps Lead Gen

## When to Use

Building outbound sales lists for local service businesses,Generating leads for B2B services (contractors, medical, legal, etc.),Researching businesses in a specific geographic area,Creating prospecting lists with verified contact info

## What This Does

Generate and enrich B2B leads from Google Maps by scraping websites and using Claude to extract contact data, then deduplicate and save leads.

## Workflow

Scrape Google Maps for business listings using the specified search query and limit.,For each business, scrape the website (main page and up to 5 contact pages).,Enrich the business information by searching DuckDuckGo for additional contact details.,Extract structured contact data from all sources using Claude.,Deduplicate leads based on lead_id (MD5 hash of name|address).,Append new leads to a Google Sheet, either creating a new sheet or appending to an existing one.

## Constraints

Requires a valid Apify API token.,Google Sheet credentials (credentials.json) must be valid.,Input search query must be valid and include location for best results.,Some websites may block scrapers with 403/503 errors; these leads will still be saved with Google Maps data.,Ensure the .env file has the APIFY_API_TOKEN defined.
