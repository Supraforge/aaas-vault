---
name: jack-email-webinar-confirmation-template
description: A fill-in-the-blanks email template to confirm webinar registration.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - email template
  - webinar
  - confirmation
  - registration
triggers:
  - when you need to send a confirmation email after webinar registration
  - when automating email responses to webinar sign-ups
allowed-tools: []
metadata:
  source: jack-school
  lesson: 102
  lesson_title: Tools
  difficulty: easy
  category: email
  estimated_setup_time: 5min
compatibility: 'agent-zero, claude-code, cursor'
---

# Email Webinar Confirmation Template

## When to Use

Use this skill when you need to:
- when you need to send a confirmation email after webinar registration
- when automating email responses to webinar sign-ups

## What This Does

A fill-in-the-blanks email template to confirm webinar registration.

## Workflow

<!DOCTYPE html>
<html>
  <body style="font-family: Arial, sans-serif; font-size: 16px; color: #333; line-height: 1.5;">
    
    <p>{{ $json['👋 Name'] }}, you’re all set! ✅</p>

    <p><strong>Your free spot is confirmed for:</strong><br>
    📅 {{ $json['Select Webinar'] }}</p>

    <p>This workshop is all about one thing: helping you land your very first paying client using AI systems.</p>

    <p><strong>To get the most out of it, please do ONE thing:</strong></p>

    <p>Take the 3-Minute Prep Scorecard:<br>
    <a href="https://wellness-magnet.carrd.co/" target="_blank">https://wellness-magnet.carrd.co/</a></p>

    <p>This short scorecard will:</p>
    <ul>
      <li>Benchmark where you’re at right now</li>
      <li>Highlight your biggest opportunities to win a client fast</li>
      <li>Give us valuable context to tailor the session</li>
    </ul>

    <p>I can’t wait to show you how to use AI to shortcut the path to your first client 🤙</p>

    <p>To your success,<br>
    Jack Roberts<br>
    Founder, AI Automations</p>

    <p><strong>P.S.</strong> Reply to this email with “AI” so I know you got it.</p>

  </body>
</html>

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
