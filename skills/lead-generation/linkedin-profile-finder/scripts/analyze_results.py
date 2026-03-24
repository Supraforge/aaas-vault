#!/usr/bin/env python3
"""
Analyze LinkedIn profile discovery results.
Reads JSONL output from linkedin_tavily.py or linkedin_google_cse.py.

Usage:
  python3 analyze_results.py context/profiles-dach.jsonl
  python3 analyze_results.py context/profiles-dach.jsonl --export-by-persona context/by-persona/
  python3 analyze_results.py context/profiles-dach.jsonl --export-csv context/profiles-dach.csv
"""

import argparse
import csv
import json
import os
import sys
from collections import Counter


def load_jsonl(path):
    """Load JSONL file (one JSON object per line)."""
    results = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    results.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return results


def analyze(results):
    """Print summary statistics."""
    total = len(results)
    personas = Counter(r.get("persona", "untagged") for r in results)
    industries = Counter(r.get("industry", "untagged") for r in results)
    regions = Counter(r.get("region", "untagged") for r in results)
    locations = Counter(r.get("location", "untagged") for r in results)

    print(f"LinkedIn Profile Discovery — Results Analysis")
    print(f"{'=' * 55}")
    print(f"  Total unique profiles: {total:,}")
    print()

    print("  By Persona:")
    for p, c in personas.most_common():
        pct = c / total * 100
        bar = "#" * int(pct / 2)
        print(f"    {p:30s} {c:5,}  ({pct:4.1f}%)  {bar}")

    print()
    print("  By Industry:")
    for ind, c in industries.most_common():
        pct = c / total * 100
        print(f"    {ind:20s} {c:5,}  ({pct:4.1f}%)")

    print()
    print("  By Region:")
    for r, c in regions.most_common():
        pct = r and c / total * 100 or 0
        print(f"    {r:20s} {c:5,}  ({pct:4.1f}%)")

    print()
    print("  Top 10 Locations:")
    for loc, c in locations.most_common(10):
        print(f"    {loc:20s} {c:5,}")

    # Cross-tab: persona × industry
    print()
    print("  Persona × Industry Matrix:")
    ind_keys = sorted(set(r.get("industry", "") for r in results))
    header = f"    {'':25s}" + "".join(f"{k:>10s}" for k in ind_keys)
    print(header)
    for p, _ in personas.most_common():
        row = f"    {p:25s}"
        for ind in ind_keys:
            count = sum(1 for r in results if r.get("persona") == p and r.get("industry") == ind)
            row += f"{count:10,}"
        print(row)


def export_by_persona(results, output_dir):
    """Export separate URL files per persona for activation."""
    os.makedirs(output_dir, exist_ok=True)
    grouped = {}
    for r in results:
        persona = r.get("persona", "untagged")
        grouped.setdefault(persona, []).append(r)

    for persona, profiles in grouped.items():
        # URLs file
        url_path = os.path.join(output_dir, f"{persona}_urls.txt")
        with open(url_path, "w") as f:
            for p in profiles:
                f.write(p["url"] + "\n")

        # Full JSONL file
        jsonl_path = os.path.join(output_dir, f"{persona}.jsonl")
        with open(jsonl_path, "w") as f:
            for p in profiles:
                f.write(json.dumps(p, ensure_ascii=False) + "\n")

        print(f"  {persona}: {len(profiles):,} profiles → {url_path}")

    print(f"\n  Exported {len(grouped)} persona files to {output_dir}")


def export_csv(results, output_path):
    """Export as CSV for spreadsheet use."""
    if not results:
        print("No results to export.", file=sys.stderr)
        return

    fields = ["url", "name", "persona", "title_searched", "industry", "location", "region", "source_query"]
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(results)
    print(f"  Exported {len(results):,} profiles to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Analyze LinkedIn profile discovery results")
    parser.add_argument("input", help="Path to JSONL results file")
    parser.add_argument("--export-by-persona", help="Export separate files per persona to this directory")
    parser.add_argument("--export-csv", help="Export as CSV to this path")
    args = parser.parse_args()

    results = load_jsonl(args.input)
    if not results:
        print(f"No results found in {args.input}", file=sys.stderr)
        sys.exit(1)

    analyze(results)

    if args.export_by_persona:
        print()
        export_by_persona(results, args.export_by_persona)

    if args.export_csv:
        print()
        export_csv(results, args.export_csv)


if __name__ == "__main__":
    main()
