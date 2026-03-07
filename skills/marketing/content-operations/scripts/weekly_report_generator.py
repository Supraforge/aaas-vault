#!/usr/bin/env python3
"""
Weekly Report Generator - Automated weekly content reports.
"""

import argparse
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List

SKILL_DIR = Path(__file__).parent.parent
PROJECT_ROOT = SKILL_DIR.parent.parent
CALENDAR_PATH = SKILL_DIR / "data" / "calendar.json"


def load_calendar() -> Dict:
    """Load calendar data."""
    if CALENDAR_PATH.exists():
        with open(CALENDAR_PATH) as f:
            return json.load(f)
    return {"entries": []}


def load_brand_config(brand_slug: str) -> Dict:
    """Load brand configuration."""
    config_path = PROJECT_ROOT / "context" / "brand_configs" / f"{brand_slug}.json"
    if config_path.exists():
        with open(config_path) as f:
            return json.load(f)
    return {"brand_name": brand_slug.upper()}


def parse_date(date_str: str) -> datetime:
    """Parse date string to datetime."""
    if date_str == "today":
        return datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    # Try various formats
    for fmt in ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"]:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue

    raise ValueError(f"Could not parse date: {date_str}")


def get_week_entries(start_date: datetime) -> Dict[str, List[Dict]]:
    """Get entries for a week, grouped by status."""
    end_date = start_date + timedelta(days=7)
    cal = load_calendar()
    entries = cal.get("entries", [])

    week_entries = {
        "published": [],
        "scheduled": [],
        "drafted": [],
        "planned": [],
        "idea": []
    }

    for entry in entries:
        date_str = entry.get("scheduled_date", "")
        if not date_str:
            continue

        try:
            entry_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            continue

        # Check if in this week
        if start_date <= entry_date < end_date:
            status = entry.get("status", "planned")
            if status in week_entries:
                week_entries[status].append(entry)

    return week_entries


def get_upcoming_entries(start_date: datetime, days: int = 14) -> List[Dict]:
    """Get entries for upcoming period."""
    end_date = start_date + timedelta(days=days)
    cal = load_calendar()
    entries = cal.get("entries", [])

    upcoming = []
    for entry in entries:
        date_str = entry.get("scheduled_date", "")
        if not date_str:
            continue

        try:
            entry_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            continue

        if start_date <= entry_date < end_date:
            upcoming.append(entry)

    upcoming.sort(key=lambda x: x.get("scheduled_date", ""))
    return upcoming


def calculate_pillar_distribution(entries: List[Dict]) -> Dict[str, int]:
    """Calculate content pillar distribution."""
    distribution = {
        "educational": 0,
        "thought_leadership": 0,
        "engagement": 0,
        "promotional": 0
    }

    for entry in entries:
        pillar = entry.get("pillar", "educational")
        if pillar in distribution:
            distribution[pillar] += 1

    return distribution


def generate_report(start_date: datetime, brand_slug: str = "[PROJECT_NAME]") -> str:
    """Generate weekly content report."""
    brand_config = load_brand_config(brand_slug)
    brand_name = brand_config.get("brand_name", brand_slug.upper())

    end_date = start_date + timedelta(days=7)
    week_entries = get_week_entries(start_date)
    upcoming = get_upcoming_entries(end_date, 14)

    # Calculate totals
    all_week = []
    for entries in week_entries.values():
        all_week.extend(entries)

    total_this_week = len(all_week)
    published_count = len(week_entries["published"])
    pipeline_count = len(week_entries["drafted"]) + len(week_entries["scheduled"])

    # Pillar distribution
    pillar_dist = calculate_pillar_distribution(all_week)

    # Generate report
    report = f"""# Weekly Content Report

**Brand:** {brand_name}
**Week of:** {start_date.strftime('%B %d, %Y')} - {(end_date - timedelta(days=1)).strftime('%B %d, %Y')}
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}

---

## Summary

| Metric | Count |
|--------|-------|
| Total Content Pieces | {total_this_week} |
| Published | {published_count} |
| In Pipeline | {pipeline_count} |
| Planned | {len(week_entries['planned'])} |
| Ideas | {len(week_entries['idea'])} |

## Content Pillar Distribution

| Pillar | Count | Target |
|--------|-------|--------|
| Educational | {pillar_dist['educational']} | 40% |
| Thought Leadership | {pillar_dist['thought_leadership']} | 25% |
| Engagement | {pillar_dist['engagement']} | 25% |
| Promotional | {pillar_dist['promotional']} | 10% |

"""

    # Published content
    if week_entries["published"]:
        report += "## Published This Week\n\n"
        for entry in week_entries["published"]:
            report += f"- **{entry.get('title', 'Untitled')}**\n"
            report += f"  - Platform: {entry.get('platform', 'N/A')} | Type: {entry.get('content_type', 'N/A')}\n"
            report += f"  - Date: {entry.get('scheduled_date', 'N/A')}\n"
    else:
        report += "## Published This Week\n\nNo content published this week.\n"

    report += "\n"

    # Pipeline
    pipeline = week_entries["drafted"] + week_entries["scheduled"]
    if pipeline:
        report += "## Content Pipeline\n\n"
        report += "### Ready to Publish\n\n"
        for entry in week_entries["scheduled"]:
            report += f"- [{entry.get('scheduled_date', 'TBD')}] {entry.get('title', 'Untitled')} ({entry.get('platform', 'N/A')})\n"

        if week_entries["drafted"]:
            report += "\n### In Draft\n\n"
            for entry in week_entries["drafted"]:
                report += f"- {entry.get('title', 'Untitled')} ({entry.get('platform', 'N/A')})\n"
    else:
        report += "## Content Pipeline\n\nNo content in pipeline.\n"

    report += "\n"

    # Upcoming
    if upcoming:
        report += "## Upcoming (Next 2 Weeks)\n\n"
        current_date = None
        for entry in upcoming[:10]:
            entry_date = entry.get("scheduled_date", "")
            if entry_date != current_date:
                if entry_date:
                    try:
                        dt = datetime.strptime(entry_date, "%Y-%m-%d")
                        report += f"\n### {dt.strftime('%A, %B %d')}\n\n"
                    except ValueError:
                        report += f"\n### {entry_date}\n\n"
                current_date = entry_date

            status_icon = {
                "idea": "?", "planned": ".", "drafted": "*",
                "scheduled": ">", "published": "+", "archived": "-"
            }.get(entry.get("status", ""), " ")

            report += f"- [{status_icon}] {entry.get('title', 'Untitled')} ({entry.get('platform', 'N/A')})\n"
    else:
        report += "## Upcoming (Next 2 Weeks)\n\nNo content scheduled.\n"

    report += "\n"

    # Action items
    report += """## Action Items

### This Week
"""

    action_items = []

    if pipeline_count < 3:
        action_items.append("- [ ] Add more content to pipeline (current: {})".format(pipeline_count))

    if pillar_dist["thought_leadership"] == 0:
        action_items.append("- [ ] Create thought leadership content")

    if len(week_entries["idea"]) > 5:
        action_items.append("- [ ] Review and prioritize {} content ideas".format(len(week_entries["idea"])))

    if not action_items:
        action_items.append("- [ ] Review content performance metrics")
        action_items.append("- [ ] Plan next week's content")

    report += "\n".join(action_items)

    report += """

### Ongoing
- [ ] Maintain consistent posting schedule
- [ ] Engage with comments and discussions
- [ ] Track content performance

---

*Report generated by Content Operations skill*
"""

    return report


def main():
    parser = argparse.ArgumentParser(description="Generate weekly content report")
    parser.add_argument("--week-start", "-w", default="today", help="Week start date (YYYY-MM-DD or 'today')")
    parser.add_argument("--brand", "-b", default="[PROJECT_NAME]", help="Brand slug")
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument("--format", "-f", choices=["markdown", "json"], default="markdown", help="Output format")

    args = parser.parse_args()

    try:
        start_date = parse_date(args.week_start)
        # Adjust to Monday of that week
        start_date = start_date - timedelta(days=start_date.weekday())
    except ValueError as e:
        print(f"Error: {e}")
        return

    if args.format == "markdown":
        report = generate_report(start_date, args.brand)

        if args.output:
            with open(args.output, "w") as f:
                f.write(report)
            print(f"Report saved to: {args.output}")
        else:
            print(report)

    elif args.format == "json":
        week_entries = get_week_entries(start_date)
        upcoming = get_upcoming_entries(start_date + timedelta(days=7), 14)

        data = {
            "week_start": start_date.strftime("%Y-%m-%d"),
            "week_end": (start_date + timedelta(days=6)).strftime("%Y-%m-%d"),
            "brand": args.brand,
            "generated_at": datetime.now().isoformat(),
            "summary": {
                "published": len(week_entries["published"]),
                "scheduled": len(week_entries["scheduled"]),
                "drafted": len(week_entries["drafted"]),
                "planned": len(week_entries["planned"]),
                "ideas": len(week_entries["idea"])
            },
            "entries": week_entries,
            "upcoming": upcoming
        }

        if args.output:
            with open(args.output, "w") as f:
                json.dump(data, f, indent=2)
            print(f"Report saved to: {args.output}")
        else:
            print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
