"""
StatCard Component

Displays a big number with context - perfect for highlighting key statistics
from clinical trials, study results, or health metrics.

Usage:
    card = StatCard(
        value="26%",
        label="Mortality Reduction",
        sublabel="HR 0.74, 95% CI 0.65-0.85",
        source="PARADIGM-HF Trial"
    )
    card.render("output.png")
"""

import json
import os
import subprocess
from pathlib import Path
from typing import Optional

from .base import Component, RenderBackend, RenderConfig, NotImplementedBackend, get_drawsvg


class StatCard(Component):
    """
    StatCard component for displaying key statistics.

    Best backends: SATORI (primary), DRAWSVG (alternative)
    """

    DEFAULT_BACKEND = RenderBackend.SATORI
    SUPPORTED_BACKENDS = [RenderBackend.SATORI, RenderBackend.DRAWSVG]

    def __init__(
        self,
        value: str,
        label: str,
        sublabel: Optional[str] = None,
        trend: Optional[str] = None,  # "up", "down", or None
        trend_color: Optional[str] = None,  # "success", "danger", or hex
        source: Optional[str] = None,
        title: Optional[str] = None,
        config: Optional[RenderConfig] = None,
    ):
        """
        Initialize StatCard.

        Args:
            value: The main statistic (e.g., "26%", "42", "3.5x")
            label: Description of the statistic
            sublabel: Additional context (e.g., confidence interval)
            trend: Direction arrow ("up", "down", or None)
            trend_color: Color for trend arrow
            source: Data source citation
            title: Optional title above the card
            config: Render configuration
        """
        super().__init__(title=title, source=source, config=config)
        self.value = value
        self.label = label
        self.sublabel = sublabel
        self.trend = trend
        self.trend_color = trend_color

    def to_dict(self):
        """Convert to Satori-compatible JSON."""
        data = {
            "value": self.value,
            "label": self.label,
        }
        if self.sublabel:
            data["sublabel"] = self.sublabel
        if self.source:
            data["source"] = self.source
        if self.trend:
            data["trend"] = self.trend
        if self.trend_color:
            data["trendColor"] = self.trend_color
        return data

    def _render_satori(self, output_path: str) -> str:
        """Render using Satori (Node.js)."""
        satori_dir = Path(__file__).parent.parent / "satori"
        renderer_js = satori_dir / "renderer.js"

        if not renderer_js.exists():
            raise FileNotFoundError(f"Satori renderer not found at {renderer_js}")

        # Prepare data
        data_json = json.dumps(self.to_dict())

        # Build command
        cmd = [
            "node", str(renderer_js),
            "--template", "stat-card",
            "--data", data_json,
            "--width", str(self.config.width),
            "--height", str(self.config.height),
            "-o", output_path
        ]

        # Run renderer
        result = subprocess.run(
            cmd,
            cwd=str(satori_dir),
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise RuntimeError(f"Satori render failed: {result.stderr}")

        return output_path

    def _render_drawsvg(self, output_path: str) -> str:
        """Render using drawsvg (pure Python)."""
        try:
            dw = get_drawsvg()
        except Exception:
            raise ImportError("drawsvg not installed. Run: pip install drawsvg cairosvg")

        # Get colors from tokens
        bg_color = self.get_color("backgrounds.white")
        text_primary = self.get_color("text.primary")
        text_secondary = self.get_color("text.secondary")
        accent = self.get_color("primary.navy")

        # Create drawing
        width, height = self.config.width, self.config.height
        d = dw.Drawing(width, height)

        # Background
        d.append(dw.Rectangle(0, 0, width, height, fill=bg_color))

        # Value (large centered text)
        value_y = height * 0.4
        d.append(dw.Text(
            self.value,
            x=width / 2,
            y=value_y,
            font_size=72,
            font_family="Helvetica, Arial, sans-serif",
            font_weight="bold",
            fill=accent,
            text_anchor="middle",
            dominant_baseline="middle"
        ))

        # Label
        label_y = value_y + 60
        d.append(dw.Text(
            self.label,
            x=width / 2,
            y=label_y,
            font_size=24,
            font_family="Helvetica, Arial, sans-serif",
            fill=text_primary,
            text_anchor="middle",
            dominant_baseline="middle"
        ))

        # Sublabel
        if self.sublabel:
            sublabel_y = label_y + 35
            d.append(dw.Text(
                self.sublabel,
                x=width / 2,
                y=sublabel_y,
                font_size=16,
                font_family="Helvetica, Arial, sans-serif",
                fill=text_secondary,
                text_anchor="middle",
                dominant_baseline="middle"
            ))

        # Source
        if self.source:
            d.append(dw.Text(
                f"Source: {self.source}",
                x=width / 2,
                y=height - 30,
                font_size=12,
                font_family="Helvetica, Arial, sans-serif",
                fill=text_secondary,
                text_anchor="middle"
            ))

        # Save
        if output_path.endswith(".png"):
            d.save_png(output_path)
        else:
            d.save_svg(output_path)

        return output_path

    def _render_plotly(self, output_path: str) -> str:
        """Plotly is not optimal for stat cards."""
        raise NotImplementedBackend(
            "StatCard does not support Plotly backend. Use SATORI or DRAWSVG."
        )

    def _select_backend(self) -> RenderBackend:
        """Prefer Satori for stat cards."""
        return RenderBackend.SATORI


def create_stat_card(
    value: str,
    label: str,
    sublabel: Optional[str] = None,
    source: Optional[str] = None,
    output: str = "stat_card.png",
    **kwargs
) -> str:
    """
    Quick function to create and render a StatCard.

    Args:
        value: The main statistic
        label: Description
        sublabel: Additional context
        source: Data source
        output: Output file path
        **kwargs: Additional options

    Returns:
        Path to rendered file
    """
    card = StatCard(
        value=value,
        label=label,
        sublabel=sublabel,
        source=source,
    )
    return card.render(output, **kwargs)
