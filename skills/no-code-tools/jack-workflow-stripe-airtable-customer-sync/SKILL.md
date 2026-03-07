---
name: jack-workflow-stripe-airtable-customer-sync
description: >-
  Automates syncing new Stripe customers to an Airtable database using Make.com,
  triggering on Stripe events and updating Airtable records.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - stripe
  - airtable
  - make.com
  - automation
  - crm
triggers:
  - When a new customer subscribes through Stripe.
  - When you need to automatically update customer info in Airtable.
allowed-tools: []
compatibility: 'make.com, stripe, airtable'
metadata:
  source: jack-school
  lesson: 47
  lesson_title: Tools
  difficulty: medium
  category: nocode
  tools_required:
    - make.com
    - stripe
    - airtable
  estimated_setup_time: 30min
  extracted_from:
    - Stripe Customer Creation 2_3.json
    - API Email scenario 3_3.json
---

# Workflow Stripe Airtable Customer Sync

## When to Use

Use this skill when you need to:
- When a new customer subscribes through Stripe.
- When you need to automatically update customer info in Airtable.

## What This Does

Automates syncing new Stripe customers to an Airtable database using Make.com, triggering on Stripe events and updating Airtable records.

## Workflow

Stripe Customer Creation 2/3.json and API Email scenario 3_3.json are the related files.

## Configuration

**Required tools/platforms:**
- make.com
- stripe
- airtable

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
