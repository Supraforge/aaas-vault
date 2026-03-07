---
name: jack-nocode-ssh-tunnel-clawdbot
description: >-
  Provides step-by-step instructions on how to create an SSH tunnel to access a
  ClawdBot dashboard running on a VPS.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - ssh
  - tunnel
  - clawdbot
  - vps
  - access
  - security
triggers:
  - accessing clawdbot
  - connecting to vps dashboard
allowed-tools: []
compatibility: 'terminal, ssh'
metadata:
  source: jack-school
  lesson: 130
  lesson_title: ClawdBot gives you Superpowers... lets Unlock them
  difficulty: easy
  category: nocode
  tools_required:
    - terminal
    - ssh
  estimated_setup_time: 5min
---

# Nocode Ssh Tunnel Clawdbot

## When to Use

Use this skill when you need to:
- accessing clawdbot
- connecting to vps dashboard

## What This Does

Provides step-by-step instructions on how to create an SSH tunnel to access a ClawdBot dashboard running on a VPS.

## Workflow

1. Open Terminal.
2. Start the tunnel: `ssh -i ~/.ssh/YOUR_KEY_NAME -L 18789:127.0.0.1:18789 root@YOUR_VPS_IP -N -f`
3. Open browser: `http://localhost:18789/?token=YOUR_TOKEN`
4. Start using Clawdbot!

## Configuration

**Required tools/platforms:**
- terminal
- ssh

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
