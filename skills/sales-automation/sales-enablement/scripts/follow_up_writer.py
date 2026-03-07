#!/usr/bin/env python3
"""
Follow-Up Writer - Generate post-meeting follow-up emails.
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
    return {"demo_booking_url": "https://calendar.google.com"}


def generate_follow_up(
    prospect_name: str,
    meeting_notes: str,
    next_steps: str = None,
    timeline: str = "next week",
    brand_config: Dict = None
) -> Dict:
    """Generate a follow-up email."""
    brand_config = brand_config or {}
    booking_url = brand_config.get("demo_booking_url", "https://calendar.google.com")

    # Generate subject
    subject = f"Following up on our conversation"

    # Generate body
    body = f"""Hi {prospect_name},

Thank you for taking the time to speak with me today.

## Key Points We Discussed

{meeting_notes}

## Next Steps

{next_steps or "I'll follow up " + timeline + " to continue the conversation."}

If any questions come up in the meantime, don't hesitate to reach out.

Looking forward to continuing the discussion.

Best,
Tobias

---
Book a follow-up: {booking_url}"""

    return {
        "subject": subject,
        "body": body,
        "prospect": prospect_name,
        "generated_at": datetime.now().isoformat()
    }


def main():
    parser = argparse.ArgumentParser(description="Generate follow-up email")
    parser.add_argument("--prospect", "-p", required=True, help="Prospect name")
    parser.add_argument("--meeting-notes", "-m", required=True, help="Key discussion points")
    parser.add_argument("--next-steps", "-n", help="Agreed next steps")
    parser.add_argument("--timeline", "-t", default="next week", help="Follow-up timeline")
    parser.add_argument("--brand", "-b", default="[PROJECT_NAME]", help="Brand slug")
    parser.add_argument("--output", "-o", choices=["json", "text"], default="text")

    args = parser.parse_args()

    brand_config = load_brand_config(args.brand)

    email = generate_follow_up(
        prospect_name=args.prospect,
        meeting_notes=args.meeting_notes,
        next_steps=args.next_steps,
        timeline=args.timeline,
        brand_config=brand_config
    )

    if args.output == "json":
        print(json.dumps(email, indent=2))
    else:
        print(f"\n{'='*60}")
        print("FOLLOW-UP EMAIL")
        print(f"{'='*60}\n")
        print(f"To: {email['prospect']}")
        print(f"Subject: {email['subject']}\n")
        print("-" * 40)
        print(email['body'])
        print()


if __name__ == "__main__":
    main()
