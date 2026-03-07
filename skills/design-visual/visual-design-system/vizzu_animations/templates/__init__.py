"""
Medical animation templates for Vizzu.

Pre-configured templates for common cardiology visualizations.
"""

from .forest_plot import create_animated_forest_plot
from .kaplan_meier import create_animated_kaplan_meier
from .bar_chart import create_animated_bar_comparison
from .line_chart import create_animated_trend_line
from .trial_enrollment import create_animated_trial_enrollment

__all__ = [
    "create_animated_forest_plot",
    "create_animated_kaplan_meier",
    "create_animated_bar_comparison",
    "create_animated_trend_line",
    "create_animated_trial_enrollment",
]
