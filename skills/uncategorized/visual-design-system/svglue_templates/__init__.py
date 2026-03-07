"""
SVG Infographic Templates - Template-Based SVG Generation

Renders publication-grade infographics by populating SVG templates with data.
Uses lxml for direct SVG manipulation (more flexible than svglue).
All templates follow Nature/JACC/NEJM design standards.

Available Templates:
- trial_results: Clinical trial summary with key endpoints
- drug_mechanism: Mechanism of action explainer
- patient_stats: Patient demographics dashboard
- before_after: Before/after comparison layout
- risk_factors: Risk factor breakdown visualization

Usage:
    from svglue_templates.template_renderer import render_template, get_demo_data

    # Render with demo data
    svg = render_template("trial_results", get_demo_data("trial_results"))

    # Render with custom data
    svg = render_template("trial_results", {"trial_name": "MY-TRIAL", ...})
"""

from pathlib import Path

TEMPLATE_DIR = Path(__file__).parent / "templates"

def get_template_path(template_name: str) -> Path:
    """Get the path to a template SVG file."""
    template_file = TEMPLATE_DIR / f"{template_name}.svg"
    if not template_file.exists():
        raise FileNotFoundError(f"Template '{template_name}' not found at {template_file}")
    return template_file

def list_templates() -> list:
    """List all available templates."""
    return [
        {"name": "trial_results", "description": "Clinical trial summary with key endpoints"},
        {"name": "drug_mechanism", "description": "Mechanism of action explainer"},
        {"name": "patient_stats", "description": "Patient demographics dashboard"},
        {"name": "before_after", "description": "Before/after comparison layout"},
        {"name": "risk_factors", "description": "Risk factor breakdown visualization"}
    ]
