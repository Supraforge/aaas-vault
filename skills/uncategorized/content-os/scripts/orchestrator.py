#!/usr/bin/env python3
"""
Content OS Orchestrator - Produce all content types from one idea.

This orchestrator chains together existing skills to create a complete
content package from a single topic or seed idea.

Usage:
    python orchestrator.py "Statin myths for Indians"
    python orchestrator.py "GLP-1 cardiovascular benefits" --skip newsletter
    python orchestrator.py --backward content.md  # Split long-form into short-form

The orchestrator does NOT re-implement skills. It coordinates:
- PubMed client for research
- Carousel generator for visuals
- Quality checker for review
- And produces output files that Claude/user can complete
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field

# Add parent paths for imports
SCRIPT_DIR = Path(__file__).parent
SKILL_DIR = SCRIPT_DIR.parent
SKILLS_ROOT = SKILL_DIR.parent
PROJECT_ROOT = SKILLS_ROOT.parent.parent

sys.path.insert(0, str(PROJECT_ROOT / "scripts"))
sys.path.insert(0, str(SKILLS_ROOT / "carousel-generator-v2" / "scripts"))
sys.path.insert(0, str(SKILLS_ROOT / "parallel-literature-search" / "scripts"))
sys.path.insert(0, str(SKILLS_ROOT / "quick-topic-researcher" / "scripts"))

# Try to import available modules
try:
    from pubmed_client import PubMedClient
    PUBMED_AVAILABLE = True
except ImportError:
    PUBMED_AVAILABLE = False

try:
    from carousel_generator import CarouselGenerator, CarouselConfig
    from models import AspectRatio
    CAROUSEL_AVAILABLE = True
except ImportError:
    CAROUSEL_AVAILABLE = False

try:
    from research_integration import ResearchIntegration
    RESEARCH_AVAILABLE = True
except ImportError:
    RESEARCH_AVAILABLE = False

try:
    from scientific_skills_bridge import ScientificSkillsBridge
    SCIENTIFIC_SKILLS_AVAILABLE = True
except ImportError:
    SCIENTIFIC_SKILLS_AVAILABLE = False


@dataclass
class ContentPackage:
    """Container for all generated content."""
    topic: str
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    output_dir: Optional[Path] = None

    # Research
    research_brief: Optional[str] = None
    pubmed_articles: List[Dict] = field(default_factory=list)

    # Long-form (templates/outlines for Claude to complete)
    youtube_script_outline: Optional[str] = None
    newsletter_b2c_outline: Optional[str] = None
    newsletter_b2b_outline: Optional[str] = None
    editorial_outline: Optional[str] = None
    blog_outline: Optional[str] = None

    # Short-form
    tweets: List[str] = field(default_factory=list)
    thread: Optional[str] = None
    carousel_content: Optional[str] = None

    # Visual
    carousel_path: Optional[Path] = None

    # Status
    phases_completed: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)


class ContentOSOrchestrator:
    """Orchestrates content production across multiple skills."""

    def __init__(self, output_dir: Optional[Path] = None):
        self.output_dir = output_dir or (PROJECT_ROOT / "output" / "content-os")
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def _print(self, msg: str, style: str = None):
        """Print with optional styling."""
        if style == "header":
            print(f"\n{'='*60}")
            print(f"  {msg}")
            print(f"{'='*60}")
        elif style == "phase":
            print(f"\n▶ {msg}")
            print("-" * 40)
        elif style == "success":
            print(f"  ✓ {msg}")
        elif style == "warning":
            print(f"  ⚠️  {msg}")
        elif style == "error":
            print(f"  ✗ {msg}")
        else:
            print(f"  {msg}")

    def run_forward(self, topic: str, skip: List[str] = None) -> ContentPackage:
        """
        Forward mode: Topic → All content types.

        Args:
            topic: The content topic/idea
            skip: List of phases to skip (research, long-form, short-form, visual)

        Returns:
            ContentPackage with all generated content
        """
        skip = skip or []
        package = ContentPackage(topic=topic)

        # Create topic-specific output directory
        safe_topic = "".join(c if c.isalnum() or c in (' ', '-') else '_' for c in topic)
        safe_topic = safe_topic.replace(' ', '-')[:40]
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        package.output_dir = self.output_dir / f"{safe_topic}-{timestamp}"
        package.output_dir.mkdir(parents=True, exist_ok=True)

        self._print(f"CONTENT OS: {topic}", "header")
        self._print(f"Output: {package.output_dir}")

        # Phase 1: Research
        if "research" not in skip:
            self._run_research_phase(package)
        else:
            self._print("Skipping research phase", "warning")

        # Phase 2: Long-form outlines
        if "long-form" not in skip:
            self._run_longform_phase(package)
        else:
            self._print("Skipping long-form phase", "warning")

        # Phase 3: Short-form content
        if "short-form" not in skip:
            self._run_shortform_phase(package)
        else:
            self._print("Skipping short-form phase", "warning")

        # Phase 4: Visual content
        if "visual" not in skip:
            self._run_visual_phase(package)
        else:
            self._print("Skipping visual phase", "warning")

        # Save package manifest
        self._save_manifest(package)

        self._print("CONTENT PACKAGE COMPLETE", "header")
        self._print(f"Phases completed: {', '.join(package.phases_completed)}")
        if package.errors:
            self._print(f"Errors: {len(package.errors)}")

        return package

    def _run_research_phase(self, package: ContentPackage):
        """Phase 1: Research using PubMed."""
        self._print("PHASE 1: RESEARCH", "phase")

        if not PUBMED_AVAILABLE:
            self._print("PubMed client not available", "warning")
            package.errors.append("PubMed client not available")
            return

        try:
            client = PubMedClient()

            # Search for relevant articles
            self._print("Searching PubMed...")
            articles = client.search_and_fetch(
                query=f"{package.topic} randomized controlled trial OR meta-analysis",
                max_results=10,
                sort="relevance"
            )

            if articles:
                self._print(f"Found {len(articles)} articles", "success")

                # Format articles for research brief
                brief_parts = [f"# Research Brief: {package.topic}\n"]
                brief_parts.append(f"Generated: {datetime.now().isoformat()}\n")
                brief_parts.append(f"Source: PubMed NCBI E-utilities\n\n")
                brief_parts.append("## Key Articles\n\n")

                for i, article in enumerate(articles[:5], 1):
                    brief_parts.append(f"### {i}. {article.title}\n")
                    brief_parts.append(f"- **PMID**: {article.pmid}\n")
                    brief_parts.append(f"- **Journal**: {article.journal}\n")
                    brief_parts.append(f"- **Date**: {article.pub_date or 'N/A'}\n")
                    if article.abstract:
                        brief_parts.append(f"- **Abstract**: {article.abstract[:500]}...\n")
                    brief_parts.append("\n")

                    package.pubmed_articles.append({
                        "pmid": article.pmid,
                        "title": article.title,
                        "journal": article.journal,
                        "date": article.pub_date
                    })

                package.research_brief = "".join(brief_parts)

                # Save research brief
                brief_path = package.output_dir / "research-brief.md"
                with open(brief_path, "w") as f:
                    f.write(package.research_brief)
                self._print(f"Saved: {brief_path.name}", "success")

            else:
                self._print("No articles found", "warning")

            package.phases_completed.append("research")

        except Exception as e:
            self._print(f"Research failed: {e}", "error")
            package.errors.append(f"Research: {e}")

    def _run_longform_phase(self, package: ContentPackage):
        """Phase 2: Generate long-form content outlines."""
        self._print("PHASE 2: LONG-FORM OUTLINES", "phase")

        # Generate outlines for each content type
        # These are templates that Claude can complete

        content_types = {
            "youtube-script": self._generate_youtube_outline,
            "newsletter-b2c": self._generate_newsletter_b2c_outline,
            "newsletter-b2b": self._generate_newsletter_b2b_outline,
            "editorial": self._generate_editorial_outline,
            "blog": self._generate_blog_outline
        }

        for name, generator in content_types.items():
            try:
                outline = generator(package)
                if outline:
                    # Save outline
                    filename = f"{name}-outline.md"
                    path = package.output_dir / "long-form" / filename
                    path.parent.mkdir(parents=True, exist_ok=True)
                    with open(path, "w") as f:
                        f.write(outline)
                    self._print(f"Created: {filename}", "success")
            except Exception as e:
                self._print(f"{name} failed: {e}", "error")
                package.errors.append(f"{name}: {e}")

        package.phases_completed.append("long-form")

    def _generate_youtube_outline(self, package: ContentPackage) -> str:
        """Generate YouTube script outline (Hinglish)."""
        pmids = ", ".join([a["pmid"] for a in package.pubmed_articles[:3]])

        return f"""# YouTube Script Outline: {package.topic}

## Format
- Language: Hinglish (70% Hindi, 30% English)
- Style: Peter Attia-inspired (deep but accessible)
- Duration: 15-20 minutes

## Key Sources (from PubMed)
{pmids if pmids else "[Research pending]"}

## Structure

### HOOK (0:00-0:30)
- Provocative question or myth
- Why viewers should care
- Preview of what they'll learn

### CONTEXT (0:30-2:00)
- Brief background on {package.topic}
- Why this matters for Indian audience
- Common misconceptions to address

### MAIN CONTENT (2:00-15:00)

#### Point 1: [Key insight]
- Data: [Cite PMID]
- Relatable example
- Practical takeaway

#### Point 2: [Key insight]
- Data: [Cite PMID]
- Relatable example
- Practical takeaway

#### Point 3: [Key insight]
- Data: [Cite PMID]
- Relatable example
- Practical takeaway

### SUMMARY (15:00-17:00)
- Recap key points
- Action items for viewers
- CTA for next video/subscribe

## Claude: Complete this outline
Use the research brief and your medical knowledge to fill in the specific content.
Apply the youtube-script-master skill for final script.
"""

    def _generate_newsletter_b2c_outline(self, package: ContentPackage) -> str:
        """Generate B2C newsletter outline (patient-focused)."""
        return f"""# Newsletter (B2C): {package.topic}

## Target Audience
Patients and health-conscious individuals in India

## Tone
Eric Topol / Ground Truths style - authoritative but accessible

## Structure

### Subject Line Options
1. [Curiosity-driven option]
2. [Benefit-driven option]
3. [News-driven option]

### Opening Hook
[Personal anecdote or patient story related to {package.topic}]

### The Problem
What most people get wrong about {package.topic}

### The Evidence
Key findings from research (cite PMIDs)

### What This Means For You
Practical implications for patients

### Action Items
1. [Specific action]
2. [Specific action]
3. [Specific action]

### Closing
Personal note + upcoming content preview

## Claude: Complete using cardiology-newsletter-writer skill
Apply quality pipeline before finalizing.
"""

    def _generate_newsletter_b2b_outline(self, package: ContentPackage) -> str:
        """Generate B2B newsletter outline (doctor-focused)."""
        return f"""# Newsletter (B2B): {package.topic}

## Target Audience
Physicians, cardiologists, medical professionals

## Tone
JACC editorial style - clinical, evidence-focused

## Structure

### Clinical Context
Current landscape of {package.topic} in practice

### New Evidence Summary
Recent trials and guidelines

### Practice Implications
- What to change
- What to continue
- What to monitor

### Guidelines Update
ACC/ESC/ADA recommendations

### Key References
[PMIDs with brief annotations]

## Claude: Complete using medical-newsletter-writer skill
Apply rigorous citation standards.
"""

    def _generate_editorial_outline(self, package: ContentPackage) -> str:
        """Generate editorial outline."""
        return f"""# Editorial: {package.topic}

## Style
Eric Topol editorials from Lancet/NEJM

## Opening
[Bold thesis statement about {package.topic}]

## The Evidence Base
Recent landmark trials

## Critical Analysis
- What works
- What's still unknown
- Limitations of current evidence

## Clinical Implications
Impact on practice

## Future Directions
What research is needed

## Conclusion
Clear position with nuance

## Claude: Complete using cardiology-editorial skill
"""

    def _generate_blog_outline(self, package: ContentPackage) -> str:
        """Generate blog post outline."""
        return f"""# Blog Post: {package.topic}

## SEO Considerations
- Primary keyword: {package.topic}
- Secondary keywords: [derive from research]

## Structure

### Title Options
1. [Question format]
2. [List format]
3. [Statement format]

### Introduction
Hook + thesis + preview

### Main Content
H2/H3 structure with key points

### Conclusion
Summary + CTA

### Meta Description
150-160 characters summarizing value

## Claude: Complete using cardiology-writer skill
"""

    def _run_shortform_phase(self, package: ContentPackage):
        """Phase 3: Generate short-form content."""
        self._print("PHASE 3: SHORT-FORM CONTENT", "phase")

        try:
            # Generate tweet ideas
            tweets = self._generate_tweet_ideas(package)
            package.tweets = tweets

            # Save tweets
            tweets_path = package.output_dir / "short-form" / "tweets.md"
            tweets_path.parent.mkdir(parents=True, exist_ok=True)
            with open(tweets_path, "w") as f:
                f.write(f"# Tweet Ideas: {package.topic}\n\n")
                for i, tweet in enumerate(tweets, 1):
                    f.write(f"## Tweet {i}\n{tweet}\n\n")
            self._print(f"Created: {len(tweets)} tweet ideas", "success")

            # Generate thread outline
            thread = self._generate_thread_outline(package)
            package.thread = thread

            thread_path = package.output_dir / "short-form" / "thread.md"
            with open(thread_path, "w") as f:
                f.write(thread)
            self._print("Created: thread outline", "success")

            # Generate carousel content
            carousel_content = self._generate_carousel_content(package)
            package.carousel_content = carousel_content

            carousel_path = package.output_dir / "short-form" / "carousel-content.md"
            with open(carousel_path, "w") as f:
                f.write(carousel_content)
            self._print("Created: carousel content", "success")

            package.phases_completed.append("short-form")

        except Exception as e:
            self._print(f"Short-form failed: {e}", "error")
            package.errors.append(f"Short-form: {e}")

    def _generate_tweet_ideas(self, package: ContentPackage) -> List[str]:
        """Generate tweet ideas from topic and research."""
        ideas = [
            f"🧵 Thread: What you need to know about {package.topic}",
            f"Myth: [Common misconception about {package.topic}]\n\nReality: [Evidence-based truth]\n\n(PMID: [cite research])",
            f"📊 Key stat about {package.topic}:\n\n[X]% [outcome]\n\nThis matters because: [implication]\n\nSource: [journal]",
            f"Why your doctor talks about {package.topic}:\n\n1. [reason]\n2. [reason]\n3. [reason]\n\nThe evidence is clear. 👇",
            f"\"[Quote from key paper about {package.topic}]\"\n\n— [Author], [Journal] [Year]",
        ]
        return ideas

    def _generate_thread_outline(self, package: ContentPackage) -> str:
        """Generate Twitter thread outline."""
        return f"""# Thread Outline: {package.topic}

## 1/ Hook
[Provocative opening about {package.topic}]

## 2/ Context
Why this matters now

## 3/ Key Point 1
Evidence + implication

## 4/ Key Point 2
Evidence + implication

## 5/ Key Point 3
Evidence + implication

## 6/ Summary
What to remember

## 7/ CTA
Follow for more / Your thoughts?

## Claude: Expand using twitter-longform-medical skill
"""

    def _generate_carousel_content(self, package: ContentPackage) -> str:
        """Generate carousel slide content."""
        return f"""# Carousel Content: {package.topic}

## Slide 1: Hook
**Title**: [Attention-grabbing title about {package.topic}]
**Subtitle**: What you need to know

## Slide 2-4: Key Points (Myth/Tip format)
- Point 1: [Key insight]
- Point 2: [Key insight]
- Point 3: [Key insight]

## Slide 5: Stats
**Stat**: [Key number]
**Label**: [What it means]
**Source**: [PMID]

## Slide 6: CTA
Follow @heartdocshailesh for more

## Claude: Use carousel-generator-v2 to render
"""

    def _run_visual_phase(self, package: ContentPackage):
        """Phase 4: Generate visual content."""
        self._print("PHASE 4: VISUAL CONTENT", "phase")

        if not CAROUSEL_AVAILABLE:
            self._print("Carousel generator not available", "warning")
            package.errors.append("Carousel generator not available")
            return

        try:
            config = CarouselConfig(
                output_dir=package.output_dir / "visual" / "carousel",
                aspect_ratio=AspectRatio.INSTAGRAM_4X5,
                generate_caption=True,
                generate_hashtags=True
            )

            generator = CarouselGenerator(config)

            result = generator.generate_from_topic(
                package.topic,
                template="myth_busting" if "myth" in package.topic.lower() else "tips_5",
                use_ai=False  # Use database content first
            )

            package.carousel_path = result.output_directory
            self._print(f"Created carousel: {result.output_directory}", "success")

            package.phases_completed.append("visual")

        except Exception as e:
            self._print(f"Visual phase failed: {e}", "error")
            package.errors.append(f"Visual: {e}")

    def _save_manifest(self, package: ContentPackage):
        """Save package manifest for reference."""
        manifest = {
            "topic": package.topic,
            "created_at": package.created_at,
            "output_dir": str(package.output_dir),
            "phases_completed": package.phases_completed,
            "errors": package.errors,
            "pubmed_articles": package.pubmed_articles,
            "carousel_path": str(package.carousel_path) if package.carousel_path else None
        }

        manifest_path = package.output_dir / "manifest.json"
        with open(manifest_path, "w") as f:
            json.dump(manifest, f, indent=2)

        # Also create a README
        readme = f"""# Content Package: {package.topic}

Generated: {package.created_at}

## Contents

### Research
- `research-brief.md` - PubMed research summary

### Long-form (Outlines for Claude)
- `long-form/youtube-script-outline.md`
- `long-form/newsletter-b2c-outline.md`
- `long-form/newsletter-b2b-outline.md`
- `long-form/editorial-outline.md`
- `long-form/blog-outline.md`

### Short-form
- `short-form/tweets.md`
- `short-form/thread.md`
- `short-form/carousel-content.md`

### Visual
- `visual/carousel/` - Generated Instagram slides

## Next Steps

1. Review research brief
2. Ask Claude to complete long-form outlines using appropriate skills
3. Generate final carousel with carousel-generator-v2
4. Apply quality checks before publishing

## Phases Completed
{', '.join(package.phases_completed)}

{'## Errors' if package.errors else ''}
{chr(10).join('- ' + e for e in package.errors) if package.errors else ''}
"""
        readme_path = package.output_dir / "README.md"
        with open(readme_path, "w") as f:
            f.write(readme)


def main():
    parser = argparse.ArgumentParser(
        description="Content OS - Produce all content types from one idea"
    )
    parser.add_argument('topic', nargs='?', help='Topic or seed idea')
    parser.add_argument('--backward', type=str, metavar='FILE',
                       help='Backward mode: split long-form content into short-form')
    parser.add_argument('--skip', type=str, nargs='+',
                       choices=['research', 'long-form', 'short-form', 'visual'],
                       help='Phases to skip')
    parser.add_argument('-o', '--output', type=str,
                       help='Output directory')
    parser.add_argument('--suggest-topics', action='store_true',
                       help='Suggest topics from research engine')
    parser.add_argument('--from-research', action='store_true',
                       help='Use top research-suggested topic')
    parser.add_argument('--batch-from-research', type=int, metavar='N',
                       help='Process top N topics from research engine')

    args = parser.parse_args()

    output_dir = Path(args.output) if args.output else None
    orchestrator = ContentOSOrchestrator(output_dir)

    # Suggest topics from research
    if args.suggest_topics:
        if not RESEARCH_AVAILABLE:
            print("Error: Research integration not available")
            return
        research = ResearchIntegration()
        topics = research.suggest_topics(count=15)
        print("\n📊 SUGGESTED TOPICS FROM RESEARCH ENGINE:\n")
        for i, topic in enumerate(topics, 1):
            print(f"{i:2}. {topic.topic}")
            print(f"     Score: {topic.score:.1f} | Formats: {', '.join(topic.suggested_formats)}")
        print("\nUse: python orchestrator.py \"<topic>\" to generate content")
        return

    # Use top research topic
    if args.from_research:
        if not RESEARCH_AVAILABLE:
            print("Error: Research integration not available")
            return
        research = ResearchIntegration()
        topics = research.suggest_topics(count=1)
        if topics:
            args.topic = topics[0].topic
            print(f"Using research-suggested topic: {args.topic}")
        else:
            print("No topics available from research. Run research pipeline first.")
            return

    # Batch from research
    if args.batch_from_research:
        if not RESEARCH_AVAILABLE:
            print("Error: Research integration not available")
            return
        research = ResearchIntegration()
        topics = research.suggest_topics(count=args.batch_from_research)
        print(f"\n{'='*60}")
        print(f"BATCH CONTENT-OS: {len(topics)} topics from research")
        print(f"{'='*60}\n")
        for i, topic in enumerate(topics, 1):
            print(f"\n[{i}/{len(topics)}] {topic.topic}")
            try:
                package = orchestrator.run_forward(topic.topic, skip=args.skip or [])
                print(f"  ✓ Output: {package.output_dir}")
            except Exception as e:
                print(f"  ✗ Failed: {e}")
        return

    if not args.topic and not args.backward:
        parser.print_help()
        print("\nExamples:")
        print("  python orchestrator.py \"Statin myths for Indians\"")
        print("  python orchestrator.py --suggest-topics")
        print("  python orchestrator.py --from-research")
        print("  python orchestrator.py --batch-from-research 5")
        return

    if args.backward:
        print("Backward mode not yet implemented")
        print("Use: Content OS: [paste long-form content] in Claude")
        return

    package = orchestrator.run_forward(args.topic, skip=args.skip or [])
    print(f"\nOutput: {package.output_dir}")


if __name__ == "__main__":
    main()
