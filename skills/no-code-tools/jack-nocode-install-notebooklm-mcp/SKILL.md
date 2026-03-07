---
name: jack-nocode-install-notebooklm-mcp
description: >-
  Provides a prompt to install and setup the NotebookLM MCP server using
  AntiGravity, guiding the user through the process.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - NotebookLM
  - AntiGravity
  - MCP server
  - installation
  - setup
triggers:
  - when you want to connect AntiGravity to NotebookLM
  - when setting up NotebookLM MCP server
allowed-tools: []
compatibility: 'antigravity, notebooklm'
metadata:
  source: jack-school
  lesson: 128
  lesson_title: NotebookLM just got 10X better (AntiGravity)
  difficulty: medium
  category: nocode
  tools_required:
    - antigravity
    - notebooklm
  estimated_setup_time: 15min
  extracted_from:
    - NotebookLMjustgot10Xbetter.txt
---

# Nocode Install Notebooklm Mcp

## When to Use

Use this skill when you need to:
- when you want to connect AntiGravity to NotebookLM
- when setting up NotebookLM MCP server

## What This Does

Provides a prompt to install and setup the NotebookLM MCP server using AntiGravity, guiding the user through the process.

## Workflow

Install and set up the NotebookLM MCP server for me:
1. Install the notebooklm-mcp-server package using uv (or pip if uv isn't available)
2. Add it to my MCP configuration file (usually at ~/.config/opencode/opencode.json or similar)
3. Run the authentication command (notebooklm-mcp-auth) and open a browser to authorize it
4. Verify the installation is working by listing my NotebookLM notebooks
Make sure to:
- Use the correct installation method for my system
- Configure the MCP server properly in my config file
- Guide me through the browser authentication process
- Confirm everything is working at the end

## Configuration

**Required tools/platforms:**
- antigravity
- notebooklm

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
