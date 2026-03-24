---
name: pinecone-context
description: Semantic context layer using Pinecone integrated indexes for skill discovery, directive lookup, and cross-project knowledge retrieval.
version: 1.0.0
author: antigravity
dependencies:
  - pinecone (pip install pinecone)
env:
  - PINECONE_API_KEY or PINECONE_API
---

# Pinecone Context Layer

## Purpose

Provides semantic search across the entire AntiGravity ecosystem:
- **5,800+ skills** from the central vault
- **9+ directives** (operational DNA)
- **System registry** documents (infrastructure, projects)
- **Per-client context** (brand, goals, strategy documents)

## Architecture

```
┌─────────────────────────────────────────┐
│          Pinecone Integrated Index       │
│     (multilingual-e5-large, 1024d)      │
├────────────┬────────────┬───────────────┤
│ skills     │ directives │ system-registry│
│ 5,800+     │ 9 docs     │ 6 docs        │
├────────────┴────────────┴───────────────┤
│         {client}-context                 │
│      Per-client namespaces               │
└─────────────────────────────────────────┘
```

## Setup

### 1. Create Pinecone Index

Create an **integrated index** (has built-in embeddings) via Pinecone dashboard or CLI:
- Name: `{project}-context` (e.g., `aaas-context`)
- Model: `multilingual-e5-large` (1024 dimensions)
- Region: `aws/us-east-1` (serverless)
- Metric: Cosine

### 2. Set API Key

Add to `.env`:
```
PINECONE_API_KEY=pcsk_xxxxx
```

### 3. Sync Content

```bash
# Sync all namespaces
python3 skills/pinecone-context/scripts/sync_context.py --all

# Sync specific namespace
python3 skills/pinecone-context/scripts/sync_context.py --namespace skills
python3 skills/pinecone-context/scripts/sync_context.py --namespace directives
python3 skills/pinecone-context/scripts/sync_context.py --namespace system-registry

# Add client context
python3 skills/pinecone-context/scripts/sync_context.py --namespace my-client-context

# List available namespaces
python3 skills/pinecone-context/scripts/sync_context.py --list
```

### 4. Query (Semantic Search)

```bash
# Find skills related to a topic
python3 skills/pinecone-context/scripts/query_context.py "email automation with drip campaigns"

# Search specific namespace
python3 skills/pinecone-context/scripts/query_context.py "brand voice guidelines" --namespace directives

# Get top N results
python3 skills/pinecone-context/scripts/query_context.py "firebase hosting" --top 10
```

## Scheduling

Add to crontab for weekly sync:
```bash
# Weekly Monday 08:00 — full sync
0 8 * * 1 python3 ~/.gemini/base/skills/pinecone-context/scripts/sync_context.py --all >> ~/.gemini/base/.tmp/logs/pinecone-sync.log 2>&1
```

## Namespace Strategy

| Namespace | Content | Records | Sync Frequency |
|-----------|---------|---------|----------------|
| `skills` | SKILL.md files from vault + base | ~5,800 | Weekly |
| `directives` | Operational SOPs from base | ~9 | On change |
| `system-registry` | Infrastructure docs | ~6 | On change |
| `{client}-context` | Per-client brand, goals, strategy | Varies | On change |

## Integration with Skill Discovery

The Pinecone context layer enhances the 4-tier skill discovery:

1. **Local** `./skills/` (keyword match)
2. **Vault** `~/.gemini/antigravity-vault/skills/` (keyword match)
3. **Pinecone** → **SEMANTIC MATCH** (understands intent, not just keywords)
4. **Remote** `npx skills find` (external registry)

When `find-skills/scripts/discover.py` finds no keyword matches, it falls back to Pinecone semantic search for fuzzy, intent-aware discovery.
