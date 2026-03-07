#!/usr/bin/env python3
"""
Gap Analyzer - Analyzes patterns in logged gaps and prioritizes skill needs.

Usage:
    python gap_analyzer.py --list              # List all gaps
    python gap_analyzer.py --analyze           # Analyze patterns
    python gap_analyzer.py --report            # Generate priority report
    python gap_analyzer.py --top 5             # Show top 5 priority gaps
"""

import json
import os
import argparse
from datetime import datetime, timedelta
from pathlib import Path
from collections import Counter, defaultdict
from typing import Optional

# Paths
SCRIPT_DIR = Path(__file__).parent.parent
DATA_DIR = SCRIPT_DIR / "data"
GAP_LOG_PATH = DATA_DIR / "gap-log.json"
BACKLOG_PATH = DATA_DIR / "skill-backlog.json"
REGISTRY_PATH = DATA_DIR / "capability-registry.json"


def load_json(path: Path) -> dict:
    """Load JSON file or return empty structure."""
    if path.exists():
        with open(path, 'r') as f:
            return json.load(f)
    return {}


def save_json(path: Path, data: dict) -> None:
    """Save data to JSON file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)


def calculate_priority_score(gap: dict) -> float:
    """
    Calculate priority score for a gap.

    Factors:
    - Frequency (how often requested): 0-40 points
    - Urgency level: 0-30 points
    - Recency (recent requests matter more): 0-20 points
    - Category (some categories are more important): 0-10 points
    """
    score = 0.0

    # Frequency score (40 points max)
    frequency = gap.get("frequency", 1)
    score += min(frequency * 10, 40)

    # Urgency score (30 points max)
    urgency_scores = {
        "critical": 30,
        "high": 20,
        "medium": 10,
        "low": 5
    }
    score += urgency_scores.get(gap.get("urgency", "medium"), 10)

    # Recency score (20 points max)
    try:
        last_seen = datetime.fromisoformat(gap.get("last_seen", gap.get("timestamp", "")))
        days_ago = (datetime.now() - last_seen).days
        recency_score = max(0, 20 - days_ago * 2)  # Lose 2 points per day
        score += recency_score
    except (ValueError, TypeError):
        score += 10  # Default if date parsing fails

    # Category importance (10 points max)
    category_scores = {
        "medical-imaging": 10,  # High priority for medical domain
        "research": 9,
        "content-creation": 8,
        "analysis": 8,
        "quality": 7,
        "automation": 6,
        "visual": 6,
        "data-extraction": 5,
        "integration": 5,
        "audio-video": 5,
        "other": 3
    }
    score += category_scores.get(gap.get("category", "other"), 3)

    return round(score, 1)


def detect_patterns(gaps: list) -> dict:
    """Detect patterns in gaps to identify themes."""
    patterns = {
        "by_category": Counter(),
        "by_urgency": Counter(),
        "high_frequency": [],
        "keyword_clusters": defaultdict(list),
        "recent_surge": [],
        "stale": []
    }

    # Common keywords to look for
    keyword_themes = {
        "image": ["image", "photo", "visual", "picture", "scan"],
        "audio": ["audio", "voice", "speech", "sound", "podcast"],
        "data": ["data", "extract", "parse", "scrape", "download"],
        "analysis": ["analyze", "calculate", "compare", "statistics"],
        "integration": ["api", "connect", "integrate", "sync"],
        "automation": ["automate", "schedule", "batch", "workflow"]
    }

    now = datetime.now()
    week_ago = now - timedelta(days=7)

    for gap in gaps:
        # Category distribution
        patterns["by_category"][gap.get("category", "other")] += 1

        # Urgency distribution
        patterns["by_urgency"][gap.get("urgency", "medium")] += 1

        # High frequency gaps
        if gap.get("frequency", 1) >= 3:
            patterns["high_frequency"].append({
                "id": gap["id"],
                "request": gap["request"],
                "frequency": gap["frequency"]
            })

        # Keyword clustering
        request_lower = gap["request"].lower()
        for theme, keywords in keyword_themes.items():
            if any(kw in request_lower for kw in keywords):
                patterns["keyword_clusters"][theme].append(gap["id"])

        # Recent surge (multiple requests in last week)
        try:
            last_seen = datetime.fromisoformat(gap.get("last_seen", gap.get("timestamp", "")))
            if last_seen >= week_ago and gap.get("frequency", 1) >= 2:
                patterns["recent_surge"].append({
                    "id": gap["id"],
                    "request": gap["request"],
                    "frequency": gap["frequency"]
                })
        except (ValueError, TypeError):
            pass

        # Stale gaps (older than 30 days, not addressed)
        try:
            created = datetime.fromisoformat(gap.get("timestamp", ""))
            if (now - created).days > 30 and gap.get("status") == "open":
                patterns["stale"].append({
                    "id": gap["id"],
                    "request": gap["request"],
                    "days_old": (now - created).days
                })
        except (ValueError, TypeError):
            pass

    return patterns


def generate_recommendations(gaps: list, patterns: dict) -> list:
    """Generate actionable recommendations based on analysis."""
    recommendations = []

    # High frequency gaps should become skills
    for gap in patterns["high_frequency"]:
        recommendations.append({
            "priority": "high",
            "action": "build_skill",
            "gap_id": gap["id"],
            "reason": f"Requested {gap['frequency']} times",
            "suggested_name": gap["request"][:30] + "..."
        })

    # Keyword clusters suggest unified skills
    for theme, gap_ids in patterns["keyword_clusters"].items():
        if len(gap_ids) >= 2:
            recommendations.append({
                "priority": "medium",
                "action": "build_unified_skill",
                "theme": theme,
                "gap_count": len(gap_ids),
                "reason": f"{len(gap_ids)} related gaps around '{theme}'"
            })

    # Stale gaps need decision
    for gap in patterns["stale"]:
        recommendations.append({
            "priority": "low",
            "action": "decide",
            "gap_id": gap["id"],
            "reason": f"Open for {gap['days_old']} days without action"
        })

    return recommendations


def list_gaps(gaps: list, limit: int = None, status: str = None) -> None:
    """Print formatted list of gaps."""
    filtered = gaps
    if status:
        filtered = [g for g in gaps if g.get("status") == status]

    if limit:
        filtered = filtered[-limit:]

    print(f"\n📋 Capability Gaps ({len(filtered)} shown, {len(gaps)} total)")
    print("=" * 80)

    for gap in filtered:
        score = calculate_priority_score(gap)
        print(f"\n  [{gap['id']}]")
        print(f"  📝 {gap['request']}")
        print(f"     Category: {gap.get('category', 'N/A')} | Urgency: {gap.get('urgency', 'N/A')} | Freq: {gap.get('frequency', 1)}")
        print(f"     Priority Score: {score}/100 | Status: {gap.get('status', 'open')}")
        if gap.get("potential_skill"):
            print(f"     💡 Potential Skill: {gap['potential_skill']}")

    print("\n" + "=" * 80)


def show_report(gaps: list, patterns: dict, recommendations: list) -> None:
    """Display comprehensive analysis report."""
    print("\n" + "=" * 80)
    print("                    📊 SYSTEM AWARENESS REPORT")
    print("=" * 80)

    # Summary stats
    print(f"\n📈 Summary")
    print(f"   Total Gaps: {len(gaps)}")
    print(f"   Open: {sum(1 for g in gaps if g.get('status') == 'open')}")
    print(f"   High Frequency (3+): {len(patterns['high_frequency'])}")
    print(f"   Recent Surge: {len(patterns['recent_surge'])}")
    print(f"   Stale (30+ days): {len(patterns['stale'])}")

    # Category distribution
    print(f"\n📂 By Category")
    for cat, count in patterns["by_category"].most_common():
        bar = "█" * min(count * 2, 20)
        print(f"   {cat:20} {bar} ({count})")

    # Urgency distribution
    print(f"\n⚡ By Urgency")
    for urg, count in patterns["by_urgency"].most_common():
        bar = "█" * min(count * 2, 20)
        print(f"   {urg:20} {bar} ({count})")

    # Top priority gaps
    print(f"\n🎯 Top 5 Priority Gaps")
    scored = [(g, calculate_priority_score(g)) for g in gaps if g.get("status") == "open"]
    scored.sort(key=lambda x: x[1], reverse=True)

    for gap, score in scored[:5]:
        print(f"   [{score:5.1f}] {gap['request'][:50]}...")
        print(f"          → Potential: {gap.get('potential_skill', 'N/A')}")

    # Recommendations
    if recommendations:
        print(f"\n💡 Recommendations ({len(recommendations)})")
        for rec in recommendations[:5]:
            icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(rec["priority"], "⚪")
            print(f"   {icon} [{rec['priority'].upper()}] {rec['action']}")
            print(f"      Reason: {rec['reason']}")

    # Keyword themes
    if any(len(ids) >= 2 for ids in patterns["keyword_clusters"].values()):
        print(f"\n🔗 Emerging Themes (2+ related gaps)")
        for theme, gap_ids in patterns["keyword_clusters"].items():
            if len(gap_ids) >= 2:
                print(f"   {theme}: {len(gap_ids)} related gaps")

    print("\n" + "=" * 80)
    print("Run 'python skill_proposer.py --gap-id <ID>' to create a skill proposal")
    print("=" * 80 + "\n")


def update_backlog(gaps: list, patterns: dict) -> None:
    """Update the skill backlog with prioritized gaps."""
    backlog = load_json(BACKLOG_PATH)

    if "metadata" not in backlog:
        backlog["metadata"] = {"created": datetime.now().isoformat()}
    if "backlog" not in backlog:
        backlog["backlog"] = []

    # Get existing backlog IDs
    existing_ids = {item["gap_id"] for item in backlog["backlog"]}

    # Add high-priority gaps to backlog
    scored = [(g, calculate_priority_score(g)) for g in gaps if g.get("status") == "open"]
    scored.sort(key=lambda x: x[1], reverse=True)

    for gap, score in scored:
        if score >= 40 and gap["id"] not in existing_ids:  # Threshold for backlog
            backlog["backlog"].append({
                "id": f"backlog_{datetime.now().strftime('%Y%m%d%H%M%S')}",
                "gap_id": gap["id"],
                "proposed_skill": gap.get("potential_skill", "unnamed"),
                "priority_score": score,
                "category": gap.get("category"),
                "status": "pending_review",
                "added_date": datetime.now().isoformat()
            })

    backlog["metadata"]["last_updated"] = datetime.now().isoformat()
    save_json(BACKLOG_PATH, backlog)
    print(f"✅ Backlog updated with {len(backlog['backlog'])} items")


def main():
    parser = argparse.ArgumentParser(
        description="Analyze capability gaps and prioritize skill needs"
    )
    parser.add_argument("--list", "-l", action="store_true", help="List all gaps")
    parser.add_argument("--analyze", "-a", action="store_true", help="Analyze patterns")
    parser.add_argument("--report", "-r", action="store_true", help="Generate full report")
    parser.add_argument("--top", "-t", type=int, help="Show top N priority gaps")
    parser.add_argument("--status", "-s", help="Filter by status (open/closed)")
    parser.add_argument("--update-backlog", action="store_true", help="Update skill backlog")

    args = parser.parse_args()

    # Load gaps
    gap_data = load_json(GAP_LOG_PATH)
    gaps = gap_data.get("gaps", [])

    if not gaps:
        print("\n📭 No gaps logged yet.")
        print("Use 'python gap_logger.py' to log capability gaps.\n")
        return

    # Default to report if no specific action
    if not any([args.list, args.analyze, args.report, args.top, args.update_backlog]):
        args.report = True

    if args.list:
        list_gaps(gaps, status=args.status)
        return

    # Run analysis
    patterns = detect_patterns(gaps)
    recommendations = generate_recommendations(gaps, patterns)

    if args.top:
        print(f"\n🎯 Top {args.top} Priority Gaps")
        print("=" * 60)
        scored = [(g, calculate_priority_score(g)) for g in gaps if g.get("status") == "open"]
        scored.sort(key=lambda x: x[1], reverse=True)

        for gap, score in scored[:args.top]:
            print(f"\n  [{gap['id']}] Score: {score}/100")
            print(f"  📝 {gap['request']}")
            print(f"  💡 Potential: {gap.get('potential_skill', 'N/A')}")

        print("\n" + "=" * 60 + "\n")
        return

    if args.report or args.analyze:
        show_report(gaps, patterns, recommendations)

    if args.update_backlog:
        update_backlog(gaps, patterns)


if __name__ == "__main__":
    main()
