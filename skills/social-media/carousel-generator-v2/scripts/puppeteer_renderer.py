#!/usr/bin/env python3
"""
Puppeteer-based Carousel Renderer

Uses a React + Puppeteer pipeline to render high-quality carousel slides.
This replaces the Satori-based renderer which had issues with emoji rendering.

Usage:
    from puppeteer_renderer import PuppeteerRenderer

    renderer = PuppeteerRenderer()
    slides = [
        {
            "type": "hook",
            "data": {
                "slideNumber": 1,
                "totalSlides": 6,
                "headline": "5 Statin Myths Debunked",
                "subtitle": "What the science says",
                "icon": "Pill",
                "theme": "teal"
            }
        },
        # ... more slides
    ]
    output_paths = renderer.render_carousel(slides, output_dir="./output")
"""

import json
import os
import subprocess
import tempfile
import time
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional, Union

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


DIMENSIONS = {
    "square": {"width": 1080, "height": 1080},
    "portrait": {"width": 1080, "height": 1350},
}


class PuppeteerRenderer:
    """Renders carousel slides using React + Puppeteer."""

    def __init__(self, renderer_dir: Optional[str] = None, dimensions: str = "portrait", account: int = 1):
        """
        Initialize the renderer.

        Args:
            renderer_dir: Path to the renderer React project. If None, uses default location.
            dimensions: Output dimensions ("square" or "portrait").
            account: Author account to use (1 or 2). Defaults to 1.
        """
        if renderer_dir:
            self.renderer_dir = Path(renderer_dir)
        else:
            # Default to the renderer directory in this project
            self.renderer_dir = Path(__file__).parent.parent / "renderer"

        self.render_script = self.renderer_dir / "scripts" / "render.js"
        self.dimensions = dimensions if dimensions in DIMENSIONS else "square"
        self.width = DIMENSIONS[self.dimensions]["width"]
        self.height = DIMENSIONS[self.dimensions]["height"]
        self.account = account

        # Load author config
        self.author_config = self._load_author_config()

        # Verify the renderer exists
        if not self.render_script.exists():
            raise FileNotFoundError(
                f"Render script not found at {self.render_script}. "
                "Make sure npm dependencies are installed."
            )

    def _load_author_config(self) -> Dict[str, Any]:
        """Load author configuration from config file."""
        config_path = Path(__file__).parent.parent / "config" / "author-config.json"

        # Default config if file doesn't exist
        default_config = {
            "author": {
                "name": "Dr Shailesh Singh",
                "credentials": "Cardiologist | Evidence-Based Medicine",
                "photo": "assets/5e4311be9235ba207024edfb13240abe8cf20f3f.png",
                "accounts": {
                    "1": {
                        "handle": "@heartdocshailesh",
                        "platform": "Instagram",
                        "followerCount": "50K+",
                        "bio": "Follow for evidence-based cardiology insights"
                    },
                    "2": {
                        "handle": "@dr.shailesh.singh",
                        "platform": "Instagram",
                        "followerCount": "25K+",
                        "bio": "Clinical cardiology and lifestyle medicine"
                    }
                },
                "defaultAccount": "1"
            },
            "branding": {
                "tagline": "Evidence-Based Cardiology",
                "secondaryText": "New posts every week",
                "valueProposition": "Follow for myth-busting cardiology content"
            }
        }

        if config_path.exists():
            try:
                with open(config_path, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Warning: Failed to load author config: {e}. Using defaults.")
                return default_config
        else:
            return default_config

    def _generate_plotly_chart(
        self,
        chart_type: str,
        data: Dict[str, Any],
        output_path: str,
        title: str = ""
    ) -> str:
        """
        Generate a Plotly chart and save as PNG.

        Args:
            chart_type: Type of chart ('bar', 'forest', 'line', 'survival')
            data: Chart data (varies by type)
            output_path: Path to save PNG
            title: Chart title

        Returns:
            Path to the saved chart image
        """
        # Add plotly_charts.py to path
        plotly_script_dir = Path(__file__).parent.parent.parent / "cardiology-visual-system" / "scripts"
        if plotly_script_dir.exists():
            sys.path.insert(0, str(plotly_script_dir))

        try:
            from plotly_charts import (
                create_bar_chart,
                create_forest_plot,
                create_trend_line,
                create_survival_curve,
                save_chart
            )
            import pandas as pd
        except ImportError:
            print("Warning: Plotly not available. Data slides will use StatSlide template.")
            return None

        # Generate chart based on type
        fig = None

        if chart_type == "bar" and "data" in data:
            df = pd.DataFrame(data["data"])
            x = data.get("x", df.columns[0])
            y = data.get("y", df.columns[1])
            color = data.get("color", None)
            fig = create_bar_chart(df, x, y, title, color)

        elif chart_type == "forest" and "studies" in data:
            fig = create_forest_plot(
                studies=data["studies"],
                estimates=data["estimates"],
                lower_ci=data["lower_ci"],
                upper_ci=data["upper_ci"],
                title=title,
                null_value=data.get("null_value", 1.0)
            )

        elif chart_type == "line" and "data" in data:
            df = pd.DataFrame(data["data"])
            x = data.get("x", df.columns[0])
            y = data.get("y", df.columns[1])
            color = data.get("color", None)
            fig = create_trend_line(df, x, y, title, color)

        elif chart_type == "survival" and "time_data" in data:
            fig = create_survival_curve(
                time_data=data["time_data"],
                survival_data=data["survival_data"],
                group_names=data["group_names"],
                title=title
            )

        if fig:
            # Save chart at publication quality
            save_chart(fig, output_path, width=800, height=600, scale=4)
            return output_path

        return None

    def _normalize_icon_name(self, icon: Optional[str]) -> Optional[str]:
        """Normalize icon names to lucide-react PascalCase where possible."""
        if not icon:
            return None

        # Comprehensive icon lookup for Lucide icons
        # Keys are lowercase/normalized, values are PascalCase Lucide names
        lookup = {
            # Cardiology & Medical
            "heart": "Heart",
            "heartpulse": "HeartPulse",
            "hearthandshake": "HeartHandshake",
            "pill": "Pill",
            "pills": "Pill",
            "stethoscope": "Stethoscope",
            "thermometer": "Thermometer",
            "syringe": "Syringe",
            "activity": "Activity",
            "pulse": "Activity",
            "ecg": "Activity",
            "hospital": "Hospital",
            "ambulance": "Ambulance",
            "brain": "Brain",
            "bone": "Bone",
            "eye": "Eye",
            "microscope": "Microscope",

            # Charts & Data
            "chart": "TrendingUp",
            "chartup": "TrendingUp",
            "chart-up": "TrendingUp",
            "trendingup": "TrendingUp",
            "trendingdown": "TrendingDown",
            "chartbar": "BarChart3",
            "barchart": "BarChart3",
            "barchart3": "BarChart3",
            "linechart": "LineChart",
            "piechart": "PieChart",
            "areachart": "AreaChart",

            # Lifestyle & Wellness
            "running": "Activity",
            "exercise": "Dumbbell",
            "dumbbell": "Dumbbell",
            "gym": "Dumbbell",
            "weight": "Weight",
            "salad": "Salad",
            "food": "Salad",
            "apple": "Apple",
            "nutrition": "Apple",
            "coffee": "Coffee",
            "cigarette": "Cigarette",
            "smoking": "Cigarette",
            "cigaretteoff": "CigaretteOff",
            "nosmoking": "CigaretteOff",
            "bed": "Bed",
            "sleep": "Moon",
            "moon": "Moon",
            "sun": "Sun",

            # Communication
            "clock": "Clock",
            "timer": "Timer",
            "calendar": "Calendar",
            "message": "MessageCircle",
            "messagecircle": "MessageCircle",
            "messagesquare": "MessageSquare",
            "mail": "Mail",
            "phone": "Phone",
            "bell": "Bell",
            "megaphone": "Megaphone",

            # Objects & Symbols
            "quote": "Quote",
            "star": "Star",
            "shield": "Shield",
            "shieldcheck": "ShieldCheck",
            "shieldx": "ShieldX",
            "lock": "Lock",
            "unlock": "Unlock",
            "key": "Key",
            "book": "Book",
            "bookopen": "BookOpen",
            "bookmark": "Bookmark",
            "lightbulb": "Lightbulb",
            "target": "Target",
            "crosshair": "Crosshair",
            "zap": "Zap",
            "bolt": "Zap",
            "flame": "Flame",
            "fire": "Flame",
            "droplet": "Droplet",
            "water": "Droplet",
            "leaf": "Leaf",
            "flower": "Flower",

            # Actions & Status
            "check": "Check",
            "checkmark": "Check",
            "checkcircle": "CheckCircle",
            "x": "X",
            "xcircle": "XCircle",
            "alerttriangle": "AlertTriangle",
            "warning": "AlertTriangle",
            "alertcircle": "AlertCircle",
            "info": "Info",
            "helpcircle": "HelpCircle",
            "question": "HelpCircle",
            "plus": "Plus",
            "minus": "Minus",
            "refresh": "RefreshCw",
            "refreshcw": "RefreshCw",

            # Arrows
            "arrowup": "ArrowUp",
            "arrowdown": "ArrowDown",
            "arrowleft": "ArrowLeft",
            "arrowright": "ArrowRight",
            "chevronup": "ChevronUp",
            "chevrondown": "ChevronDown",
            "chevronleft": "ChevronLeft",
            "chevronright": "ChevronRight",
            "arrowupright": "ArrowUpRight",
            "externallink": "ExternalLink",

            # People & Social
            "user": "User",
            "users": "Users",
            "usercircle": "UserCircle",
            "userplus": "UserPlus",
            "usercheck": "UserCheck",
            "thumbsup": "ThumbsUp",
            "thumbsdown": "ThumbsDown",
            "share": "Share",
            "share2": "Share2",
            "instagram": "Instagram",
            "twitter": "Twitter",
            "facebook": "Facebook",
            "youtube": "Youtube",
            "linkedin": "Linkedin",

            # Files & Folders
            "file": "File",
            "filetext": "FileText",
            "folder": "Folder",
            "download": "Download",
            "upload": "Upload",
            "clipboard": "Clipboard",
            "copy": "Copy",

            # UI Elements
            "menu": "Menu",
            "grid": "Grid",
            "list": "List",
            "search": "Search",
            "filter": "Filter",
            "settings": "Settings",
            "sliders": "Sliders",
            "maximize": "Maximize",
            "minimize": "Minimize",
            "expand": "Expand",
            "shrink": "Shrink",

            # Navigation
            "home": "Home",
            "map": "Map",
            "mappin": "MapPin",
            "navigation": "Navigation",
            "compass": "Compass",
            "globe": "Globe",
        }

        normalized = icon.strip().replace(" ", "").replace("_", "").replace("-", "").lower()
        return lookup.get(normalized, icon)

    def _split_context_source(
        self,
        context: str,
        source: Optional[str] = None
    ) -> (str, Optional[str]):
        """Split context into context + source when encoded as 'context - source'."""
        if source:
            return context, source
        if not context:
            return context, source
        if " - " in context:
            left, right = context.split(" - ", 1)
            return left.strip(), right.strip()
        if " — " in context:
            left, right = context.split(" — ", 1)
            return left.strip(), right.strip()
        return context, source

    def _slide_content_to_render_data(
        self,
        slide: Any,
        slide_number: int,
        total_slides: int,
    ) -> Dict[str, Any]:
        """Convert SlideContent to renderer slide data."""
        slide_type = slide.slide_type.value if hasattr(slide.slide_type, "value") else str(slide.slide_type)
        color_mode = slide.color_mode.value if hasattr(slide.color_mode, "value") else str(slide.color_mode)
        theme = "teal" if color_mode != "dark" else "red"

        if slide_type == "hook":
            return {
                "type": "hook",
                "data": {
                    "slideNumber": slide_number,
                    "totalSlides": total_slides,
                    "headline": slide.title or "Evidence-Based Cardiology",
                    "subtitle": slide.subtitle or slide.body or "",
                    "icon": self._normalize_icon_name(slide.icon_name or "Heart"),
                    "theme": theme,
                    "dimensions": self.dimensions,
                },
            }

        if slide_type == "myth":
            return {
                "type": "myth",
                "data": {
                    "slideNumber": slide_number,
                    "totalSlides": total_slides,
                    "myth": slide.myth_text or "",
                    "truth": slide.truth_text or "",
                    "source": slide.source or "",
                    "dimensions": self.dimensions,
                },
            }

        if slide_type == "stats":
            context, source = self._split_context_source(
                slide.stat_context or slide.body or "",
                slide.source
            )
            return {
                "type": "stat",
                "data": {
                    "slideNumber": slide_number,
                    "totalSlides": total_slides,
                    "stat": slide.statistic or "",
                    "label": slide.stat_label or slide.title or "",
                    "context": context,
                    "source": source or "",
                    "icon": self._normalize_icon_name(slide.icon_name or "TrendingUp"),
                    "color": "green",
                    "dimensions": self.dimensions,
                },
            }

        if slide_type == "data":
            # Check if slide has chart data that should use Plotly
            if hasattr(slide, "chart_data") and slide.chart_data:
                # Generate Plotly chart
                chart_type = getattr(slide, "chart_type", "bar")
                chart_title = slide.title or "Data Visualization"

                # Create temp file for chart
                import uuid
                chart_filename = f"chart_{uuid.uuid4().hex[:8]}.png"
                chart_path = Path(tempfile.gettempdir()) / chart_filename

                # Generate chart
                chart_file = self._generate_plotly_chart(
                    chart_type=chart_type,
                    data=slide.chart_data,
                    output_path=str(chart_path),
                    title=chart_title
                )

                if chart_file:
                    # Return DataSlide with chart
                    return {
                        "type": "data",
                        "data": {
                            "slideNumber": slide_number,
                            "totalSlides": total_slides,
                            "title": chart_title,
                            "chartPath": chart_file,
                            "caption": getattr(slide, "stat_context", None) or getattr(slide, "body", None),
                            "source": getattr(slide, "source", None),
                            "icon": self._normalize_icon_name(getattr(slide, "icon_name", None) or "BarChart3"),
                            "dimensions": self.dimensions,
                        },
                    }

            # Fallback to StatSlide if no chart data or Plotly unavailable
            context, source = self._split_context_source(
                slide.stat_context or slide.body or "",
                slide.source
            )
            return {
                "type": "stat",
                "data": {
                    "slideNumber": slide_number,
                    "totalSlides": total_slides,
                    "stat": slide.statistic or "",
                    "label": slide.stat_label or slide.title or "",
                    "context": context,
                    "source": source or "",
                    "icon": self._normalize_icon_name(slide.icon_name or "TrendingUp"),
                    "color": "teal",
                    "dimensions": self.dimensions,
                },
            }

        if slide_type in ["tips", "steps"]:
            tips = []
            if slide.bullet_points:
                for point in slide.bullet_points:
                    tips.append({"text": point})
            if slide.steps:
                for step in slide.steps:
                    tips.append({"text": step})
            if not tips:
                tips.append({"text": slide.body or slide.title or "Key takeaway"})

            return {
                "type": "tips",
                "data": {
                    "slideNumber": slide_number,
                    "totalSlides": total_slides,
                    "title": slide.title or "Key Tips",
                    "tips": tips,
                    "dimensions": self.dimensions,
                },
            }

        if slide_type == "quote":
            return {
                "type": "stat",
                "data": {
                    "slideNumber": slide_number,
                    "totalSlides": total_slides,
                    "stat": "“”",
                    "label": slide.quote_text or "",
                    "context": f"— {slide.quote_author}" if slide.quote_author else "",
                    "source": "",
                    "icon": "Quote",
                    "color": "teal",
                    "dimensions": self.dimensions,
                },
            }

        if slide_type == "comparison":
            return {
                "type": "myth",
                "data": {
                    "slideNumber": slide_number,
                    "totalSlides": total_slides,
                    "myth": slide.before_text or "Common approach",
                    "truth": slide.after_text or "Better approach",
                    "source": "",
                    "dimensions": self.dimensions,
                },
            }

        if slide_type == "story":
            return {
                "type": "stat",
                "data": {
                    "slideNumber": slide_number,
                    "totalSlides": total_slides,
                    "stat": slide.title or "Real story",
                    "label": slide.body or "",
                    "context": "",
                    "source": "",
                    "icon": "Heart",
                    "color": "teal",
                    "dimensions": self.dimensions,
                },
            }

        if slide_type == "cta":
            # Get author and account info from config
            author = self.author_config.get("author", {})
            account_str = str(self.account)
            account_info = author.get("accounts", {}).get(account_str, {})
            branding = self.author_config.get("branding", {})

            # Resolve photo path relative to renderer/src directory
            photo_path = author.get("photo", "assets/5e4311be9235ba207024edfb13240abe8cf20f3f.png")
            # Convert to path accessible from React app (starts with @ for alias or src/ for relative)
            if not photo_path.startswith("@/") and not photo_path.startswith("http"):
                photo_path = f"@/{photo_path}"

            return {
                "type": "cta",
                "data": {
                    "slideNumber": slide_number,
                    "totalSlides": total_slides,
                    "name": author.get("name", "Dr Shailesh Singh"),
                    "credentials": author.get("credentials", "Cardiologist | Evidence-Based Medicine"),
                    "handle": slide.cta_handle or account_info.get("handle", "@dr.shailesh.singh"),
                    "valueProposition": slide.cta_text or branding.get("valueProposition", "Follow for evidence-based cardiology"),
                    "secondaryText": branding.get("secondaryText", ""),
                    "followerCount": account_info.get("followerCount", ""),
                    "photoPath": photo_path,
                    "dimensions": self.dimensions,
                },
            }

        return {
            "type": "tips",
            "data": {
                "slideNumber": slide_number,
                "totalSlides": total_slides,
                "title": slide.title or "Key Point",
                "tips": [{"text": slide.body or slide.title or "Important insight"}],
                "dimensions": self.dimensions,
            },
        }

    def render_slide(
        self,
        slide_data: Dict[str, Any],
        output_path: str
    ) -> str:
        """
        Render a single slide to PNG.

        Args:
            slide_data: Slide data dictionary with 'type' and 'data' keys
            output_path: Path to save the PNG file

        Returns:
            Path to the rendered PNG file
        """
        # Validate slide data
        if "type" not in slide_data:
            raise ValueError("Slide data must have 'type' key")
        if "data" not in slide_data:
            raise ValueError("Slide data must have 'data' key")

        # Run the Node.js render script
        result = subprocess.run(
            [
                "node",
                str(self.render_script),
                "--slide",
                json.dumps(slide_data),
                "--output",
                output_path,
                "--width",
                str(self.width),
                "--height",
                str(self.height),
            ],
            cwd=str(self.renderer_dir),
            capture_output=True,
            text=True,
            timeout=120  # Increased for complex slides
        )

        if result.returncode != 0:
            raise RuntimeError(f"Render failed: {result.stderr}")

        return output_path

    def render_carousel(
        self,
        slides: List[Union[Dict[str, Any], Any]],
        output_dir: str = "./output",
        filename_prefix: str = "carousel_slide"
    ) -> List[Any]:
        """
        Render multiple slides to PNG files.

        Args:
            slides: List of slide data dictionaries
            output_dir: Directory to save PNG files
            filename_prefix: Prefix for output filenames

        Returns:
            List of SlideRenderResult objects or file paths
        """
        # Create output directory
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        normalized_slides = slides
        if slides and MODELS_AVAILABLE and SlideContent and hasattr(slides[0], "slide_type"):
            normalized_slides = []
            total_slides = len(slides)
            for i, slide in enumerate(slides, 1):
                normalized_slides.append(
                    self._slide_content_to_render_data(slide, i, total_slides)
                )

        # Write slides to temp JSON file
        with tempfile.NamedTemporaryFile(
            mode='w',
            suffix='.json',
            delete=False
        ) as f:
            json.dump(normalized_slides, f)
            input_file = f.name

        start_time = time.time()
        try:
            # Run the Node.js render script
            result = subprocess.run(
                [
                    "node",
                    str(self.render_script),
                    "--input",
                    input_file,
                    "--output",
                    str(output_path),
                    "--width",
                    str(self.width),
                    "--height",
                    str(self.height),
                ],
                cwd=str(self.renderer_dir),
                capture_output=True,
                text=True,
                timeout=180  # 3 minutes for carousel with multiple slides
            )

            if result.returncode != 0:
                raise RuntimeError(f"Render failed: {result.stderr}")

            # Return list of output files
            output_files = sorted(output_path.glob("slide_*.png"))
            if MODELS_AVAILABLE and SlideRenderResult:
                render_time = (time.time() - start_time) * 1000
                per_slide = render_time / max(len(output_files), 1)
                return [
                    SlideRenderResult(
                        slide_number=i + 1,
                        output_path=f,
                        width=self.width,
                        height=self.height,
                        render_time_ms=per_slide,
                        renderer_used="puppeteer",
                        warnings=None,
                    )
                    for i, f in enumerate(output_files)
                ]
            return [str(f) for f in output_files]

        finally:
            # Clean up temp file
            os.unlink(input_file)

    def create_hook_slide(
        self,
        slide_number: int,
        total_slides: int,
        headline: str,
        subtitle: Optional[str] = None,
        icon: Optional[str] = None,
        theme: str = "teal"
    ) -> Dict[str, Any]:
        """Create a hook slide data structure."""
        return {
            "type": "hook",
            "data": {
                "slideNumber": slide_number,
                "totalSlides": total_slides,
                "headline": headline,
                "subtitle": subtitle,
                "icon": self._normalize_icon_name(icon),
                "theme": theme,
                "dimensions": self.dimensions,
            }
        }

    def create_myth_slide(
        self,
        slide_number: int,
        total_slides: int,
        myth: str,
        truth: str,
        source: Optional[str] = None
    ) -> Dict[str, Any]:
        """Create a myth/truth slide data structure."""
        return {
            "type": "myth",
            "data": {
                "slideNumber": slide_number,
                "totalSlides": total_slides,
                "myth": myth,
                "truth": truth,
                "source": source,
                "dimensions": self.dimensions,
            }
        }

    def create_stat_slide(
        self,
        slide_number: int,
        total_slides: int,
        stat: str,
        label: str,
        context: Optional[str] = None,
        source: Optional[str] = None,
        icon: Optional[str] = None,
        color: str = "teal"
    ) -> Dict[str, Any]:
        """Create a statistics slide data structure."""
        return {
            "type": "stat",
            "data": {
                "slideNumber": slide_number,
                "totalSlides": total_slides,
                "stat": stat,
                "label": label,
                "context": context,
                "source": source,
                "icon": self._normalize_icon_name(icon),
                "color": color,
                "dimensions": self.dimensions,
            }
        }

    def create_tips_slide(
        self,
        slide_number: int,
        total_slides: int,
        title: str,
        tips: List[Dict[str, str]]
    ) -> Dict[str, Any]:
        """
        Create a tips slide data structure.

        Args:
            tips: List of dicts with 'text' and optional 'icon' keys
        """
        return {
            "type": "tips",
            "data": {
                "slideNumber": slide_number,
                "totalSlides": total_slides,
                "title": title,
                "tips": tips,
                "dimensions": self.dimensions,
            }
        }

    def create_data_slide(
        self,
        slide_number: int,
        total_slides: int,
        title: str,
        chart_data: Dict[str, Any],
        chart_type: str = "bar",
        caption: Optional[str] = None,
        source: Optional[str] = None,
        icon: Optional[str] = None,
        output_dir: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create a data slide with Plotly chart.

        Args:
            slide_number: Slide number
            total_slides: Total slides in carousel
            title: Slide title
            chart_data: Data for Plotly chart (format varies by chart_type)
            chart_type: Type of chart ('bar', 'forest', 'line', 'survival')
            caption: Optional caption below chart
            source: Data source citation
            icon: Icon name (lucide-react)
            output_dir: Directory to save chart PNG (uses temp dir if None)

        Returns:
            Slide data dictionary
        """
        # Generate Plotly chart
        import uuid
        chart_filename = f"chart_{uuid.uuid4().hex[:8]}.png"

        if output_dir:
            chart_path = Path(output_dir) / chart_filename
        else:
            chart_path = Path(tempfile.gettempdir()) / chart_filename

        chart_file = self._generate_plotly_chart(
            chart_type=chart_type,
            data=chart_data,
            output_path=str(chart_path),
            title=title
        )

        if chart_file:
            return {
                "type": "data",
                "data": {
                    "slideNumber": slide_number,
                    "totalSlides": total_slides,
                    "title": title,
                    "chartPath": chart_file,
                    "caption": caption,
                    "source": source,
                    "icon": self._normalize_icon_name(icon or "BarChart3"),
                    "dimensions": self.dimensions,
                },
            }
        else:
            # Fallback to stat slide if Plotly unavailable
            return self.create_stat_slide(
                slide_number=slide_number,
                total_slides=total_slides,
                stat="Data",
                label=title,
                context=caption,
                source=source,
                icon=icon or "BarChart3"
            )

    def create_cta_slide(
        self,
        slide_number: int,
        total_slides: int,
        value_proposition: Optional[str] = None,
        name: Optional[str] = None,
        credentials: Optional[str] = None,
        handle: Optional[str] = None,
        secondary_text: Optional[str] = None,
        follower_count: Optional[str] = None
    ) -> Dict[str, Any]:
        """Create a CTA slide data structure using author config."""
        # Get author and account info from config
        author = self.author_config.get("author", {})
        account_str = str(self.account)
        account_info = author.get("accounts", {}).get(account_str, {})
        branding = self.author_config.get("branding", {})

        # Resolve photo path
        photo_path = author.get("photo", "assets/5e4311be9235ba207024edfb13240abe8cf20f3f.png")
        if not photo_path.startswith("@/") and not photo_path.startswith("http"):
            photo_path = f"@/{photo_path}"

        return {
            "type": "cta",
            "data": {
                "slideNumber": slide_number,
                "totalSlides": total_slides,
                "name": name or author.get("name", "Dr Shailesh Singh"),
                "credentials": credentials or author.get("credentials", "Cardiologist | Evidence-Based Medicine"),
                "handle": handle or account_info.get("handle", "@dr.shailesh.singh"),
                "valueProposition": value_proposition or branding.get("valueProposition", "Follow for evidence-based cardiology"),
                "secondaryText": secondary_text or branding.get("secondaryText", ""),
                "followerCount": follower_count or account_info.get("followerCount", ""),
                "photoPath": photo_path,
                "dimensions": self.dimensions,
            }
        }


def main():
    """Test the renderer with sample slides."""
    renderer = PuppeteerRenderer()

    # Create test slides
    slides = [
        renderer.create_hook_slide(
            slide_number=1,
            total_slides=5,
            headline="5 Statin Myths That Need to Die",
            subtitle="What the science actually says",
            icon="Pill",
            theme="teal"
        ),
        renderer.create_myth_slide(
            slide_number=2,
            total_slides=5,
            myth="Statins cause muscle pain in everyone",
            truth="Only 5-10% experience muscle symptoms, and it's usually mild",
            source="Lancet 2022"
        ),
        renderer.create_stat_slide(
            slide_number=3,
            total_slides=5,
            stat="25%",
            label="Reduction in Heart Attack Risk",
            context="For every 1 mmol/L reduction in LDL",
            source="CTT Meta-analysis",
            icon="Heart",
            color="green"
        ),
        renderer.create_tips_slide(
            slide_number=4,
            total_slides=5,
            title="3 Tips for Statin Success",
            tips=[
                {"text": "Take at the same time daily", "icon": "Clock"},
                {"text": "Report symptoms early", "icon": "MessageCircle"},
                {"text": "Combine with lifestyle changes", "icon": "Salad"}
            ]
        ),
        renderer.create_cta_slide(
            slide_number=5,
            total_slides=5,
            value_proposition="Follow for evidence-based cardiology",
            secondary_text="New posts every week",
            follower_count="50K+"
        )
    ]

    # Render
    output_dir = Path(__file__).parent.parent / "outputs" / "test_carousel"
    output_files = renderer.render_carousel(slides, str(output_dir))

    print(f"\nRendered {len(output_files)} slides:")
    for f in output_files:
        print(f"  - {f}")


if __name__ == "__main__":
    main()
