#!/usr/bin/env python3
"""
Calendar Manager - CRUD operations for content calendar.
"""

import argparse
import json
import sys
import uuid
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional

SKILL_DIR = Path(__file__).parent.parent
CALENDAR_PATH = SKILL_DIR / "data" / "calendar.json"


def ensure_data_dir():
    """Ensure data directory exists."""
    (SKILL_DIR / "data").mkdir(exist_ok=True)


def load_calendar() -> Dict:
    """Load or create calendar data."""
    ensure_data_dir()
    if CALENDAR_PATH.exists():
        with open(CALENDAR_PATH) as f:
            return json.load(f)
    return {"entries": [], "last_updated": None}


def save_calendar(calendar: Dict):
    """Save calendar data."""
    ensure_data_dir()
    calendar["last_updated"] = datetime.now().isoformat()
    with open(CALENDAR_PATH, "w") as f:
        json.dump(calendar, f, indent=2)


def parse_date(date_str: str) -> str:
    """Parse date string to YYYY-MM-DD format."""
    if date_str == "today":
        return datetime.now().strftime("%Y-%m-%d")
    if date_str.startswith("+"):
        # Relative date like +7d
        days = int(date_str[1:-1])
        return (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
    # Assume already in correct format
    return date_str


def generate_id() -> str:
    """Generate unique calendar entry ID."""
    return f"cal_{uuid.uuid4().hex[:8]}"


def add_entry(
    title: str,
    content_type: str,
    platform: str,
    scheduled_date: str,
    scheduled_time: str = "09:00",
    pillar: str = "educational",
    status: str = "planned",
    content_path: str = None,
    assets: List[str] = None,
    tags: List[str] = None
) -> Dict:
    """Add new calendar entry."""
    calendar = load_calendar()

    entry = {
        "id": generate_id(),
        "title": title,
        "content_type": content_type,
        "platform": platform,
        "pillar": pillar,
        "scheduled_date": parse_date(scheduled_date),
        "scheduled_time": scheduled_time,
        "status": status,
        "content_path": content_path,
        "assets": assets or [],
        "tags": tags or [],
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }

    calendar["entries"].append(entry)
    save_calendar(calendar)

    return entry


def get_entries(
    start_date: str = None,
    end_date: str = None,
    platform: str = None,
    content_type: str = None,
    status: str = None,
    pillar: str = None
) -> List[Dict]:
    """Get calendar entries with filtering."""
    calendar = load_calendar()
    entries = calendar.get("entries", [])

    # Parse dates
    if start_date:
        start = parse_date(start_date)
        entries = [e for e in entries if e.get("scheduled_date", "") >= start]

    if end_date:
        end = parse_date(end_date)
        entries = [e for e in entries if e.get("scheduled_date", "") <= end]

    # Other filters
    if platform:
        entries = [e for e in entries if e.get("platform") == platform]

    if content_type:
        entries = [e for e in entries if e.get("content_type") == content_type]

    if status:
        entries = [e for e in entries if e.get("status") == status]

    if pillar:
        entries = [e for e in entries if e.get("pillar") == pillar]

    # Sort by date
    entries.sort(key=lambda x: (x.get("scheduled_date", ""), x.get("scheduled_time", "")))

    return entries


def update_entry(entry_id: str, updates: Dict) -> Optional[Dict]:
    """Update calendar entry."""
    calendar = load_calendar()

    for i, entry in enumerate(calendar.get("entries", [])):
        if entry["id"] == entry_id:
            # Apply updates
            for key, value in updates.items():
                if key not in ["id", "created_at"]:  # Protect these fields
                    entry[key] = value
            entry["updated_at"] = datetime.now().isoformat()
            calendar["entries"][i] = entry
            save_calendar(calendar)
            return entry

    return None


def delete_entry(entry_id: str) -> bool:
    """Delete calendar entry."""
    calendar = load_calendar()
    original_count = len(calendar.get("entries", []))

    calendar["entries"] = [e for e in calendar.get("entries", []) if e["id"] != entry_id]

    if len(calendar["entries"]) < original_count:
        save_calendar(calendar)
        return True

    return False


def main():
    parser = argparse.ArgumentParser(description="Manage content calendar")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add command
    add_parser = subparsers.add_parser("add", help="Add calendar entry")
    add_parser.add_argument("--title", "-t", required=True, help="Entry title")
    add_parser.add_argument("--type", dest="content_type", required=True,
                           choices=["social", "email", "blog", "video"],
                           help="Content type")
    add_parser.add_argument("--platform", "-p", required=True,
                           help="Platform (linkedin, twitter, email, website)")
    add_parser.add_argument("--date", "-d", required=True, help="Scheduled date (YYYY-MM-DD or 'today' or '+7d')")
    add_parser.add_argument("--time", default="09:00", help="Scheduled time (default: 09:00)")
    add_parser.add_argument("--pillar", default="educational",
                           choices=["educational", "thought_leadership", "engagement", "promotional"])
    add_parser.add_argument("--status", default="planned",
                           choices=["idea", "planned", "drafted", "scheduled", "published", "archived"])
    add_parser.add_argument("--content-path", help="Path to content file")
    add_parser.add_argument("--tags", help="Comma-separated tags")

    # Get command
    get_parser = subparsers.add_parser("get", help="Get calendar entries")
    get_parser.add_argument("--start", "-s", help="Start date")
    get_parser.add_argument("--end", "-e", help="End date")
    get_parser.add_argument("--platform", "-p", help="Filter by platform")
    get_parser.add_argument("--type", dest="content_type", help="Filter by content type")
    get_parser.add_argument("--status", help="Filter by status")
    get_parser.add_argument("--pillar", help="Filter by content pillar")
    get_parser.add_argument("--output", "-o", choices=["json", "text"], default="text")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update calendar entry")
    update_parser.add_argument("entry_id", help="Entry ID to update")
    update_parser.add_argument("--title", help="New title")
    update_parser.add_argument("--status", help="New status")
    update_parser.add_argument("--date", dest="scheduled_date", help="New scheduled date")
    update_parser.add_argument("--time", dest="scheduled_time", help="New scheduled time")
    update_parser.add_argument("--content-path", help="Path to content file")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete calendar entry")
    delete_parser.add_argument("entry_id", help="Entry ID to delete")
    delete_parser.add_argument("--force", "-f", action="store_true", help="Skip confirmation")

    args = parser.parse_args()

    if args.command == "add":
        tags = args.tags.split(",") if args.tags else []
        entry = add_entry(
            title=args.title,
            content_type=args.content_type,
            platform=args.platform,
            scheduled_date=args.date,
            scheduled_time=args.time,
            pillar=args.pillar,
            status=args.status,
            content_path=args.content_path,
            tags=tags
        )
        print(f"Created entry: {entry['id']}")
        print(f"  Title: {entry['title']}")
        print(f"  Date: {entry['scheduled_date']} {entry['scheduled_time']}")

    elif args.command == "get":
        entries = get_entries(
            start_date=args.start,
            end_date=args.end,
            platform=args.platform,
            content_type=args.content_type,
            status=args.status,
            pillar=args.pillar
        )

        if args.output == "json":
            print(json.dumps(entries, indent=2))
        else:
            print(f"\n{'='*70}")
            print(f"CONTENT CALENDAR ({len(entries)} entries)")
            print(f"{'='*70}\n")

            if not entries:
                print("No entries found matching criteria.\n")
                return

            # Group by date
            by_date = {}
            for e in entries:
                date = e.get("scheduled_date", "Unknown")
                by_date.setdefault(date, []).append(e)

            for date, date_entries in sorted(by_date.items()):
                # Format date header
                try:
                    dt = datetime.strptime(date, "%Y-%m-%d")
                    date_str = dt.strftime("%A, %B %d, %Y")
                except:
                    date_str = date

                print(f"--- {date_str} ---")
                for e in date_entries:
                    status_icon = {
                        "idea": "?",
                        "planned": ".",
                        "drafted": "*",
                        "scheduled": ">",
                        "published": "+",
                        "archived": "-"
                    }.get(e.get("status", ""), " ")

                    print(f"  [{status_icon}] {e['scheduled_time']} | {e['platform']:10} | {e['title'][:40]}")
                    print(f"      ID: {e['id']} | Type: {e['content_type']} | Pillar: {e.get('pillar', 'N/A')}")
                print()

            # Legend
            print("Legend: [?] idea  [.] planned  [*] drafted  [>] scheduled  [+] published  [-] archived")
            print()

    elif args.command == "update":
        updates = {}
        if args.title:
            updates["title"] = args.title
        if args.status:
            updates["status"] = args.status
        if args.scheduled_date:
            updates["scheduled_date"] = parse_date(args.scheduled_date)
        if args.scheduled_time:
            updates["scheduled_time"] = args.scheduled_time
        if args.content_path:
            updates["content_path"] = args.content_path

        if not updates:
            print("Error: No updates specified", file=sys.stderr)
            sys.exit(1)

        entry = update_entry(args.entry_id, updates)
        if entry:
            print(f"Updated entry: {entry['id']}")
            print(f"  Title: {entry['title']}")
            print(f"  Status: {entry['status']}")
        else:
            print(f"Error: Entry not found: {args.entry_id}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "delete":
        if not args.force:
            confirm = input(f"Delete entry {args.entry_id}? [y/N] ")
            if confirm.lower() != "y":
                print("Cancelled")
                return

        if delete_entry(args.entry_id):
            print(f"Deleted entry: {args.entry_id}")
        else:
            print(f"Error: Entry not found: {args.entry_id}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
