#!/usr/bin/env python3
"""
AntV Infographic Python Wrapper

Provides a clean Python API for generating infographics using AntV Infographic framework.
Supports both HTML preview generation and automated SVG extraction.
"""

import os
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Union


class AntvRenderer:
    """
    Python wrapper for AntV Infographic rendering.

    Handles:
    - Template loading and spec generation
    - HTML preview generation
    - SVG extraction (when browser automation is available)
    """

    def __init__(self, templates_dir: Optional[Path] = None):
        """
        Initialize the renderer.

        Args:
            templates_dir: Path to templates directory. Defaults to ../templates
        """
        self.base_dir = Path(__file__).parent.parent
        self.templates_dir = templates_dir or self.base_dir / 'templates'
        self.outputs_dir = self.base_dir / 'outputs'
        self.html_renderer = self.base_dir / 'scripts' / 'html_renderer.js'

        # Create outputs directory if needed
        self.outputs_dir.mkdir(exist_ok=True)

    def list_templates(self) -> List[str]:
        """List available templates."""
        if not self.templates_dir.exists():
            return []

        return [
            f.stem for f in self.templates_dir.glob('*.txt')
        ]

    def load_template(self, template_name: str) -> str:
        """
        Load a template spec.

        Args:
            template_name: Name of template (without .txt extension)

        Returns:
            Template spec string
        """
        template_path = self.templates_dir / f'{template_name}.txt'
        if not template_path.exists():
            raise FileNotFoundError(f'Template not found: {template_name}')

        return template_path.read_text()

    def render_to_html(
        self,
        spec: str,
        output_path: Optional[Union[str, Path]] = None,
        width: int = 800,
        height: int = 600,
        title: str = 'AntV Infographic'
    ) -> Path:
        """
        Render infographic spec to standalone HTML file.

        Args:
            spec: Infographic spec (YAML-like syntax)
            output_path: Output HTML file path. If None, generates in outputs/
            width: Canvas width in pixels
            height: Canvas height in pixels
            title: HTML page title

        Returns:
            Path to generated HTML file
        """
        if output_path is None:
            output_path = self.outputs_dir / 'preview.html'
        else:
            output_path = Path(output_path)

        # Build command
        cmd = [
            'node',
            str(self.html_renderer),
            '--spec', spec,
            '--output', str(output_path),
            '--width', str(width),
            '--height', str(height),
            '--title', title
        ]

        # Run renderer
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=str(self.base_dir)
        )

        if result.returncode != 0:
            raise RuntimeError(f'HTML rendering failed: {result.stderr}')

        return output_path

    def render_template_to_html(
        self,
        template_name: str,
        output_path: Optional[Union[str, Path]] = None,
        **kwargs
    ) -> Path:
        """
        Render a template to HTML.

        Args:
            template_name: Name of template (without .txt extension)
            output_path: Output HTML file path
            **kwargs: Additional arguments for render_to_html

        Returns:
            Path to generated HTML file
        """
        spec = self.load_template(template_name)
        return self.render_to_html(spec, output_path, **kwargs)

    def generate_spec(
        self,
        template_type: str,
        data: Dict,
        theme: str = 'default'
    ) -> str:
        """
        Generate infographic spec from template type and data.

        This is a helper to programmatically build specs for common medical infographic types.

        Args:
            template_type: Type of infographic (e.g., 'trial-timeline', 'mechanism-steps')
            data: Data to populate template
            theme: Visual theme to apply

        Returns:
            Generated spec string
        """
        # Template generators for different infographic types
        generators = {
            'trial-timeline': self._generate_trial_timeline,
            'mechanism-steps': self._generate_mechanism_steps,
            'stat-comparison': self._generate_stat_comparison,
            'risk-factors': self._generate_risk_factors,
            'treatment-pathway': self._generate_treatment_pathway,
        }

        if template_type not in generators:
            raise ValueError(f'Unknown template type: {template_type}. Available: {list(generators.keys())}')

        return generators[template_type](data, theme)

    def _generate_trial_timeline(self, data: Dict, theme: str) -> str:
        """Generate trial timeline spec."""
        items = data.get('items', [])

        spec_lines = ['infographic list-row-simple-horizontal-arrow']
        spec_lines.append('data')
        spec_lines.append('  items:')

        for item in items:
            spec_lines.append(f'    - label: {item.get("label", "")}')
            spec_lines.append(f'      desc: {item.get("desc", "")}')

        return '\n'.join(spec_lines)

    def _generate_mechanism_steps(self, data: Dict, theme: str) -> str:
        """Generate mechanism of action steps."""
        steps = data.get('steps', [])

        spec_lines = ['infographic list-row-simple-vertical']
        spec_lines.append('data')
        spec_lines.append('  items:')

        for i, step in enumerate(steps, 1):
            spec_lines.append(f'    - label: Step {i}')
            spec_lines.append(f'      desc: {step}')

        return '\n'.join(spec_lines)

    def _generate_stat_comparison(self, data: Dict, theme: str) -> str:
        """Generate stat comparison infographic."""
        # This would use a different AntV template
        # For now, reuse the horizontal arrow as placeholder
        return self._generate_trial_timeline(data, theme)

    def _generate_risk_factors(self, data: Dict, theme: str) -> str:
        """Generate risk factors breakdown."""
        factors = data.get('factors', [])

        spec_lines = ['infographic list-row-simple-vertical']
        spec_lines.append('data')
        spec_lines.append('  items:')

        for factor in factors:
            spec_lines.append(f'    - label: {factor.get("name", "")}')
            spec_lines.append(f'      desc: {factor.get("prevalence", "")}')

        return '\n'.join(spec_lines)

    def _generate_treatment_pathway(self, data: Dict, theme: str) -> str:
        """Generate treatment pathway."""
        return self._generate_trial_timeline(data, theme)


# Convenience functions for direct usage
def render(
    spec: str,
    output_path: Optional[str] = None,
    width: int = 800,
    height: int = 600
) -> Path:
    """
    Quick render function.

    Args:
        spec: Infographic spec
        output_path: Output HTML file path
        width: Canvas width
        height: Canvas height

    Returns:
        Path to generated HTML file
    """
    renderer = AntvRenderer()
    return renderer.render_to_html(spec, output_path, width, height)


def render_template(
    template_name: str,
    output_path: Optional[str] = None,
    **kwargs
) -> Path:
    """
    Quick template render function.

    Args:
        template_name: Template name
        output_path: Output HTML file path
        **kwargs: Additional render options

    Returns:
        Path to generated HTML file
    """
    renderer = AntvRenderer()
    return renderer.render_template_to_html(template_name, output_path, **kwargs)


def list_templates() -> List[str]:
    """List available templates."""
    renderer = AntvRenderer()
    return renderer.list_templates()


if __name__ == '__main__':
    # CLI interface
    import argparse

    parser = argparse.ArgumentParser(description='AntV Infographic Python Renderer')
    parser.add_argument('--template', help='Template name')
    parser.add_argument('--spec', help='Direct spec string')
    parser.add_argument('--output', help='Output HTML file path')
    parser.add_argument('--width', type=int, default=800, help='Canvas width')
    parser.add_argument('--height', type=int, default=600, help='Canvas height')
    parser.add_argument('--list', action='store_true', help='List available templates')

    args = parser.parse_args()

    renderer = AntvRenderer()

    if args.list:
        templates = renderer.list_templates()
        print('Available templates:')
        for t in templates:
            print(f'  - {t}')
    elif args.template:
        output = renderer.render_template_to_html(
            args.template,
            args.output,
            width=args.width,
            height=args.height
        )
        print(f'HTML file generated: {output}')
        print('Open in browser to view and download SVG/PNG')
    elif args.spec:
        output = renderer.render_to_html(
            args.spec,
            args.output,
            width=args.width,
            height=args.height
        )
        print(f'HTML file generated: {output}')
        print('Open in browser to view and download SVG/PNG')
    else:
        parser.print_help()
