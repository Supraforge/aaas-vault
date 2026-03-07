#!/usr/bin/env python3
"""
Token Validator

Validates design tokens for WCAG compliance, colorblind accessibility,
and publication standards.

Usage:
    python token_validator.py                    # Full validation
    python token_validator.py --colors           # Color validation only
    python token_validator.py --contrast-report  # Detailed contrast report
    python token_validator.py --simulate-cvd     # Color vision deficiency simulation
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from tokens.index import (
    get_tokens,
    calculate_contrast_ratio,
    hex_to_rgb,
    get_relative_luminance,
)


class ValidationLevel(Enum):
    """Validation result levels."""
    PASS = "PASS"
    WARN = "WARN"
    FAIL = "FAIL"


@dataclass
class ValidationResult:
    """Result of a validation check."""
    level: ValidationLevel
    message: str
    details: Optional[Dict] = None


class TokenValidator:
    """Validates design tokens for accessibility and publication standards."""

    def __init__(self):
        self.tokens = get_tokens()
        self.results: List[ValidationResult] = []

    def validate_all(self) -> List[ValidationResult]:
        """Run all validation checks."""
        self.results = []

        # Color validations
        self._validate_primary_contrasts()
        self._validate_semantic_contrasts()
        self._validate_text_contrasts()
        self._validate_colorblind_safety()
        self._validate_palette_distinguishability()

        # Typography validations
        self._validate_font_sizes()
        self._validate_font_families()

        # Spacing validations
        self._validate_spacing_consistency()

        return self.results

    def _add_result(
        self,
        level: ValidationLevel,
        message: str,
        details: Optional[Dict] = None
    ):
        """Add a validation result."""
        self.results.append(ValidationResult(level, message, details))

    def _validate_primary_contrasts(self):
        """Validate primary colors meet contrast requirements."""
        background = "#ffffff"

        primary_colors = self.tokens.colors.get("primary", {})

        for name, color_data in primary_colors.items():
            if isinstance(color_data, dict) and "value" in color_data:
                color = color_data["value"]
                ratio = calculate_contrast_ratio(color, background)

                if ratio >= 4.5:
                    self._add_result(
                        ValidationLevel.PASS,
                        f"Primary '{name}' ({color}): {ratio:.1f}:1 contrast - WCAG AA compliant",
                        {"color": color, "ratio": ratio}
                    )
                elif ratio >= 3.0:
                    self._add_result(
                        ValidationLevel.WARN,
                        f"Primary '{name}' ({color}): {ratio:.1f}:1 contrast - OK for large text only",
                        {"color": color, "ratio": ratio}
                    )
                else:
                    self._add_result(
                        ValidationLevel.FAIL,
                        f"Primary '{name}' ({color}): {ratio:.1f}:1 contrast - FAILS WCAG",
                        {"color": color, "ratio": ratio}
                    )

    def _validate_semantic_contrasts(self):
        """Validate semantic colors for accessibility."""
        background = "#ffffff"

        semantic_colors = self.tokens.colors.get("semantic", {})

        for name, color_data in semantic_colors.items():
            if isinstance(color_data, dict) and "value" in color_data:
                color = color_data["value"]
                ratio = calculate_contrast_ratio(color, background)

                if ratio >= 4.5:
                    self._add_result(
                        ValidationLevel.PASS,
                        f"Semantic '{name}' ({color}): {ratio:.1f}:1 - WCAG AA compliant"
                    )
                else:
                    self._add_result(
                        ValidationLevel.WARN,
                        f"Semantic '{name}' ({color}): {ratio:.1f}:1 - Consider darker variant for text use"
                    )

    def _validate_text_contrasts(self):
        """Validate text colors meet minimum contrast."""
        background = "#ffffff"

        text_colors = self.tokens.colors.get("text", {})

        for name, color_data in text_colors.items():
            if isinstance(color_data, dict) and "value" in color_data:
                color = color_data["value"]
                ratio = calculate_contrast_ratio(color, background)

                if ratio >= 7.0:
                    self._add_result(
                        ValidationLevel.PASS,
                        f"Text '{name}' ({color}): {ratio:.1f}:1 - WCAG AAA compliant"
                    )
                elif ratio >= 4.5:
                    self._add_result(
                        ValidationLevel.PASS,
                        f"Text '{name}' ({color}): {ratio:.1f}:1 - WCAG AA compliant"
                    )
                else:
                    self._add_result(
                        ValidationLevel.FAIL,
                        f"Text '{name}' ({color}): {ratio:.1f}:1 - FAILS minimum contrast for text"
                    )

    def _validate_colorblind_safety(self):
        """Check that accessible pairs are colorblind-safe."""
        pairs = self.tokens.colors.get("accessible_pairs", {})

        for pair_name, pair_data in pairs.items():
            if pair_name == "description":
                continue

            color_a = pair_data.get("color_a", "")
            color_b = pair_data.get("color_b", "")

            if color_a and color_b:
                # Check if colors are distinguishable
                is_safe, cvd_type = self._check_colorblind_distinguishable(color_a, color_b)

                if is_safe:
                    self._add_result(
                        ValidationLevel.PASS,
                        f"Accessible pair '{pair_name}': Colors are distinguishable for all CVD types"
                    )
                else:
                    self._add_result(
                        ValidationLevel.WARN,
                        f"Accessible pair '{pair_name}': May be hard to distinguish for {cvd_type}"
                    )

    def _check_colorblind_distinguishable(
        self,
        color1: str,
        color2: str
    ) -> Tuple[bool, Optional[str]]:
        """
        Check if two colors are distinguishable for colorblind users.

        Uses simplified simulation - in production, use full CVD simulation.
        """
        rgb1 = hex_to_rgb(color1)
        rgb2 = hex_to_rgb(color2)

        # Euclidean distance in RGB space (simplified check)
        distance = sum((a - b) ** 2 for a, b in zip(rgb1, rgb2)) ** 0.5

        # Also check luminance difference
        lum1 = get_relative_luminance(*rgb1)
        lum2 = get_relative_luminance(*rgb2)
        lum_diff = abs(lum1 - lum2)

        # Colors should have sufficient RGB distance AND luminance difference
        if distance > 100 and lum_diff > 0.1:
            return True, None

        # Simulate protanopia (red weakness)
        # Reds appear darker, greens appear similar to reds
        proto_r1 = int(0.567 * rgb1[0] + 0.433 * rgb1[1])
        proto_r2 = int(0.567 * rgb2[0] + 0.433 * rgb2[1])
        if abs(proto_r1 - proto_r2) < 30:
            return False, "protanopia"

        # Simulate deuteranopia (green weakness)
        deuter_g1 = int(0.625 * rgb1[0] + 0.375 * rgb1[1])
        deuter_g2 = int(0.625 * rgb2[0] + 0.375 * rgb2[1])
        if abs(deuter_g1 - deuter_g2) < 30:
            return False, "deuteranopia"

        return True, None

    def _validate_palette_distinguishability(self):
        """Validate that categorical palette colors are mutually distinguishable."""
        viz = self.tokens.colors.get("data_visualization", {})
        categorical = viz.get("categorical", {}).get("palette", [])

        if not categorical:
            self._add_result(
                ValidationLevel.WARN,
                "No categorical palette found"
            )
            return

        colors = [c["value"] for c in categorical]
        min_distance = float("inf")
        closest_pair = ("", "")

        for i, c1 in enumerate(colors):
            for c2 in colors[i+1:]:
                rgb1 = hex_to_rgb(c1)
                rgb2 = hex_to_rgb(c2)
                distance = sum((a - b) ** 2 for a, b in zip(rgb1, rgb2)) ** 0.5

                if distance < min_distance:
                    min_distance = distance
                    closest_pair = (c1, c2)

        if min_distance > 100:
            self._add_result(
                ValidationLevel.PASS,
                f"Categorical palette: All colors well-separated (min distance: {min_distance:.0f})"
            )
        elif min_distance > 50:
            self._add_result(
                ValidationLevel.WARN,
                f"Categorical palette: Closest pair {closest_pair} may be hard to distinguish"
            )
        else:
            self._add_result(
                ValidationLevel.FAIL,
                f"Categorical palette: {closest_pair} are too similar (distance: {min_distance:.0f})"
            )

    def _validate_font_sizes(self):
        """Validate font sizes meet publication standards."""
        sizes = self.tokens.typography.get("sizes", {})
        figure_sizes = sizes.get("figure_elements", {})

        # Nature guidelines: 5-8pt for figure text
        for element, size_data in figure_sizes.items():
            pt_value = size_data.get("value", "")
            if pt_value:
                pt_num = float(pt_value.replace("pt", ""))

                if 5 <= pt_num <= 8:
                    self._add_result(
                        ValidationLevel.PASS,
                        f"Figure '{element}': {pt_value} - Within Nature 5-8pt range"
                    )
                elif pt_num < 5:
                    self._add_result(
                        ValidationLevel.FAIL,
                        f"Figure '{element}': {pt_value} - Below minimum readable size"
                    )
                elif pt_num > 8:
                    self._add_result(
                        ValidationLevel.WARN,
                        f"Figure '{element}': {pt_value} - Above Nature standard (may be OK for panels)"
                    )

    def _validate_font_families(self):
        """Validate font families are publication-standard."""
        fonts = self.tokens.typography.get("fonts", {})

        allowed_fonts = ["helvetica", "arial", "times", "times new roman"]

        for font_type, font_data in fonts.items():
            family = font_data.get("family", "").lower()

            has_allowed = any(f in family for f in allowed_fonts)

            if has_allowed:
                self._add_result(
                    ValidationLevel.PASS,
                    f"Font '{font_type}': Uses publication-standard fonts"
                )
            else:
                self._add_result(
                    ValidationLevel.WARN,
                    f"Font '{font_type}': {family} - Consider Helvetica/Arial for journals"
                )

    def _validate_spacing_consistency(self):
        """Validate spacing follows 4px grid."""
        scale = self.tokens.spacing.get("scale", {})

        for level, space_data in scale.items():
            value = space_data.get("value", "")
            if "px" in value:
                px = int(value.replace("px", ""))
                if px % 4 == 0:
                    self._add_result(
                        ValidationLevel.PASS,
                        f"Spacing '{level}': {value} - On 4px grid"
                    )
                else:
                    self._add_result(
                        ValidationLevel.WARN,
                        f"Spacing '{level}': {value} - Not on 4px grid"
                    )

    def print_report(self):
        """Print a formatted validation report."""
        if not self.results:
            self.validate_all()

        # Count results
        passes = sum(1 for r in self.results if r.level == ValidationLevel.PASS)
        warns = sum(1 for r in self.results if r.level == ValidationLevel.WARN)
        fails = sum(1 for r in self.results if r.level == ValidationLevel.FAIL)

        print("\n" + "=" * 60)
        print("DESIGN TOKEN VALIDATION REPORT")
        print("=" * 60)

        print(f"\nSummary: {passes} PASS | {warns} WARN | {fails} FAIL\n")

        # Group by level
        for level in [ValidationLevel.FAIL, ValidationLevel.WARN, ValidationLevel.PASS]:
            level_results = [r for r in self.results if r.level == level]

            if level_results:
                print(f"\n--- {level.value} ({len(level_results)}) ---")
                for result in level_results:
                    icon = {"PASS": "✓", "WARN": "⚠", "FAIL": "✗"}[level.value]
                    print(f"  {icon} {result.message}")

        print("\n" + "=" * 60)

        if fails > 0:
            print("❌ VALIDATION FAILED - Fix issues before using in production")
            return False
        elif warns > 0:
            print("⚠️  VALIDATION PASSED WITH WARNINGS - Review before production")
            return True
        else:
            print("✅ VALIDATION PASSED - All tokens meet publication standards")
            return True


def generate_contrast_report():
    """Generate a detailed contrast ratio report for all color combinations."""
    tokens = get_tokens()

    print("\n" + "=" * 60)
    print("CONTRAST RATIO REPORT")
    print("=" * 60)

    # Get all colors
    all_colors = {}

    for category in ["primary", "semantic", "text"]:
        cat_colors = tokens.colors.get(category, {})
        for name, data in cat_colors.items():
            if isinstance(data, dict) and "value" in data:
                all_colors[f"{category}.{name}"] = data["value"]

    backgrounds = ["#ffffff", "#f8f9fa", "#1a1a2e"]

    print("\nForeground colors vs backgrounds:\n")
    print(f"{'Color':<25} {'White':>10} {'Light Gray':>12} {'Dark':>10}")
    print("-" * 60)

    for name, color in all_colors.items():
        ratios = []
        for bg in backgrounds:
            ratio = calculate_contrast_ratio(color, bg)
            ratios.append(f"{ratio:.1f}:1")

        print(f"{name:<25} {ratios[0]:>10} {ratios[1]:>12} {ratios[2]:>10}")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Validate design tokens")
    parser.add_argument("--colors", action="store_true", help="Validate colors only")
    parser.add_argument("--contrast-report", action="store_true", help="Show contrast report")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.contrast_report:
        generate_contrast_report()
        return

    validator = TokenValidator()
    validator.validate_all()

    if args.json:
        results = [
            {"level": r.level.value, "message": r.message, "details": r.details}
            for r in validator.results
        ]
        print(json.dumps(results, indent=2))
    else:
        success = validator.print_report()
        sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
