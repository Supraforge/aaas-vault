#!/usr/bin/env python3
"""
G2 Medical Charts - Demo Examples

Demonstrates all available medical chart grammars with realistic data.
Generates publication-quality outputs for forest plots, Kaplan-Meier curves,
grouped comparisons, multi-panel figures, and more.

Usage:
    python demo_charts.py              # Generate all demos
    python demo_charts.py forest       # Generate forest plot only
    python demo_charts.py --format svg # Generate SVG outputs
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from medical_grammars import (
    forest_plot_grammar,
    kaplan_meier_grammar,
    grouped_comparison_grammar,
    multi_panel_grammar,
    scatter_regression_grammar,
    heatmap_grammar
)
from grammar_renderer import G2Chart
import json


def demo_forest_plot(output_dir: Path, format: str = 'png'):
    """Demo: Meta-analysis forest plot"""
    print("📊 Generating forest plot...")

    grammar = forest_plot_grammar(
        studies=[
            'PARADIGM-HF',
            'DAPA-HF',
            'EMPEROR-Reduced',
            'VICTORIA',
            'GALACTIC-HF'
        ],
        estimates=[0.80, 0.74, 0.75, 0.90, 0.92],
        lower_ci=[0.73, 0.65, 0.65, 0.82, 0.86],
        upper_ci=[0.87, 0.85, 0.86, 0.98, 0.99],
        weights=[84, 60, 50, 40, 35],
        title="Heart Failure Trials: Hazard Ratios for Primary Endpoint"
    )

    output = output_dir / f'demo_forest_plot.{format}'

    # Save grammar for reference
    with open(output_dir / 'demo_forest_plot_grammar.json', 'w') as f:
        json.dump(grammar, f, indent=2)

    chart = G2Chart(width=900, height=500)
    chart.grammar = grammar
    chart.render(str(output), format=format)

    return output


def demo_kaplan_meier(output_dir: Path, format: str = 'png'):
    """Demo: Kaplan-Meier survival curves"""
    print("📊 Generating Kaplan-Meier curve...")

    # Simulated survival data
    treatment_time = [0, 3, 6, 9, 12, 18, 24, 30, 36]
    treatment_survival = [1.0, 0.95, 0.90, 0.85, 0.82, 0.78, 0.75, 0.72, 0.70]

    control_time = [0, 3, 6, 9, 12, 18, 24, 30, 36]
    control_survival = [1.0, 0.92, 0.85, 0.78, 0.72, 0.65, 0.58, 0.52, 0.48]

    grammar = kaplan_meier_grammar(
        time_data=[treatment_time, control_time],
        survival_data=[treatment_survival, control_survival],
        group_names=['Treatment', 'Control'],
        title="Overall Survival (DAPA-HF Trial)",
        xlabel="Time (months)",
        ylabel="Survival Probability"
    )

    output = output_dir / f'demo_kaplan_meier.{format}'

    with open(output_dir / 'demo_kaplan_meier_grammar.json', 'w') as f:
        json.dump(grammar, f, indent=2)

    chart = G2Chart(width=800, height=600)
    chart.grammar = grammar
    chart.render(str(output), format=format)

    return output


def demo_grouped_bars(output_dir: Path, format: str = 'png'):
    """Demo: Grouped bar chart for treatment comparisons"""
    print("📊 Generating grouped comparison...")

    grammar = grouped_comparison_grammar(
        categories=['Primary Endpoint', 'CV Death', 'HF Hospitalization', 'Safety Events'],
        groups=['Treatment', 'Placebo'],
        values=[
            [12.3, 8.1, 5.2, 3.4],  # Treatment
            [18.7, 12.5, 9.8, 2.9]   # Placebo
        ],
        title="Clinical Trial Results: Treatment vs Placebo",
        ylabel="Event Rate (%)"
    )

    output = output_dir / f'demo_grouped_bars.{format}'

    with open(output_dir / 'demo_grouped_bars_grammar.json', 'w') as f:
        json.dump(grammar, f, indent=2)

    chart = G2Chart(width=800, height=600)
    chart.grammar = grammar
    chart.render(str(output), format=format)

    return output


def demo_scatter_regression(output_dir: Path, format: str = 'png'):
    """Demo: Scatter plot with regression line"""
    print("📊 Generating scatter plot with regression...")

    # Simulated data: EF vs NT-proBNP
    ef_values = [25, 30, 28, 35, 22, 38, 32, 27, 40, 24, 36, 29, 33, 26, 31]
    bnp_values = [2800, 2200, 2500, 1800, 3200, 1500, 2000, 2700, 1200, 3000, 1600, 2400, 1900, 2900, 2100]

    grammar = scatter_regression_grammar(
        x_data=ef_values,
        y_data=bnp_values,
        regression_line=True,
        title="LVEF vs NT-proBNP Correlation",
        xlabel="Left Ventricular Ejection Fraction (%)",
        ylabel="NT-proBNP (pg/mL)"
    )

    output = output_dir / f'demo_scatter.{format}'

    with open(output_dir / 'demo_scatter_grammar.json', 'w') as f:
        json.dump(grammar, f, indent=2)

    chart = G2Chart(width=800, height=600)
    chart.grammar = grammar
    chart.render(str(output), format=format)

    return output


def demo_heatmap(output_dir: Path, format: str = 'png'):
    """Demo: Heatmap for biomarker correlations"""
    print("📊 Generating correlation heatmap...")

    # Simulated correlation matrix
    biomarkers = ['BNP', 'Troponin', 'CRP', 'Creatinine', 'eGFR']
    correlations = []

    values_matrix = [
        [1.00, 0.65, 0.42, 0.58, -0.72],
        [0.65, 1.00, 0.38, 0.45, -0.55],
        [0.42, 0.38, 1.00, 0.32, -0.28],
        [0.58, 0.45, 0.32, 1.00, -0.89],
        [-0.72, -0.55, -0.28, -0.89, 1.00]
    ]

    for i, marker1 in enumerate(biomarkers):
        for j, marker2 in enumerate(biomarkers):
            correlations.append({
                'marker1': marker1,
                'marker2': marker2,
                'correlation': values_matrix[i][j]
            })

    grammar = heatmap_grammar(
        data=correlations,
        x_field='marker1',
        y_field='marker2',
        value_field='correlation',
        title="Biomarker Correlation Matrix"
    )

    output = output_dir / f'demo_heatmap.{format}'

    with open(output_dir / 'demo_heatmap_grammar.json', 'w') as f:
        json.dump(grammar, f, indent=2)

    chart = G2Chart(width=700, height=700)
    chart.grammar = grammar
    chart.render(str(output), format=format)

    return output


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Generate G2 medical chart demos')
    parser.add_argument(
        'chart',
        nargs='?',
        choices=['forest', 'kaplan', 'grouped', 'scatter', 'heatmap', 'all'],
        default='all',
        help='Chart type to generate'
    )
    parser.add_argument(
        '--format', '-f',
        choices=['png', 'svg'],
        default='png',
        help='Output format'
    )
    parser.add_argument(
        '--output-dir', '-o',
        default='outputs',
        help='Output directory'
    )

    args = parser.parse_args()

    output_dir = Path(__file__).parent.parent / args.output_dir
    output_dir.mkdir(exist_ok=True)

    print("\n🎨 G2 Medical Charts Demo")
    print("=" * 50)
    print(f"Output directory: {output_dir.absolute()}")
    print(f"Format: {args.format.upper()}")
    print("=" * 50 + "\n")

    demos = {
        'forest': demo_forest_plot,
        'kaplan': demo_kaplan_meier,
        'grouped': demo_grouped_bars,
        'scatter': demo_scatter_regression,
        'heatmap': demo_heatmap
    }

    if args.chart == 'all':
        for name, func in demos.items():
            try:
                output = func(output_dir, args.format)
                print(f"✅ {name}: {output.name}\n")
            except Exception as e:
                print(f"❌ {name}: {e}\n")
    else:
        try:
            output = demos[args.chart](output_dir, args.format)
            print(f"✅ Generated: {output.name}\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")
            sys.exit(1)

    print("=" * 50)
    print(f"✅ Demo complete! Check {output_dir.absolute()}")
    print("=" * 50 + "\n")


if __name__ == '__main__':
    main()
