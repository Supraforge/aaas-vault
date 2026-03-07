---
name: turborepo-caching
description: >-
  Configure Turborepo for efficient monorepo builds with local and remote
  caching. Use when setting up Turborepo, optimizing build pipelines, or
  implementing distributed caching.
version: 1.0.0
dependencies:
  - nodejs
  - npm
  - git
compatibility: 'agent-zero, claude-code, cursor'
---

# Turborepo Caching

Production patterns for Turborepo build optimization.

## When to Use This Skill

- Setting up new Turborepo projects
- Configuring build pipelines
- Implementing remote caching
- Optimizing CI/CD performance
- Migrating from other monorepo tools
- Debugging cache misses

## Core Concepts

### 1. Turborepo Architecture

```
Workspace Root/
├── apps/
│   ├── web/
│   │   └── package.json
│   └── docs/
│       └── package.json
├── packages/
│   ├── ui/
│   │   └── package.json
│   └── utils/
│       └── package.json
└── turbo.json
```

### 2. Caching Strategies

**Local Caching:**
```json
{
  "$schema": "https://turbo.build/schema.json",
  "pipeline": {
    "build": {
      "outputs": ["dist/**", ".next/**"],
      "cache": true
    },
    "test": {
      "outputs": [],
      "cache": true
    }
  }
}
```

**Remote Caching:**
```bash
# Set up remote cache
npx turbo login
npx turbo link

# Configure environment variables
export TURBO_TOKEN="your-token"
export TURBO_TEAM="your-team"
export TURBO_REMOTE_CACHE="enabled"
```

### 3. Cache Optimization Patterns

**Selective Caching:**
```json
{
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**"],
      "cache": true
    },
    "lint": {
      "outputs": [],
      "cache": false  # Don't cache lint results
    }
  }
}
```

**Environment Variable Hashing:**
```json
{
  "pipeline": {
    "build": {
      "env": ["NODE_ENV", "API_URL"],
      "outputs": ["dist/**"]
    }
  }
}
```

## Workflow

### 1. Setup Turborepo

```bash
# Initialize new Turborepo
npx create-turbo@latest

# Or add to existing monorepo
npm install turbo --save-dev
```

### 2. Configure turbo.json

Create `turbo.json` in workspace root:

```json
{
  "$schema": "https://turbo.build/schema.json",
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**", "build/**"]
    },
    "test": {
      "dependsOn": ["build"],
      "outputs": []
    },
    "lint": {
      "outputs": []
    },
    "dev": {
      "cache": false
    }
  }
}
```

### 3. Implement Remote Caching

```bash
# Login to Vercel for remote cache
npx turbo login

# Link your repository
npx turbo link

# Verify cache status
npx turbo run build --dry-run

# Run with remote cache
npx turbo run build
```

### 4. Optimize Cache Hits

**Use .turboignore:**
```
# Ignore files that shouldn't affect cache
node_modules/
*.log
coverage/
*.tmp
```

**Configure Outputs Carefully:**
```json
{
  "build": {
    "outputs": ["dist/**", "!dist/temp/**"]
  }
}
```

## Advanced Patterns

### 1. Distributed Caching

```bash
# GitHub Actions example
- name: Setup Turborepo
  run: |
    npm install turbo --save-dev
    npx turbo login --sso
    
- name: Restore cache
  uses: actions/cache@v3
  with:
    path: .turbo
    key: turbo-${{ github.ref }}-${{ github.sha }}
    restore-keys: |
      turbo-${{ github.ref }}-
      turbo-
```

### 2. Custom Cache Providers

```javascript
// custom-cache-provider.js
module.exports = {
  async put(key, value) {
    // Store in S3, Redis, etc.
  },
  async get(key) {
    // Retrieve from custom store
  }
};
```

### 3. Cache Invalidation Strategies

```json
{
  "pipeline": {
    "build": {
      "env": ["NODE_ENV", "VERSION"],
      "outputs": ["dist/**"]
    }
  }
}
```

## Troubleshooting

### Common Issues

1. **Cache Misses:**
   - Check `.turboignore` patterns
   - Verify environment variables in `turbo.json`
   - Ensure consistent file outputs

2. **Remote Cache Not Working:**
   - Verify `TURBO_TOKEN` is set
   - Check network connectivity
   - Confirm team permissions

3. **Build Order Issues:**
   - Review `dependsOn` configurations
   - Check for circular dependencies
   - Use `npx turbo run build --graph`

## Best Practices

1. **Cache Everything Possible:** Enable cache for all deterministic tasks
2. **Exclude Non-Deterministic Outputs:** Don't cache dev servers or watch modes
3. **Use Remote Cache in CI:** Share cache across team and CI runs
4. **Version Cache Keys:** Include environment variables that affect output
5. **Monitor Cache Hits:** Use `--dry-run` to analyze cache behavior

## Resources

- [Turborepo Documentation](https://turbo.build/repo/docs)
- [Remote Caching Guide](https://turbo.build/repo/docs/core-concepts/remote-caching)
- [Cache Configuration](https://turbo.build/repo/docs/reference/configuration)
