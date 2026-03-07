---
name: internal-comms
description: >-
  A set of resources to help me write all kinds of internal communications,
  using the formats that my company likes to use. Claude should use this skill
  whenever asked to write some sort of internal communications (status reports,
  leadership updates, 3P updates, company newsletters, FAQs, incident reports,
  project updates, etc.).
version: 1.0.0
dependencies:
  - python3
  - bash
inputs:
  - name: input
    description: Input for the skill
outputs:
  - type: file/stdout
    description: Result of the skill execution
compatibility: 'agent-zero, claude-code, cursor'
---

# Internal Comms Anthropic

## 🎯 Triggers
- Use this skill when you need to a set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3p updates, company newsletters, faqs, incident reports, project updates, etc.).

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/internal-comms-anthropic/test.sh`.
- [ ] Check `.env` contains required keys (if applicable).

## 📋 Workflow
1. **Context Load**: Scan `context/` for project-specific goals.
2. **Ingest**: Process input according to skill requirements.
3. **Execute**: Run the skill's main logic.
4. **Verify**: Check outputs and validate results.

## 🛠️ Script Reference
- Use `scripts/` folder for executable scripts.

## When to use this skill
To write internal communications, use this skill for:
- 3P updates (Progress, Plans, Problems)
- Company newsletters
- FAQ responses
- Status reports
- Leadership updates
- Project updates
- Incident reports

## How to use this skill

To write any internal communication:

1. **Identify the communication type** from the request
2. **Load the appropriate guideline file** from the `examples/` directory:
    - `examples/3p-updates.md` - For Progress/Plans/Problems team updates
    - `examples/company-newsletter.md` - For company-wide newsletters
    - `examples/faq-answers.md` - For answering frequently asked questions
    - `examples/general-comms.md` - For anything else that doesn't explicitly match one of the above
3. **Follow the specific instructions** in that file for formatting, tone, and content gathering

If the communication type doesn't match any existing guideline, ask for clarification or more context about the desired format.

## Keywords
3P updates, company newsletter, company comms, weekly update, faqs, common questions, updates, internal comms

