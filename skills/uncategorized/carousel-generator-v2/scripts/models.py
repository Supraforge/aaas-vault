"""
Data models for Carousel Generator v2

Pydantic models for type-safe carousel generation with validation.
"""

from enum import Enum
from typing import List, Optional, Dict, Any, Literal
from pydantic import BaseModel, Field, validator
from pathlib import Path


class SlideType(str, Enum):
    """Types of slides available in the carousel system."""
    HOOK = "hook"           # Opening hook, bold question, surprising stat
    TIPS = "tips"           # Numbered tips with icons
    STATS = "stats"         # Big number + context
    COMPARISON = "comparison"  # Before/after, vs layout
    STORY = "story"         # Patient narrative, quote
    DATA = "data"           # Chart, graph, forest plot
    STEPS = "steps"         # Process with arrows
    MYTH = "myth"           # Crossed-out myth + truth
    QUOTE = "quote"         # Expert opinion
    CTA = "cta"             # Call to action, follow, save


class ColorMode(str, Enum):
    """Color modes for slides."""
    LIGHT = "light"
    DARK = "dark"
    MINIMAL = "minimal"
    AUTO = "auto"  # AI-selected per slide


class AspectRatio(str, Enum):
    """Supported aspect ratios."""
    INSTAGRAM_4X5 = "4:5"   # 1080x1350, Instagram optimized
    SQUARE_1X1 = "1:1"      # 1080x1080, multi-platform


class ContentCategory(str, Enum):
    """4A Framework content categories."""
    ACTIONABLE = "actionable"      # Practical tips they can use today
    ANALYTICAL = "analytical"       # Data-driven insights
    ASPIRATIONAL = "aspirational"   # Motivational, showing what's possible
    ANTHROPOLOGICAL = "anthropological"  # Stories and human experiences


class IconStyle(str, Enum):
    """Icon rendering styles."""
    FILLED = "filled"
    OUTLINE = "outline"
    NONE = "none"


class SlideContent(BaseModel):
    """Content for a single slide."""

    slide_type: SlideType
    title: Optional[str] = None
    subtitle: Optional[str] = None
    body: Optional[str] = None
    bullet_points: Optional[List[str]] = None
    statistic: Optional[str] = None
    stat_label: Optional[str] = None
    stat_context: Optional[str] = None
    source: Optional[str] = None
    quote_text: Optional[str] = None
    quote_author: Optional[str] = None
    myth_text: Optional[str] = None
    truth_text: Optional[str] = None
    before_text: Optional[str] = None
    after_text: Optional[str] = None
    steps: Optional[List[str]] = None
    cta_text: Optional[str] = None
    cta_handle: Optional[str] = None
    icon_name: Optional[str] = None
    icons: Optional[List[str]] = None  # For slides with multiple icons
    color_mode: ColorMode = ColorMode.AUTO
    icon_style: IconStyle = IconStyle.OUTLINE

    # Chart/data specific
    chart_type: Optional[str] = None
    chart_data: Optional[Dict[str, Any]] = None

    # Animation specific (Manim integration)
    animation_scene: Optional[str] = None
    animation_quality: Optional[str] = None  # l, m, h, k (Manim presets)
    animation_format: Optional[str] = None   # mp4, gif

    # Metadata
    slide_number: int = 0
    word_count: int = 0

    @validator('word_count', always=True)
    def calculate_word_count(cls, v, values):
        """Auto-calculate word count from content."""
        text_fields = ['title', 'subtitle', 'body', 'quote_text',
                       'myth_text', 'truth_text', 'before_text', 'after_text',
                       'cta_text', 'source']
        total = 0
        for field in text_fields:
            if values.get(field):
                total += len(str(values[field]).split())
        if values.get('bullet_points'):
            total += sum(len(bp.split()) for bp in values['bullet_points'])
        if values.get('steps'):
            total += sum(len(s.split()) for s in values['steps'])
        return total


class CarouselConfig(BaseModel):
    """Configuration for carousel generation."""

    aspect_ratio: AspectRatio = AspectRatio.INSTAGRAM_4X5
    color_mode: ColorMode = ColorMode.AUTO
    icon_style: IconStyle = IconStyle.OUTLINE
    account: int = Field(default=1, ge=1, le=2)
    max_slides: int = Field(default=10, ge=1, le=10)
    max_words_per_slide: int = Field(default=15, ge=5, le=30)

    # Quality settings
    check_contrast: bool = True
    check_text_density: bool = True
    check_anti_ai: bool = True

    # Output settings
    output_dir: Optional[Path] = None
    generate_both_ratios: bool = False
    generate_caption: bool = True
    generate_alt_text: bool = True
    generate_hashtags: bool = True

    # Animation settings (Manim)
    manim_venv: Optional[Path] = None
    manim_bin: Optional[Path] = None


class Carousel(BaseModel):
    """Complete carousel with all slides and metadata."""

    topic: str
    category: ContentCategory = ContentCategory.ACTIONABLE
    slides: List[SlideContent]
    config: CarouselConfig = Field(default_factory=CarouselConfig)

    # Generated outputs
    output_paths: Optional[List[Path]] = None
    caption: Optional[str] = None
    alt_texts: Optional[List[str]] = None
    hashtags: Optional[List[str]] = None

    # Quality metrics
    avg_word_count: Optional[float] = None
    contrast_passed: Optional[bool] = None
    anti_ai_passed: Optional[bool] = None

    @validator('slides')
    def validate_slide_count(cls, v, values):
        """Ensure slide count is within Instagram limits."""
        if len(v) > 10:
            raise ValueError("Instagram allows maximum 10 slides per carousel")
        return v

    def calculate_metrics(self):
        """Calculate quality metrics for the carousel."""
        if self.slides:
            self.avg_word_count = sum(s.word_count for s in self.slides) / len(self.slides)


class SlideRenderResult(BaseModel):
    """Result from rendering a single slide."""

    slide_number: int
    output_path: Path
    width: int
    height: int
    render_time_ms: float
    renderer_used: str  # "pillow", "satori", "gemini"
    warnings: Optional[List[str]] = None


class CarouselRenderResult(BaseModel):
    """Complete result from rendering a carousel."""

    carousel: Carousel
    slides: List[SlideRenderResult]
    total_render_time_ms: float
    output_directory: Path
    preview_path: Optional[Path] = None

    # Quality check results
    contrast_check: Optional[Dict[str, Any]] = None
    text_density_check: Optional[Dict[str, Any]] = None


# Template presets for common use cases
TEMPLATE_PRESETS = {
    "tips_5": {
        "slides": [
            SlideType.HOOK,
            SlideType.TIPS,
            SlideType.TIPS,
            SlideType.TIPS,
            SlideType.TIPS,
            SlideType.TIPS,
            SlideType.STATS,
            SlideType.CTA
        ],
        "description": "5 tips with hook, stats, and CTA"
    },
    "myth_busting": {
        "slides": [
            SlideType.HOOK,
            SlideType.MYTH,
            SlideType.MYTH,
            SlideType.MYTH,
            SlideType.STATS,
            SlideType.CTA
        ],
        "description": "Myth-busting format"
    },
    "patient_story": {
        "slides": [
            SlideType.HOOK,
            SlideType.STORY,
            SlideType.STORY,
            SlideType.DATA,
            SlideType.TIPS,
            SlideType.QUOTE,
            SlideType.CTA
        ],
        "description": "Patient narrative format"
    },
    "data_driven": {
        "slides": [
            SlideType.HOOK,
            SlideType.STATS,
            SlideType.DATA,
            SlideType.COMPARISON,
            SlideType.TIPS,
            SlideType.CTA
        ],
        "description": "Data-focused format"
    },
    "how_to": {
        "slides": [
            SlideType.HOOK,
            SlideType.STEPS,
            SlideType.STEPS,
            SlideType.STEPS,
            SlideType.TIPS,
            SlideType.CTA
        ],
        "description": "Step-by-step process format"
    }
}
