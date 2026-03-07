#!/usr/bin/env python3
"""
SVG Template Renderer

Renders publication-grade infographics by populating SVG templates with data.
Uses lxml for direct SVG manipulation (more flexible than svglue).

Usage:
    python template_renderer.py trial_results --demo -o output.svg
    python template_renderer.py trial_results --data '{"trial_name": "DAPA-HF", ...}' -o output.svg
    python template_renderer.py --list
    python template_renderer.py --demo-all

Templates:
    - trial_results: Clinical trial summary with endpoints
    - drug_mechanism: Mechanism of action explainer
    - patient_stats: Patient demographics dashboard
    - before_after: Before/after comparison
    - risk_factors: Risk factor visualization
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Any, Optional

from lxml import etree

try:
    import cairosvg
    HAS_CAIROSVG = True
except ImportError:
    HAS_CAIROSVG = False
    print("Note: cairosvg not installed. PNG export disabled. Install with: pip install cairosvg")

# Template directory
TEMPLATE_DIR = Path(__file__).parent / "templates"
OUTPUT_DIR = Path(__file__).parent.parent / "outputs"

# SVG namespace
SVG_NS = "http://www.w3.org/2000/svg"
NAMESPACES = {"svg": SVG_NS}


def list_templates() -> list:
    """List all available templates."""
    return [
        {"name": "trial_results", "description": "Clinical trial summary with key endpoints"},
        {"name": "drug_mechanism", "description": "Mechanism of action explainer"},
        {"name": "patient_stats", "description": "Patient demographics dashboard"},
        {"name": "before_after", "description": "Before/after comparison layout"},
        {"name": "risk_factors", "description": "Risk factor breakdown visualization"}
    ]


def get_demo_data(template_name: str) -> Dict[str, Any]:
    """Get demo data for a template."""
    demos = {
        "trial_results": {
            "trial_name": "DAPA-HF Trial",
            "trial_subtitle": "Dapagliflozin in Heart Failure with Reduced Ejection Fraction",
            "primary_endpoint_name": "CV Death or HF Hospitalization",
            "primary_hr": "0.74",
            "primary_ci": "95% CI: 0.65-0.85",
            "primary_p": "P < 0.001",
            "secondary_endpoint_name": "All-Cause Mortality",
            "secondary_hr": "0.83",
            "secondary_ci": "95% CI: 0.71-0.97",
            "secondary_p": "P = 0.022",
            "stat1_value": "4,744",
            "stat1_label": "Patients enrolled",
            "stat2_value": "18.2",
            "stat2_label": "Months median follow-up",
            "stat3_value": "21",
            "stat3_label": "NNT over 18 months",
            "stat4_value": "4.9%",
            "stat4_label": "Absolute risk reduction",
            "treatment_label": "Dapagliflozin 10mg",
            "control_label": "Placebo",
            "source": "McMurray JJV et al. N Engl J Med. 2019;381:1995-2008",
            "author": "Prepared by: Dr. Shailesh Singh",
            "date": "January 2026"
        },
        "drug_mechanism": {
            "drug_name": "Dapagliflozin (SGLT2i)",
            "drug_class": "Sodium-Glucose Co-Transporter 2 Inhibitor",
            "step1_title": "Oral Administration",
            "step1_desc": "10mg once daily",
            "step2_title": "SGLT2 Inhibition",
            "step2_desc": "Proximal tubule",
            "step3_title": "Glucosuria",
            "step3_desc": "↓ Glucose reabsorption",
            "step4_title": "Cardioprotection",
            "step4_desc": "↓ HF hospitalization",
            "target_name": "SGLT2 Receptor",
            "target_mechanism": "Blocks sodium-glucose cotransporter 2 in kidney",
            "target_result": "Increased urinary glucose excretion (50-80g/day)",
            "target_binding": "IC50 = 1.1 nM (highly selective)",
            "effect1": "Reduced HF hospitalization (-30%)",
            "effect2": "Weight loss (2-4 kg)",
            "effect3": "Blood pressure reduction (-4 mmHg)",
            "effect4": "Risk: Genital infections (5-8%)",
            "bioavail_value": "78%",
            "bioavail_label": "Bioavailability",
            "halflife_value": "12.9h",
            "halflife_label": "Half-life",
            "onset_value": "2h",
            "onset_label": "Tmax",
            "dose_value": "10mg",
            "dose_label": "Standard dose",
            "source": "FDA Label / DAPA-HF Trial Data",
            "date": "January 2026"
        },
        "patient_stats": {
            "title": "DAPA-HF PATIENT DEMOGRAPHICS",
            "subtitle": "Baseline characteristics of 4,744 patients with HFrEF",
            "total_patients": "4,744",
            "treatment_n": "2,373",
            "control_n": "2,371",
            "sites_n": "410",
            "mean_age": "66.3 years",
            "male_pct": "77%",
            "female_pct": "23%",
            "mean_bmi": "28.2 kg/m²",
            "diabetes_pct": "42%",
            "htn_pct": "74%",
            "mi_pct": "37%",
            "ckd_pct": "41%",
            "acei_pct": "84%",
            "bb_pct": "96%",
            "statin_pct": "71%",
            "egfr_value": "66 mL/min/1.73m²",
            "bnp_value": "1,437 pg/mL",
            "lvef_value": "31%",
            "source": "McMurray JJV et al. N Engl J Med. 2019",
            "date": "January 2026"
        },
        "before_after": {
            "title": "SGLT2i TREATMENT EFFECTS",
            "subtitle": "Changes from baseline at 12 months",
            "before_label": "BASELINE",
            "after_label": "12 MONTHS",
            "metric1_label": "HF HOSPITALIZATION RATE",
            "metric1_before": "9.8%",
            "metric1_after": "5.6%",
            "metric1_change": "-4.2%",
            "metric2_label": "SYSTOLIC BP (mmHg)",
            "metric2_before": "122",
            "metric2_after": "119",
            "metric2_change": "-3",
            "metric3_label": "6-MIN WALK DISTANCE",
            "metric3_before": "295",
            "metric3_after": "340",
            "metric3_change": "+45",
            "stat1_value": "18 mo",
            "stat1_label": "Median follow-up",
            "stat2_value": "74%",
            "stat2_label": "Relative risk reduction",
            "stat3_value": "P < 0.001",
            "stat3_label": "Primary endpoint",
            "source": "DAPA-HF / DELIVER Trials",
            "date": "January 2026"
        },
        "risk_factors": {
            "title": "HEART FAILURE RISK PROFILE",
            "subtitle": "Risk stratification in 1,000 patients with ASCVD",
            "overall_risk_score": "HIGH",
            "overall_risk_value": "5-year HF risk: 18.5%",
            "high_pct": "35%",
            "moderate_pct": "40%",
            "low_pct": "25%",
            "rf1_name": "Hypertension (BP >140/90)",
            "rf1_pct": "72%",
            "rf2_name": "Elevated NT-proBNP",
            "rf2_pct": "58%",
            "rf3_name": "Current Smoking",
            "rf3_pct": "18%",
            "rf4_name": "Obesity (BMI >30)",
            "rf4_pct": "42%",
            "rf5_name": "Age >65 years",
            "rf5_pct": "55%",
            "rf6_name": "Male Sex",
            "rf6_pct": "62%",
            "rf7_name": "Prior MI",
            "rf7_pct": "38%",
            "rf8_name": "Diabetes Mellitus",
            "rf8_pct": "35%",
            "source": "ACC/AHA HF Risk Calculator / Registry Data",
            "date": "January 2026"
        }
    }
    return demos.get(template_name, {})


def render_template(template_name: str, data: Dict[str, Any]) -> str:
    """
    Render a template with the given data.

    Uses lxml to find elements by ID and replace their text content.

    Args:
        template_name: Name of the template (without .svg extension)
        data: Dictionary of placeholder IDs to values

    Returns:
        SVG string with placeholders replaced
    """
    template_path = TEMPLATE_DIR / f"{template_name}.svg"
    if not template_path.exists():
        raise FileNotFoundError(f"Template '{template_name}' not found at {template_path}")

    # Parse the SVG file
    parser = etree.XMLParser(remove_blank_text=False)
    tree = etree.parse(str(template_path), parser)
    root = tree.getroot()

    # Find and replace text elements by ID
    replaced_count = 0
    for element_id, value in data.items():
        # Try to find element with this ID
        elements = root.xpath(f'//*[@id="{element_id}"]')
        for elem in elements:
            elem.text = str(value)
            replaced_count += 1

    # Convert back to string
    svg_bytes = etree.tostring(root, encoding='unicode', pretty_print=True)
    return svg_bytes


def save_svg(svg_content: str, output_path: Path) -> None:
    """Save SVG content to file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"  SVG saved: {output_path}")


def save_png(svg_content: str, output_path: Path, scale: int = 2) -> None:
    """Convert SVG to PNG using cairosvg."""
    if not HAS_CAIROSVG:
        print("  PNG export skipped (cairosvg not installed)")
        return

    output_path.parent.mkdir(parents=True, exist_ok=True)
    png_path = output_path.with_suffix('.png')

    cairosvg.svg2png(
        bytestring=svg_content.encode('utf-8'),
        write_to=str(png_path),
        scale=scale  # 2x scale = 1600x1200 for 300 DPI at 5.3x4 inches
    )
    print(f"  PNG saved: {png_path} (scale={scale}x)")


def render_all_demos(output_dir: Optional[Path] = None) -> None:
    """Render all templates with demo data."""
    if output_dir is None:
        output_dir = OUTPUT_DIR

    output_dir.mkdir(parents=True, exist_ok=True)

    for template_info in list_templates():
        template_name = template_info["name"]
        demo_data = get_demo_data(template_name)

        try:
            svg_content = render_template(template_name, demo_data)
            svg_path = output_dir / f"demo_{template_name}.svg"
            save_svg(svg_content, svg_path)

            if HAS_CAIROSVG:
                save_png(svg_content, svg_path, scale=2)

            print(f"  {template_name}: SUCCESS")
        except Exception as e:
            print(f"  {template_name}: FAILED - {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Render publication-grade infographics from SVG templates",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # List available templates
  python template_renderer.py --list

  # Render demo for all templates
  python template_renderer.py --demo-all

  # Render specific template with demo data
  python template_renderer.py trial_results --demo -o output.svg

  # Render with custom data
  python template_renderer.py trial_results --data '{"trial_name": "MY-TRIAL", ...}' -o output.svg

  # Export as PNG (requires cairosvg)
  python template_renderer.py trial_results --demo --png --scale 3 -o output.svg
        """
    )

    parser.add_argument('template', nargs='?', help='Template name to render')
    parser.add_argument('--list', action='store_true', help='List available templates')
    parser.add_argument('--demo', action='store_true', help='Use demo data for the template')
    parser.add_argument('--demo-all', action='store_true', help='Render all templates with demo data')
    parser.add_argument('--data', type=str, help='JSON data for template (or @file.json)')
    parser.add_argument('-o', '--output', type=str, help='Output file path')
    parser.add_argument('--png', action='store_true', help='Also export as PNG')
    parser.add_argument('--scale', type=int, default=2, help='PNG scale factor (default: 2)')
    parser.add_argument('--output-dir', type=str, help='Output directory for --demo-all')

    args = parser.parse_args()

    # List templates
    if args.list:
        print("\nAvailable Templates:")
        print("-" * 60)
        for t in list_templates():
            print(f"  {t['name']:20} - {t['description']}")
        print()
        return

    # Render all demos
    if args.demo_all:
        print("\nRendering all templates with demo data...")
        print("-" * 60)
        output_dir = Path(args.output_dir) if args.output_dir else OUTPUT_DIR
        render_all_demos(output_dir)
        print("\nDone!")
        return

    # Need a template name for individual rendering
    if not args.template:
        parser.print_help()
        return

    # Get data
    if args.demo:
        data = get_demo_data(args.template)
    elif args.data:
        if args.data.startswith('@'):
            with open(args.data[1:], 'r') as f:
                data = json.load(f)
        else:
            data = json.loads(args.data)
    else:
        print("Error: Must specify --demo or --data")
        return

    # Render template
    try:
        svg_content = render_template(args.template, data)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    # Output
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = OUTPUT_DIR / f"{args.template}.svg"

    save_svg(svg_content, output_path)

    if args.png:
        save_png(svg_content, output_path, scale=args.scale)

    print("\nDone!")


if __name__ == "__main__":
    main()
