#!/usr/bin/env python3
"""
Meeting Brief Generator - Generate pre-call intelligence briefs.
"""

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Dict

SKILL_DIR = Path(__file__).parent.parent
PROJECT_ROOT = SKILL_DIR.parent.parent


def load_brand_config(brand_slug: str) -> Dict:
    """Load brand configuration."""
    config_path = PROJECT_ROOT / "context" / "brand_configs" / f"{brand_slug}.json"
    if config_path.exists():
        with open(config_path) as f:
            return json.load(f)
    return {"brand_name": brand_slug.upper(), "demo_booking_url": "https://calendar.google.com"}


def generate_brief(
    company: str,
    contact: str = None,
    contact_title: str = None,
    meeting_type: str = "discovery",
    context: str = None,
    brand_config: Dict = None
) -> str:
    """Generate a pre-call meeting brief."""
    brand_config = brand_config or {}
    booking_url = brand_config.get("demo_booking_url", "https://calendar.google.com")
    product = brand_config.get("brand_name", "[PROJECT_NAME]")

    # Discovery questions based on meeting type
    discovery_questions = {
        "discovery": """### Situational
- What tools are you currently using for requirements management?
- How do you currently prepare for audits?
- How long does your typical audit preparation cycle take?

### Problem
- What's the biggest challenge with your current approach?
- How much engineering time is spent on compliance activities?
- When do you typically discover compliance gaps?

### Implication
- What happens when gaps are discovered late?
- How does this impact your release timeline?
- What's the cost of a failed audit?

### Need-Payoff
- If you could see compliance status in real-time, how would that change things?
- What would reclaiming 40% of engineering time mean for your roadmap?""",

        "demo": """### Technical
- What's your current tool stack (ALM, PLM, CI/CD)?
- How many artifacts do you typically manage?
- What's your team size?

### Integration
- Do you have API access to your current tools?
- Who manages your toolchain?

### Evaluation
- What would success look like in a pilot?
- What's your timeline for making a decision?""",

        "follow-up": """### Progress Check
- How has your thinking evolved since we last spoke?
- Have you discussed with other stakeholders?
- Any new requirements or concerns?

### Next Steps
- What would help you move forward?
- Who else needs to be involved?
- What's the best timeline?"""
    }

    # Pain points based on company type
    pain_points = """- **Audit Blindness**: Not knowing compliance status until audit prep begins
- **Manual Compliance Tax**: 40%+ of engineering time on documentation
- **Tool Fragmentation**: Traceability scattered across Jira, DOORS, Polarion, Git
- **Late Visibility**: Gaps discovered too late to fix efficiently
- **SOP Pressure**: Aggressive timelines with compliance requirements"""

    # Talking points
    talking_points = f"""1. **Lead with the problem**: "Most teams we talk to spend 40% of their time on compliance..."
2. **Position as layer, not replacement**: "We sit on top of your existing tools..."
3. **Emphasize continuous vs. periodic**: "Instead of a 3-month audit prep cycle..."
4. **Reference similar companies**: "A Tier-1 supplier we work with reduced audit prep from 3 months to 2 days..."
5. **Propose clear next step**: "Would a 90-minute baseline assessment be helpful?"""

    brief = f"""# Meeting Brief: {company}

**Meeting Type:** {meeting_type.title()}
**Contact:** {contact or 'TBD'}{f', {contact_title}' if contact_title else ''}
**Prepared:** {datetime.now().strftime('%Y-%m-%d')}
{f'**Context:** {context}' if context else ''}

---

## Company Overview

[Research {company} before the call - check LinkedIn, website, recent news]

**Industry:** [Automotive / Manufacturing / Software]
**Size:** [Employees, likely engineering team size]
**Relevant Products:** [What they build that needs compliance]

---

## Likely Pain Points

{pain_points}

---

## Discovery Questions

{discovery_questions.get(meeting_type, discovery_questions['discovery'])}

---

## Talking Points

{talking_points}

---

## Key Messages

1. **Problem**: "40% of engineering time goes to compliance administration"
2. **Differentiation**: "We're not a tool replacement - we're an invisible layer"
3. **Value**: "See the risk before it sees you"
4. **Proof**: "Teams reduce audit prep from 3 months to 2 days"

---

## Objection Responses

| Objection | Response |
|-----------|----------|
| "We already have tools" | "We integrate with your existing tools - no replacement" |
| "Not a priority now" | "When is your next audit? Would a risk baseline help?" |
| "Need more people involved" | "Happy to do a broader demo - who should join?" |
| "Too expensive" | "What's the cost of 40% of engineering time?" |

---

## Next Steps to Propose

1. **If interested**: Schedule technical demo with engineering team
2. **If exploring**: Offer 90-minute risk baseline assessment
3. **If skeptical**: Share case study or reference call
4. **If not ready**: Add to nurture sequence, follow up in 1 month

---

## Logistics

**Booking Link:** {booking_url}

**Materials:**
- [ ] Pitch deck (if requested)
- [ ] Case study (matching their industry)
- [ ] Technical overview (if technical audience)

---

*Generated by Sales Enablement skill*
"""

    return brief


def main():
    parser = argparse.ArgumentParser(description="Generate meeting brief")
    parser.add_argument("--company", "-c", required=True, help="Company name")
    parser.add_argument("--contact", help="Contact name")
    parser.add_argument("--title", help="Contact title")
    parser.add_argument("--type", "-t", default="discovery", choices=["discovery", "demo", "follow-up"])
    parser.add_argument("--context", help="Additional context")
    parser.add_argument("--brand", "-b", default="[PROJECT_NAME]", help="Brand slug")
    parser.add_argument("--output", "-o", help="Output file")

    args = parser.parse_args()

    brand_config = load_brand_config(args.brand)

    brief = generate_brief(
        company=args.company,
        contact=args.contact,
        contact_title=args.title,
        meeting_type=args.type,
        context=args.context,
        brand_config=brand_config
    )

    if args.output:
        with open(args.output, "w") as f:
            f.write(brief)
        print(f"Brief saved to: {args.output}")
    else:
        print(brief)


if __name__ == "__main__":
    main()
