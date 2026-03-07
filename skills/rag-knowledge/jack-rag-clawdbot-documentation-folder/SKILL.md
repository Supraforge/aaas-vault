---
name: jack-rag-clawdbot-documentation-folder
description: >-
  Sets up a local documentation folder for ClawdBot VPS setup with README,
  SETUP, QUICK-REFERENCE, and SECURITY-NOTES files.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - clawdbot
  - documentation
  - vps
  - setup
  - organization
triggers:
  - setting up clawdbot
  - need to organize clawdbot info
allowed-tools: []
compatibility: none
metadata:
  source: jack-school
  lesson: 130
  lesson_title: ClawdBot gives you Superpowers... lets Unlock them
  difficulty: easy
  category: rag
  tools_required:
    - none
  estimated_setup_time: 5min
---

# Rag Clawdbot Documentation Folder

## When to Use

Use this skill when you need to:
- setting up clawdbot
- need to organize clawdbot info

## What This Does

Sets up a local documentation folder for ClawdBot VPS setup with README, SETUP, QUICK-REFERENCE, and SECURITY-NOTES files.

## Workflow

Please help me set up a local documentation folder for my Clawdbot VPS setup.

Create a folder structure at ~/Desktop/clawdbot/ with the following files:

1. README.md - Main documentation with:
   - Quick start instructions for accessing Clawdbot
   - Server info (VPS provider, IP, SSH key location, port)
   - Links to other documentation files
   - Changes log

2. SETUP.md - Complete setup details:
   - Server information
   - Security architecture
   - Installation history
   - Configuration details

3. QUICK-REFERENCE.md - Day-to-day commands:
   - How to start/stop SSH tunnel
   - VPS management commands
   - Troubleshooting steps
   - Common operations

4. SECURITY-NOTES.md - Security documentation:
   - Security layers explained
   - Monthly security audit checklist
   - Incident response procedures
   - Best practices

Use this information for the files:
- VPS Provider: [YOUR_PROVIDER]
- VPS IP: [YOUR_IP]
- SSH Key Location: ~/.ssh/[YOUR_KEY_NAME]
- Clawdbot Port: 18789
- Access Method: SSH tunnel

Format everything in markdown with clear sections, code blocks, and tables where appropriate.

## Configuration

**Required tools/platforms:**
- none

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
