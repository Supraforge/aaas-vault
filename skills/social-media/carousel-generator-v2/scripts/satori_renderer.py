"""
Satori Renderer - Python bridge to Node.js Satori rendering pipeline

This module provides a Python interface to the Satori-based carousel rendering
system. It maps carousel content data to Satori template data and calls the
Node.js renderer via subprocess.

Integrates with:
- models.py: SlideContent, SlideType, ColorMode
- content_structurer.py: ContentStructure
- carousel_employee.py: Main orchestration

Usage:
    from satori_renderer import SatoriRenderer

    renderer = SatoriRenderer()

    # From SlideContent objects
    from models import SlideContent, SlideType
    slide = SlideContent(slide_type=SlideType.HOOK, title="5 Myths", subtitle="Exposed")
    result = renderer.render_slide_content(slide, 1, 10)

    # From ContentStructure
    from content_structurer import ContentStructurer
    structure = ContentStructurer().structure_from_topic("statins")
    results = renderer.render_structure(structure)
"""

import json
import os
import subprocess
import time
from pathlib import Path
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, asdict

# Import models for type hints and enum values
try:
    from .models import SlideContent, SlideType, ColorMode, SlideRenderResult
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False
    SlideContent = None
    SlideType = None
    ColorMode = None
    SlideRenderResult = None


# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
VISUAL_SYSTEM_DIR = PROJECT_ROOT.parent / "visual-design-system"
SATORI_DIR = VISUAL_SYSTEM_DIR / "satori"
RENDERER_PATH = SATORI_DIR / "renderer.js"

# Default dimensions for Instagram carousels
CAROUSEL_DIMENSIONS = {
    "instagram4x5": {"width": 1080, "height": 1350},
    "instagram1x1": {"width": 1080, "height": 1080},
    "default": {"width": 1080, "height": 1350},
}

# Template mapping from slide types to Satori templates
TEMPLATE_MAPPING = {
    "hook": "carousel-hook",
    "myth": "carousel-myth",
    "stat": "carousel-stat",
    "stats": "carousel-stat",
    "tips": "carousel-tips",
    "tip": "carousel-tips",
    "cta": "carousel-cta",
    "calltoaction": "carousel-cta",
    # Fallbacks
    "comparison": "comparison",
    "process": "process-flow",
    "trial": "trial-summary",
    "finding": "key-finding",
}


@dataclass
class SlideData:
    """Data structure for a single carousel slide."""
    slide_type: str
    data: Dict[str, Any]
    slide_number: Optional[int] = None
    total_slides: Optional[int] = None


@dataclass
class RenderResult:
    """Result of rendering a slide."""
    success: bool
    output_path: Optional[str] = None
    error: Optional[str] = None
    size: Optional[int] = None


class SatoriRenderer:
    """
    Python bridge to the Satori rendering pipeline.

    Provides methods to render individual slides or complete carousels
    using the Satori-based templates.
    """

    def __init__(
        self,
        output_dir: Optional[Path] = None,
        dimensions: str = "instagram4x5",
        footer_name: str = "Dr. Shailesh Singh",
        footer_handle: str = "@heartdocshailesh",
    ):
        """
        Initialize the Satori renderer.

        Args:
            output_dir: Directory to save rendered images
            dimensions: Dimension preset (instagram4x5, instagram1x1)
            footer_name: Name to show in footer
            footer_handle: Social media handle for footer
        """
        self.output_dir = output_dir or PROJECT_ROOT / "outputs"
        self.output_dir.mkdir(parents=True, exist_ok=True)

        dims = CAROUSEL_DIMENSIONS.get(dimensions, CAROUSEL_DIMENSIONS["default"])
        self.width = dims["width"]
        self.height = dims["height"]

        self.footer_name = footer_name
        self.footer_handle = footer_handle

        # Verify Node.js renderer exists
        if not RENDERER_PATH.exists():
            raise FileNotFoundError(f"Satori renderer not found at {RENDERER_PATH}")

    def _get_template_name(self, slide_type: str) -> str:
        """Map slide type to Satori template name."""
        normalized = slide_type.lower().replace("_", "").replace("-", "").replace("slide", "")
        return TEMPLATE_MAPPING.get(normalized, "carousel-stat")

    def _prepare_hook_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Prepare data for carousel-hook template."""
        return {
            "headline": data.get("headline") or data.get("title", ""),
            "subtitle": data.get("subtitle") or data.get("subheadline", ""),
            "icon": data.get("icon", "heart"),
            "theme": data.get("theme", "dark"),
        }

    def _prepare_myth_data(
        self, data: Dict[str, Any], slide_number: int, total_slides: int
    ) -> Dict[str, Any]:
        """Prepare data for carousel-myth template."""
        return {
            "slideNumber": slide_number,
            "totalSlides": total_slides,
            "myth": data.get("myth", ""),
            "truth": data.get("truth") or data.get("fact", ""),
            "source": data.get("source", ""),
            "showFooter": data.get("show_footer", True),
            "footerName": self.footer_name,
            "footerHandle": self.footer_handle,
        }

    def _prepare_stat_data(
        self, data: Dict[str, Any], slide_number: int, total_slides: int
    ) -> Dict[str, Any]:
        """Prepare data for carousel-stat template."""
        return {
            "stat": data.get("stat") or data.get("value", ""),
            "label": data.get("label") or data.get("title", ""),
            "context": data.get("context") or data.get("sublabel", ""),
            "source": data.get("source", ""),
            "icon": data.get("icon", "chart-up"),
            "theme": data.get("theme", "primary"),
            "slideNumber": slide_number,
            "totalSlides": total_slides,
            "showFooter": data.get("show_footer", True),
            "footerName": self.footer_name,
            "footerHandle": self.footer_handle,
        }

    def _prepare_tips_data(
        self, data: Dict[str, Any], slide_number: int, total_slides: int
    ) -> Dict[str, Any]:
        """Prepare data for carousel-tips template."""
        tips = data.get("tips") or data.get("items") or []

        # Normalize tips format
        normalized_tips = []
        for i, tip in enumerate(tips):
            if isinstance(tip, str):
                normalized_tips.append({
                    "number": i + 1,
                    "text": tip,
                    "icon": "",
                })
            elif isinstance(tip, dict):
                normalized_tips.append({
                    "number": tip.get("number", i + 1),
                    "text": tip.get("text") or tip.get("content", ""),
                    "icon": tip.get("icon", ""),
                })

        return {
            "title": data.get("title", "Tips"),
            "tips": normalized_tips,
            "theme": data.get("theme", "light"),
            "slideNumber": slide_number,
            "totalSlides": total_slides,
            "showFooter": data.get("show_footer", True),
            "footerName": self.footer_name,
            "footerHandle": self.footer_handle,
        }

    def _prepare_cta_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Prepare data for carousel-cta template."""
        return {
            "name": data.get("name") or self.footer_name,
            "credentials": data.get("credentials", "Cardiologist | Evidence-Based Medicine"),
            "handle": data.get("handle") or self.footer_handle,
            "valueProposition": data.get("value_proposition") or data.get("message", ""),
            "followerCount": data.get("follower_count", ""),
            "ctaText": data.get("cta_text", "Follow for more"),
            "theme": data.get("theme", "dark"),
        }

    def _prepare_template_data(
        self,
        slide: SlideData,
    ) -> Dict[str, Any]:
        """Prepare template data based on slide type."""
        slide_type = slide.slide_type.lower()
        data = slide.data
        slide_number = slide.slide_number or 1
        total_slides = slide.total_slides or 1

        if "hook" in slide_type:
            return self._prepare_hook_data(data)
        elif "myth" in slide_type:
            return self._prepare_myth_data(data, slide_number, total_slides)
        elif "stat" in slide_type:
            return self._prepare_stat_data(data, slide_number, total_slides)
        elif "tip" in slide_type:
            return self._prepare_tips_data(data, slide_number, total_slides)
        elif "cta" in slide_type or "call" in slide_type:
            return self._prepare_cta_data(data)
        else:
            # Default to stat template
            return self._prepare_stat_data(data, slide_number, total_slides)

    def render_slide(
        self,
        slide: Union[SlideData, Dict[str, Any]],
        output_filename: Optional[str] = None,
    ) -> RenderResult:
        """
        Render a single slide to PNG.

        Args:
            slide: SlideData object or dict with slide_type and data
            output_filename: Optional filename for output (without extension)

        Returns:
            RenderResult with success status and output path
        """
        # Convert dict to SlideData if needed
        if isinstance(slide, dict):
            slide = SlideData(
                slide_type=slide.get("slide_type", "stat"),
                data=slide.get("data", {}),
                slide_number=slide.get("slide_number"),
                total_slides=slide.get("total_slides"),
            )

        # Get template name and prepare data
        template_name = self._get_template_name(slide.slide_type)
        template_data = self._prepare_template_data(slide)

        # Prepare output path
        if output_filename is None:
            output_filename = f"slide_{slide.slide_number or 1}"
        output_path = self.output_dir / f"{output_filename}.png"

        # Build command
        input_json = json.dumps({
            "template": template_name,
            "data": template_data,
            "output": str(output_path),
            "width": self.width,
            "height": self.height,
        })

        try:
            # Run Node.js renderer
            result = subprocess.run(
                ["node", str(RENDERER_PATH), "--stdin"],
                input=input_json,
                capture_output=True,
                text=True,
                timeout=60,
                cwd=str(SATORI_DIR),
            )

            if result.returncode == 0:
                output = json.loads(result.stdout)
                if output.get("success"):
                    return RenderResult(
                        success=True,
                        output_path=output.get("output"),
                        size=output.get("size"),
                    )
                else:
                    return RenderResult(
                        success=False,
                        error=output.get("error", "Unknown error"),
                    )
            else:
                return RenderResult(
                    success=False,
                    error=result.stderr or "Renderer failed",
                )

        except subprocess.TimeoutExpired:
            return RenderResult(success=False, error="Rendering timed out")
        except json.JSONDecodeError as e:
            return RenderResult(success=False, error=f"Invalid JSON response: {e}")
        except Exception as e:
            return RenderResult(success=False, error=str(e))

    def render_carousel(
        self,
        slides: List[Union[SlideData, Dict[str, Any]]],
        carousel_name: Optional[str] = None,
    ) -> List[RenderResult]:
        """
        Render a complete carousel (multiple slides).

        Args:
            slides: List of SlideData objects or dicts
            carousel_name: Optional name prefix for output files

        Returns:
            List of RenderResult objects for each slide
        """
        results = []
        total_slides = len(slides)
        prefix = carousel_name or "carousel"

        for i, slide in enumerate(slides):
            # Convert dict to SlideData if needed
            if isinstance(slide, dict):
                slide = SlideData(
                    slide_type=slide.get("slide_type", "stat"),
                    data=slide.get("data", {}),
                    slide_number=i + 1,
                    total_slides=total_slides,
                )
            else:
                # Update slide numbers
                slide.slide_number = i + 1
                slide.total_slides = total_slides

            output_filename = f"{prefix}_slide_{i + 1:02d}"
            result = self.render_slide(slide, output_filename)
            results.append(result)

        return results


    # =========================================================================
    # SlideContent Integration (models.py)
    # =========================================================================

    def _slide_content_to_template_data(
        self,
        slide: Any,  # SlideContent from models.py
        slide_number: int,
        total_slides: int,
    ) -> tuple:
        """
        Convert SlideContent object to (template_name, template_data) tuple.

        Args:
            slide: SlideContent object from models.py
            slide_number: Current slide number
            total_slides: Total number of slides

        Returns:
            Tuple of (template_name, template_data_dict)
        """
        slide_type = slide.slide_type.value if hasattr(slide.slide_type, 'value') else str(slide.slide_type)

        # Determine theme based on color mode
        color_mode = slide.color_mode.value if hasattr(slide.color_mode, 'value') else str(slide.color_mode)
        theme = "dark" if color_mode == "dark" else "light"

        # Common footer data
        footer_data = {
            "showFooter": True,
            "footerName": self.footer_name,
            "footerHandle": self.footer_handle,
        }

        # Map slide types to templates
        if slide_type == "hook":
            return "carousel-hook", {
                "headline": slide.title or "Evidence-Based Insights",
                "subtitle": slide.subtitle or "",
                "icon": slide.icon_name or "heart",
                "theme": theme,
            }

        elif slide_type == "myth":
            return "carousel-myth", {
                "slideNumber": slide_number,
                "totalSlides": total_slides,
                "myth": slide.myth_text or "",
                "truth": slide.truth_text or "",
                "source": "",  # Add source if available
                **footer_data,
            }

        elif slide_type in ["stats", "data"]:
            return "carousel-stat", {
                "stat": slide.statistic or "",
                "label": slide.stat_label or "",
                "context": slide.stat_context or "",
                "source": "",
                "icon": slide.icon_name or "chart-up",
                "theme": "success" if slide_type == "stats" else "primary",
                "slideNumber": slide_number,
                "totalSlides": total_slides,
                **footer_data,
            }

        elif slide_type == "tips":
            # Single tip slide - convert to tips format
            tips = []
            if slide.bullet_points:
                for i, point in enumerate(slide.bullet_points):
                    tips.append({
                        "number": i + 1,
                        "text": point,
                        "icon": "",
                    })
            elif slide.title:
                tips.append({
                    "number": 1,
                    "text": slide.title,
                    "icon": slide.icon_name or "",
                })

            return "carousel-tips", {
                "title": slide.title or "Key Point",
                "tips": tips if tips else [{"number": 1, "text": "Important insight", "icon": ""}],
                "theme": theme,
                "slideNumber": slide_number,
                "totalSlides": total_slides,
                **footer_data,
            }

        elif slide_type == "steps":
            # Steps slide - convert to tips format with numbered steps
            tips = []
            if slide.steps:
                for i, step in enumerate(slide.steps):
                    tips.append({
                        "number": i + 1,
                        "text": step,
                        "icon": "",
                    })

            return "carousel-tips", {
                "title": slide.title or "Action Steps",
                "tips": tips if tips else [{"number": 1, "text": "Take action", "icon": ""}],
                "theme": theme,
                "slideNumber": slide_number,
                "totalSlides": total_slides,
                **footer_data,
            }

        elif slide_type == "quote":
            # Quote slide - use stat template with quote styling
            return "carousel-stat", {
                "stat": '""',  # Quote marks
                "label": slide.quote_text or "",
                "context": f"— {slide.quote_author}" if slide.quote_author else "",
                "source": "",
                "icon": "star",
                "theme": "dark",
                "slideNumber": slide_number,
                "totalSlides": total_slides,
                **footer_data,
            }

        elif slide_type == "comparison":
            # Comparison - use myth template structure
            return "carousel-myth", {
                "slideNumber": slide_number,
                "totalSlides": total_slides,
                "myth": slide.before_text or "Common Approach",
                "truth": slide.after_text or "Better Approach",
                "source": "",
                **footer_data,
            }

        elif slide_type == "story":
            # Story slide - use stat template
            return "carousel-stat", {
                "stat": slide.title or "Real Story",
                "label": slide.body or "",
                "context": "",
                "source": "",
                "icon": "heart",
                "theme": "primary",
                "slideNumber": slide_number,
                "totalSlides": total_slides,
                **footer_data,
            }

        elif slide_type == "cta":
            return "carousel-cta", {
                "name": self.footer_name,
                "credentials": "Cardiologist | Evidence-Based Medicine",
                "handle": slide.cta_handle or self.footer_handle,
                "valueProposition": slide.cta_text or "Follow for more evidence-based content",
                "followerCount": "",
                "ctaText": "Follow for more",
                "theme": "dark",
            }

        else:
            # Default to tips template
            return "carousel-tips", {
                "title": slide.title or "Key Point",
                "tips": [{"number": 1, "text": slide.body or slide.title or "", "icon": ""}],
                "theme": theme,
                "slideNumber": slide_number,
                "totalSlides": total_slides,
                **footer_data,
            }

    def render_slide_content(
        self,
        slide: Any,  # SlideContent
        slide_number: int,
        total_slides: int,
        output_filename: Optional[str] = None,
    ) -> "SlideRenderResult":
        """
        Render a SlideContent object to PNG.

        Args:
            slide: SlideContent object from models.py
            slide_number: Current slide number
            total_slides: Total slides in carousel
            output_filename: Optional filename (without extension)

        Returns:
            SlideRenderResult with output path and metrics
        """
        start_time = time.time()

        # Convert SlideContent to template data
        template_name, template_data = self._slide_content_to_template_data(
            slide, slide_number, total_slides
        )

        # Prepare output path
        if output_filename is None:
            output_filename = f"slide_{slide_number:02d}"
        output_path = self.output_dir / f"{output_filename}.png"

        # Build command
        input_json = json.dumps({
            "template": template_name,
            "data": template_data,
            "output": str(output_path),
            "width": self.width,
            "height": self.height,
        })

        try:
            # Run Node.js renderer
            result = subprocess.run(
                ["node", str(RENDERER_PATH), "--stdin"],
                input=input_json,
                capture_output=True,
                text=True,
                timeout=60,
                cwd=str(SATORI_DIR),
            )

            render_time = (time.time() - start_time) * 1000  # ms

            if result.returncode == 0:
                output = json.loads(result.stdout)
                if output.get("success"):
                    # Return SlideRenderResult if available
                    if MODELS_AVAILABLE and SlideRenderResult:
                        return SlideRenderResult(
                            slide_number=slide_number,
                            output_path=Path(output.get("output")),
                            width=self.width,
                            height=self.height,
                            render_time_ms=render_time,
                            renderer_used="satori",
                            warnings=None,
                        )
                    else:
                        return RenderResult(
                            success=True,
                            output_path=output.get("output"),
                            size=output.get("size"),
                        )

            # Error case
            error_msg = result.stderr or "Renderer failed"
            if MODELS_AVAILABLE and SlideRenderResult:
                return SlideRenderResult(
                    slide_number=slide_number,
                    output_path=output_path,
                    width=self.width,
                    height=self.height,
                    render_time_ms=render_time,
                    renderer_used="satori",
                    warnings=[error_msg],
                )
            return RenderResult(success=False, error=error_msg)

        except Exception as e:
            render_time = (time.time() - start_time) * 1000
            if MODELS_AVAILABLE and SlideRenderResult:
                return SlideRenderResult(
                    slide_number=slide_number,
                    output_path=output_path,
                    width=self.width,
                    height=self.height,
                    render_time_ms=render_time,
                    renderer_used="satori",
                    warnings=[str(e)],
                )
            return RenderResult(success=False, error=str(e))

    def render_structure(
        self,
        structure: Any,  # ContentStructure from content_structurer.py
        carousel_name: Optional[str] = None,
    ) -> List:
        """
        Render a complete ContentStructure to PNG files.

        Args:
            structure: ContentStructure from content_structurer.py
            carousel_name: Optional name prefix for output files

        Returns:
            List of SlideRenderResult objects
        """
        results = []
        total_slides = len(structure.slides)
        prefix = carousel_name or structure.topic.replace(" ", "-").lower()[:20]

        for i, slide in enumerate(structure.slides):
            output_filename = f"{prefix}_slide_{i + 1:02d}"
            result = self.render_slide_content(
                slide,
                slide_number=i + 1,
                total_slides=total_slides,
                output_filename=output_filename,
            )
            results.append(result)

        return results


def render_from_content_database(
    topic: str,
    content_db: Any,
    output_dir: Optional[Path] = None,
) -> List[RenderResult]:
    """
    Convenience function to render a carousel from content database.

    Args:
        topic: Topic name from content database
        content_db: ContentDatabase instance
        output_dir: Optional output directory

    Returns:
        List of RenderResult objects
    """
    # This would integrate with content_database.py
    # For now, just return empty list as placeholder
    renderer = SatoriRenderer(output_dir=output_dir)
    return []


# CLI for testing
if __name__ == "__main__":
    import sys

    # Test rendering
    renderer = SatoriRenderer()

    # Test hook slide
    test_hook = SlideData(
        slide_type="hook",
        data={
            "headline": "5 Statin Myths Exposed",
            "subtitle": "What every patient needs to know",
            "icon": "pill",
            "theme": "dark",
        },
    )

    # Test myth slide
    test_myth = SlideData(
        slide_type="myth",
        data={
            "myth": "Statins cause muscle pain in everyone",
            "truth": "Only 5-10% experience muscle symptoms, and it's usually mild",
            "source": "Lancet 2022",
        },
        slide_number=2,
        total_slides=10,
    )

    # Test stat slide
    test_stat = SlideData(
        slide_type="stat",
        data={
            "stat": "26%",
            "label": "Mortality Reduction",
            "context": "HR 0.74, 95% CI 0.65-0.85",
            "source": "PARADIGM-HF Trial",
            "icon": "chart-up",
        },
        slide_number=3,
        total_slides=10,
    )

    # Test tips slide
    test_tips = SlideData(
        slide_type="tips",
        data={
            "title": "3 Ways to Protect Your Heart",
            "tips": [
                {"number": 1, "text": "Take statins as prescribed", "icon": "pill"},
                {"number": 2, "text": "Monitor your cholesterol yearly", "icon": "chart"},
                {"number": 3, "text": "Exercise 150 min/week", "icon": "running"},
            ],
        },
        slide_number=5,
        total_slides=10,
    )

    # Test CTA slide
    test_cta = SlideData(
        slide_type="cta",
        data={
            "name": "Dr. Shailesh Singh",
            "credentials": "Cardiologist | Evidence-Based Medicine",
            "handle": "@heartdocshailesh",
            "value_proposition": "Follow for myth-busting cardiology content",
            "follower_count": "50K+",
            "theme": "dark",
        },
    )

    test_slides = [test_hook, test_myth, test_stat, test_tips, test_cta]

    print("Testing Satori Carousel Renderer...")
    print(f"Output directory: {renderer.output_dir}")
    print("-" * 50)

    results = renderer.render_carousel(test_slides, "test_carousel")

    for i, result in enumerate(results):
        status = "SUCCESS" if result.success else "FAILED"
        print(f"Slide {i + 1}: {status}")
        if result.success:
            print(f"  Output: {result.output_path}")
            print(f"  Size: {result.size} bytes")
        else:
            print(f"  Error: {result.error}")

    print("-" * 50)
    success_count = sum(1 for r in results if r.success)
    print(f"Total: {success_count}/{len(results)} slides rendered successfully")
