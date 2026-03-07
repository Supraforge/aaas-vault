---
name: jack-email-lead-magnet-delivery
description: >-
  Sends an email with a link to a lead magnet after a form submission,
  personalizing the message with the lead's name.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - email
  - lead magnet
  - automation
triggers:
  - after a lead fills out a form to receive a lead magnet
  - when you need to automatically deliver a digital asset via email
allowed-tools: []
compatibility: email service provider
metadata:
  source: jack-school
  lesson: 110
  lesson_title: How to Automate UNSTOPPABLE Lead Magnets
  difficulty: easy
  category: email
  tools_required:
    - email service provider
  estimated_setup_time: 5min
---

# Email Lead Magnet Delivery

## When to Use

Use this skill when you need to:
- after a lead fills out a form to receive a lead magnet
- when you need to automatically deliver a digital asset via email

## What This Does

Sends an email with a link to a lead magnet after a form submission, personalizing the message with the lead's name.

## Workflow

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto; padding: 20px;">
    <p>Hey {{4.data.bhp6i.value}} ,</p>
    
    <p>Here's your <a href="[insert URL here]" style="color: #0066cc; text-decoration: none;">lead magnet</a>.</p>
    
    <p>All the best,<br>
    Jack</p>
</body>
</html>

## Configuration

**Required tools/platforms:**
- email service provider

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
