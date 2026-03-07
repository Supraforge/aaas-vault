"""
Timeline Component

Patient journey or temporal progression visualization.
Shows stages, events, and milestones over time.

Usage:
    timeline = Timeline(
        title="Heart Failure Patient Journey",
        stages=[
            {"name": "Diagnosis", "duration": "Day 1", "events": ["ECG", "Blood tests"]},
            {"name": "Treatment", "duration": "Days 2-7", "events": ["Medication", "Monitoring"]},
            {"name": "Recovery", "duration": "Weeks 2-4", "events": ["Cardiac rehab"]},
        ]
    )
    timeline.render("journey.png")
"""

import os
from pathlib import Path
from typing import Optional, List, Dict, Any

from .base import Component, RenderBackend, RenderConfig, get_drawsvg


class Timeline(Component):
    """
    Timeline component for patient journeys and temporal progressions.

    Best backends: DRAWSVG (for publication), SATORI (for infographic style)
    """

    DEFAULT_BACKEND = RenderBackend.DRAWSVG
    SUPPORTED_BACKENDS = [RenderBackend.DRAWSVG, RenderBackend.SATORI]

    def __init__(
        self,
        stages: List[Dict[str, Any]],
        title: Optional[str] = None,
        orientation: str = "horizontal",  # "horizontal" or "vertical"
        show_connectors: bool = True,
        source: Optional[str] = None,
        config: Optional[RenderConfig] = None,
    ):
        """
        Initialize Timeline.

        Args:
            stages: List of stage dictionaries with keys:
                - name: Stage name
                - duration: Time period (e.g., "Day 1", "Weeks 2-4")
                - events: Optional list of events
                - color: Optional custom color
            title: Timeline title
            orientation: "horizontal" or "vertical"
            show_connectors: Show arrows between stages
            source: Data source citation
            config: Render configuration
        """
        super().__init__(title=title, source=source, config=config)
        self.stages = stages
        self.orientation = orientation
        self.show_connectors = show_connectors

    def _render_satori(self, output_path: str) -> str:
        """Render using Satori (process-flow template)."""
        import json
        import subprocess

        satori_dir = Path(__file__).parent.parent / "satori"
        renderer_js = satori_dir / "renderer.js"

        if not renderer_js.exists():
            raise FileNotFoundError(f"Satori renderer not found at {renderer_js}")

        # Convert stages to steps format
        steps = []
        for stage in self.stages:
            step = {
                "title": stage["name"],
                "description": stage.get("duration", ""),
            }
            if stage.get("events"):
                step["description"] += "\n" + ", ".join(stage["events"])
            steps.append(step)

        data = {
            "title": self.title or "Timeline",
            "steps": steps,
        }

        cmd = [
            "node", str(renderer_js),
            "--template", "process-flow",
            "--data", json.dumps(data),
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
        """Plotly not ideal for timelines - use drawsvg."""
        return self._render_drawsvg(output_path)

    def _render_drawsvg(self, output_path: str) -> str:
        """Render using drawsvg."""
        try:
            dw = get_drawsvg()
        except Exception:
            raise ImportError("drawsvg not installed. Run: pip install drawsvg cairosvg")

        # Get colors
        palette = self.get_palette("categorical")
        bg_color = self.get_color("backgrounds.white")
        text_primary = self.get_color("text.primary")
        text_secondary = self.get_color("text.secondary")
        connector_color = self.get_color("text.muted")

        width, height = self.config.width, self.config.height
        d = dw.Drawing(width, height)
        d.append(dw.Rectangle(0, 0, width, height, fill=bg_color))

        # Title
        title_y = 50
        if self.title:
            d.append(dw.Text(
                self.title,
                x=width / 2,
                y=title_y,
                font_size=24,
                font_family="Helvetica, Arial, sans-serif",
                font_weight="bold",
                fill=text_primary,
                text_anchor="middle"
            ))
            title_y += 30

        n_stages = len(self.stages)

        if self.orientation == "horizontal":
            # Horizontal timeline
            margin_x = 80
            stage_width = (width - 2 * margin_x) / n_stages
            center_y = height / 2

            # Draw timeline line
            d.append(dw.Line(
                margin_x, center_y,
                width - margin_x, center_y,
                stroke=connector_color,
                stroke_width=2
            ))

            for i, stage in enumerate(self.stages):
                x = margin_x + (i + 0.5) * stage_width
                color = stage.get("color", palette[i % len(palette)])

                # Stage circle
                d.append(dw.Circle(
                    x, center_y,
                    30,
                    fill=color,
                    stroke=color,
                    stroke_width=2
                ))

                # Stage number
                d.append(dw.Text(
                    str(i + 1),
                    x=x,
                    y=center_y + 6,
                    font_size=18,
                    font_family="Helvetica, Arial, sans-serif",
                    font_weight="bold",
                    fill="white",
                    text_anchor="middle"
                ))

                # Stage name
                d.append(dw.Text(
                    stage["name"],
                    x=x,
                    y=center_y - 50,
                    font_size=14,
                    font_family="Helvetica, Arial, sans-serif",
                    font_weight="bold",
                    fill=text_primary,
                    text_anchor="middle"
                ))

                # Duration
                if stage.get("duration"):
                    d.append(dw.Text(
                        stage["duration"],
                        x=x,
                        y=center_y + 55,
                        font_size=11,
                        font_family="Helvetica, Arial, sans-serif",
                        fill=text_secondary,
                        text_anchor="middle"
                    ))

                # Events
                if stage.get("events"):
                    events_y = center_y + 75
                    for j, event in enumerate(stage["events"][:3]):  # Max 3 events
                        d.append(dw.Text(
                            f"• {event}",
                            x=x,
                            y=events_y + j * 16,
                            font_size=10,
                            font_family="Helvetica, Arial, sans-serif",
                            fill=text_secondary,
                            text_anchor="middle"
                        ))

        else:
            # Vertical timeline
            margin_y = 100
            margin_x = width * 0.3
            stage_height = (height - 2 * margin_y) / n_stages

            # Draw timeline line
            d.append(dw.Line(
                margin_x, margin_y,
                margin_x, height - margin_y,
                stroke=connector_color,
                stroke_width=2
            ))

            for i, stage in enumerate(self.stages):
                y = margin_y + (i + 0.5) * stage_height
                color = stage.get("color", palette[i % len(palette)])

                # Stage circle
                d.append(dw.Circle(
                    margin_x, y,
                    20,
                    fill=color,
                    stroke=color,
                    stroke_width=2
                ))

                # Stage number
                d.append(dw.Text(
                    str(i + 1),
                    x=margin_x,
                    y=y + 5,
                    font_size=14,
                    font_family="Helvetica, Arial, sans-serif",
                    font_weight="bold",
                    fill="white",
                    text_anchor="middle"
                ))

                # Stage name
                d.append(dw.Text(
                    stage["name"],
                    x=margin_x + 40,
                    y=y - 5,
                    font_size=14,
                    font_family="Helvetica, Arial, sans-serif",
                    font_weight="bold",
                    fill=text_primary,
                ))

                # Duration
                if stage.get("duration"):
                    d.append(dw.Text(
                        stage["duration"],
                        x=margin_x + 40,
                        y=y + 15,
                        font_size=11,
                        font_family="Helvetica, Arial, sans-serif",
                        fill=text_secondary,
                    ))

                # Events
                if stage.get("events"):
                    events_text = " | ".join(stage["events"][:3])
                    d.append(dw.Text(
                        events_text,
                        x=margin_x + 40,
                        y=y + 30,
                        font_size=10,
                        font_family="Helvetica, Arial, sans-serif",
                        fill=text_secondary,
                    ))

        # Source
        if self.source:
            d.append(dw.Text(
                f"Source: {self.source}",
                x=width / 2,
                y=height - 25,
                font_size=10,
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
        """Prefer drawsvg for timelines."""
        return RenderBackend.DRAWSVG


def create_timeline(
    stages: List[Dict[str, Any]],
    title: Optional[str] = None,
    orientation: str = "horizontal",
    output: str = "timeline.png",
    backend: str = "drawsvg",
    **kwargs
) -> str:
    """
    Quick function to create and render a Timeline.

    Args:
        stages: List of stage dictionaries
        title: Timeline title
        orientation: "horizontal" or "vertical"
        output: Output file path
        backend: "drawsvg" or "satori"
        **kwargs: Additional options

    Returns:
        Path to rendered file
    """
    timeline = Timeline(
        stages=stages,
        title=title,
        orientation=orientation,
    )
    return timeline.render(output, backend=backend, **kwargs)
