#!/usr/bin/env python3
"""
Carousel Generator v2 - Main Orchestrator

World-class Instagram carousel generator that combines:
- AI content intelligence
- Multi-tool visual generation
- Professional design systems
- Quality assurance automation

Usage:
    python carousel_generator.py "GLP-1 for weight loss" --template tips
    python carousel_generator.py input.json --output ./my-carousel/

Part of Dr. Shailesh Singh's Integrated Cowriting System.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import List, Optional, Dict, Any
import time
import shutil
from datetime import datetime

from .models import (
    Carousel, CarouselConfig, SlideContent, SlideType,
    ColorMode, AspectRatio, ContentCategory, CarouselRenderResult,
    TEMPLATE_PRESETS
)
from .pillow_renderer import PillowRenderer
from .puppeteer_renderer import PuppeteerRenderer
from .tokens import get_account, get_quality_gates
from .content_structurer import ContentStructurer, structure_content, structure_from_text
from .quality_checker import QualityChecker, QualityCheckResult
from .caption_generator import CaptionGenerator, generate_caption_for_carousel


class CarouselGenerator:
    """Main orchestrator for carousel generation."""

    def __init__(self, config: CarouselConfig = None):
        self.config = config or CarouselConfig()
        self.renderer = self._init_renderer()
        self.structurer = ContentStructurer(use_ai=True)
        self.quality_checker = QualityChecker()
        self.caption_generator = CaptionGenerator(use_ai=True)

    def _init_renderer(self):
        """Initialize the preferred renderer."""
        dimensions = "portrait" if self.config.aspect_ratio == AspectRatio.INSTAGRAM_4X5 else "square"
        try:
            return PuppeteerRenderer(dimensions=dimensions)
        except Exception:
            return PillowRenderer(self.config)

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

    def _render_dual_ratios(self, slides: List[SlideContent], output_dir: Path):
        ratio_specs = [
            ("4x5", AspectRatio.INSTAGRAM_4X5, "portrait"),
            ("1x1", AspectRatio.SQUARE_1X1, "square")
        ]

        all_results = []
        original_ratio = self.config.aspect_ratio
        for suffix, aspect_ratio, dimensions in ratio_specs:
            if isinstance(self.renderer, PuppeteerRenderer):
                renderer = PuppeteerRenderer(dimensions=dimensions)
                temp_dir = output_dir / f"_tmp_{suffix}"
                temp_dir.mkdir(parents=True, exist_ok=True)
                results = renderer.render_carousel(
                    slides,
                    output_dir=str(temp_dir),
                    filename_prefix="slide"
                )
                all_results.extend(self._rename_with_suffix(results, output_dir, suffix))
                shutil.rmtree(temp_dir, ignore_errors=True)
            else:
                self.config.aspect_ratio = aspect_ratio
                self.renderer = PillowRenderer(self.config)
                results = self.renderer.render_carousel(slides, topic=output_dir.name)
                all_results.extend(self._rename_with_suffix(results, output_dir, suffix))

        self.config.aspect_ratio = original_ratio
        return all_results

    def _render_slides(self, slides: List[SlideContent], topic: str):
        """Render slides using the configured renderer."""
        output_dir = self.config.output_dir or (
            Path(__file__).parent.parent / "output" / "carousels" / topic.replace(" ", "-")
        )
        output_dir.mkdir(parents=True, exist_ok=True)

        if self.config.generate_both_ratios and self.config.output_dir is None:
            if list(output_dir.glob("slide_*.png")):
                timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                output_dir = output_dir / f"dual-{timestamp}"
                output_dir.mkdir(parents=True, exist_ok=True)

        self.config.output_dir = output_dir

        if self.config.generate_both_ratios:
            return self._render_dual_ratios(slides, output_dir)

        if isinstance(self.renderer, PuppeteerRenderer):
            return self.renderer.render_carousel(slides, output_dir=str(output_dir), filename_prefix="slide")
        return self.renderer.render_carousel(slides, topic)

    def generate_from_topic(self, topic: str,
                           template: str = "tips_5",
                           use_ai: bool = True) -> CarouselRenderResult:
        """
        Generate a carousel from just a topic.

        Args:
            topic: The carousel topic (e.g., "GLP-1 for weight loss")
            template: Template preset name (tips_5, myth_busting, etc.)
            use_ai: Whether to use AI for content structuring

        Returns:
            CarouselRenderResult with paths to generated slides
        """
        print(f"\nGenerating carousel: {topic}")
        print(f"Template: {template}")

        start_time = time.time()

        # Use content structurer for intelligent slide generation
        if use_ai:
            print("Structuring content with AI...")
        else:
            print("Structuring content from curated database...")

        content_structure = self.structurer.structure_from_topic(topic, template)
        slides = content_structure.slides
        print(f"  Framework: {content_structure.framework.value}")
        print(f"  Template: {content_structure.template}")

        # Create carousel object
        carousel = Carousel(
            topic=topic,
            slides=slides,
            config=self.config
        )

        # Run quality checks
        quality_results = None
        if self.config.check_text_density or self.config.check_anti_ai:
            print("Running quality checks...")
            quality_results = self.quality_checker.run_all_checks(carousel)

            # Update carousel with quality metrics
            all_checks = quality_results["carousel"] + [
                c for checks in quality_results["slides"].values() for c in checks
            ]
            carousel.contrast_passed = all(
                c.passed for c in all_checks if c.check_name == "contrast_ratio"
            )
            carousel.anti_ai_passed = all(
                c.passed for c in all_checks if c.check_name == "anti_ai"
            )

        # Render slides
        print(f"\nRendering {len(slides)} slides...")
        results = self._render_slides(slides, topic)

        total_time = (time.time() - start_time) * 1000

        output_dir = self.config.output_dir or (
            Path(__file__).parent.parent / "output" / "carousels" / topic.replace(" ", "-")
        )

        render_result = CarouselRenderResult(
            carousel=carousel,
            slides=results,
            total_render_time_ms=total_time,
            output_directory=output_dir
        )

        # Add quality check results to render result
        if quality_results:
            render_result.text_density_check = {
                "passed": all(
                    c.passed for slide_checks in quality_results["slides"].values()
                    for c in slide_checks if c.check_name == "text_density"
                ),
                "details": {
                    slide_num: next(
                        (c.details for c in checks if c.check_name == "text_density"), None
                    )
                    for slide_num, checks in quality_results["slides"].items()
                }
            }

        # Generate caption and hashtags if enabled
        caption_result = None
        if self.config.generate_caption or self.config.generate_hashtags:
            print("Generating caption and hashtags...")
            # Determine style from template
            style = "myth_busting" if "myth" in template else "tips" if "tip" in template else "educational"
            caption_result = self.caption_generator.generate_caption(slides, topic, style)

            # Save caption to file
            if self.config.generate_caption:
                caption_file = output_dir / "caption.txt"
                with open(caption_file, "w") as f:
                    f.write(self.caption_generator.format_for_instagram(caption_result))
                print(f"  Caption saved: {caption_file}")

            # Save hashtags to file
            if self.config.generate_hashtags:
                hashtags_file = output_dir / "hashtags.txt"
                with open(hashtags_file, "w") as f:
                    f.write(" ".join(caption_result.hashtags))
                print(f"  Hashtags saved: {hashtags_file}")

            # Save alt texts to file
            if self.config.generate_alt_text and caption_result.alt_texts:
                alt_text_file = output_dir / "alt-text.txt"
                with open(alt_text_file, "w") as f:
                    for alt in caption_result.alt_texts:
                        f.write(f"{alt}\n")
                print(f"  Alt texts saved: {alt_text_file}")

            # Update carousel with caption info
            carousel.caption = caption_result.caption
            carousel.hashtags = caption_result.hashtags

        print(f"\nCarousel complete!")
        print(f"  Slides: {len(results)}")
        print(f"  Output: {output_dir}")
        print(f"  Time: {total_time:.0f}ms")

        # Print quality summary
        if quality_results:
            all_checks = quality_results["carousel"] + [
                c for checks in quality_results["slides"].values() for c in checks
            ]
            passed = sum(1 for c in all_checks if c.passed)
            total = len(all_checks)
            print(f"  Quality: {passed}/{total} checks passed")

            # Show any failures
            failures = [c for c in all_checks if not c.passed]
            if failures:
                print("  Issues:")
                for f in failures[:3]:  # Show first 3 issues
                    print(f"    - {f.check_name}: {f.message}")

        return render_result

    def generate_from_json(self, json_path: Path) -> CarouselRenderResult:
        """
        Generate a carousel from structured JSON input.

        Args:
            json_path: Path to JSON file with slide definitions

        Returns:
            CarouselRenderResult
        """
        with open(json_path, 'r') as f:
            data = json.load(f)

        slides = []
        for i, slide_data in enumerate(data.get('slides', []), 1):
            slide = SlideContent(
                slide_type=SlideType(slide_data.get('type', 'tips')),
                slide_number=i,
                **{k: v for k, v in slide_data.items() if k != 'type'}
            )
            slides.append(slide)

        topic = data.get('topic', json_path.stem)

        carousel = Carousel(
            topic=topic,
            slides=slides,
            config=self.config
        )

        print(f"\nRendering {len(slides)} slides from JSON...")
        results = self._render_slides(slides, topic)

        output_dir = self.config.output_dir or (
            Path(__file__).parent.parent / "output" / "carousels" / topic.replace(" ", "-")
        )

        return CarouselRenderResult(
            carousel=carousel,
            slides=results,
            total_render_time_ms=0,
            output_directory=output_dir
        )

    def generate_from_longform(self, content: str,
                               content_type: str = "newsletter") -> CarouselRenderResult:
        """
        Generate a carousel from long-form content (backward mode).

        Args:
            content: Long-form text (newsletter, blog, script)
            content_type: Type of content for appropriate parsing

        Returns:
            CarouselRenderResult
        """
        print(f"\nExtracting carousel from {content_type}...")

        start_time = time.time()

        # Use content structurer to extract slides from long-form
        content_structure = self.structurer.structure_from_longform(content, content_type)
        slides = content_structure.slides
        topic = content_structure.topic

        print(f"  Topic: {topic}")
        print(f"  Framework: {content_structure.framework.value}")
        print(f"  Slides: {len(slides)}")

        carousel = Carousel(
            topic=topic,
            slides=slides,
            config=self.config
        )

        print(f"\nRendering {len(slides)} slides...")
        results = self._render_slides(slides, topic)

        total_time = (time.time() - start_time) * 1000

        output_dir = self.config.output_dir or (
            Path(__file__).parent.parent / "output" / "carousels" / topic.replace(" ", "-")[:50]
        )

        render_result = CarouselRenderResult(
            carousel=carousel,
            slides=results,
            total_render_time_ms=total_time,
            output_directory=output_dir
        )

        print(f"\nCarousel extracted!")
        print(f"  Slides: {len(results)}")
        print(f"  Output: {output_dir}")
        print(f"  Time: {total_time:.0f}ms")

        return render_result

    def run_quality_check(self, carousel: Carousel, verbose: bool = False) -> Dict[str, Any]:
        """
        Run quality checks on a carousel and optionally print report.

        Args:
            carousel: The carousel to check
            verbose: Whether to print detailed report

        Returns:
            Dict with quality results
        """
        results = self.quality_checker.run_all_checks(carousel)

        if verbose:
            report = self.quality_checker.generate_report(results)
            print(report)

        return results

    def save_quality_report(self, carousel: Carousel, output_dir: Path) -> Path:
        """
        Save quality report to the output directory.

        Args:
            carousel: The carousel to check
            output_dir: Directory to save report

        Returns:
            Path to the saved report file
        """
        results = self.quality_checker.run_all_checks(carousel)
        report = self.quality_checker.generate_report(results)

        output_dir.mkdir(parents=True, exist_ok=True)
        report_path = output_dir / "quality-report.txt"

        with open(report_path, 'w') as f:
            f.write(report)

        return report_path

    def generate_preview(self, slide_paths: List[Path], output_dir: Path,
                         max_slides: int = 4) -> Optional[Path]:
        """
        Generate a mobile preview image showing multiple slides.

        Creates a horizontal strip of slides for quick preview.

        Args:
            slide_paths: Paths to rendered slide images
            output_dir: Directory to save preview
            max_slides: Maximum slides to include in preview

        Returns:
            Path to the preview image, or None if failed
        """
        try:
            from PIL import Image

            if not slide_paths:
                return None

            # Load and resize slides
            slides_to_show = slide_paths[:max_slides]
            images = []

            for path in slides_to_show:
                if path.exists():
                    img = Image.open(path)
                    # Resize to thumbnail for preview (300px height)
                    aspect = img.width / img.height
                    new_height = 300
                    new_width = int(new_height * aspect)
                    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    images.append(img)

            if not images:
                return None

            # Create horizontal strip
            total_width = sum(img.width for img in images) + (len(images) - 1) * 10  # 10px gap
            max_height = max(img.height for img in images)

            preview = Image.new('RGB', (total_width, max_height), (255, 255, 255))

            x_offset = 0
            for img in images:
                preview.paste(img, (x_offset, 0))
                x_offset += img.width + 10

            output_dir.mkdir(parents=True, exist_ok=True)
            preview_path = output_dir / "preview.png"
            preview.save(preview_path, "PNG")

            return preview_path

        except Exception as e:
            print(f"Warning: Could not generate preview: {e}")
            return None

    def _create_placeholder_slides(self, topic: str,
                                   slide_types: List[SlideType]) -> List[SlideContent]:
        """Create placeholder slides for a topic (until AI integration)."""
        slides = []
        account = get_account(self.config.account)

        for i, slide_type in enumerate(slide_types, 1):
            slide = SlideContent(
                slide_type=slide_type,
                slide_number=i,
                color_mode=ColorMode.DARK if slide_type in [SlideType.HOOK, SlideType.QUOTE, SlideType.CTA] else ColorMode.LIGHT
            )

            if slide_type == SlideType.HOOK:
                slide.title = topic
                slide.subtitle = "What you need to know"

            elif slide_type == SlideType.TIPS:
                slide.title = f"Tip #{i - 1}" if i > 1 else "Key Tips"
                slide.bullet_points = [
                    "First important point about this topic",
                    "Second key insight to remember",
                    "Third actionable takeaway"
                ]

            elif slide_type == SlideType.STATS:
                slide.statistic = "73%"
                slide.stat_label = "of patients benefit"
                slide.stat_context = "Based on recent clinical trials"

            elif slide_type == SlideType.MYTH:
                slide.myth_text = "Common misconception about this topic"
                slide.truth_text = "The evidence actually shows something different"

            elif slide_type == SlideType.QUOTE:
                slide.quote_text = "Expert insight that provides valuable perspective"
                slide.quote_author = "Dr. Expert, Cardiologist"

            elif slide_type == SlideType.STEPS:
                slide.title = "How to Apply This"
                slide.steps = [
                    "First step to take",
                    "Second step in the process",
                    "Final step for success"
                ]

            elif slide_type == SlideType.COMPARISON:
                slide.title = "Before vs After"
                slide.before_text = "The old approach that doesn't work"
                slide.after_text = "The new evidence-based method"

            elif slide_type == SlideType.STORY:
                slide.title = "Patient Story"
                slide.body = "A brief narrative that illustrates the key point and makes it relatable."

            elif slide_type == SlideType.DATA:
                slide.statistic = "2.3x"
                slide.stat_label = "Risk reduction"
                slide.stat_context = "Meta-analysis of 15 studies (n=50,000)"

            elif slide_type == SlideType.CTA:
                slide.cta_text = "Follow for more"
                slide.cta_handle = account['handle']

            slides.append(slide)

        return slides


    def generate_batch(self, topics: List[str], template: str = "tips_5",
                       use_ai: bool = True, parallel: bool = False) -> List[CarouselRenderResult]:
        """
        Generate multiple carousels in batch mode.

        Args:
            topics: List of topics to generate carousels for
            template: Template preset to use for all
            use_ai: Whether to use AI for content structuring
            parallel: Whether to process in parallel (experimental)

        Returns:
            List of CarouselRenderResult objects
        """
        print(f"\n{'='*60}")
        print(f"BATCH GENERATION: {len(topics)} carousels")
        print(f"Template: {template}")
        print(f"{'='*60}\n")

        results = []
        failed = []

        for i, topic in enumerate(topics, 1):
            print(f"\n[{i}/{len(topics)}] Processing: {topic}")
            print("-" * 40)

            try:
                result = self.generate_from_topic(topic, template=template, use_ai=use_ai)
                results.append(result)
                print(f"  ✓ Success: {result.output_directory}")
            except Exception as e:
                print(f"  ✗ Failed: {e}")
                failed.append({"topic": topic, "error": str(e)})

        # Summary
        print(f"\n{'='*60}")
        print(f"BATCH COMPLETE")
        print(f"  Successful: {len(results)}/{len(topics)}")
        if failed:
            print(f"  Failed: {len(failed)}")
            for f in failed:
                print(f"    - {f['topic']}: {f['error'][:50]}...")
        print(f"{'='*60}\n")

        return results

    def generate_batch_from_file(self, topics_file: Path,
                                 template: str = "tips_5",
                                 use_ai: bool = True) -> List[CarouselRenderResult]:
        """
        Generate batch from a topics file (one topic per line, or JSON array).

        Args:
            topics_file: Path to file with topics (txt or json)
            template: Template preset
            use_ai: Whether to use AI

        Returns:
            List of CarouselRenderResult objects
        """
        if topics_file.suffix == '.json':
            with open(topics_file, 'r') as f:
                data = json.load(f)
                if isinstance(data, list):
                    topics = data
                else:
                    topics = data.get('topics', [])
        else:
            # Text file - one topic per line
            with open(topics_file, 'r') as f:
                topics = [line.strip() for line in f if line.strip() and not line.startswith('#')]

        return self.generate_batch(topics, template=template, use_ai=use_ai)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Generate Instagram carousels with AI-powered content structuring'
    )
    parser.add_argument('input', nargs='?', help='Topic string, JSON file path, or text file')
    parser.add_argument('-t', '--template', default='tips_5',
                       choices=list(TEMPLATE_PRESETS.keys()),
                       help='Template preset (default: tips_5)')
    parser.add_argument('-a', '--account', type=int, default=1, choices=[1, 2],
                       help='Account: 1=@heartdocshailesh, 2=@dr.shailesh.singh')
    parser.add_argument('-r', '--ratio', default='4:5', choices=['4:5', '1:1'],
                       help='Aspect ratio (default: 4:5)')
    parser.add_argument('--both-ratios', action='store_true',
                       help='Generate both 4:5 and 1:1 outputs')
    parser.add_argument('-o', '--output', help='Output directory')
    parser.add_argument('--no-ai', action='store_true',
                       help='Skip AI content structuring')
    parser.add_argument('--quality-report', action='store_true',
                       help='Generate detailed quality report')
    parser.add_argument('--preview', action='store_true',
                       help='Generate preview image strip')
    parser.add_argument('--no-quality', action='store_true',
                       help='Skip quality checks')
    parser.add_argument('--batch', type=str, metavar='FILE',
                       help='Batch mode: process topics from file (one per line, or JSON array)')
    parser.add_argument('--no-caption', action='store_true',
                       help='Skip caption/hashtag generation')

    args = parser.parse_args()

    # Configure
    config = CarouselConfig(
        account=args.account,
        aspect_ratio=AspectRatio.INSTAGRAM_4X5 if args.ratio == '4:5' else AspectRatio.SQUARE_1X1,
        output_dir=Path(args.output) if args.output else None,
        check_text_density=not args.no_quality,
        check_anti_ai=not args.no_quality,
        generate_both_ratios=args.both_ratios,
        generate_caption=not args.no_caption,
        generate_hashtags=not args.no_caption
    )

    generator = CarouselGenerator(config)

    # Batch mode
    if args.batch:
        batch_path = Path(args.batch)
        if not batch_path.exists():
            print(f"Error: Batch file not found: {args.batch}")
            return
        results = generator.generate_batch_from_file(
            batch_path,
            template=args.template,
            use_ai=not args.no_ai
        )
        print(f"\nGenerated {len(results)} carousels in batch mode")
        return

    # Single mode - requires input
    if not args.input:
        parser.print_help()
        print("\nError: Input required (topic, JSON file, or use --batch)")
        return

    # Determine input type
    input_path = Path(args.input)

    if input_path.exists() and input_path.suffix == '.json':
        result = generator.generate_from_json(input_path)
    elif input_path.exists() and input_path.suffix in ['.txt', '.md']:
        with open(input_path, 'r') as f:
            content = f.read()
        result = generator.generate_from_longform(content)
    else:
        # Treat as topic string
        result = generator.generate_from_topic(
            args.input,
            template=args.template,
            use_ai=not args.no_ai
        )

    print(f"\nGenerated {len(result.slides)} slides to {result.output_directory}")

    # Generate quality report if requested
    if args.quality_report:
        report_path = generator.save_quality_report(result.carousel, result.output_directory)
        print(f"Quality report: {report_path}")

        # Also print to console
        generator.run_quality_check(result.carousel, verbose=True)

    # Generate preview if requested
    if args.preview:
        slide_paths = [s.output_path for s in result.slides]
        preview_path = generator.generate_preview(slide_paths, result.output_directory)
        if preview_path:
            print(f"Preview: {preview_path}")


if __name__ == '__main__':
    main()
