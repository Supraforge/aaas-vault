# Advanced Debugging Techniques

### Technique 1: Binary Search Debugging
Use `git bisect` to find the exact commit that introduced a regression.

### Technique 2: Differential Debugging
Compare working vs broken environments/users to find the delta.
Example: `Node 18.16.0 (Working)` vs `Node 18.15.0 (Broken)`.

### Technique 3: Trace Debugging
Use decorators or wrappers to trace function calls and returns automatically.

### Technique 4: Memory Leak Detection
- **Heap Snapshots**: Compare state before and after actions in DevTools.
- **writeHeapSnapshot()**: Generate dumps in Node.js.
- **Memory Testing**: Monitor `process.memoryUsage().heapUsed` in test suites.
