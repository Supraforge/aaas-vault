#!/usr/bin/env python3
"""
CLI interface for Vizzu animated visualizations.

Usage:
    python vizzu_cli.py demo --template kaplan-meier
    python vizzu_cli.py create --template bar-comparison --data data.csv
    python vizzu_cli.py export animation.html --format mp4
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Optional

import pandas as pd

from data_animator import VizzuAnimator
from export_utils import export_to_mp4, export_to_gif, export_to_webm
from templates import (
    create_animated_bar_comparison,
    create_animated_forest_plot,
    create_animated_kaplan_meier,
    create_animated_trend_line,
    create_animated_trial_enrollment,
)


def generate_demo_kaplan_meier(output: Optional[Path] = None) -> Path:
    """Generate demo Kaplan-Meier curves."""
    treatment = [(0, 100), (6, 94), (12, 88), (18, 83), (24, 78)]
    control = [(0, 100), (6, 91), (12, 83), (18, 76), (24, 69)]

    return create_animated_kaplan_meier(
        treatment,
        control,
        treatment_name="Dapagliflozin",
        control_name="Placebo",
        title="DAPA-HF: Event-Free Survival",
        hr_text="HR 0.74 (95% CI 0.65-0.85)",
        output=output,
    )


def generate_demo_forest_plot(output: Optional[Path] = None) -> Path:
    """Generate demo forest plot."""
    studies = [
        {"name": "DAPA-HF", "estimate": 0.74, "lower": 0.65, "upper": 0.85, "weight": 60},
        {"name": "EMPEROR-Reduced", "estimate": 0.75, "lower": 0.65, "upper": 0.86, "weight": 50},
        {"name": "SOLOIST-WHF", "estimate": 0.67, "lower": 0.52, "upper": 0.85, "weight": 30},
        {"name": "DELIVER", "estimate": 0.82, "lower": 0.73, "upper": 0.92, "weight": 70},
    ]

    return create_animated_forest_plot(
        studies,
        title="SGLT2 Inhibitors in Heart Failure",
        output=output,
        show_pooled=True,
    )


def generate_demo_bar_comparison(output: Optional[Path] = None) -> Path:
    """Generate demo bar comparison."""
    return create_animated_bar_comparison(
        categories=["Primary Endpoint", "CV Death", "HF Hospitalization"],
        group1_values=[16.3, 11.6, 10.0],
        group2_values=[21.2, 14.5, 15.6],
        group1_name="Dapagliflozin",
        group2_name="Placebo",
        title="DAPA-HF Trial Results",
        y_label="Event Rate (%)",
        output=output,
    )


def generate_demo_trend_line(output: Optional[Path] = None) -> Path:
    """Generate demo trend line."""
    data = {
        "2010-2015": [(2010, 28.5), (2012, 26.2), (2015, 23.8)],
        "2015-2020": [(2015, 23.8), (2017, 21.5), (2020, 19.2)],
        "2020-2024": [(2020, 19.2), (2022, 17.8), (2024, 16.5)],
    }

    return create_animated_trend_line(
        data,
        title="Heart Failure Mortality Trends (2010-2024)",
        x_label="Year",
        y_label="Age-Adjusted Mortality Rate (per 100,000)",
        output=output,
    )


def generate_demo_trial_enrollment(output: Optional[Path] = None) -> Path:
    """Generate demo trial enrollment."""
    enrollment = [
        ("Month 1", 142),
        ("Month 3", 456),
        ("Month 6", 1024),
        ("Month 9", 2187),
        ("Month 12", 3456),
        ("Month 15", 4320),
        ("Month 18", 4744),
    ]

    return create_animated_trial_enrollment(
        enrollment,
        target=4744,
        title="DAPA-HF Enrollment Progress",
        output=output,
    )


def cmd_demo(args: argparse.Namespace) -> int:
    """Generate demo animations."""
    demos = {
        "kaplan-meier": generate_demo_kaplan_meier,
        "forest-plot": generate_demo_forest_plot,
        "bar-comparison": generate_demo_bar_comparison,
        "trend-line": generate_demo_trend_line,
        "trial-enrollment": generate_demo_trial_enrollment,
    }

    if args.template == "all":
        print("Generating all demo animations...")
        for name, func in demos.items():
            output = func()
            print(f"  ✅ {name}: {output}")
        return 0

    if args.template not in demos:
        print(f"Unknown template: {args.template}")
        print(f"Available: {', '.join(demos.keys())}, all")
        return 1

    output = demos[args.template](args.output)
    print(f"✅ Demo animation generated: {output}")
    return 0


def cmd_create(args: argparse.Namespace) -> int:
    """Create custom animation from data."""
    # Load data
    if args.data.endswith('.csv'):
        df = pd.read_csv(args.data)
    elif args.data.endswith('.json'):
        df = pd.read_json(args.data)
    else:
        print("Unsupported data format. Use CSV or JSON.")
        return 1

    # Create animator
    animator = VizzuAnimator()

    # Route to appropriate template
    if args.template == "bar":
        output = animator.create_animated_bar(
            df,
            x_col=args.x,
            y_col=args.y,
            color_col=args.color,
            title=args.title or "Bar Chart",
            output=args.output,
        )
    elif args.template == "line":
        output = animator.create_animated_line(
            df,
            x_col=args.x,
            y_col=args.y,
            series_col=args.color,
            title=args.title or "Line Chart",
            output=args.output,
        )
    elif args.template == "scatter":
        output = animator.create_animated_scatter(
            df,
            x_col=args.x,
            y_col=args.y,
            size_col=args.size,
            color_col=args.color,
            title=args.title or "Scatter Plot",
            output=args.output,
        )
    elif args.template == "area":
        output = animator.create_animated_area(
            df,
            x_col=args.x,
            y_col=args.y,
            series_col=args.color,
            title=args.title or "Area Chart",
            output=args.output,
        )
    else:
        print(f"Unknown template: {args.template}")
        return 1

    print(f"✅ Animation created: {output}")
    return 0


def cmd_export(args: argparse.Namespace) -> int:
    """Export HTML animation to video format."""
    html_path = Path(args.input)
    if not html_path.exists():
        print(f"File not found: {html_path}")
        return 1

    try:
        if args.format == "mp4":
            output = export_to_mp4(
                html_path,
                args.output,
                duration=args.duration,
                fps=args.fps,
                width=args.width,
                height=args.height,
            )
        elif args.format == "gif":
            output = export_to_gif(
                html_path,
                args.output,
                duration=args.duration,
                fps=args.fps,
                width=args.width,
                height=args.height,
            )
        elif args.format == "webm":
            output = export_to_webm(
                html_path,
                args.output,
                duration=args.duration,
                fps=args.fps,
                width=args.width,
                height=args.height,
            )
        else:
            print(f"Unknown format: {args.format}")
            return 1

        print(f"✅ Exported to {args.format.upper()}: {output}")
        return 0

    except Exception as e:
        print(f"❌ Export failed: {e}")
        return 1


def cmd_list(args: argparse.Namespace) -> int:
    """List available templates."""
    print("\n📊 Medical Animation Templates:\n")
    templates = [
        ("kaplan-meier", "Animated Kaplan-Meier survival curves"),
        ("forest-plot", "Animated forest plot for meta-analysis"),
        ("bar-comparison", "Animated bar chart for group comparisons"),
        ("trend-line", "Animated line chart for trends over time"),
        ("trial-enrollment", "Animated trial enrollment dashboard"),
    ]

    for name, desc in templates:
        print(f"  • {name:20s} - {desc}")

    print("\n🎨 Generic Chart Types:\n")
    charts = [
        ("bar", "Bar chart"),
        ("line", "Line chart"),
        ("scatter", "Scatter plot"),
        ("area", "Area chart"),
    ]

    for name, desc in charts:
        print(f"  • {name:20s} - {desc}")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Vizzu animated data visualizations for cardiology",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Demo command
    demo_parser = subparsers.add_parser("demo", help="Generate demo animations")
    demo_parser.add_argument(
        "--template",
        choices=["kaplan-meier", "forest-plot", "bar-comparison", "trend-line", "trial-enrollment", "all"],
        default="all",
        help="Demo template to generate",
    )
    demo_parser.add_argument("--output", type=Path, help="Output file path")

    # Create command
    create_parser = subparsers.add_parser("create", help="Create animation from data")
    create_parser.add_argument("--template", required=True, choices=["bar", "line", "scatter", "area"])
    create_parser.add_argument("--data", required=True, help="Data file (CSV or JSON)")
    create_parser.add_argument("--x", required=True, help="Column for x-axis")
    create_parser.add_argument("--y", required=True, help="Column for y-axis")
    create_parser.add_argument("--color", help="Column for color grouping")
    create_parser.add_argument("--size", help="Column for size (scatter only)")
    create_parser.add_argument("--title", help="Chart title")
    create_parser.add_argument("--output", type=Path, help="Output file path")

    # Export command
    export_parser = subparsers.add_parser("export", help="Export HTML to video")
    export_parser.add_argument("input", help="Input HTML file")
    export_parser.add_argument("--format", choices=["mp4", "gif", "webm"], default="mp4")
    export_parser.add_argument("--output", type=Path, help="Output file path")
    export_parser.add_argument("--duration", type=int, default=5000, help="Animation duration (ms)")
    export_parser.add_argument("--fps", type=int, default=30, help="Frames per second")
    export_parser.add_argument("--width", type=int, default=800, help="Width in pixels")
    export_parser.add_argument("--height", type=int, default=600, help="Height in pixels")

    # List command
    list_parser = subparsers.add_parser("list", help="List available templates")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    if args.command == "demo":
        return cmd_demo(args)
    elif args.command == "create":
        return cmd_create(args)
    elif args.command == "export":
        return cmd_export(args)
    elif args.command == "list":
        return cmd_list(args)

    return 0


if __name__ == "__main__":
    sys.exit(main())
