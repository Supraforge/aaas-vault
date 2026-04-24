# Agentic Index MCP — Technical Specification

> **Universal discovery layer for the entire agentic ecosystem.**
> One MCP. Every skill, agent, tool, API, model, MCP server, execution file, dataset, benchmark, and integration — indexed, scored, and instantly searchable.

**Version:** 0.1.0-draft
**Date:** 2026-04-24
**Author:** Supraforge
**Status:** Architecture Design

---

## 1. Problem Statement

The agentic ecosystem is fragmented across multiple disconnected registries:

| Source                                   | Assets                                                | Discovery                            |
| ---------------------------------------- | ----------------------------------------------------- | ------------------------------------ |
| **aaas-vault** (GitHub)                  | 5,441 skills / 52 categories                          | Browse folders or keyword grep       |
| **aaas-blocks** (MCP + GitHub)           | 12 composable code blocks / 3 layers                  | MCP tools, but limited to Next.js    |
| **aaas.blog** (Firestore)                | 800+ entities / 11 types                              | Web UI + API, but not MCP-accessible |
| **Harness index** (~/.claude)            | 4,326 components (agents, skills, plugins, templates) | `search-harness.mjs` keyword search  |
| **MCP Registries** (npm, GitHub)         | 1,000+ MCP servers                                    | Manual npm search                    |
| **Package Registries** (npm/PyPI/crates) | Millions of packages                                  | Per-registry search                  |
| **GitHub**                               | Open-source agents, tools, frameworks                 | `gh search code`                     |

**No single system can answer:** "What is the best tool/skill/agent/API to solve X right now?"

An AI agent mid-task cannot query across all sources to find the optimal asset. It must know which registry to search, use the right tool, parse the right format. This is the bottleneck.

---

## 2. Vision

**One MCP server that acts as the universal agentic asset resolver.**

Any AI agent — Claude Code, Agent Zero, Cursor, Windsurf, custom — connects this MCP and gains instant access to:

- What skill solves this problem?
- What MCP server provides this capability?
- What API endpoint does this?
- What agent is best for this task?
- What model should I use for this workload?
- What tools does this agent need?
- How do these assets relate to each other?

The MCP doesn't store the assets — it **indexes and routes to them**.

---

## 3. Universal Agentic Asset Taxonomy

### 3.1 Entity Types (16 types — superset of all sources)

```
EXISTING (from aaas.blog):        NEW (gap-filling):
─────────────────────────         ──────────────────
tool                              mcp-server
model                             api-endpoint
agent                             execution-file
skill                             plugin
script                            template
benchmark                         code-block
dataset
paper
provider
hardware
integration
```

### 3.2 Unified Base Schema

Every entity in the index conforms to this base schema. Type-specific extensions follow.

```typescript
interface AgenticAsset {
  // === IDENTITY ===
  id: string; // Deterministic: `${source}:${type}:${slug}`
  slug: string; // URL-safe identifier
  type: AssetType; // One of 16 types
  name: string; // Human-readable display name

  // === CLASSIFICATION ===
  category: string; // Primary category (from 52 vault cats or custom)
  subcategory?: string; // Optional refinement
  tags: string[]; // Freeform searchable tags
  domains: string[]; // Business domains: ["devops", "marketing", "finance"]

  // === CONTENT ===
  description: string; // One-paragraph summary
  capabilities: string[]; // What it can do (action phrases)
  useCases: string[]; // When to use it (scenario descriptions)
  triggers: string[]; // Activation phrases for agents

  // === RELATIONSHIPS ===
  requires: string[]; // Asset IDs this depends on
  enhances: string[]; // Asset IDs this improves
  alternatives: string[]; // Asset IDs that solve the same problem
  relatedTools: string[]; // Cross-type relationships
  relatedModels: string[];
  relatedAgents: string[];
  relatedSkills: string[];

  // === QUALITY ===
  scores: {
    adoption: number; // 0-100: how widely used
    quality: number; // 0-100: documentation, testing, maintenance
    freshness: number; // 0-100: recency of updates
    citations: number; // 0-100: references in papers/docs
    engagement: number; // 0-100: usage analytics
    composite: number; // Weighted aggregate
  };
  qualityTier: "gold" | "silver" | "bronze" | "unrated";
  schemaCompleteness: number; // 0-100: how many fields are populated

  // === PROVENANCE ===
  source: string; // "aaas-vault" | "aaas-blog" | "harness" | "npm" | "github"
  sourceUrl: string; // Direct link to the asset
  sourcePath?: string; // Local file path if available
  provider: string; // Company/author
  version: string;
  license: string;
  pricingModel: "free" | "freemium" | "paid" | "open-source";

  // === COMPATIBILITY ===
  platforms: string[]; // ["claude-code", "agent-zero", "cursor", "windsurf"]
  languages: string[]; // Programming languages
  runtimeRequirements: string[]; // ["node>=18", "python>=3.10", "docker"]

  // === TEMPORAL ===
  addedDate: string; // ISO 8601
  lastUpdated: string;
  lastVerified: string;

  // === SEARCH ===
  embedding?: number[]; // 1536-dim vector (generated, not stored in JSON)
  searchText: string; // Concatenated searchable text blob
}

type AssetType =
  | "tool"
  | "model"
  | "agent"
  | "skill"
  | "script"
  | "benchmark"
  | "dataset"
  | "paper"
  | "provider"
  | "hardware"
  | "integration"
  | "mcp-server"
  | "api-endpoint"
  | "execution-file"
  | "plugin"
  | "template"
  | "code-block";
```

### 3.3 Type-Specific Extensions

```typescript
// === MCP SERVER (NEW) ===
interface McpServerAsset extends AgenticAsset {
  type: "mcp-server";
  transport: "stdio" | "sse" | "streamable-http";
  toolCount: number;
  tools: string[]; // Tool names exposed
  resourceTypes: string[]; // Resource types exposed
  npmPackage?: string; // npm install target
  dockerImage?: string; // Docker pull target
  configSchema?: object; // JSON Schema for configuration
}

// === API ENDPOINT (NEW) ===
interface ApiEndpointAsset extends AgenticAsset {
  type: "api-endpoint";
  baseUrl: string;
  authType: "api-key" | "oauth2" | "bearer" | "none";
  endpoints: { method: string; path: string; description: string }[];
  rateLimits: string;
  sdkLanguages: string[];
  openApiUrl?: string;
}

// === EXECUTION FILE (NEW) ===
interface ExecutionFileAsset extends AgenticAsset {
  type: "execution-file";
  language: string;
  entrypoint: string;
  dependencies: string[];
  estimatedRuntime: string;
  executionEnvironment: string;
}

// === PLUGIN (NEW) ===
interface PluginAsset extends AgenticAsset {
  type: "plugin";
  pluginType: "hook" | "agent" | "skill" | "mcp" | "command";
  installCommand: string;
  configLocation: string;
  hooks: string[]; // Lifecycle events it hooks into
}

// === TEMPLATE (NEW) ===
interface TemplateAsset extends AgenticAsset {
  type: "template";
  templateType: "project" | "file" | "workflow" | "prompt";
  outputFormat: string;
  variables: string[]; // Template variables
}

// === CODE BLOCK (NEW — from aaas-blocks) ===
interface CodeBlockAsset extends AgenticAsset {
  type: "code-block";
  layer: "foundation" | "integration" | "feature";
  framework: string; // "nextjs", "remix", etc.
  frameworkVersion: string; // ">=16.0.0"
  files: { src: string; dest: string }[]; // Installable files
  dependencies: Record<string, string>; // npm packages
  devDependencies: Record<string, string>;
  envVars: {
    key: string;
    required?: boolean;
    default?: string;
    description?: string;
  }[];
  verifiedWith: Record<string, string>; // Version-pinned verification
  installCommand: string; // "npx aaas-blocks add auth/clerk"
}

// === SKILL (extended from vault + blog) ===
interface SkillAsset extends AgenticAsset {
  type: "skill";
  difficulty: "beginner" | "intermediate" | "advanced";
  prerequisites: string[];
  supportedAgents: string[];
  allowedTools: string[]; // From vault frontmatter
  contextEnhanced: boolean; // Supports CLIENT_CONTEXT.md
  contentWordCount: number;
  hasExamples: boolean;
  hasReferences: boolean;
}

// === AGENT (extended from blog) ===
interface AgentAsset extends AgenticAsset {
  type: "agent";
  autonomyLevel: "supervised" | "semi-autonomous" | "fully-autonomous";
  toolsUsed: string[];
  skills: string[];
  trustScore: number;
  agentType: "core" | "pool" | "external";
}

// Remaining types (tool, model, script, benchmark, dataset, paper,
// provider, hardware, integration) inherit directly from aaas.blog types.ts
// with no schema changes needed.
```

---

## 4. MCP Server Architecture

### 4.1 Server Identity

```
Name:        agentic-index
Package:     @supraforge/mcp-agentic-index
Transport:   stdio (local) + streamable-http (remote)
Runtime:     Node.js 20+ (Bun compatible)
```

### 4.2 MCP Tools Exposed

```
DISCOVERY (read-only):
──────────────────────
search              — Hybrid keyword + semantic search across all 16 asset types
resolve             — "I need to do X" → ranked list of assets that solve it
lookup              — Get full details for a specific asset by ID
browse              — List assets by type, category, or domain
compare             — Side-by-side comparison of 2-5 assets
related             — Get relationship graph for an asset
stats               — Index statistics and health

RECOMMENDATION:
───────────────
recommend           — Given a task description + current toolset, suggest missing assets
compatibility       — Check if assets work together (platform, version, dependency)
stack               — Recommend a complete stack for a use case (agent + tools + skills)

MANAGEMENT (write, auth required):
──────────────────────────────────
submit              — Submit a new asset for review
update              — Update asset metadata
verify              — Mark an asset as verified (human or agent)
flag                — Report an issue with an asset
```

### 4.3 Tool Signatures

```typescript
// === SEARCH: The primary discovery tool ===
tool("search", {
  query: string,              // Natural language or keywords
  type?: AssetType[],         // Filter by asset type(s)
  category?: string[],        // Filter by category
  domain?: string[],          // Filter by business domain
  platform?: string[],        // Filter by compatible platform
  qualityTier?: string[],     // Filter by quality tier
  minScore?: number,          // Minimum composite score (0-100)
  sort?: "relevance" | "quality" | "freshness" | "adoption",
  limit?: number,             // Default 10, max 50
}) → {
  results: AgenticAsset[],
  total: number,
  facets: {                   // Aggregations for filtering
    types: Record<string, number>,
    categories: Record<string, number>,
    platforms: Record<string, number>,
    tiers: Record<string, number>,
  }
}

// === RESOLVE: Intent-based discovery ===
tool("resolve", {
  intent: string,             // "I need to send emails from my agent"
  context?: {                 // Current environment
    platform: string,         // "claude-code"
    languages: string[],      // ["typescript", "python"]
    existingAssets: string[], // Already-installed asset IDs
  },
  limit?: number,
}) → {
  recommendations: {
    asset: AgenticAsset,
    relevanceScore: number,   // 0-1 how well it matches intent
    reasoning: string,        // Why this was recommended
  }[]
}

// === LOOKUP: Direct access ===
tool("lookup", {
  id: string,                 // "aaas-vault:skill:playwright-expert"
  // OR
  slug: string,
  type: AssetType,
}) → AgenticAsset              // Full entity with all fields

// === STACK: Complete solution recommendation ===
tool("stack", {
  useCase: string,            // "Build an automated code review pipeline"
  platform: string,           // "claude-code"
  constraints?: {
    maxCost: "free" | "freemium" | "any",
    maxComplexity: "beginner" | "intermediate" | "advanced",
    requiredLanguages: string[],
  }
}) → {
  agent: AgentAsset,
  tools: ToolAsset[],
  skills: SkillAsset[],
  mcpServers: McpServerAsset[],
  integrations: IntegrationAsset[],
  reasoning: string,
}

// === BROWSE: Structured navigation ===
tool("browse", {
  type?: AssetType,
  category?: string,
  page?: number,              // Pagination (10 per page)
  sort?: "name" | "quality" | "freshness" | "adoption",
}) → {
  items: AgenticAsset[],      // Compact view (no embedding, truncated description)
  total: number,
  page: number,
  pages: number,
  categories: string[],       // Available subcategories for drill-down
}
```

### 4.4 Search Architecture

```
                     ┌──────────────────────┐
                     │     MCP Client       │
                     │  (Claude Code, A0)   │
                     └─────────┬────────────┘
                               │ MCP Protocol
                     ┌─────────▼────────────┐
                     │   Agentic Index MCP  │
                     │      (Node.js)       │
                     └─────────┬────────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
    ┌─────────▼──────┐ ┌──────▼───────┐ ┌──────▼───────┐
    │  Keyword Index  │ │ Vector Index │ │  Graph Index │
    │   (SQLite FTS5) │ │  (SQLite +   │ │  (SQLite     │
    │                 │ │   vec ext)   │ │   relations) │
    └─────────────────┘ └──────────────┘ └──────────────┘
              │                │                │
              └────────────────┼────────────────┘
                               │
                     ┌─────────▼────────────┐
                     │   Unified Index DB   │
                     │  (SQLite, ~50MB)     │
                     │  agentic-index.db    │
                     └──────────────────────┘
```

**Why SQLite (not Firestore/Pinecone)?**

- Zero external dependencies — runs fully offline
- Embeddable in any agent's local environment
- FTS5 for keyword search + sqlite-vec for vector similarity
- Single file, portable, git-trackable (LFS for binary)
- Firestore/Pinecone remain the source-of-truth; SQLite is the local cache

**Hybrid Search Pipeline:**

```
Query: "playwright e2e testing for next.js"

1. KEYWORD (FTS5):    "playwright" AND "e2e" AND "testing" AND "next.js"
                      → 47 matches, BM25-scored

2. SEMANTIC (vec):    embed(query) → cosine_similarity(all embeddings)
                      → 50 nearest neighbors

3. MERGE:             RRF (Reciprocal Rank Fusion)
                      score = Σ 1/(k + rank_i) for each ranker
                      k = 60 (standard RRF constant)

4. FILTER:            Apply type/category/platform/tier filters

5. BOOST:             quality_tier boost: gold=1.2x, silver=1.0x, bronze=0.8x

6. RETURN:            Top N results with facet counts
```

---

## 5. Aggregation Pipeline

### 5.1 Data Sources & Ingestion

```
┌─────────────────────────────────────────────────────┐
│                 AGGREGATION PIPELINE                │
│                                                     │
│  ┌──────────────┐    ┌─────────────────────────┐   │
│  │  aaas-vault   │───▶│  vault-ingester.ts      │   │
│  │  (5,441 skills)│   │  Parse SKILL.md YAML    │   │
│  │  ~/Projects/   │   │  + qa-report.json tiers │   │
│  └──────────────┘    └────────────┬────────────┘   │
│                                   │                 │
│  ┌──────────────┐    ┌───────────▼─────────────┐   │
│  │  aaas.blog    │───▶│  firestore-ingester.ts  │   │
│  │  (800+ entities)│  │  Fetch all collections  │   │
│  │  Firestore     │   │  Map to unified schema  │   │
│  └──────────────┘    └────────────┬────────────┘   │
│                                   │                 │
│  ┌──────────────┐    ┌───────────▼─────────────┐   │
│  │  Harness      │───▶│  harness-ingester.ts    │   │
│  │  (~/.claude)   │   │  Read harness-index.json│   │
│  │  4,326 items   │   │  + agent/skill .md files│   │
│  └──────────────┘    └────────────┬────────────┘   │
│                                   │                 │
│  ┌──────────────┐    ┌───────────▼─────────────┐   │
│  │  aaas-blocks  │───▶│  blocks-ingester.ts     │   │
│  │  (12 code     │   │  Parse block.json +     │   │
│  │   blocks)     │   │  registry/index.json    │   │
│  └──────────────┘    └────────────┬────────────┘   │
│                                   │                 │
│  ┌──────────────┐    ┌───────────▼─────────────┐   │
│  │  MCP Registry │───▶│  mcp-registry-ingester  │   │
│  │  (npm, GitHub) │   │  npm search @modelcon.. │   │
│  │              │   │  + awesome-mcp-servers  │   │
│  └──────────────┘    └────────────┬────────────┘   │
│                                   │                 │
│                      ┌────────────▼────────────┐   │
│                      │    DEDUPLICATOR          │   │
│                      │  slug-match + fuzzy name │   │
│                      │  merge scores, keep best │   │
│                      └────────────┬────────────┘   │
│                                   │                 │
│                      ┌────────────▼────────────┐   │
│                      │    EMBEDDER              │   │
│                      │  Generate 1536-dim vecs  │   │
│                      │  from searchText field   │   │
│                      └────────────┬────────────┘   │
│                                   │                 │
│                      ┌────────────▼────────────┐   │
│                      │  SQLite Writer           │   │
│                      │  FTS5 + vec + relations  │   │
│                      │  → agentic-index.db      │   │
│                      └──────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

### 5.2 Ingester Details

#### vault-ingester.ts

```
Input:  ~/Projects/aaas-vault/skills/{category}/{skill}/SKILL.md
Parse:  YAML frontmatter → name, description, tags, version, compatibility, triggers
Enrich: qa-report.json → qualityTier, scores.quality
Map:    type="skill", source="aaas-vault"
        sourcePath="skills/{category}/{skill}/SKILL.md"
        sourceUrl="https://github.com/Supraforge/aaas-vault/tree/main/skills/..."
Output: 5,441 SkillAsset records
```

#### firestore-ingester.ts

```
Input:  Firestore collections: tools, models, agents, skills, scripts,
        benchmarks, datasets, papers, providers, hardware, integrations
Auth:   Firebase Admin SDK (service account)
Map:    Direct field mapping (blog schema ⊂ unified schema)
Dedup:  Skills that exist in both vault AND blog → merge, vault as sourcePath
Output: ~800 records (11 types)
```

#### harness-ingester.ts

```
Input:  ~/.claude/config/harness-index.json
        + Read actual .md files for richer metadata
Parse:  Agent .md → name, description from frontmatter
        Skill .md → full SKILL.md frontmatter
        Plugin manifests → installed_plugins.json
Map:    agents → type="agent", agentType="core"|"pool"
        skills → type="skill" (merge with vault if duplicate slug)
        plugins → type="plugin"
        templates → type="template"
Output: ~4,326 records (deduplicated against vault)
```

#### blocks-ingester.ts

```
Input:  Supraforge/aaas-blocks registry/index.json
        + registry/{layer}/{block-name}/block.json (full metadata)
        + registry/{layer}/{block-name}/README.md (documentation)
Auth:   GitHub API or local clone
Parse:  block.json → name, title, description, layer, category, tags,
        framework, frameworkVersion, requires, enhances, files,
        dependencies, devDependencies, envVars, verifiedWith
Map:    type="code-block", source="aaas-blocks"
        layer → subcategory
        requires/enhances → asset_relations
        verifiedWith → metadata.verifiedWith
        installCommand = "npx aaas-blocks add {name}"
        sourceUrl="https://github.com/Supraforge/aaas-blocks/tree/main/registry/..."
Routing: Discovery via Agentic Index → installation via aaas-blocks MCP
         (Index finds, Blocks installs — complementary, not redundant)
Output: ~12 CodeBlockAsset records (growing as blocks are added)
```

#### mcp-registry-ingester.ts

```
Input:  npm search "@modelcontextprotocol/*"
        + GitHub: awesome-mcp-servers, mcp-servers-registry
        + Local: ~/.claude/settings.json mcpServers config
Parse:  npm package.json → name, description, version, keywords
        README.md → tools list, transport type, config schema
Map:    type="mcp-server"
Output: ~1,000+ McpServerAsset records
```

### 5.3 Deduplication Strategy

```
For each new record:
  1. Exact slug match within same type → MERGE (update fields, keep highest scores)
  2. Fuzzy name match (Levenshtein ≤ 2) within same type → FLAG for review
  3. No match → INSERT as new

Merge priority (when same asset exists in multiple sources):
  aaas-blog > aaas-blocks > aaas-vault > harness > npm/github
  (Blog has richest metadata; blocks have verified code; vault has deepest content)

  Merge rule: take non-null field from highest-priority source
```

### 5.4 Build Schedule

```
Full rebuild:     Weekly (Sunday 02:00 UTC) via cron
Incremental:      On git push to aaas-vault main
                  On Firestore document change (Cloud Function trigger)
                  On harness-index.json rebuild (SessionStart hook)
Local refresh:    On MCP server startup if index > 24h old
```

---

## 6. ask.blog Integration

### 6.1 Bidirectional Sync

```
┌─────────────────┐                    ┌─────────────────┐
│   ask.blog       │                    │  Agentic Index   │
│   (aaas.blog/ask)│                    │  MCP Server      │
│                  │                    │                  │
│  Firestore ──────┼──── ingestion ────▶│  SQLite DB       │
│  (source of      │                    │  (local cache)   │
│   truth for      │                    │                  │
│   800+ entities) │                    │                  │
│                  │◀── enrichment ─────┼  New assets      │
│  Pinecone ───────┼──── vectors ──────▶│  discovered via  │
│  (semantic       │                    │  vault/harness/  │
│   search)        │                    │  npm ingestion   │
│                  │                    │                  │
│  /api/search ────┼──── fallback ─────▶│  When local DB   │
│  (web API)       │                    │  misses, query   │
│                  │                    │  blog API live   │
└─────────────────┘                    └─────────────────┘
```

### 6.2 New API Routes on ask.blog

```
POST /api/index/ingest    — Receive new assets from MCP build pipeline
GET  /api/index/export    — Export full index as JSON (for MCP rebuild)
GET  /api/index/delta     — Export changes since timestamp (for incremental sync)
POST /api/index/verify    — Mark asset as verified
```

### 6.3 Unified Search Contract

Both the MCP `search` tool and the ask.blog `/api/search` endpoint will share the **same query interface**:

```typescript
interface SearchRequest {
  query: string;
  type?: AssetType[];
  category?: string[];
  domain?: string[];
  platform?: string[];
  qualityTier?: ("gold" | "silver" | "bronze")[];
  minScore?: number;
  sort?: "relevance" | "quality" | "freshness" | "adoption";
  limit?: number;
  offset?: number;
}

interface SearchResponse {
  results: AgenticAsset[];
  total: number;
  facets: {
    types: Record<string, number>;
    categories: Record<string, number>;
    platforms: Record<string, number>;
    tiers: Record<string, number>;
  };
  source: "local" | "remote" | "hybrid";
}
```

This means the MCP server can operate in three modes:

1. **Offline** — SQLite only (airplane mode, no network)
2. **Online** — Firestore/Pinecone via ask.blog API (richest, freshest)
3. **Hybrid** — Local SQLite first, fall back to remote for misses

---

## 7. Repository Structure

```
aaas-vault/
├── skills/                      # Existing: 5,441 skills
├── scripts/
│   ├── clean_and_score.py       # Existing: QA pipeline
│   └── qa-report.json           # Existing: Quality report
├── SKILLS_MANIFEST.json         # Existing → DEPRECATED by index
├── CONTEXT_BRIDGE.md            # Existing
├── README.md                    # Existing
│
├── index/                       # NEW: Agentic Index MCP
│   ├── package.json             # @supraforge/mcp-agentic-index
│   ├── tsconfig.json
│   ├── src/
│   │   ├── server.ts            # MCP server entrypoint
│   │   ├── tools/               # MCP tool implementations
│   │   │   ├── search.ts        # Hybrid search
│   │   │   ├── resolve.ts       # Intent-based discovery
│   │   │   ├── lookup.ts        # Direct access
│   │   │   ├── browse.ts        # Structured navigation
│   │   │   ├── compare.ts       # Side-by-side comparison
│   │   │   ├── related.ts       # Relationship graph
│   │   │   ├── recommend.ts     # Smart recommendation
│   │   │   ├── stack.ts         # Full stack suggestion
│   │   │   ├── stats.ts         # Index statistics
│   │   │   └── submit.ts        # Asset submission
│   │   ├── ingesters/           # Data source connectors
│   │   │   ├── vault.ts         # aaas-vault SKILL.md parser
│   │   │   ├── firestore.ts     # aaas.blog Firestore reader
│   │   │   ├── harness.ts       # ~/.claude harness reader
│   │   │   ├── blocks.ts        # aaas-blocks registry reader
│   │   │   ├── mcp-registry.ts  # npm/GitHub MCP discovery
│   │   │   └── dedup.ts         # Cross-source deduplication
│   │   ├── search/              # Search engine
│   │   │   ├── keyword.ts       # FTS5 keyword search
│   │   │   ├── semantic.ts      # Vector similarity search
│   │   │   ├── hybrid.ts        # RRF fusion
│   │   │   └── embedder.ts      # Embedding generation
│   │   ├── db/                  # Database layer
│   │   │   ├── schema.sql       # SQLite schema (FTS5 + vec)
│   │   │   ├── migrations/      # Schema migrations
│   │   │   └── client.ts        # DB connection + queries
│   │   └── types.ts             # Unified schema types
│   ├── build.ts                 # Full index rebuild script
│   ├── agentic-index.db         # Built index (gitignored)
│   └── tests/
│       ├── search.test.ts
│       ├── ingest.test.ts
│       └── fixtures/
│
└── .spec/
    └── agentic-index-mcp.md     # This document
```

---

## 8. SQLite Schema

```sql
-- Core entity table
CREATE TABLE assets (
  id TEXT PRIMARY KEY,           -- "aaas-vault:skill:playwright-expert"
  slug TEXT NOT NULL,
  type TEXT NOT NULL,            -- One of 16 types
  name TEXT NOT NULL,
  category TEXT,
  subcategory TEXT,
  description TEXT,
  provider TEXT,
  version TEXT,
  license TEXT,
  pricing_model TEXT,
  source TEXT NOT NULL,          -- "aaas-vault" | "aaas-blog" | "harness" | ...
  source_url TEXT,
  source_path TEXT,
  quality_tier TEXT,
  schema_completeness REAL,

  -- Scores (denormalized for fast filtering)
  score_adoption REAL DEFAULT 0,
  score_quality REAL DEFAULT 0,
  score_freshness REAL DEFAULT 0,
  score_citations REAL DEFAULT 0,
  score_engagement REAL DEFAULT 0,
  score_composite REAL DEFAULT 0,

  -- Temporal
  added_date TEXT,
  last_updated TEXT,
  last_verified TEXT,

  -- Full JSON for type-specific fields
  metadata JSON,                -- All type-specific extensions

  -- Searchable text blob
  search_text TEXT
);

-- Full-text search index
CREATE VIRTUAL TABLE assets_fts USING fts5(
  name, description, search_text,
  content='assets',
  content_rowid='rowid',
  tokenize='porter unicode61'
);

-- Vector similarity index (sqlite-vec)
CREATE VIRTUAL TABLE assets_vec USING vec0(
  id TEXT PRIMARY KEY,
  embedding float[1536]
);

-- Array fields (normalized)
CREATE TABLE asset_tags (
  asset_id TEXT REFERENCES assets(id),
  tag TEXT,
  PRIMARY KEY (asset_id, tag)
);

CREATE TABLE asset_domains (
  asset_id TEXT REFERENCES assets(id),
  domain TEXT,
  PRIMARY KEY (asset_id, domain)
);

CREATE TABLE asset_platforms (
  asset_id TEXT REFERENCES assets(id),
  platform TEXT,
  PRIMARY KEY (asset_id, platform)
);

CREATE TABLE asset_capabilities (
  asset_id TEXT REFERENCES assets(id),
  capability TEXT
);

CREATE TABLE asset_use_cases (
  asset_id TEXT REFERENCES assets(id),
  use_case TEXT
);

CREATE TABLE asset_triggers (
  asset_id TEXT REFERENCES assets(id),
  trigger_phrase TEXT
);

-- Relationships (graph edges)
CREATE TABLE asset_relations (
  source_id TEXT REFERENCES assets(id),
  target_id TEXT REFERENCES assets(id),
  relation_type TEXT,            -- "requires" | "enhances" | "alternative" | "related"
  PRIMARY KEY (source_id, target_id, relation_type)
);

-- Index statistics
CREATE TABLE index_meta (
  key TEXT PRIMARY KEY,
  value TEXT
);

-- Useful indexes
CREATE INDEX idx_assets_type ON assets(type);
CREATE INDEX idx_assets_category ON assets(category);
CREATE INDEX idx_assets_source ON assets(source);
CREATE INDEX idx_assets_tier ON assets(quality_tier);
CREATE INDEX idx_assets_composite ON assets(score_composite DESC);
CREATE INDEX idx_tags_tag ON asset_tags(tag);
CREATE INDEX idx_domains_domain ON asset_domains(domain);
CREATE INDEX idx_platforms_platform ON asset_platforms(platform);
CREATE INDEX idx_relations_target ON asset_relations(target_id);
```

---

## 9. Implementation Phases

### Phase 1: Foundation (Week 1-2)

**Goal:** Working MCP server with vault ingestion + keyword search

- [ ] Initialize `index/` package with TypeScript + MCP SDK
- [ ] Implement SQLite schema + FTS5
- [ ] Build `vault-ingester.ts` — parse all 5,441 SKILL.md files
- [ ] Implement `search` tool (keyword only, FTS5)
- [ ] Implement `lookup` and `browse` tools
- [ ] Register MCP in Claude Code settings.json
- [ ] Test: search for skills by name, category, keyword

### Phase 2: Multi-Source (Week 3-4)

**Goal:** Ingest all four data sources, deduplication working

- [ ] Build `harness-ingester.ts` — read harness-index.json + .md files
- [ ] Build `firestore-ingester.ts` — connect to aaas.blog Firestore
- [ ] Build `mcp-registry-ingester.ts` — npm + GitHub discovery
- [ ] Implement `dedup.ts` — slug-match + fuzzy name merge
- [ ] Build `build.ts` — full pipeline orchestrator
- [ ] Implement `stats` tool
- [ ] Test: 10,000+ entities across all sources, zero duplicates

### Phase 3: Semantic Search (Week 5-6)

**Goal:** Vector embeddings + hybrid search + recommendations

- [ ] Integrate sqlite-vec extension
- [ ] Build `embedder.ts` — generate embeddings (OpenAI or local model)
- [ ] Implement hybrid search (RRF fusion)
- [ ] Implement `resolve` tool (intent-based discovery)
- [ ] Implement `recommend` tool
- [ ] Implement `stack` tool
- [ ] Test: "I need to send emails" → returns Resend, SendGrid, SES skills/tools

### Phase 4: ask.blog Integration (Week 7-8)

**Goal:** Bidirectional sync, unified search contract

- [ ] Add `/api/index/export` and `/api/index/delta` routes to aaas.blog
- [ ] Add `/api/index/ingest` for MCP→blog asset submission
- [ ] Implement online/offline/hybrid search modes in MCP
- [ ] Shared SearchRequest/SearchResponse types (shared package)
- [ ] Cloud Function trigger: on Firestore change → rebuild delta
- [ ] Test: MCP search returns same results as ask.blog/ask

### Phase 5: Production Hardening (Week 9-10)

**Goal:** npm publishable, documentation, CI/CD

- [ ] npm package: `@supraforge/mcp-agentic-index`
- [ ] Docker image for self-hosted deployment
- [ ] Auto-rebuild via GitHub Actions (on vault push)
- [ ] Pre-built index artifact (GitHub Releases, ~50MB)
- [ ] README + integration guides for Claude Code, Agent Zero, Cursor
- [ ] Rate limiting, caching, error handling
- [ ] Telemetry: search queries → aggregated insights (no PII)

---

## 10. Expected Scale

| Metric             | Phase 1   | Phase 2 | Phase 3 | Phase 5         |
| ------------------ | --------- | ------- | ------- | --------------- |
| **Total entities** | 5,441     | ~11,000 | ~11,000 | 15,000+         |
| **Entity types**   | 1 (skill) | 17      | 17      | 17              |
| **Sources**        | 1 (vault) | 5       | 5       | 5+              |
| **Search modes**   | Keyword   | Keyword | Hybrid  | Hybrid + remote |
| **DB size**        | ~10MB     | ~30MB   | ~50MB   | ~60MB           |
| **Query latency**  | <50ms     | <100ms  | <200ms  | <200ms          |
| **MCP tools**      | 3         | 5       | 9       | 11              |

---

## 11. Integration with Existing Infrastructure

### Claude Code (settings.json)

```json
{
  "mcpServers": {
    "agentic-index": {
      "command": "node",
      "args": ["~/Projects/aaas-vault/index/dist/server.js"],
      "env": {
        "AGENTIC_INDEX_DB": "~/Projects/aaas-vault/index/agentic-index.db",
        "AGENTIC_INDEX_MODE": "hybrid"
      }
    }
  }
}
```

### Harness Hook (auto-refresh)

```json
{
  "SessionStart": [
    {
      "matcher": "*",
      "hooks": [
        {
          "type": "command",
          "command": "node ~/Projects/aaas-vault/index/build.js --incremental --if-stale",
          "timeout": 30,
          "async": true
        }
      ]
    }
  ]
}
```

### Agent Pool Integration

When an agent needs a capability it doesn't have:

```
Agent: "I need to interact with Jira"
  → MCP search("jira integration", type=["mcp-server", "skill", "api-endpoint"])
  → Returns: mcp-server:atlassian-mcp (score: 92), skill:jira (score: 87)
  → Agent installs/activates the top result
```

---

## 12. Competitive Advantage

This MCP is unique because:

1. **Multi-source aggregation** — no other index combines skills + MCPs + APIs + agents + tools
2. **Offline-first** — works without network (SQLite), scales to cloud (Firestore)
3. **Quality-scored** — every asset has a composite quality score, not just a name
4. **Relationship-aware** — knows what works together, what's an alternative
5. **Intent-based** — "I need to do X" resolves to concrete assets, not keyword matches
6. **Platform-agnostic** — works with any MCP-compatible agent platform
7. **Self-healing** — ingestion pipeline auto-discovers new assets from registries
8. **ask.blog synergy** — public web discovery + private agent discovery from same data
9. **aaas-blocks chain** — Index discovers, Blocks installs: two MCPs that compose into a complete workflow

---

## 12a. Relationship to aaas-blocks

**aaas-blocks** (`@supraforge/aaas-blocks`) is an existing MCP server with 5 tools that serves as a **specialized installer** for composable Next.js code patterns. The Agentic Index is the **universal finder**.

```
Role separation:
┌─────────────────────────┐     ┌──────────────────────────┐
│   Agentic Index MCP     │     │   aaas-blocks MCP        │
│   (horizontal discovery)│     │   (vertical installer)   │
│                         │     │                          │
│   search / resolve      │────▶│   get_block / get_code   │
│   "what solves auth     │     │   "install auth/clerk"   │
│    for Next.js?"        │     │                          │
│                         │     │   check_compatibility    │
│   17 asset types        │     │   12 code blocks         │
│   5+ data sources       │     │   3 layers               │
│   11,000+ entities      │     │   Next.js 16 only        │
└─────────────────────────┘     └──────────────────────────┘
```

**Integration pattern:**

1. Agent queries Agentic Index: `resolve("auth for Next.js app")`
2. Index returns `code-block:auth/clerk` (score: 95) among other results
3. Agent sees `installCommand: "npx aaas-blocks add auth/clerk"` or routes to blocks MCP
4. Blocks MCP handles installation: `get_block_code("auth/clerk")` → files + deps

**Shared schema lineage:**

- `BlockJson.requires` / `enhances` → maps to `AgenticAsset.requires` / `enhances`
- `BlockJson.tags` → maps to `AgenticAsset.tags`
- `BlockJson.layer` → maps to `CodeBlockAsset.layer` (foundation/integration/feature)
- `BlockJson.verifiedWith` → maps to `CodeBlockAsset.verifiedWith` (version pinning)

**Not redundant:** Blocks MCP stays focused on its strength (curated, installable, version-verified code). The Index adds cross-ecosystem discovery that blocks alone cannot provide.

---

## 13. Open Questions

1. **Embedding model**: OpenAI text-embedding-3-small (API cost) vs. local model (no cost, slower)?
   [ASSUMPTION] Start with OpenAI for quality, add local fallback later.

2. **Pre-built index distribution**: GitHub Releases (~50MB binary) or npm postinstall script?
   [ASSUMPTION] GitHub Releases + optional rebuild command. npm postinstall for convenience.

3. **Write permissions**: Should any agent be able to submit new assets, or only authenticated?
   [ASSUMPTION] Read is open, write requires agent JWT (via secrets-manager `agent_create`).

4. **MCP server registry ingestion**: npm `@modelcontextprotocol/*` only, or broader?
   [ASSUMPTION] Start with official MCP packages + awesome-mcp-servers list, expand later.

5. **Vault manifest migration**: Replace SKILLS_MANIFEST.json with agentic-index.db export?
   [ASSUMPTION] Yes. Deprecate manifest, generate from index for backwards compat.
