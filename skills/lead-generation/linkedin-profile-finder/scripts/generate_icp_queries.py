#!/usr/bin/env python3
"""
Generate structured LinkedIn search queries from ICP definitions.
Each query is tagged with persona, industry, location, region for activation.

Usage:
  # From config file
  python3 generate_icp_queries.py --config context/icp-targets.json --output queries.json

  # Filter to specific region
  python3 generate_icp_queries.py --config context/icp-targets.json --region dach --output queries-dach.json

  # Override target count
  python3 generate_icp_queries.py --config context/icp-targets.json --target 10000 --output queries.json

  # Use built-in SQUR defaults (no config file needed)
  python3 generate_icp_queries.py --squr-defaults --region dach --output queries-dach.json
"""

import argparse
import json
import os
import sys
from collections import Counter

# ─── SQUR Default ICPs (used when no config file provided) ───

SQUR_PERSONAS = {
    "alex_cto": {
        "weight": 3,
        "titles": [
            "CTO", "Chief Technology Officer", "VP Engineering",
            "VP of Engineering", "Head of Engineering",
            "Chief Technical Officer", "Co-Founder CTO",
        ],
    },
    "delia_ciso": {
        "weight": 3,
        "titles": [
            "CISO", "Chief Information Security Officer",
            "VP Security", "VP of Security",
            "Head of Information Security", "Director of Security",
            "Chief Security Officer",
        ],
    },
    "beatrice_budget_ciso": {
        "weight": 2,
        "titles": [
            "Head of Security", "Security Manager",
            "IT Security Manager", "Information Security Manager",
            "Security Director", "Head of Cybersecurity",
        ],
    },
    "felix_head_it": {
        "weight": 2,
        "titles": [
            "Head of IT", "IT Director", "IT Manager",
            "Director of IT", "VP IT",
            "Head of Technology", "IT Lead",
        ],
    },
    "carlos_engineering": {
        "weight": 1,
        "titles": [
            "Engineering Lead", "Lead Engineer",
            "Principal Engineer", "Staff Engineer",
            "Engineering Manager", "DevOps Lead",
        ],
    },
    "evan_product": {
        "weight": 1,
        "titles": [
            "Product Manager security", "Head of Product",
            "VP Product", "Director of Product",
            "Product Lead", "CPO",
        ],
    },
    "greta_appsec": {
        "weight": 2,
        "titles": [
            "AppSec Engineer", "Application Security Engineer",
            "Security Engineer", "Penetration Tester",
            "Senior Security Engineer", "AppSec Lead",
            "Security Analyst", "Offensive Security",
        ],
    },
    "hanna_founder": {
        "weight": 2,
        "titles": [
            "Founder", "CEO", "Co-Founder",
            "Managing Director", "Geschaeftsfuehrer",
        ],
    },
}

SQUR_INDUSTRIES = {
    "fintech": ["fintech", "neobank", "payments", "banking software"],
    "saas": ["SaaS", "B2B SaaS", "cloud software"],
    "cybersecurity": ["cybersecurity", "infosec", "security software"],
    "legaltech": ["legaltech", "legal tech", "law firm technology"],
    "healthtech": ["healthtech", "health tech", "digital health", "medtech"],
    "insurance": ["insurtech", "insurance technology", "insurance"],
    "ecommerce": ["ecommerce", "e-commerce", "online marketplace"],
    "govtech": ["govtech", "government technology", "public sector IT"],
    "regtech": ["regtech", "regulatory technology", "compliance software"],
}

SQUR_LOCATIONS = {
    "dach": ["Berlin", "Munich", "Frankfurt", "Hamburg", "Zurich", "Vienna", "Stuttgart", "Cologne", "Dusseldorf"],
    "uk": ["London", "Manchester", "Edinburgh", "Dublin", "Bristol", "Cambridge"],
    "nordics": ["Stockholm", "Copenhagen", "Oslo", "Helsinki"],
    "benelux": ["Amsterdam", "Rotterdam", "Brussels", "Luxembourg"],
    "southern_eu": ["Barcelona", "Madrid", "Milan", "Lisbon"],
    "france": ["Paris", "Lyon"],
    "global": ["Singapore", "Sydney", "Toronto", "Tel Aviv", "San Francisco", "New York", "Austin"],
}


def load_config(path):
    """Load ICP definitions from a JSON config file."""
    with open(path) as f:
        config = json.load(f)
    return (
        config.get("personas", SQUR_PERSONAS),
        config.get("industries", SQUR_INDUSTRIES),
        config.get("locations", SQUR_LOCATIONS),
        config.get("target_count", 50000),
    )


def build_lookups(industries, locations):
    """Build reverse lookups: term→industry_key, city→region."""
    ind_map = {}
    for key, terms in industries.items():
        for t in terms:
            ind_map[t] = key
    loc_map = {}
    for region, cities in locations.items():
        for city in cities:
            loc_map[city] = region
    return ind_map, loc_map


def generate_queries(personas, industries, locations, target_count=50000, region_filter=None, profiles_per_query=13):
    """Generate structured query objects with ICP metadata."""
    ind_map, loc_map = build_lookups(industries, locations)

    # Flatten and optionally filter locations
    all_locations = []
    for region, cities in locations.items():
        if region_filter and region != region_filter:
            continue
        all_locations.extend(cities)

    if not all_locations:
        print(f"ERROR: No cities found for region '{region_filter}'", file=sys.stderr)
        print(f"Available regions: {', '.join(locations.keys())}", file=sys.stderr)
        sys.exit(1)

    queries = []
    for persona_name, persona in personas.items():
        weight = persona.get("weight", 1)
        titles = persona["titles"]

        # Weight controls how many industry terms per industry
        if weight >= 3:
            industry_terms = []
            for terms in industries.values():
                industry_terms.extend(terms[:2])
        elif weight >= 2:
            industry_terms = [terms[0] for terms in industries.values()]
            titles = titles[:5]
        else:
            industry_terms = []
            for key in list(industries.keys())[:4]:
                industry_terms.append(industries[key][0])
            titles = titles[:4]

        for title in titles:
            for term in industry_terms:
                for city in all_locations:
                    queries.append({
                        "query": f"{title} {term} {city}",
                        "persona": persona_name,
                        "title_searched": title,
                        "industry": ind_map.get(term, "unknown"),
                        "industry_term": term,
                        "location": city,
                        "region": loc_map.get(city, "unknown"),
                    })

    # Deduplicate by query string
    seen = set()
    unique = []
    for q in queries:
        if q["query"] not in seen:
            seen.add(q["query"])
            unique.append(q)
    queries = unique

    # Trim to target if needed
    needed = target_count // profiles_per_query
    if len(queries) > needed:
        step = len(queries) / needed
        queries = [queries[int(i * step)] for i in range(needed)]

    return queries


def print_summary(queries):
    """Print a summary of the generated query matrix."""
    personas = Counter(q["persona"] for q in queries)
    industries = Counter(q["industry"] for q in queries)
    regions = Counter(q["region"] for q in queries)

    cost_tavily = len(queries) * 0.008
    cost_google = (len(queries) / 10) * 0.005  # 10 pages per query at $5/1K
    est_profiles = len(queries) * 13

    print(f"ICP LinkedIn Query Matrix")
    print(f"{'=' * 50}")
    print(f"  Queries:            {len(queries):,}")
    print(f"  Expected profiles:  ~{est_profiles:,}")
    print(f"  Cost (Tavily):      ${cost_tavily:.2f}")
    print(f"  Cost (Google CSE):  ${cost_google:.2f}")
    print()
    print("  By persona:")
    for p, c in personas.most_common():
        print(f"    {p:30s} {c:5,}")
    print()
    print("  By industry:")
    for ind, c in industries.most_common():
        print(f"    {ind:20s} {c:5,}")
    print()
    print("  By region:")
    for r, c in regions.most_common():
        print(f"    {r:20s} {c:5,}")


def main():
    parser = argparse.ArgumentParser(description="Generate ICP-tagged LinkedIn search queries")
    parser.add_argument("--config", "-c", help="Path to ICP config JSON file")
    parser.add_argument("--squr-defaults", action="store_true", help="Use built-in SQUR ICP definitions")
    parser.add_argument("--region", "-r", help="Filter to specific region (e.g., dach, uk, nordics)")
    parser.add_argument("--target", "-t", type=int, default=50000, help="Target profile count (default: 50000)")
    parser.add_argument("--output", "-o", required=True, help="Output JSON file path")
    args = parser.parse_args()

    if args.config:
        personas, industries, locations, target = load_config(args.config)
        if args.target != 50000:
            target = args.target
    elif args.squr_defaults:
        personas, industries, locations, target = SQUR_PERSONAS, SQUR_INDUSTRIES, SQUR_LOCATIONS, args.target
    else:
        parser.error("Provide --config or --squr-defaults")

    queries = generate_queries(personas, industries, locations, target, args.region)
    print_summary(queries)

    with open(args.output, "w") as f:
        json.dump(queries, f, indent=2)
    print(f"\n  Saved to: {args.output}")


if __name__ == "__main__":
    main()
