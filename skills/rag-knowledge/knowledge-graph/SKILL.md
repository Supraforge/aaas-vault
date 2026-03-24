---
name: knowledge-graph
version: "1.0.0"
description: "SQLite-backed entity/relationship knowledge graph with decay and traversal. Extracted from GravityClaw."
dependencies:
  - sqlite3 (built-in)
  - pinecone (optional, for hybrid search)
tags: [memory, knowledge, graph, entities, relationships]
---

# Knowledge Graph — Entity/Relationship Memory

> Extracted from GravityClaw's production knowledge graph system. Provides structured entity and relationship storage beyond simple vector search.

## Why Knowledge Graphs + Vector Search

| Feature | Vector Search (Pinecone) | Knowledge Graph (SQLite) |
|---------|-------------------------|--------------------------|
| **Query type** | "Find similar to X" | "What relates to X?" |
| **Best for** | Semantic similarity, fuzzy recall | Structured relationships, traversal |
| **Data model** | Flat documents with embeddings | Entities + typed relationships |
| **Traversal** | No | BFS/DFS across relationships |
| **Deduplication** | Embedding distance | Entity name normalization |
| **Decay** | Manual TTL | Automatic confidence decay |

**Use both together**: Vector search for discovery, knowledge graph for structured reasoning.

## Schema

```sql
-- Entities: People, companies, concepts, tools, projects
CREATE TABLE entities (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL,           -- person|company|concept|tool|project|topic
    description TEXT,
    metadata TEXT,                -- JSON blob for flexible attributes
    confidence REAL DEFAULT 1.0, -- 0.0 to 1.0 (decays over time)
    source TEXT,                  -- Where this entity was learned
    created_at TEXT DEFAULT (datetime('now')),
    updated_at TEXT DEFAULT (datetime('now')),
    last_accessed TEXT            -- For access-based decay
);

-- Relationships: Typed edges between entities
CREATE TABLE relationships (
    id TEXT PRIMARY KEY,
    source_id TEXT NOT NULL REFERENCES entities(id),
    target_id TEXT NOT NULL REFERENCES entities(id),
    type TEXT NOT NULL,           -- works_at|founded|uses|competes_with|part_of|related_to
    weight REAL DEFAULT 1.0,     -- Relationship strength (0.0 to 1.0)
    metadata TEXT,                -- JSON: context, evidence, timestamps
    created_at TEXT DEFAULT (datetime('now')),
    UNIQUE(source_id, target_id, type)
);

-- Indexes for fast traversal
CREATE INDEX idx_entities_type ON entities(type);
CREATE INDEX idx_entities_name ON entities(name);
CREATE INDEX idx_rel_source ON relationships(source_id);
CREATE INDEX idx_rel_target ON relationships(target_id);
CREATE INDEX idx_rel_type ON relationships(type);
```

## Core Operations

### Add Entity
```python
def add_entity(name: str, type: str, description: str = None, metadata: dict = None) -> str:
    """Add or update an entity. Returns entity ID."""
    entity_id = normalize_id(name, type)
    existing = db.get(entity_id)
    if existing:
        # Merge: boost confidence, update description if richer
        merge_entity(existing, description, metadata)
    else:
        db.insert(entity_id, name, type, description, json.dumps(metadata))
    return entity_id
```

### Add Relationship
```python
def add_relationship(source: str, target: str, rel_type: str, weight: float = 1.0) -> str:
    """Create a typed edge between two entities."""
    # Entities must exist
    assert db.get(source) and db.get(target)
    db.upsert_relationship(source, target, rel_type, weight)
```

### Traverse (BFS)
```python
def traverse(start_id: str, max_depth: int = 3, rel_types: list = None) -> dict:
    """BFS traversal from an entity. Returns subgraph."""
    visited = set()
    queue = [(start_id, 0)]
    subgraph = {"entities": [], "relationships": []}

    while queue:
        entity_id, depth = queue.pop(0)
        if entity_id in visited or depth > max_depth:
            continue
        visited.add(entity_id)

        entity = db.get(entity_id)
        subgraph["entities"].append(entity)

        rels = db.get_relationships(entity_id, rel_types)
        for rel in rels:
            subgraph["relationships"].append(rel)
            neighbor = rel["target_id"] if rel["source_id"] == entity_id else rel["source_id"]
            queue.append((neighbor, depth + 1))

    return subgraph
```

### Search
```python
def search_entities(query: str, type: str = None, limit: int = 10) -> list:
    """Fuzzy search entities by name/description."""
    sql = "SELECT * FROM entities WHERE name LIKE ? OR description LIKE ?"
    if type:
        sql += " AND type = ?"
    sql += " ORDER BY confidence DESC LIMIT ?"
    return db.execute(sql, params)
```

## Confidence Decay

Entities lose confidence over time if not accessed:

```python
def apply_decay(half_life_days: int = 30):
    """Reduce confidence of entities not accessed recently."""
    decay_factor = 0.5 ** (days_since_access / half_life_days)
    db.execute("""
        UPDATE entities
        SET confidence = confidence * ?
        WHERE last_accessed < datetime('now', '-7 days')
    """, (decay_factor,))
```

**Access refreshes confidence**: Every time an entity is queried or referenced, its `last_accessed` and `confidence` are boosted back toward 1.0.

## Relationship Types

| Type | Example | Direction |
|------|---------|-----------|
| `works_at` | Person → Company | Directed |
| `founded` | Person → Company | Directed |
| `uses` | Project → Tool | Directed |
| `competes_with` | Company ↔ Company | Bidirectional |
| `part_of` | Concept → Topic | Directed |
| `related_to` | Entity ↔ Entity | Bidirectional |
| `depends_on` | Tool → Tool | Directed |
| `invested_in` | Company → Company | Directed |
| `authored` | Person → Paper | Directed |
| `mentioned_in` | Entity → Source | Directed |

## Memory Evolution

The knowledge graph supports **memory evolution** — automatic refinement over time:

1. **Merge duplicates**: When a new entity matches an existing one (fuzzy name match >0.85), merge metadata rather than creating a duplicate
2. **Strengthen paths**: When a relationship is observed multiple times from different sources, increase its weight
3. **Prune weak nodes**: Entities with confidence <0.1 after decay are candidates for removal
4. **Promote patterns**: Frequently traversed paths become "strong connections" (weight >0.8)

```python
def evolve():
    """Run evolution cycle: merge → strengthen → prune → promote."""
    merged = merge_duplicate_entities(threshold=0.85)
    strengthened = strengthen_frequent_relationships()
    pruned = prune_weak_entities(min_confidence=0.1)
    promoted = promote_strong_paths(min_weight=0.8)
    return {"merged": merged, "strengthened": strengthened, "pruned": pruned, "promoted": promoted}
```

## Usage

```bash
# Initialize the knowledge graph database
python3 skills/knowledge-graph/scripts/init_db.py

# Add entities from a research scan
python3 skills/knowledge-graph/scripts/ingest.py --source=.tmp/scout_results.json

# Query the graph
python3 skills/knowledge-graph/scripts/query.py --entity="Anthropic" --depth=2

# Run evolution cycle
python3 skills/knowledge-graph/scripts/evolve.py

# Export subgraph as JSON
python3 skills/knowledge-graph/scripts/export.py --entity="AI agents" --format=json
```

## Integration with Base Skills

```
scout-research (discovers entities)
    → knowledge-graph (stores structured relationships)
    → pinecone (stores embeddings for semantic search)
    → research-protocol Phase 3 (strategy uses graph traversal)
```
