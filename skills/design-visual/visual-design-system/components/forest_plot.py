"""
ForestPlot Component

Meta-analysis forest plot following publication standards.
Shows effect estimates with confidence intervals for multiple studies.

Usage:
    studies = [
        {"name": "DAPA-HF", "estimate": 0.74, "lower": 0.65, "upper": 0.85, "weight": 60},
        {"name": "EMPEROR-Reduced", "estimate": 0.75, "lower": 0.65, "upper": 0.86, "weight": 50},
    ]
    plot = ForestPlot(
        studies=studies,
        title="SGLT2 Inhibitors in Heart Failure",
        x_label="Hazard Ratio (95% CI)"
    )
    plot.render("forest.png")
"""

import os
from pathlib import Path
from typing import Optional, List, Dict, Any

from .base import Component, RenderBackend, RenderConfig, get_drawsvg


class ForestPlot(Component):
    """
    ForestPlot component for meta-analysis visualization.

    Best backends: PLOTLY (for interactivity), DRAWSVG (for publication)
    """

    DEFAULT_BACKEND = RenderBackend.PLOTLY
    SUPPORTED_BACKENDS = [RenderBackend.PLOTLY, RenderBackend.DRAWSVG]

    def __init__(
        self,
        studies: List[Dict[str, Any]],
        title: Optional[str] = None,
        x_label: str = "Hazard Ratio (95% CI)",
        null_value: float = 1.0,
        show_pooled: bool = True,
        pooled_estimate: Optional[Dict[str, float]] = None,
        source: Optional[str] = None,
        config: Optional[RenderConfig] = None,
    ):
        """
        Initialize ForestPlot.

        Args:
            studies: List of study dictionaries with keys:
                - name: Study name
                - estimate: Point estimate (HR, OR, RR)
                - lower: Lower CI bound
                - upper: Upper CI bound
                - weight: Optional weight for symbol sizing
            title: Plot title
            x_label: X-axis label
            null_value: Value for null effect line (default 1.0)
            show_pooled: Whether to show pooled estimate
            pooled_estimate: Optional pooled estimate dict (auto-calculated if None)
            source: Data source citation
            config: Render configuration
        """
        super().__init__(title=title, source=source, config=config)
        self.studies = studies
        self.x_label = x_label
        self.null_value = null_value
        self.show_pooled = show_pooled
        self.pooled_estimate = pooled_estimate

    def _calculate_pooled(self) -> Dict[str, float]:
        """Calculate pooled estimate (simple weighted average for demo)."""
        if self.pooled_estimate:
            return self.pooled_estimate

        total_weight = sum(s.get("weight", 1) for s in self.studies)
        weighted_sum = sum(s["estimate"] * s.get("weight", 1) for s in self.studies)
        pooled = weighted_sum / total_weight if total_weight > 0 else 1.0

        # Approximate CI (simplified)
        min_lower = min(s["lower"] for s in self.studies)
        max_upper = max(s["upper"] for s in self.studies)

        return {
            "name": "Pooled",
            "estimate": pooled,
            "lower": min_lower + (pooled - min_lower) * 0.3,
            "upper": max_upper - (max_upper - pooled) * 0.3,
        }

    def _render_satori(self, output_path: str) -> str:
        """Satori not ideal for forest plots."""
        # Fall back to drawsvg
        return self._render_drawsvg(output_path)

    def _render_plotly(self, output_path: str) -> str:
        """Render using Plotly."""
        try:
            import plotly.graph_objects as go
        except ImportError:
            raise ImportError("plotly not installed. Run: pip install plotly kaleido")

        # Get colors
        forest_colors = self._tokens.get_forest_plot_colors()
        point_color = forest_colors.get("point_estimate", self.get_color("primary.navy"))
        null_color = forest_colors.get("null_line", self.get_color("text.muted"))
        diamond_color = forest_colors.get("summary_diamond", self.get_color("primary.blue"))

        # Prepare data
        study_names = [s["name"] for s in self.studies]
        estimates = [s["estimate"] for s in self.studies]
        lowers = [s["lower"] for s in self.studies]
        uppers = [s["upper"] for s in self.studies]
        weights = [s.get("weight", 50) for s in self.studies]

        fig = go.Figure()

        # Add confidence intervals
        for i, study in enumerate(self.studies):
            fig.add_trace(go.Scatter(
                x=[study["lower"], study["upper"]],
                y=[study["name"], study["name"]],
                mode="lines",
                line=dict(color=point_color, width=2),
                showlegend=False,
                hoverinfo="skip",
            ))

        # Add point estimates
        fig.add_trace(go.Scatter(
            x=estimates,
            y=study_names,
            mode="markers",
            marker=dict(
                color=point_color,
                size=[w / 5 + 8 for w in weights],  # Scale by weight
                symbol="square",
            ),
            text=[f"{e:.2f} ({l:.2f}-{u:.2f})" for e, l, u in zip(estimates, lowers, uppers)],
            hoverinfo="text+y",
            showlegend=False,
        ))

        # Add pooled estimate
        if self.show_pooled:
            pooled = self._calculate_pooled()
            study_names.insert(0, "")  # Spacing
            study_names.insert(0, pooled["name"])

            # Diamond shape for pooled
            fig.add_trace(go.Scatter(
                x=[pooled["lower"], pooled["estimate"], pooled["upper"], pooled["estimate"], pooled["lower"]],
                y=[pooled["name"], pooled["name"], pooled["name"], pooled["name"], pooled["name"]],
                mode="lines",
                fill="toself",
                fillcolor=diamond_color,
                line=dict(color=diamond_color),
                showlegend=False,
            ))

        # Null line
        fig.add_vline(
            x=self.null_value,
            line=dict(color=null_color, width=1, dash="dash"),
            annotation_text="Null",
            annotation_position="top",
        )

        # Layout
        fig.update_layout(
            title=dict(
                text=self.title or "Forest Plot",
                font=dict(size=18, family="Helvetica, Arial, sans-serif"),
            ),
            xaxis_title=self.x_label,
            yaxis=dict(
                categoryorder="array",
                categoryarray=list(reversed(study_names)),
            ),
            font=dict(family="Helvetica, Arial, sans-serif"),
            plot_bgcolor="white",
            paper_bgcolor="white",
            showlegend=False,
            margin=dict(l=150, r=80, t=80, b=60),
        )

        # Add source
        if self.source:
            fig.add_annotation(
                text=f"Source: {self.source}",
                xref="paper", yref="paper",
                x=0.5, y=-0.12,
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
        import sys
        sys.path.insert(0, str(Path(__file__).parent.parent / "svg_diagrams"))

        try:
            from data_charts import forest_plot as draw_forest_plot
        except ImportError:
            # Fallback to inline implementation
            return self._render_drawsvg_inline(output_path)

        svg = draw_forest_plot(
            studies=self.studies,
            title=self.title or "Forest Plot",
            x_label=self.x_label,
            show_pooled=self.show_pooled,
        )

        if output_path.endswith(".png"):
            svg.save_png(output_path)
        else:
            svg.save_svg(output_path)

        return output_path

    def _render_drawsvg_inline(self, output_path: str) -> str:
        """Inline drawsvg implementation if module import fails."""
        try:
            dw = get_drawsvg()
        except Exception:
            raise ImportError("drawsvg not installed. Run: pip install drawsvg cairosvg")

        # Colors
        point_color = self.get_color("primary.navy")
        null_color = self.get_color("text.muted")
        text_primary = self.get_color("text.primary")
        bg_color = self.get_color("backgrounds.white")

        width, height = self.config.width, self.config.height
        d = dw.Drawing(width, height)
        d.append(dw.Rectangle(0, 0, width, height, fill=bg_color))

        # Title
        if self.title:
            d.append(dw.Text(
                self.title,
                x=width / 2,
                y=40,
                font_size=18,
                font_family="Helvetica, Arial, sans-serif",
                font_weight="bold",
                fill=text_primary,
                text_anchor="middle"
            ))

        # Plot area
        margin_left = 200
        margin_right = 80
        margin_top = 80
        margin_bottom = 80
        plot_width = width - margin_left - margin_right
        plot_height = height - margin_top - margin_bottom

        # Calculate x scale
        all_values = []
        for s in self.studies:
            all_values.extend([s["lower"], s["upper"]])
        x_min = min(all_values) * 0.9
        x_max = max(all_values) * 1.1

        def x_to_px(val):
            return margin_left + (val - x_min) / (x_max - x_min) * plot_width

        # Draw null line
        null_px = x_to_px(self.null_value)
        d.append(dw.Line(
            null_px, margin_top,
            null_px, height - margin_bottom,
            stroke=null_color,
            stroke_width=1,
            stroke_dasharray="4,4"
        ))

        # Draw studies
        n_studies = len(self.studies)
        row_height = plot_height / (n_studies + 1)

        for i, study in enumerate(self.studies):
            y = margin_top + (i + 0.5) * row_height

            # Study name
            d.append(dw.Text(
                study["name"],
                x=margin_left - 20,
                y=y + 4,
                font_size=12,
                font_family="Helvetica, Arial, sans-serif",
                fill=text_primary,
                text_anchor="end"
            ))

            # Confidence interval line
            x1 = x_to_px(study["lower"])
            x2 = x_to_px(study["upper"])
            d.append(dw.Line(x1, y, x2, y, stroke=point_color, stroke_width=2))

            # Point estimate
            x_point = x_to_px(study["estimate"])
            size = study.get("weight", 50) / 10 + 4
            d.append(dw.Rectangle(
                x_point - size / 2, y - size / 2,
                size, size,
                fill=point_color
            ))

            # CI text
            ci_text = f"{study['estimate']:.2f} ({study['lower']:.2f}-{study['upper']:.2f})"
            d.append(dw.Text(
                ci_text,
                x=width - margin_right + 10,
                y=y + 4,
                font_size=10,
                font_family="Helvetica, Arial, sans-serif",
                fill=text_primary,
            ))

        # X-axis label
        d.append(dw.Text(
            self.x_label,
            x=width / 2,
            y=height - 30,
            font_size=12,
            font_family="Helvetica, Arial, sans-serif",
            fill=text_primary,
            text_anchor="middle"
        ))

        # Save
        if output_path.endswith(".png"):
            d.save_png(output_path)
        else:
            d.save_svg(output_path)

        return output_path

    def _select_backend(self) -> RenderBackend:
        """Prefer Plotly for forest plots (better quality)."""
        return RenderBackend.PLOTLY


def create_forest_plot(
    studies: List[Dict[str, Any]],
    title: Optional[str] = None,
    x_label: str = "Hazard Ratio (95% CI)",
    output: str = "forest_plot.png",
    backend: str = "plotly",
    **kwargs
) -> str:
    """
    Quick function to create and render a ForestPlot.

    Args:
        studies: List of study dictionaries
        title: Plot title
        x_label: X-axis label
        output: Output file path
        backend: "plotly" or "drawsvg"
        **kwargs: Additional options

    Returns:
        Path to rendered file
    """
    plot = ForestPlot(
        studies=studies,
        title=title,
        x_label=x_label,
    )
    return plot.render(output, backend=backend, **kwargs)
