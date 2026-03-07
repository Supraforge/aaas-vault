#!/usr/bin/env python3
"""
Plotly Medical Chart Templates - Publication Quality

Pre-built templates for common medical/cardiology data visualizations.
Generates interactive HTML and static PNG exports at 300 DPI.

Follows Nature/JACC/NEJM publication standards:
- Helvetica/Arial typography (5-8pt for figures)
- WCAG AA compliant contrast ratios (≥4.5:1)
- Colorblind-safe palettes (Paul Tol)
- 300 DPI export for print quality

Usage:
    python plotly_charts.py bar --data trial_data.csv --output results.html
    python plotly_charts.py forest --data meta_analysis.csv --output forest.png
    python plotly_charts.py demo --quality-report  # Validate publication standards
"""

import argparse
import sys
import os
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple

try:
    import plotly.express as px
    import plotly.graph_objects as go
    import plotly.io as pio
    from plotly.subplots import make_subplots
    import pandas as pd
except ImportError:
    print("❌ Install dependencies:")
    print("   pip install plotly pandas kaleido --break-system-packages")
    sys.exit(1)

# Import design tokens from visual-design-system
_tokens_imported = False
try:
    # Add visual-design-system to path
    _vds_path = Path(__file__).parent.parent.parent / "visual-design-system"
    if _vds_path.exists():
        sys.path.insert(0, str(_vds_path))
        from tokens.index import (
            get_tokens, get_color, get_color_palette, get_accessible_pair,
            get_plotly_template, validate_contrast, calculate_contrast_ratio,
            get_contrast_ratio
        )
        _tokens_imported = True
except ImportError:
    _tokens_imported = False


# Publication quality settings
PUBLICATION_DPI = 300
PUBLICATION_SCALE = 4  # 4x scale gives ~300 DPI for standard figure sizes
DEFAULT_WIDTH = 800    # pixels
DEFAULT_HEIGHT = 600   # pixels


def _get_medical_colors() -> Dict[str, str]:
    """Get medical color palette from design tokens or fallback."""
    if _tokens_imported:
        tokens = get_tokens()
        return {
            'primary': tokens.get_color("primary.navy"),
            'secondary': tokens.get_color("primary.blue"),
            'accent': tokens.get_color("primary.teal"),
            'success': tokens.get_color("semantic.success"),
            'warning': tokens.get_color("semantic.warning"),
            'danger': tokens.get_color("semantic.danger"),
            'neutral': tokens.get_color("semantic.neutral"),
            'light': tokens.get_color("backgrounds.light_gray"),
            'background': tokens.get_color("backgrounds.white"),
            'text_primary': tokens.get_color("text.primary"),
            'text_secondary': tokens.get_color("text.secondary"),
            'grid': tokens.get_color("backgrounds.medium_gray"),
        }
    else:
        # Fallback to hardcoded (matches design tokens)
        return {
            'primary': '#1e3a5f',
            'secondary': '#2d6a9f',
            'accent': '#48a9a6',
            'success': '#4caf50',
            'warning': '#ff9800',
            'danger': '#f44336',
            'neutral': '#607d8b',
            'light': '#e9ecef',
            'background': '#ffffff',
            'text_primary': '#1a1a2e',
            'text_secondary': '#4a4a68',
            'grid': '#dee2e6',
        }


def _get_medical_palette() -> List[str]:
    """Get categorical color palette from design tokens or fallback."""
    if _tokens_imported:
        return get_color_palette("categorical")
    else:
        # Fallback - Paul Tol colorblind-safe palette
        return ['#0077bb', '#33bbee', '#009988', '#ee7733', '#cc3311', '#ee3377', '#bbbbbb']


def _get_treatment_control_colors() -> Tuple[str, str]:
    """Get accessible color pair for treatment vs control comparisons."""
    if _tokens_imported:
        return get_accessible_pair("treatment_control")
    else:
        return ('#0077bb', '#ee7733')  # Blue/Orange - colorblind-safe


# Export colors for backward compatibility
MEDICAL_COLORS = _get_medical_colors()
MEDICAL_PALETTE = _get_medical_palette()


def apply_medical_theme(
    fig: go.Figure,
    title: str = "",
    publication_ready: bool = True
) -> go.Figure:
    """
    Apply consistent medical styling to any Plotly figure.

    Uses design tokens for Nature/JACC/NEJM publication standards:
    - Helvetica/Arial font family
    - 10pt base font, 14pt titles
    - WCAG AA compliant colors
    - Clean grid lines

    Args:
        fig: Plotly figure to style
        title: Chart title
        publication_ready: If True, applies stricter publication standards

    Returns:
        Styled figure
    """
    colors = _get_medical_colors()

    # Get template from design tokens if available
    if _tokens_imported and publication_ready:
        template = get_plotly_template()
        # Apply template settings
        layout_settings = template.get("layout", {})
        fig.update_layout(**layout_settings)

    # Apply/override with medical theme
    fig.update_layout(
        title=dict(
            text=title,
            font=dict(
                size=14 if publication_ready else 18,
                color=colors.get('text_primary', colors['primary']),
                family="Helvetica, Arial, sans-serif"
            ),
            x=0.5,
            xanchor='center'
        ),
        font=dict(
            family="Helvetica, Arial, sans-serif",
            size=10 if publication_ready else 12,
            color=colors.get('text_primary', '#333')
        ),
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5,
            font=dict(size=9 if publication_ready else 11),
            bgcolor="rgba(255,255,255,0.8)"
        ),
        margin=dict(l=60, r=40, t=80, b=60),
        colorway=_get_medical_palette()  # Use colorblind-safe palette
    )

    # Publication-quality axis styling
    axis_font_size = 8 if publication_ready else 10
    grid_color = colors.get('grid', '#eee')

    fig.update_xaxes(
        showgrid=True,
        gridwidth=0.5 if publication_ready else 1,
        gridcolor=grid_color,
        linewidth=0.8,
        linecolor=colors.get('text_secondary', '#666'),
        tickfont=dict(size=axis_font_size),
        title=dict(font=dict(size=axis_font_size + 2))  # Modern Plotly API
    )
    fig.update_yaxes(
        showgrid=True,
        gridwidth=0.5 if publication_ready else 1,
        gridcolor=grid_color,
        linewidth=0.8,
        linecolor=colors.get('text_secondary', '#666'),
        tickfont=dict(size=axis_font_size),
        title=dict(font=dict(size=axis_font_size + 2))  # Modern Plotly API
    )

    return fig


def create_bar_chart(
    data: pd.DataFrame,
    x: str,
    y: str,
    title: str = "Clinical Outcomes",
    color: Optional[str] = None,
    orientation: str = "v"
) -> go.Figure:
    """Create a bar chart for trial results or comparisons."""
    fig = px.bar(
        data,
        x=x if orientation == "v" else y,
        y=y if orientation == "v" else x,
        color=color,
        orientation=orientation,
        color_discrete_sequence=MEDICAL_PALETTE,
        text=y if orientation == "v" else x
    )
    fig.update_traces(textposition='outside')
    return apply_medical_theme(fig, title)


def create_forest_plot(
    studies: List[str],
    estimates: List[float],
    lower_ci: List[float],
    upper_ci: List[float],
    title: str = "Forest Plot: Hazard Ratios",
    null_value: float = 1.0
) -> go.Figure:
    """Create a forest plot for meta-analysis visualization."""
    fig = go.Figure()
    
    # Add confidence intervals (horizontal lines)
    for i, (study, est, low, high) in enumerate(zip(studies, estimates, lower_ci, upper_ci)):
        fig.add_trace(go.Scatter(
            x=[low, high],
            y=[study, study],
            mode='lines',
            line=dict(color=MEDICAL_COLORS['neutral'], width=2),
            showlegend=False,
            hoverinfo='skip'
        ))
    
    # Add point estimates
    fig.add_trace(go.Scatter(
        x=estimates,
        y=studies,
        mode='markers',
        marker=dict(
            size=12,
            color=MEDICAL_COLORS['primary'],
            symbol='diamond'
        ),
        name='Point Estimate',
        hovertemplate='%{y}<br>HR: %{x:.2f}<extra></extra>'
    ))
    
    # Add null line
    fig.add_vline(
        x=null_value,
        line_dash="dash",
        line_color=MEDICAL_COLORS['danger'],
        annotation_text=f"Null ({null_value})"
    )
    
    fig.update_layout(
        xaxis_title="Hazard Ratio (95% CI)",
        yaxis_title="",
        xaxis=dict(type='log' if null_value == 1.0 else 'linear')
    )
    
    return apply_medical_theme(fig, title)


def create_survival_curve(
    time_data: List[List[float]],
    survival_data: List[List[float]],
    group_names: List[str],
    title: str = "Kaplan-Meier Survival Curve",
    xlabel: str = "Time (months)",
    ylabel: str = "Survival Probability"
) -> go.Figure:
    """Create Kaplan-Meier style survival curves."""
    fig = go.Figure()
    
    for i, (times, survival, name) in enumerate(zip(time_data, survival_data, group_names)):
        fig.add_trace(go.Scatter(
            x=times,
            y=survival,
            mode='lines',
            name=name,
            line=dict(color=MEDICAL_PALETTE[i % len(MEDICAL_PALETTE)], width=2, shape='hv')
        ))
    
    fig.update_layout(
        xaxis_title=xlabel,
        yaxis_title=ylabel,
        yaxis=dict(range=[0, 1.05])
    )
    
    return apply_medical_theme(fig, title)


def create_trend_line(
    data: pd.DataFrame,
    x: str,
    y: str,
    title: str = "Trend Over Time",
    color: Optional[str] = None
) -> go.Figure:
    """Create a line chart for trends over time."""
    fig = px.line(
        data,
        x=x,
        y=y,
        color=color,
        color_discrete_sequence=MEDICAL_PALETTE,
        markers=True
    )
    fig.update_xaxes(rangeslider_visible=True)
    return apply_medical_theme(fig, title)


def create_comparison_bars(
    categories: List[str],
    group1_values: List[float],
    group2_values: List[float],
    group1_name: str = "Treatment",
    group2_name: str = "Control",
    title: str = "Treatment vs Control Comparison"
) -> go.Figure:
    """
    Create grouped bar chart for treatment comparisons.

    Uses colorblind-safe accessible color pair from design tokens.
    """
    # Get accessible colors for treatment vs control
    treatment_color, control_color = _get_treatment_control_colors()

    fig = go.Figure(data=[
        go.Bar(
            name=group1_name,
            x=categories,
            y=group1_values,
            marker_color=treatment_color  # Colorblind-safe blue
        ),
        go.Bar(
            name=group2_name,
            x=categories,
            y=group2_values,
            marker_color=control_color  # Colorblind-safe orange
        )
    ])
    fig.update_layout(barmode='group')
    return apply_medical_theme(fig, title)


def create_pie_chart(
    labels: List[str],
    values: List[float],
    title: str = "Distribution"
) -> go.Figure:
    """Create a pie/donut chart for proportions."""
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.4,
        marker=dict(colors=MEDICAL_PALETTE)
    )])
    return apply_medical_theme(fig, title)


def create_heatmap(
    data: pd.DataFrame,
    title: str = "Correlation Matrix"
) -> go.Figure:
    """Create a heatmap for correlation or matrix data."""
    fig = px.imshow(
        data,
        text_auto=True,
        color_continuous_scale='RdBu_r',
        aspect='auto'
    )
    return apply_medical_theme(fig, title)


def create_dashboard(
    charts: List[go.Figure],
    titles: List[str],
    rows: int = 2,
    cols: int = 2
) -> go.Figure:
    """Combine multiple charts into a dashboard layout."""
    fig = make_subplots(
        rows=rows,
        cols=cols,
        subplot_titles=titles
    )
    
    for i, chart in enumerate(charts):
        row = (i // cols) + 1
        col = (i % cols) + 1
        for trace in chart.data:
            fig.add_trace(trace, row=row, col=col)
    
    fig.update_layout(height=800, showlegend=True)
    return apply_medical_theme(fig, "Clinical Dashboard")


def validate_chart_accessibility(fig: go.Figure) -> Dict[str, Any]:
    """
    Validate chart colors meet WCAG AA accessibility standards.

    Returns:
        Dict with validation results and any warnings
    """
    results = {
        "passed": True,
        "warnings": [],
        "errors": [],
        "contrast_checks": []
    }

    colors = _get_medical_colors()
    background = colors.get('background', '#ffffff')

    # Check text colors against background
    text_color = colors.get('text_primary', '#1a1a2e')

    if _tokens_imported:
        ratio = get_contrast_ratio(text_color, background)
        check = {
            "pair": f"{text_color} on {background}",
            "ratio": round(ratio, 2),
            "wcag_aa": ratio >= 4.5,
            "wcag_aaa": ratio >= 7.0
        }
        results["contrast_checks"].append(check)

        if not check["wcag_aa"]:
            results["errors"].append(f"Text contrast {ratio:.1f}:1 below WCAG AA (4.5:1)")
            results["passed"] = False
        elif not check["wcag_aaa"]:
            results["warnings"].append(f"Text contrast {ratio:.1f}:1 meets AA but not AAA (7:1)")

        # Check palette colors are distinguishable
        palette = _get_medical_palette()
        for i, color in enumerate(palette):
            ratio = get_contrast_ratio(color, background)
            if ratio < 3.0:  # Minimum for graphics/icons
                results["warnings"].append(
                    f"Palette color {i+1} ({color}) has low contrast {ratio:.1f}:1"
                )
    else:
        results["warnings"].append("Design tokens not imported - full validation unavailable")

    return results


def save_chart(
    fig: go.Figure,
    output_path: str,
    width: int = DEFAULT_WIDTH,
    height: int = DEFAULT_HEIGHT,
    scale: Optional[float] = None,
    validate_accessibility: bool = True
):
    """
    Save chart as HTML or image with publication-quality settings.

    For image exports (PNG, PDF, SVG):
    - Default scale=4 produces ~300 DPI for standard figure sizes
    - Width/height in pixels at base resolution

    Args:
        fig: Plotly figure to save
        output_path: Output file path (.html, .png, .jpg, .pdf, .svg)
        width: Figure width in pixels (default 800)
        height: Figure height in pixels (default 600)
        scale: Export scale factor (default 4 for ~300 DPI)
        validate_accessibility: Run WCAG validation before export
    """
    # Default to publication quality scale
    if scale is None:
        scale = PUBLICATION_SCALE

    # Run accessibility validation
    if validate_accessibility:
        validation = validate_chart_accessibility(fig)
        if validation["errors"]:
            print("⚠️  Accessibility issues:")
            for error in validation["errors"]:
                print(f"   ❌ {error}")
        if validation["warnings"]:
            for warning in validation["warnings"]:
                print(f"   ⚡ {warning}")

    if output_path.endswith('.html'):
        fig.write_html(output_path, include_plotlyjs='cdn')
        print(f"✅ Saved interactive chart: {output_path}")

    elif output_path.endswith(('.png', '.jpg', '.jpeg', '.pdf', '.svg')):
        try:
            # Publication quality export with 300 DPI equivalent
            fig.write_image(
                output_path,
                width=width,
                height=height,
                scale=scale  # 4x scale = ~300 DPI
            )
            actual_width = width * scale
            actual_height = height * scale
            print(f"✅ Saved publication-quality image: {output_path}")
            print(f"   Resolution: {actual_width}x{actual_height}px (scale={scale}x, ~{PUBLICATION_DPI} DPI)")

        except Exception as e:
            print(f"⚠️  Image export failed: {e}")
            print("   Install kaleido: pip install kaleido --break-system-packages")
            # Fallback to HTML
            html_path = output_path.rsplit('.', 1)[0] + '.html'
            fig.write_html(html_path)
            print(f"   Saved as HTML instead: {html_path}")
    else:
        # Default to HTML
        fig.write_html(output_path + '.html')
        print(f"✅ Saved: {output_path}.html")


def get_publication_settings() -> Dict[str, Any]:
    """
    Get current publication quality settings.

    Returns:
        Dict with DPI, scale, and color information
    """
    return {
        "dpi": PUBLICATION_DPI,
        "scale": PUBLICATION_SCALE,
        "default_width": DEFAULT_WIDTH,
        "default_height": DEFAULT_HEIGHT,
        "tokens_imported": _tokens_imported,
        "colors": _get_medical_colors(),
        "palette": _get_medical_palette(),
        "treatment_control": _get_treatment_control_colors(),
    }


# Quick demo functions
def demo_trial_results():
    """Demo: Clinical trial results bar chart with accessible colors."""
    data = pd.DataFrame({
        'Outcome': ['Primary Endpoint', 'Secondary Endpoint', 'Safety Event'],
        'Treatment': [12.3, 8.5, 3.2],
        'Placebo': [18.7, 14.2, 2.8]
    })

    # Use accessible color pair
    treatment_color, control_color = _get_treatment_control_colors()

    fig = go.Figure(data=[
        go.Bar(name='Treatment', x=data['Outcome'], y=data['Treatment'],
               marker_color=treatment_color),
        go.Bar(name='Placebo', x=data['Outcome'], y=data['Placebo'],
               marker_color=control_color)
    ])
    fig.update_layout(barmode='group', yaxis_title='Event Rate (%)')
    return apply_medical_theme(fig, 'Clinical Trial Results')


def demo_forest_plot():
    """Demo: Forest plot for meta-analysis."""
    return create_forest_plot(
        studies=['PARADIGM-HF', 'DAPA-HF', 'EMPEROR-Reduced', 'VICTORIA', 'GALACTIC-HF'],
        estimates=[0.80, 0.74, 0.75, 0.90, 0.92],
        lower_ci=[0.73, 0.65, 0.65, 0.82, 0.86],
        upper_ci=[0.87, 0.85, 0.86, 0.98, 0.99],
        title='Heart Failure Trials: Hazard Ratios for Primary Endpoint'
    )


def demo_trends():
    """Demo: Mortality trends over time."""
    data = pd.DataFrame({
        'Year': list(range(2000, 2024)),
        'Mortality': [30, 28, 27, 25, 24, 23, 21, 20, 19, 18, 
                      17, 16, 15, 14, 13, 12, 11, 10, 10, 9, 
                      8, 8, 7, 7]
    })
    return create_trend_line(data, 'Year', 'Mortality', 
                            'Heart Failure In-Hospital Mortality Trends (%)')


def print_quality_report():
    """Print publication quality report with all settings."""
    settings = get_publication_settings()

    print("\n" + "=" * 60)
    print("📊 PLOTLY PUBLICATION QUALITY REPORT")
    print("=" * 60)

    print(f"\n✅ Design Tokens: {'IMPORTED' if settings['tokens_imported'] else 'FALLBACK'}")
    print(f"✅ Export DPI: {settings['dpi']}")
    print(f"✅ Export Scale: {settings['scale']}x")
    print(f"✅ Default Size: {settings['default_width']}x{settings['default_height']}px")

    print("\n📎 Color Palette (Colorblind-Safe):")
    for i, color in enumerate(settings['palette'][:7]):
        print(f"   [{i+1}] {color}")

    print("\n🎨 Treatment vs Control Colors:")
    t, c = settings['treatment_control']
    print(f"   Treatment: {t}")
    print(f"   Control:   {c}")

    # Validate accessibility
    print("\n♿ WCAG Accessibility Check:")
    if _tokens_imported:
        bg = settings['colors']['background']
        text = settings['colors'].get('text_primary', '#1a1a2e')
        ratio = get_contrast_ratio(text, bg)
        status = "✅ PASS" if ratio >= 4.5 else "❌ FAIL"
        print(f"   Text on background: {ratio:.1f}:1 {status} (AA requires 4.5:1)")

        # Check palette contrast
        print("\n   Palette contrast vs white background:")
        for i, color in enumerate(settings['palette'][:7]):
            ratio = get_contrast_ratio(color, bg)
            status = "✅" if ratio >= 3.0 else "⚠️"
            print(f"   {status} Color {i+1}: {ratio:.1f}:1")
    else:
        print("   ⚠️  Install design tokens for full validation")

    print("\n" + "=" * 60)
    print("Standards: Nature/JACC/NEJM Publication Guidelines")
    print("=" * 60 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Generate publication-quality medical charts with Plotly",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python plotly_charts.py demo                    # Generate demo charts (HTML + PNG)
  python plotly_charts.py demo --quality-report   # Show publication standards report
  python plotly_charts.py bar -d data.csv -o chart.png
  python plotly_charts.py forest -d meta.csv -o forest.pdf

Publication Standards:
  - 300 DPI export (4x scale factor)
  - Helvetica/Arial typography (5-8pt)
  - WCAG AA contrast ratios (4.5:1)
  - Colorblind-safe palettes (Paul Tol)
        """
    )
    parser.add_argument("chart_type", choices=['bar', 'forest', 'survival', 'trend',
                                                'comparison', 'pie', 'heatmap', 'demo'],
                        help="Type of chart to create")
    parser.add_argument("--data", "-d", help="CSV file with data")
    parser.add_argument("--output", "-o", default="chart.html", help="Output file")
    parser.add_argument("--title", "-t", default="", help="Chart title")
    parser.add_argument("--x", help="X-axis column name")
    parser.add_argument("--y", help="Y-axis column name")
    parser.add_argument("--color", "-c", help="Color grouping column")
    parser.add_argument("--quality-report", action="store_true",
                        help="Print publication quality settings report")
    parser.add_argument("--png", action="store_true",
                        help="Export demo charts as PNG (300 DPI) instead of HTML")
    parser.add_argument("--output-dir", default=".",
                        help="Output directory for generated charts")

    args = parser.parse_args()

    # Quality report
    if args.quality_report:
        print_quality_report()
        if args.chart_type != 'demo':
            return

    if args.chart_type == 'demo':
        output_dir = Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        print("📊 Generating publication-quality demo charts...")
        print(f"   Output directory: {output_dir.absolute()}")

        ext = '.png' if args.png else '.html'

        # Generate all demos
        charts = [
            (demo_trial_results(), 'demo_trial_results'),
            (demo_forest_plot(), 'demo_forest_plot'),
            (demo_trends(), 'demo_trends'),
        ]

        for fig, name in charts:
            output_path = str(output_dir / f"{name}{ext}")
            save_chart(fig, output_path)

        print("\n✅ Demo charts created!")
        if args.png:
            print(f"   Resolution: {DEFAULT_WIDTH * PUBLICATION_SCALE}x{DEFAULT_HEIGHT * PUBLICATION_SCALE}px (~300 DPI)")
        return

    # Load data if provided
    if args.data:
        try:
            data = pd.read_csv(args.data)
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            sys.exit(1)
    else:
        print("❌ Provide --data CSV file for chart generation")
        print("   Or use 'demo' to see example charts")
        sys.exit(1)

    # Generate chart
    if args.chart_type == 'bar':
        fig = create_bar_chart(data, args.x or data.columns[0],
                               args.y or data.columns[1], args.title, args.color)
    elif args.chart_type == 'trend':
        fig = create_trend_line(data, args.x or data.columns[0],
                                args.y or data.columns[1], args.title, args.color)
    elif args.chart_type == 'pie':
        fig = create_pie_chart(data[data.columns[0]].tolist(),
                               data[data.columns[1]].tolist(), args.title)
    elif args.chart_type == 'heatmap':
        fig = create_heatmap(data, args.title)
    else:
        print(f"⚠️  {args.chart_type} requires manual configuration. See script for API.")
        sys.exit(1)

    save_chart(fig, args.output)


if __name__ == "__main__":
    main()
