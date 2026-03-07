---
name: executing-plans
description: >-
  Orchestrates the step-by-step implementation of a technical plan. Scans
  context for project constraints and ensures state-safe execution with
  mandatory checkpoints.
version: 2.2.0
dependencies:
  - bash
compatibility: 'agent-zero, claude-code, cursor'
---

# Executing Plans

Orchestrate the implementation of approved technical plans with precision, safety, and project-context awareness.

## 🎯 Triggers
- "I have a plan to implement, let's execute it step by step."
- "Load this plan and follow it with checkpoints."
- "Execute the implementation plan in batches."
- Starting a task designated in `PLAN.md` or `IMPLEMENTATION_PLAN.md`.

## ⚡ Quick Start (Self-Check)
Before running complex logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/executing-plans/test.sh` to check dependencies.

## 📋 Workflow
1. **Context Load**: Scan the root `context/` folder (e.g., `context/goals.md`, `context/brand.md`) to ground the execution in project-specific constraints.
2. **Ingest**: Load the `PLAN.md` or `implementation_plan.md`. Review critically to identify any gaps or risks given the current project state.
3. **Safety Check**: Verify that the environment is ready (e.g., git branch is clean) and confirm that no destructive changes will occur without user approval.
4. **Execute**: Follow the plan steps exactly. Work in atomic batches (ideally 3 tasks at a time) to allow for frequent feedback loops.
5. **Verify**: Run verification steps specified in the plan after each task/batch. Document the results in a progress report or `walkthrough.md`.
6. **Refine**: If errors occur during execution, analyze the root cause, fix the issue, and refine this skill or project context if the plan was fundamentally flawed.

## 🤖 System Instructions
- **Operator Mindset**: You are executing a blueprint. Be precise, methodical, and literal unless the context suggests a critical conflict.
- **Batched Execution**: Default to batches of 3 tasks. Report progress after each batch and wait for feedback before proceeding.
- **DOE Compliance**: Ensure all intermediate files are stored in `.tmp/` and secrets are read from `.env` only.
- **Gating**: If a task requires a skill that failed its health check, stop and alert the user.

## 🛠️ Script Reference
- `scripts/`: Use for any task-specific automation or migrations.
- `templates/`: Use for generating verification reports or status updates.
