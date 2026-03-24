#!/usr/bin/env python3
"""
LinkedIn Profile Finder — bulk-discover LinkedIn profile URLs via Apify.
Uses harvestapi/linkedin-profile-search actor in links-only mode ($4/1K profiles).

Usage:
  # Single query
  python3 linkedin_finder.py --query "CISO cybersecurity United States" --max-items 100 --output results.json

  # Batch mode (multiple ICP queries)
  python3 linkedin_finder.py --batch queries.json --output results.json

  # Extract URLs only
  python3 linkedin_finder.py --query "CTO fintech London" --max-items 50 --urls-only --output urls.txt

Environment:
  APIFY_API_TOKEN_PREMIUM  — Apify API token (required)
"""

import argparse
import json
import math
import os
import ssl
import sys
import time
import urllib.request
import urllib.error

# macOS Python often lacks system certs — create unverified context as fallback
try:
    _SSL_CTX = ssl.create_default_context()
    urllib.request.urlopen("https://api.apify.com", timeout=5, context=_SSL_CTX)
except Exception:
    _SSL_CTX = ssl._create_unverified_context()

ACTOR_ID = "harvestapi~linkedin-profile-search"
BASE_URL = "https://api.apify.com/v2"
RESULTS_PER_PAGE = 25


def get_token():
    token = os.environ.get("APIFY_API_TOKEN_PREMIUM")
    if token:
        return token
    env_paths = [".env", os.path.expanduser("~/.gemini/squr/.env")]
    for path in env_paths:
        if os.path.isfile(path):
            with open(path) as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("APIFY_API_TOKEN_PREMIUM="):
                        return line.split("=", 1)[1].strip().strip('"').strip("'")
    print("ERROR: APIFY_API_TOKEN_PREMIUM not found in environment or .env", file=sys.stderr)
    sys.exit(1)


def api_request(url, data=None, method="GET"):
    headers = {"Content-Type": "application/json"}
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60, context=_SSL_CTX) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        err_body = e.read().decode() if e.fp else ""
        print(f"API error {e.code}: {err_body}", file=sys.stderr)
        sys.exit(1)


def start_run(token, search_query, max_items):
    url = f"{BASE_URL}/acts/{ACTOR_ID}/runs?token={token}"
    payload = {
        "searchQuery": search_query,
        "maxItems": max_items,
        "scrapeProfiles": False,
    }
    result = api_request(url, data=payload, method="POST")
    run_data = result.get("data", {})
    run_id = run_data.get("id")
    dataset_id = run_data.get("defaultDatasetId")
    if not run_id:
        print(f"ERROR: Failed to start run. Response: {json.dumps(result)}", file=sys.stderr)
        sys.exit(1)
    return run_id, dataset_id


def wait_for_run(token, run_id, poll_interval=5, max_wait=600):
    url = f"{BASE_URL}/actor-runs/{run_id}?token={token}"
    elapsed = 0
    while elapsed < max_wait:
        result = api_request(url)
        status = result.get("data", {}).get("status")
        if status in ("SUCCEEDED", "FAILED", "ABORTED", "TIMED-OUT"):
            usage = result.get("data", {}).get("usageTotalUsd", 0)
            charged = result.get("data", {}).get("chargedEventCounts", {})
            return status, usage, charged
        time.sleep(poll_interval)
        elapsed += poll_interval
    print(f"ERROR: Run {run_id} did not complete within {max_wait}s", file=sys.stderr)
    return "TIMEOUT", 0, {}


def fetch_results(token, dataset_id, fields=None):
    url = f"{BASE_URL}/datasets/{dataset_id}/items?token={token}&limit=10000"
    if fields:
        url += f"&fields={','.join(fields)}"
    result = api_request(url)
    return result if isinstance(result, list) else []


def estimate_cost(max_items):
    pages = math.ceil(max_items / RESULTS_PER_PAGE)
    return pages * 0.10


def run_search(token, query, max_items, verbose=True):
    est = estimate_cost(max_items)
    if verbose:
        print(f"  Query: \"{query}\"")
        print(f"  Max items: {max_items} (~{math.ceil(max_items/RESULTS_PER_PAGE)} pages)")
        print(f"  Estimated cost: ${est:.2f}")

    run_id, dataset_id = start_run(token, query, max_items)
    if verbose:
        print(f"  Run started: {run_id}")

    status, usage, charged = wait_for_run(token, run_id)
    if verbose:
        print(f"  Status: {status} | Actual cost: ${usage:.3f} | Pages: {charged.get('search-page', 0)}")

    if status != "SUCCEEDED":
        print(f"  WARNING: Run {status}. Skipping.", file=sys.stderr)
        return []

    results = fetch_results(token, dataset_id)
    if verbose:
        print(f"  Profiles found: {len(results)}")
    return results


def deduplicate(results):
    seen = set()
    unique = []
    for r in results:
        url = r.get("linkedinUrl", "")
        if url and url not in seen:
            seen.add(url)
            unique.append(r)
    return unique


def main():
    parser = argparse.ArgumentParser(description="LinkedIn Profile Finder via Apify")
    parser.add_argument("--query", "-q", help="Single search query (e.g., 'CTO fintech United States')")
    parser.add_argument("--batch", "-b", help="Path to batch queries JSON file")
    parser.add_argument("--max-items", "-m", type=int, default=100, help="Max profiles per query (default: 100)")
    parser.add_argument("--output", "-o", help="Output file path (default: stdout)")
    parser.add_argument("--urls-only", action="store_true", help="Output only LinkedIn URLs, one per line")
    parser.add_argument("--dry-run", action="store_true", help="Show cost estimate without running")
    parser.add_argument("--quiet", action="store_true", help="Suppress progress output")
    args = parser.parse_args()

    if not args.query and not args.batch:
        parser.error("Provide --query or --batch")

    token = get_token()
    verbose = not args.quiet

    queries = []
    if args.batch:
        with open(args.batch) as f:
            batch = json.load(f)
        for item in batch:
            q = item if isinstance(item, dict) else {"query": item}
            q.setdefault("maxItems", args.max_items)
            queries.append(q)
    else:
        queries.append({"query": args.query, "maxItems": args.max_items})

    total_est = sum(estimate_cost(q["maxItems"]) for q in queries)
    total_items = sum(q["maxItems"] for q in queries)

    if verbose:
        print(f"LinkedIn Profile Finder")
        print(f"  Queries: {len(queries)}")
        print(f"  Total max items: {total_items}")
        print(f"  Estimated total cost: ${total_est:.2f}")
        print()

    if args.dry_run:
        for i, q in enumerate(queries, 1):
            est = estimate_cost(q["maxItems"])
            print(f"  [{i}] \"{q['query']}\" — max {q['maxItems']} items — ~${est:.2f}")
        print(f"\n  TOTAL: ~${total_est:.2f}")
        return

    all_results = []
    total_cost = 0.0

    for i, q in enumerate(queries, 1):
        if verbose:
            print(f"[{i}/{len(queries)}]")
        results = run_search(token, q["query"], q["maxItems"], verbose=verbose)
        all_results.extend(results)
        if verbose:
            print()

    all_results = deduplicate(all_results)

    if verbose:
        print(f"Total unique profiles: {len(all_results)}")

    if args.urls_only:
        output = "\n".join(r.get("linkedinUrl", "") for r in all_results if r.get("linkedinUrl"))
    else:
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
