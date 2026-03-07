"""
Animated trial enrollment dashboard.

Shows patient recruitment progress accumulating over time.
"""

from __future__ import annotations

from pathlib import Path
from typing import List, Tuple, Optional

import pandas as pd

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from data_animator import VizzuAnimator


def create_animated_trial_enrollment(
    enrollment_data: List[Tuple[str, int]],
    target: Optional[int] = None,
    title: str = "Trial Enrollment Progress",
    x_label: str = "Month",
    y_label: str = "Patients Enrolled",
    output: Optional[str] = None,
    duration: int = 4000,
) -> Path:
    """
    Create animated trial enrollment dashboard.

    Args:
        enrollment_data: List of (time_period, cumulative_enrolled) tuples
        target: Optional target enrollment number
        title: Chart title
        x_label: X-axis label
        y_label: Y-axis label
        output: Output HTML file path
        duration: Animation duration in milliseconds

    Returns:
        Path to output HTML file

    Examples:
        >>> enrollment = [
        ...     ("Month 1", 50),
        ...     ("Month 2", 125),
        ...     ("Month 3", 230),
        ...     ("Month 4", 380),
        ...     ("Month 5", 500),
        ... ]
        >>> create_animated_trial_enrollment(
        ...     enrollment,
        ...     target=500,
        ...     title="PARADIGM-HF Enrollment",
        ... )
    """
    # Prepare data
    data = []

    for period, enrolled in enrollment_data:
        data.append({
            "Period": period,
            "Enrolled": enrolled,
            "Type": "Actual",
        })

    # Add target line if provided
    if target:
        for period, _ in enrollment_data:
            data.append({
                "Period": period,
                "Enrolled": target,
                "Type": "Target",
            })

    df = pd.DataFrame(data)

    # Create animator
    animator = VizzuAnimator()

    if output is None:
        output = animator.outputs_dir / "animated_trial_enrollment.html"

    # Add target to title if provided
    full_title = title
    if target:
        full_title = f"{title} (Target: {target:,})"

    # Use area chart for cumulative enrollment
    return animator.create_animated_area(
        df,
        x_col="Period",
        y_col="Enrolled",
        series_col="Type",
        title=full_title,
        output=output,
        duration=duration,
    )
