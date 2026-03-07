"""
Carousel Generator v2 - World-Class Instagram Carousel Generator

This module provides a comprehensive carousel generation system that combines:
- AI content intelligence (Claude/GPT-4o-mini)
- Multi-tool visual generation (Pillow, Satori, Gemini, Fal.ai)
- Professional design systems (10 template types)
- Quality assurance automation (WCAG, text density, anti-AI)

Usage:
    from scripts.carousel_generator import CarouselGenerator

    generator = CarouselGenerator()
    carousel = generator.generate(
        topic="GLP-1 for weight loss",
        template_type="tips"
    )
"""

__version__ = "2.0.0"
__author__ = "Dr. Shailesh Singh"

from .models import (
    SlideType,
    ColorMode,
    SlideContent,
    Carousel,
    CarouselConfig,
)
from .tokens import load_tokens, get_colors, get_typography
