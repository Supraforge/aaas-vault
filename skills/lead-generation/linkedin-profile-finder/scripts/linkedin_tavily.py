#!/usr/bin/env python3
"""
LinkedIn Profile Finder via Tavily Search API.
Finds LinkedIn profile URLs by searching for site:linkedin.com/in profiles
matching ICP criteria. ~$24 for 50K profiles.

Requires: TAVILY_API_KEY in .env (already configured)

Pricing:
  - Free: 1,000 searches/month (~17K profiles)
  - Pay-as-you-go: $0.008/search (~17 profiles each)
  - 50K profiles ≈ 2,940 searches ≈ $24

Usage:
  # Single ICP query
  python3 linkedin_tavily.py -q "CISO cybersecurity San Francisco" -o results.json

  # Batch mode
  python3 linkedin_tavily.py -b queries.json -o results.json

  # Generate ICP queries
  python3 linkedin_tavily.py --generate-queries \
    --titles "CISO,Head of Security" \
    --industries "fintech,cybersecurity" \
    --locations "San Francisco,New York" \
    --output-queries queries.json

  # Dry run
  python3 linkedin_tavily.py -b queries.json --dry-run

  # URLs only
  python3 linkedin_tavily.py -b queries.json --urls-only -o urls.txt
"""

import argparse
import json
import math
import os
import ssl
import sys
import time
import urllib.error
import urllib.request
from itertools import product as cartesian

try:
    _SSL_CTX = ssl.create_default_context()
    urllib.request.urlopen("https://api.tavily.com", timeout=5, context=_SSL_CTX)
except Exception:
    _SSL_CTX = ssl._create_unverified_context()

TAVILY_URL = "https://api.tavily.com/search"
MAX_RESULTS_PER_QUERY = 20
COST_PER_SEARCH = 0.008
AVG_PROFILES_PER_SEARCH = 17


def get_token():
    token = os.environ.get("TAVILY_API_KEY")
    if token:
        return token
    for path in [".env", os.path.expanduser("~/.gemini/squr/.env")]:
        if os.path.isfile(path):
            with open(path) as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("TAVILY_API_KEY="):
                        return line.split("=", 1)[1].strip().strip('"').strip("'")
    print("ERROR: TAVILY_API_KEY not found", file=sys.stderr)
    sys.exit(1)


def search_tavily(api_key, query, max_results=20):
    payload = json.dumps({
        "api_key": api_key,
        "query": f"site:linkedin.com/in {query}",
        "max_results": min(max_results, MAX_RESULTS_PER_QUERY),
        "include_domains": ["linkedin.com"],
    }).encode()

    req = urllib.request.Request(
        TAVILY_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=30, context=_SSL_CTX) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode()[:200] if e.fp else ""
        if e.code == 429:
            return "RATE_LIMITED", []
        if e.code == 432 or "usage limit" in body.lower() or "upgrade" in body.lower():
            print(f"\n  PLAN LIMIT REACHED (HTTP {e.code}). Upgrade at https://app.tavily.com", file=sys.stderr)
            return "PLAN_LIMIT", []
        print(f"  API error {e.code}: {body}", file=sys.stderr)
        return "ERROR", []
    except Exception as e:
        print(f"  Request error: {e}", file=sys.stderr)
        return "ERROR", []

    results = []
    for r in data.get("results", []):
        url = r.get("url", "").split("?")[0]
        if "linkedin.com/in/" in url:
            title = r.get("title", "")
            name = title.split(" - ")[0].split(" | ")[0].strip() if title else None
            results.append({
                "url": url,
                "name": name if name and name != "LinkedIn" and len(name) < 60 else None,
                "title": title,
                "snippet": r.get("content", "")[:200],
            })

    return "OK", results


def generate_queries(titles, industries, locations):
    queries = []
    for title, industry, location in cartesian(titles, industries, locations):
        parts = [p for p in [title, industry, location] if p]
        queries.append(" ".join(parts))
    return queries


def deduplicate(results):
    seen = set()
    unique = []
    for r in results:
        url = r.get("url", "").rstrip("/").lower()
        if url and url not in seen:
            seen.add(url)
            unique.append(r)
    return unique


def main():
    parser = argparse.ArgumentParser(description="LinkedIn Profile Finder via Tavily")
    parser.add_argument("--query", "-q", help="Single search query")
    parser.add_argument("--batch", "-b", help="Batch queries JSON file")
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument("--urls-only", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--delay", type=float, default=1.0,
                        help="Delay between queries in seconds (default: 1.0)")

    parser.add_argument("--generate-queries", action="store_true")
    parser.add_argument("--titles", help="Comma-separated job titles")
    parser.add_argument("--industries", help="Comma-separated industries")
    parser.add_argument("--locations", help="Comma-separated locations")
    parser.add_argument("--output-queries", help="Save generated queries to file")

    args = parser.parse_args()

    # Query generation mode
    if args.generate_queries:
        if not args.titles:
            parser.error("--titles required")
        titles = [t.strip() for t in args.titles.split(",")]
        industries = [i.strip() for i in args.industries.split(",")] if args.industries else [""]
        locations = [l.strip() for l in args.locations.split(",")] if args.locations else [""]

        queries = generate_queries(titles, industries, locations)
        est_cost = len(queries) * COST_PER_SEARCH
        est_profiles = len(queries) * AVG_PROFILES_PER_SEARCH

        print(f"Generated {len(queries)} ICP query variations")
        print(f"  Estimated cost: ${est_cost:.2f}")
        print(f"  Expected profiles: ~{est_profiles:,}")
        print()
        for i, q in enumerate(queries[:10], 1):
            print(f"  {i}. {q}")
        if len(queries) > 10:
            print(f"  ... and {len(queries) - 10} more")

        if args.output_queries:
            with open(args.output_queries, "w") as f:
                json.dump(queries, f, indent=2)
            print(f"\nSaved to: {args.output_queries}")
        return

    if not args.query and not args.batch:
        parser.error("Provide --query, --batch, or --generate-queries")

    api_key = get_token()
    verbose = not args.quiet

    queries = []
    if args.batch:
        with open(args.batch) as f:
            raw = json.load(f)
        # Support both structured (dict with metadata) and plain string queries
        for item in raw:
            if isinstance(item, dict):
                queries.append(item)  # keep full metadata
            else:
                queries.append({"query": item})
    else:
        queries.append({"query": args.query})

    est_cost = len(queries) * COST_PER_SEARCH
    est_profiles = len(queries) * AVG_PROFILES_PER_SEARCH

    if verbose:
        print(f"LinkedIn Profile Finder (Tavily)")
        print(f"  Queries: {len(queries)}")
        print(f"  Estimated cost: ${est_cost:.2f}")
        print(f"  Expected profiles: ~{est_profiles:,}")
        print()

    if args.dry_run:
        for i, q in enumerate(queries[:20], 1):
            qs = q["query"] if isinstance(q, dict) else q
            meta = ""
            if isinstance(q, dict) and "persona" in q:
                meta = f" [{q['persona']} | {q.get('industry','')} | {q.get('location','')}]"
            print(f"  [{i}] \"{qs}\"{meta}")
        if len(queries) > 20:
            print(f"  ... and {len(queries) - 20} more")
        print(f"\n  TOTAL: ~${est_cost:.2f} | ~{est_profiles:,} profiles")
        return

    seen_urls = set()
    searches_done = 0
    total_found = 0
    rate_limited_count = 0

    # Open output file incrementally (append mode for crash safety)
    out_f = open(args.output, "w") if args.output else None

    for i, q_obj in enumerate(queries, 1):
        query_str = q_obj["query"] if isinstance(q_obj, dict) else q_obj
        metadata = {k: v for k, v in q_obj.items() if k != "query"} if isinstance(q_obj, dict) else {}

        if verbose:
            print(f"[{i}/{len(queries)}] \"{query_str}\"", end="", flush=True)

        status, results = search_tavily(api_key, query_str)
        searches_done += 1

        if status == "RATE_LIMITED":
            rate_limited_count += 1
            for wait in [30, 60, 120]:
                if verbose:
                    print(f" → RATE LIMITED, waiting {wait}s...", flush=True)
                time.sleep(wait)
                status, results = search_tavily(api_key, query_str)
                searches_done += 1
                if status != "RATE_LIMITED":
                    break
            if status == "RATE_LIMITED":
                if verbose:
                    print(" → Still limited. Stopping.", flush=True)
                break
        elif status == "PLAN_LIMIT":
            if verbose:
                print(f" → PLAN LIMIT. Saved {total_found:,} profiles so far.", flush=True)
            break
        elif status == "ERROR":
            if verbose:
                print(" → ERROR, skipping", flush=True)
            continue

        # Deduplicate on the fly, tag with metadata, write incrementally
        new_urls = []
        for r in results:
            url = r.get("url", "").rstrip("/").lower()
            if url and url not in seen_urls:
                seen_urls.add(url)
                # Tag the result with ICP metadata from the query
                tagged = {**r, **metadata, "source_query": query_str}
                new_urls.append(tagged)
                if out_f:
                    if args.urls_only:
                        out_f.write(r["url"] + "\n")
                    else:
                        out_f.write(json.dumps(tagged, ensure_ascii=False) + "\n")

        total_found += len(new_urls)
        if verbose:
            print(f" → {len(results)} found, {len(new_urls)} new (total: {total_found:,})", flush=True)

        # Flush every 10 queries so progress is saved
        if out_f and i % 10 == 0:
            out_f.flush()

        if i < len(queries):
            time.sleep(args.delay)

    if out_f:
        out_f.close()

    actual_cost = searches_done * COST_PER_SEARCH

    if verbose:
        print(f"\nTotal unique profiles: {total_found:,}")
        print(f"Searches used: {searches_done}")
        print(f"Actual cost: ${actual_cost:.2f}")
        if rate_limited_count:
            print(f"Rate limits hit: {rate_limited_count}")
        if args.output:
            print(f"Saved to: {args.output}")

    if not args.output:
        # Print to stdout if no output file
        # Re-read from nothing since we wrote incrementally to file
        pass


if __name__ == "__main__":
    main()
