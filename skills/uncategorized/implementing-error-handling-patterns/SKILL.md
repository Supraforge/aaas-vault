---
name: implementing-error-handling-patterns
description: >-
  Masters error handling patterns across languages including exceptions, Result
  types, error propagation, and graceful degradation to build resilient
  applications.
version: 1.0.0
dependencies:
  - python3
  - bash
compatibility: 'agent-zero, claude-code, cursor'
---

# Error Handling Patterns

Build resilient applications with robust error handling strategies that gracefully handle failures and provide excellent debugging experiences.

## 🎯 Triggers
- Implementing error handling in new features
- Designing error-resilient APIs
- Debugging production issues
- Improving application reliability
- Creating better error messages for users and developers
- Implementing retry and circuit breaker patterns
- Handling async/concurrent errors
- Building fault-tolerant distributed systems

## ⚡ Quick Start (Self-Check)
Before running complex logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/implementing-error-handling-patterns/test.sh` to check dependencies.

## 📋 Workflow
1. **Ingest**: Analyze the current codebase and the specific error handling needs (language, framework, and failure scenarios).
2. **Execute**: Apply the appropriate patterns (Circuit Breaker, Result Types, Retry, etc.) defined in the templates.
3. **Verify**: Ensure error cases are caught, logged correctly, and resources are cleaned up.

## 🤖 System Instructions
When applying this skill:
- **Always fail fast**: Validate input and conditions early.
- **Preserve context**: Ensure stack traces and metadata are not lost during propagation.
- **Differentiate errors**: Distinguish between recoverable (network) and unrecoverable (logic bug) errors.
- **Clean up resources**: Use proper abstractions (context managers, defer, try-finally).

## 🛠️ Template Reference
- `templates/python-patterns.md`: Python-specific robust error handling.
- `templates/typescript-patterns.md`: TypeScript/JavaScript pattern guide.
- `templates/rust-patterns.md`: Rust's Result and Option patterns.
- `templates/go-patterns.md`: Go's dual-return error handling.
- `templates/universal-patterns.md`: Circuit Breaker, Aggregation, and Fallback patterns.
