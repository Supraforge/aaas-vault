---
name: jack-email-tone-analysis
description: >-
  Analyzes email responses to learn the writer's communication patterns,
  covering structure, formality, content flow, and technical elements.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - email
  - tone of voice
  - AI
  - analysis
triggers:
  - When you need to understand and replicate someone's email style.
  - When you want to train an AI to write emails in a specific person's voice.
allowed-tools: []
compatibility: openai
metadata:
  source: jack-school
  lesson: 58
  lesson_title: Never Write an Email Again... (AI RAG Automation)
  difficulty: medium
  category: email
  tools_required:
    - openai
  estimated_setup_time: 15min
  extracted_from:
    - 1_Email_Cleanse_.txt
    - 2_Vectorisation_.txt
    - 3_Email_Brain_.txt
---

# Email Tone Analysis

## When to Use

Use this skill when you need to:
- When you need to understand and replicate someone's email style.
- When you want to train an AI to write emails in a specific person's voice.

## What This Does

Analyzes email responses to learn the writer's communication patterns, covering structure, formality, content flow, and technical elements.

## Workflow

You are to analyze email responses to identify and learn the writer's unique communication patterns. Follow these precise steps for analysis:

## 1. Initial Response Structure 🤔
Analyze:
- First line response patterns
- Whether they reference the original email
- Greeting style categorization (none/informal/formal)
- Space patterns after greeting
- Acknowledgment phrases used

Example format to identify:

```
Original: "Quick question about..."
Response: "Thanks for reaching out about [topic]. [next line break?] [main content]"
```

## 2. Visual Structure Pattern Analysis 📚
Count and categorize:
- Average lines between paragraphs (1 or 2?)
- Typical paragraph length (lines)
- Use of white space
- Bullet point/list formatting style
- Indentation patterns
- Line break frequency

Document exact patterns like:
```
[Greeting]
[1 line break]
[Content]
[2 line breaks between major points?]
[Bullets with specific indentation?]
```

## 3. Formality Markers 🤓
Identify frequency and context of:
- Professional vocabulary vs. casual terms
- Contraction usage (don't vs do not)
- Emoji placement patterns
- Informal language triggers
- Business jargon usage

Create a formality scale:
1 = Very informal ("Hey!")
5 = Mixed formal/informal
10 = Highly formal ("Dear Sir/Madam")

## 4. Content Flow Patterns 👀
Map out:
- Multi-point response organization
- Quote/reference patterns from original email
- Transition phrases between topics
- Question handling order (sequential/priority)
- Information chunking methods

## 5. Closing Analysis 📈
Document:
- Standard sign-off phrases
- Action item formatting
- Follow-up question patterns
- Signature consistency
- Space before closing

## 6. Technical Elements 🤖
Count and analyze:
- Average sentence length
- Punctuation preferences (semicolons, dashes, etc.)
- Capitalization patterns
- Formatting conventions (bold/italic usage)
- List/bullet styling

## Output Format
After analysis, create a style guide with these sections:

1. "ALWAYS" rules
- List mandatory patterns found in every email

2. "USUALLY" patterns
- List patterns appearing in >70% of emails

3. "SOMETIMES" elements
- List patterns appearing in 30-70% of emails

4. "NEVER" patterns
- List elements consistently avoided

5. Style Quantification
- Paragraph length range
- Line break patterns
- Emoji frequency
- Formality score (1-10)

## Special Instructions 🌈
1. Track all deviations from standard email formats
2. Note unique identifiers in writing style
3. Document any context-dependent style changes
4. Map response patterns to different email types

When training to replicate this style, your outputs should maintain absolute consistency with these documented patterns, using them as rigid guidelines rather than suggestions.

## Configuration

**Required tools/platforms:**
- openai

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
