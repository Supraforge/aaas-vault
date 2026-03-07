---
name: creating-viral-tweets
description: >-
  Generates concise, punchy, and high-impact tweets for X.com (Twitter) designed
  for viral reach. Use when the user wants to turn a topic into a short,
  engaging post or a multi-tweet thread.
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---

# Creating Viral Tweets

This skill specializes in crafting high-engagement content for X.com, focusing on brevity, "punchy" hooks, and the specific writing style that performs well on the platform.

## When to use this skill
- When you want to share an insight, news, or opinion in a very concise format.
- When you need to summarize a complex topic into a single tweet or a thread.
- When you want to maximize visibility using X-native formatting and hashtags.

## Workflow

1. **Extraction**:
   - Identify the "core insight" from the user's topic.
   - Determine the intended tone (e.g., Bold, Educational, Humorous, Provocative).

2. **Drafting**:
   - Write the "Hook" (the first sentence) to be ultra-short and intriguing.
   - Use the remaining space for the "Meat" (the value) and a "Call to Action" (CTA).
   - Ensure the total length is well within 280 characters (aim for <200 for better readability).

3. **Viral Pass**:
   - Apply "X Formatting": Use line breaks, lists, and bold declarations.
   - Add 1-2 relevant hashtags (X algorithm prefers fewer, more specific hashtags).

4. **Review**:
   - Check against [Twitter Safety Guidelines](resources/twitter-safety-guidelines.md).
   - Offer the user a single tweet version and a "Thread Starter" version.

## Instructions

### 1. The "X Style" Guide
- **Brevity is King**: If you can say it in 5 words, don't use 10.
- **Strong Openers**: Start with a punchy statement (e.g., "Software engineering is 10% coding, 90% thinking.").
- **White Space**: Don't use blocks of text. Use line breaks to make the tweet scroll-friendly.

### 2. Thread Logic (Optional)
If the topic is too big for one tweet, output a "Thread" format:
- **Tweet 1**: The Hook + "A thread 🧵"
- **Tweets 2-N**: Sequential insights.
- **Final Tweet**: Summary + CTA (Follow/Retweet).

### 3. Safety & Guidelines
- Follow [Twitter Safety Guidelines](resources/twitter-safety-guidelines.md).
- Avoid misinformation, offensive language, or spammy behavior.
- Ensure content is relevant and adds value to the conversation.

## Resources
- [Viral Tweet Templates](resources/tweet-templates.md)
- [Twitter Safety Guidelines](resources/twitter-safety-guidelines.md)
