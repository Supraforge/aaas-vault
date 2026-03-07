"""
Visual Design System - Component Library

A unified, shadcn-inspired component library for medical and scientific graphics.
Each component auto-selects the best renderer (Satori, Plotly, or drawsvg) and
applies publication-grade styling from the design tokens.

Usage:
    from components import StatCard, ForestPlot, Timeline, ProcessFlow, DataTable

    # Create a stat card
    card = StatCard(value="26%", label="Mortality Reduction")
    card.render("output.png")

    # Create a forest plot
    plot = ForestPlot(studies=[...])
    plot.render("forest.png", backend="plotly")  # or "drawsvg"
"""

from .base import Component, RenderBackend
from .stat_card import StatCard
from .comparison import ComparisonChart
from .forest_plot import ForestPlot
from .timeline import Timeline
from .process_flow import ProcessFlow
from .data_table import DataTable

__all__ = [
    "Component",
    "RenderBackend",
    "StatCard",
    "ComparisonChart",
    "ForestPlot",
    "Timeline",
    "ProcessFlow",
    "DataTable",
]

__version__ = "2.1.0"
