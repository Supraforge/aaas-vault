---
name: jack-nocode-troubleshoot-clawdbot-tunnel
description: Provides troubleshooting steps for common ClawdBot SSH tunnel issues.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - troubleshooting
  - ssh
  - tunnel
  - clawdbot
  - vps
triggers:
  - clawdbot not working
  - ssh tunnel issues
allowed-tools: []
compatibility: 'terminal, ssh'
metadata:
  source: jack-school
  lesson: 130
  lesson_title: ClawdBot gives you Superpowers... lets Unlock them
  difficulty: medium
  category: nocode
  tools_required:
    - terminal
    - ssh
  estimated_setup_time: 15min
---

# Nocode Troubleshoot Clawdbot Tunnel

## When to Use

Use this skill when you need to:
- clawdbot not working
- ssh tunnel issues

## What This Does

Provides troubleshooting steps for common ClawdBot SSH tunnel issues.

## Workflow

**Dashboard won't load?** Check if the tunnel is running: `lsof -i :18789`. If you see output, tunnel is running. If no output, tunnel is not running (run the ssh command again).

**Port already in use?** Find the process: `lsof -i :18789`. Kill it (replace PID): `kill PID`. Start fresh tunnel.

**Can't connect to VPS?** Check if Clawdbot is running on the VPS: `ssh -i ~/.ssh/YOUR_KEY_NAME root@YOUR_VPS_IP "systemctl status clawdbot"`. If it's not running, start it: `ssh -i ~/.ssh/YOUR_KEY_NAME root@YOUR_VPS_IP "systemctl start clawdbot"`.

## Configuration

**Required tools/platforms:**
- terminal
- ssh

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
