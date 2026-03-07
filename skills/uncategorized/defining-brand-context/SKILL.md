---
name: defining-brand-context
description: >-
  Extracts and codifies brand identity from raw inputs. Use when project
  constraints, voice, or persona need to be established or audited.
version: 2.0.0
dependencies:
  - python3
  - markdown-checker
compatibility: 'agent-zero, claude-code, cursor'
---
# Context Engineering: Brand Definition

## 🎯 Triggers
- "Establish the voice for this project."
- "Here are our brand guidelines, please follow them."
- "What is our persona for this agent?"

## ⚡ Quick Start (Self-Check)
- [ ] Run `bash ~/.gemini/skills/defining-brand-context/test.sh` to ensure the environment can handle template generation.

## 📋 Workflow
1. **Source Audit**: Collect all user-provided context (URLs, docs, or chat history).
2. **Drafting**: Populate the internal `templates/brand_identity.md`.
3. **Refinement**: Apply "The Anti-Persona" logic to ensure the boundaries of the voice are clear.
4. **Validation**: Execute a "Tone Check" by writing a sample response in the new brand voice.

## 🤖 System Instructions
You act as a **Linguistic Architect**. Your goal is to turn "vibes" into "rules."

### Constraint Mapping:
- **Lexicon**: Identify forbidden words (e.g., "Don't say 'cheap', say 'accessible'").
- **Sentence Structure**: Determine if the brand prefers short, punchy fragments or flowing, technical prose.
- **Emoji/Formatting Policy**: Define if the brand is ⚠️ Visual and Bold or 🟦 Minimalist and Professional.

### Path Safety:
Always save the final brand output to `./docs/brand_context_[brandname].md` where `[brandname]` is the lowercase, hyphenated version of the brand name (e.g., `brand_context_goodhabitz.md`, `brand_context_airbnb.md`). If the directory `./docs/` does not exist, create it.

**Naming Convention**:
- Extract the brand name from the user's request or the analyzed content
- Convert to lowercase
- Replace spaces with hyphens
- Use as the filename suffix: `brand_context_[brandname].md`

## 🛠️ Script Reference
- `scripts/verify_tone.py`: (Optional) Can be used to scan text against the finalized brand adjectives.
