"""
Animated bar chart for before/after or treatment comparisons.

Shows outcome changes with animated transitions.
"""

from __future__ import annotations

from pathlib import Path
from typing import List, Dict, Optional

import pandas as pd

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from data_animator import VizzuAnimator


def create_animated_bar_comparison(
    categories: List[str],
    group1_values: List[float],
    group2_values: List[float],
    group1_name: str = "Treatment",
    group2_name: str = "Control",
    title: str = "Treatment Comparison",
    y_label: str = "Event Rate (%)",
    output: Optional[str] = None,
    duration: int = 3000,
) -> Path:
    """
    Create animated bar chart comparing two groups.

    Args:
        categories: List of outcome categories
        group1_values: Values for first group
        group2_values: Values for second group
        group1_name: Name of first group
        group2_name: Name of second group
        title: Chart title
        y_label: Y-axis label
        output: Output HTML file path
        duration: Animation duration in milliseconds

    Returns:
        Path to output HTML file

    Examples:
        >>> create_animated_bar_comparison(
        ...     categories=["Primary", "Secondary"],
        ...     group1_values=[12.3, 8.5],
        ...     group2_values=[18.7, 14.2],
        ...     group1_name="Dapagliflozin",
        ...     group2_name="Placebo",
        ... )
    """
    # Prepare data in long format
    data = []

    for i, category in enumerate(categories):
        data.append({
            "Outcome": category,
            "Value": group1_values[i],
            "Group": group1_name,
        })
        data.append({
            "Outcome": category,
            "Value": group2_values[i],
            "Group": group2_name,
        })

    df = pd.DataFrame(data)

    # Create animator
    animator = VizzuAnimator()

    if output is None:
        output = animator.outputs_dir / "animated_bar_comparison.html"

    # Use bar chart with color grouping
    return animator.create_animated_bar(
        df,
        x_col="Outcome",
        y_col="Value",
        color_col="Group",
        title=title,
        output=output,
        duration=duration,
    )
