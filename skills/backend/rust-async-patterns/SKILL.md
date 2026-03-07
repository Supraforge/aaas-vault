---
name: rust-async-patterns
description: >-
  Master Rust async programming with Tokio, async traits, error handling, and
  concurrent patterns. Use when building async Rust applications, implementing
  concurrent systems, or debugging async code.
version: 1.0.0
dependencies:
  - rustc
  - cargo
compatibility: 'agent-zero, claude-code, cursor'
---

# Rust Async Patterns

Production patterns for async Rust programming with Tokio runtime, including tasks, channels, streams, and error handling.

## When to Use This Skill

- Building async Rust applications
- Implementing concurrent network services
- Using Tokio for async I/O
- Handling async errors properly
- Debugging async code issues
- Optimizing async performance

## Core Concepts

### 1. Async Execution Model

```
Future (lazy) → poll() → Ready(value) | Pending
                ↑           ↓
              Waker ← Runtime schedules
```

### 2. Key Abstractions

| Concept | Purpose |
|---------|---------|
| `Future` | Lazy computation that may complete later |
| `async fn` | Function returning impl Future |
| `await` | Suspend until future completes |
| `Task` | Spawned future running concurrently |
| `Runtime` | Executor that polls futures |

## Quick Start

```toml
# Cargo.toml
[dependencies]
tokio = { version = "1", features = ["full"] }
futures = "0.3"
async-trait = "0.1"
anyhow = "1.0"
tracing = "0.1"
tracing-subscriber = "0.3"
```

```rust
use tokio::time::{sleep, Duration};
use anyhow::Result;

#[tokio::main]
async fn main() -> Result<()> {
    // Initialize tracing
    tracing_subscriber::fmt::init();

    // Async operations
    let result = fetch_data("https://api.example.com").await?;
    println!("Got: {}", result);

    Ok(())
}

async fn fetch_data(url: &str) -> Result<String> {
    // Simulated async operation
    sleep(Duration::from_millis(100)).await;
    Ok(format!("Data from {}", url))
}
```

## Patterns

### Pattern 1: Concurrent Task Execution

```rust
use tokio::task::JoinSet;
use anyhow::Result;

// Spawn multiple concurrent tasks
async fn fetch_all_concurrent(urls: Vec<String>) -> Result<Vec<String>> {
    let mut set = JoinSet::new();

    for url in urls {
        set.spawn(async move {
            fetch_data(&url).await
        });
    }

    let mut results = Vec::new();
    while let Some(res) = set.join_next().await {
        match res {
            Ok(Ok(data)) => results.push(data),
            Ok(Err(e)) => tracing::error!("Task failed: {}", e),
            Err(e) => tracing::error!("Join error: {}", e),
        }
    }
    Ok(results)
}
```

### Pattern 2: Async Traits with `async-trait`

```rust
use async_trait::async_trait;
use anyhow::Result;

#[async_trait]
pub trait DataFetcher {
    async fn fetch(&self, url: &str) -> Result<String>;
}

struct HttpClient;

#[async_trait]
impl DataFetcher for HttpClient {
    async fn fetch(&self, url: &str) -> Result<String> {
        // Implementation
        Ok(format!("Data from {}", url))
    }
}
```

### Pattern 3: Error Handling with `anyhow`

```rust
use anyhow::{Context, Result};

async fn load_config() -> Result<Config> {
    let content = tokio::fs::read_to_string("config.toml")
        .await
        .context("Failed to read config file")?;

    toml::from_str(&content)
        .context("Failed to parse config")
}
```

### Pattern 4: Channels for Communication

```rust
use tokio::sync::mpsc;

let (tx, mut rx) = mpsc::channel(32);

// Producer task
tokio::spawn(async move {
    for i in 0..10 {
        tx.send(i).await.unwrap();
    }
});

// Consumer task
while let Some(item) = rx.recv().await {
    println!("Got: {}", item);
}
```

### Pattern 5: Stream Processing

```rust
use futures::stream::{self, StreamExt};
use tokio::time::{sleep, Duration};

let stream = stream::iter(0..5)
    .then(|n| async move {
        sleep(Duration::from_millis(100)).await;
        n * 2
    });

let results: Vec<_> = stream.collect().await;
println!("Results: {:?}", results);
```

## Advanced Patterns

### Pattern 6: Cancellation with `CancellationToken`

```rust
use tokio_util::sync::CancellationToken;

let token = CancellationToken::new();
let child_token = token.child_token();

tokio::spawn(async move {
    tokio::select! {
        _ = child_token.cancelled() => {
            println!("Task cancelled");
        }
        _ = async {
            // Long-running work
            tokio::time::sleep(Duration::from_secs(10)).await;
        } => {}
    }
});

// Later, cancel all tasks
token.cancel();
```

### Pattern 7: Rate Limiting with `tokio::time::interval`

```rust
use tokio::time::{interval, Duration};

let mut interval = interval(Duration::from_millis(100));
loop {
    interval.tick().await;
    // Execute at most 10 times per second
    do_work().await;
}
```

### Pattern 8: Async Mutex for Shared State

```rust
use tokio::sync::Mutex;

let counter = Arc::new(Mutex::new(0));

for _ in 0..10 {
    let counter = Arc::clone(&counter);
    tokio::spawn(async move {
        let mut lock = counter.lock().await;
        *lock += 1;
    });
}
```

## Debugging Async Code

### Using `tracing` for Instrumentation

```rust
use tracing::{info, error, warn, debug};
use tracing::instrument;

#[instrument(skip(pool))]
async fn fetch_user(pool: &PgPool, id: &str) -> Result<User> {
    tracing::debug!("Fetching user");
    // ...
}

// Track task spawning
let span = tracing::info_span!("worker", id = %worker_id);
tokio::spawn(async move {
    // Enters span when polled
}.instrument(span));
```

## Best Practices

### Do's
- **Use `tokio::select!`** - For racing futures
- **Prefer channels** - Over shared state when possible
- **Use `JoinSet`** - For managing multiple tasks
- **Instrument with tracing** - For debugging async code
- **Handle cancellation** - Check `CancellationToken`

### Don'ts
- **Don't block** - Never use `std::thread::sleep` in async
- **Don't hold locks across awaits** - Causes deadlocks
- **Don't spawn unboundedly** - Use semaphores for limits
- **Don't ignore errors** - Propagate with `?` or log
- **Don't forget Send bounds** - For spawned futures

## Resources

- [Tokio Tutorial](https://tokio.rs/tokio/tutorial)
- [Async Book](https://rust-lang.github.io/async-book/)
- [Tokio Console](https://github.com/tokio-rs/console)
