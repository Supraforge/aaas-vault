---
name: applying-debugging-strategies
description: >-
  Masters systematic debugging techniques, profiling tools, and root cause
  analysis across any codebase or technology stack.
version: 1.0.0
dependencies:
  - python3
  - bash
compatibility: 'agent-zero, claude-code, cursor'
---

# Debugging Strategies

Transform debugging from frustrating guesswork into systematic problem-solving with proven strategies, powerful tools, and methodical approaches.

## 🎯 Triggers
- Tracking down elusive bugs
- Investigating performance issues
- Understanding unfamiliar codebases
- Debugging production issues
- Analyzing crash dumps and stack traces
- Profiling application performance
- Investigating memory leaks
- Debugging distributed systems

## ⚡ Quick Start (Self-Check)
Before running complex logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/applying-debugging-strategies/test.sh` to check dependencies.

## 📋 Workflow
1. **Ingest**: Reproduce the error consistently. Create a minimal reproduction case and isolate the problem.
2. **Execute**: 
   - Gather Information (Error messages, Environment, Recent changes).
   - Form Hypothesis (Ask: What changed? What's different?).
   - Test & Verify (Binary search, Strategic logging, Isolate components).
3. **Verify**: Test the fix thoroughly. Ensure the root cause is addressed and no regressions are introduced.

## 🤖 System Instructions
When applying this skill:
- **Reproduce First**: You cannot fix what you cannot reproduce.
- **Scientific Method**: Observe ➔ Hypothesize ➔ Experiment ➔ Analyze.
- **Don't Assume**: Question everything, including "It works on my machine."
- **Isolate**: Remove complexity until the minimal failing case is found.

## 🛠️ Template Reference
- `templates/core-principles.md`: Scientific method, Mindset, and Rubber Ducking.
- `templates/the-process.md`: Phase-by-phase reproduction and hypothesis testing.
- `templates/tooling.md`: JS/TS, Python, and Go debugging tools.
- `templates/advanced-techniques.md`: Git bisect, Differential debugging, and Memory leaks.
- `templates/issue-patterns.md`: Flaky bugs, Performance issues, and Production strategies.
