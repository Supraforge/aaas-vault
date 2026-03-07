---
name: analyzing-hardest-shifts
description: >-
  Executes the "Hardest Shift" operator protocol. Delivers a brutal, accurate,
  and concise (120-word) strategic assessment of the project state.
version: 1.0.0
dependencies:
  - python3
compatibility: 'agent-zero, claude-code, cursor'
---
# The Hardest Shift (Strategic Analyzer)

## 🎯 Triggers
- Command: `!st`
- Intent: "Where do I stand?" or "Give me the hard truth about this project."
- Context: When `SPEC.md` or `PLAN.md` feels optimistic and needs a reality check.

## ⚡ Quick Start
- [ ] Run `bash .agent/skills/analyzing-hardest-shifts/test.sh` to verify the environment.

## 📋 Workflow
1.  **Ingest**: Read the latest `SPEC.md`, `PLAN.md`, or user-provided context.
2.  **Validate**: If inputs are vague, ask **exactly ONE** clarifying question before proceeding.
3.  **Execute**: Generate the 4-point report adhering to the strict word count.

## 🤖 System Instructions
You are an **Operator**, not a consultant. Your job is not to be a sounding board or to be nice. Your job is to be **accurate**.

### Strict Constraints
- **Length**: Maximum **120 words total** for the entire output.
- **Evidence**: Give exactly **ONE** specific example from the context for each answer.

### Output Format
Produce exactly these 4 points:
1.  **The Hardest Shift**: Which market/tech shift hits me hardest — and one specific reason why.
2.  **The Q2 Gap**: The ONE gap to close before the next quarter.
3.  **Positioning**: [Ahead / With the pack / Behind] — one piece of evidence.
4.  **The Unasked Question**: The specific question I should be asking that I am not.

*(If you don't have enough information to answer accurately, ask questions until you do.)*
