#!/usr/bin/env python3
"""
AntV Infographic CLI

Comprehensive command-line interface for AntV Infographic integration.
Provides easy access to templates, rendering, and examples.
"""

import sys
import argparse
from pathlib import Path
from antv_renderer import AntvRenderer, list_templates


def cmd_list(args):
    """List available templates."""
    templates = list_templates()

    if args.verbose:
        print(f"\n📋 Available AntV Infographic Templates ({len(templates)} total)")
        print("=" * 60)

        template_descriptions = {
            'trial_result_simple': 'Clinical trial timeline (4 phases)',
            'mechanism_of_action': 'Drug mechanism steps (5 steps)',
            'treatment_comparison': 'Side-by-side treatment comparison',
            'patient_journey': 'Patient care pathway (5 stages)',
            'guideline_recommendations': 'Guideline strength classification',
            'dosing_schedule': 'Medication dosing schedule (4 weeks)',
            'safety_profile': 'Adverse events by frequency',
            'biomarker_progression': 'Biomarker changes over time',
            'trial_endpoints': 'Primary and secondary endpoints',
            'risk_stratification': 'Risk level classification',
            'diagnostic_pathway': 'Diagnostic workflow (5 steps)',
        }

        for template in sorted(templates):
            desc = template_descriptions.get(template, 'No description')
            print(f"  • {template:30} {desc}")

    else:
        for template in templates:
            print(template)


def cmd_render(args):
    """Render a template or spec."""
    renderer = AntvRenderer()

    if args.template:
        print(f"📊 Rendering template: {args.template}")
        output = renderer.render_template_to_html(
            args.template,
            args.output,
            width=args.width,
            height=args.height,
            title=args.title or f"AntV Infographic: {args.template}"
        )
    elif args.spec:
        print(f"📊 Rendering custom spec")
        output = renderer.render_to_html(
            args.spec,
            args.output,
            width=args.width,
            height=args.height,
            title=args.title or "AntV Infographic"
        )
    else:
        print("❌ Error: Either --template or --spec is required")
        sys.exit(1)

    print(f"✅ HTML file generated: {output}")
    print(f"\n📂 Next steps:")
    print(f"  1. Open {output} in your browser")
    print(f"  2. Click 'Download SVG' to save as vector graphic")
    print(f"  3. Click 'Download PNG' to save as raster image")


def cmd_examples(args):
    """Generate example outputs for all templates."""
    renderer = AntvRenderer()
    templates = renderer.list_templates()

    print(f"\n🎨 Generating {len(templates)} example infographics")
    print("=" * 60)

    outputs_dir = renderer.outputs_dir / 'examples'
    outputs_dir.mkdir(exist_ok=True)

    for template in templates:
        try:
            output = outputs_dir / f'{template}.html'
            renderer.render_template_to_html(
                template,
                output,
                width=args.width,
                height=args.height
            )
            print(f"  ✅ {template:30} → {output.name}")
        except Exception as e:
            print(f"  ❌ {template:30} → Error: {e}")

    print(f"\n📂 All examples saved to: {outputs_dir}")


def cmd_info(args):
    """Show information about AntV Infographic integration."""
    print("""
╔══════════════════════════════════════════════════════════════╗
║                 AntV Infographic Integration                 ║
╚══════════════════════════════════════════════════════════════╝

📦 Package: @antv/infographic v0.2.3
🎯 Purpose: Template-driven medical infographics with 200+ templates
🔧 Status: Integrated into visual-design-system

KEY FEATURES:
  • 200+ built-in infographic templates
  • AI-optimized declarative syntax (YAML-like)
  • SVG output (editable, scalable, publication-ready)
  • Theme system with gradients and patterns
  • Streaming-compatible for LLM generation

MEDICAL USE CASES:
  • Trial result summary cards
  • Patient education infographics
  • Social media carousels
  • Research paper figures
  • Treatment pathway diagrams

INTEGRATION POINTS:
  • Python API: antv_renderer.py
  • Visual Router: Automatically routes template requests
  • CLI: antv_cli.py (this tool)
  • Templates: 11 medical-specific presets

DIRECTORIES:
  scripts/       Python wrapper and Node.js renderer
  templates/     Medical infographic templates (.txt files)
  outputs/       Generated HTML/SVG/PNG files
  examples/      Example outputs for all templates

USAGE:
  # List templates
  python antv_cli.py list

  # Render template
  python antv_cli.py render --template trial_result_simple

  # Generate examples
  python antv_cli.py examples

  # Python API
  from antv_renderer import render_template
  render_template('mechanism_of_action', 'output.html')

WORKFLOW:
  1. Choose template or write custom spec
  2. Render to HTML (opens in browser)
  3. Download as SVG or PNG
  4. Use in presentations, papers, social media

For more info, see: skills/cardiology/visual-design-system/antv_infographic/
    """)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='AntV Infographic CLI - Medical infographic generation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # List all templates
  python antv_cli.py list --verbose

  # Render a template
  python antv_cli.py render --template mechanism_of_action

  # Render custom spec
  python antv_cli.py render --spec "infographic list-row-simple..."

  # Generate all examples
  python antv_cli.py examples

  # Show integration info
  python antv_cli.py info
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # List command
    list_parser = subparsers.add_parser('list', help='List available templates')
    list_parser.add_argument('--verbose', '-v', action='store_true',
                            help='Show template descriptions')
    list_parser.set_defaults(func=cmd_list)

    # Render command
    render_parser = subparsers.add_parser('render', help='Render infographic')
    render_parser.add_argument('--template', '-t', help='Template name')
    render_parser.add_argument('--spec', '-s', help='Custom spec string')
    render_parser.add_argument('--output', '-o', help='Output HTML file path')
    render_parser.add_argument('--width', type=int, default=800, help='Canvas width (default: 800)')
    render_parser.add_argument('--height', type=int, default=600, help='Canvas height (default: 600)')
    render_parser.add_argument('--title', help='HTML page title')
    render_parser.set_defaults(func=cmd_render)

    # Examples command
    examples_parser = subparsers.add_parser('examples', help='Generate example outputs')
    examples_parser.add_argument('--width', type=int, default=800, help='Canvas width (default: 800)')
    examples_parser.add_argument('--height', type=int, default=600, help='Canvas height (default: 600)')
    examples_parser.set_defaults(func=cmd_examples)

    # Info command
    info_parser = subparsers.add_parser('info', help='Show integration information')
    info_parser.set_defaults(func=cmd_info)

    # Parse and execute
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    args.func(args)


if __name__ == '__main__':
    main()
