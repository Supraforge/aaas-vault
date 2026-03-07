---
name: jack-social-instagram-scraper
description: >-
  Scrape Instagram profiles to gather engagement metrics (likes, comments,
  views, etc.) and store in Airtable or Google Sheets.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - instagram
  - scraping
  - data analysis
  - social media marketing
  - n8n
  - apify
  - airtable
triggers:
  - Need to track engagement metrics on Instagram profiles
  - Want to analyze competitor strategies on Instagram
allowed-tools: []
compatibility: 'n8n, Apify, Airtable'
metadata:
  source: jack-school
  lesson: 104
  lesson_title: Tools
  difficulty: medium
  category: social
  tools_required:
    - n8n
    - Apify
    - Airtable
  estimated_setup_time: 30min
---

# Social Instagram Scraper

## When to Use

Use this skill when you need to:
- Need to track engagement metrics on Instagram profiles
- Want to analyze competitor strategies on Instagram

## What This Does

Scrape Instagram profiles to gather engagement metrics (likes, comments, views, etc.) and store in Airtable or Google Sheets.

## Workflow

1. Upload provided n8n blueprint.
2. Create an Apify account and grab API key.
3. Configure Apify API key in the 'Scrape' node in n8n.
4. Configure Airtable (or Google Sheets) with API key and create a base copy.
5. Create a list of Instagram profiles to track.
6. Update the 'Instagram Accounts' node with profile URLs.

## Configuration

**Required tools/platforms:**
- n8n
- Apify
- Airtable

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
