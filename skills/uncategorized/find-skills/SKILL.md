---
name: find-skills
description: >-
  Discovers and manages agent skills using a Three-Tier Discovery Protocol.
  Searches local project skills first, then the central Vault, then the global
  skills.sh registry. Use when asking "how do I do X", "find a skill for", or
  extending capabilities.
version: 2.0.0
compatibility: 'agent-zero, claude-code, cursor'
---

# Find Skills (Three-Tier Discovery)

**Version:** 2.0.0  
**Purpose:** Locate relevant skills across your local project, the central Vault, or the global registry.

## Architecture Overview

This skill operates within your centralized skill management system:

```
/Users/user/.gemini/
├── base/                          ← Template project (continuously evolving)
│   └── skills/                    ← Local skills for this project
├── [cloned-projects]/             ← Active projects cloned from base
│   └── skills/                    ← Project-specific skills (may evolve)
├── antigravity-vault/             ← Central Vault (write-back destination)
│   └── skills/                    ← Generically reusable skills
└── antigravity/
    └── global_skills/             ← Symlinked skills from skills.sh
```

**The Workflow:**
1. Clone `base` → create a new project
2. Evolve skills within that project as needed
3. De-brand and sync improved skills back to `antigravity-vault`
4. Future clones automatically benefit from vault improvements

## When to Use This Skill

Use this skill when the user:

- Asks "how do I do X" where X might be a common task
- Says "find a skill for X" or "is there a skill for X"
- Asks "can you do X" where X is a specialized capability
- Expresses interest in extending agent capabilities
- Wants to search for tools, templates, or workflows
- Mentions they wish they had help with a specific domain

## The Three-Tier Discovery Protocol

### Tier 1: Local Project Skills (Highest Priority)
Search the current project's `skills/` folder first. These are project-specific and have immediate relevance.

### Tier 2: The Vault (Central Repository)
Search `/Users/user/.gemini/antigravity-vault/skills`. These are de-branded, generically reusable skills that have been proven across projects.

### Tier 3: The Global Registry (External)
Fallback to `skills.sh` via `npx skills find`. Use this only when no local or vault skills match.

**Key Principle:** Always prefer local/vault skills before installing new ones from external sources.

## Usage

### Option 1: Run the Discovery Script

```bash
python3 ~/.gemini/base/skills/find-skills/scripts/discover.py "your query"
```

**Example:**
```bash
python3 ~/.gemini/base/skills/find-skills/scripts/discover.py "brand identity"
```

**Output:**
```
🔍 Searching capabilities for: 'brand identity'...

✅ **FOUND INSTALLED SKILLS (Local):**
- **brand-identity** (Relevance: 4)
  Path: `skills/brand-identity/SKILL.md`

🏛️ **FOUND IN THE VAULT:**
- **brand-identity** (Relevance: 4)
  Path: `/Users/user/.gemini/antigravity-vault/skills/brand-identity/SKILL.md`

(Use current skills before installing new ones!)
```

### Option 2: Use the Skills CLI (Tier 3 Only)

For searching the global registry directly:

```bash
npx skills find [query]
```

**Key CLI Commands:**
- `npx skills find [query]` - Search skills.sh
- `npx skills add <owner/repo@skill>` - Install a skill
- `npx skills add <owner/repo@skill> -g` - Install globally
- `npx skills check` - Check for updates
- `npx skills update` - Update all installed skills
- `npx skills list -g` - List globally installed skills

**Browse skills at:** https://skills.sh/

## How to Help Users Find Skills

### Step 1: Understand What They Need

Identify:
1. The domain (e.g., React, testing, design, deployment)
2. The specific task (e.g., writing tests, creating animations)
3. Whether this is common enough that a skill likely exists

### Step 2: Search Using Three Tiers

**Always check in order:**

1. **Local first:** Does the current project have a relevant skill?
2. **Vault second:** Is there a proven skill in the central vault?
3. **Remote last:** Only if nothing found locally, search skills.sh

### Step 3: Present Options to the User

When you find relevant skills, present them with:

1. **Source tier** (Local, Vault, or Remote)
2. The skill name and what it does
3. The path or install command
4. Recommendation on which to use

**Example Response:**
```
I found a skill that might help!

🏛️ **From the Vault:** `brand-identity`
This skill provides brand analysis and identity guidelines.
Path: `/Users/user/.gemini/antigravity-vault/skills/brand-identity/SKILL.md`

Recommendation: Use this vault skill - it's already proven across projects.
```

### Step 4: If Installing from Remote

If the user wants to install from skills.sh:

```bash
npx skills add <owner/repo@skill> -g -y
```

The `-g` flag installs to `~/.agents/skills/` (user-level) and `-y` skips prompts.

## Common Skill Categories

| Category        | Example Queries                          |
| --------------- | ---------------------------------------- |
| Branding        | brand, identity, logo, design-system     |
| Web Development | react, nextjs, typescript, css, tailwind |
| Testing         | testing, jest, playwright, e2e           |
| DevOps          | deploy, docker, kubernetes, ci-cd        |
| Documentation   | docs, readme, changelog, api-docs        |
| Code Quality    | review, lint, refactor, best-practices   |
| Design          | ui, ux, design-system, accessibility     |
| Research        | research, analysis, market, competitor   |

## When No Skills Are Found

If no relevant skills exist in any tier:

1. Acknowledge that no existing skill was found
2. Offer to help with the task directly using general capabilities
3. Suggest creating a new skill if it's a repeating need:

```bash
npx skills init my-new-skill
```

## Syncing Skills Back to the Vault

When a project-specific skill becomes generic enough to share:

1. De-brand the skill (remove project-specific references)
2. Copy to `/Users/user/.gemini/antigravity-vault/skills/`
3. Future clones of `base` will benefit

See the `skill-vault-sync` skill for automated de-branding and sync.

## Important Boundaries

- **Scope:** All skill management is limited to `/Users/user/.gemini/`
- **Priority:** Always prefer local → vault → remote
- **No External Writes:** Never modify skills outside `~/.gemini/`
- **Version Control:** The vault is the single source of truth for reusable skills
