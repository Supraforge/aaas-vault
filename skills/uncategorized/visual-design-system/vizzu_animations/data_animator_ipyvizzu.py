"""
Python wrapper for Vizzu animated data visualizations using ipyvizzu.

This module provides a Python interface using the official ipyvizzu library.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd

try:
    from ipyvizzu import Chart, Data, Config, Style
    IPYVIZZU_AVAILABLE = True
except ImportError:
    IPYVIZZU_AVAILABLE = False


class VizzuAnimatorIPy:
    """
    Python interface for creating animated data visualizations with ipyvizzu.

    This is an alternative to the JavaScript-based animator that uses
    the official ipyvizzu Python library for better integration.

    Examples:
        >>> animator = VizzuAnimatorIPy()
        >>> df = pd.DataFrame({
        ...     'Study': ['DAPA-HF', 'EMPEROR-Reduced', 'DELIVER'],
        ...     'HR': [0.74, 0.75, 0.82]
        ... })
        >>> chart = animator.create_bar_chart(df, 'Study', 'HR')
    """

    def __init__(self, vizzu_dir: Optional[Path] = None):
        """
        Initialize Vizzu animator with ipyvizzu.

        Args:
            vizzu_dir: Path to vizzu_animations directory. Auto-detected if None.
        """
        if not IPYVIZZU_AVAILABLE:
            raise RuntimeError(
                "ipyvizzu not installed. Run: pip install ipyvizzu"
            )

        if vizzu_dir is None:
            self.vizzu_dir = Path(__file__).parent
        else:
            self.vizzu_dir = Path(vizzu_dir)

        self.outputs_dir = self.vizzu_dir / "outputs"
        self.outputs_dir.mkdir(exist_ok=True)

        # Design tokens colors
        self.colors = {
            "primary": "#2d6a9f",
            "secondary": "#48a9a6",
            "success": "#2e7d32",
            "danger": "#c62828",
            "navy": "#1e3a5f",
            "blue": "#4477AA",
            "orange": "#ee7733",
            "treatment": "#0077bb",
            "control": "#ee7733",
        }

    def _create_chart(self) -> Chart:
        """Create a new Vizzu chart with design system styling."""
        chart = Chart()

        # Apply design tokens
        style = Style({
            "plot": {
                "marker": {
                    "colorPalette": [
                        self.colors["blue"],
                        self.colors["orange"],
                        self.colors["success"],
                        self.colors["danger"],
                        self.colors["primary"],
                    ]
                }
            },
            "title": {
                "fontSize": "24px",
                "fontFamily": "Helvetica, Arial, sans-serif",
            },
        })

        chart.style = style
        return chart

    def create_bar_chart(
        self,
        df: pd.DataFrame,
        x_col: str,
        y_col: str,
        color_col: Optional[str] = None,
        title: str = "Bar Chart",
    ) -> Chart:
        """
        Create animated bar chart.

        Args:
            df: DataFrame with data
            x_col: Column name for x-axis (categories)
            y_col: Column name for y-axis (values)
            color_col: Optional column for color grouping
            title: Chart title

        Returns:
            Vizzu Chart object
        """
        chart = self._create_chart()

        # Convert DataFrame to Vizzu Data format
        data = Data()
        data.add_data_frame(df)

        chart.animate(data)

        # Configure chart
        config = Config({
            "x": x_col,
            "y": y_col,
            "title": title,
        })

        if color_col:
            config["color"] = color_col

        chart.animate(config)

        return chart

    def create_line_chart(
        self,
        df: pd.DataFrame,
        x_col: str,
        y_col: str,
        series_col: Optional[str] = None,
        title: str = "Line Chart",
    ) -> Chart:
        """
        Create animated line chart.

        Args:
            df: DataFrame with data
            x_col: Column name for x-axis (time)
            y_col: Column name for y-axis (value)
            series_col: Column for multiple series
            title: Chart title

        Returns:
            Vizzu Chart object
        """
        chart = self._create_chart()

        data = Data()
        data.add_data_frame(df)

        chart.animate(data)

        config = Config({
            "x": x_col,
            "y": y_col,
            "title": title,
            "coordSystem": "cartesian",
        })

        if series_col:
            config["color"] = series_col

        chart.animate(config, style={"plot": {"marker": {"guides": {"lineWidth": 2}}}})

        return chart

    def create_scatter_plot(
        self,
        df: pd.DataFrame,
        x_col: str,
        y_col: str,
        size_col: Optional[str] = None,
        color_col: Optional[str] = None,
        title: str = "Scatter Plot",
    ) -> Chart:
        """
        Create animated scatter plot.

        Args:
            df: DataFrame with data
            x_col: Column name for x-axis
            y_col: Column name for y-axis
            size_col: Optional column for point sizes
            color_col: Optional column for colors
            title: Chart title

        Returns:
            Vizzu Chart object
        """
        chart = self._create_chart()

        data = Data()
        data.add_data_frame(df)

        chart.animate(data)

        config = Config({
            "x": x_col,
            "y": y_col,
            "title": title,
        })

        if size_col:
            config["size"] = size_col
        if color_col:
            config["color"] = color_col

        chart.animate(config)

        return chart

    def create_area_chart(
        self,
        df: pd.DataFrame,
        x_col: str,
        y_col: str,
        series_col: Optional[str] = None,
        title: str = "Area Chart",
    ) -> Chart:
        """
        Create animated area chart.

        Args:
            df: DataFrame with data
            x_col: Column name for x-axis
            y_col: Column name for y-axis
            series_col: Column for stacked series
            title: Chart title

        Returns:
            Vizzu Chart object
        """
        chart = self._create_chart()

        data = Data()
        data.add_data_frame(df)

        chart.animate(data)

        config = Config({
            "x": x_col,
            "y": y_col,
            "title": title,
        })

        if series_col:
            config["color"] = series_col

        chart.animate(config, style={"plot": {"marker": {"rectangleSpacing": 0}}})

        return chart
