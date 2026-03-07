---
name: go-concurrency-patterns
description: >-
  Master Go concurrency with goroutines, channels, sync primitives, and context.
  Use when building concurrent Go applications, implementing worker pools, or
  debugging race conditions.
version: 1.0.0
dependencies:
  - go
compatibility: 'agent-zero, claude-code, cursor'
---

# Go Concurrency Patterns

Production patterns for Go concurrency including goroutines, channels, synchronization primitives, and context management.

## 🎯 Triggers
- Building concurrent Go applications
- Implementing worker pools and pipelines
- Managing goroutine lifecycles
- Using channels for communication
- Debugging race conditions
- Implementing graceful shutdown

## ⚡ Quick Start (Self-Check)
Before running complex logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/go-concurrency-patterns/test.sh` to check dependencies.

## 📋 Workflow
1. **Ingest**: Analyze the Go concurrency problem or pattern needed
2. **Execute**: Apply appropriate Go concurrency primitives and patterns
3. **Verify**: Test for race conditions and ensure proper synchronization

## 🤖 System Instructions
When working with Go concurrency:
- Always use the race detector during development: `go test -race ./...`
- Prefer channels over shared memory when possible
- Use context for cancellation and deadlines
- Close channels from the sender side only
- Use errgroup for concurrent operations with error handling
- Implement graceful shutdown patterns
- Avoid goroutine leaks by ensuring all goroutines have exit paths

## Core Concepts

### 1. Go Concurrency Primitives

| Primitive | Purpose |
|-----------|---------|
| `goroutine` | Lightweight concurrent execution |
| `channel` | Communication between goroutines |
| `select` | Multiplex channel operations |
| `sync.Mutex` | Mutual exclusion |
| `sync.WaitGroup` | Wait for goroutines to complete |
| `context.Context` | Cancellation and deadlines |

### 2. Go Concurrency Mantra

```
Don't communicate by sharing memory;
share memory by communicating.
```

## Quick Start

```go
package main

import (
    "context"
    "fmt"
    "sync"
    "time"
)

func main() {
    // Basic goroutine
    go func() {
        fmt.Println("Hello from goroutine")
    }()

    // WaitGroup for coordination
    var wg sync.WaitGroup
    for i := 0; i < 5; i++ {
        wg.Add(1)
        go func(id int) {
            defer wg.Done()
            time.Sleep(time.Duration(id) * time.Millisecond)
            fmt.Printf("Worker %d done\n", id)
        }(i)
    }
    wg.Wait()

    // Channel communication
    ch := make(chan string, 1)
    ch <- "message"
    msg := <-ch
    fmt.Println("Received:", msg)

    // Context with timeout
    ctx, cancel := context.WithTimeout(context.Background(), 1*time.Second)
    defer cancel()

    select {
    case <-time.After(2 * time.Second):
        fmt.Println("Operation completed")
    case <-ctx.Done():
        fmt.Println("Operation timed out")
    }
}
```

## Common Patterns

### Worker Pool
```go
func workerPool(numWorkers int, jobs <-chan Job, results chan<- Result) {
    var wg sync.WaitGroup
    for i := 0; i < numWorkers; i++ {
        wg.Add(1)
        go func(workerID int) {
            defer wg.Done()
            for job := range jobs {
                results <- process(job)
            }
        }(i)
    }
    wg.Wait()
    close(results)
}
```

### Pipeline
```go
func pipeline(input <-chan int) <-chan int {
    stage1 := make(chan int)
    stage2 := make(chan int)
    
    go func() {
        defer close(stage1)
        for n := range input {
            stage1 <- n * 2
        }
    }()
    
    go func() {
        defer close(stage2)
        for n := range stage1 {
            stage2 <- n + 1
        }
    }()
    
    return stage2
}
```

### Fan-out/Fan-in
```go
func fanOutFanIn(input <-chan int, numWorkers int) <-chan int {
    out := make(chan int)
    var wg sync.WaitGroup
    
    for i := 0; i < numWorkers; i++ {
        wg.Add(1)
        go func() {
            defer wg.Done()
            for n := range input {
                out <- processWork(n)
            }
        }()
    }
    
    go func() {
        wg.Wait()
        close(out)
    }()
    
    return out
}
```

## Race Detection

```bash
# Run tests with race detector
go test -race ./...

# Build with race detector
go build -race .

# Run with race detector
go run -race main.go
```

## Best Practices

### Do's
- **Use context** - For cancellation and deadlines
- **Close channels** - From sender side only
- **Use errgroup** - For concurrent operations with errors
- **Buffer channels** - When you know the count
- **Prefer channels** - Over mutexes when possible

### Don'ts
- **Don't leak goroutines** - Always have exit path
- **Don't close from receiver** - Causes panic
- **Don't use shared memory** - Unless necessary
- **Don't ignore context cancellation** - Check ctx.Done()
- **Don't use time.Sleep for sync** - Use proper primitives

## Resources

- [Go Concurrency Patterns](https://go.dev/blog/pipelines)
- [Effective Go - Concurrency](https://go.dev/doc/effective_go#concurrency)
- [Go by Example - Goroutines](https://gobyexample.com/goroutines)
