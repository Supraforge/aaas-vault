---
name: jack-nocode-security-reminder-clawdbot
description: >-
  Lists security reminders for ClawdBot setup: never expose port 18789, secure
  SSH key, use token in URLs, monthly security audit, enable 2FA.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - security
  - clawdbot
  - vps
  - ssh
  - best practices
triggers:
  - securing clawdbot
  - clawdbot best practices
allowed-tools: []
compatibility: none
metadata:
  source: jack-school
  lesson: 130
  lesson_title: ClawdBot gives you Superpowers... lets Unlock them
  difficulty: easy
  category: nocode
  tools_required:
    - none
  estimated_setup_time: 5min
---

# Nocode Security Reminder Clawdbot

## When to Use

Use this skill when you need to:
- securing clawdbot
- clawdbot best practices

## What This Does

Lists security reminders for ClawdBot setup: never expose port 18789, secure SSH key, use token in URLs, monthly security audit, enable 2FA.

## Workflow

- Never expose port 18789 to the internet - Always use SSH tunnel
- Keep your SSH key secure - Don't share or commit to git
- Use the token in URLs - This authenticates you to Clawdbot
- Monthly security audit - Check your VPS firewall settings
- Enable 2FA on VPS provider - Protect your hosting account

## Configuration

**Required tools/platforms:**
- none

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
