#!/usr/bin/env python3
"""
G2 Charts CLI - Command-Line Interface

Unified CLI for creating medical charts with AntV G2.
Supports both grammar-based and template-based workflows.

Usage:
    python g2_cli.py forest --studies "A,B,C" --estimates "0.8,0.7,0.9" -o forest.png
    python g2_cli.py kaplan --data survival.json -o km.svg --format svg
    python g2_cli.py list-templates
    python g2_cli.py demo --all
"""

import argparse
import json
import sys
from pathlib import Path
from typing import List

from medical_grammars import (
    forest_plot_grammar,
    kaplan_meier_grammar,
    grouped_comparison_grammar,
    scatter_regression_grammar,
    heatmap_grammar
)
from grammar_renderer import G2Chart, list_templates


def parse_list_arg(arg: str) -> List[str]:
    """Parse comma-separated list argument."""
    return [x.strip() for x in arg.split(',')]


def parse_float_list(arg: str) -> List[float]:
    """Parse comma-separated float list."""
    return [float(x.strip()) for x in arg.split(',')]


def cmd_forest_plot(args):
    """Generate forest plot from CLI arguments."""
    if not all([args.studies, args.estimates, args.lower, args.upper]):
        print("❌ Required: --studies, --estimates, --lower, --upper")
        sys.exit(1)

    studies = parse_list_arg(args.studies)
    estimates = parse_float_list(args.estimates)
    lower_ci = parse_float_list(args.lower)
    upper_ci = parse_float_list(args.upper)
    weights = parse_float_list(args.weights) if args.weights else None

    grammar = forest_plot_grammar(
        studies=studies,
        estimates=estimates,
        lower_ci=lower_ci,
        upper_ci=upper_ci,
        weights=weights,
        title=args.title or "Forest Plot"
    )

    chart = G2Chart(width=args.width, height=args.height)
    chart.grammar = grammar
    output = chart.render(args.output, format=args.format)

    print(f"✅ Forest plot saved: {output}")


def cmd_kaplan_meier(args):
    """Generate Kaplan-Meier curve from CLI arguments or data file."""
    if not args.data:
        print("❌ Required: --data (JSON file with time/survival data)")
        sys.exit(1)

    with open(args.data) as f:
        data = json.load(f)

    # Expected format: {"groups": ["A", "B"], "time": [[...], [...]], "survival": [[...], [...]]}
    grammar = kaplan_meier_grammar(
        time_data=data['time'],
        survival_data=data['survival'],
        group_names=data['groups'],
        title=args.title or "Kaplan-Meier Curve"
    )

    chart = G2Chart(width=args.width, height=args.height)
    chart.grammar = grammar
    output = chart.render(args.output, format=args.format)

    print(f"✅ Kaplan-Meier curve saved: {output}")


def cmd_grouped_bars(args):
    """Generate grouped bar chart from CLI arguments or data file."""
    if not args.data:
        print("❌ Required: --data (JSON file with categories/groups/values)")
        sys.exit(1)

    with open(args.data) as f:
        data = json.load(f)

    # Expected format: {"categories": [...], "groups": [...], "values": [[...], [...]]}
    grammar = grouped_comparison_grammar(
        categories=data['categories'],
        groups=data['groups'],
        values=data['values'],
        title=args.title or "Grouped Comparison"
    )

    chart = G2Chart(width=args.width, height=args.height)
    chart.grammar = grammar
    output = chart.render(args.output, format=args.format)

    print(f"✅ Grouped bars saved: {output}")


def cmd_list_templates(args):
    """List available templates."""
    templates = list_templates()
    print("\n📊 Available G2 Medical Templates:\n")
    for i, t in enumerate(templates, 1):
        print(f"   {i}. {t}")
    print("")


def cmd_demo(args):
    """Generate demo charts."""
    from examples.demo_charts import main as demo_main
    sys.argv = ['demo_charts.py']
    if args.all:
        sys.argv.append('all')
    if args.format:
        sys.argv.extend(['--format', args.format])
    demo_main()


def main():
    parser = argparse.ArgumentParser(
        description='AntV G2 Medical Charts - Command-Line Interface',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Forest plot from arguments
  python g2_cli.py forest --studies "A,B,C" --estimates "0.8,0.7,0.9" \\
    --lower "0.7,0.6,0.8" --upper "0.9,0.8,1.0" -o forest.png

  # Kaplan-Meier from data file
  python g2_cli.py kaplan --data survival.json -o km.svg --format svg

  # Grouped bars from data file
  python g2_cli.py grouped --data trial_results.json -o bars.png

  # List available templates
  python g2_cli.py list-templates

  # Generate all demos
  python g2_cli.py demo --all
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='Chart type or command')

    # Forest plot
    forest_parser = subparsers.add_parser('forest', help='Generate forest plot')
    forest_parser.add_argument('--studies', help='Comma-separated study names')
    forest_parser.add_argument('--estimates', help='Comma-separated estimates')
    forest_parser.add_argument('--lower', help='Comma-separated lower CI bounds')
    forest_parser.add_argument('--upper', help='Comma-separated upper CI bounds')
    forest_parser.add_argument('--weights', help='Comma-separated weights (optional)')
    forest_parser.add_argument('--title', help='Chart title')
    forest_parser.add_argument('--output', '-o', default='forest.png', help='Output file')
    forest_parser.add_argument('--format', '-f', choices=['png', 'svg'], default='png')
    forest_parser.add_argument('--width', type=int, default=900)
    forest_parser.add_argument('--height', type=int, default=500)

    # Kaplan-Meier
    km_parser = subparsers.add_parser('kaplan', help='Generate Kaplan-Meier curve')
    km_parser.add_argument('--data', '-d', required=True, help='JSON data file')
    km_parser.add_argument('--title', help='Chart title')
    km_parser.add_argument('--output', '-o', default='kaplan.png', help='Output file')
    km_parser.add_argument('--format', '-f', choices=['png', 'svg'], default='png')
    km_parser.add_argument('--width', type=int, default=800)
    km_parser.add_argument('--height', type=int, default=600)

    # Grouped bars
    bars_parser = subparsers.add_parser('grouped', help='Generate grouped bar chart')
    bars_parser.add_argument('--data', '-d', required=True, help='JSON data file')
    bars_parser.add_argument('--title', help='Chart title')
    bars_parser.add_argument('--output', '-o', default='grouped.png', help='Output file')
    bars_parser.add_argument('--format', '-f', choices=['png', 'svg'], default='png')
    bars_parser.add_argument('--width', type=int, default=800)
    bars_parser.add_argument('--height', type=int, default=600)

    # List templates
    subparsers.add_parser('list-templates', help='List available templates')

    # Demo
    demo_parser = subparsers.add_parser('demo', help='Generate demo charts')
    demo_parser.add_argument('--all', action='store_true', help='Generate all demos')
    demo_parser.add_argument('--format', '-f', choices=['png', 'svg'], default='png')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Route to command handlers
    commands = {
        'forest': cmd_forest_plot,
        'kaplan': cmd_kaplan_meier,
        'grouped': cmd_grouped_bars,
        'list-templates': cmd_list_templates,
        'demo': cmd_demo
    }

    handler = commands.get(args.command)
    if handler:
        handler(args)
    else:
        print(f"❌ Unknown command: {args.command}")
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
