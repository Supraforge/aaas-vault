---
name: jack-content-format-message-markdown
description: >-
  Formats a given text string to HTML with URL linking, bold, italic,
  strikethrough, inline code, blockquote, and line break support.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - markdown
  - html
  - formatting
  - url
  - bold
  - italic
  - strikethrough
  - blockquote
  - code
  - javascript
triggers:
  - >-
    When you need to convert markdown-like text into formatted HTML for display
    in a web application.
  - When you want to automatically create hyperlinks from URLs in a string.
allowed-tools: []
metadata:
  source: jack-school
  lesson: 54
  lesson_title: This RAG Chatbot Automation Changes Everything
  difficulty: easy
  category: content
  estimated_setup_time: 5min
compatibility: 'agent-zero, claude-code, cursor'
---

# Content Format Message Markdown

## When to Use

Use this skill when you need to:
- When you need to convert markdown-like text into formatted HTML for display in a web application.
- When you want to automatically create hyperlinks from URLs in a string.

## What This Does

Formats a given text string to HTML with URL linking, bold, italic, strikethrough, inline code, blockquote, and line break support.

## Workflow

function formatMessage(text) {
    // Convert URLs into clickable links
    const urlRegex = /(https?:\/\/[^\s]+)/g;
    let linkedText = text.replace(urlRegex, '<a href="$1" target="_blank" rel="noopener noreferrer">$1</a>');

    // Convert Markdown syntax to HTML
    // Bold: **text** or __text__
    linkedText = linkedText.replace(/(\*\*|__)(.*?)\1/g, '<strong>$2</strong>');

    // Italic: *text* or _text_
    linkedText = linkedText.replace(/(\*|_)(.*?)\1/g, '<em>$2</em>');

    // Strikethrough: ~~text~~
    linkedText = linkedText.replace(/~~(.*?)~~/g, '<del>$1</del>');

    // Inline code: `code`
    linkedText = linkedText.replace(/`(.*?)`/g, '<code>$1</code>');

    // Blockquote: > quote
    linkedText = linkedText.replace(/^> (.*)$/gm, '<blockquote>$1</blockquote>');

    // Replace line breaks with <br><br> for paragraph spacing
    linkedText = linkedText.replace(/\n/g, '<br><br>');

    return linkedText;
}

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
