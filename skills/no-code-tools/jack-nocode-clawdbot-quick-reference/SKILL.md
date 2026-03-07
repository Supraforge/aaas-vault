---
name: jack-nocode-clawdbot-quick-reference
description: Provides a quick reference card with essential commands for managing ClawdBot.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - quick reference
  - clawdbot
  - vps
  - commands
  - cheat sheet
triggers:
  - need clawdbot commands
  - managing clawdbot
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

# Nocode Clawdbot Quick Reference

## When to Use

Use this skill when you need to:
- need clawdbot commands
- managing clawdbot

## What This Does

Provides a quick reference card with essential commands for managing ClawdBot.

## Workflow

### Start Tunnel
```bash
ssh -i ~/.ssh/YOUR_KEY -L 18789:127.0.0.1:18789 root@YOUR_IP -N -f
```

### Check Tunnel
```bash
lsof -i :18789
```

### Stop Tunnel
```bash
kill $(lsof -t -i:18789)
```

### Dashboard URL
```
http://localhost:18789/?token=YOUR_TOKEN
```

### Check Clawdbot Status
```bash
ssh -i ~/.ssh/YOUR_KEY root@YOUR_IP "systemctl status clawdbot"
```

### Restart Clawdbot
```bash
ssh -i ~/.ssh/YOUR_KEY root@YOUR_IP "systemctl restart clawdbot"
```

## Configuration

**Required tools/platforms:**
- none

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
