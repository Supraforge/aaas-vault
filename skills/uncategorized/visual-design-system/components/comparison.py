"""
ComparisonChart Component

Side-by-side comparison of two values - ideal for treatment vs control,
before/after, or any two-group comparison.

Usage:
    chart = ComparisonChart(
        title="DAPA-HF Primary Endpoint",
        left_value="11.4%",
        left_label="Dapagliflozin",
        right_value="15.6%",
        right_label="Placebo",
        metric="CV Death or HF Hospitalization"
    )
    chart.render("comparison.png")
"""

import json
import os
import subprocess
from pathlib import Path
from typing import Optional, List

from .base import Component, RenderBackend, RenderConfig, NotImplementedBackend, get_drawsvg


class ComparisonChart(Component):
    """
    ComparisonChart component for side-by-side comparisons.

    Best backends: SATORI (infographic style), PLOTLY (bar chart style)
    """

    DEFAULT_BACKEND = RenderBackend.SATORI
    SUPPORTED_BACKENDS = [RenderBackend.SATORI, RenderBackend.PLOTLY, RenderBackend.DRAWSVG]

    def __init__(
        self,
        left_value: str,
        left_label: str,
        right_value: str,
        right_label: str,
        title: Optional[str] = None,
        metric: Optional[str] = None,
        difference: Optional[str] = None,  # e.g., "26% reduction"
        source: Optional[str] = None,
        highlight: str = "left",  # "left", "right", or "none"
        config: Optional[RenderConfig] = None,
    ):
        """
        Initialize ComparisonChart.

        Args:
            left_value: Value for left side
            left_label: Label for left side (e.g., "Treatment")
            right_value: Value for right side
            right_label: Label for right side (e.g., "Control")
            title: Chart title
            metric: What is being measured
            difference: Optional difference text
            source: Data source citation
            highlight: Which side to highlight
            config: Render configuration
        """
        super().__init__(title=title, source=source, config=config)
        self.left_value = left_value
        self.left_label = left_label
        self.right_value = right_value
        self.right_label = right_label
        self.metric = metric
        self.difference = difference
        self.highlight = highlight

    def to_dict(self):
        """Convert to Satori-compatible JSON."""
        data = {
            "title": self.title or "Comparison",
            "left": {
                "value": self.left_value,
                "label": self.left_label,
            },
            "right": {
                "value": self.right_value,
                "label": self.right_label,
            },
        }
        if self.metric:
            data["metric"] = self.metric
        if self.difference:
            data["difference"] = self.difference
        if self.source:
            data["source"] = self.source
        return data

    def _render_satori(self, output_path: str) -> str:
        """Render using Satori (Node.js)."""
        satori_dir = Path(__file__).parent.parent / "satori"
        renderer_js = satori_dir / "renderer.js"

        if not renderer_js.exists():
            raise FileNotFoundError(f"Satori renderer not found at {renderer_js}")

        data_json = json.dumps(self.to_dict())

        cmd = [
            "node", str(renderer_js),
            "--template", "comparison",
            "--data", data_json,
            "--width", str(self.config.width),
            "--height", str(self.config.height),
            "-o", output_path
        ]

        result = subprocess.run(
            cmd,
            cwd=str(satori_dir),
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise RuntimeError(f"Satori render failed: {result.stderr}")

        return output_path

    def _render_plotly(self, output_path: str) -> str:
        """Render as a bar chart using Plotly."""
        import sys
        sys.path.insert(0, str(Path(__file__).parent.parent.parent / "cardiology-visual-system" / "scripts"))

        try:
            import plotly.graph_objects as go
        except ImportError:
            raise ImportError("plotly not installed. Run: pip install plotly kaleido")

        # Get accessible colors
        left_color, right_color = self.get_accessible_colors("treatment_control")

        # Parse values (remove % if present)
        left_val = float(self.left_value.replace("%", "").replace(",", ""))
        right_val = float(self.right_value.replace("%", "").replace(",", ""))

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=[self.left_label],
            y=[left_val],
            name=self.left_label,
            marker_color=left_color,
            text=[self.left_value],
            textposition="outside",
            textfont=dict(size=16, family="Helvetica, Arial, sans-serif"),
        ))

        fig.add_trace(go.Bar(
            x=[self.right_label],
            y=[right_val],
            name=self.right_label,
            marker_color=right_color,
            text=[self.right_value],
            textposition="outside",
            textfont=dict(size=16, family="Helvetica, Arial, sans-serif"),
        ))

        fig.update_layout(
            title=dict(
                text=self.title or "Comparison",
                font=dict(size=20, family="Helvetica, Arial, sans-serif"),
            ),
            xaxis_title=self.metric or "",
            yaxis_title="",
            showlegend=False,
            barmode="group",
            font=dict(family="Helvetica, Arial, sans-serif"),
            plot_bgcolor="white",
            paper_bgcolor="white",
            margin=dict(t=80, b=60, l=60, r=40),
        )

        # Add source annotation
        if self.source:
            fig.add_annotation(
                text=f"Source: {self.source}",
                xref="paper", yref="paper",
                x=0.5, y=-0.1,
                showarrow=False,
                font=dict(size=10, color="#6c757d"),
            )

        # Export
        scale = 4 if self.config.quality == "print" else 2
        if output_path.endswith(".html"):
            fig.write_html(output_path)
        else:
            fig.write_image(output_path, width=self.config.width, height=self.config.height, scale=scale)

        return output_path

    def _render_drawsvg(self, output_path: str) -> str:
        """Render using drawsvg."""
        try:
            dw = get_drawsvg()
        except Exception:
            raise ImportError("drawsvg not installed. Run: pip install drawsvg cairosvg")

        # Get colors
        left_color, right_color = self.get_accessible_colors("treatment_control")
        bg_color = self.get_color("backgrounds.white")
        text_primary = self.get_color("text.primary")
        text_secondary = self.get_color("text.secondary")

        width, height = self.config.width, self.config.height
        d = dw.Drawing(width, height)

        # Background
        d.append(dw.Rectangle(0, 0, width, height, fill=bg_color))

        # Title
        if self.title:
            d.append(dw.Text(
                self.title,
                x=width / 2,
                y=50,
                font_size=24,
                font_family="Helvetica, Arial, sans-serif",
                font_weight="bold",
                fill=text_primary,
                text_anchor="middle"
            ))

        # Left panel
        left_x = width * 0.25
        panel_y = height * 0.45

        # Left value
        d.append(dw.Text(
            self.left_value,
            x=left_x,
            y=panel_y,
            font_size=48,
            font_family="Helvetica, Arial, sans-serif",
            font_weight="bold",
            fill=left_color,
            text_anchor="middle"
        ))

        # Left label
        d.append(dw.Text(
            self.left_label,
            x=left_x,
            y=panel_y + 40,
            font_size=18,
            font_family="Helvetica, Arial, sans-serif",
            fill=text_primary,
            text_anchor="middle"
        ))

        # VS divider
        d.append(dw.Text(
            "vs",
            x=width / 2,
            y=panel_y,
            font_size=20,
            font_family="Helvetica, Arial, sans-serif",
            fill=text_secondary,
            text_anchor="middle"
        ))

        # Right panel
        right_x = width * 0.75

        # Right value
        d.append(dw.Text(
            self.right_value,
            x=right_x,
            y=panel_y,
            font_size=48,
            font_family="Helvetica, Arial, sans-serif",
            font_weight="bold",
            fill=right_color,
            text_anchor="middle"
        ))

        # Right label
        d.append(dw.Text(
            self.right_label,
            x=right_x,
            y=panel_y + 40,
            font_size=18,
            font_family="Helvetica, Arial, sans-serif",
            fill=text_primary,
            text_anchor="middle"
        ))

        # Difference (if provided)
        if self.difference:
            d.append(dw.Text(
                self.difference,
                x=width / 2,
                y=height * 0.75,
                font_size=20,
                font_family="Helvetica, Arial, sans-serif",
                fill=self.get_color("semantic.success"),
                text_anchor="middle"
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

    def _select_backend(self) -> RenderBackend:
        """Prefer Satori for infographic style, Plotly for charts."""
        return RenderBackend.SATORI


def create_comparison(
    title: str,
    left_value: str,
    left_label: str,
    right_value: str,
    right_label: str,
    metric: Optional[str] = None,
    source: Optional[str] = None,
    output: str = "comparison.png",
    backend: str = "satori",
    **kwargs
) -> str:
    """
    Quick function to create and render a ComparisonChart.

    Args:
        title: Chart title
        left_value: Left value
        left_label: Left label
        right_value: Right value
        right_label: Right label
        metric: What's being measured
        source: Data source
        output: Output file path
        backend: "satori", "plotly", or "drawsvg"
        **kwargs: Additional options

    Returns:
        Path to rendered file
    """
    chart = ComparisonChart(
        title=title,
        left_value=left_value,
        left_label=left_label,
        right_value=right_value,
        right_label=right_label,
        metric=metric,
        source=source,
    )
    return chart.render(output, backend=backend, **kwargs)
