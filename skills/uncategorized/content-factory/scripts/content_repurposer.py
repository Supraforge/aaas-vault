#!/usr/bin/env python3
"""
Content Repurposer - Transform one piece of content into multiple formats.
"""

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List

OUTPUT_FORMATS = {
    "linkedin": {
        "name": "LinkedIn Post",
        "max_chars": 1300,
        "description": "Professional thought leadership post"
    },
    "twitter": {
        "name": "Twitter/X Thread",
        "tweet_max": 280,
        "thread_size": 10,
        "description": "10-tweet thread with hooks"
    },
    "email": {
        "name": "Email Newsletter",
        "description": "Newsletter snippet with teaser"
    },
    "carousel": {
        "name": "Carousel Outline",
        "slides": 8,
        "description": "8-10 slide carousel structure"
    },
    "video": {
        "name": "Video Script",
        "duration": "60-90 seconds",
        "description": "Short-form video script"
    }
}


def extract_key_points(content: str) -> List[str]:
    """Extract key points from content."""
    # Find sentences with key markers
    key_markers = ["important", "key", "critical", "essential", "must", "should", "need"]

    sentences = re.split(r'[.!?]+', content)
    key_points = []

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence or len(sentence) < 20:
            continue

        # Check for key markers
        if any(marker in sentence.lower() for marker in key_markers):
            key_points.append(sentence)

        # Check for statistics
        if re.search(r'\d+%|\d+ [a-z]+', sentence):
            key_points.append(sentence)

    # If not enough key points, use first sentences of paragraphs
    if len(key_points) < 5:
        paragraphs = content.split('\n\n')
        for p in paragraphs:
            first_sentence = re.split(r'[.!?]', p)[0].strip()
            if first_sentence and len(first_sentence) > 20:
                key_points.append(first_sentence)

    return key_points[:10]


def generate_linkedin_post(content: str, key_points: List[str]) -> str:
    """Generate LinkedIn post from content."""
    # Extract hook (first compelling point)
    hook = key_points[0] if key_points else "Here's something most people don't realize..."

    # Build post
    post = f"""{hook}

Here's what I've learned:

"""

    # Add 3-4 key points
    for i, point in enumerate(key_points[1:5], 1):
        post += f"- {point}\n"

    post += """
The bottom line: Real-time visibility beats periodic audits every time.

What's your experience? Drop a comment below.

#AI #QualityEngineering #Compliance"""

    return post[:1300]


def generate_twitter_thread(content: str, key_points: List[str]) -> List[str]:
    """Generate Twitter thread from content."""
    tweets = []

    # Tweet 1: Hook
    hook = key_points[0] if key_points else "Thread time. Here's what most people miss:"
    tweets.append(f"{hook[:250]}\n\n(Thread 1/{min(10, len(key_points) + 2)})")

    # Middle tweets: Key points
    for i, point in enumerate(key_points[1:8], 2):
        tweet = f"{point[:250]}\n\n({i}/{min(10, len(key_points) + 2)})"
        tweets.append(tweet)

    # Final tweet: CTA
    final = f"""TL;DR:
- 40% of engineering time wasted on compliance
- Real-time visibility solves this
- No tool replacement needed

If this resonated, follow for more insights on engineering quality.

({len(tweets) + 1}/{len(tweets) + 1})"""

    tweets.append(final)

    return tweets[:10]


def generate_email_snippet(content: str, key_points: List[str]) -> str:
    """Generate email newsletter snippet."""
    teaser = key_points[0][:100] if key_points else "This week's insight on engineering quality..."

    snippet = f"""**This Week's Insight**

{teaser}...

Here's the key takeaway:

{key_points[1] if len(key_points) > 1 else "Quality engineering doesn't have to mean more overhead."}

**Why This Matters**

{key_points[2] if len(key_points) > 2 else "Teams that adopt continuous compliance see 40% productivity gains."}

[Read the full article →](link)

---

*Forwarded this? Subscribe here to get insights like this weekly.*"""

    return snippet


def generate_carousel_outline(content: str, key_points: List[str]) -> List[Dict]:
    """Generate carousel slide outline."""
    slides = [
        {"slide": 1, "type": "cover", "content": key_points[0] if key_points else "The Hidden Cost of Compliance", "notes": "Bold hook, brand colors"},
        {"slide": 2, "type": "problem", "content": "The Problem: 40% of engineering time lost to compliance overhead", "notes": "Statistics, visual impact"},
        {"slide": 3, "type": "context", "content": "Why This Happens: Fragmented tools, periodic audits, late visibility", "notes": "3 bullet points"},
    ]

    # Add content slides
    for i, point in enumerate(key_points[1:4], 4):
        slides.append({
            "slide": i,
            "type": "insight",
            "content": point[:100],
            "notes": "One key point per slide"
        })

    # Add solution and CTA
    slides.extend([
        {"slide": len(slides) + 1, "type": "solution", "content": "The Better Way: Continuous visibility, automated traceability", "notes": "Show transformation"},
        {"slide": len(slides) + 2, "type": "proof", "content": "Results: 3 months → 2 days audit prep", "notes": "Social proof, metrics"},
        {"slide": len(slides) + 3, "type": "cta", "content": "Get Your Free Risk Baseline", "notes": "Clear CTA, link in comments"}
    ])

    return slides[:10]


def generate_video_script(content: str, key_points: List[str]) -> str:
    """Generate 60-90 second video script."""
    script = f"""# Video Script (60-90 seconds)

## HOOK (0-10 sec)
[On camera, energetic]
"{key_points[0] if key_points else 'Here is something that might surprise you...'}"

## PROBLEM (10-25 sec)
[B-roll of busy office/code]
"Most engineering teams spend 40% of their time on compliance activities.
That's nearly half their capacity - diverted from actual innovation."

## INSIGHT (25-45 sec)
[Graphics/animations]
"The real issue isn't compliance itself - it's the lack of visibility.
Teams don't know their status until audit prep begins.
By then, it's too late to fix efficiently."

## SOLUTION (45-65 sec)
[Product demo or visualization]
"What if compliance happened as a by-product of your existing workflow?
Real-time visibility. Continuous traceability. No tool replacement.
That's the approach we've built."

## CTA (65-75 sec)
[On camera, direct]
"Want to see where you stand? Link in bio for a free risk baseline.
Takes 90 minutes, zero commitment."

---

**Visual Notes:**
- Use brand colors (gold accent, dark background)
- Include text overlays for key stats
- Fast cuts during problem section
- Slow down for solution reveal

**Audio Notes:**
- Background music: Subtle, professional
- Clear voiceover throughout
- Sound effects on stat reveals"""

    return script


def repurpose_content(source_path: str, formats: List[str] = None) -> Dict:
    """Repurpose content into multiple formats."""
    # Read source content
    path = Path(source_path)
    if not path.exists():
        raise FileNotFoundError(f"Source file not found: {source_path}")

    with open(path) as f:
        content = f.read()

    # Extract key points
    key_points = extract_key_points(content)

    # Default to all formats
    if not formats:
        formats = list(OUTPUT_FORMATS.keys())

    results = {
        "source": source_path,
        "key_points_extracted": len(key_points),
        "formats": {}
    }

    for fmt in formats:
        if fmt == "linkedin":
            results["formats"]["linkedin"] = {
                "name": OUTPUT_FORMATS["linkedin"]["name"],
                "content": generate_linkedin_post(content, key_points),
                "chars": len(generate_linkedin_post(content, key_points))
            }
        elif fmt == "twitter":
            thread = generate_twitter_thread(content, key_points)
            results["formats"]["twitter"] = {
                "name": OUTPUT_FORMATS["twitter"]["name"],
                "tweets": thread,
                "thread_size": len(thread)
            }
        elif fmt == "email":
            results["formats"]["email"] = {
                "name": OUTPUT_FORMATS["email"]["name"],
                "content": generate_email_snippet(content, key_points)
            }
        elif fmt == "carousel":
            results["formats"]["carousel"] = {
                "name": OUTPUT_FORMATS["carousel"]["name"],
                "slides": generate_carousel_outline(content, key_points)
            }
        elif fmt == "video":
            results["formats"]["video"] = {
                "name": OUTPUT_FORMATS["video"]["name"],
                "script": generate_video_script(content, key_points)
            }

    return results


def main():
    parser = argparse.ArgumentParser(description="Repurpose content into multiple formats")
    parser.add_argument("--source", "-s", required=True, help="Source content file")
    parser.add_argument("--formats", "-f", help="Comma-separated formats (linkedin,twitter,email,carousel,video)")
    parser.add_argument("--output", "-o", choices=["json", "text"], default="text")

    args = parser.parse_args()

    formats = args.formats.split(",") if args.formats else None

    try:
        results = repurpose_content(args.source, formats)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    if args.output == "json":
        print(json.dumps(results, indent=2))
    else:
        print(f"\n{'='*60}")
        print(f"CONTENT REPURPOSER")
        print(f"Source: {results['source']}")
        print(f"Key Points Extracted: {results['key_points_extracted']}")
        print(f"{'='*60}\n")

        for fmt, data in results["formats"].items():
            print(f"\n{'='*60}")
            print(f"FORMAT: {data['name']}")
            print(f"{'='*60}\n")

            if fmt == "linkedin":
                print(data["content"])
                print(f"\n[{data['chars']} characters]")

            elif fmt == "twitter":
                for i, tweet in enumerate(data["tweets"], 1):
                    print(f"Tweet {i}:")
                    print(tweet)
                    print()

            elif fmt == "email":
                print(data["content"])

            elif fmt == "carousel":
                for slide in data["slides"]:
                    print(f"Slide {slide['slide']} [{slide['type']}]: {slide['content']}")

            elif fmt == "video":
                print(data["script"])

            print()


if __name__ == "__main__":
    main()
