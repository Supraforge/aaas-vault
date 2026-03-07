---
name: jack-content-website-change-analyzer
description: >-
  Compares two versions of website text to identify and summarize meaningful
  content changes, ignoring superficial differences like formatting.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - content
  - website
  - comparison
  - ai
  - gpt-4
triggers:
  - >-
    When you need to identify changes between two versions of a website's
    content.
  - >-
    When you want to ignore superficial formatting differences and focus on
    meaningful content updates.
allowed-tools: []
compatibility: openai
metadata:
  source: jack-school
  lesson: 51
  lesson_title: 51)Steal This $297/m Competitor Intelligence Automation
  difficulty: medium
  category: content
  tools_required:
    - openai
  estimated_setup_time: 15min
---

# Content Website Change Analyzer

## When to Use

Use this skill when you need to:
- When you need to identify changes between two versions of a website's content.
- When you want to ignore superficial formatting differences and focus on meaningful content updates.

## What This Does

Compares two versions of website text to identify and summarize meaningful content changes, ignoring superficial differences like formatting.

## Workflow

**Revised Prompt for the AI:**

---

**Task Overview:**

You are provided with two versions of text from a website:

1. **Previous Version (7 Days Ago):**

   ```
   {{1.`Original File`}}
   ```

2. **Current Version (Today):**

   ```
{{3.text}}

   ```

**Objective:**

Compare the "Previous Version" and "Current Version" texts and produce a JSON object with exactly two fields:

- **"Changes":** Indicate whether updates have been made.
  - If meaningful differences are found between the two texts, set this field to `"Updates made ✅"`.
  - If the texts are effectively identical in content, set this field to `"No changes 🔵"`.

- **"Detail":** Provide details based on the comparison.
  - If no changes are detected, set this field to `"Nothing to update"`.
  - If changes are detected:
    - Begin with a concise summary (70 words or less) describing what's changed and potential impacts.
    - Follow with a bulleted list of each specific change, starting each bullet point with an appropriate emoji.

**Instructions:**

1. **Comparison:**

   - Carefully compare the "Previous Version" and "Current Version" texts.
   - Identify any **meaningful content differences**, including additions, deletions, or modifications that affect the information conveyed.
   - **Ignore superficial changes** such as formatting, styling, or reordering of items **unless they alter the meaning or significance**.
   - Do not consider changes in the order of logos, images, or lists as changes unless the order conveys specific meaning.
   - Focus solely on the textual content provided.
   - Do not include or assume any external information.

2. **JSON Output Format:**

   - Output must be a valid JSON object with two fields: `"Changes"` and `"Detail"`.
   - Ensure proper JSON syntax (quotation marks, commas, braces).
   - Do not include any additional text outside the JSON object.

3. **Detail Field Formatting:**

   - **When Changes Are Detected:**
     - Start with a brief summary (maximum 70 words) of the overall changes and potential impacts.
     - Provide a bulleted list of each specific change, using an appropriate emoji at the start of each bullet point.
     - Each bullet point should be on a new line and clearly describe the specific change.

   - **When No Changes Are Detected:**
     - Set the `"Detail"` field to `"Nothing to update"`.

4. **Emojis Usage:**

   - Use relevant emojis that represent the nature of each change:
     - 🆕 for new additions
     - ✏️ for modifications or edits
     - ❌ for deletions or removals
     - 📢 for announcements or important updates
     - 🔄 for reorganizations that **alter meaning**

5. **Style Guidelines:**

   - Use clear and professional language.
   - Be objective; do not include personal opinions.
   - Do not ask questions or seek clarification.
   - Do not reference any content outside of the provided texts.

6. **Validation:**

   - Ensure the final output is properly formatted JSON.
   - Check for syntax errors such as missing commas, quotation marks, or braces.
   - Do not include any introductory or concluding text—only provide the JSON object.

**Examples:**

- **No Changes Detected:**

  ```json
  {
    "Changes": "No changes 🔵",
    "Detail": "Nothing to update"
  }
  ```

- **Changes Detected:**

  ```json
  {
    "Changes": "Updates made ✅",
    "Detail": "The current version includes updates to product features and pricing, which may affect customer decisions.\n\n- 🆕 Added a new 'Premium Plus' subscription tier.\n- ✏️ Modified the pricing for the 'Basic' plan from £9.99 to £12.99.\n- ❌ Removed the 'Student Discount' section."
  }
  ```

**Important Notes:**

- **Focus on Meaningful Content Changes:**

  - **Ignore superficial differences** in formatting, styling, or ordering that do not impact the meaning.
  - Do not report changes due to rendering issues or variations in how content is displayed.
  - **Only report changes that affect the information or message** conveyed by the text.

- **Order of Items:**

  - Do not consider changes in the order of items (e.g., logos, lists) as changes **unless the order conveys specific meaning or priority**.
  - If the same items are present but simply reordered, and the order does not impact the meaning, **do not report this as a change**.

- **No Additional Commentary:**

  - Do not include personal opinions or subjective statements.
  - Do not ask for further information or provide disclaimers.

**Final Checklist Before Submission:**

- [ ] The output is a valid JSON object with `"Changes"` and `"Detail"` fields.
- [ ] The `"Changes"` field correctly indicates whether updates were made.
- [ ] The `"Detail"` field is formatted according to the instructions, including emojis and bullet points if changes are detected.
- [ ] The summary at the top of the `"Detail"` field is 70 words or less.
- [ ] All information is derived solely from comparing the two provided texts.
- [ ] **Only meaningful content changes are reported; superficial differences are ignored.**
- [ ] No external information or assumptions are included.
- [ ] The output adheres to the style guidelines and is free of grammatical errors.
- [ ] No additional text is included outside of the JSON object.

---

By specifying that the AI should ignore changes in the order of items unless it alters the meaning, we reduce the likelihood of false positives due to superficial reordering. This adjustment ensures that only significant content changes are reported, providing you with accurate and relevant information.

**Additional Suggestion:**

- **If Possible, Normalize the Texts Before Comparison:**
  - Convert both texts to a consistent format (e.g., plain text without styling or formatting).
  - This can help eliminate differences caused by rendering or formatting issues.
  - Remove any non-content elements like HTML tags, scripts, or styles that don't affect the actual content.

---

## Configuration

**Required tools/platforms:**
- openai

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
