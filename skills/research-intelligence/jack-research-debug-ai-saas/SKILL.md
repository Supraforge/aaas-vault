---
name: jack-research-debug-ai-saas
description: >-
  Provides a structured approach to debugging issues in an AI SaaS built with
  Lovable, n8n, and Stripe.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - debugging
  - ai saas
  - lovable
  - n8n
  - stripe
triggers:
  - when encountering errors in your AI SaaS application
  - 'when needing to troubleshoot integrations between Lovable, n8n, and Stripe'
allowed-tools: []
compatibility: 'lovable, n8n, stripe'
metadata:
  source: jack-school
  lesson: 80
  lesson_title: Tools
  difficulty: medium
  category: research
  tools_required:
    - lovable
    - n8n
    - stripe
  estimated_setup_time: 15min
---

# Research Debug Ai Saas

## When to Use

Use this skill when you need to:
- when encountering errors in your AI SaaS application
- when needing to troubleshoot integrations between Lovable, n8n, and Stripe

## What This Does

Provides a structured approach to debugging issues in an AI SaaS built with Lovable, n8n, and Stripe.

## Workflow

1. **Identify the Issue Location:** Pinpoint the exact component (Lovable, n8n, Stripe, Supabase) where the problem occurs.
2. **Document the Problem:** Record a short Loom video or take screenshots showing the issue and configuration.
3. **Efficient Question Structure:**
   * Start with a one-sentence summary of the problem.
   * List the troubleshooting steps already attempted.
   * Include complete error messages (copy/paste).
4. **Example Questions:** "My Stripe payment integration shows 'Failed to create checkout session'...".

## Configuration

**Required tools/platforms:**
- lovable
- n8n
- stripe

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
