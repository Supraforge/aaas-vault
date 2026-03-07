# Debugging Patterns by Issue Type

### Pattern 1: Intermittent Bugs
- Add extensive timing and state transition logging.
- Look for race conditions in shared state.
- Check timing (setTimeout, animation frame).
- Stress test with high frequency repetitions.

### Pattern 2: Performance Issues
- **Profile first**: Don't guess bottlenecks.
- Common culprits: N+1 queries, un-optimized re-renders, large data processing.
- Tools: Chrome Performance tab, Lighthouse, cProfile.

### Pattern 3: Production Bugs
- Gather evidence from Sentry, logs, and user reports.
- Reproduce locally with anonymized production data.
- Investigate safely using feature flags and enhanced monitoring.
