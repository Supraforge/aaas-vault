---
name: "upwork-job-apply"
description: "Scrapes Upwork, generates proposals and cover letters, and creates a Google Sheet with apply links.  Use when targeting freelance gigs."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["upwork","automation","proposal generation","lead generation","freelance"]
triggers:
  - "when I need to quickly apply to Upwork jobs"
  - "when I want to automate Upwork proposal creation"
  - "when I need to scrape and filter Upwork jobs"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "directive"
  original_file: "upwork_scrape_apply.md"
---

# Upwork Job Apply

## When to Use

When you need to find Upwork jobs matching specific keywords.,When you want to automatically generate personalized cover letters and proposals for Upwork jobs.,When you need to create a Google Sheet with job details and one-click apply links.,When you want to quickly apply for multiple Upwork jobs.

## What This Does

Scrapes Upwork, generates proposals and cover letters, and creates a Google Sheet with apply links.  Use when targeting freelance gigs.

## Workflow

Scrape Upwork jobs using the specified keywords, limit, and date range using the `upwork-vibe~upwork-job-scraper` Apify actor.,Filter jobs based on criteria such as verified payment, minimum client spend, and experience level.,Generate personalized cover letters and project proposals for each job using Opus 4.5.,Discover and extract contact names from job descriptions and company research using Opus 4.5 for personalized greetings.,Create a Google Sheet with job details, including apply links, cover letters, and proposal documents.,Apply to jobs via the one-click apply links in the Google Sheet.

## Constraints

Apify free tier limits the available filtering options to `limit`, `fromDate`, and `toDate`.  All other filters are applied post-scrape.,Google API quota limits the number of Google Doc creations per day on the free tier (~100).,Anthropic rate limits might occur when using Opus 4.5, especially with a high number of workers. Reduce the `--workers` parameter if needed.,Ensure sufficient Apify PPE credits are available for the scraper actor (PPE $0/event).,Extended thinking budget is set to 5000 tokens for cover letters and 8000 tokens for proposals.
