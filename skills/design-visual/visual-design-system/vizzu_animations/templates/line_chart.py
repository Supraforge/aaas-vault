"""
Animated line chart for outcome trends over time.

Shows progression of outcomes with smooth transitions.
"""

from __future__ import annotations

from pathlib import Path
from typing import List, Tuple, Optional, Dict

import pandas as pd

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from data_animator import VizzuAnimator


def create_animated_trend_line(
    series_data: Dict[str, List[Tuple[float, float]]],
    title: str = "Outcome Trends",
    x_label: str = "Time",
    y_label: str = "Value",
    output: Optional[str] = None,
    duration: int = 4000,
) -> Path:
    """
    Create animated line chart showing trends over time.

    Args:
        series_data: Dict mapping series names to list of (x, y) tuples
        title: Chart title
        x_label: X-axis label
        y_label: Y-axis label
        output: Output HTML file path
        duration: Animation duration in milliseconds

    Returns:
        Path to output HTML file

    Examples:
        >>> data = {
        ...     "2010-2015": [(2010, 25), (2012, 22), (2015, 18)],
        ...     "2015-2020": [(2015, 18), (2017, 15), (2020, 12)],
        ... }
        >>> create_animated_trend_line(
        ...     data,
        ...     title="Heart Failure Mortality Trends",
        ...     x_label="Year",
        ...     y_label="Mortality Rate (%)",
        ... )
    """
    # Prepare data
    data = []

    for series_name, points in series_data.items():
        for x, y in points:
            data.append({
                "X": x,
                "Y": y,
                "Series": series_name,
            })

    df = pd.DataFrame(data)

    # Create animator
    animator = VizzuAnimator()

    if output is None:
        output = animator.outputs_dir / "animated_trend_line.html"

    # Use line chart
    return animator.create_animated_line(
        df,
        x_col="X",
        y_col="Y",
        series_col="Series",
        title=title,
        output=output,
        duration=duration,
    )
