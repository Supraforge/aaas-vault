---
name: jack-email-proposal-followup
description: >-
  HTML email template to follow up after a client meeting, summarizing the
  conversation and attaching the proposal.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - email
  - sales
  - proposal
  - follow-up
triggers:
  - After sending a proposal to a client
  - When needing a follow-up email template
allowed-tools: []
metadata:
  source: jack-school
  lesson: 63
  lesson_title: Tools
  difficulty: easy
  category: email
  estimated_setup_time: 5min
  extracted_from:
    - "\U0001F525 Meeting to PDF Bonus Resources.txt"
compatibility: 'agent-zero, claude-code, cursor'
---

# Email Proposal Followup

## When to Use

Use this skill when you need to:
- After sending a proposal to a client
- When needing a follow-up email template

## What This Does

HTML email template to follow up after a client meeting, summarizing the conversation and attaching the proposal.

## Workflow

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meeting Proposal Summary</title>
    <style>
        @import url('https://fonts.cdnjs.com/css2?family=Avenir:wght@400;500;700&display=swap');
        
        body {
            font-family: 'Avenir', Arial, sans-serif;
            line-height: 1.6;
            color: #333333;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
        .top-banner {
            background: linear-gradient(135deg, #4158D0, #C850C0, #FFCC70);
            color: white;
            padding: 20px;
            margin: -20px -20px 20px -20px;
            border-radius: 5px 5px 0 0;
        }
        .content {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 5px;
        }
        .signature {
            margin-top: 30px;
            border-left: 4px solid #4158D0;
            padding-left: 15px;
        }
        h1 {
            margin: 0;
            font-weight: 500;
            font-size: 22px;
        }
    </style>
</head>
<body>
    <div class="top-banner">
        <h1>Meeting Summary</h1>
    </div>


    <div class="content">
        <p>Hey [INSERT FIRST NAME],</p>
        
        <p>It was excellent to chat 😊</p>
        
        <p>Based on our conversation, I've attached a proposal for you.</p>


        <p>Please let me know if you have any questions or if there's anything else you'd like to discuss.</p>


        <div class="signature">
            <p>Best regards,<br>
            <strong>Jack Roberts</strong><br>
            AI Automations</p>
        </div>
    </div>
</body>
</html>

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
