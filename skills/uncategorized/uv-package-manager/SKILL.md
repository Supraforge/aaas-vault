---
name: uv-package-manager
description: >-
  Master the uv package manager for fast Python dependency management, virtual
  environments, and modern Python project workflows. Use when setting up Python
  projects, managing dependencies, or optimizing Python development workflows
  with uv.
version: 1.0.0
dependencies:
  - uv
  - python3
compatibility: 'agent-zero, claude-code, cursor'
---

# UV Package Manager

Comprehensive guide to using uv, an extremely fast Python package installer and resolver written in Rust, for modern Python project management and dependency workflows.

## When to Use This Skill

- Setting up new Python projects quickly
- Managing Python dependencies faster than pip
- Creating and managing virtual environments
- Installing Python interpreters
- Resolving dependency conflicts efficiently
- Migrating from pip/pip-tools/poetry
- Speeding up CI/CD pipelines
- Managing monorepo Python projects
- Working with lockfiles for reproducible builds
- Optimizing Docker builds with Python dependencies

## Core Concepts

### 1. What is uv?
- **Ultra-fast package installer**: 10-100x faster than pip
- **Written in Rust**: Leverages Rust's performance
- **Drop-in pip replacement**: Compatible with pip workflows
- **Virtual environment manager**: Create and manage venvs
- **Python installer**: Download and manage Python versions
- **Lockfile support**: Reproducible dependency resolution
- **Workspace support**: Monorepo project management
- **Cross-platform**: Works on Linux, macOS, Windows

### 2. Key Benefits
- **Speed**: Dramatically faster than traditional tools
- **Simplicity**: Single binary, no Python installation required
- **Compatibility**: Works with existing requirements.txt, pyproject.toml
- **Modern features**: Built-in lockfiles, workspace support
- **Reliability**: Deterministic dependency resolution

## Installation

### Quick Install (Linux/macOS)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Verify Installation
```bash
uv --version
```

## Basic Usage

### Project Initialization
```bash
uv init myproject          # Create new project
cd myproject
```

### Virtual Environment Management
```bash
uv venv                    # Create .venv in current directory
uv sync                    # Install dependencies
uv run python script.py    # Run script in virtual environment
```

### Dependency Management
```bash
uv add requests            # Add package
uv add "requests>=2.31"   # Add with version constraint
uv remove requests         # Remove package
uv sync                    # Sync dependencies
uv lock                    # Generate/update lockfile
```

### Python Version Management
```bash
uv python install 3.12     # Install Python 3.12
uv python list             # List installed versions
uv python pin 3.12         # Pin Python version for project
```

## Advanced Workflows

### 1. Migrating from pip
```bash
# Convert requirements.txt to uv.lock
uv pip compile requirements.txt

# Install from requirements.txt
uv pip install -r requirements.txt
```

### 2. CI/CD Optimization
```bash
# Use frozen mode for reproducibility
uv sync --frozen

# Cache uv dependencies
uv cache dir
```

### 3. Monorepo Management
```bash
# Workspace configuration
uv init --workspace

# Add packages to workspace
uv add --workspace requests
```

### 4. Docker Optimization
```bash
# Multi-stage Dockerfile example
FROM python:3.12-slim AS builder
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen

FROM python:3.12-slim
COPY --from=builder /app/.venv /app/.venv
COPY . .
CMD ["uv", "run", "app.py"]
```

## Common Commands Reference

```bash
# Project Management
uv init [name]            # Initialize project
uv init --workspace       # Initialize workspace
uv sync                   # Install dependencies
uv lock                   # Generate lockfile

# Virtual Environments
uv venv                   # Create .venv
uv venv --python 3.12     # Create with specific Python
uv run <command>          # Run command in venv

# Dependency Management
uv add <package>          # Add package
uv remove <package>       # Remove package
uv tree                   # Show dependency tree
uv show <package>         # Show package info

# Python Management
uv python install <ver>   # Install Python
uv python list            # List installed
uv python pin <ver>       # Pin version

# Pip Compatibility
uv pip install <pkg>      # Install via pip interface
uv pip uninstall <pkg>    # Uninstall package
uv pip freeze             # List installed
uv pip list               # List packages

# Utility
uv cache clean            # Clear cache
uv cache dir              # Show cache location
uv --version              # Show version
```

## Resources

- **Official documentation**: https://docs.astral.sh/uv/
- **GitHub repository**: https://github.com/astral-sh/uv
- **Astral blog**: https://astral.sh/blog
- **Migration guides**: https://docs.astral.sh/uv/guides/
- **Comparison with other tools**: https://docs.astral.sh/uv/pip/compatibility/

## Best Practices Summary

1. **Use uv for all new projects** - Start with `uv init`
2. **Commit lockfiles** - Ensure reproducible builds
3. **Pin Python versions** - Use .python-version
4. **Use uv run** - Avoid manual venv activation
5. **Leverage caching** - Let uv manage global cache
6. **Use --frozen in CI** - Exact reproduction
7. **Keep uv updated** - Fast-moving project
8. **Use workspaces** - For monorepo projects
9. **Export for compatibility** - Generate requirements.txt when needed
10. **Read the docs** - uv is feature-rich and evolving
