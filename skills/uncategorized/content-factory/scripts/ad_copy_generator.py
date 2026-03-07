#!/usr/bin/env python3
"""
Ad Copy Generator - Generate platform-optimized ad copy.
"""

import argparse
import json
from typing import Dict, List

# Platform specifications
PLATFORM_SPECS = {
    "linkedin_sponsored": {
        "name": "LinkedIn Sponsored Content",
        "headline_max": 70,
        "headline_recommended": 50,
        "description_max": 300,
        "cta_options": ["Learn More", "Download", "Sign Up", "Contact Us", "Apply Now"],
        "image_size": "1200x627"
    },
    "linkedin_text": {
        "name": "LinkedIn Text Ads",
        "headline_max": 25,
        "description_max": 75,
        "image_size": "100x100"
    },
    "google_search": {
        "name": "Google Responsive Search Ads",
        "headline_max": 30,
        "headline_count": 3,
        "description_max": 90,
        "description_count": 2,
        "path_max": 15
    },
    "google_display": {
        "name": "Google Display Ads",
        "headline_max": 30,
        "long_headline_max": 90,
        "description_max": 90
    }
}


def generate_linkedin_sponsored(product: str, offer: str, audience: str = None) -> Dict:
    """Generate LinkedIn sponsored content ad."""
    spec = PLATFORM_SPECS["linkedin_sponsored"]

    headlines = [
        f"Stop Audit Blindness. See Risks First.",
        f"40% Engineering Time Back. {product}.",
        f"Compliance at the Speed of Code",
        f"{offer} - {product}",
    ]

    descriptions = [
        f"Engineering teams lose 40% of their time to compliance overhead. {product} provides real-time visibility into ASPICE and ISO 26262 requirements - no tool replacement needed.",
        f"See the risk before it sees you. {product} turns compliance from a 3-month audit prep cycle into a continuous by-product of development. Get your free baseline.",
        f"Tired of audit surprises? {product} integrates with your existing tools to provide continuous compliance visibility. {offer} - no commitment required.",
    ]

    return {
        "platform": spec["name"],
        "variants": [
            {
                "variant": i + 1,
                "headline": h[:spec["headline_max"]],
                "headline_chars": len(h),
                "description": d[:spec["description_max"]],
                "description_chars": len(d),
                "cta": "Learn More",
                "within_limits": len(h) <= spec["headline_max"] and len(d) <= spec["description_max"]
            }
            for i, (h, d) in enumerate(zip(headlines, descriptions))
        ],
        "specs": spec
    }


def generate_google_search(product: str, offer: str, audience: str = None) -> Dict:
    """Generate Google responsive search ads."""
    spec = PLATFORM_SPECS["google_search"]

    headlines = [
        f"{product} - Compliance Solution",
        "Real-Time ASPICE Visibility",
        f"{offer}",
        "40% Engineering Time Back",
        "Stop Audit Blindness Now",
        "Continuous Compliance",
        "ISO 26262 Made Simple",
        "See Risks Before Audits",
    ]

    descriptions = [
        f"{product} turns compliance into a by-product of development. Real-time visibility, no tool replacement.",
        f"Engineering teams reclaim 40% of their time. Get your {offer.lower()} and see the difference.",
    ]

    return {
        "platform": spec["name"],
        "headlines": [
            {"text": h[:spec["headline_max"]], "chars": len(h), "within_limit": len(h) <= spec["headline_max"]}
            for h in headlines[:8]
        ],
        "descriptions": [
            {"text": d[:spec["description_max"]], "chars": len(d), "within_limit": len(d) <= spec["description_max"]}
            for d in descriptions
        ],
        "paths": [product.lower(), "demo"],
        "specs": spec
    }


def generate_linkedin_text(product: str, offer: str, audience: str = None) -> Dict:
    """Generate LinkedIn text ads."""
    spec = PLATFORM_SPECS["linkedin_text"]

    ads = [
        {"headline": f"{product} for ASPICE", "description": f"{offer}. Real-time compliance visibility for engineering teams."},
        {"headline": "Stop Audit Blindness", "description": f"40% engineering time back. {offer} from {product}."},
        {"headline": "Compliance Made Easy", "description": f"{product}: Real-time ASPICE & ISO 26262 visibility."},
    ]

    return {
        "platform": spec["name"],
        "variants": [
            {
                "variant": i + 1,
                "headline": ad["headline"][:spec["headline_max"]],
                "headline_chars": len(ad["headline"]),
                "description": ad["description"][:spec["description_max"]],
                "description_chars": len(ad["description"]),
                "within_limits": len(ad["headline"]) <= spec["headline_max"] and len(ad["description"]) <= spec["description_max"]
            }
            for i, ad in enumerate(ads)
        ],
        "specs": spec
    }


def main():
    parser = argparse.ArgumentParser(description="Generate platform-optimized ad copy")
    parser.add_argument("--product", "-p", default="[PROJECT_NAME]", help="Product name")
    parser.add_argument("--platform", required=True, choices=list(PLATFORM_SPECS.keys()))
    parser.add_argument("--offer", "-o", default="Free Risk Baseline", help="Offer/CTA")
    parser.add_argument("--audience", "-a", help="Target audience")
    parser.add_argument("--output", choices=["json", "text"], default="text")

    args = parser.parse_args()

    if args.platform == "linkedin_sponsored":
        result = generate_linkedin_sponsored(args.product, args.offer, args.audience)
    elif args.platform == "google_search":
        result = generate_google_search(args.product, args.offer, args.audience)
    elif args.platform == "linkedin_text":
        result = generate_linkedin_text(args.product, args.offer, args.audience)
    else:
        result = generate_linkedin_sponsored(args.product, args.offer, args.audience)

    if args.output == "json":
        print(json.dumps(result, indent=2))
    else:
        print(f"\n{'='*60}")
        print(f"AD COPY: {result['platform']}")
        print(f"Product: {args.product} | Offer: {args.offer}")
        print(f"{'='*60}\n")

        if "variants" in result:
            for v in result["variants"]:
                status = "OK" if v.get("within_limits", True) else "OVER LIMIT"
                print(f"--- Variant {v['variant']} [{status}] ---")
                print(f"Headline ({v.get('headline_chars', 0)} chars): {v['headline']}")
                print(f"Description ({v.get('description_chars', 0)} chars): {v['description']}")
                if "cta" in v:
                    print(f"CTA: {v['cta']}")
                print()

        if "headlines" in result:
            print("--- Headlines ---")
            for i, h in enumerate(result["headlines"], 1):
                status = "OK" if h["within_limit"] else "OVER"
                print(f"  {i}. [{h['chars']}/{result['specs']['headline_max']}] {h['text']}")

            print("\n--- Descriptions ---")
            for i, d in enumerate(result["descriptions"], 1):
                status = "OK" if d["within_limit"] else "OVER"
                print(f"  {i}. [{d['chars']}/{result['specs']['description_max']}] {d['text']}")

        print(f"\n--- Platform Specs ---")
        for key, value in result["specs"].items():
            if key != "name":
                print(f"  {key}: {value}")
        print()


if __name__ == "__main__":
    main()
