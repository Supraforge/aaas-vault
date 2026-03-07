#!/usr/bin/env python3
"""
Unified Batch Generator - Generate All Visual Content Types

Generates multiple visual outputs from a single topic or content source.
Routes to the appropriate rendering tool based on content type.

Usage:
    python batch_generator.py --topic "Statin therapy" --output-dir ./outputs/statin/
    python batch_generator.py --content article.txt --types infographic,pdf,carousel
    python batch_generator.py --topic "SGLT2 inhibitors" --all

Outputs:
    - Infographics (Satori): stat cards, comparisons, key findings
    - PDFs (react-pdf): newsletters, editorials, trial summaries
    - Carousel slides (Satori): Instagram-ready 1080x1350 images
    - Charts (Plotly): forest plots, Kaplan-Meier, bar charts
    - Diagrams (svg_diagrams): flowcharts, process flows
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

# Add parent directories to path
SCRIPT_DIR = Path(__file__).parent.resolve()
VISUAL_SYSTEM_DIR = SCRIPT_DIR.parent
sys.path.insert(0, str(VISUAL_SYSTEM_DIR))

from tokens.index import get_color, get_accessible_pair


class BatchGenerator:
    """Unified batch generator for all visual content types."""

    # Available output types
    OUTPUT_TYPES = {
        "infographic": "Satori infographics (stat cards, comparisons)",
        "pdf": "Publication-grade PDFs (newsletter, editorial, trial summary)",
        "carousel": "Instagram carousel slides",
        "chart": "Plotly charts (forest plot, Kaplan-Meier)",
        "diagram": "SVG diagrams (flowcharts, process flows)",
    }

    def __init__(self, output_dir: Path | str = None):
        """Initialize the batch generator.

        Args:
            output_dir: Base output directory (default: visual-design-system/outputs/batch/)
        """
        self.visual_system_dir = VISUAL_SYSTEM_DIR
        self.output_dir = Path(output_dir) if output_dir else VISUAL_SYSTEM_DIR / "outputs" / "batch"
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Track generated outputs
        self.generated: List[Dict[str, Any]] = []

    def _run_command(self, cmd: List[str], cwd: Path = None) -> subprocess.CompletedProcess:
        """Run a shell command and return the result."""
        return subprocess.run(
            cmd,
            cwd=cwd or self.visual_system_dir,
            capture_output=True,
            text=True,
        )

    def generate_infographic(
        self,
        template: str,
        data: Dict[str, Any],
        output_name: str,
    ) -> Dict[str, Any]:
        """Generate a Satori infographic.

        Args:
            template: Template name (stat-card, comparison, process-flow, etc.)
            data: Template data
            output_name: Output filename (without extension)

        Returns:
            Result dictionary with success status and path
        """
        output_path = self.output_dir / f"{output_name}.png"
        satori_dir = self.visual_system_dir / "satori"

        cmd = [
            "node", "renderer.js",
            "--template", template,
            "--data", json.dumps(data),
            "-o", str(output_path),
        ]

        result = self._run_command(cmd, satori_dir)

        if result.returncode == 0:
            self.generated.append({
                "type": "infographic",
                "template": template,
                "path": str(output_path),
                "size": output_path.stat().st_size if output_path.exists() else 0,
            })
            return {"success": True, "path": str(output_path)}
        else:
            return {"success": False, "error": result.stderr}

    def generate_pdf(
        self,
        template: str,
        data: Dict[str, Any],
        output_name: str,
    ) -> Dict[str, Any]:
        """Generate a react-pdf document.

        Args:
            template: Template name (newsletter, editorial, trialSummary, clinicalReport)
            data: Template data
            output_name: Output filename (without extension)

        Returns:
            Result dictionary with success status and path
        """
        output_path = self.output_dir / f"{output_name}.pdf"
        react_pdf_dir = self.visual_system_dir / "react-pdf"

        cmd = [
            "node", "dist/renderer.js",
            "--template", template,
            "--data", json.dumps(data),
            "--output", str(output_path),
        ]

        result = self._run_command(cmd, react_pdf_dir)

        if result.returncode == 0:
            try:
                output_data = json.loads(result.stdout)
                self.generated.append({
                    "type": "pdf",
                    "template": template,
                    "path": str(output_path),
                    "size": output_data.get("size", 0),
                })
                return {"success": True, "path": str(output_path)}
            except json.JSONDecodeError:
                return {"success": False, "error": "Invalid JSON output"}
        else:
            return {"success": False, "error": result.stderr}

    def generate_carousel_slide(
        self,
        template: str,
        data: Dict[str, Any],
        output_name: str,
    ) -> Dict[str, Any]:
        """Generate a carousel slide (1080x1350).

        Args:
            template: Carousel template (carousel-hook, carousel-myth, etc.)
            data: Slide data
            output_name: Output filename (without extension)

        Returns:
            Result dictionary with success status and path
        """
        # Carousel templates use Satori with 1080x1350 dimensions
        output_path = self.output_dir / f"{output_name}.png"
        satori_dir = self.visual_system_dir / "satori"

        cmd = [
            "node", "renderer.js",
            "--template", template,
            "--data", json.dumps(data),
            "-o", str(output_path),
        ]

        result = self._run_command(cmd, satori_dir)

        if result.returncode == 0:
            self.generated.append({
                "type": "carousel",
                "template": template,
                "path": str(output_path),
                "size": output_path.stat().st_size if output_path.exists() else 0,
            })
            return {"success": True, "path": str(output_path)}
        else:
            return {"success": False, "error": result.stderr}

    def generate_from_topic(
        self,
        topic: str,
        types: List[str] = None,
        author: str = "Dr. Shailesh Singh",
    ) -> Dict[str, Any]:
        """Generate multiple outputs from a topic.

        Args:
            topic: The topic to generate content for
            types: List of output types to generate (default: all)
            author: Author name for PDFs

        Returns:
            Summary of all generated outputs
        """
        types = types or list(self.OUTPUT_TYPES.keys())
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        topic_slug = topic.lower().replace(" ", "_")[:30]

        results = {
            "topic": topic,
            "timestamp": timestamp,
            "outputs": [],
            "errors": [],
        }

        # Generate infographics
        if "infographic" in types:
            # Stat card
            result = self.generate_infographic(
                "stat-card",
                {"value": "N/A", "label": f"{topic} Key Statistic", "source": "Research data"},
                f"{topic_slug}_stat_{timestamp}",
            )
            if result["success"]:
                results["outputs"].append(result)
            else:
                results["errors"].append({"type": "infographic", "error": result["error"]})

            # Key finding
            result = self.generate_infographic(
                "key-finding",
                {"title": f"Key Finding: {topic}", "finding": f"Important insight about {topic}", "evidence": "Based on clinical evidence"},
                f"{topic_slug}_finding_{timestamp}",
            )
            if result["success"]:
                results["outputs"].append(result)
            else:
                results["errors"].append({"type": "infographic", "error": result["error"]})

        # Generate PDF
        if "pdf" in types:
            result = self.generate_pdf(
                "newsletter",
                {
                    "title": f"{topic}: What You Need to Know",
                    "subtitle": "Evidence-based insights",
                    "author": author,
                    "sections": [
                        {"title": "Overview", "content": f"This newsletter covers key aspects of {topic}."},
                        {"title": "Key Points", "content": f"Important considerations for {topic} in clinical practice."},
                    ],
                    "keyTakeaways": [
                        f"Understanding {topic} is essential",
                        "Evidence-based approach is key",
                        "Consult guidelines for recommendations",
                    ],
                },
                f"{topic_slug}_newsletter_{timestamp}",
            )
            if result["success"]:
                results["outputs"].append(result)
            else:
                results["errors"].append({"type": "pdf", "error": result["error"]})

        # Generate carousel slides
        if "carousel" in types:
            # Hook slide
            result = self.generate_carousel_slide(
                "carousel-hook",
                {"title": f"What Every Cardiologist Should Know About {topic}", "subtitle": "Swipe to learn more"},
                f"{topic_slug}_slide_hook_{timestamp}",
            )
            if result["success"]:
                results["outputs"].append(result)
            else:
                results["errors"].append({"type": "carousel", "error": result["error"]})

            # CTA slide
            result = self.generate_carousel_slide(
                "carousel-cta",
                {"handle": "@heartdocshailesh", "action": "Follow for more cardiology insights"},
                f"{topic_slug}_slide_cta_{timestamp}",
            )
            if result["success"]:
                results["outputs"].append(result)
            else:
                results["errors"].append({"type": "carousel", "error": result["error"]})

        return results

    def get_summary(self) -> Dict[str, Any]:
        """Get a summary of all generated outputs."""
        return {
            "total_outputs": len(self.generated),
            "output_directory": str(self.output_dir),
            "by_type": {
                output_type: [g for g in self.generated if g["type"] == output_type]
                for output_type in self.OUTPUT_TYPES.keys()
            },
            "total_size_bytes": sum(g.get("size", 0) for g in self.generated),
        }


def main():
    """CLI for batch generator."""
    parser = argparse.ArgumentParser(
        description="Generate all visual content types from a topic",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python batch_generator.py --topic "Statin therapy"
    python batch_generator.py --topic "SGLT2 inhibitors" --types infographic,pdf
    python batch_generator.py --topic "Heart failure" --output-dir ./hf-outputs/
    python batch_generator.py --list-types
        """,
    )
    parser.add_argument("--topic", "-t", type=str, help="Topic to generate content for")
    parser.add_argument("--types", type=str, help="Comma-separated list of output types")
    parser.add_argument("--output-dir", "-o", type=str, help="Output directory")
    parser.add_argument("--author", type=str, default="Dr. Shailesh Singh", help="Author name for PDFs")
    parser.add_argument("--list-types", action="store_true", help="List available output types")
    parser.add_argument("--all", action="store_true", help="Generate all output types")

    args = parser.parse_args()

    if args.list_types:
        print("Available output types:")
        for name, desc in BatchGenerator.OUTPUT_TYPES.items():
            print(f"  {name}: {desc}")
        return

    if not args.topic:
        parser.error("--topic is required")

    # Parse types
    types = None
    if args.types:
        types = [t.strip() for t in args.types.split(",")]
        invalid = [t for t in types if t not in BatchGenerator.OUTPUT_TYPES]
        if invalid:
            parser.error(f"Invalid types: {invalid}. Use --list-types to see available types.")
    elif args.all:
        types = list(BatchGenerator.OUTPUT_TYPES.keys())

    # Generate
    generator = BatchGenerator(output_dir=args.output_dir)
    results = generator.generate_from_topic(args.topic, types=types, author=args.author)

    # Print results
    print(f"\n{'='*60}")
    print(f"Batch Generation Complete: {args.topic}")
    print(f"{'='*60}")
    print(f"Output directory: {generator.output_dir}")
    print(f"Generated: {len(results['outputs'])} outputs")
    print(f"Errors: {len(results['errors'])}")

    if results["outputs"]:
        print("\nGenerated files:")
        for output in results["outputs"]:
            print(f"  ✓ {output['path']}")

    if results["errors"]:
        print("\nErrors:")
        for error in results["errors"]:
            print(f"  ✗ {error['type']}: {error['error'][:100]}...")

    # Summary
    summary = generator.get_summary()
    print(f"\nTotal size: {summary['total_size_bytes'] / 1024:.1f} KB")


if __name__ == "__main__":
    main()
