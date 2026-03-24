#!/usr/bin/env python3
"""
AntiGravity Context Layer — Semantic Query
Search the Pinecone context index for skills, directives, or any content.

Usage:
  python3 skills/pinecone-context/scripts/query_context.py "email automation"
  python3 skills/pinecone-context/scripts/query_context.py "brand guidelines" --namespace directives
  python3 skills/pinecone-context/scripts/query_context.py "firebase hosting" --top 10
"""

import argparse
import json
import os
import sys
from pathlib import Path

try:
    from pinecone import Pinecone
except ImportError:
    sys.exit("Error: pinecone not installed. Run: pip install pinecone")

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
GEMINI_ROOT = Path.home() / ".gemini"
CONFIG_FILE = PROJECT_DIR / "context" / "pinecone_config.json"


def load_config() -> dict:
    defaults = {"index_name": "antigravity-context"}
    if CONFIG_FILE.exists():
        try:
            defaults.update(json.loads(CONFIG_FILE.read_text()))
        except Exception:
            pass
    return defaults


def load_api_key() -> str:
    key = os.environ.get("PINECONE_API_KEY") or os.environ.get("PINECONE_API")
    if key:
        return key
    for env_path in [PROJECT_DIR / ".env", GEMINI_ROOT / "base" / ".env"]:
        if env_path.exists():
            for line in env_path.read_text().splitlines():
                if line.startswith(("PINECONE_API_KEY=", "PINECONE_API=")):
                    return line.split("=", 1)[1].strip()
    sys.exit("Error: PINECONE_API_KEY not found.")


def main():
    parser = argparse.ArgumentParser(description="Query AntiGravity context layer")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--namespace", default="skills", help="Namespace to search (default: skills)")
    parser.add_argument("--top", type=int, default=5, help="Number of results (default: 5)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    config = load_config()
    api_key = load_api_key()
    pc = Pinecone(api_key=api_key)
    index = pc.Index(config["index_name"])

    results = index.search(
        namespace=args.namespace,
        query={"inputs": {"text": args.query}, "top_k": args.top},
    )

    hits = results.get("result", {}).get("hits", [])

    if args.json:
        print(json.dumps(hits, indent=2))
        return

    if not hits:
        print(f"No results for '{args.query}' in namespace '{args.namespace}'")
        return

    print(f"\n🔍 Results for '{args.query}' in [{args.namespace}]:\n")
    for i, hit in enumerate(hits, 1):
        fields = hit.get("fields", {})
        score = hit.get("_score", 0)
        name = fields.get("name", "unknown")
        desc = fields.get("description", "")[:120]
        category = fields.get("category", "")
        source = fields.get("source", "")

        print(f"  {i}. [{score:.3f}] {name}")
        if desc:
            print(f"     {desc}")
        if category:
            print(f"     📁 {category}/{source}")
        print()


if __name__ == "__main__":
    main()
