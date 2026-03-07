"""
Python wrapper for Vizzu animated data visualizations.

This module provides a Python interface to Vizzu-lib for creating
animated data visualizations for medical content.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd


class VizzuAnimator:
    """
    Python interface for creating animated data visualizations with Vizzu.

    Examples:
        >>> animator = VizzuAnimator()
        >>> df = pd.DataFrame({
        ...     'Study': ['DAPA-HF', 'EMPEROR-Reduced', 'DELIVER'],
        ...     'HR': [0.74, 0.75, 0.82]
        ... })
        >>> animator.create_animated_bar(df, output='bar.html')
    """

    def __init__(self, vizzu_dir: Optional[Path] = None):
        """
        Initialize Vizzu animator.

        Args:
            vizzu_dir: Path to vizzu_animations directory. Auto-detected if None.
        """
        if vizzu_dir is None:
            self.vizzu_dir = Path(__file__).parent
        else:
            self.vizzu_dir = Path(vizzu_dir)

        self.renderer_path = self.vizzu_dir / "renderer.js"
        self.templates_dir = self.vizzu_dir / "templates"
        self.outputs_dir = self.vizzu_dir / "outputs"

        # Ensure outputs directory exists
        self.outputs_dir.mkdir(exist_ok=True)

    def _prepare_data(self, df: pd.DataFrame) -> List[Dict[str, Any]]:
        """Convert DataFrame to Vizzu-compatible format."""
        return df.to_dict('records')

    def _render_animation(
        self,
        data: List[Dict[str, Any]],
        config: Dict[str, Any],
        output_path: Path,
        duration: int = 3000,
        easing: str = "cubic-bezier(0.65,0,0.35,1)",
    ) -> Path:
        """
        Render animation using Node.js renderer.

        Args:
            data: Data in Vizzu format
            config: Vizzu configuration
            output_path: Output file path
            duration: Animation duration in milliseconds
            easing: CSS easing function

        Returns:
            Path to rendered file
        """
        # Prepare payload
        payload = {
            "data": data,
            "config": config,
            "animation": {
                "duration": duration,
                "easing": easing,
            },
            "output": str(output_path.absolute()),
        }

        # Write payload to temp file
        payload_path = self.outputs_dir / "payload.json"
        with open(payload_path, 'w') as f:
            json.dump(payload, f, indent=2)

        # Run renderer
        cmd = [
            "node",
            str(self.renderer_path),
            str(payload_path),
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=str(self.vizzu_dir),
        )

        if result.returncode != 0:
            raise RuntimeError(f"Vizzu rendering failed: {result.stderr}")

        return output_path

    def create_animated_bar(
        self,
        df: pd.DataFrame,
        x_col: str,
        y_col: str,
        title: str = "Animated Bar Chart",
        output: Optional[str] = None,
        duration: int = 2000,
        color_col: Optional[str] = None,
    ) -> Path:
        """
        Create animated bar chart.

        Args:
            df: DataFrame with data
            x_col: Column name for x-axis (categories)
            y_col: Column name for y-axis (values)
            title: Chart title
            output: Output file path (HTML)
            duration: Animation duration in milliseconds
            color_col: Optional column for color grouping

        Returns:
            Path to output file
        """
        if output is None:
            output = self.outputs_dir / "animated_bar.html"
        else:
            output = Path(output)

        data = self._prepare_data(df)

        config = {
            "title": title,
            "x": x_col,
            "y": y_col,
            "color": color_col if color_col else None,
        }

        return self._render_animation(data, config, output, duration)

    def create_animated_line(
        self,
        df: pd.DataFrame,
        x_col: str,
        y_col: str,
        series_col: Optional[str] = None,
        title: str = "Animated Line Chart",
        output: Optional[str] = None,
        duration: int = 3000,
    ) -> Path:
        """
        Create animated line chart (e.g., Kaplan-Meier curves).

        Args:
            df: DataFrame with data
            x_col: Column name for x-axis (time)
            y_col: Column name for y-axis (value)
            series_col: Column for multiple series
            title: Chart title
            output: Output file path (HTML)
            duration: Animation duration in milliseconds

        Returns:
            Path to output file
        """
        if output is None:
            output = self.outputs_dir / "animated_line.html"
        else:
            output = Path(output)

        data = self._prepare_data(df)

        config = {
            "title": title,
            "x": x_col,
            "y": y_col,
            "color": series_col if series_col else None,
            "coordSystem": "cartesian",
        }

        return self._render_animation(data, config, output, duration)

    def create_animated_scatter(
        self,
        df: pd.DataFrame,
        x_col: str,
        y_col: str,
        size_col: Optional[str] = None,
        color_col: Optional[str] = None,
        title: str = "Animated Scatter Plot",
        output: Optional[str] = None,
        duration: int = 2500,
    ) -> Path:
        """
        Create animated scatter plot.

        Args:
            df: DataFrame with data
            x_col: Column name for x-axis
            y_col: Column name for y-axis
            size_col: Optional column for point sizes
            color_col: Optional column for colors
            title: Chart title
            output: Output file path (HTML)
            duration: Animation duration in milliseconds

        Returns:
            Path to output file
        """
        if output is None:
            output = self.outputs_dir / "animated_scatter.html"
        else:
            output = Path(output)

        data = self._prepare_data(df)

        config = {
            "title": title,
            "x": x_col,
            "y": y_col,
            "size": size_col if size_col else None,
            "color": color_col if color_col else None,
        }

        return self._render_animation(data, config, output, duration)

    def create_animated_area(
        self,
        df: pd.DataFrame,
        x_col: str,
        y_col: str,
        series_col: Optional[str] = None,
        title: str = "Animated Area Chart",
        output: Optional[str] = None,
        duration: int = 3000,
    ) -> Path:
        """
        Create animated area chart.

        Args:
            df: DataFrame with data
            x_col: Column name for x-axis
            y_col: Column name for y-axis
            series_col: Column for stacked series
            title: Chart title
            output: Output file path (HTML)
            duration: Animation duration in milliseconds

        Returns:
            Path to output file
        """
        if output is None:
            output = self.outputs_dir / "animated_area.html"
        else:
            output = Path(output)

        data = self._prepare_data(df)

        config = {
            "title": title,
            "x": x_col,
            "y": y_col,
            "color": series_col if series_col else None,
        }

        return self._render_animation(data, config, output, duration)
