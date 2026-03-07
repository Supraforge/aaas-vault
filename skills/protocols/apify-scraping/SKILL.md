---
name: "apify-scraping"
description: "Use Apify actors for advanced web scraping when standard tools are insufficient or blocked, enabling high-volume data extraction and crawling."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["web scraping","data extraction","apify","automation"]
triggers:
  - "when standard scraping tools are blocked"
  - "when high-volume data extraction is needed"
  - "when advanced crawling is required"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "directive"
  original_file: "apify_scraping.md"
---

# Apify Scraping

## When to Use

Standard scraping tools like Tavily/Firecrawl are blocked.,High-volume data extraction is needed.,Deep crawling of websites is required.,YouTube video data and transcripts are needed.,Targeted investors are needed based on industry and stage.

## What This Does

Use Apify actors for advanced web scraping when standard tools are insufficient or blocked, enabling high-volume data extraction and crawling.

## Workflow

Ensure `APIFY_API_TOKEN` is set in Modal secrets or `.env`.,Choose the appropriate Apify actor based on the scraping mode (YouTube Intel, Investor Discovery, General Web Scraping).,Execute the scraping process either via a Modal webhook or a local script.,Pass the required parameters based on the actor's input schema (e.g., keywords, industry, stage).,Monitor the execution and handle any errors.,Process the scraped data as needed.

## Constraints

Ensure `APIFY_API_TOKEN` is configured correctly.,Use `maxResults` to limit consumption and manage costs.,Verify the actor exists and is compatible with the input schema.,Be aware of rate limiting and potential timeouts.
