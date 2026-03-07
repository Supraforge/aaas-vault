"""
Design token utilities for Carousel Generator v2

Load and access brand tokens for consistent styling.
"""

import json
from pathlib import Path
from typing import Dict, Any, Tuple, Optional
from functools import lru_cache


SKILL_DIR = Path(__file__).parent.parent
TOKENS_FILE = SKILL_DIR / "tokens" / "brand-tokens.json"


@lru_cache(maxsize=1)
def load_tokens() -> Dict[str, Any]:
    """Load brand tokens from JSON file."""
    with open(TOKENS_FILE, 'r') as f:
        return json.load(f)


def get_colors() -> Dict[str, str]:
    """Get color palette as hex strings."""
    tokens = load_tokens()
    return {k: v['value'] for k, v in tokens['colors'].items()}


def get_color_rgb(color_name: str) -> Tuple[int, int, int]:
    """Get color as RGB tuple."""
    tokens = load_tokens()
    if color_name in tokens['colors']:
        return tuple(tokens['colors'][color_name]['rgb'])
    # Check if it's a hex value
    if color_name.startswith('#'):
        return hex_to_rgb(color_name)
    raise ValueError(f"Unknown color: {color_name}")


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb: Tuple[int, int, int]) -> str:
    """Convert RGB tuple to hex string."""
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"


def get_color_mode(mode: str) -> Dict[str, str]:
    """Get color scheme for a specific mode (light/dark/minimal)."""
    tokens = load_tokens()
    mode_colors = tokens['colorModes'].get(mode, tokens['colorModes']['light'])

    # Resolve token references like "{colors.primary}"
    resolved = {}
    colors = tokens['colors']
    for key, value in mode_colors.items():
        if isinstance(value, str) and value.startswith('{colors.'):
            color_name = value[8:-1]  # Extract color name
            resolved[key] = colors[color_name]['value']
        else:
            resolved[key] = value

    return resolved


def get_typography() -> Dict[str, Dict[str, Any]]:
    """Get typography specifications."""
    tokens = load_tokens()
    return tokens['typography']


def get_typography_for_element(element: str) -> Dict[str, Any]:
    """Get typography specs for a specific element."""
    tokens = load_tokens()
    if element in tokens['typography']:
        return tokens['typography'][element]
    raise ValueError(f"Unknown typography element: {element}")


def get_dimensions(aspect_ratio: str = "4:5") -> Dict[str, int]:
    """Get dimensions for a specific aspect ratio."""
    tokens = load_tokens()
    key = "instagram4x5" if aspect_ratio == "4:5" else "instagram1x1"
    return tokens['dimensions'][key]


def get_spacing() -> Dict[str, int]:
    """Get spacing values."""
    tokens = load_tokens()
    return tokens['spacing']


def get_footer_specs() -> Dict[str, Any]:
    """Get footer specifications."""
    tokens = load_tokens()
    return tokens['footer']


def get_account(account_num: int = 1) -> Dict[str, str]:
    """Get account information."""
    tokens = load_tokens()
    return tokens['accounts'][str(account_num)]


def get_quality_gates() -> Dict[str, Any]:
    """Get quality gate thresholds."""
    tokens = load_tokens()
    return tokens['qualityGates']


def get_template_defaults(template_name: str) -> Dict[str, Any]:
    """Get default settings for a template type."""
    tokens = load_tokens()
    if template_name in tokens['templateDefaults']:
        return tokens['templateDefaults'][template_name]
    return tokens['templateDefaults']['TipsSlide']


def get_font_path(weight: str = "Regular") -> Path:
    """Get path to Inter font file."""
    fonts_dir = SKILL_DIR / "assets" / "fonts"
    font_file = fonts_dir / f"Inter-{weight}.ttf"
    if font_file.exists():
        return font_file
    # Fallback to system fonts
    return None


def get_icon_path(icon_name: str) -> Optional[Path]:
    """Get path to an SVG icon."""
    icons_dir = SKILL_DIR / "assets" / "icons"
    icon_file = icons_dir / f"{icon_name}.svg"
    if icon_file.exists():
        return icon_file
    return None


def get_all_icons() -> list:
    """Get list of all available icon names."""
    icons_dir = SKILL_DIR / "assets" / "icons"
    return [f.stem for f in icons_dir.glob("*.svg")]


def calculate_contrast_ratio(color1: Tuple[int, int, int],
                             color2: Tuple[int, int, int]) -> float:
    """
    Calculate WCAG contrast ratio between two colors.
    Returns ratio from 1:1 to 21:1.
    """
    def relative_luminance(rgb):
        r, g, b = [x / 255.0 for x in rgb]
        r = r / 12.92 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
        g = g / 12.92 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
        b = b / 12.92 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    l1 = relative_luminance(color1)
    l2 = relative_luminance(color2)

    lighter = max(l1, l2)
    darker = min(l1, l2)

    return (lighter + 0.05) / (darker + 0.05)


def check_wcag_aa(foreground: Tuple[int, int, int],
                  background: Tuple[int, int, int],
                  is_large_text: bool = False) -> bool:
    """
    Check if color combination meets WCAG AA standards.
    Large text (>=18pt or >=14pt bold) requires 3:1 ratio.
    Normal text requires 4.5:1 ratio.
    """
    ratio = calculate_contrast_ratio(foreground, background)
    min_ratio = 3.0 if is_large_text else 4.5
    return ratio >= min_ratio
