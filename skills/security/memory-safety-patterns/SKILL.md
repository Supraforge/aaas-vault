---
name: memory-safety-patterns
description: >-
  Implement memory-safe programming with RAII, ownership, smart pointers, and
  resource management across Rust, C++, and C. Use when writing safe systems
  code, managing resources, or preventing memory bugs.
version: 1.0.0
dependencies:
  - rustc
  - g++
  - gcc
  - valgrind
  - cargo
compatibility: 'agent-zero, claude-code, cursor'
---

# Memory Safety Patterns

## 🎯 Triggers
- "Write memory-safe C++ code"
- "Implement RAII for resource management"
- "Use smart pointers to prevent leaks"
- "Write safe Rust code with ownership"
- "Debug memory issues with AddressSanitizer"
- "Prevent use-after-free and buffer overflows"

## ⚡ Quick Start (Self-Check)
Before writing memory-safe code, verify your environment:
- [ ] Run `bash ~/.gemini/skills/memory-safety-patterns/test.sh` to check dependencies.
- [ ] Ensure you have Rust, C++, and C compilers installed.
- [ ] Install debugging tools like Valgrind and AddressSanitizer.

## 📋 Workflow
1. **Ingest**: Analyze the request to determine which language (Rust, C++, C) and which memory safety pattern is needed.
2. **Execute**: Implement the appropriate pattern using the examples below.
3. **Verify**: Run the code with appropriate safety checks (AddressSanitizer, Valgrind, Miri).

## 🤖 System Instructions
- Always prefer Rust for new code when memory safety is critical.
- In C++, use RAII and smart pointers (unique_ptr, shared_ptr, weak_ptr).
- In C, implement manual RAII patterns with cleanup functions.
- Use AddressSanitizer for C/C++ debugging.
- Use Miri for Rust undefined behavior detection.
- Never return references/pointers to local variables.
- Always check array bounds before access.
- Use const-correctness to prevent accidental modifications.

## 🛠️ Pattern Reference

### Pattern 1: RAII (Resource Acquisition Is Initialization)

```cpp
// C++ RAII example
template<typename T>
class Transaction {
public:
    Transaction(T& target) 
        : target_(target), backup_(target), committed_(false) {}

    ~Transaction() {
        if (!committed_) {
            target_ = backup_; // Rollback
        }
    }

    void commit() { committed_ = true; }

    T& get() { return target_; }

private:
    T& target_;
    T backup_;
    bool committed_;
};
```

### Pattern 2: Smart Pointers in C++

```cpp
#include <memory>

// unique_ptr: Single ownership
class Engine {
public:
    void start() { /* ... */ }
};

class Car {
public:
    Car() : engine_(std::make_unique<Engine>()) {}

    void start() {
        engine_->start();
    }

    // Transfer ownership
    std::unique_ptr<Engine> extractEngine() {
        return std::move(engine_);
    }

private:
    std::unique_ptr<Engine> engine_;
};

// shared_ptr: Shared ownership
class Node {
public:
    std::string data;
    std::shared_ptr<Node> next;

    // Use weak_ptr to break cycles
    std::weak_ptr<Node> parent;
};

void sharedPtrExample() {
    auto node1 = std::make_shared<Node>();
    auto node2 = std::make_shared<Node>();

    node1->next = node2;
    node2->parent = node1; // Weak reference
}
```

### Pattern 3: Rust Ownership

```rust
// Rust ownership example
fn main() {
    let s1 = String::from("hello");
    let s2 = s1; // s1 is moved, not copied
    // println!("{}", s1); // ERROR: value borrowed after move
    println!("{}", s2); // OK

    let s3 = String::from("world");
    let len = calculate_length(&s3); // Borrow reference
    println!("Length of '{}' is {}.", s3, len);
}

fn calculate_length(s: &String) -> usize {
    s.len()
}
```

### Pattern 4: Manual RAII in C

```c
// C manual RAII pattern
typedef struct {
    FILE* file;
    int is_open;
} SafeFile;

SafeFile safe_fopen(const char* filename, const char* mode) {
    SafeFile sf = {fopen(filename, mode), 0};
    if (sf.file) {
        sf.is_open = 1;
    }
    return sf;
}

void safe_fclose(SafeFile* sf) {
    if (sf->is_open && sf->file) {
        fclose(sf->file);
        sf->is_open = 0;
        sf->file = NULL;
    }
}

// Usage
void process_file() {
    SafeFile sf = safe_fopen("data.txt", "r");
    if (!sf.is_open) {
        // Handle error
        return;
    }
    
    // Use sf.file...
    
    // Automatically cleaned up when sf goes out of scope
    // But we need to explicitly call safe_fclose
    safe_fclose(&sf);
}
```

### Pattern 5: Bounds Checking

```cpp
// Safe array access
template<typename T, size_t N>
class SafeArray {
public:
    T& operator[](size_t index) {
        if (index >= N) {
            throw std::out_of_range("Index out of bounds");
        }
        return data_[index];
    }
    
    const T& operator[](size_t index) const {
        if (index >= N) {
            throw std::out_of_range("Index out of bounds");
        }
        return data_[index];
    }
    
private:
    T data_[N];
};
```

## 📝 Best Practices

### Do's
- **Use RAII** - Bind resource lifetime to object scope
- **Use smart pointers** - Avoid raw pointers in C++
- **Understand ownership** - Know who owns what
- **Check bounds** - Use safe access methods
- **Use tools** - AddressSanitizer, Valgrind, Miri

### Don'ts
- **Don't use raw pointers** - Unless interfacing with C
- **Don't return local references** - Dangling pointer
- **Don't ignore compiler warnings** - They catch bugs
- **Don't use `unsafe` carelessly** - In Rust, minimize it
- **Don't assume thread safety** - Be explicit

## Debugging Tools

```bash
# AddressSanitizer (Clang/GCC)
clang++ -fsanitize=address -g source.cpp

# Valgrind
valgrind --leak-check=full ./program

# Rust Miri (undefined behavior detector)
cargo +nightly miri run

# ThreadSanitizer
clang++ -fsanitize=thread -g source.cpp
```

## Resources

- [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/)
- [Rust Ownership](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html)
- [AddressSanitizer](https://clang.llvm.org/docs/AddressSanitizer.html)
