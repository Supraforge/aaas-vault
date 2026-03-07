---
name: architecting-spec-driven-features
description: >-
  Orchestrates the full GitHub Spec Kit lifecycle (SSD). Use when starting
  features, refactoring, or when commands like /specify, /plan, or /tasks are
  issued. Gated by project constitution.
version: 2.2.0
dependencies:
  - python3
  - bash
compatibility: 'agent-zero, claude-code, cursor'
---
# Spec-Driven Architect (GitHub Spec Kit)

## 🎯 Triggers
- Commands: `/specify [desc]`, `/plan`, `/tasks`
- Intent: "Start a new feature," "Let's plan this out," "Standardize the project requirements."

## 📋 SDD Workflow Checklist
- [ ] **Phase 0: Constitution Check**: Verify project-root `constitution.md`.
- [ ] **Phase 1: /specify**: Generate functional requirements in `docs/specs/[feature-slug]/SPEC.md`.
- [ ] **Phase 2: /plan**: Generate technical architecture in `PLAN.md` (Constitution Gated).
- [ ] **Phase 3: /tasks**: Generate atomic backlog in `TASKS.md`.

## 🤖 System Instructions (The Architect)

### ⚖️ Mandatory Constitution Gating
1. **The /plan command is hard-gated.** You MUST NOT proceed with technical planning unless `constitution.md` exists in the project root.
2. **Missing Constitution**: If missing, STOP. Inform the user: *"No constitution.md found. I must initialize one from the Global Constitution Template before planning."*
3. **Compliance Verification**: Every technical decision in `PLAN.md` MUST be cross-referenced against the `constitution.md`. If a decision violates a rule (e.g. adding a dependency without justification), you MUST flag it.

### 🛠️ Command Implementation
- **`/specify [description]`**:
    - Slugify the description for the directory name.
    - Create `docs/specs/[feature-slug]/SPEC.md`.
    - Use `templates/SPEC_TEMPLATE.md`.
- **`/plan`**:
    - **Step A**: Read root `constitution.md`.
    - **Step B**: Ingest the active `SPEC.md`.
    - **Step C**: Create `docs/specs/[feature-slug]/PLAN.md` using `templates/PLAN_TEMPLATE.md`.
    - **Step D**: Explicitly check for violations of the Constitution.
- **`/tasks`**:
    - Ingest the approved `PLAN.md`.
    - Create `docs/specs/[feature-slug]/TASKS.md` using `templates/TASKS_TEMPLATE.md`.
    - Focus on atomic, 15-minute tasks with verification steps.

## 📋 Path Standards
All SDD artifacts reside in `docs/specs/[feature-slug]/`.

## ⚡ Verification (Self-Check)
- [ ] Run `bash ~/.gemini/skills/architecting-spec-driven-features/test.sh`.
