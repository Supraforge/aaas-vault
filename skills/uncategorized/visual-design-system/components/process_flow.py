"""
ProcessFlow Component

Treatment algorithms, decision trees, and step-by-step processes.
Supports both simple linear flows and branching decision nodes.

Usage:
    # Simple linear flow
    flow = ProcessFlow(
        title="HFrEF Treatment Algorithm",
        steps=["Diagnose", "Initiate GDMT", "Titrate", "Follow-up"]
    )
    flow.render("algorithm.png")

    # With decision nodes
    flow = ProcessFlow(
        title="ACS Pathway",
        steps=["Chest pain", "ECG", "Risk stratify", "Treat"],
        decisions=[
            {"after": 1, "question": "STEMI?", "yes": "PCI", "no": "Continue"}
        ]
    )
    flow.render("pathway.png")
"""

import json
import os
import subprocess
from pathlib import Path
from typing import Optional, List, Dict, Any, Union

from .base import Component, RenderBackend, RenderConfig, get_drawsvg


class ProcessFlow(Component):
    """
    ProcessFlow component for treatment algorithms and workflows.

    Best backends: SATORI (infographic), DRAWSVG (publication)
    """

    DEFAULT_BACKEND = RenderBackend.SATORI
    SUPPORTED_BACKENDS = [RenderBackend.SATORI, RenderBackend.DRAWSVG]

    def __init__(
        self,
        steps: List[Union[str, Dict[str, str]]],
        title: Optional[str] = None,
        decisions: Optional[List[Dict[str, Any]]] = None,
        orientation: str = "horizontal",  # "horizontal" or "vertical"
        style: str = "chevron",  # "chevron", "boxes", "circles"
        source: Optional[str] = None,
        config: Optional[RenderConfig] = None,
    ):
        """
        Initialize ProcessFlow.

        Args:
            steps: List of step strings or dictionaries with:
                - title: Step title
                - description: Optional description
            title: Flow title
            decisions: Optional decision nodes with:
                - after: Index of step after which to add decision
                - question: Decision question
                - yes: Action for yes
                - no: Action for no
            orientation: "horizontal" or "vertical"
            style: "chevron", "boxes", or "circles"
            source: Data source citation
            config: Render configuration
        """
        super().__init__(title=title, source=source, config=config)

        # Normalize steps to dict format
        self.steps = []
        for step in steps:
            if isinstance(step, str):
                self.steps.append({"title": step, "description": ""})
            else:
                self.steps.append(step)

        self.decisions = decisions or []
        self.orientation = orientation
        self.style = style

    def _render_satori(self, output_path: str) -> str:
        """Render using Satori (process-flow template)."""
        satori_dir = Path(__file__).parent.parent / "satori"
        renderer_js = satori_dir / "renderer.js"

        if not renderer_js.exists():
            raise FileNotFoundError(f"Satori renderer not found at {renderer_js}")

        data = {
            "title": self.title or "Process Flow",
            "steps": self.steps,
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
        """Plotly not ideal for process flows."""
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
        decision_color = self.get_color("semantic.warning")

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

        n_steps = len(self.steps)

        if self.orientation == "horizontal":
            # Horizontal flow (chevron style)
            margin_x = 60
            step_width = (width - 2 * margin_x) / n_steps
            center_y = height / 2

            for i, step in enumerate(self.steps):
                x = margin_x + i * step_width
                color = palette[i % len(palette)]

                if self.style == "chevron":
                    # Chevron shape
                    points = [
                        (x, center_y - 40),  # Top left
                        (x + step_width - 20, center_y - 40),  # Top right before point
                        (x + step_width, center_y),  # Right point
                        (x + step_width - 20, center_y + 40),  # Bottom right before point
                        (x, center_y + 40),  # Bottom left
                    ]
                    if i > 0:
                        # Add left notch
                        points = [
                            (x, center_y - 40),
                            (x + step_width - 20, center_y - 40),
                            (x + step_width, center_y),
                            (x + step_width - 20, center_y + 40),
                            (x, center_y + 40),
                            (x + 20, center_y),  # Left notch
                        ]

                    d.append(dw.Lines(
                        *[coord for point in points for coord in point],
                        fill=color,
                        close=True
                    ))

                elif self.style == "boxes":
                    # Simple rounded rectangle
                    d.append(dw.Rectangle(
                        x + 5, center_y - 35,
                        step_width - 20, 70,
                        rx=8, ry=8,
                        fill=color
                    ))

                    # Arrow connector
                    if i < n_steps - 1:
                        arrow_x = x + step_width - 10
                        d.append(dw.Lines(
                            arrow_x, center_y - 8,
                            arrow_x + 15, center_y,
                            arrow_x, center_y + 8,
                            fill=text_secondary,
                            close=True
                        ))

                else:  # circles
                    cx = x + step_width / 2
                    d.append(dw.Circle(cx, center_y, 35, fill=color))

                    # Connector line
                    if i < n_steps - 1:
                        d.append(dw.Line(
                            cx + 40, center_y,
                            cx + step_width - 40, center_y,
                            stroke=text_secondary,
                            stroke_width=2
                        ))

                # Step text
                text_x = x + step_width / 2
                d.append(dw.Text(
                    step["title"],
                    x=text_x,
                    y=center_y + 4,
                    font_size=12 if self.style == "chevron" else 11,
                    font_family="Helvetica, Arial, sans-serif",
                    font_weight="bold",
                    fill="white",
                    text_anchor="middle"
                ))

                # Description below
                if step.get("description"):
                    d.append(dw.Text(
                        step["description"],
                        x=text_x,
                        y=center_y + 70,
                        font_size=10,
                        font_family="Helvetica, Arial, sans-serif",
                        fill=text_secondary,
                        text_anchor="middle"
                    ))

        else:
            # Vertical flow
            margin_y = 100
            margin_x = width * 0.5
            step_height = (height - 2 * margin_y) / n_steps

            for i, step in enumerate(self.steps):
                y = margin_y + i * step_height + step_height / 2
                color = palette[i % len(palette)]

                # Box
                d.append(dw.Rectangle(
                    margin_x - 100, y - 25,
                    200, 50,
                    rx=8, ry=8,
                    fill=color
                ))

                # Step text
                d.append(dw.Text(
                    step["title"],
                    x=margin_x,
                    y=y + 5,
                    font_size=14,
                    font_family="Helvetica, Arial, sans-serif",
                    font_weight="bold",
                    fill="white",
                    text_anchor="middle"
                ))

                # Arrow connector
                if i < n_steps - 1:
                    arrow_y = y + 30
                    d.append(dw.Lines(
                        margin_x - 8, arrow_y + 10,
                        margin_x, arrow_y + 25,
                        margin_x + 8, arrow_y + 10,
                        fill=text_secondary,
                        close=True
                    ))
                    d.append(dw.Line(
                        margin_x, arrow_y,
                        margin_x, arrow_y + 15,
                        stroke=text_secondary,
                        stroke_width=2
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
        """Prefer Satori for process flows."""
        return RenderBackend.SATORI


def create_process_flow(
    steps: List[Union[str, Dict[str, str]]],
    title: Optional[str] = None,
    orientation: str = "horizontal",
    style: str = "chevron",
    output: str = "process_flow.png",
    backend: str = "satori",
    **kwargs
) -> str:
    """
    Quick function to create and render a ProcessFlow.

    Args:
        steps: List of step strings or dictionaries
        title: Flow title
        orientation: "horizontal" or "vertical"
        style: "chevron", "boxes", or "circles"
        output: Output file path
        backend: "satori" or "drawsvg"
        **kwargs: Additional options

    Returns:
        Path to rendered file
    """
    flow = ProcessFlow(
        steps=steps,
        title=title,
        orientation=orientation,
        style=style,
    )
    return flow.render(output, backend=backend, **kwargs)
