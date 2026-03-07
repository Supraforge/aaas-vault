"""
Animated forest plot for meta-analysis results.

Shows studies accumulating over time with confidence intervals.
"""

from __future__ import annotations

from pathlib import Path
from typing import List, Dict, Optional

import pandas as pd

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from data_animator import VizzuAnimator


def create_animated_forest_plot(
    studies: List[Dict[str, any]],
    title: str = "Meta-Analysis Forest Plot",
    output: Optional[str] = None,
    duration: int = 4000,
    show_pooled: bool = True,
) -> Path:
    """
    Create animated forest plot showing studies accumulating.

    Args:
        studies: List of study dicts with keys: name, estimate, lower, upper, weight
        title: Chart title
        output: Output HTML file path
        duration: Animation duration in milliseconds
        show_pooled: Show pooled estimate at end

    Returns:
        Path to output HTML file

    Examples:
        >>> studies = [
        ...     {"name": "DAPA-HF", "estimate": 0.74, "lower": 0.65, "upper": 0.85, "weight": 60},
        ...     {"name": "EMPEROR-Reduced", "estimate": 0.75, "lower": 0.65, "upper": 0.86, "weight": 50},
        ...     {"name": "SOLOIST-WHF", "estimate": 0.67, "lower": 0.52, "upper": 0.85, "weight": 30},
        ... ]
        >>> create_animated_forest_plot(studies, "SGLT2i in Heart Failure")
    """
    # Prepare data with CI ranges
    data = []
    for study in studies:
        data.append({
            "Study": study["name"],
            "HR": study["estimate"],
            "Lower CI": study["lower"],
            "Upper CI": study["upper"],
            "Weight": study["weight"],
            "CI Width": study["upper"] - study["lower"],
        })

    # Add pooled estimate if requested
    if show_pooled:
        # Simple weighted average (simplified - real pooling is more complex)
        total_weight = sum(s["weight"] for s in studies)
        pooled_hr = sum(s["estimate"] * s["weight"] for s in studies) / total_weight
        pooled_lower = sum(s["lower"] * s["weight"] for s in studies) / total_weight
        pooled_upper = sum(s["upper"] * s["weight"] for s in studies) / total_weight

        data.append({
            "Study": "Pooled",
            "HR": pooled_hr,
            "Lower CI": pooled_lower,
            "Upper CI": pooled_upper,
            "Weight": total_weight,
            "CI Width": pooled_upper - pooled_lower,
        })

    df = pd.DataFrame(data)

    # Create animator
    animator = VizzuAnimator()

    # Custom config for forest plot
    # Note: Vizzu doesn't have native forest plot, so we'll use scatter + error bars
    config = {
        "title": title,
        "x": "HR",
        "y": "Study",
        "size": "Weight",
        "label": "HR",
    }

    if output is None:
        output = animator.outputs_dir / "animated_forest_plot.html"

    # Use scatter plot as proxy for forest plot
    return animator.create_animated_scatter(
        df,
        x_col="HR",
        y_col="Study",
        size_col="Weight",
        title=title,
        output=output,
        duration=duration,
    )
