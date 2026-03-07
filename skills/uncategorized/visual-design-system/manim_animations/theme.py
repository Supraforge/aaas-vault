"""
Shared Manim theme utilities for cardiology animations.
"""

from __future__ import annotations

from pathlib import Path
import sys

VISUAL_SYSTEM_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(VISUAL_SYSTEM_ROOT))

from tokens.index import get_tokens, get_color, get_accessible_pair


def _get_available_font(preferred: list[str], fallback: str) -> str:
    """
    Return the first available font from the preferred list.
    Falls back to a generic font if none are available.
    """
    import subprocess
    try:
        # Use fc-list with specific format to get just the family name
        result = subprocess.run(
            ["fc-list", "--format", "%{family}\n"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        # Parse multi-family entries (e.g., "Liberation Sans,Sans" becomes two entries)
        available_fonts = set()
        for line in result.stdout.split("\n"):
            for family in line.split(","):
                family_clean = family.strip()
                if family_clean:
                    available_fonts.add(family_clean)
    except Exception:
        available_fonts = set()

    for font in preferred:
        font_clean = font.strip()
        if font_clean in available_fonts or not available_fonts:
            return font_clean
    return fallback


# Font preferences with cross-platform fallbacks
# Liberation Sans is metric-compatible with Arial/Helvetica on Linux
_SANS_PREFERENCES = ["Helvetica", "Arial", "Liberation Sans", "FreeSans", "DejaVu Sans", "Sans"]
_MONO_PREFERENCES = ["Courier", "Liberation Mono", "FreeMono", "DejaVu Sans Mono", "Monospace"]

PRIMARY_FONT = _get_available_font(_SANS_PREFERENCES, "Sans")
MONO_FONT = _get_available_font(_MONO_PREFERENCES, "Monospace")

COLORS = {
    "navy": get_color("primary.navy"),
    "blue": get_color("primary.blue"),
    "teal": get_color("primary.teal"),
    "success": get_color("semantic.success"),
    "warning": get_color("semantic.warning"),
    "danger": get_color("semantic.danger"),
    "neutral": get_color("semantic.neutral"),
    "text": get_color("text.primary"),
    "muted": get_color("text.muted"),
    "background": get_color("backgrounds.white"),
    "panel": get_color("backgrounds.light_gray"),
}

ACCESSIBLE_PAIR = get_accessible_pair("treatment_control")

FONT_SIZES = {
    "title": 44,
    "subtitle": 34,
    "label": 26,
    "small": 22,
}


def apply_theme(config, resolution: str = "1080p") -> None:
    """
    Apply a publication-style Manim config.

    Args:
        config: manim config object
        resolution: "1080p" or "4k"
    """
    config.background_color = COLORS["background"]
    config.frame_rate = 30

    if resolution == "4k":
        config.pixel_width = 3840
        config.pixel_height = 2160
    else:
        config.pixel_width = 1920
        config.pixel_height = 1080
