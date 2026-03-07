"""
Carousel Employee - An AI Graphic Designer for Dr. Shailesh Singh

This module acts like a real graphic designer employee who can:
1. Work AUTONOMOUSLY when given a broad topic
2. Work with SPECIFIC CONTENT when provided
3. RESEARCH topics using PubMed before creating
4. Create INFOGRAPHICS (single-image summaries)
5. Work INTERACTIVELY in conversational mode

Usage:
    # As a module
    from scripts.carousel_employee import CarouselEmployee

    employee = CarouselEmployee()

    # Autonomous - just give a topic
    employee.create("Statin myths")

    # With specific content
    employee.create("Statin myths", content={
        "myths": [
            {"myth": "Statins cause muscle pain", "truth": "Only 5-10% affected"}
        ]
    })

    # Research first
    employee.research_and_create("SGLT2 inhibitors heart failure")

    # Interactive mode
    employee.interactive()

    # Infographic
    employee.create_infographic("5 facts about statins")

CLI Usage:
    # Autonomous (quick)
    python -m scripts.carousel_employee "Statin myths" --auto

    # Interactive (default)
    python -m scripts.carousel_employee "Statin myths"

    # Research mode
    python -m scripts.carousel_employee "Statin myths" --research

    # With content file
    python -m scripts.carousel_employee "Statin myths" --content content.json

    # Infographic
    python -m scripts.carousel_employee "Statin myths" --infographic
"""

import os
import sys
import json
import argparse
import shutil
from pathlib import Path
from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime

# Internal imports
from .models import SlideType, ColorMode, SlideContent, TEMPLATE_PRESETS, AspectRatio
from .content_structurer import ContentStructurer, ResearchResult, ContentStructure
from .content_database import (
    get_content, get_myths_for_topic, get_statistics_for_topic,
    get_tips_for_topic, get_hooks_for_topic, normalize_topic, list_available_topics
)
from .hooks_generator import HooksGenerator
from .pillow_renderer import PillowRenderer
from .puppeteer_renderer import PuppeteerRenderer
from .quality_checker import QualityChecker

# Import PubMed client
try:
    sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent / "scripts"))
    from pubmed_client import PubMedClient
    PUBMED_CLIENT_AVAILABLE = True
except ImportError:
    PUBMED_CLIENT_AVAILABLE = False


class OperationMode(str, Enum):
    """How the employee should work."""
    AUTONOMOUS = "autonomous"      # Auto-generate everything
    CONTENT = "content"            # Use provided content
    RESEARCH = "research"          # Research first, then create
    INTERACTIVE = "interactive"    # Conversational flow
    INFOGRAPHIC = "infographic"    # Single-image output


@dataclass
class ContentBrief:
    """Brief from user about what they want."""
    topic: str
    angle: Optional[str] = None           # "myth-busting", "tips", "data", "story"
    target_audience: str = "patients"      # "patients", "doctors", "general"
    specific_points: List[str] = field(default_factory=list)
    myths: List[Dict[str, str]] = field(default_factory=list)
    statistics: List[Dict[str, str]] = field(default_factory=list)
    tips: List[str] = field(default_factory=list)
    sources: List[str] = field(default_factory=list)
    tone: str = "educational"              # "educational", "urgent", "reassuring"
    slide_count: Optional[int] = None


@dataclass
class ResearchFindings:
    """Research results to present to user."""
    topic: str
    summary: str
    myths_found: List[Dict[str, str]]
    statistics_found: List[Dict[str, str]]
    key_points: List[str]
    sources: List[str]
    pmids: List[str]
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


class CarouselEmployee:
    """
    An AI Graphic Designer employee for carousel creation.

    Works like a real employee:
    - Understands context and intent
    - Asks clarifying questions when needed
    - Researches when appropriate
    - Delivers polished output
    """

    def __init__(self, verbose: bool = True, use_puppeteer: bool = True,
                 use_satori: Optional[bool] = None, dimensions: str = "portrait",
                 generate_both_ratios: bool = False):
        """Initialize the employee with tools.

        Args:
            verbose: Whether to print progress messages
            use_puppeteer: Whether to use Puppeteer renderer (True) or Pillow (False)
            use_satori: Deprecated alias (treated as use_puppeteer)
            dimensions: Output dimensions ("square" or "portrait")
            generate_both_ratios: Render both 4:5 and 1:1 outputs
        """
        self.verbose = verbose
        if use_satori is not None:
            use_puppeteer = use_satori
        self.use_puppeteer = use_puppeteer
        self.structurer = ContentStructurer()
        self.generate_both_ratios = generate_both_ratios

        # Output directory
        self.output_dir = Path(__file__).parent.parent / "output" / "carousels"
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Initialize renderers
        self.pillow_renderer = PillowRenderer()
        self.puppeteer_renderer = PuppeteerRenderer(dimensions=dimensions)
        self.renderer = self.puppeteer_renderer if self.use_puppeteer else self.pillow_renderer

        self.quality_checker = QualityChecker()
        self.hooks_generator = HooksGenerator()

    def _log(self, message: str):
        """Print if verbose mode."""
        if self.verbose:
            print(message)

    def _detect_mode(self, topic: str, content: Dict = None,
                     research: bool = False, interactive: bool = False,
                     infographic: bool = False) -> OperationMode:
        """Intelligently detect which mode to use."""
        if infographic:
            return OperationMode.INFOGRAPHIC
        if interactive:
            return OperationMode.INTERACTIVE
        if research:
            return OperationMode.RESEARCH
        if content:
            return OperationMode.CONTENT
        return OperationMode.AUTONOMOUS

    def _detect_template(self, topic: str, angle: str = None) -> str:
        """Detect the best template for the topic."""
        topic_lower = topic.lower()

        if angle:
            angle_map = {
                "myth": "myth_busting",
                "myths": "myth_busting",
                "myth-busting": "myth_busting",
                "tips": "tips_5",
                "data": "data_driven",
                "story": "patient_story",
                "how-to": "how_to",
                "howto": "how_to",
            }
            if angle.lower() in angle_map:
                return angle_map[angle.lower()]

        # Auto-detect from topic
        if any(word in topic_lower for word in ["myth", "truth", "lie", "wrong", "debunk"]):
            return "myth_busting"
        if any(word in topic_lower for word in ["tip", "way", "improve", "reduce"]):
            return "tips_5"
        if any(word in topic_lower for word in ["data", "study", "trial", "research", "evidence"]):
            return "data_driven"
        if any(word in topic_lower for word in ["story", "patient", "case", "journey"]):
            return "patient_story"
        if any(word in topic_lower for word in ["how to", "step", "guide"]):
            return "how_to"

        return "tips_5"  # Default

    # =========================================================================
    # MODE: AUTONOMOUS
    # =========================================================================
    def create_autonomous(self, topic: str, template: str = None) -> Path:
        """
        Autonomous mode: Generate carousel from topic using content database.

        Args:
            topic: The carousel topic
            template: Optional template override

        Returns:
            Path to output directory
        """
        self._log(f"\n🤖 AUTONOMOUS MODE: Creating carousel for '{topic}'")
        self._log("-" * 50)

        # Detect template
        if not template:
            template = self._detect_template(topic)
        self._log(f"📋 Template: {template}")

        # Check content database
        db_content = get_content(topic)
        if db_content:
            self._log(f"📚 Found curated content for: {db_content.topic}")
            self._log(f"   {len(db_content.myths)} myths, {len(db_content.statistics)} stats, {len(db_content.tips)} tips")
        else:
            self._log(f"⚠️  No curated content found - using general generation")

        # Structure content
        structure = self.structurer.structure_from_topic(topic, template=template)

        # Quality check
        self._log(f"\n🔍 Running quality checks...")

        # Render
        output_path = self._render_carousel(structure, topic)

        self._log(f"\n✅ Carousel complete!")
        self._log(f"   📁 Output: {output_path}")

        return output_path

    # =========================================================================
    # MODE: CONTENT (User-provided)
    # =========================================================================
    def create_with_content(self, topic: str, content: Dict[str, Any],
                           template: str = None) -> Path:
        """
        Content mode: Generate carousel from user-provided content.

        Args:
            topic: The carousel topic
            content: Dict with myths, statistics, tips, etc.
            template: Optional template override

        Returns:
            Path to output directory
        """
        self._log(f"\n📝 CONTENT MODE: Creating carousel for '{topic}'")
        self._log("-" * 50)

        # Detect template
        if not template:
            template = self._detect_template(topic)
        self._log(f"📋 Template: {template}")

        # Build ResearchResult from user content
        research = ResearchResult(
            topic=topic,
            key_points=content.get("tips", content.get("key_points", [])),
            statistics=content.get("statistics", content.get("stats", [])),
            myths=content.get("myths", []),
            quotes=content.get("quotes", []),
            steps=content.get("steps", []),
            sources=content.get("sources", []),
            pmids=content.get("pmids", [])
        )

        self._log(f"📊 Using your content:")
        self._log(f"   {len(research.myths)} myths")
        self._log(f"   {len(research.statistics)} statistics")
        self._log(f"   {len(research.key_points)} key points")

        # Structure with user content
        structure = self.structurer.structure_from_topic(topic, template=template, research=research)

        # Render
        output_path = self._render_carousel(structure, topic)

        self._log(f"\n✅ Carousel complete with your content!")
        self._log(f"   📁 Output: {output_path}")

        return output_path

    # =========================================================================
    # MODE: RESEARCH
    # =========================================================================
    def research_topic(self, topic: str) -> ResearchFindings:
        """
        Research a topic using PubMed and content database.

        Args:
            topic: Topic to research

        Returns:
            ResearchFindings with discovered information
        """
        self._log(f"\n🔬 RESEARCHING: '{topic}'")
        self._log("-" * 50)

        findings = ResearchFindings(
            topic=topic,
            summary="",
            myths_found=[],
            statistics_found=[],
            key_points=[],
            sources=[],
            pmids=[]
        )

        # Check content database first
        db_content = get_content(topic)
        if db_content:
            self._log(f"📚 Found in content database: {db_content.topic}")
            findings.myths_found = db_content.myths[:5]
            findings.statistics_found = db_content.statistics[:5]
            findings.key_points = db_content.tips[:5]
            findings.sources = db_content.sources
            findings.summary = f"Found curated content for {db_content.topic} with {len(db_content.myths)} myths and {len(db_content.statistics)} statistics."

        # Search PubMed for real evidence
        if PUBMED_CLIENT_AVAILABLE:
            try:
                self._log(f"🔍 Searching PubMed for: {topic}")
                client = PubMedClient()

                # Search for relevant articles
                articles = client.search_and_fetch(
                    query=f"{topic} randomized controlled trial OR meta-analysis",
                    max_results=5,
                    sort="relevance"
                )

                if articles:
                    self._log(f"   ✓ Found {len(articles)} relevant articles")
                    # Extract key statistics from abstracts
                    for article in articles[:3]:
                        self._log(f"   • {article.title[:60]}... (PMID: {article.pmid})")
                        if article.abstract:
                            # Add source
                            findings.sources.append(f"{article.journal} (PMID: {article.pmid})")
                else:
                    self._log(f"   ℹ️  No PubMed articles found for this topic")

            except Exception as e:
                self._log(f"   ⚠️  PubMed search error: {e}")
        else:
            self._log(f"   ℹ️  PubMed client not available, using database only")

        return findings

    def research_and_create(self, topic: str, template: str = None,
                           auto_approve: bool = False) -> Path:
        """
        Research mode: Research topic, show findings, then create.

        Args:
            topic: Topic to research and create carousel for
            template: Optional template override
            auto_approve: If True, skip confirmation

        Returns:
            Path to output directory
        """
        self._log(f"\n🔬 RESEARCH MODE: '{topic}'")
        self._log("=" * 50)

        # Research
        findings = self.research_topic(topic)

        # Present findings
        self._log(f"\n📋 RESEARCH FINDINGS:")
        self._log("-" * 50)

        if findings.myths_found:
            self._log(f"\n🎭 MYTHS FOUND ({len(findings.myths_found)}):")
            for i, myth in enumerate(findings.myths_found[:3], 1):
                self._log(f"   {i}. {myth.get('myth', '')[:60]}...")

        if findings.statistics_found:
            self._log(f"\n📊 STATISTICS FOUND ({len(findings.statistics_found)}):")
            for stat in findings.statistics_found[:3]:
                self._log(f"   • {stat.get('value', '')} - {stat.get('label', '')[:40]}")

        if findings.key_points:
            self._log(f"\n💡 KEY POINTS ({len(findings.key_points)}):")
            for i, point in enumerate(findings.key_points[:3], 1):
                self._log(f"   {i}. {point[:60]}...")

        # Confirmation (unless auto-approve)
        if not auto_approve:
            self._log(f"\n" + "=" * 50)
            response = input("Proceed with this content? [Y/n/customize]: ").strip().lower()
            if response == 'n':
                self._log("Cancelled by user.")
                return None
            elif response == 'customize':
                self._log("Customization mode - implement interactive selection")
                # TODO: Interactive selection of which points to include

        # Create carousel with research findings
        content = {
            "myths": findings.myths_found,
            "statistics": findings.statistics_found,
            "tips": findings.key_points,
            "sources": findings.sources,
            "pmids": findings.pmids
        }

        return self.create_with_content(topic, content, template=template)

    # =========================================================================
    # MODE: INTERACTIVE
    # =========================================================================
    def interactive(self, initial_topic: str = None) -> Path:
        """
        Interactive mode: Conversational carousel creation.

        Like working with a real designer - back and forth until it's right.
        """
        print("\n" + "=" * 60)
        print("🎨 INTERACTIVE CAROUSEL DESIGNER")
        print("=" * 60)
        print("I'll help you create a carousel. Let's start!\n")

        # Step 1: Topic
        if initial_topic:
            topic = initial_topic
            print(f"📌 Topic: {topic}")
        else:
            topic = input("What topic should the carousel cover?\n> ").strip()

        if not topic:
            print("No topic provided. Exiting.")
            return None

        # Step 2: Check what we know
        db_content = get_content(topic)
        normalized = normalize_topic(topic)

        print(f"\n🔍 Analyzing: '{topic}'")
        if db_content:
            print(f"   ✓ Found curated content for: {db_content.core_subject}")
            print(f"   ✓ {len(db_content.myths)} myths, {len(db_content.statistics)} stats available")
        else:
            print(f"   ⚠ No curated content - will need your input or research")

        # Step 3: Determine angle
        print(f"\n📐 What angle do you want?")
        print("   1. Myth-busting (debunk misconceptions)")
        print("   2. Tips (actionable advice)")
        print("   3. Data-driven (statistics and evidence)")
        print("   4. Story (patient journey)")
        print("   5. How-to (step-by-step guide)")

        angle_choice = input("\nChoose [1-5] or describe: ").strip()

        angle_map = {"1": "myth_busting", "2": "tips_5", "3": "data_driven",
                     "4": "patient_story", "5": "how_to"}
        template = angle_map.get(angle_choice, self._detect_template(topic, angle_choice))

        print(f"   → Using template: {template}")

        # Step 4: Content source
        print(f"\n📚 Content source:")
        print("   1. Use curated content (from database)")
        print("   2. Research topic (PubMed + database)")
        print("   3. I'll provide the content")
        print("   4. Generate autonomously")

        source_choice = input("\nChoose [1-4]: ").strip()

        if source_choice == "1" and db_content:
            # Use database content
            content = {
                "myths": db_content.myths,
                "statistics": db_content.statistics,
                "tips": db_content.tips,
                "quotes": db_content.quotes,
                "sources": db_content.sources
            }
            return self.create_with_content(topic, content, template=template)

        elif source_choice == "2":
            # Research mode
            return self.research_and_create(topic, template=template)

        elif source_choice == "3":
            # User provides content
            print("\n📝 Enter your content:")
            content = self._collect_user_content(template)
            return self.create_with_content(topic, content, template=template)

        else:
            # Autonomous
            return self.create_autonomous(topic, template=template)

    def _collect_user_content(self, template: str) -> Dict[str, Any]:
        """Collect content from user based on template type."""
        content = {"myths": [], "statistics": [], "tips": [], "quotes": []}

        if template == "myth_busting":
            print("\nEnter myths (empty line to finish):")
            while True:
                myth = input("MYTH: ").strip()
                if not myth:
                    break
                truth = input("TRUTH: ").strip()
                content["myths"].append({"myth": myth, "truth": truth})

        elif template in ["tips_5", "how_to"]:
            print("\nEnter tips/steps (empty line to finish):")
            while True:
                tip = input(f"Tip {len(content['tips'])+1}: ").strip()
                if not tip:
                    break
                content["tips"].append(tip)

        elif template == "data_driven":
            print("\nEnter statistics (empty line to finish):")
            while True:
                value = input("VALUE (e.g., 25%): ").strip()
                if not value:
                    break
                label = input("LABEL: ").strip()
                context = input("CONTEXT: ").strip()
                content["statistics"].append({
                    "value": value, "label": label, "context": context
                })

        return content

    # =========================================================================
    # MODE: INFOGRAPHIC
    # =========================================================================
    def create_infographic(self, topic: str, content: Dict = None) -> Path:
        """
        Create a single-image infographic summarizing the topic.

        Args:
            topic: The infographic topic
            content: Optional content dict

        Returns:
            Path to output image
        """
        self._log(f"\n🖼️  INFOGRAPHIC MODE: '{topic}'")
        self._log("-" * 50)

        # Get content
        if not content:
            db_content = get_content(topic)
            if db_content:
                content = {
                    "title": topic,
                    "points": db_content.tips[:5],
                    "statistic": db_content.statistics[0] if db_content.statistics else None,
                    "source": db_content.sources[0] if db_content.sources else None
                }

        # For now, create a single slide with key info
        # TODO: Implement dedicated infographic renderer
        self._log("⚠️  Infographic mode uses carousel renderer (single slide)")

        # Create single-slide carousel
        structure = self.structurer.structure_from_topic(topic, template="tips_5")
        structure.slides = structure.slides[:1]  # Just the hook slide

        output_path = self._render_carousel(structure, f"{topic}-infographic", single_slide=True)

        self._log(f"\n✅ Infographic complete!")
        self._log(f"   📁 Output: {output_path}")

        return output_path

    # =========================================================================
    # RENDERING
    # =========================================================================
    def _rename_with_suffix(self, results, output_dir: Path, suffix: str):
        renamed = []
        for i, result in enumerate(results, 1):
            slide_number = getattr(result, "slide_number", i)
            output_path = Path(getattr(result, "output_path", result))
            target_name = output_dir / f"slide_{slide_number:02d}_{suffix}.png"
            target_name.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(output_path), str(target_name))
            if hasattr(result, "output_path"):
                result.output_path = target_name
            renamed.append(result)
        return renamed

    def _render_dual_ratios(self, slides_to_render: List[SlideContent], output_dir: Path):
        ratio_specs = [
            ("4x5", "portrait"),
            ("1x1", "square")
        ]
        all_results = []
        for suffix, dimensions in ratio_specs:
            if self.use_puppeteer:
                renderer = PuppeteerRenderer(dimensions=dimensions)
                temp_dir = output_dir / f"_tmp_{suffix}"
                temp_dir.mkdir(parents=True, exist_ok=True)
                results = renderer.render_carousel(
                    slides_to_render,
                    output_dir=str(temp_dir),
                    filename_prefix="slide"
                )
                all_results.extend(self._rename_with_suffix(results, output_dir, suffix))
                shutil.rmtree(temp_dir, ignore_errors=True)
            else:
                self.pillow_renderer.config.aspect_ratio = (
                    AspectRatio.INSTAGRAM_4X5 if dimensions == "portrait" else AspectRatio.SQUARE_1X1
                )
                results = self.pillow_renderer.render_carousel(slides_to_render, topic=output_dir.name)
                all_results.extend(self._rename_with_suffix(results, output_dir, suffix))
        return all_results

    def _render_carousel(self, structure: ContentStructure, topic: str,
                        single_slide: bool = False) -> Path:
        """Render the carousel slides using Puppeteer or Pillow renderer."""
        # Create output directory
        safe_name = "".join(c if c.isalnum() or c in "- " else "" for c in topic)
        safe_name = safe_name.replace(" ", "-")
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        output_dir = self.output_dir / f"{safe_name}-{timestamp}"
        output_dir.mkdir(parents=True, exist_ok=True)

        # Render slides
        slides_to_render = structure.slides[:1] if single_slide else structure.slides
        total_slides = len(slides_to_render)

        renderer_name = "Puppeteer" if self.use_puppeteer else "Pillow"
        self._log(f"\n🎨 Rendering {total_slides} slide(s) with {renderer_name}...")

        if self.generate_both_ratios:
            results = self._render_dual_ratios(slides_to_render, output_dir)
            for i, result in enumerate(results, 1):
                render_time = getattr(result, 'render_time_ms', 0)
                self._log(f"   ✓ Slide {i}/{len(results)} ({render_time:.0f}ms)")
        elif self.use_puppeteer:
            # Use Puppeteer renderer
            for i, slide in enumerate(slides_to_render, 1):
                slide.slide_number = i
            results = self.puppeteer_renderer.render_carousel(
                slides_to_render,
                output_dir=str(output_dir),
                filename_prefix="slide"
            )
            for i, result in enumerate(results, 1):
                render_time = getattr(result, 'render_time_ms', 0)
                self._log(f"   ✓ Slide {i}/{total_slides} ({render_time:.0f}ms)")
        else:
            # Use Pillow renderer (legacy)
            self.pillow_renderer.config.output_dir = output_dir
            for i, slide in enumerate(slides_to_render, 1):
                result = self.pillow_renderer.render_slide(slide)
                self._log(f"   ✓ Slide {i}/{total_slides} ({result.render_time_ms:.0f}ms)")

        # Save metadata
        ratio_label = "4:5"
        if self.use_puppeteer:
            ratio_label = "4:5" if self.puppeteer_renderer.dimensions == "portrait" else "1:1"
        else:
            ratio_label = "4:5" if self.pillow_renderer.config.aspect_ratio == AspectRatio.INSTAGRAM_4X5 else "1:1"

        metadata = {
            "topic": structure.topic,
            "template": structure.template,
            "framework": structure.framework.value,
            "slide_count": len(slides_to_render),
            "created": datetime.now().isoformat(),
            "renderer": renderer_name,
            "ratios": ["4:5", "1:1"] if self.generate_both_ratios else [ratio_label],
            "slides": [
                {
                    "number": s.slide_number,
                    "type": s.slide_type.value,
                    "title": s.title,
                    "myth": s.myth_text,
                    "truth": s.truth_text,
                    "statistic": s.statistic,
                    "stat_label": s.stat_label
                }
                for s in slides_to_render
            ]
        }

        with open(output_dir / "metadata.json", "w") as f:
            json.dump(metadata, f, indent=2)

        return output_dir

    # =========================================================================
    # MAIN ENTRY POINT
    # =========================================================================
    def create(self, topic: str,
               content: Dict = None,
               template: str = None,
               mode: str = None,
               research: bool = False,
               interactive: bool = False,
               infographic: bool = False,
               auto: bool = False) -> Path:
        """
        Main entry point - intelligently routes to appropriate mode.

        Args:
            topic: The carousel topic
            content: Optional content dict
            template: Optional template override
            mode: Force a specific mode
            research: Enable research mode
            interactive: Enable interactive mode
            infographic: Create infographic instead
            auto: Force autonomous mode

        Returns:
            Path to output
        """
        # Detect mode
        if mode:
            op_mode = OperationMode(mode)
        elif auto:
            op_mode = OperationMode.AUTONOMOUS
        else:
            op_mode = self._detect_mode(topic, content, research, interactive, infographic)

        # Route to appropriate handler
        if op_mode == OperationMode.INFOGRAPHIC:
            return self.create_infographic(topic, content)
        elif op_mode == OperationMode.INTERACTIVE:
            return self.interactive(topic)
        elif op_mode == OperationMode.RESEARCH:
            return self.research_and_create(topic, template=template)
        elif op_mode == OperationMode.CONTENT:
            return self.create_with_content(topic, content, template=template)
        else:  # AUTONOMOUS
            return self.create_autonomous(topic, template=template)


# =============================================================================
# CLI
# =============================================================================
def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="🎨 Carousel Employee - AI Graphic Designer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode (default)
  python -m scripts.carousel_employee "Statin myths"

  # Autonomous mode
  python -m scripts.carousel_employee "Statin myths" --auto

  # Research mode
  python -m scripts.carousel_employee "SGLT2 inhibitors" --research

  # With content file
  python -m scripts.carousel_employee "My topic" --content content.json

  # Infographic
  python -m scripts.carousel_employee "5 statin facts" --infographic

  # Specific template
  python -m scripts.carousel_employee "Blood pressure" --template myth_busting
        """
    )

    parser.add_argument("topic", nargs="?", help="Carousel topic")
    parser.add_argument("--auto", "-a", action="store_true",
                        help="Autonomous mode - generate without asking")
    parser.add_argument("--research", "-r", action="store_true",
                        help="Research mode - search PubMed first")
    parser.add_argument("--interactive", "-i", action="store_true",
                        help="Interactive mode - conversational flow")
    parser.add_argument("--infographic", action="store_true",
                        help="Create single-image infographic")
    parser.add_argument("--content", "-c", type=str,
                        help="Path to content JSON file")
    parser.add_argument("--template", "-t", type=str,
                        help="Template: myth_busting, tips_5, data_driven, etc.")
    parser.add_argument("--ratio", default="4:5", choices=["4:5", "1:1"],
                        help="Aspect ratio (default: 4:5)")
    parser.add_argument("--both-ratios", action="store_true",
                        help="Generate both 4:5 and 1:1 outputs")
    parser.add_argument("--quiet", "-q", action="store_true",
                        help="Suppress output messages")
    parser.add_argument("--list-topics", action="store_true",
                        help="List available curated topics")

    args = parser.parse_args()

    # List topics
    if args.list_topics:
        print("\n📚 Available Curated Topics:")
        print("-" * 40)
        for topic in list_available_topics():
            content = get_content(topic)
            print(f"  • {topic}: {len(content.myths)} myths, {len(content.statistics)} stats")
        return

    # Create employee
    dimensions = "portrait" if args.ratio == "4:5" else "square"
    employee = CarouselEmployee(
        verbose=not args.quiet,
        dimensions=dimensions,
        generate_both_ratios=args.both_ratios
    )

    # Load content file if provided
    content = None
    if args.content:
        with open(args.content) as f:
            content = json.load(f)

    # Determine mode and execute
    if not args.topic and not args.interactive:
        # No topic - go interactive
        employee.interactive()
    else:
        employee.create(
            topic=args.topic or "",
            content=content,
            template=args.template,
            research=args.research,
            interactive=args.interactive or (not args.auto and not args.research and not content),
            infographic=args.infographic,
            auto=args.auto
        )


if __name__ == "__main__":
    main()
