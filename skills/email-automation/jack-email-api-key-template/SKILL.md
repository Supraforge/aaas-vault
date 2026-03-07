---
name: jack-email-api-key-template
description: >-
  An HTML email template for sending API keys, including instructions on how to
  use them in Google Chrome.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - email
  - api
  - template
  - html
triggers:
  - When you need to send API keys to users via email.
  - When providing instructions on how to use an API key with Google Chrome.
allowed-tools: []
metadata:
  source: jack-school
  lesson: 47
  lesson_title: Tools
  difficulty: easy
  category: email
  estimated_setup_time: 5min
compatibility: 'agent-zero, claude-code, cursor'
---

# Email Api Key Template

## When to Use

Use this skill when you need to:
- When you need to send API keys to users via email.
- When providing instructions on how to use an API key with Google Chrome.

## What This Does

An HTML email template for sending API keys, including instructions on how to use them in Google Chrome.

## Workflow

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your API Code</title>
    <style>
        body {
            font-family: 'Avenir', 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .container {
            background-color: #ffffff;
            border-radius: 8px;
            padding: 30px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #2c3e50;
            font-size: 24px;
            margin-bottom: 20px;
        }
        .code {
            background-color: #e9f5ff;
            border: 1px solid #b3d4fc;
            border-radius: 4px;
            padding: 10px 15px;
            font-family: monospace;
            font-size: 18px;
            margin: 20px 0;
        }
        .instructions {
            margin-top: 20px;
            font-size: 16px;
        }
        .button {
            display: inline-block;
            background-color: #3498db;
            color: #ffffff;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 4px;
            margin-top: 20px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Your API adventure begins here!</h1>
        <p>Great news! Your API code is ready to power up your experience. Here it is:</p>
        <div class="code">
            {{1.`Unique ID 🆔`}}
        </div>
        <div class="instructions">
            <p>Follow these simple steps to get started:</p>
            <ol>
                <li>Fire up Google Chrome (it's our browser of choice for the best experience)</li>
                <li>Navigate to our API key entry page</li>
                <li>Copy and paste your shiny new API key into the designated field</li>
                <li>Hit that 'Submit' button with confidence</li>
                <li>Sit back, relax, and enjoy the magic! 🎉</li>
            </ol>
        </div>
        <a href="#" class="button" id="launchChromeBtn">Launch Chrome</a>
    </div>

    <script>
        document.getElementById('launchChromeBtn').addEventListener('click', function(e) {
            e.preventDefault();
            // Attempt to launch Chrome
            window.location.href = 'googlechrome://';
            
            // Fallback: If Chrome doesn't launch after a short delay, open a new tab
            setTimeout(function() {
                window.open('https://www.google.com', '_blank');
            }, 1000);
        });
    </script>
</body>
</html>

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
