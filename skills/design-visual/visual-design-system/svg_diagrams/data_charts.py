"""
Data Charts Module

Creates publication-quality data visualizations using drawsvg.
No Plotly dependency - pure Python SVG generation.

Charts:
    - bar_chart: Vertical or horizontal bar charts
    - grouped_bar_chart: Multi-series bar charts
    - line_chart: Time series or trend lines
    - forest_plot: Meta-analysis forest plots
    - dot_plot: Cleveland dot plots
    - waterfall_chart: Showing changes/contributions
"""

import drawsvg as draw
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
import math

# Import design tokens
try:
    from tokens.index import (
        get_color, get_color_palette, get_accessible_pair,
        get_tokens, get_spacing, hex_to_rgb
    )
except ImportError:
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from tokens.index import (
        get_color, get_color_palette, get_accessible_pair,
        get_tokens, get_spacing, hex_to_rgb
    )


# Constants
DEFAULT_WIDTH = 600
DEFAULT_HEIGHT = 400
FONT_FAMILY = "Helvetica, Arial, sans-serif"


def _get_chart_colors() -> Dict[str, str]:
    """Get standard colors for charts."""
    return {
        "axis": get_color("text.secondary"),
        "grid": get_color("backgrounds.medium_gray"),
        "label": get_color("text.primary"),
        "title": get_color("text.primary"),
        "background": get_color("backgrounds.white"),
    }


def _calculate_nice_range(min_val: float, max_val: float, target_ticks: int = 5) -> Tuple[float, float, float]:
    """
    Calculate nice axis range and tick interval.

    Returns:
        (nice_min, nice_max, tick_interval)
    """
    range_val = max_val - min_val
    if range_val == 0:
        range_val = 1

    # Calculate rough tick interval
    rough_interval = range_val / target_ticks

    # Find nice interval (1, 2, 5, 10, 20, 50, etc.)
    magnitude = 10 ** math.floor(math.log10(rough_interval))
    residual = rough_interval / magnitude

    if residual <= 1.5:
        nice_interval = magnitude
    elif residual <= 3:
        nice_interval = 2 * magnitude
    elif residual <= 7:
        nice_interval = 5 * magnitude
    else:
        nice_interval = 10 * magnitude

    # Calculate nice min/max
    nice_min = math.floor(min_val / nice_interval) * nice_interval
    nice_max = math.ceil(max_val / nice_interval) * nice_interval

    return nice_min, nice_max, nice_interval


def bar_chart(
    data: List[float],
    labels: List[str],
    width: int = DEFAULT_WIDTH,
    height: int = DEFAULT_HEIGHT,
    title: Optional[str] = None,
    y_label: Optional[str] = None,
    colors: Optional[List[str]] = None,
    horizontal: bool = False,
    show_values: bool = True,
    value_format: str = "{:.1f}",
    error_bars: Optional[List[Tuple[float, float]]] = None
) -> draw.Drawing:
    """
    Create a bar chart.

    Args:
        data: List of values
        labels: List of bar labels
        width: Canvas width
        height: Canvas height
        title: Chart title
        y_label: Y-axis label
        colors: Optional list of bar colors (uses design tokens by default)
        horizontal: If True, create horizontal bar chart
        show_values: Show value labels on bars
        value_format: Format string for values
        error_bars: Optional list of (lower_error, upper_error) tuples

    Returns:
        drawsvg.Drawing object
    """
    d = draw.Drawing(width, height)
    chart_colors = _get_chart_colors()

    # Background
    d.append(draw.Rectangle(0, 0, width, height, fill=chart_colors["background"]))

    # Margins
    margin_left = 70
    margin_right = 30
    margin_top = 50 if title else 30
    margin_bottom = 60

    plot_width = width - margin_left - margin_right
    plot_height = height - margin_top - margin_bottom

    # Get bar colors
    if colors is None:
        palette = get_color_palette("categorical")
        colors = [palette[i % len(palette)] for i in range(len(data))]

    # Title
    if title:
        d.append(draw.Text(
            title, 14,
            width / 2, 25,
            center=True,
            font_family=FONT_FAMILY,
            font_weight="bold",
            fill=chart_colors["title"]
        ))

    # Calculate axis range
    min_val = min(0, min(data))
    max_val = max(data)
    if error_bars:
        max_val = max(d + e[1] for d, e in zip(data, error_bars))

    nice_min, nice_max, tick_interval = _calculate_nice_range(min_val, max_val)

    # Draw axes
    axis_x = margin_left
    axis_y = height - margin_bottom

    # X-axis (or Y for horizontal)
    d.append(draw.Line(
        margin_left, axis_y,
        width - margin_right, axis_y,
        stroke=chart_colors["axis"], stroke_width=1
    ))

    # Y-axis (or X for horizontal)
    d.append(draw.Line(
        margin_left, margin_top,
        margin_left, axis_y,
        stroke=chart_colors["axis"], stroke_width=1
    ))

    # Y-axis label
    if y_label:
        d.append(draw.Text(
            y_label, 10,
            15, height / 2,
            center=True,
            font_family=FONT_FAMILY,
            fill=chart_colors["label"],
            transform=f"rotate(-90, 15, {height/2})"
        ))

    # Grid lines and Y-axis ticks
    y_ticks = []
    current = nice_min
    while current <= nice_max + tick_interval * 0.01:
        y_ticks.append(current)
        current += tick_interval

    for tick in y_ticks:
        y_pos = axis_y - ((tick - nice_min) / (nice_max - nice_min)) * plot_height

        # Grid line
        d.append(draw.Line(
            margin_left, y_pos,
            width - margin_right, y_pos,
            stroke=chart_colors["grid"], stroke_width=0.5
        ))

        # Tick label
        label_text = f"{tick:.0f}" if tick == int(tick) else f"{tick:.1f}"
        d.append(draw.Text(
            label_text, 9,
            margin_left - 10, y_pos + 3,
            text_anchor="end",
            font_family=FONT_FAMILY,
            fill=chart_colors["label"]
        ))

    # Draw bars
    n_bars = len(data)
    bar_spacing = 0.2  # 20% spacing between bars
    total_bar_width = plot_width / n_bars
    bar_width = total_bar_width * (1 - bar_spacing)

    for i, (value, label, color) in enumerate(zip(data, labels, colors)):
        bar_x = margin_left + i * total_bar_width + (total_bar_width - bar_width) / 2

        # Calculate bar height
        bar_height = ((value - nice_min) / (nice_max - nice_min)) * plot_height
        bar_y = axis_y - bar_height

        # Draw bar
        d.append(draw.Rectangle(
            bar_x, bar_y,
            bar_width, bar_height,
            fill=color,
            stroke="none"
        ))

        # Error bars
        if error_bars and i < len(error_bars):
            err_lower, err_upper = error_bars[i]
            center_x = bar_x + bar_width / 2
            err_y_top = axis_y - ((value + err_upper - nice_min) / (nice_max - nice_min)) * plot_height
            err_y_bottom = axis_y - ((value - err_lower - nice_min) / (nice_max - nice_min)) * plot_height

            # Vertical line
            d.append(draw.Line(
                center_x, err_y_top,
                center_x, err_y_bottom,
                stroke=chart_colors["axis"], stroke_width=1.5
            ))
            # Top cap
            d.append(draw.Line(
                center_x - 5, err_y_top,
                center_x + 5, err_y_top,
                stroke=chart_colors["axis"], stroke_width=1.5
            ))
            # Bottom cap
            d.append(draw.Line(
                center_x - 5, err_y_bottom,
                center_x + 5, err_y_bottom,
                stroke=chart_colors["axis"], stroke_width=1.5
            ))

        # Value label
        if show_values:
            d.append(draw.Text(
                value_format.format(value), 9,
                bar_x + bar_width / 2, bar_y - 5,
                center=True,
                font_family=FONT_FAMILY,
                font_weight="bold",
                fill=chart_colors["label"]
            ))

        # X-axis label
        d.append(draw.Text(
            label, 9,
            bar_x + bar_width / 2, axis_y + 15,
            center=True,
            font_family=FONT_FAMILY,
            fill=chart_colors["label"]
        ))

    return d


def grouped_bar_chart(
    data: List[List[float]],
    labels: List[str],
    series_names: List[str],
    width: int = DEFAULT_WIDTH,
    height: int = DEFAULT_HEIGHT,
    title: Optional[str] = None,
    y_label: Optional[str] = None,
    colors: Optional[List[str]] = None,
    show_values: bool = False,
    show_legend: bool = True
) -> draw.Drawing:
    """
    Create a grouped bar chart for comparing multiple series.

    Args:
        data: List of lists, each inner list is a series
        labels: X-axis labels (groups)
        series_names: Names for each series (for legend)
        width: Canvas width
        height: Canvas height
        title: Chart title
        y_label: Y-axis label
        colors: Optional colors for each series
        show_values: Show value labels
        show_legend: Show legend

    Returns:
        drawsvg.Drawing object
    """
    d = draw.Drawing(width, height)
    chart_colors = _get_chart_colors()

    # Background
    d.append(draw.Rectangle(0, 0, width, height, fill=chart_colors["background"]))

    # Margins
    margin_left = 70
    margin_right = 30 if not show_legend else 120
    margin_top = 50 if title else 30
    margin_bottom = 60

    plot_width = width - margin_left - margin_right
    plot_height = height - margin_top - margin_bottom

    # Get series colors
    if colors is None:
        colors = get_accessible_pair("treatment_control")
        if len(data) > 2:
            palette = get_color_palette("categorical")
            colors = palette[:len(data)]
        else:
            colors = list(colors)

    # Title
    if title:
        d.append(draw.Text(
            title, 14,
            (margin_left + width - margin_right) / 2, 25,
            center=True,
            font_family=FONT_FAMILY,
            font_weight="bold",
            fill=chart_colors["title"]
        ))

    # Calculate axis range
    all_values = [v for series in data for v in series]
    min_val = min(0, min(all_values))
    max_val = max(all_values)
    nice_min, nice_max, tick_interval = _calculate_nice_range(min_val, max_val)

    # Axes
    axis_y = height - margin_bottom

    d.append(draw.Line(margin_left, axis_y, width - margin_right, axis_y,
                      stroke=chart_colors["axis"], stroke_width=1))
    d.append(draw.Line(margin_left, margin_top, margin_left, axis_y,
                      stroke=chart_colors["axis"], stroke_width=1))

    # Y-axis label
    if y_label:
        d.append(draw.Text(
            y_label, 10,
            15, height / 2,
            center=True,
            font_family=FONT_FAMILY,
            fill=chart_colors["label"],
            transform=f"rotate(-90, 15, {height/2})"
        ))

    # Grid and ticks
    current = nice_min
    while current <= nice_max + tick_interval * 0.01:
        y_pos = axis_y - ((current - nice_min) / (nice_max - nice_min)) * plot_height

        d.append(draw.Line(margin_left, y_pos, width - margin_right, y_pos,
                          stroke=chart_colors["grid"], stroke_width=0.5))

        label_text = f"{current:.0f}" if current == int(current) else f"{current:.1f}"
        d.append(draw.Text(label_text, 9, margin_left - 10, y_pos + 3,
                          text_anchor="end", font_family=FONT_FAMILY, fill=chart_colors["label"]))
        current += tick_interval

    # Draw grouped bars
    n_groups = len(labels)
    n_series = len(data)
    group_width = plot_width / n_groups
    bar_spacing = 0.15
    bar_width = (group_width * (1 - bar_spacing * 2)) / n_series

    for g, label in enumerate(labels):
        group_x = margin_left + g * group_width + group_width * bar_spacing

        for s in range(n_series):
            value = data[s][g]
            bar_x = group_x + s * bar_width

            bar_height = ((value - nice_min) / (nice_max - nice_min)) * plot_height
            bar_y = axis_y - bar_height

            d.append(draw.Rectangle(
                bar_x, bar_y,
                bar_width * 0.9, bar_height,
                fill=colors[s % len(colors)],
                stroke="none"
            ))

            if show_values:
                d.append(draw.Text(
                    f"{value:.1f}", 8,
                    bar_x + bar_width * 0.45, bar_y - 3,
                    center=True,
                    font_family=FONT_FAMILY,
                    fill=chart_colors["label"]
                ))

        # Group label
        d.append(draw.Text(
            label, 9,
            group_x + (n_series * bar_width) / 2, axis_y + 15,
            center=True,
            font_family=FONT_FAMILY,
            fill=chart_colors["label"]
        ))

    # Legend
    if show_legend:
        legend_x = width - margin_right + 10
        legend_y = margin_top + 20

        for i, (name, color) in enumerate(zip(series_names, colors)):
            y = legend_y + i * 20
            d.append(draw.Rectangle(legend_x, y - 6, 12, 12, fill=color))
            d.append(draw.Text(
                name, 9,
                legend_x + 18, y + 3,
                font_family=FONT_FAMILY,
                fill=chart_colors["label"]
            ))

    return d


def line_chart(
    data: List[List[Tuple[float, float]]],
    series_names: List[str],
    width: int = DEFAULT_WIDTH,
    height: int = DEFAULT_HEIGHT,
    title: Optional[str] = None,
    x_label: Optional[str] = None,
    y_label: Optional[str] = None,
    colors: Optional[List[str]] = None,
    show_points: bool = True,
    show_legend: bool = True,
    line_width: float = 2.0
) -> draw.Drawing:
    """
    Create a line chart.

    Args:
        data: List of series, each series is list of (x, y) tuples
        series_names: Names for each series
        width: Canvas width
        height: Canvas height
        title: Chart title
        x_label: X-axis label
        y_label: Y-axis label
        colors: Optional colors for each series
        show_points: Show data points as circles
        show_legend: Show legend
        line_width: Stroke width for lines

    Returns:
        drawsvg.Drawing object
    """
    d = draw.Drawing(width, height)
    chart_colors = _get_chart_colors()

    # Background
    d.append(draw.Rectangle(0, 0, width, height, fill=chart_colors["background"]))

    # Margins
    margin_left = 70
    margin_right = 30 if not show_legend else 120
    margin_top = 50 if title else 30
    margin_bottom = 60

    plot_width = width - margin_left - margin_right
    plot_height = height - margin_top - margin_bottom

    # Colors
    if colors is None:
        palette = get_color_palette("categorical")
        colors = palette[:len(data)]

    # Title
    if title:
        d.append(draw.Text(
            title, 14,
            (margin_left + width - margin_right) / 2, 25,
            center=True,
            font_family=FONT_FAMILY,
            font_weight="bold",
            fill=chart_colors["title"]
        ))

    # Calculate ranges
    all_x = [p[0] for series in data for p in series]
    all_y = [p[1] for series in data for p in series]

    x_min, x_max, x_tick = _calculate_nice_range(min(all_x), max(all_x))
    y_min, y_max, y_tick = _calculate_nice_range(min(all_y), max(all_y))

    # Axes
    axis_y = height - margin_bottom

    d.append(draw.Line(margin_left, axis_y, width - margin_right, axis_y,
                      stroke=chart_colors["axis"], stroke_width=1))
    d.append(draw.Line(margin_left, margin_top, margin_left, axis_y,
                      stroke=chart_colors["axis"], stroke_width=1))

    # Axis labels
    if x_label:
        d.append(draw.Text(
            x_label, 10,
            (margin_left + width - margin_right) / 2, height - 15,
            center=True,
            font_family=FONT_FAMILY,
            fill=chart_colors["label"]
        ))

    if y_label:
        d.append(draw.Text(
            y_label, 10,
            15, height / 2,
            center=True,
            font_family=FONT_FAMILY,
            fill=chart_colors["label"],
            transform=f"rotate(-90, 15, {height/2})"
        ))

    # Y-axis grid and ticks
    current = y_min
    while current <= y_max + y_tick * 0.01:
        y_pos = axis_y - ((current - y_min) / (y_max - y_min)) * plot_height

        d.append(draw.Line(margin_left, y_pos, width - margin_right, y_pos,
                          stroke=chart_colors["grid"], stroke_width=0.5))

        label = f"{current:.0f}" if current == int(current) else f"{current:.1f}"
        d.append(draw.Text(label, 9, margin_left - 10, y_pos + 3,
                          text_anchor="end", font_family=FONT_FAMILY, fill=chart_colors["label"]))
        current += y_tick

    # X-axis ticks
    current = x_min
    while current <= x_max + x_tick * 0.01:
        x_pos = margin_left + ((current - x_min) / (x_max - x_min)) * plot_width

        d.append(draw.Line(x_pos, axis_y, x_pos, axis_y + 5,
                          stroke=chart_colors["axis"], stroke_width=1))

        label = f"{current:.0f}" if current == int(current) else f"{current:.1f}"
        d.append(draw.Text(label, 9, x_pos, axis_y + 18,
                          center=True, font_family=FONT_FAMILY, fill=chart_colors["label"]))
        current += x_tick

    # Draw lines
    for s, (series, name, color) in enumerate(zip(data, series_names, colors)):
        if not series:
            continue

        # Line path
        path = draw.Path(stroke=color, stroke_width=line_width, fill="none")

        for i, (x, y) in enumerate(series):
            px = margin_left + ((x - x_min) / (x_max - x_min)) * plot_width
            py = axis_y - ((y - y_min) / (y_max - y_min)) * plot_height

            if i == 0:
                path.M(px, py)
            else:
                path.L(px, py)

        d.append(path)

        # Points
        if show_points:
            for x, y in series:
                px = margin_left + ((x - x_min) / (x_max - x_min)) * plot_width
                py = axis_y - ((y - y_min) / (y_max - y_min)) * plot_height

                d.append(draw.Circle(
                    px, py, 4,
                    fill=chart_colors["background"],
                    stroke=color,
                    stroke_width=2
                ))

    # Legend
    if show_legend:
        legend_x = width - margin_right + 10
        legend_y = margin_top + 20

        for i, (name, color) in enumerate(zip(series_names, colors)):
            y = legend_y + i * 20

            # Line sample
            d.append(draw.Line(legend_x, y, legend_x + 20, y, stroke=color, stroke_width=2))
            if show_points:
                d.append(draw.Circle(legend_x + 10, y, 3, fill=chart_colors["background"],
                                    stroke=color, stroke_width=1.5))

            d.append(draw.Text(
                name, 9,
                legend_x + 28, y + 3,
                font_family=FONT_FAMILY,
                fill=chart_colors["label"]
            ))

    return d


def forest_plot(
    studies: List[Dict],
    width: int = 700,
    height: int = None,
    title: Optional[str] = None,
    x_label: str = "Hazard Ratio (95% CI)",
    show_pooled: bool = True,
    null_value: float = 1.0,
    log_scale: bool = True
) -> draw.Drawing:
    """
    Create a forest plot for meta-analysis.

    Args:
        studies: List of dicts with keys:
                 - name: Study name
                 - estimate: Point estimate (HR, OR, RR)
                 - lower: Lower CI bound
                 - upper: Upper CI bound
                 - weight: Optional weight (1-100)
        width: Canvas width
        height: Auto-calculated if None
        title: Plot title
        x_label: X-axis label
        show_pooled: Show pooled estimate
        null_value: Line of no effect (1.0 for ratio measures)
        log_scale: Use log scale for x-axis

    Returns:
        drawsvg.Drawing object
    """
    chart_colors = _get_chart_colors()

    # Calculate height based on number of studies
    row_height = 25
    margin_top = 60 if title else 40
    margin_bottom = 50
    n_rows = len(studies) + (2 if show_pooled else 0)

    if height is None:
        height = margin_top + n_rows * row_height + margin_bottom

    d = draw.Drawing(width, height)

    # Background
    d.append(draw.Rectangle(0, 0, width, height, fill=chart_colors["background"]))

    # Margins
    margin_left = 180  # Space for study names
    margin_right = 120  # Space for estimates text
    plot_width = width - margin_left - margin_right

    # Title
    if title:
        d.append(draw.Text(
            title, 14,
            width / 2, 25,
            center=True,
            font_family=FONT_FAMILY,
            font_weight="bold",
            fill=chart_colors["title"]
        ))

    # Calculate x-axis range
    all_values = []
    for study in studies:
        all_values.extend([study["lower"], study["upper"]])

    if log_scale:
        x_min = math.log10(min(all_values) * 0.9)
        x_max = math.log10(max(all_values) * 1.1)
    else:
        x_min = min(all_values) * 0.9
        x_max = max(all_values) * 1.1

    def x_to_px(val):
        if log_scale:
            val = math.log10(val)
        return margin_left + ((val - x_min) / (x_max - x_min)) * plot_width

    # Header
    header_y = margin_top
    d.append(draw.Text("Study", 10, 10, header_y,
                      font_family=FONT_FAMILY, font_weight="bold", fill=chart_colors["label"]))
    d.append(draw.Text("Estimate (95% CI)", 10, width - margin_right + 10, header_y,
                      font_family=FONT_FAMILY, font_weight="bold", fill=chart_colors["label"]))

    d.append(draw.Line(10, header_y + 8, width - 10, header_y + 8,
                      stroke=chart_colors["axis"], stroke_width=1))

    # Null effect line
    null_x = x_to_px(null_value)
    d.append(draw.Line(
        null_x, margin_top + 15,
        null_x, height - margin_bottom,
        stroke=chart_colors["axis"],
        stroke_width=1,
        stroke_dasharray="4,2"
    ))

    # Colors
    try:
        treatment_color, _ = get_accessible_pair("treatment_control")
    except:
        treatment_color = "#2d6a9f"

    # Draw studies
    for i, study in enumerate(studies):
        y = margin_top + 20 + (i + 1) * row_height

        # Study name
        d.append(draw.Text(
            study["name"], 9,
            10, y + 4,
            font_family=FONT_FAMILY,
            fill=chart_colors["label"]
        ))

        # CI line
        x1 = x_to_px(study["lower"])
        x2 = x_to_px(study["upper"])
        d.append(draw.Line(x1, y, x2, y, stroke=treatment_color, stroke_width=1.5))

        # Point estimate (square, size by weight)
        x_point = x_to_px(study["estimate"])
        weight = study.get("weight", 50)
        box_size = 4 + (weight / 100) * 8

        d.append(draw.Rectangle(
            x_point - box_size/2, y - box_size/2,
            box_size, box_size,
            fill=treatment_color
        ))

        # Estimate text
        ci_text = f"{study['estimate']:.2f} ({study['lower']:.2f}-{study['upper']:.2f})"
        d.append(draw.Text(
            ci_text, 9,
            width - margin_right + 10, y + 4,
            font_family=FONT_FAMILY,
            fill=chart_colors["label"]
        ))

    # Pooled estimate (diamond)
    if show_pooled and len(studies) > 1:
        # Simple pooled calculation (weighted average)
        weights = [s.get("weight", 1) for s in studies]
        total_weight = sum(weights)
        pooled_est = sum(s["estimate"] * w for s, w in zip(studies, weights)) / total_weight
        pooled_lower = sum(s["lower"] * w for s, w in zip(studies, weights)) / total_weight
        pooled_upper = sum(s["upper"] * w for s, w in zip(studies, weights)) / total_weight

        y = margin_top + 20 + (len(studies) + 1.5) * row_height

        d.append(draw.Line(10, y - 12, width - 10, y - 12,
                          stroke=chart_colors["axis"], stroke_width=1))

        d.append(draw.Text("Pooled", 9, 10, y + 4,
                          font_family=FONT_FAMILY, font_weight="bold", fill=chart_colors["label"]))

        # Diamond
        x_center = x_to_px(pooled_est)
        x_left = x_to_px(pooled_lower)
        x_right = x_to_px(pooled_upper)

        diamond = draw.Path(fill=treatment_color, stroke="none")
        diamond.M(x_left, y)
        diamond.L(x_center, y - 8)
        diamond.L(x_right, y)
        diamond.L(x_center, y + 8)
        diamond.Z()
        d.append(diamond)

        ci_text = f"{pooled_est:.2f} ({pooled_lower:.2f}-{pooled_upper:.2f})"
        d.append(draw.Text(ci_text, 9, width - margin_right + 10, y + 4,
                          font_family=FONT_FAMILY, font_weight="bold", fill=chart_colors["label"]))

    # X-axis
    axis_y = height - margin_bottom + 10
    d.append(draw.Line(margin_left, axis_y, width - margin_right, axis_y,
                      stroke=chart_colors["axis"], stroke_width=1))

    # X-axis label
    d.append(draw.Text(x_label, 10, (margin_left + width - margin_right) / 2, height - 15,
                      center=True, font_family=FONT_FAMILY, fill=chart_colors["label"]))

    # X-axis ticks
    if log_scale:
        tick_values = [0.5, 1.0, 2.0]
        for t in [0.25, 0.75, 1.5, 3.0, 4.0]:
            if x_min <= math.log10(t) <= x_max:
                tick_values.append(t)
        tick_values = sorted(set(tick_values))
    else:
        _, _, tick_int = _calculate_nice_range(10**x_min, 10**x_max, 5)
        tick_values = []
        current = 0
        while current <= 10**x_max:
            if current >= 10**x_min:
                tick_values.append(current)
            current += tick_int

    for val in tick_values:
        x = x_to_px(val)
        if margin_left <= x <= width - margin_right:
            d.append(draw.Line(x, axis_y - 3, x, axis_y + 3,
                              stroke=chart_colors["axis"], stroke_width=1))
            d.append(draw.Text(f"{val:.1f}".rstrip('0').rstrip('.'), 8, x, axis_y + 15,
                              center=True, font_family=FONT_FAMILY, fill=chart_colors["label"]))

    return d


if __name__ == "__main__":
    # Demo: Generate sample charts
    output_dir = Path(__file__).parent.parent / "outputs"
    output_dir.mkdir(exist_ok=True)

    print("Generating data charts...")

    # Bar chart
    bar = bar_chart(
        data=[45.2, 32.1, 28.5, 21.3],
        labels=["Treatment A", "Treatment B", "Control", "Placebo"],
        title="Primary Endpoint by Treatment Arm",
        y_label="Event Rate (%)",
        show_values=True
    )
    bar.save_png(str(output_dir / "bar_chart.png"))
    print("  -> bar_chart.png")

    # Grouped bar chart
    grouped = grouped_bar_chart(
        data=[[45, 32, 28], [38, 29, 25]],
        labels=["6 Months", "12 Months", "24 Months"],
        series_names=["Treatment", "Control"],
        title="Event Rates Over Time",
        y_label="Event Rate (%)"
    )
    grouped.save_png(str(output_dir / "grouped_bar_chart.png"))
    print("  -> grouped_bar_chart.png")

    # Line chart
    line = line_chart(
        data=[
            [(0, 100), (6, 85), (12, 72), (18, 65), (24, 58)],
            [(0, 100), (6, 90), (12, 82), (18, 76), (24, 71)]
        ],
        series_names=["Treatment", "Control"],
        title="Kaplan-Meier Survival Curve",
        x_label="Months",
        y_label="Survival (%)"
    )
    line.save_png(str(output_dir / "line_chart.png"))
    print("  -> line_chart.png")

    # Forest plot
    studies = [
        {"name": "DAPA-HF", "estimate": 0.74, "lower": 0.65, "upper": 0.85, "weight": 60},
        {"name": "EMPEROR-Reduced", "estimate": 0.75, "lower": 0.65, "upper": 0.86, "weight": 50},
        {"name": "SOLOIST-WHF", "estimate": 0.67, "lower": 0.52, "upper": 0.85, "weight": 30},
        {"name": "DELIVER", "estimate": 0.82, "lower": 0.73, "upper": 0.92, "weight": 70},
    ]
    forest = forest_plot(
        studies=studies,
        title="SGLT2 Inhibitors in Heart Failure",
        x_label="Hazard Ratio (95% CI)"
    )
    forest.save_png(str(output_dir / "forest_plot.png"))
    print("  -> forest_plot.png")

    print("\nDone! Check outputs/ directory.")
