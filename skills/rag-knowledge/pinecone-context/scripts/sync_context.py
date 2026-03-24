#!/usr/bin/env python3
"""
AntiGravity Context Layer — Pinecone Sync Engine
Syncs skills, directives, system registry, and client context to a
Pinecone integrated index (multilingual-e5-large).

Usage:
  python3 skills/pinecone-context/scripts/sync_context.py --namespace skills
  python3 skills/pinecone-context/scripts/sync_context.py --namespace directives
  python3 skills/pinecone-context/scripts/sync_context.py --namespace system-registry
  python3 skills/pinecone-context/scripts/sync_context.py --all
  python3 skills/pinecone-context/scripts/sync_context.py --list

Requires:
  pip install pinecone
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

try:
    from pinecone import Pinecone
except ImportError:
    sys.exit("Error: pinecone not installed. Run: pip install pinecone")

# ── Configuration ────────────────────────────────────────────────────────────

GEMINI_ROOT = Path.home() / ".gemini"
PROJECT_DIR = Path(__file__).resolve().parent.parent.parent  # skills/pinecone-context/scripts/ → base/
CONFIG_FILE = PROJECT_DIR / "context" / "pinecone_config.json"

# Default paths (can be overridden by config file)
VAULT_PATH = GEMINI_ROOT / "antigravity-vault" / "skills"
DIRECTIVES_PATH = PROJECT_DIR / "directives"
SYSTEM_REGISTRY_PATH = GEMINI_ROOT / ".system-registry"
BASE_SKILLS_PATH = PROJECT_DIR / "skills"

BATCH_SIZE = 96  # Pinecone integrated index max per batch


def load_config() -> dict:
    """Load config from context/pinecone_config.json or use defaults."""
    defaults = {
        "index_name": "antigravity-context",
        "client_context_sources": {},
    }
    if CONFIG_FILE.exists():
        try:
            user_config = json.loads(CONFIG_FILE.read_text())
            defaults.update(user_config)
        except Exception:
            pass
    return defaults


def load_api_key() -> str:
    """Load Pinecone API key from environment or .env files."""
    key = os.environ.get("PINECONE_API_KEY") or os.environ.get("PINECONE_API")
    if key:
        return key
    # Search .env files
    env_paths = [
        PROJECT_DIR / ".env",
        GEMINI_ROOT / "base" / ".env",
    ]
    for env_path in env_paths:
        if env_path.exists():
            for line in env_path.read_text().splitlines():
                if line.startswith(("PINECONE_API_KEY=", "PINECONE_API=")):
                    return line.split("=", 1)[1].strip()
    sys.exit("Error: PINECONE_API_KEY not found. Set it in .env or environment.")


def doc_id(filepath: str) -> str:
    """Deterministic ID from filepath (16-char hex)."""
    return hashlib.md5(filepath.encode()).hexdigest()[:16]


def parse_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter fields from markdown."""
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}
    meta = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.strip().startswith("|"):
            key, _, val = line.partition(":")
            key = key.strip().strip('"')
            val = val.strip().strip('"').strip("'")
            if val and not val.startswith("|"):
                meta[key] = val
    return meta


def read_file_safe(path: Path) -> str:
    """Read file with fallback encoding."""
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="latin-1")
    except Exception:
        return ""


# ── Namespace collectors ─────────────────────────────────────────────────────

def collect_skills() -> list[dict]:
    """Collect all SKILL.md files from vault + base skills."""
    records = []
    skill_files = []
    if VAULT_PATH.exists():
        skill_files.extend(VAULT_PATH.rglob("SKILL.md"))
    if BASE_SKILLS_PATH.exists():
        skill_files.extend(BASE_SKILLS_PATH.rglob("SKILL.md"))

    for path in skill_files:
        content = read_file_safe(path)
        if not content or len(content) < 20:
            continue

        meta = parse_frontmatter(content)
        try:
            rel = path.relative_to(VAULT_PATH) if str(path).startswith(str(VAULT_PATH)) else path.relative_to(BASE_SKILLS_PATH)
            parts = rel.parts
        except ValueError:
            parts = (path.parent.name,)

        category = parts[0] if len(parts) > 0 else "uncategorized"
        subcategory = parts[1] if len(parts) > 1 else "general"

        if len(content) > 8000:
            content = content[:8000] + "\n\n[truncated]"

        records.append({
            "_id": doc_id(str(path)),
            "content": content,
            "name": meta.get("name", subcategory),
            "description": meta.get("description", "")[:500],
            "category": category,
            "subcategory": subcategory,
            "source": "vault" if str(path).startswith(str(VAULT_PATH)) else "base",
            "doc_type": "skill",
        })

    return records


def collect_directives() -> list[dict]:
    """Collect directive markdown files."""
    records = []
    if not DIRECTIVES_PATH.exists():
        return records
    for path in DIRECTIVES_PATH.glob("*.md"):
        content = read_file_safe(path)
        if not content:
            continue
        if len(content) > 8000:
            content = content[:8000] + "\n\n[truncated]"
        records.append({
            "_id": doc_id(str(path)),
            "content": content,
            "name": path.stem,
            "description": f"Operational directive: {path.stem.replace('_', ' ')}",
            "category": "directive",
            "subcategory": path.stem,
            "source": "base",
            "doc_type": "directive",
        })
    return records


def collect_system_registry() -> list[dict]:
    """Collect system registry docs."""
    records = []
    if not SYSTEM_REGISTRY_PATH.exists():
        return records
    for path in SYSTEM_REGISTRY_PATH.rglob("*.md"):
        content = read_file_safe(path)
        if not content:
            continue
        if len(content) > 8000:
            content = content[:8000] + "\n\n[truncated]"
        records.append({
            "_id": doc_id(str(path)),
            "content": content,
            "name": path.stem,
            "description": f"System registry: {path.stem.replace('_', ' ')}",
            "category": "infrastructure",
            "subcategory": path.stem,
            "source": "system-registry",
            "doc_type": "registry",
        })
    return records


def collect_client_context(client_name: str, source_path: Path) -> list[dict]:
    """Collect client-specific context documents."""
    if not source_path.exists():
        print(f"  Warning: Path not found for {client_name}: {source_path}")
        return []
    records = []
    for path in source_path.rglob("*"):
        if not path.is_file() or path.suffix not in (".md", ".txt", ".json") or path.name.startswith("."):
            continue
        content = read_file_safe(path)
        if not content or len(content) < 10:
            continue
        rel = path.relative_to(source_path)
        parts = rel.parts
        category = parts[0] if parts else "general"
        if len(content) > 8000:
            content = content[:8000] + "\n\n[truncated]"
        records.append({
            "_id": doc_id(str(path)),
            "content": content,
            "name": path.stem,
            "description": f"Client context: {path.stem}",
            "category": category,
            "subcategory": parts[1] if len(parts) > 1 else "general",
            "source": client_name,
            "doc_type": "context",
        })
    return records


# ── Sync engine ──────────────────────────────────────────────────────────────

COLLECTORS = {
    "skills": collect_skills,
    "directives": collect_directives,
    "system-registry": collect_system_registry,
}


def sync_namespace(pc, index_name: str, namespace: str, client_sources: dict) -> dict:
    """Sync a single namespace. Returns stats dict."""
    index = pc.Index(index_name)

    if namespace in COLLECTORS:
        records = COLLECTORS[namespace]()
    elif namespace in client_sources:
        records = collect_client_context(namespace, Path(client_sources[namespace]))
    else:
        print(f"  Error: Unknown namespace '{namespace}'")
        return {"namespace": namespace, "status": "error", "count": 0}

    if not records:
        return {"namespace": namespace, "status": "empty", "count": 0}

    print(f"  Syncing {len(records)} records to {index_name}/{namespace}...")

    total_batches = (len(records) + BATCH_SIZE - 1) // BATCH_SIZE
    failed_batches = []

    for i in range(0, len(records), BATCH_SIZE):
        batch = records[i : i + BATCH_SIZE]
        batch_num = i // BATCH_SIZE + 1
        retries = 0
        while retries < 3:
            try:
                index.upsert_records(namespace, batch)
                break
            except Exception as e:
                if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                    retries += 1
                    wait = 30 * retries
                    print(f"  Rate limited on batch {batch_num}/{total_batches}, waiting {wait}s (retry {retries}/3)...")
                    time.sleep(wait)
                else:
                    print(f"  Batch {batch_num}/{total_batches} failed: {e}")
                    failed_batches.append(batch_num)
                    break
        else:
            failed_batches.append(batch_num)

        if batch_num % 10 == 0 or batch_num == total_batches:
            print(f"  Batch {batch_num}/{total_batches} complete")

    print(f"  Done: {len(records)} records → {namespace}")
    return {"namespace": namespace, "status": "success", "count": len(records)}


def main():
    parser = argparse.ArgumentParser(description="AntiGravity Context Layer — Pinecone Sync")
    parser.add_argument("--namespace", type=str, help="Namespace to sync")
    parser.add_argument("--all", action="store_true", help="Sync all namespaces")
    parser.add_argument("--list", action="store_true", help="List available namespaces")
    args = parser.parse_args()

    config = load_config()
    index_name = config["index_name"]
    client_sources = config.get("client_context_sources", {})

    if args.list:
        print("Available namespaces:")
        for ns in COLLECTORS:
            print(f"  - {ns}")
        for ns in client_sources:
            print(f"  - {ns} (client)")
        return

    if not args.namespace and not args.all:
        parser.print_help()
        return

    api_key = load_api_key()
    pc = Pinecone(api_key=api_key)

    try:
        pc.describe_index(index_name)
    except Exception as e:
        sys.exit(f"Error: Index '{index_name}' not found. Create it first.\n{e}")

    namespaces = list(COLLECTORS.keys()) + list(client_sources.keys()) if args.all else [args.namespace]

    print(f"\n{'='*60}")
    print(f"AntiGravity Context Sync → Pinecone ({index_name})")
    print(f"{'='*60}\n")

    start = time.time()
    results = []
    for ns in namespaces:
        print(f"\n[{ns}]")
        result = sync_namespace(pc, index_name, ns, client_sources)
        results.append(result)

    elapsed = time.time() - start

    print(f"\n{'='*60}")
    print(f"Sync Summary ({elapsed:.1f}s)")
    print(f"{'='*60}")
    total = 0
    for r in results:
        icon = "✅" if r["status"] == "success" else "⚠️" if r["status"] == "empty" else "❌"
        count = r.get("count", 0)
        total += count
        print(f"  {icon} {r['namespace']}: {count} records")
    print(f"\n  Total: {total} records synced")


if __name__ == "__main__":
    main()
