"""
DataTable Component

Publication-ready tables for clinical trial results, baseline characteristics,
and statistical summaries.

Usage:
    table = DataTable(
        title="Baseline Characteristics",
        headers=["Characteristic", "Treatment (n=500)", "Control (n=500)", "P-value"],
        rows=[
            ["Age, years", "65.2 ± 12.1", "64.8 ± 11.9", "0.62"],
            ["Male, n (%)", "320 (64%)", "318 (64%)", "0.91"],
            ["Diabetes, n (%)", "175 (35%)", "180 (36%)", "0.74"],
        ]
    )
    table.render("baseline.png")
"""

import os
from pathlib import Path
from typing import Optional, List, Any, Dict

from .base import Component, RenderBackend, RenderConfig, get_drawsvg


class DataTable(Component):
    """
    DataTable component for publication-ready tables.

    Best backends: DRAWSVG (publication), PLOTLY (interactive)
    """

    DEFAULT_BACKEND = RenderBackend.DRAWSVG
    SUPPORTED_BACKENDS = [RenderBackend.DRAWSVG, RenderBackend.PLOTLY]

    def __init__(
        self,
        headers: List[str],
        rows: List[List[str]],
        title: Optional[str] = None,
        footer: Optional[str] = None,
        highlight_rows: Optional[List[int]] = None,
        alignment: Optional[List[str]] = None,  # "left", "center", "right" per column
        source: Optional[str] = None,
        config: Optional[RenderConfig] = None,
    ):
        """
        Initialize DataTable.

        Args:
            headers: Column headers
            rows: Table rows (list of lists)
            title: Table title
            footer: Table footnote
            highlight_rows: Row indices to highlight
            alignment: Column alignments
            source: Data source citation
            config: Render configuration
        """
        super().__init__(title=title, source=source, config=config)
        self.headers = headers
        self.rows = rows
        self.footer = footer
        self.highlight_rows = highlight_rows or []
        self.alignment = alignment or ["left"] * len(headers)

    def _render_satori(self, output_path: str) -> str:
        """Satori not ideal for tables - use drawsvg."""
        return self._render_drawsvg(output_path)

    def _render_plotly(self, output_path: str) -> str:
        """Render using Plotly table."""
        try:
            import plotly.graph_objects as go
        except ImportError:
            raise ImportError("plotly not installed. Run: pip install plotly kaleido")

        # Get colors
        header_color = self.get_color("primary.navy")
        row_color = "#f8f9fa"  # Light gray
        alt_row_color = self.get_color("backgrounds.white")
        highlight_color = "#fff3cd"  # Yellow highlight
        text_primary = self.get_color("text.primary")

        # Prepare colors for each row
        row_colors = []
        for i in range(len(self.rows)):
            if i in self.highlight_rows:
                row_colors.append(highlight_color)
            elif i % 2 == 0:
                row_colors.append(alt_row_color)
            else:
                row_colors.append(row_color)

        # Transpose rows for Plotly
        values = [[row[i] for row in self.rows] for i in range(len(self.headers))]

        fig = go.Figure(data=[go.Table(
            header=dict(
                values=[f"<b>{h}</b>" for h in self.headers],
                fill_color=header_color,
                font=dict(color="white", size=12, family="Helvetica, Arial, sans-serif"),
                align=self.alignment,
                line_color="white",
                height=35,
            ),
            cells=dict(
                values=values,
                fill_color=[row_colors],
                font=dict(color=text_primary, size=11, family="Helvetica, Arial, sans-serif"),
                align=self.alignment,
                line_color="white",
                height=30,
            )
        )])

        # Layout
        fig.update_layout(
            title=dict(
                text=self.title or "",
                font=dict(size=18, family="Helvetica, Arial, sans-serif"),
            ),
            font=dict(family="Helvetica, Arial, sans-serif"),
            paper_bgcolor="white",
            margin=dict(t=60, b=60, l=20, r=20),
        )

        # Add footer/source
        annotations = []
        if self.footer:
            annotations.append(dict(
                text=self.footer,
                xref="paper", yref="paper",
                x=0, y=-0.08,
                showarrow=False,
                font=dict(size=10, color="#6c757d"),
                align="left",
            ))
        if self.source:
            annotations.append(dict(
                text=f"Source: {self.source}",
                xref="paper", yref="paper",
                x=0.5, y=-0.12,
                showarrow=False,
                font=dict(size=10, color="#6c757d"),
            ))
        if annotations:
            fig.update_layout(annotations=annotations)

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
        header_color = self.get_color("primary.navy")
        row_color = "#f8f9fa"  # Light gray
        alt_row_color = self.get_color("backgrounds.white")
        highlight_color = "#fff3cd"
        text_primary = self.get_color("text.primary")
        text_secondary = self.get_color("text.secondary")
        border_color = "#dee2e6"  # Light border

        width, height = self.config.width, self.config.height
        d = dw.Drawing(width, height)
        d.append(dw.Rectangle(0, 0, width, height, fill="white"))

        # Calculate dimensions
        margin_x = 40
        margin_y = 60 if self.title else 30
        table_width = width - 2 * margin_x
        col_width = table_width / len(self.headers)
        row_height = 35
        header_height = 40

        # Title
        if self.title:
            d.append(dw.Text(
                self.title,
                x=width / 2,
                y=35,
                font_size=18,
                font_family="Helvetica, Arial, sans-serif",
                font_weight="bold",
                fill=text_primary,
                text_anchor="middle"
            ))

        # Header row
        header_y = margin_y
        d.append(dw.Rectangle(
            margin_x, header_y,
            table_width, header_height,
            fill=header_color
        ))

        for i, header in enumerate(self.headers):
            x = margin_x + i * col_width
            align = self.alignment[i] if i < len(self.alignment) else "left"

            if align == "center":
                text_x = x + col_width / 2
                anchor = "middle"
            elif align == "right":
                text_x = x + col_width - 10
                anchor = "end"
            else:
                text_x = x + 10
                anchor = "start"

            d.append(dw.Text(
                header,
                x=text_x,
                y=header_y + header_height / 2 + 5,
                font_size=12,
                font_family="Helvetica, Arial, sans-serif",
                font_weight="bold",
                fill="white",
                text_anchor=anchor
            ))

        # Data rows
        for row_idx, row in enumerate(self.rows):
            row_y = margin_y + header_height + row_idx * row_height

            # Row background
            if row_idx in self.highlight_rows:
                bg = highlight_color
            elif row_idx % 2 == 0:
                bg = alt_row_color
            else:
                bg = row_color

            d.append(dw.Rectangle(
                margin_x, row_y,
                table_width, row_height,
                fill=bg
            ))

            # Row border
            d.append(dw.Line(
                margin_x, row_y + row_height,
                margin_x + table_width, row_y + row_height,
                stroke=border_color,
                stroke_width=0.5
            ))

            # Cell values
            for col_idx, value in enumerate(row):
                x = margin_x + col_idx * col_width
                align = self.alignment[col_idx] if col_idx < len(self.alignment) else "left"

                if align == "center":
                    text_x = x + col_width / 2
                    anchor = "middle"
                elif align == "right":
                    text_x = x + col_width - 10
                    anchor = "end"
                else:
                    text_x = x + 10
                    anchor = "start"

                d.append(dw.Text(
                    str(value),
                    x=text_x,
                    y=row_y + row_height / 2 + 5,
                    font_size=11,
                    font_family="Helvetica, Arial, sans-serif",
                    fill=text_primary,
                    text_anchor=anchor
                ))

        # Footer
        footer_y = margin_y + header_height + len(self.rows) * row_height + 20
        if self.footer:
            d.append(dw.Text(
                self.footer,
                x=margin_x,
                y=footer_y,
                font_size=10,
                font_family="Helvetica, Arial, sans-serif",
                fill=text_secondary
            ))
            footer_y += 18

        if self.source:
            d.append(dw.Text(
                f"Source: {self.source}",
                x=margin_x,
                y=footer_y,
                font_size=10,
                font_family="Helvetica, Arial, sans-serif",
                fill=text_secondary
            ))

        # Save
        if output_path.endswith(".png"):
            d.save_png(output_path)
        else:
            d.save_svg(output_path)

        return output_path

    def _select_backend(self) -> RenderBackend:
        """Prefer drawsvg for publication tables."""
        return RenderBackend.DRAWSVG


def create_data_table(
    headers: List[str],
    rows: List[List[str]],
    title: Optional[str] = None,
    output: str = "table.png",
    backend: str = "drawsvg",
    **kwargs
) -> str:
    """
    Quick function to create and render a DataTable.

    Args:
        headers: Column headers
        rows: Table rows
        title: Table title
        output: Output file path
        backend: "drawsvg" or "plotly"
        **kwargs: Additional options

    Returns:
        Path to rendered file
    """
    table = DataTable(
        headers=headers,
        rows=rows,
        title=title,
    )
    return table.render(output, backend=backend, **kwargs)
