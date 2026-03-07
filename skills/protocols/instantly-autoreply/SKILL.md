---
name: "instantly-autoreply"
description: "Automatically replies to Instantly campaign emails using a knowledge base and web research for personalized and context-aware responses."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["email","automation","sales","instantly","ai"]
triggers:
  - "when a reply is received from an Instantly campaign"
  - "when an email requires an automated, personalized response"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "directive"
  original_file: "instantly_autoreply.md"
---

# Instantly Autoreply

## When to Use

When an Instantly campaign receives a reply.,When a campaign-specific knowledge base is available.,When a quick, intelligent reply is needed to engage prospects.

## What This Does

Automatically replies to Instantly campaign emails using a knowledge base and web research for personalized and context-aware responses.

## Workflow

1. Parse the incoming reply email content from the payload (subject, text, html).,2. Optionally, retrieve the full conversation history using `instantly_get_emails` if more context is needed.,3. Extract the campaign ID from the `campaign_name` or use `campaign_id` directly.,4. Lookup the campaign's knowledge base and reply examples in spreadsheet `1QS7MYDm6RUTzzTWoMfX-0G9NzT5EoE2KiCE7iR1DBLM`.,5. If no knowledge base is found, return empty.,6. Generate a reply using extended thinking, following the specified role, tone, research guidelines, and output format.,7. If the generated reply is empty or whitespace, skip sending and return success with `skipped: true`.,8. Send the reply using `instantly_send_reply` with the appropriate parameters.

## Constraints

Use the specified knowledge base spreadsheet ID: `1QS7MYDm6RUTzzTWoMfX-0G9NzT5EoE2KiCE7iR1DBLM`.,Adhere to the defined role, tone, and formatting guidelines for generating replies.,Always research the sender and their company before generating the reply using web search.,Do not send a reply if it would be needless, explicitly negative, or if no knowledge base is found.,Handle errors gracefully and log any failures in the Instantly API or AI generation process.
