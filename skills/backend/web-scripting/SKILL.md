---
name: web-scripting
description: >-
  Develops web applications and scripts using Ruby and PHP with focus on
  idiomatic patterns, performance optimization, and modern frameworks
version: 1.0.0
dependencies:
  - ruby
  - php
  - rails
  - composer
compatibility: 'agent-zero, claude-code, cursor'
---

# Web Scripting with Ruby and PHP

## 🎯 Triggers
- "Build a Ruby on Rails application"
- "Create a PHP web application"
- "Optimize Ruby code performance"
- "Develop a PHP API with modern features"
- "Refactor legacy Ruby or PHP code"
- "Set up testing for Ruby/PHP applications"

## ⚡ Quick Start (Self-Check)
Before running complex logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/web-scripting/test.sh` to check dependencies.
- [ ] Ensure Ruby and PHP are installed with appropriate versions.

## 📋 Workflow
1. **Ingest**: Analyze the request to determine whether Ruby or PHP is more appropriate based on requirements, existing codebase, or team preferences.
2. **Execute**: Develop the solution following language-specific best practices and patterns.
3. **Verify**: Test the implementation, check for performance issues, and ensure security best practices are followed.

## 🤖 System Instructions

### Ruby Development Guidelines
- Embrace Ruby's expressiveness and metaprogramming features
- Follow Ruby and Rails conventions and idioms
- Use blocks and enumerables effectively
- Handle exceptions with proper rescue/ensure patterns
- Optimize for readability first, performance second
- Include Gemfile and .rubocop.yml when relevant

### PHP Development Guidelines
- Start with built-in PHP functions before writing custom implementations
- Use generators for large datasets to minimize memory footprint
- Apply strict typing and leverage type inference
- Use SPL data structures when they provide clear performance benefits
- Profile performance bottlenecks before optimizing
- Handle errors with exceptions and proper error levels
- Write self-documenting code with meaningful names
- Test edge cases and error conditions thoroughly

### Common Web Development Principles
- Follow MVC architecture for web applications
- Implement proper authentication and authorization
- Use secure coding practices to prevent injection attacks
- Optimize database queries and implement caching where appropriate
- Write comprehensive tests with appropriate frameworks
- Document APIs and key architectural decisions

## 🛠️ Language-Specific Expertise

### Ruby Focus Areas
- Ruby metaprogramming (modules, mixins, DSLs)
- Rails patterns (ActiveRecord, controllers, views)
- Gem development and dependency management
- Performance optimization and profiling
- Testing with RSpec and Minitest
- Code quality with RuboCop and static analysis

### PHP Focus Areas
- Generators and iterators for memory-efficient data processing
- SPL data structures (SplQueue, SplStack, SplHeap, ArrayObject)
- Modern PHP 8+ features (match expressions, enums, attributes, constructor property promotion)
- Type system mastery (union types, intersection types, never type, mixed type)
- Advanced OOP patterns (traits, late static binding, magic methods, reflection)
- Memory management and reference handling
- Stream contexts and filters for I/O operations
- Performance profiling and optimization techniques

## 📝 Output Standards

### Ruby Output
- Idiomatic Ruby code following community conventions
- Rails applications with MVC architecture
- RSpec/Minitest tests with fixtures and mocks
- Gem specifications with proper versioning
- Performance benchmarks with benchmark-ips
- Refactoring suggestions for legacy Ruby code

### PHP Output
- Memory-efficient code using generators and iterators appropriately
- Type-safe implementations with full type coverage
- Performance-optimized solutions with measured improvements
- Clean architecture following SOLID principles
- Secure code preventing injection and validation vulnerabilities
- Well-structured namespaces and autoloading setup
- PSR-compliant code following community standards
- Comprehensive error handling with custom exceptions
- Production-ready code with proper logging and monitoring hooks

## 🔧 Tooling Recommendations
- **Ruby**: Bundler for dependency management, RuboCop for linting, RSpec for testing
- **PHP**: Composer for dependency management, PHPStan for static analysis, PHPUnit for testing
- **Both**: Docker for environment consistency, CI/CD pipelines for automated testing
