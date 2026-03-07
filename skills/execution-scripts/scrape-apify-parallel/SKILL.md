---
name: "parallel-apify-lead-scrape"
description: "Scrapes leads in parallel using Apify, partitioning by geography to optimize costs and speed. Supports region, metro, and state-level splits. Deduplicates results."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["lead scraping","apify","parallel processing","data extraction","sales"]
triggers:
  - "when I need to quickly scrape leads from Apify"
  - "when I want to scrape leads with geographical partitioning"
  - "when I have a large lead scraping task"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "execution"
  original_file: "scrape_apify_parallel.py"
---

# Parallel Apify Lead Scrape

## When to Use

- when I need to quickly scrape leads from Apify
- when I want to scrape leads with geographical partitioning
- when I have a large lead scraping task

## What This Does

Scrapes leads in parallel using Apify, partitioning by geography to optimize costs and speed. Supports region, metro, and state-level splits. Deduplicates results.

## Execution

```bash
./parallel-apify-lead-scrape.py --query <query> --location <location> --total_count <total_count> [--strategy <strategy>] [--company_keywords <company_keywords>] [--require_email]
```

### Parameters

query (string): The job title or keyword to search for. location (string): The target geographic location ('United States', 'European Union', etc.). total_count (integer): Total leads desired. strategy (string, optional): Partitioning strategy ('regions', 'metros', 'states'). Defaults to 'regions'. company_keywords (string, optional): Company keywords for filtering. require_email (boolean, optional): Whether to require validated email addresses. Defaults to False.

### Dependencies

- python3
- python3-dotenv
- apify-client
- concurrent.futures
