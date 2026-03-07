#!/usr/bin/env python3
"""
Gap Logger - Records unmet capability needs for the system.

Usage:
    python gap_logger.py "I need to analyze ECG images"
    python gap_logger.py --request "description" --category "medical-imaging" --urgency "high"
    python gap_logger.py --interactive
"""

import json
import os
import argparse
from datetime import datetime
from pathlib import Path
from typing import Optional
import hashlib

# Paths
SCRIPT_DIR = Path(__file__).parent.parent
DATA_DIR = SCRIPT_DIR / "data"
GAP_LOG_PATH = DATA_DIR / "gap-log.json"

# Categories for gap classification
CATEGORIES = [
    "content-creation",     # New content formats
    "research",             # Research/data gathering
    "analysis",             # Data analysis capabilities
    "visual",               # Image/diagram generation
    "medical-imaging",      # Medical image analysis
    "audio-video",          # Audio/video processing
    "automation",           # Workflow automation
    "integration",          # External service integration
    "data-extraction",      # Extracting data from sources
    "quality",              # Quality/review capabilities
    "other"                 # Uncategorized
]

URGENCY_LEVELS = ["low", "medium", "high", "critical"]


def load_gap_log() -> dict:
    """Load existing gap log or create new one."""
    if GAP_LOG_PATH.exists():
        with open(GAP_LOG_PATH, 'r') as f:
            return json.load(f)
    return {
        "metadata": {
            "created": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat(),
            "total_gaps": 0
        },
        "gaps": []
    }


def save_gap_log(data: dict) -> None:
    """Save gap log to file."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    data["metadata"]["last_updated"] = datetime.now().isoformat()
    data["metadata"]["total_gaps"] = len(data["gaps"])
    with open(GAP_LOG_PATH, 'w') as f:
        json.dump(data, f, indent=2)


def generate_gap_id(request: str) -> str:
    """Generate unique gap ID based on timestamp and request hash."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    request_hash = hashlib.md5(request.encode()).hexdigest()[:6]
    return f"gap_{timestamp}_{request_hash}"


def find_similar_gaps(gaps: list, request: str) -> list:
    """Find gaps with similar requests using simple keyword matching."""
    request_words = set(request.lower().split())
    similar = []

    for gap in gaps:
        gap_words = set(gap["request"].lower().split())
        overlap = len(request_words & gap_words)
        if overlap >= 2:  # At least 2 words in common
            similar.append(gap["request"])

    return similar[:5]  # Return top 5 similar


def suggest_category(request: str) -> str:
    """Suggest a category based on keywords in the request."""
    request_lower = request.lower()

    keyword_map = {
        "content-creation": ["write", "create", "script", "post", "article", "blog"],
        "research": ["search", "find", "lookup", "research", "papers", "studies"],
        "analysis": ["analyze", "analyse", "calculate", "statistics", "compare"],
        "visual": ["image", "diagram", "chart", "graph", "infographic", "visual"],
        "medical-imaging": ["ecg", "xray", "mri", "ct scan", "ultrasound", "scan"],
        "audio-video": ["audio", "video", "podcast", "transcribe", "speech"],
        "automation": ["automate", "schedule", "workflow", "batch", "pipeline"],
        "integration": ["connect", "integrate", "api", "sync", "import", "export"],
        "data-extraction": ["extract", "scrape", "parse", "download", "fetch"],
        "quality": ["review", "check", "validate", "verify", "improve"]
    }

    for category, keywords in keyword_map.items():
        if any(kw in request_lower for kw in keywords):
            return category

    return "other"


def suggest_skill_name(request: str) -> str:
    """Generate a potential skill name from the request."""
    # Remove common words
    stop_words = {"i", "need", "to", "want", "can", "you", "the", "a", "an", "is", "it", "for", "from", "with"}
    words = [w.lower() for w in request.split() if w.lower() not in stop_words]

    # Take first 3-4 meaningful words
    name_words = words[:4] if len(words) >= 4 else words

    # Join with hyphens
    return "-".join(name_words) if name_words else "unnamed-skill"


def log_gap(
    request: str,
    context: Optional[str] = None,
    category: Optional[str] = None,
    urgency: str = "medium",
    source: str = "manual"
) -> dict:
    """Log a new capability gap."""

    # Load existing gaps
    data = load_gap_log()

    # Auto-suggest category if not provided
    if category is None:
        category = suggest_category(request)

    # Find similar existing gaps
    similar = find_similar_gaps(data["gaps"], request)

    # Check if this exact request already exists
    existing = [g for g in data["gaps"] if g["request"].lower() == request.lower()]
    if existing:
        # Increment frequency instead of creating new
        existing[0]["frequency"] += 1
        existing[0]["last_seen"] = datetime.now().isoformat()
        save_gap_log(data)
        return {
            "status": "incremented",
            "gap_id": existing[0]["id"],
            "frequency": existing[0]["frequency"],
            "message": f"Gap already exists. Frequency increased to {existing[0]['frequency']}"
        }

    # Create new gap entry
    gap = {
        "id": generate_gap_id(request),
        "timestamp": datetime.now().isoformat(),
        "last_seen": datetime.now().isoformat(),
        "request": request,
        "context": context,
        "category": category,
        "urgency": urgency,
        "frequency": 1,
        "similar_requests": similar,
        "potential_skill": suggest_skill_name(request),
        "source": source,
        "status": "open",
        "notes": []
    }

    data["gaps"].append(gap)
    save_gap_log(data)

    return {
        "status": "logged",
        "gap_id": gap["id"],
        "category": category,
        "potential_skill": gap["potential_skill"],
        "similar_count": len(similar),
        "message": f"Gap logged successfully: {gap['id']}"
    }


def interactive_log():
    """Interactive gap logging mode."""
    print("\n🔍 Gap Logger - Interactive Mode")
    print("=" * 40)

    request = input("\nDescribe what you couldn't do:\n> ").strip()
    if not request:
        print("❌ Request cannot be empty")
        return

    context = input("\nProvide additional context (optional, press Enter to skip):\n> ").strip()
    context = context if context else None

    print(f"\nCategories: {', '.join(CATEGORIES)}")
    suggested = suggest_category(request)
    category = input(f"Category [{suggested}]: ").strip()
    category = category if category in CATEGORIES else suggested

    print(f"\nUrgency levels: {', '.join(URGENCY_LEVELS)}")
    urgency = input("Urgency [medium]: ").strip()
    urgency = urgency if urgency in URGENCY_LEVELS else "medium"

    result = log_gap(request, context, category, urgency, source="interactive")

    print("\n" + "=" * 40)
    print(f"✅ {result['message']}")
    print(f"   Category: {result.get('category', 'N/A')}")
    print(f"   Potential Skill: {result.get('potential_skill', 'N/A')}")
    if result.get('similar_count', 0) > 0:
        print(f"   Similar gaps found: {result['similar_count']}")
    print("=" * 40 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Log capability gaps for the system awareness module"
    )
    parser.add_argument(
        "request",
        nargs="?",
        help="Description of what couldn't be done"
    )
    parser.add_argument(
        "--context", "-c",
        help="Additional context about the request"
    )
    parser.add_argument(
        "--category", "-cat",
        choices=CATEGORIES,
        help="Category for the gap"
    )
    parser.add_argument(
        "--urgency", "-u",
        choices=URGENCY_LEVELS,
        default="medium",
        help="Urgency level (default: medium)"
    )
    parser.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="Interactive logging mode"
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="List recent gaps"
    )

    args = parser.parse_args()

    if args.list:
        data = load_gap_log()
        print(f"\n📋 Recent Gaps ({len(data['gaps'])} total)")
        print("=" * 60)
        for gap in data["gaps"][-10:]:  # Last 10
            print(f"  [{gap['id']}] {gap['request'][:50]}...")
            print(f"    Category: {gap['category']} | Urgency: {gap['urgency']} | Freq: {gap['frequency']}")
        print("=" * 60 + "\n")
        return

    if args.interactive or not args.request:
        interactive_log()
        return

    result = log_gap(
        request=args.request,
        context=args.context,
        category=args.category,
        urgency=args.urgency,
        source="cli"
    )

    print(f"\n✅ {result['message']}")
    if result.get('potential_skill'):
        print(f"   Potential Skill: {result['potential_skill']}")
    print()


if __name__ == "__main__":
    main()
