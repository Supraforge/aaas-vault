"""
Animated Kaplan-Meier survival curves.

Shows survival divergence over time between treatment groups.
"""

from __future__ import annotations

from pathlib import Path
from typing import List, Tuple, Optional

import pandas as pd

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from data_animator import VizzuAnimator


def create_animated_kaplan_meier(
    treatment_data: List[Tuple[float, float]],
    control_data: List[Tuple[float, float]],
    treatment_name: str = "Treatment",
    control_name: str = "Control",
    title: str = "Event-Free Survival",
    x_label: str = "Months",
    y_label: str = "Survival (%)",
    hr_text: Optional[str] = None,
    output: Optional[str] = None,
    duration: int = 5000,
) -> Path:
    """
    Create animated Kaplan-Meier survival curves.

    Args:
        treatment_data: List of (time, survival) tuples for treatment arm
        control_data: List of (time, survival) tuples for control arm
        treatment_name: Name of treatment group
        control_name: Name of control group
        title: Chart title
        x_label: X-axis label
        y_label: Y-axis label
        hr_text: Hazard ratio text (e.g., "HR 0.74 (95% CI 0.65-0.85)")
        output: Output HTML file path
        duration: Animation duration in milliseconds

    Returns:
        Path to output HTML file

    Examples:
        >>> treatment = [(0, 100), (6, 94), (12, 88), (18, 83), (24, 78)]
        >>> control = [(0, 100), (6, 91), (12, 83), (18, 76), (24, 69)]
        >>> create_animated_kaplan_meier(
        ...     treatment, control,
        ...     hr_text="HR 0.76 (95% CI 0.64-0.90)"
        ... )
    """
    # Prepare data
    data = []

    for time, survival in treatment_data:
        data.append({
            "Time": time,
            "Survival": survival,
            "Group": treatment_name,
        })

    for time, survival in control_data:
        data.append({
            "Time": time,
            "Survival": survival,
            "Group": control_name,
        })

    df = pd.DataFrame(data)

    # Create animator
    animator = VizzuAnimator()

    if output is None:
        output = animator.outputs_dir / "animated_kaplan_meier.html"

    # Add HR text to title if provided
    full_title = title
    if hr_text:
        full_title = f"{title}\n{hr_text}"

    # Use line chart
    return animator.create_animated_line(
        df,
        x_col="Time",
        y_col="Survival",
        series_col="Group",
        title=full_title,
        output=output,
        duration=duration,
    )
