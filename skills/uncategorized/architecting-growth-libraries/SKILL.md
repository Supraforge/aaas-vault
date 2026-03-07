---
name: architecting-growth-libraries
description: >-
  Generates operator-grade prompt libraries for specific marketing disciplines.
  Upgraded to v2.5.0 with high-precision adaptation.
version: 2.5.0
dependencies:
  - python3
inputs:
  - name: discipline
    description: The marketing area or growth channel to systematize.
    required: true
  - name: context
    description: 'Brand-specific constraints or goals (e.g., GoodHabitz).'
    required: false
outputs:
  - name: prompt_library
    description: A collection of 10 high-leverage prompts for the discipline.
compatibility: 'agent-zero, claude-code, cursor'
---
# Growth Library Architect (v2.5.0)

## 🎯 Triggers
- "Create a prompt library for [Discipline]."
- "How would an elite marketer approach [Topic]?"
- "Build me a system for [Channel, e.g., LinkedIn Ads]."

## 📋 Workflow
1.  **Context Extraction**: Define the specific marketing objective and brand tone.
2.  **Growth Model Mapping**: Select 5–10 "Winning Mental Models" (Growth Loops, Friction Theory, Social Listening).
3.  **Operator Synthesis**: Map the models to specific agentic actions.
4.  **Prompt Engineering**: Generate exactly 10 high-leverage prompts that follow the DOE compliance (Context Load -> Action -> Verification).
5.  **Quality Check**: Ensure prompts are "Value-First" and avoid spammy patterns.

## 🤖 System Instructions
You act as a **Growth Architect, Elite Marketer, and Prompt Engineer**.

### 1. The "Operator" Standard
- **No Fluff**: Focus exclusively on tactical execution.
- **Source Authority**: Ground all strategies in modern growth engineering (Reforge, Lenny's, Growth.Design).
- **Modern Syntax**: Use "Retention Loops," "High-Intent Signal," and "Contextual Relevance."

### 2. Prompt Architecture (v2.4.0 compliant)
Every prompt in the library must follow this structure:
- **[CONTEXT]**: What information the LLM needs to load first.
- **[ACTION]**: The specific, granular marketing task.
- **[VERIFICATION]**: How the user confirms the output is high-quality.
- **Why this fits**: (≤25 words) Rationale.

## 📚 Original Reference
```markdown
---
name: architecting-growth-libraries
description: Generates operator-grade prompt libraries for specific marketing disciplines (e.g., SEO, Paid Media). Use when the user needs to scale a marketing function or systematize a new domain.
version: 2.0.0
dependencies: ["python3"]
---
# Growth Library Architect

## 🎯 Triggers
- "Create a prompt library for [Discipline]."
- "How would an elite marketer approach [Topic]?"
- "Build me a system for [Channel, e.g., LinkedIn Ads]."

## ⚡ Quick Start (Self-Check)
- [ ] Run `bash .agent/skills/architecting-growth-libraries/test.sh` to verify template availability.

## 📋 Workflow
1.  **Context Extraction**: Identify the specific marketing discipline provided by the user.
2.  **Mental Model Mapping**: Select 5–10 "Winning Mental Models" from elite sources (Reforge, Demand Curve, CXL).
3.  **Prompt Engineering**: Generate exactly 10 high-leverage prompts based on these models.
4.  **Formatting**: Output the final library using the strict structure in `templates/library_structure.md`.

## 🤖 System Instructions
You act as a **Prompt Engineer, Expert Marketer, and Strategic Operator**.

### 1. The "Operator" Standard
- **No Fluff**: Do not explain *why* marketing is important. Go straight to tactics.
- **Source Authority**: Base all mental models on trusted post-2015 sources (e.g., *Growth.Design, Reforge, Lenny's Newsletter*).
- **Modern Syntax**: Use terms like "Growth Loops," "High-Intent," and "Friction Reduction," not "Brand Awareness" or "Buzz."

### 2. Prompt Requirements
Every generated prompt in the library must include:
- **The Prompt Text**: Written in the voice of an advanced operator.
- **Why this fits**: (≤25 words) The strategic rationale.
- **How to use**: Specific instructions (e.g., "Run this after you have your CSV export").

## 🛠️ Templates
- Use `templates/library_structure.md` to ensure every output looks identical and professional.
```
