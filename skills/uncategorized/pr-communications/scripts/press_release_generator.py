#!/usr/bin/env python3
"""
Press Release Generator - Generate AP-style press releases.
"""

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Dict

SKILL_DIR = Path(__file__).parent.parent
PROJECT_ROOT = SKILL_DIR.parent.parent


def load_boilerplate(brand: str = "[PROJECT_NAME]") -> Dict:
    """Load company boilerplate."""
    boilerplate_path = SKILL_DIR / "resources" / "boilerplate" / f"{brand}.md"

    default = {
        "about": f"""SUPRA FORGE develops [PROJECT_NAME], the Neural Quality Layer for automotive engineering. [PROJECT_NAME] enables automotive teams to achieve compliance at the speed of code by providing continuous visibility into ASPICE and ISO 26262 requirements. Unlike traditional compliance tools, [PROJECT_NAME] integrates as an invisible layer across existing engineering workflows, transforming compliance from a periodic burden into a continuous by-product of development.

For more information, visit [supra-forge.com](https://supra-forge.com).""",
        "contact_name": "Media Relations",
        "contact_email": "press@supra-forge.com"
    }

    if boilerplate_path.exists():
        with open(boilerplate_path) as f:
            content = f.read()
            default["about"] = content

    return default


def generate_press_release(
    headline: str,
    news_type: str = "product_launch",
    city: str = "Munich",
    lead: str = None,
    key_facts: str = None,
    quote_name: str = "Tobias Mueller",
    quote_title: str = "Founder & CEO",
    quote_text: str = None,
    availability: str = None,
    brand: str = "[PROJECT_NAME]"
) -> str:
    """Generate a press release."""
    boilerplate = load_boilerplate(brand)
    date = datetime.now().strftime("%B %d, %Y")

    # Default lead paragraph based on type
    default_leads = {
        "product_launch": f"SUPRA FORGE today announced {headline.lower()}, enabling engineering teams to achieve compliance at the speed of code.",
        "partnership": f"SUPRA FORGE today announced a strategic partnership, {headline.lower()}.",
        "funding": f"SUPRA FORGE today announced {headline.lower()}, accelerating the company's mission to transform compliance for automotive engineering teams.",
        "milestone": f"SUPRA FORGE today announced {headline.lower()}, marking a significant milestone in the company's growth.",
        "event": f"SUPRA FORGE today announced {headline.lower()}."
    }

    lead = lead or default_leads.get(news_type, default_leads["product_launch"])

    # Default quote
    quote_text = quote_text or "This represents a significant step forward in our mission to end Audit Blindness and give engineering teams back the 40% of their time currently lost to compliance overhead."

    # Default key facts
    if not key_facts:
        key_facts = """- Real-time compliance visibility across existing tools
- No replacement of current engineering workflows
- 90-minute risk baseline assessment
- Integration with Jira, DOORS, Polarion, Git, and more"""

    pr = f"""# {headline}

**{city}, {date}** — {lead}

## Key Highlights

{key_facts}

## Executive Commentary

"{quote_text}" said {quote_name}, {quote_title} at SUPRA FORGE.

"""

    if availability:
        pr += f"""## Availability

{availability}

"""

    pr += f"""## About SUPRA FORGE

{boilerplate['about']}

## Media Contact

{boilerplate['contact_name']}
SUPRA FORGE
{boilerplate['contact_email']}

###
"""

    return pr


def main():
    parser = argparse.ArgumentParser(description="Generate press release")
    parser.add_argument("--headline", "-h", required=True, help="Press release headline")
    parser.add_argument("--type", "-t", default="product_launch",
                       choices=["product_launch", "partnership", "funding", "milestone", "event"])
    parser.add_argument("--city", "-c", default="Munich", help="Dateline city")
    parser.add_argument("--lead", "-l", help="Lead paragraph")
    parser.add_argument("--facts", "-f", help="Key facts (bullet points)")
    parser.add_argument("--quote", "-q", help="Executive quote")
    parser.add_argument("--quote-name", default="Tobias Mueller", help="Quote attribution name")
    parser.add_argument("--quote-title", default="Founder & CEO", help="Quote attribution title")
    parser.add_argument("--availability", "-a", help="Availability information")
    parser.add_argument("--brand", "-b", default="[PROJECT_NAME]", help="Brand slug")
    parser.add_argument("--output", "-o", help="Output file")

    args = parser.parse_args()

    pr = generate_press_release(
        headline=args.headline,
        news_type=args.type,
        city=args.city,
        lead=args.lead,
        key_facts=args.facts,
        quote_name=args.quote_name,
        quote_title=args.quote_title,
        quote_text=args.quote,
        availability=args.availability,
        brand=args.brand
    )

    if args.output:
        with open(args.output, "w") as f:
            f.write(pr)
        print(f"Press release saved to: {args.output}")
    else:
        print(pr)


if __name__ == "__main__":
    main()
