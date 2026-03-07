---
name: dispatching-parallel-agents
description: >-
  Dispatches parallel agents when facing 2+ independent tasks that can be worked
  on without shared state or sequential dependencies.
version: 1.0.0
dependencies: []
compatibility: 'agent-zero, claude-code, cursor'
---

# Dispatching Parallel Agents

## 🎯 Triggers
- When facing multiple independent failures in test files or subsystems.
- When tasks can be worked on concurrently without shared state or sequential dependencies.
- Use for 3+ test files failing with different root causes.

## ⚡ Quick Start (Self-Check)
- [ ] Run `bash ~/.gemini/skills/dispatching-parallel-agents/test.sh` to verify dependencies.

## 📋 Workflow
1. **Identify Independent Domains**: Group failures by what's broken (e.g., file A tests tool approval flow, file B tests batch completion).
2. **Create Focused Agent Tasks**: Each agent gets specific scope, clear goal, constraints, and expected output.
3. **Dispatch in Parallel**: Run agents concurrently to investigate independently.
4. **Review and Integrate**: Read summaries, verify no conflicts, run full test suite, integrate changes.

## 🤖 System Instructions
- Agent prompts must be focused, self-contained, and specific about output.
- Avoid common mistakes: too broad scope, no context, vague output, or lack of constraints.
- Use the provided agent prompt structure as a template for creating tasks.
- Do not use when failures are related, full system context is needed, or agents would interfere.

## 🛠️ Script Reference
- This skill provides a pattern; no additional scripts are required. Use agent dispatching tools in your environment.

## 📖 Detailed Guidance
Refer to the original content for diagrams, examples, and common mistakes. Key principles:
- Parallelization saves time when problems are independent.
- Each agent should have a narrow focus to avoid confusion.
- Always verify results and check for conflicts after parallel execution.
