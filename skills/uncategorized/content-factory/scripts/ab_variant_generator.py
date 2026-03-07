#!/usr/bin/env python3
"""
A/B Variant Generator - Generate copy variants for testing.
"""

import argparse
import json
import random
from typing import List, Dict

# Headline transformation patterns
HEADLINE_PATTERNS = {
    "question": "What if {core_concept}?",
    "how_to": "How to {action} in {timeframe}",
    "number": "{number} ways to {action}",
    "contrarian": "Why {conventional_wisdom} is wrong",
    "benefit": "{benefit} without {pain}",
    "urgency": "Stop {pain} before it costs you {cost}",
    "curiosity": "The hidden truth about {topic}",
}

# Power words for copy
POWER_WORDS = {
    "urgency": ["now", "today", "immediately", "instant", "fast"],
    "value": ["free", "save", "proven", "guaranteed", "exclusive"],
    "emotion": ["discover", "unlock", "transform", "breakthrough", "revolutionary"],
    "trust": ["proven", "trusted", "expert", "certified", "secure"]
}


def generate_headline_variants(original: str, num_variants: int = 3) -> List[Dict]:
    """Generate headline variants."""
    variants = [{"variant": 1, "copy": original, "rationale": "Original headline"}]

    # Extract key concepts from original
    words = original.lower().split()

    # Variant 2: Question form
    if "?" not in original:
        question = f"What if you could {original.lower().rstrip('.')}?"
        variants.append({
            "variant": 2,
            "copy": question,
            "rationale": "Question format increases curiosity and engagement"
        })

    # Variant 3: Benefit-focused
    benefit_variant = f"Finally: {original}"
    variants.append({
        "variant": 3,
        "copy": benefit_variant,
        "rationale": "Opens with 'Finally' to suggest solution to long-standing problem"
    })

    # Variant 4: Numbers
    number_variant = f"The 3-step approach: {original}"
    variants.append({
        "variant": 4,
        "copy": number_variant,
        "rationale": "Numbers increase specificity and clickability"
    })

    # Variant 5: Urgency
    urgency_variant = f"{original} (Before your next audit)"
    variants.append({
        "variant": 5,
        "copy": urgency_variant,
        "rationale": "Adds urgency with specific deadline reference"
    })

    return variants[:num_variants + 1]


def generate_cta_variants(original: str, num_variants: int = 3) -> List[Dict]:
    """Generate CTA variants."""
    variants = [{"variant": 1, "copy": original, "rationale": "Original CTA"}]

    cta_patterns = [
        ("Get {}", "Action-oriented, focuses on receiving value"),
        ("Start {}", "Emphasizes beginning of journey"),
        ("Discover {}", "Appeals to curiosity"),
        ("Claim {}", "Creates sense of ownership"),
        ("Unlock {}", "Suggests hidden value"),
    ]

    # Extract the action/object from original
    core = original.replace("Get ", "").replace("Start ", "").replace("Learn ", "")

    for i, (pattern, rationale) in enumerate(cta_patterns[:num_variants], 2):
        variants.append({
            "variant": i,
            "copy": pattern.format(core),
            "rationale": rationale
        })

    return variants[:num_variants + 1]


def generate_body_variants(original: str, num_variants: int = 3) -> List[Dict]:
    """Generate body copy variants."""
    variants = [{"variant": 1, "copy": original, "rationale": "Original copy"}]

    # Variant 2: Lead with statistic
    stat_version = f"40% of engineering time is lost to compliance overhead.\n\n{original}"
    variants.append({
        "variant": 2,
        "copy": stat_version,
        "rationale": "Opens with specific statistic to establish credibility"
    })

    # Variant 3: Lead with question
    question_version = f"How much time does your team spend on audit prep?\n\n{original}"
    variants.append({
        "variant": 3,
        "copy": question_version,
        "rationale": "Opens with question to engage reader"
    })

    # Variant 4: Lead with story
    story_version = f"A Tier-1 supplier told us their audit prep took 3 months. Now it takes 2 days.\n\n{original}"
    variants.append({
        "variant": 4,
        "copy": story_version,
        "rationale": "Opens with mini case study for social proof"
    })

    return variants[:num_variants + 1]


def main():
    parser = argparse.ArgumentParser(description="Generate A/B copy variants")
    parser.add_argument("--copy", "-c", required=True, help="Original copy to create variants from")
    parser.add_argument("--type", "-t", default="headline", choices=["headline", "cta", "body"])
    parser.add_argument("--variants", "-v", type=int, default=3, help="Number of variants")
    parser.add_argument("--output", "-o", choices=["json", "text"], default="text")

    args = parser.parse_args()

    if args.type == "headline":
        variants = generate_headline_variants(args.copy, args.variants)
    elif args.type == "cta":
        variants = generate_cta_variants(args.copy, args.variants)
    else:
        variants = generate_body_variants(args.copy, args.variants)

    if args.output == "json":
        print(json.dumps(variants, indent=2))
    else:
        print(f"\n{'='*60}")
        print(f"A/B VARIANTS: {args.type.upper()}")
        print(f"Original: \"{args.copy}\"")
        print(f"{'='*60}\n")

        for v in variants:
            print(f"--- Variant {v['variant']} ---")
            print(f"Copy: {v['copy']}")
            print(f"Rationale: {v['rationale']}")
            print()


if __name__ == "__main__":
    main()
