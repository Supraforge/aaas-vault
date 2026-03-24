#!/usr/bin/env python3
"""
LinkedIn Profile Finder via Google Custom Search API.
Finds LinkedIn profile URLs by searching Google for site:linkedin.com/in profiles
matching ICP criteria. ~$25 for 50K profiles.

SETUP (one-time, 30 seconds):
  1. Go to https://programmablesearchengine.google.com/
  2. Click "Add" → Name: "LinkedIn Profiles"
  3. Under "What to search": select "Search specific sites"
     → Add: linkedin.com/in/*
  4. Create → copy the "Search engine ID" (cx value)
  5. Add to .env: GOOGLE_CSE_ID=<your cx value>
  6. Ensure GOOGLE_API_KEY is set in .env (already confirmed)

PRICING:
  - Free: 100 queries/day
  - Paid: $5/1,000 queries (enable billing in Google Cloud Console)
  - Each query returns up to 10 results, paginate up to 100 results/query
  - 50K profiles ≈ 5,000 queries ≈ $25

Usage:
  # Single ICP query
  python3 linkedin_google_cse.py --query "CISO cybersecurity San Francisco" --output results.json

  # Batch mode with ICP file
  python3 linkedin_google_cse.py --batch icps.json --output results.json

  # Generate ICP query variations automatically
  python3 linkedin_google_cse.py --generate-queries --titles "CISO,Head of Security,VP Security" \
    --industries "fintech,cybersecurity,SaaS" \
    --locations "San Francisco,New York,Austin,London,Berlin" \
    --output-queries queries.json

  # Dry run (estimate cost without searching)
  python3 linkedin_google_cse.py --batch queries.json --dry-run

  # URLs only output
  python3 linkedin_google_cse.py --batch queries.json --urls-only --output urls.txt
"""

import argparse
import json
import math
import os
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from itertools import product as cartesian

# SSL fix for macOS Python
try:
    _SSL_CTX = ssl.create_default_context()
    urllib.request.urlopen("https://www.googleapis.com", timeout=5, context=_SSL_CTX)
except Exception:
    _SSL_CTX = ssl._create_unverified_context()

CSE_BASE = "https://www.googleapis.com/customsearch/v1"
RESULTS_PER_PAGE = 10
MAX_PAGES = 10  # Google CSE limit: start param max 91, so 10 pages of 10
MAX_RESULTS_PER_QUERY = MAX_PAGES * RESULTS_PER_PAGE  # 100
COST_PER_QUERY = 0.005  # $5/1000 queries
FREE_DAILY_LIMIT = 100


def load_env():
    """Load API key and CSE ID from environment or .env file."""
    env_paths = [".env", os.path.expanduser("~/.gemini/squr/.env")]
    env_vars = {}
    for path in env_paths:
        if os.path.isfile(path):
            with open(path) as f:
                for line in f:
                    line = line.strip()
                    if "=" in line and not line.startswith("#"):
                        key, _, val = line.partition("=")
                        key = key.strip()
                        val = val.strip().strip('"').strip("'")
                        if key in ("GOOGLE_API_KEY", "GOOGLE_CSE_API_KEY", "GOOGLE_CSE_ID"):
                            env_vars[key] = val

    # Prefer dedicated CSE key, fall back to general Google API key
    api_key = (os.environ.get("GOOGLE_CSE_API_KEY") or env_vars.get("GOOGLE_CSE_API_KEY")
               or os.environ.get("GOOGLE_API_KEY") or env_vars.get("GOOGLE_API_KEY"))
    cse_id = os.environ.get("GOOGLE_CSE_ID") or env_vars.get("GOOGLE_CSE_ID")

    if not api_key:
        print("ERROR: GOOGLE_API_KEY not found", file=sys.stderr)
        sys.exit(1)
    if not cse_id:
        print("ERROR: GOOGLE_CSE_ID not found.", file=sys.stderr)
        print("\nSETUP (30 seconds):", file=sys.stderr)
        print("  1. Go to https://programmablesearchengine.google.com/", file=sys.stderr)
        print('  2. Click "Add" → Name: "LinkedIn Profiles"', file=sys.stderr)
        print('  3. "What to search" → "Search specific sites" → Add: linkedin.com/in/*', file=sys.stderr)
        print('  4. Create → copy the "Search engine ID"', file=sys.stderr)
        print("  5. Add to .env: GOOGLE_CSE_ID=<your cx value>", file=sys.stderr)
        sys.exit(1)

    return api_key, cse_id


def api_get(url):
    """Make a GET request with SSL context."""
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req, timeout=30, context=_SSL_CTX) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode() if e.fp else ""
        if e.code == 429:
            return {"error": "RATE_LIMITED"}
        if e.code == 403:
            err = json.loads(body) if body else {}
            reason = err.get("error", {}).get("errors", [{}])[0].get("reason", "")
            if reason == "dailyLimitExceeded":
                return {"error": "DAILY_LIMIT"}
        print(f"  API error {e.code}: {body[:200]}", file=sys.stderr)
        return {"error": f"HTTP_{e.code}"}
    except Exception as e:
        print(f"  Request error: {e}", file=sys.stderr)
        return {"error": str(e)}


def search_google(api_key, cse_id, query, max_results=100):
    """
    Search Google CSE for LinkedIn profiles matching the query.
    Returns list of {url, title, snippet}.
    """
    results = []
    pages_needed = min(math.ceil(max_results / RESULTS_PER_PAGE), MAX_PAGES)

    for page in range(pages_needed):
        start = page * RESULTS_PER_PAGE + 1
        params = urllib.parse.urlencode({
            "key": api_key,
            "cx": cse_id,
            "q": query,
            "start": start,
            "num": RESULTS_PER_PAGE,
        })
        url = f"{CSE_BASE}?{params}"
        data = api_get(url)

        if "error" in data:
            if data["error"] == "RATE_LIMITED":
                print("  Rate limited — waiting 10s...", file=sys.stderr)
                time.sleep(10)
                data = api_get(url)
                if "error" in data:
                    break
            elif data["error"] == "DAILY_LIMIT":
                print("  Daily free limit reached. Enable billing or wait.", file=sys.stderr)
                break
            else:
                break

        items = data.get("items", [])
        if not items:
            break

        for item in items:
            link = item.get("link", "")
            # Only keep actual profile URLs, not company pages etc.
            if "linkedin.com/in/" in link:
                results.append({
                    "url": link.split("?")[0],  # strip tracking params
                    "title": item.get("title", ""),
                    "snippet": item.get("snippet", ""),
                })

        if len(results) >= max_results:
            break

        # Small delay to avoid rate limits
        if page < pages_needed - 1:
            time.sleep(0.5)

    return results[:max_results]


def generate_queries(titles, industries, locations):
    """
    Generate ICP query combinations.
    E.g., titles=["CISO","VP Security"], industries=["fintech"], locations=["NYC","SF"]
    → ["CISO fintech NYC", "CISO fintech SF", "VP Security fintech NYC", ...]
    """
    queries = []
    for title, industry, location in cartesian(titles, industries, locations):
        parts = [p for p in [title, industry, location] if p]
        queries.append(" ".join(parts))
    return queries


def deduplicate(results):
    """Deduplicate by LinkedIn URL (normalized)."""
    seen = set()
    unique = []
    for r in results:
        url = r.get("url", "").rstrip("/").lower()
        if url and url not in seen:
            seen.add(url)
            unique.append(r)
    return unique


def extract_name_from_title(title):
    """Try to extract name from Google result title like 'John Doe - CISO - Company | LinkedIn'."""
    if not title:
        return None
    # Typical format: "Name - Title - Company | LinkedIn"
    name = title.split(" - ")[0].split(" | ")[0].strip()
    if name and name != "LinkedIn" and len(name) < 60:
        return name
    return None


def main():
    parser = argparse.ArgumentParser(
        description="LinkedIn Profile Finder via Google Custom Search"
    )
    parser.add_argument("--query", "-q", help="Single search query")
    parser.add_argument("--batch", "-b", help="Batch queries JSON file")
    parser.add_argument("--max-per-query", "-m", type=int, default=100,
                        help="Max results per query (default: 100, max: 100)")
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument("--urls-only", action="store_true", help="Output URLs only")
    parser.add_argument("--dry-run", action="store_true", help="Estimate cost only")
    parser.add_argument("--quiet", action="store_true")

    # Query generation mode
    parser.add_argument("--generate-queries", action="store_true",
                        help="Generate ICP query combinations")
    parser.add_argument("--titles", help="Comma-separated job titles")
    parser.add_argument("--industries", help="Comma-separated industries")
    parser.add_argument("--locations", help="Comma-separated locations")
    parser.add_argument("--output-queries", help="Save generated queries to file")

    args = parser.parse_args()

    # Query generation mode
    if args.generate_queries:
        if not args.titles:
            parser.error("--titles required for query generation")
        titles = [t.strip() for t in args.titles.split(",")]
        industries = [i.strip() for i in args.industries.split(",")] if args.industries else [""]
        locations = [l.strip() for l in args.locations.split(",")] if args.locations else [""]

        queries = generate_queries(titles, industries, locations)
        total_queries_api = len(queries) * min(
            math.ceil(args.max_per_query / RESULTS_PER_PAGE), MAX_PAGES
        )
        est_cost = total_queries_api * COST_PER_QUERY
        est_profiles = len(queries) * args.max_per_query

        print(f"Generated {len(queries)} ICP query variations")
        print(f"  API queries needed: {total_queries_api}")
        print(f"  Estimated cost: ${est_cost:.2f}")
        print(f"  Max possible profiles: {est_profiles:,}")
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

    # Search mode
    if not args.query and not args.batch:
        parser.error("Provide --query, --batch, or --generate-queries")

    api_key, cse_id = load_env()
    verbose = not args.quiet
    max_per = min(args.max_per_query, MAX_RESULTS_PER_QUERY)

    # Load queries
    queries = []
    if args.batch:
        with open(args.batch) as f:
            queries = json.load(f)
        if isinstance(queries[0], dict):
            queries = [q.get("query", q.get("q", "")) for q in queries]
    else:
        queries = [args.query]

    # Cost estimation
    pages_per_query = min(math.ceil(max_per / RESULTS_PER_PAGE), MAX_PAGES)
    total_api_queries = len(queries) * pages_per_query
    est_cost = total_api_queries * COST_PER_QUERY
    free_days = math.ceil(total_api_queries / FREE_DAILY_LIMIT)

    if verbose:
        print(f"LinkedIn Profile Finder (Google CSE)")
        print(f"  Search queries: {len(queries)}")
        print(f"  Pages per query: {pages_per_query}")
        print(f"  Total API calls: {total_api_queries:,}")
        print(f"  Estimated cost: ${est_cost:.2f} (paid) or {free_days} days (free tier)")
        print(f"  Max possible profiles: {len(queries) * max_per:,}")
        print()

    if args.dry_run:
        for i, q in enumerate(queries[:20], 1):
            print(f"  [{i}] \"{q}\"")
        if len(queries) > 20:
            print(f"  ... and {len(queries) - 20} more")
        print(f"\n  TOTAL: ~${est_cost:.2f} | {total_api_queries:,} API calls")
        return

    # Execute searches
    all_results = []
    total_api_calls = 0

    for i, query in enumerate(queries, 1):
        if verbose:
            print(f"[{i}/{len(queries)}] \"{query}\"", end="")

        results = search_google(api_key, cse_id, query, max_per)
        total_api_calls += pages_per_query
        all_results.extend(results)

        if verbose:
            print(f" → {len(results)} profiles")

        # Respect rate limits
        if i < len(queries):
            time.sleep(1)

    all_results = deduplicate(all_results)

    if verbose:
        actual_cost = total_api_calls * COST_PER_QUERY
        print(f"\nTotal unique profiles: {len(all_results):,}")
        print(f"API calls used: {total_api_calls:,}")
        print(f"Actual cost: ${actual_cost:.2f}")

    # Format output
    if args.urls_only:
        output = "\n".join(r["url"] for r in all_results)
    else:
        # Enrich with extracted names
        for r in all_results:
            r["name"] = extract_name_from_title(r.get("title", ""))
        output = json.dumps(all_results, indent=2, ensure_ascii=False)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        if verbose:
            print(f"Saved to: {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
