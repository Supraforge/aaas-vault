#!/usr/bin/env python3
"""
Objection Handler - Search and manage objection responses.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List

SKILL_DIR = Path(__file__).parent.parent
OBJECTIONS_PATH = SKILL_DIR / "resources" / "objection_database.json"


def ensure_resources():
    """Ensure resources directory exists."""
    OBJECTIONS_PATH.parent.mkdir(exist_ok=True)


def load_objections() -> Dict:
    """Load objection database."""
    ensure_resources()
    if OBJECTIONS_PATH.exists():
        with open(OBJECTIONS_PATH) as f:
            return json.load(f)
    return {"objections": get_default_objections()}


def save_objections(data: Dict):
    """Save objection database."""
    ensure_resources()
    with open(OBJECTIONS_PATH, "w") as f:
        json.dump(data, f, indent=2)


def get_default_objections() -> List[Dict]:
    """Return default objection database."""
    return [
        {
            "id": "obj_001",
            "category": "price",
            "objection": "It's too expensive for our budget",
            "response": "I understand budget is a concern. Many of our customers initially felt the same way. The key question is: what's the cost of NOT solving this? Our customers typically see 40% of engineering time returned - what would that be worth to your team?",
            "follow_up": "What would make this investment worthwhile for you?",
            "tags": ["budget", "roi", "value"]
        },
        {
            "id": "obj_002",
            "category": "price",
            "objection": "We need to see ROI first",
            "response": "Absolutely - that's why we offer a 90-minute risk baseline assessment at no cost. You'll see exactly what gaps exist and can calculate the potential savings before committing to anything.",
            "follow_up": "Would a baseline assessment help you build the business case?",
            "tags": ["roi", "pilot", "proof"]
        },
        {
            "id": "obj_003",
            "category": "timing",
            "objection": "We're not ready to make a decision right now",
            "response": "I completely understand. Out of curiosity, when is your next audit? Many teams find value in running a baseline assessment well in advance, even if full implementation comes later.",
            "follow_up": "What would need to change for this to become a priority?",
            "tags": ["timing", "delay", "priority"]
        },
        {
            "id": "obj_004",
            "category": "timing",
            "objection": "We're in the middle of a release",
            "response": "That makes sense - releases are intense. The good news is our implementation is designed to happen alongside your existing workflow, not interrupt it. Would it help to do a quick assessment now and plan implementation for after the release?",
            "follow_up": "When does your release cycle typically slow down?",
            "tags": ["timing", "release", "busy"]
        },
        {
            "id": "obj_005",
            "category": "competition",
            "objection": "We already have tools for this",
            "response": "Great - we actually integrate with existing tools rather than replacing them. We sit as a layer on top of your current stack (Jira, DOORS, Polarion, etc.) and provide the continuous visibility that point solutions can't. What tools are you using today?",
            "follow_up": "Are you getting real-time compliance visibility from your current setup?",
            "tags": ["competition", "tools", "integration"]
        },
        {
            "id": "obj_006",
            "category": "competition",
            "objection": "We're evaluating other solutions",
            "response": "That's smart - it's a significant decision. I'd love to understand what you're comparing. Our differentiation is the real-time, continuous approach versus periodic assessments. Would it be helpful to see a side-by-side comparison?",
            "follow_up": "What criteria are most important in your evaluation?",
            "tags": ["competition", "evaluation", "comparison"]
        },
        {
            "id": "obj_007",
            "category": "technical",
            "objection": "Will this work with our existing tools?",
            "response": "Yes - we're specifically designed to integrate with the tools teams already use. We have out-of-the-box connectors for Jira, DOORS, Polarion, Git, and others. The integration typically takes a few hours, not weeks.",
            "follow_up": "What's your current tool stack?",
            "tags": ["technical", "integration", "tools"]
        },
        {
            "id": "obj_008",
            "category": "technical",
            "objection": "How secure is the data?",
            "response": "Security is foundational for us. We're EU-hosted, GDPR compliant, and can deploy in your private cloud if needed. We never store source code - only metadata and traceability links. Happy to share our security documentation.",
            "follow_up": "Would your security team like to review our documentation?",
            "tags": ["technical", "security", "compliance"]
        },
        {
            "id": "obj_009",
            "category": "authority",
            "objection": "I need to check with my manager / team",
            "response": "Of course - decisions like this need the right people involved. Would it be helpful if I joined a call with your team to answer their questions directly? I can also prepare a one-pager that addresses common concerns.",
            "follow_up": "Who else should be part of this conversation?",
            "tags": ["authority", "stakeholder", "approval"]
        },
        {
            "id": "obj_010",
            "category": "authority",
            "objection": "This needs to go through procurement",
            "response": "Understood - we work with procurement teams regularly. I can provide all the documentation they typically need (security questionnaire, compliance certifications, etc.) upfront to speed up the process.",
            "follow_up": "What does your procurement process typically require?",
            "tags": ["authority", "procurement", "process"]
        }
    ]


def search_objections(query: str, category: str = None) -> List[Dict]:
    """Search objections by query and optional category."""
    data = load_objections()
    objections = data.get("objections", [])

    results = []
    query_lower = query.lower()

    for obj in objections:
        # Filter by category if specified
        if category and obj.get("category") != category:
            continue

        # Search in objection text, tags, and response
        searchable = (
            obj.get("objection", "").lower() +
            " " + obj.get("response", "").lower() +
            " " + " ".join(obj.get("tags", []))
        )

        if query_lower in searchable:
            results.append(obj)

    return results


def add_objection(
    objection: str,
    response: str,
    category: str,
    follow_up: str = None,
    tags: List[str] = None
) -> Dict:
    """Add new objection to database."""
    data = load_objections()

    # Generate ID
    existing_ids = [o.get("id", "") for o in data.get("objections", [])]
    new_num = len(existing_ids) + 1
    new_id = f"obj_{new_num:03d}"

    while new_id in existing_ids:
        new_num += 1
        new_id = f"obj_{new_num:03d}"

    new_objection = {
        "id": new_id,
        "category": category,
        "objection": objection,
        "response": response,
        "follow_up": follow_up or "",
        "tags": tags or []
    }

    data.setdefault("objections", []).append(new_objection)
    save_objections(data)

    return new_objection


def main():
    parser = argparse.ArgumentParser(description="Manage objection responses")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Search command
    search_parser = subparsers.add_parser("search", help="Search objections")
    search_parser.add_argument("query", help="Search query")
    search_parser.add_argument("--category", "-c", choices=["price", "timing", "competition", "technical", "authority"])
    search_parser.add_argument("--output", "-o", choices=["json", "text"], default="text")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add new objection")
    add_parser.add_argument("--objection", "-o", required=True, help="The objection text")
    add_parser.add_argument("--response", "-r", required=True, help="The response")
    add_parser.add_argument("--category", "-c", required=True, choices=["price", "timing", "competition", "technical", "authority"])
    add_parser.add_argument("--follow-up", "-f", help="Follow-up question")
    add_parser.add_argument("--tags", "-t", help="Comma-separated tags")

    # List command
    list_parser = subparsers.add_parser("list", help="List all objections")
    list_parser.add_argument("--category", "-c", help="Filter by category")
    list_parser.add_argument("--output", "-o", choices=["json", "text"], default="text")

    args = parser.parse_args()

    if args.command == "search":
        results = search_objections(args.query, args.category)

        if args.output == "json":
            print(json.dumps(results, indent=2))
        else:
            print(f"\n{'='*60}")
            print(f"OBJECTION SEARCH: \"{args.query}\"")
            print(f"{'='*60}\n")

            if not results:
                print("No matching objections found.\n")
                return

            for obj in results:
                print(f"[{obj['category'].upper()}] {obj['objection']}")
                print(f"\nResponse:")
                print(f"  {obj['response']}")
                if obj.get("follow_up"):
                    print(f"\nFollow-up: {obj['follow_up']}")
                print(f"\nTags: {', '.join(obj.get('tags', []))}")
                print("\n" + "-"*60 + "\n")

    elif args.command == "add":
        tags = args.tags.split(",") if args.tags else []
        obj = add_objection(
            objection=args.objection,
            response=args.response,
            category=args.category,
            follow_up=args.follow_up,
            tags=tags
        )
        print(f"Added objection: {obj['id']}")

    elif args.command == "list":
        data = load_objections()
        objections = data.get("objections", [])

        if args.category:
            objections = [o for o in objections if o.get("category") == args.category]

        if args.output == "json":
            print(json.dumps(objections, indent=2))
        else:
            print(f"\n{'='*60}")
            print(f"OBJECTION DATABASE ({len(objections)} objections)")
            print(f"{'='*60}\n")

            by_category = {}
            for obj in objections:
                cat = obj.get("category", "other")
                by_category.setdefault(cat, []).append(obj)

            for cat, cat_objs in sorted(by_category.items()):
                print(f"--- {cat.upper()} ({len(cat_objs)}) ---")
                for obj in cat_objs:
                    print(f"  [{obj['id']}] {obj['objection'][:50]}...")
                print()


if __name__ == "__main__":
    main()
