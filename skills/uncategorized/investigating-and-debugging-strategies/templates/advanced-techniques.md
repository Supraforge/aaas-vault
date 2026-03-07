# Advanced Debugging Techniques

### Git Bisect
Find the exact commit that introduced a bug.
```bash
git bisect start
git bisect bad
git bisect good [tag/hash]
# ... test ...
git bisect good/bad
git bisect reset
```

### Trace Debugging
Use decorators or wrappers to log every entry and exit of a function without manual console.logs.

### Memory Leak Detection
- **Heap Snapshots**: Compare state before and after actions.
- **process.memoryUsage()**: Monitor growth in Node.js.

### Intermittent Bugs (Flaky)
- Look for race conditions (async timing).
- Stress test by running operations thousands of times.
- Log state transitions extensively.
