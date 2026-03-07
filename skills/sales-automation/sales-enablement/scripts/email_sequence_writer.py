#!/usr/bin/env python3
"""
Email Sequence Writer - Generate multi-email nurture sequences.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List

SKILL_DIR = Path(__file__).parent.parent
PROJECT_ROOT = SKILL_DIR.parent.parent


def load_brand_config(brand_slug: str) -> Dict:
    """Load brand configuration."""
    config_path = PROJECT_ROOT / "context" / "brand_configs" / f"{brand_slug}.json"
    if config_path.exists():
        with open(config_path) as f:
            return json.load(f)
    return {"brand_name": brand_slug.upper(), "demo_booking_url": "https://calendar.google.com"}


def generate_nurture_sequence(prospect: Dict, brand_config: Dict, num_emails: int = 5) -> List[Dict]:
    """Generate a nurture email sequence."""
    name = prospect.get("name", "there")
    company = prospect.get("company", "your company")
    pain_point = prospect.get("pain_point", "compliance overhead")
    product = brand_config.get("brand_name", "[PROJECT_NAME]")
    booking_url = brand_config.get("demo_booking_url", "https://calendar.google.com")

    emails = [
        {
            "email_number": 1,
            "day": 0,
            "subject": f"{name}, is {pain_point} costing you more than you think?",
            "body": f"""Hi {name},

I've been following {company}'s work in the industry, and I noticed something that might resonate with you.

Most engineering teams we talk to spend 40% of their time on {pain_point}. That's nearly half their capacity diverted from actual innovation.

The question isn't whether this is happening - it's what the hidden cost really is.

I put together a quick framework for calculating this. Would it be useful if I shared it with you?

Best,
Tobias"""
        },
        {
            "email_number": 2,
            "day": 3,
            "subject": "The 40% tax nobody talks about",
            "body": f"""Hi {name},

Following up on my last note about {pain_point}.

Here's what we've learned from working with teams like yours:

**The Real Cost:**
- 40% of engineering time on administration
- 3-month feedback loops creating blind spots
- Critical issues discovered too late to fix efficiently

**The Pattern:**
Teams don't notice it because it's "just how things are done." But once you see it, you can't unsee it.

Does this match what you're seeing at {company}?

Best,
Tobias"""
        },
        {
            "email_number": 3,
            "day": 7,
            "subject": f"What if {pain_point} became a by-product?",
            "body": f"""Hi {name},

Imagine if {pain_point} wasn't a separate activity - but happened automatically as a by-product of your existing workflow.

That's the approach behind {product}.

Instead of manual documentation and periodic audits, you get:
- Continuous visibility into compliance status
- Automated traceability across your tools
- Real-time risk detection before issues compound

Would a 15-minute demo be worth your time?

Best,
Tobias"""
        },
        {
            "email_number": 4,
            "day": 12,
            "subject": "How [Similar Company] reduced compliance overhead by 60%",
            "body": f"""Hi {name},

Quick case study I thought you'd find relevant:

A Tier-1 automotive supplier was facing the same {pain_point} challenge. They were spending 3+ months preparing for each audit.

After implementing {product}:
- Audit prep time: 3 months → 2 days
- Engineering time reclaimed: 40%
- Compliance visibility: Real-time

I'd be happy to walk you through how this might look for {company}.

{booking_url}

Best,
Tobias"""
        },
        {
            "email_number": 5,
            "day": 18,
            "subject": f"Quick question, {name}",
            "body": f"""Hi {name},

I've shared a few thoughts on {pain_point} over the past few weeks. Before I assume this isn't a priority, I wanted to ask directly:

1. Is {pain_point} something {company} is actively trying to solve?
2. If so, would a 15-minute conversation make sense?

If the timing isn't right, just let me know.

Best,
Tobias

{booking_url}"""
        }
    ]

    return emails[:num_emails]


def generate_onboarding_sequence(prospect: Dict, brand_config: Dict, num_emails: int = 5) -> List[Dict]:
    """Generate an onboarding email sequence."""
    name = prospect.get("name", "there")
    product = brand_config.get("brand_name", "[PROJECT_NAME]")

    emails = [
        {
            "email_number": 1,
            "day": 0,
            "subject": f"Welcome to {product} - Let's get you started",
            "body": f"""Hi {name},

Welcome to {product}! We're excited to have you on board.

Here's your quick-start guide:

**Step 1:** Connect your first tool (5 min)
**Step 2:** Run your baseline scan (15 min)
**Step 3:** Review your risk dashboard

Need help? Reply to this email or book a setup call.

Best,
The {product} Team"""
        },
        {
            "email_number": 2,
            "day": 2,
            "subject": "Did you run your first scan?",
            "body": f"""Hi {name},

Just checking in - have you had a chance to run your first baseline scan?

Most teams are surprised by what they find. The average first scan reveals 15-20 traceability gaps that would have become audit findings.

If you haven't started yet, here's a quick video walkthrough: [link]

Any questions, just reply.

Best,
The {product} Team"""
        },
        {
            "email_number": 3,
            "day": 5,
            "subject": "Pro tip: Set up continuous monitoring",
            "body": f"""Hi {name},

Now that you've run your first scan, here's the next step most successful teams take:

**Enable continuous monitoring**

This means {product} will automatically detect new gaps as they emerge, rather than waiting for your next manual scan.

Here's how to set it up: [link]

Best,
The {product} Team"""
        }
    ]

    return emails[:num_emails]


def main():
    parser = argparse.ArgumentParser(description="Generate email nurture sequences")
    parser.add_argument("--prospect", "-p", required=True, help="Prospect data as JSON")
    parser.add_argument("--type", "-t", default="nurture", choices=["nurture", "onboarding", "reengagement"])
    parser.add_argument("--emails", "-e", type=int, default=5, help="Number of emails")
    parser.add_argument("--brand", "-b", default="[PROJECT_NAME]", help="Brand slug")
    parser.add_argument("--output", "-o", choices=["json", "text"], default="text")

    args = parser.parse_args()

    try:
        prospect = json.loads(args.prospect)
    except json.JSONDecodeError as e:
        print(f"Error parsing prospect JSON: {e}", file=sys.stderr)
        sys.exit(1)

    brand_config = load_brand_config(args.brand)

    if args.type == "nurture":
        emails = generate_nurture_sequence(prospect, brand_config, args.emails)
    elif args.type == "onboarding":
        emails = generate_onboarding_sequence(prospect, brand_config, args.emails)
    else:
        emails = generate_nurture_sequence(prospect, brand_config, args.emails)

    if args.output == "json":
        print(json.dumps(emails, indent=2))
    else:
        print(f"\n{'='*60}")
        print(f"EMAIL SEQUENCE: {args.type.upper()}")
        print(f"Prospect: {prospect.get('name', 'Unknown')} @ {prospect.get('company', 'Unknown')}")
        print(f"{'='*60}\n")

        for email in emails:
            print(f"--- EMAIL {email['email_number']} (Day {email['day']}) ---")
            print(f"Subject: {email['subject']}")
            print(f"\n{email['body']}")
            print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()
