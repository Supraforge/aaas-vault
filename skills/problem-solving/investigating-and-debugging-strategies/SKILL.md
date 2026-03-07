---
name: investigating-and-debugging-strategies
description: >-
  Masters systematic debugging techniques, profiling tools, and root cause
  analysis to efficiently track down bugs across any codebase or technology
  stack.
version: 1.0.0
dependencies:
  - git
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
- [ ] Run `bash ~/.gemini/skills/investigating-and-debugging-strategies/test.sh` to check dependencies.

## 📋 Workflow
1. **Ingest**: Analyze the issue (error message, environment, recent changes) and reproduce it consistently in a minimal environment.
2. **Execute**: 
    - Gather information (logs, stack traces, environment variables).
    - Form a hypothesis based on what changed or what is different.
    - Test hypotheses using Binary Search, Logging, or Component Isolation.
3. **Verify**: Ensure the root cause is fixed, not just the symptom, and verify the fix across different environments.

## 🤖 System Instructions
When applying this skill:
- **Reproduce before fixing**: Never attempt a fix without a consistent reproduction case.
- **Change one thing at a time**: Isolate variables during experimentation.
- **Question assumptions**: "It works on my machine" is a clue, not an excuse.
- **Use the Scientific Method**: Observe -> Hypothesize -> Experiment -> Analyze.

## 🛠️ Template Reference
- `templates/universal-principles.md`: Scientific method and debugging mindset.
- `templates/process-phases.md`: Step-by-step reproduction and hypothesis testing.
- `templates/language-tools.md`: Specific tools for JS/TS, Python, and Go.
- `templates/advanced-techniques.md`: Git bisect, memory leak detection, and tracing.
