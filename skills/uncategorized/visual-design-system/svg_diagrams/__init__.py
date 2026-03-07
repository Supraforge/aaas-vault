"""
svg_diagrams - Pure Python SVG Generation for Medical Diagrams

Uses the drawsvg library with design tokens for Nature/JACC/NEJM-quality graphics.
All outputs are publication-ready with proper colors, fonts, and accessibility.

NOTE: This package is located in the `drawsvg/` directory but should be imported
using relative paths to avoid conflicts with the external drawsvg library.

Modules:
    - medical_diagrams: Heart anatomy, organ systems, pathways
    - data_charts: Bar charts, line charts, forest plots (no Plotly dependency)
    - process_flows: Flowcharts, treatment algorithms, timelines

Usage (from within the visual-design-system directory):
    # Option 1: Import modules directly
    from drawsvg.medical_diagrams import heart_simple, ecg_wave
    from drawsvg.data_charts import bar_chart, forest_plot
    from drawsvg.process_flows import treatment_algorithm

    # Create a heart diagram
    svg = heart_simple(highlight_chamber="lv")
    svg.save_png("heart.png")

Usage (from scripts):
    # Run the modules directly as scripts:
    python drawsvg/medical_diagrams.py
    python drawsvg/data_charts.py
    python drawsvg/process_flows.py
"""

import sys
from pathlib import Path

# Add parent directory to path for token imports
_current_dir = Path(__file__).parent
_parent_dir = _current_dir.parent
if str(_parent_dir) not in sys.path:
    sys.path.insert(0, str(_parent_dir))

# Version
__version__ = "1.0.0"

# Lazy imports to avoid circular import issues with the external drawsvg library
def _get_medical_diagrams():
    from . import medical_diagrams
    return medical_diagrams

def _get_data_charts():
    from . import data_charts
    return data_charts

def _get_process_flows():
    from . import process_flows
    return process_flows

# Convenient exports
__all__ = [
    "_get_medical_diagrams",
    "_get_data_charts",
    "_get_process_flows",
    "__version__",
]
