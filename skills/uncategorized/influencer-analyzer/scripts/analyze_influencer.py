#!/usr/bin/env python3
"""
Influencer Analyzer - Track and analyze cardiology content creators.

Discovers content patterns, topics, engagement, and gap opportunities
for your Hinglish content strategy.

Usage:
    python analyze_influencer.py --name "Eric Topol" --platform twitter
    python analyze_influencer.py --compare "Topol,Attia,York Cardiology"
    python analyze_influencer.py --gaps --domain "Cardiology"
    python analyze_influencer.py --topic "GLP-1" --influencers "Topol,Attia"
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.markdown import Markdown
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    print("Note: Install 'rich' for better output formatting: pip install rich")

try:
    from anthropic import Anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    print("Error: anthropic package required. Install with: pip install anthropic")
    sys.exit(1)

from dotenv import load_dotenv

# Load environment variables
env_path = Path(__file__).parent.parent.parent.parent.parent / ".env"
if env_path.exists():
    load_dotenv(env_path)

# Pre-configured influencers
INFLUENCERS = {
    "eric topol": {
        "name": "Eric Topol",
        "handle": "@EricTopol",
        "platforms": ["twitter", "substack"],
        "focus": ["clinical trials", "digital health", "AI in medicine", "COVID"],
        "style": "Expert commentary with primary sources",
        "url_patterns": [
            "twitter.com/EricTopol",
            "erictopol.substack.com",
            "ground truths substack"
        ],
        "track_for": "voice_model"
    },
    "topol": {
        "alias": "eric topol"
    },
    "peter attia": {
        "name": "Peter Attia",
        "handle": "peterattiamd",
        "platforms": ["podcast", "youtube", "newsletter"],
        "focus": ["longevity", "metabolic health", "CVD prevention", "exercise"],
        "style": "Deep-dive, data-driven, long-form",
        "url_patterns": [
            "peterattiamd.com",
            "youtube.com/c/peterattiamd",
            "the drive podcast"
        ],
        "track_for": "format_inspiration"
    },
    "attia": {
        "alias": "peter attia"
    },
    "york cardiology": {
        "name": "York Cardiology (Dr. Sanjay Gupta)",
        "handle": "@YorkCardiology",
        "platforms": ["youtube"],
        "focus": ["ECG teaching", "patient education", "clinical cases", "palpitations"],
        "style": "Clear, patient-friendly explanations",
        "url_patterns": [
            "youtube.com/yorkcardiology",
            "yorkcardiology.co.uk"
        ],
        "track_for": "competitor"
    },
    "dr navin agrawal": {
        "name": "Dr Navin Agrawal",
        "handle": None,
        "platforms": ["youtube"],
        "focus": ["patient education", "Hindi content", "heart disease basics"],
        "style": "Simple Hindi explanations",
        "url_patterns": [
            "youtube.com Dr Navin Agrawal cardiology"
        ],
        "track_for": "competitor"
    },
    "saaol": {
        "name": "SAAOL Heart Center",
        "handle": None,
        "platforms": ["youtube"],
        "focus": ["alternative medicine claims", "anti-surgery stance"],
        "style": "Marketing-heavy, controversial claims",
        "url_patterns": [
            "saaol youtube"
        ],
        "track_for": "anti_pattern",
        "warning": "MISINFORMATION SOURCE - Track to counter, not emulate"
    }
}


class InfluencerAnalyzer:
    """Analyze cardiology influencers and find content gaps."""

    def __init__(self):
        self.console = Console() if RICH_AVAILABLE else None
        self.client = None
        self._init_client()

    def _init_client(self):
        """Initialize Anthropic client."""
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            self._print_error("ANTHROPIC_API_KEY not found in environment")
            sys.exit(1)
        self.client = Anthropic(api_key=api_key)

    def _print(self, message: str, style: str = None):
        """Print with optional rich formatting."""
        if RICH_AVAILABLE and self.console:
            self.console.print(message, style=style)
        else:
            print(message)

    def _print_error(self, message: str):
        """Print error message."""
        self._print(f"[ERROR] {message}", "red bold")

    def _print_panel(self, content: str, title: str):
        """Print content in a panel."""
        if RICH_AVAILABLE and self.console:
            self.console.print(Panel(Markdown(content), title=title))
        else:
            print(f"\n{'='*60}")
            print(f"  {title}")
            print('='*60)
            print(content)
            print('='*60 + "\n")

    def get_influencer_info(self, name: str) -> Optional[dict]:
        """Get pre-configured influencer information."""
        name_lower = name.lower().strip()

        # Check for direct match or alias
        if name_lower in INFLUENCERS:
            info = INFLUENCERS[name_lower]
            if "alias" in info:
                return INFLUENCERS[info["alias"]]
            return info

        # Partial match
        for key, info in INFLUENCERS.items():
            if name_lower in key or key in name_lower:
                if "alias" in info:
                    return INFLUENCERS[info["alias"]]
                return info

        return None

    def analyze_influencer(self, name: str, platform: str = None) -> str:
        """Analyze a single influencer's content strategy."""

        info = self.get_influencer_info(name)

        # Build context about the influencer
        if info:
            context = f"""
Known Information about {info['name']}:
- Platforms: {', '.join(info['platforms'])}
- Focus areas: {', '.join(info['focus'])}
- Style: {info['style']}
- Search patterns: {', '.join(info['url_patterns'])}
"""
            if info.get('warning'):
                context += f"- WARNING: {info['warning']}\n"
        else:
            context = f"Unknown influencer: {name}. Perform general research."

        platform_focus = f" specifically on {platform}" if platform else ""

        prompt = f"""You are analyzing cardiology content creators for Dr. Shailesh Singh,
an interventional cardiologist building thought leadership through Hinglish content.

{context}

TASK: Analyze {name}'s content strategy{platform_focus}.

Provide analysis covering:

## 1. RECENT CONTENT FOCUS (Last 30 days estimate)
- What topics are they covering?
- What percentage breakdown by topic?
- Any trending topics they're riding?

## 2. CONTENT PATTERNS
- Posting frequency
- Content formats (threads, videos, articles, etc.)
- Engagement patterns (what gets most interaction?)

## 3. STYLE ANALYSIS
- How do they communicate?
- What makes their content distinctive?
- How do they cite sources?

## 4. GAPS FOR DR. SINGH
Based on this analysis, identify opportunities:
- Topics they DON'T cover that Dr. Singh could
- Angles unique to Indian/Hinglish audience
- How Dr. Singh can differentiate

## 5. ACTIONABLE RECOMMENDATIONS
- Specific content ideas inspired by (not copying) this influencer
- Format experiments to try
- Topics to "translate" for Indian audience

Be specific and actionable. Focus on differentiation, not imitation.
"""

        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text

    def compare_influencers(self, names: list) -> str:
        """Compare multiple influencers."""

        # Gather info on all influencers
        influencer_contexts = []
        for name in names:
            info = self.get_influencer_info(name)
            if info:
                influencer_contexts.append(f"""
**{info['name']}**
- Platforms: {', '.join(info['platforms'])}
- Focus: {', '.join(info['focus'])}
- Style: {info['style']}
""")
            else:
                influencer_contexts.append(f"**{name}** - Unknown, research needed")

        context = "\n".join(influencer_contexts)

        prompt = f"""You are comparing cardiology content creators for Dr. Shailesh Singh,
an interventional cardiologist building thought leadership through Hinglish content.

INFLUENCERS TO COMPARE:
{context}

TASK: Create a comprehensive comparison.

## COMPARISON TABLE
Create a markdown table comparing:
| Aspect | {' | '.join(names)} | Dr. Singh Opportunity |
|--------|{'|'.join(['---' for _ in names])}|---|

Include rows for:
- Primary platform
- Content format
- Posting frequency
- Target audience
- Unique angle
- Main topics
- Engagement style

## GAP ANALYSIS
What topics/angles are NONE of them covering that Dr. Singh could own?

## DIFFERENTIATION STRATEGY
How can Dr. Singh stand out from all of these?

## PRIORITY TOPICS
Based on gaps, what should Dr. Singh cover first?

Be specific and actionable.
"""

        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2500,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text

    def find_content_gaps(self, domain: str = "Cardiology") -> str:
        """Find content gaps in the cardiology space."""

        prompt = f"""You are a content strategist for Dr. Shailesh Singh,
an interventional cardiologist in India building thought leadership through Hinglish YouTube content.

DOMAIN: {domain}

TASK: Identify content gaps in cardiology content creation.

Consider these dimensions:

## 1. LANGUAGE GAP
- What content exists only in English that needs Hinglish versions?
- What Indian-specific topics are underserved?

## 2. DEPTH GAP
- What topics have only surface-level coverage?
- Where is expert-level content missing?

## 3. FORMAT GAP
- What content formats are underutilized in cardiology?
- What works elsewhere but isn't used in cardiology?

## 4. AUDIENCE GAP
- What patient segments are underserved?
- What doctor segments lack content?

## 5. TOPIC GAP
Consider underserved topics:
- Rheumatic heart disease (common in India, rare in US content)
- Tropical cardiology
- Cost-conscious cardiology
- Family-centered care (Indian context)
- Vegetarian heart-healthy diets
- Yoga and heart health (evidence-based)

## 6. TIMING GAP
- What's trending that lacks quality coverage?
- What new trials need Indian context interpretation?

## PRIORITY RECOMMENDATIONS
Top 10 content ideas that fill these gaps, ranked by:
1. Audience need
2. Competition level (lower = better)
3. Dr. Singh's expertise fit
4. Viral potential

For each idea, provide:
- Topic
- Format
- Unique angle
- Why now

Be specific and actionable.
"""

        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=3000,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text

    def analyze_topic(self, topic: str, influencers: list = None) -> str:
        """Analyze how a specific topic is being covered."""

        if influencers:
            influencer_context = f"Focus on how these influencers cover it: {', '.join(influencers)}"
        else:
            influencer_context = "Consider coverage across the cardiology content space."

        prompt = f"""You are analyzing topic coverage for Dr. Shailesh Singh,
an interventional cardiologist building thought leadership through Hinglish content.

TOPIC: {topic}
{influencer_context}

TASK: Analyze how this topic is being covered and identify opportunities.

## 1. CURRENT COVERAGE
- Who is covering this topic?
- What angles are they taking?
- What's the quality level?

## 2. CONTENT AUDIT
- What's been said well?
- What's been said poorly or incorrectly?
- What hasn't been said at all?

## 3. INDIAN CONTEXT
- How does this topic apply to Indian patients specifically?
- What cultural/economic considerations matter?
- What local data exists?

## 4. OPPORTUNITY ASSESSMENT
- Is there room for more content on this topic?
- What unique angle can Dr. Singh take?
- What format would work best?

## 5. CONTENT BRIEF
If Dr. Singh were to create content on this topic:
- Recommended title (Hinglish)
- Key points to cover
- Unique angle
- Sources to cite
- Format recommendation

Be specific and actionable.
"""

        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text


def main():
    parser = argparse.ArgumentParser(
        description="Analyze cardiology influencers and find content gaps"
    )

    parser.add_argument(
        "--name", "-n",
        type=str,
        help="Influencer name to analyze (e.g., 'Eric Topol', 'Peter Attia')"
    )

    parser.add_argument(
        "--platform", "-p",
        type=str,
        choices=["twitter", "youtube", "substack", "podcast", "all"],
        default="all",
        help="Platform to focus on"
    )

    parser.add_argument(
        "--compare", "-c",
        type=str,
        help="Comma-separated list of influencers to compare"
    )

    parser.add_argument(
        "--gaps", "-g",
        action="store_true",
        help="Find content gaps in the cardiology space"
    )

    parser.add_argument(
        "--domain", "-d",
        type=str,
        default="Cardiology",
        help="Domain for gap analysis"
    )

    parser.add_argument(
        "--topic", "-t",
        type=str,
        help="Analyze coverage of a specific topic"
    )

    parser.add_argument(
        "--influencers", "-i",
        type=str,
        help="Comma-separated list of influencers for topic analysis"
    )

    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="List pre-configured influencers"
    )

    parser.add_argument(
        "--output", "-o",
        type=str,
        help="Output directory for reports"
    )

    args = parser.parse_args()

    analyzer = InfluencerAnalyzer()

    # List influencers
    if args.list:
        print("\nPre-configured Influencers:")
        print("=" * 60)
        for key, info in INFLUENCERS.items():
            if "alias" not in info:
                warning = f" [WARNING: {info.get('warning', '')}]" if info.get('warning') else ""
                print(f"\n{info['name']}{warning}")
                print(f"  Platforms: {', '.join(info['platforms'])}")
                print(f"  Focus: {', '.join(info['focus'])}")
                print(f"  Track for: {info['track_for']}")
        return

    result = None
    title = "Analysis"

    # Run appropriate analysis
    if args.name:
        title = f"Influencer Analysis: {args.name}"
        platform = args.platform if args.platform != "all" else None
        result = analyzer.analyze_influencer(args.name, platform)

    elif args.compare:
        names = [n.strip() for n in args.compare.split(",")]
        title = f"Comparison: {', '.join(names)}"
        result = analyzer.compare_influencers(names)

    elif args.gaps:
        title = f"Content Gaps: {args.domain}"
        result = analyzer.find_content_gaps(args.domain)

    elif args.topic:
        influencers = None
        if args.influencers:
            influencers = [n.strip() for n in args.influencers.split(",")]
        title = f"Topic Analysis: {args.topic}"
        result = analyzer.analyze_topic(args.topic, influencers)

    else:
        parser.print_help()
        return

    # Output result
    if result:
        analyzer._print_panel(result, title)

        # Save to file if output directory specified
        if args.output:
            output_dir = Path(args.output)
            output_dir.mkdir(parents=True, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"influencer_analysis_{timestamp}.md"
            output_path = output_dir / filename

            with open(output_path, "w") as f:
                f.write(f"# {title}\n\n")
                f.write(f"Generated: {datetime.now().isoformat()}\n\n")
                f.write("---\n\n")
                f.write(result)

            print(f"\nSaved to: {output_path}")


if __name__ == "__main__":
    main()
