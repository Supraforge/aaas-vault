---
name: mastering-debugging-strategies
description: >-
  Masters systematic debugging techniques, profiling tools, and root cause
  analysis. Provides inline checklists and code snippets for live debugging
  sessions.
version: 1.0.0
dependencies:
  - python3
  - git
  - bash
compatibility: 'agent-zero, claude-code, cursor'
---

# Debugging Strategies (Compact Reference)

Transform debugging from frustrating guesswork into systematic problem-solving.

## 🎯 Triggers
- Tracking down elusive bugs
- Investigating performance issues
- Debugging production incidents
- Analyzing crash dumps and memory leaks

## ⚡ Quick Start (Self-Check)
- [ ] Run `bash ~/.gemini/skills/mastering-debugging-strategies/test.sh`

---

## 📋 Phase 1: Reproduce

### Checklist
- [ ] Can you reproduce it? (Always / Sometimes / Randomly)
- [ ] Is a minimal reproduction case possible?
- [ ] Have you documented exact steps and environment?

---

## 📋 Phase 2: Gather Information

### Checklist
- [ ] Captured full stack trace and error codes?
- [ ] Noted OS, Runtime, and Dependency versions?
- [ ] Reviewed Git history and deployment timeline?
- [ ] Determined scope (all users / specific users)?

---

## 📋 Phase 3: Form Hypothesis

### Questions to Ask
1. **What changed?** (Code, Dependencies, Infrastructure)
2. **What's different?** (Working vs Broken environment/user)
3. **Where could this fail?** (Validation, Logic, Data, Services)

---

## 📋 Phase 4: Test & Verify

### Strategies
- **Binary Search**: Comment out halves to narrow the scope.
- **Strategic Logging**: Track variables and execution flow.
- **Isolate Components**: Test with mocks.
- **Diff**: Compare configurations and data.

---

## 🛠️ Quick Tool Reference

### JavaScript/TypeScript
```typescript
debugger; // Pause execution
console.table(arr); console.time('op'); console.trace();
performance.mark('start'); performance.measure('op', 'start', 'end');
```

### Python
```python
breakpoint()  # or pdb.set_trace()
import logging; logging.basicConfig(level=logging.DEBUG)
cProfile.run('slow_function()', 'stats')
```

### Go
```go
debug.PrintStack()
// dlv debug main.go
```

### Git Bisect
```bash
git bisect start && git bisect bad && git bisect good v1.0.0
```

---

## 🚨 When Stuck, Check:
- [ ] Typos in variable names
- [ ] Null/undefined values
- [ ] Off-by-one errors
- [ ] Race conditions / Async timing
- [ ] Environment variables and file paths
- [ ] Cache and stale data

---

## 🤖 System Instructions
- **Reproduce before fixing.**
- **Change one thing at a time.**
- **Question all assumptions.**
- **Use the scientific method: Observe ➔ Hypothesize ➔ Experiment ➔ Analyze.**

## 🛠️ Script Reference
- `scripts/debug-helper.sh`: Environment validation script.
