#!/usr/bin/env python3
"""
Calendar Visualizer - Generate visual calendar views.
"""

import argparse
import calendar
import json
import sys
import webbrowser
from datetime import datetime
from pathlib import Path
from typing import Dict, List

SKILL_DIR = Path(__file__).parent.parent
CALENDAR_PATH = SKILL_DIR / "data" / "calendar.json"


def load_calendar() -> Dict:
    """Load calendar data."""
    if CALENDAR_PATH.exists():
        with open(CALENDAR_PATH) as f:
            return json.load(f)
    return {"entries": []}


def get_entries_for_month(year: int, month: int) -> Dict[int, List[Dict]]:
    """Get calendar entries grouped by day for a month."""
    cal = load_calendar()
    entries = cal.get("entries", [])

    by_day = {}
    for entry in entries:
        date_str = entry.get("scheduled_date", "")
        if not date_str:
            continue

        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            if dt.year == year and dt.month == month:
                by_day.setdefault(dt.day, []).append(entry)
        except ValueError:
            continue

    return by_day


def generate_html_calendar(year: int, month: int) -> str:
    """Generate HTML calendar view."""
    entries_by_day = get_entries_for_month(year, month)
    month_name = calendar.month_name[month]

    # Status colors
    status_colors = {
        "idea": "#6b7280",      # gray
        "planned": "#3b82f6",   # blue
        "drafted": "#f59e0b",   # amber
        "scheduled": "#8b5cf6", # purple
        "published": "#10b981", # green
        "archived": "#9ca3af"   # light gray
    }

    # Platform icons (emoji)
    platform_icons = {
        "linkedin": "in",
        "twitter": "X",
        "email": "@",
        "website": "W",
        "blog": "B"
    }

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Content Calendar - {month_name} {year}</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #0f172a;
            color: #f8fafc;
            padding: 20px;
        }}
        h1 {{
            text-align: center;
            margin-bottom: 20px;
            color: #d4a853;
        }}
        .calendar {{
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            gap: 2px;
            background: #1e293b;
            border-radius: 8px;
            overflow: hidden;
            max-width: 1200px;
            margin: 0 auto;
        }}
        .day-header {{
            background: #334155;
            padding: 10px;
            text-align: center;
            font-weight: 600;
            color: #94a3b8;
        }}
        .day {{
            background: #1e293b;
            min-height: 120px;
            padding: 8px;
            border: 1px solid #334155;
        }}
        .day.other-month {{
            background: #0f172a;
            opacity: 0.5;
        }}
        .day.today {{
            border-color: #d4a853;
        }}
        .day-number {{
            font-size: 14px;
            font-weight: 600;
            color: #94a3b8;
            margin-bottom: 5px;
        }}
        .entry {{
            font-size: 11px;
            padding: 4px 6px;
            margin: 2px 0;
            border-radius: 4px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            cursor: pointer;
        }}
        .entry:hover {{
            opacity: 0.8;
        }}
        .platform-badge {{
            display: inline-block;
            width: 16px;
            text-align: center;
            margin-right: 4px;
            font-weight: bold;
        }}
        .legend {{
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
            flex-wrap: wrap;
        }}
        .legend-item {{
            display: flex;
            align-items: center;
            gap: 5px;
            font-size: 12px;
        }}
        .legend-dot {{
            width: 12px;
            height: 12px;
            border-radius: 50%;
        }}
    </style>
</head>
<body>
    <h1>{month_name} {year} - Content Calendar</h1>
    <div class="calendar">
"""

    # Day headers
    for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
        html += f'        <div class="day-header">{day}</div>\n'

    # Get calendar grid
    cal = calendar.Calendar(firstweekday=0)
    today = datetime.now()

    for day_tuple in cal.itermonthdays2(year, month):
        day_num, weekday = day_tuple

        if day_num == 0:
            html += '        <div class="day other-month"></div>\n'
        else:
            is_today = (year == today.year and month == today.month and day_num == today.day)
            day_class = "day today" if is_today else "day"

            html += f'        <div class="{day_class}">\n'
            html += f'            <div class="day-number">{day_num}</div>\n'

            # Add entries for this day
            day_entries = entries_by_day.get(day_num, [])
            for entry in day_entries[:4]:  # Max 4 entries shown
                status = entry.get("status", "planned")
                color = status_colors.get(status, "#3b82f6")
                platform = entry.get("platform", "other")
                icon = platform_icons.get(platform, "?")
                title = entry.get("title", "Untitled")[:25]
                time = entry.get("scheduled_time", "")

                html += f'            <div class="entry" style="background: {color}" title="{entry.get("title", "")} ({status})">\n'
                html += f'                <span class="platform-badge">{icon}</span>{time} {title}\n'
                html += f'            </div>\n'

            if len(day_entries) > 4:
                html += f'            <div style="font-size: 10px; color: #94a3b8;">+{len(day_entries) - 4} more</div>\n'

            html += '        </div>\n'

    html += """    </div>
    <div class="legend">
"""

    for status, color in status_colors.items():
        html += f'        <div class="legend-item"><div class="legend-dot" style="background: {color}"></div>{status}</div>\n'

    html += """    </div>
</body>
</html>
"""

    return html


def generate_markdown_calendar(year: int, month: int) -> str:
    """Generate Markdown calendar view."""
    entries_by_day = get_entries_for_month(year, month)
    month_name = calendar.month_name[month]

    md = f"# Content Calendar - {month_name} {year}\n\n"

    # Get all days with entries
    cal = calendar.Calendar(firstweekday=0)

    md += "| Mon | Tue | Wed | Thu | Fri | Sat | Sun |\n"
    md += "|-----|-----|-----|-----|-----|-----|-----|\n"

    week = []
    for day_tuple in cal.itermonthdays2(year, month):
        day_num, weekday = day_tuple

        if day_num == 0:
            week.append(" ")
        else:
            entries = entries_by_day.get(day_num, [])
            if entries:
                cell = f"**{day_num}** ({len(entries)})"
            else:
                cell = str(day_num)
            week.append(cell)

        if len(week) == 7:
            md += "| " + " | ".join(week) + " |\n"
            week = []

    if week:
        while len(week) < 7:
            week.append(" ")
        md += "| " + " | ".join(week) + " |\n"

    # Detailed list
    md += "\n## Scheduled Content\n\n"

    all_entries = []
    for day, entries in sorted(entries_by_day.items()):
        for entry in entries:
            all_entries.append((day, entry))

    if not all_entries:
        md += "No content scheduled for this month.\n"
    else:
        current_day = None
        for day, entry in all_entries:
            if day != current_day:
                dt = datetime(year, month, day)
                md += f"\n### {dt.strftime('%A, %B %d')}\n\n"
                current_day = day

            status_icon = {
                "idea": "?",
                "planned": ".",
                "drafted": "*",
                "scheduled": ">",
                "published": "+",
                "archived": "-"
            }.get(entry.get("status", ""), " ")

            md += f"- [{status_icon}] **{entry.get('scheduled_time', '')}** - {entry.get('title', 'Untitled')}\n"
            md += f"  - Platform: {entry.get('platform', 'N/A')} | Type: {entry.get('content_type', 'N/A')} | Status: {entry.get('status', 'N/A')}\n"

    md += "\n---\n"
    md += "Legend: [?] idea  [.] planned  [*] drafted  [>] scheduled  [+] published  [-] archived\n"

    return md


def main():
    parser = argparse.ArgumentParser(description="Generate visual calendar views")
    parser.add_argument("--month", "-m", type=int, default=datetime.now().month, help="Month (1-12)")
    parser.add_argument("--year", "-y", type=int, default=datetime.now().year, help="Year")
    parser.add_argument("--format", "-f", choices=["html", "markdown", "json"], default="html", help="Output format")
    parser.add_argument("--output", "-o", help="Output file (default: stdout for markdown/json, browser for html)")
    parser.add_argument("--no-open", action="store_true", help="Don't open HTML in browser")

    args = parser.parse_args()

    if args.format == "html":
        content = generate_html_calendar(args.year, args.month)
        if args.output:
            with open(args.output, "w") as f:
                f.write(content)
            print(f"Calendar saved to: {args.output}")
        else:
            # Save to temp file and open in browser
            temp_path = SKILL_DIR / "data" / f"calendar_{args.year}_{args.month:02d}.html"
            temp_path.parent.mkdir(exist_ok=True)
            with open(temp_path, "w") as f:
                f.write(content)

            if not args.no_open:
                webbrowser.open(f"file://{temp_path}")
                print(f"Calendar opened in browser: {temp_path}")
            else:
                print(content)

    elif args.format == "markdown":
        content = generate_markdown_calendar(args.year, args.month)
        if args.output:
            with open(args.output, "w") as f:
                f.write(content)
            print(f"Calendar saved to: {args.output}")
        else:
            print(content)

    elif args.format == "json":
        entries_by_day = get_entries_for_month(args.year, args.month)
        data = {
            "year": args.year,
            "month": args.month,
            "month_name": calendar.month_name[args.month],
            "entries_by_day": {str(k): v for k, v in entries_by_day.items()}
        }
        if args.output:
            with open(args.output, "w") as f:
                json.dump(data, f, indent=2)
            print(f"Calendar saved to: {args.output}")
        else:
            print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
