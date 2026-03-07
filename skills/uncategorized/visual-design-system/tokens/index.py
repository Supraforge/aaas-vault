"""
Design Token Loader

Loads and provides easy access to all design tokens for the visual design system.
Implements Nature/JACC/NEJM publication standards.

Usage:
    from tokens import get_tokens, get_color, get_typography

    # Get all tokens
    tokens = get_tokens()

    # Get specific color
    navy = get_color("primary.navy")  # Returns "#1e3a5f"

    # Get color palette for charts
    palette = get_color_palette("categorical")  # Returns list of hex colors

    # Get accessible pair for comparisons
    treatment, control = get_accessible_pair("treatment_control")

    # Validate contrast ratio
    is_valid = validate_contrast("#1e3a5f", "#ffffff")  # Returns True if >= 4.5:1
"""

import json
import math
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union
from functools import lru_cache


class DesignTokens:
    """Central access point for all design tokens."""

    def __init__(self, tokens_dir: Optional[Path] = None):
        """
        Initialize the design tokens.

        Args:
            tokens_dir: Path to tokens directory. Defaults to directory containing this file.
        """
        if tokens_dir is None:
            tokens_dir = Path(__file__).parent

        self.tokens_dir = tokens_dir
        self._colors: Optional[Dict] = None
        self._typography: Optional[Dict] = None
        self._spacing: Optional[Dict] = None
        self._shadows: Optional[Dict] = None

    @property
    def colors(self) -> Dict:
        """Load and return color tokens."""
        if self._colors is None:
            self._colors = self._load_json("colors.json")
        return self._colors

    @property
    def typography(self) -> Dict:
        """Load and return typography tokens."""
        if self._typography is None:
            self._typography = self._load_json("typography.json")
        return self._typography

    @property
    def spacing(self) -> Dict:
        """Load and return spacing tokens."""
        if self._spacing is None:
            self._spacing = self._load_json("spacing.json")
        return self._spacing

    @property
    def shadows(self) -> Dict:
        """Load and return shadow tokens."""
        if self._shadows is None:
            self._shadows = self._load_json("shadows.json")
        return self._shadows

    def _load_json(self, filename: str) -> Dict:
        """Load a JSON token file."""
        filepath = self.tokens_dir / filename
        with open(filepath, 'r') as f:
            return json.load(f)

    def get(self, path: str, token_type: str = "colors") -> Any:
        """
        Get a token value by dot-notation path.

        Args:
            path: Dot-notation path (e.g., "primary.navy.value")
            token_type: One of "colors", "typography", "spacing", "shadows"

        Returns:
            Token value at the specified path

        Example:
            tokens.get("primary.navy.value", "colors")  # Returns "#1e3a5f"
        """
        token_source = getattr(self, token_type)

        parts = path.split(".")
        current = token_source

        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                raise KeyError(f"Token path '{path}' not found in {token_type}")

        return current

    def get_color(self, path: str) -> str:
        """
        Get a color value by path.

        Args:
            path: Path like "primary.navy" or "semantic.success"

        Returns:
            Hex color value
        """
        result = self.get(path, "colors")

        # If we got a dict with a "value" key, return the value
        if isinstance(result, dict) and "value" in result:
            return result["value"]

        return result

    def get_color_palette(self, palette_name: str) -> List[str]:
        """
        Get a list of colors for a named palette.

        Args:
            palette_name: One of "categorical", "sequential_blue", "diverging"

        Returns:
            List of hex color values
        """
        palettes = self.colors.get("data_visualization", {})

        if palette_name not in palettes:
            raise KeyError(f"Palette '{palette_name}' not found. Available: {list(palettes.keys())}")

        palette_data = palettes[palette_name].get("palette", [])
        return [item["value"] for item in palette_data]

    def get_accessible_pair(self, use_case: str) -> Tuple[str, str]:
        """
        Get a colorblind-safe color pair for comparisons.

        Args:
            use_case: One of "treatment_control", "benefit_risk", "before_after", "intervention_placebo"
                     or "pair_1", "pair_2", "pair_3", "pair_4"

        Returns:
            Tuple of (color_a, color_b) hex values
        """
        pairs = self.colors.get("accessible_pairs", {})

        # Map friendly names to pair keys
        use_case_map = {
            "treatment_control": "pair_1",
            "benefit_risk": "pair_2",
            "before_after": "pair_3",
            "intervention_placebo": "pair_4",
        }

        pair_key = use_case_map.get(use_case, use_case)

        if pair_key not in pairs:
            raise KeyError(f"Color pair '{use_case}' not found. Available: {list(pairs.keys())}")

        pair = pairs[pair_key]
        return (pair["color_a"], pair["color_b"])

    def get_clinical_color(self, outcome_type: str) -> str:
        """
        Get the standard color for a clinical outcome type.

        Args:
            outcome_type: One of "mortality", "hospitalization", "symptom_improvement",
                         "biomarker", "safety_event"
        """
        outcomes = self.colors.get("clinical_outcomes", {})

        if outcome_type not in outcomes:
            raise KeyError(f"Outcome '{outcome_type}' not found. Available: {list(outcomes.keys())}")

        return outcomes[outcome_type]["value"]

    def get_forest_plot_colors(self) -> Dict[str, str]:
        """Get the standard colors for forest plot elements."""
        return self.colors.get("forest_plot", {})

    def get_font_family(self, font_type: str = "primary") -> str:
        """
        Get a font family string.

        Args:
            font_type: "primary" or "monospace"
        """
        fonts = self.typography.get("fonts", {})
        return fonts.get(font_type, {}).get("family", "Arial, sans-serif")

    def get_font_size(self, context: str, element: str) -> Dict:
        """
        Get font size specification.

        Args:
            context: "figure_elements", "infographic_elements", or "social_media"
            element: Specific element name (e.g., "panel_label", "headline")

        Returns:
            Dict with "value" (pt) and "pixels" keys
        """
        sizes = self.typography.get("sizes", {})
        context_sizes = sizes.get(context, {})

        if element not in context_sizes:
            raise KeyError(f"Size '{element}' not found in '{context}'")

        return context_sizes[element]

    def get_spacing(self, scale: Union[int, str]) -> str:
        """
        Get a spacing value from the scale.

        Args:
            scale: Numeric scale (0-16) or name ("xs", "sm", "md", "lg", "xl", etc.)
        """
        spacing_scale = self.spacing.get("scale", {})

        # Convert named scales to numeric
        name_to_scale = {v["name"]: k for k, v in spacing_scale.items() if "name" in v}

        if isinstance(scale, str) and scale in name_to_scale:
            scale = name_to_scale[scale]

        scale = str(scale)

        if scale not in spacing_scale:
            raise KeyError(f"Spacing scale '{scale}' not found")

        return spacing_scale[scale]["value"]

    def get_layout_spacing(self, layout_type: str, element: str) -> str:
        """
        Get spacing for a specific layout context.

        Args:
            layout_type: "figure_layout", "chart_layout", "infographic_layout", "carousel_layout"
            element: Specific spacing element
        """
        layout = self.spacing.get(layout_type, {})

        if element not in layout:
            raise KeyError(f"Spacing '{element}' not found in '{layout_type}'")

        return layout[element]["value"]

    def get_shadow(self, level: str = "md") -> str:
        """
        Get a shadow value.

        Args:
            level: "none", "xs", "sm", "md", "lg", "xl"
        """
        elevation = self.shadows.get("elevation", {})

        if level not in elevation:
            raise KeyError(f"Shadow level '{level}' not found")

        return elevation[level]["value"]

    def get_stroke_width(self, weight: str = "regular") -> str:
        """
        Get a stroke width value.

        Args:
            weight: "hairline", "thin", "regular", "medium", "thick", "extra_thick"
        """
        strokes = self.spacing.get("stroke_widths", {})
        return strokes.get(weight, "1px")

    def get_border_radius(self, size: str = "md") -> str:
        """
        Get a border radius value.

        Args:
            size: "none", "sm", "md", "lg", "xl", "full"
        """
        radii = self.spacing.get("border_radius", {})
        return radii.get(size, "4px")


# Module-level instance for convenience
_default_tokens: Optional[DesignTokens] = None


def get_tokens() -> DesignTokens:
    """Get the default DesignTokens instance."""
    global _default_tokens
    if _default_tokens is None:
        _default_tokens = DesignTokens()
    return _default_tokens


def get_color(path: str) -> str:
    """Convenience function to get a color value."""
    return get_tokens().get_color(path)


def get_typography(context: str, element: str) -> Dict:
    """Convenience function to get typography specs."""
    return get_tokens().get_font_size(context, element)


def get_spacing(scale: Union[int, str]) -> str:
    """Convenience function to get spacing value."""
    return get_tokens().get_spacing(scale)


def get_color_palette(palette_name: str) -> List[str]:
    """Convenience function to get a color palette."""
    return get_tokens().get_color_palette(palette_name)


def get_accessible_pair(use_case: str) -> Tuple[str, str]:
    """Convenience function to get an accessible color pair."""
    return get_tokens().get_accessible_pair(use_case)


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def get_relative_luminance(r: int, g: int, b: int) -> float:
    """
    Calculate relative luminance per WCAG 2.1.

    Args:
        r, g, b: RGB values (0-255)

    Returns:
        Relative luminance (0-1)
    """
    def adjust(channel: int) -> float:
        c = channel / 255
        if c <= 0.03928:
            return c / 12.92
        return ((c + 0.055) / 1.055) ** 2.4

    return 0.2126 * adjust(r) + 0.7152 * adjust(g) + 0.0722 * adjust(b)


def calculate_contrast_ratio(color1: str, color2: str) -> float:
    """
    Calculate WCAG contrast ratio between two colors.

    Args:
        color1, color2: Hex color values

    Returns:
        Contrast ratio (1-21)
    """
    rgb1 = hex_to_rgb(color1)
    rgb2 = hex_to_rgb(color2)

    lum1 = get_relative_luminance(*rgb1)
    lum2 = get_relative_luminance(*rgb2)

    lighter = max(lum1, lum2)
    darker = min(lum1, lum2)

    return (lighter + 0.05) / (darker + 0.05)


def validate_contrast(
    foreground: str,
    background: str,
    level: str = "AA",
    text_size: str = "normal"
) -> bool:
    """
    Validate if two colors meet WCAG contrast requirements.

    Args:
        foreground: Foreground (text) color
        background: Background color
        level: "AA" (4.5:1) or "AAA" (7:1)
        text_size: "normal" (< 18pt) or "large" (>= 18pt or >= 14pt bold)

    Returns:
        True if contrast is sufficient
    """
    ratio = calculate_contrast_ratio(foreground, background)

    # WCAG requirements
    requirements = {
        ("AA", "normal"): 4.5,
        ("AA", "large"): 3.0,
        ("AAA", "normal"): 7.0,
        ("AAA", "large"): 4.5,
    }

    required = requirements.get((level, text_size), 4.5)
    return ratio >= required


def get_contrast_ratio(foreground: str, background: str) -> float:
    """Get the contrast ratio between two colors."""
    return calculate_contrast_ratio(foreground, background)


# Plotly theme generator
def get_plotly_template() -> Dict:
    """
    Generate a Plotly template using design tokens.

    Returns:
        Dict suitable for plotly.io.templates

    Note: Uses modern Plotly API (title.font instead of titlefont)
    """
    tokens = get_tokens()

    return {
        "layout": {
            "font": {
                "family": tokens.get_font_family("primary"),
                "size": 10,
                "color": tokens.get_color("text.primary"),
            },
            "title": {
                "font": {
                    "size": 14,
                    "color": tokens.get_color("text.primary"),
                }
            },
            "paper_bgcolor": tokens.get_color("backgrounds.white"),
            "plot_bgcolor": tokens.get_color("backgrounds.white"),
            "colorway": tokens.get_color_palette("categorical"),
            "xaxis": {
                "gridcolor": tokens.get_color("backgrounds.medium_gray"),
                "linecolor": tokens.get_color("text.secondary"),
                "tickfont": {"size": 8},
                "title": {"font": {"size": 10}},  # Modern Plotly API
            },
            "yaxis": {
                "gridcolor": tokens.get_color("backgrounds.medium_gray"),
                "linecolor": tokens.get_color("text.secondary"),
                "tickfont": {"size": 8},
                "title": {"font": {"size": 10}},  # Modern Plotly API
            },
            "legend": {
                "font": {"size": 9},
                "bgcolor": "rgba(255,255,255,0.8)",
            },
        },
        "data": {
            "scatter": [{"marker": {"size": 8}}],
            "bar": [{"marker": {"line": {"width": 0}}}],
        }
    }


# Matplotlib style generator
def get_matplotlib_style() -> Dict:
    """
    Generate matplotlib rcParams using design tokens.

    Returns:
        Dict suitable for matplotlib.rcParams.update()
    """
    tokens = get_tokens()

    return {
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica", "Arial", "Liberation Sans"],
        "font.size": 8,
        "axes.titlesize": 10,
        "axes.labelsize": 9,
        "xtick.labelsize": 7,
        "ytick.labelsize": 7,
        "legend.fontsize": 8,
        "figure.titlesize": 12,
        "axes.prop_cycle": f"cycler('color', {tokens.get_color_palette('categorical')})",
        "axes.facecolor": tokens.get_color("backgrounds.white"),
        "figure.facecolor": tokens.get_color("backgrounds.white"),
        "axes.edgecolor": tokens.get_color("text.secondary"),
        "axes.labelcolor": tokens.get_color("text.primary"),
        "xtick.color": tokens.get_color("text.secondary"),
        "ytick.color": tokens.get_color("text.secondary"),
        "axes.grid": True,
        "grid.color": tokens.get_color("backgrounds.medium_gray"),
        "grid.linewidth": 0.5,
        "axes.linewidth": 0.8,
        "lines.linewidth": 1.5,
        "figure.dpi": 150,
        "savefig.dpi": 300,
    }


if __name__ == "__main__":
    # Demo usage
    tokens = get_tokens()

    print("=== Design Tokens Demo ===\n")

    # Colors
    print("Primary Navy:", tokens.get_color("primary.navy"))
    print("Categorical Palette:", tokens.get_color_palette("categorical"))

    # Accessible pairs
    treatment, control = tokens.get_accessible_pair("treatment_control")
    print(f"Treatment vs Control: {treatment} / {control}")

    # Contrast validation
    ratio = get_contrast_ratio("#1e3a5f", "#ffffff")
    print(f"Navy on white contrast: {ratio:.1f}:1")
    print(f"WCAG AA compliant: {validate_contrast('#1e3a5f', '#ffffff')}")

    # Typography
    print("\nPanel label size:", tokens.get_font_size("figure_elements", "panel_label"))

    # Spacing
    print("Medium spacing:", tokens.get_spacing("md"))
    print("Panel gap:", tokens.get_layout_spacing("figure_layout", "panel_gap"))
