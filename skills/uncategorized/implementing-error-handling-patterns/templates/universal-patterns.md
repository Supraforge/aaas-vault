# Universal Error Handling Patterns

### Pattern 1: Circuit Breaker
Prevent cascading failures in distributed systems.

```python
class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout=60):
        self.state = "CLOSED"
        self.failure_count = 0
        # ... implementation details
```

### Pattern 2: Error Aggregation
Collect multiple errors instead of failing on first error.

```typescript
class ErrorCollector {
    private errors: Error[] = [];
    add(error: Error): void { this.errors.push(error); }
    // ... implementation details
}
```

### Pattern 3: Graceful Degradation
Provide fallback functionality when errors occur.

```python
def with_fallback(primary, fallback):
    try:
        return primary()
    except Exception:
        return fallback()
```
