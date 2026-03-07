#!/usr/bin/env python3
"""
AntV G2 Grammar-Based Chart Renderer - Python Interface

Provides Python API for creating publication-grade charts using
G2's declarative grammar approach. Bridges to Node.js renderer.

Usage:
    from grammar_renderer import G2Chart, render_medical_chart

    # Using templates
    render_medical_chart(
        'forest_plot',
        data=[...],
        output='forest.png'
    )

    # Custom grammar
    chart = G2Chart(width=800, height=600)
    chart.add_mark('interval', encode={'x': 'category', 'y': 'value'})
    chart.render('chart.png')
"""

import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Literal


class G2Chart:
    """
    Grammar-based chart builder for AntV G2.

    Follows the declarative grammar paradigm:
    - Data: What data to visualize
    - Marks: How to draw the data (geometry layers)
    - Scales: How to map data to visual properties
    - Coordinates: Coordinate transformations
    - Axes: Axis configuration
    - Legends: Legend configuration
    """

    def __init__(
        self,
        width: int = 800,
        height: int = 600,
        padding: Optional[List[int]] = None
    ):
        """
        Initialize a new G2 chart.

        Args:
            width: Chart width in pixels
            height: Chart height in pixels
            padding: Padding [top, right, bottom, left]
        """
        self.width = width
        self.height = height
        self.padding = padding or [40, 60, 40, 60]

        self.grammar = {
            'data': [],
            'marks': [],
            'scales': {},
            'coordinate': None,
            'xAxis': {},
            'yAxis': {},
            'legend': {},
            'interactions': []
        }

    def data(self, data: List[Dict[str, Any]]):
        """Set chart data."""
        self.grammar['data'] = data
        return self

    def add_mark(
        self,
        mark_type: Literal['point', 'line', 'interval', 'area', 'cell', 'rect', 'text'],
        encode: Dict[str, str],
        style: Optional[Dict[str, Any]] = None,
        transform: Optional[List[Any]] = None
    ):
        """
        Add a mark (geometry layer) to the chart.

        Args:
            mark_type: Type of mark (point, line, interval, area, etc.)
            encode: Channel encodings (x, y, color, size, etc.)
            style: Visual styles (fillOpacity, stroke, etc.)
            transform: Data transformations
        """
        mark = {
            'type': mark_type,
            'encode': encode
        }

        if style:
            mark['style'] = style

        if transform:
            mark['transform'] = transform

        self.grammar['marks'].append(mark)
        return self

    def scale(self, channel: str, spec: Dict[str, Any]):
        """
        Configure a scale for a channel.

        Args:
            channel: Channel name (x, y, color, size, etc.)
            spec: Scale specification (type, domain, range, etc.)
        """
        self.grammar['scales'][channel] = spec
        return self

    def coordinate(self, coord_type: str, transform: Optional[List[str]] = None):
        """
        Set coordinate system.

        Args:
            coord_type: Coordinate type (transpose, polar, etc.)
            transform: Coordinate transformations
        """
        self.grammar['coordinate'] = {
            'type': coord_type
        }

        if transform:
            self.grammar['coordinate']['transform'] = transform

        return self

    def axis(
        self,
        axis: Literal['x', 'y'],
        title: Optional[str] = None,
        grid: bool = True,
        **kwargs
    ):
        """Configure axis."""
        axis_key = f"{axis}Axis"
        self.grammar[axis_key] = {
            'title': title,
            'grid': grid,
            **kwargs
        }
        return self

    def legend(self, position: str = 'bottom', **kwargs):
        """Configure legend."""
        self.grammar['legend'] = {
            'position': position,
            **kwargs
        }
        return self

    def interaction(self, interaction_type: str):
        """Add interaction."""
        self.grammar['interactions'].append(interaction_type)
        return self

    def render(
        self,
        output: str,
        format: Literal['png', 'svg'] = 'png',
        renderer_path: Optional[Path] = None
    ) -> str:
        """
        Render the chart using Node.js backend.

        Args:
            output: Output file path
            format: Output format (png or svg)
            renderer_path: Path to renderer.js (auto-detected if None)

        Returns:
            Path to rendered file
        """
        if renderer_path is None:
            renderer_path = Path(__file__).parent / 'renderer.js'

        if not renderer_path.exists():
            raise FileNotFoundError(f"Renderer not found: {renderer_path}")

        # Create temp grammar file
        grammar_file = Path(__file__).parent / 'outputs' / '_temp_grammar.json'
        grammar_file.parent.mkdir(exist_ok=True)

        with open(grammar_file, 'w') as f:
            json.dump(self.grammar, f, indent=2)

        # Call Node.js renderer
        cmd = [
            'node',
            str(renderer_path),
            '--spec', str(grammar_file),
            '--output', output,
            '--width', str(self.width),
            '--height', str(self.height),
            '--format', format
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            raise RuntimeError(f"Rendering failed: {result.stderr}")

        # Clean up temp file
        grammar_file.unlink()

        print(result.stdout)
        return output


def render_medical_chart(
    template: Literal['forest_plot', 'kaplan_meier', 'grouped_bars', 'multi_panel', 'consort_flow'],
    data: List[Dict[str, Any]],
    output: str,
    width: int = 800,
    height: int = 600,
    format: Literal['png', 'svg'] = 'png'
) -> str:
    """
    Render a chart using a medical template.

    Args:
        template: Template name
        data: Chart data
        output: Output file path
        width: Chart width
        height: Chart height
        format: Output format

    Returns:
        Path to rendered file
    """
    renderer_path = Path(__file__).parent / 'renderer.js'

    if not renderer_path.exists():
        raise FileNotFoundError(f"Renderer not found: {renderer_path}")

    # Create temp data file
    data_file = Path(__file__).parent / 'outputs' / '_temp_data.json'
    data_file.parent.mkdir(exist_ok=True)

    with open(data_file, 'w') as f:
        json.dump(data, f, indent=2)

    # Call Node.js renderer
    cmd = [
        'node',
        str(renderer_path),
        '--template', template,
        '--data', str(data_file),
        '--output', output,
        '--width', str(width),
        '--height', str(height),
        '--format', format
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError(f"Rendering failed: {result.stderr}")

    # Clean up temp file
    data_file.unlink()

    print(result.stdout)
    return output


def list_templates() -> List[str]:
    """List available medical chart templates."""
    templates_dir = Path(__file__).parent / 'templates'

    if not templates_dir.exists():
        return []

    return [
        f.stem for f in templates_dir.glob('*.json')
    ]


# CLI interface
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='AntV G2 Grammar-Based Chart Renderer - Python Interface'
    )

    parser.add_argument(
        'template',
        nargs='?',
        help='Medical chart template name'
    )
    parser.add_argument(
        '--data', '-d',
        help='Data file (JSON)'
    )
    parser.add_argument(
        '--output', '-o',
        default='chart.png',
        help='Output file path'
    )
    parser.add_argument(
        '--width', '-w',
        type=int,
        default=800,
        help='Chart width in pixels'
    )
    parser.add_argument(
        '--height', '-h',
        type=int,
        default=600,
        help='Chart height in pixels'
    )
    parser.add_argument(
        '--format', '-f',
        choices=['png', 'svg'],
        default='png',
        help='Output format'
    )
    parser.add_argument(
        '--list', '-l',
        action='store_true',
        help='List available templates'
    )

    args = parser.parse_args()

    if args.list:
        templates = list_templates()
        print('\n📊 Available G2 Medical Templates:\n')
        for i, t in enumerate(templates, 1):
            print(f'   {i}. {t}')
        print('')
        sys.exit(0)

    if not args.template:
        parser.print_help()
        sys.exit(1)

    if not args.data:
        print('❌ Provide --data file')
        sys.exit(1)

    # Load data
    with open(args.data) as f:
        data = json.load(f)

    # Render chart
    render_medical_chart(
        template=args.template,
        data=data,
        output=args.output,
        width=args.width,
        height=args.height,
        format=args.format
    )
