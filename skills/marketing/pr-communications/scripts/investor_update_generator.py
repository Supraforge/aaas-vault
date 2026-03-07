#!/usr/bin/env python3
"""
Investor Update Generator - Generate monthly investor update emails.
"""

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

SKILL_DIR = Path(__file__).parent.parent
PROJECT_ROOT = SKILL_DIR.parent.parent


def generate_investor_update(
    period: str,
    highlights: List[str] = None,
    metrics: Dict = None,
    challenges: List[str] = None,
    asks: List[str] = None,
    next_priorities: List[str] = None,
    company_name: str = "SUPRA FORGE"
) -> str:
    """Generate investor update email."""

    # Default highlights
    highlights = highlights or [
        "Continued product development",
        "Expanding market conversations",
        "Building pipeline"
    ]

    # Default metrics
    metrics = metrics or {
        "mrr": {"current": 0, "change": "N/A"},
        "pipeline": {"current": "Early stage"},
        "customers": {"current": 0, "pilots": "In discussion"},
        "runway": {"months": 12}
    }

    # Default next priorities
    next_priorities = next_priorities or [
        "Close first pilot customer",
        "Complete product MVP",
        "Build case study"
    ]

    # Build TLDR
    tldr_items = []
    for h in highlights[:5]:
        tldr_items.append(f"- {h}")
    tldr = "\n".join(tldr_items)

    # Build metrics section
    metrics_md = """| Metric | Current | Change |
|--------|---------|--------|
"""
    if "mrr" in metrics:
        mrr = metrics["mrr"]
        metrics_md += f"| MRR | ${mrr.get('current', 0):,} | {mrr.get('change', 'N/A')} |\n"
    if "customers" in metrics:
        cust = metrics["customers"]
        metrics_md += f"| Customers | {cust.get('current', 0)} | {cust.get('pilots', 'N/A')} pilots |\n"
    if "pipeline" in metrics:
        pipe = metrics["pipeline"]
        metrics_md += f"| Pipeline | {pipe.get('current', 'Building')} | - |\n"
    if "runway" in metrics:
        runway = metrics["runway"]
        metrics_md += f"| Runway | {runway.get('months', 12)} months | - |\n"

    # Build challenges section
    challenges_md = ""
    if challenges:
        challenges_md = "\n## Challenges\n\n"
        for c in challenges:
            challenges_md += f"- {c}\n"

    # Build asks section
    asks_md = ""
    if asks:
        asks_md = "\n## How You Can Help\n\n"
        for a in asks:
            asks_md += f"- {a}\n"

    # Build next priorities
    next_md = ""
    if next_priorities:
        next_md = "\n".join(f"1. {p}" for p in next_priorities)

    update = f"""# {company_name} | {period} Update

Dear Investors,

Here's your monthly update on {company_name} progress.

---

## TL;DR

{tldr}

---

## Key Metrics

{metrics_md}

---

## Highlights

### Product
[Product developments this month - new features, technical milestones, integrations]

### Customers / Pipeline
[Customer conversations, pilot progress, pipeline development]

### Team
[Hiring updates, organizational changes, team highlights]

{challenges_md}
{asks_md}

---

## What's Next

{next_md}

---

Thank you for your continued support. Happy to jump on a call if you'd like to discuss any of this in more detail.

Best,
Tobias
Founder & CEO, {company_name}

---

*Update generated {datetime.now().strftime('%Y-%m-%d')}*
"""

    return update


def main():
    parser = argparse.ArgumentParser(description="Generate investor update")
    parser.add_argument("--period", "-p", required=True, help="Update period (e.g., 'February 2026')")
    parser.add_argument("--highlights", help="Comma-separated highlights")
    parser.add_argument("--metrics", "-m", help="Metrics as JSON")
    parser.add_argument("--challenges", "-c", help="Comma-separated challenges")
    parser.add_argument("--asks", "-a", help="Comma-separated asks")
    parser.add_argument("--priorities", help="Comma-separated next priorities")
    parser.add_argument("--company", default="SUPRA FORGE", help="Company name")
    parser.add_argument("--output", "-o", help="Output file")

    args = parser.parse_args()

    highlights = args.highlights.split(",") if args.highlights else None
    challenges = args.challenges.split(",") if args.challenges else None
    asks = args.asks.split(",") if args.asks else None
    priorities = args.priorities.split(",") if args.priorities else None

    metrics = None
    if args.metrics:
        try:
            metrics = json.loads(args.metrics)
        except json.JSONDecodeError:
            print("Warning: Could not parse metrics JSON, using defaults")

    update = generate_investor_update(
        period=args.period,
        highlights=highlights,
        metrics=metrics,
        challenges=challenges,
        asks=asks,
        next_priorities=priorities,
        company_name=args.company
    )

    if args.output:
        with open(args.output, "w") as f:
            f.write(update)
        print(f"Investor update saved to: {args.output}")
    else:
        print(update)


if __name__ == "__main__":
    main()
