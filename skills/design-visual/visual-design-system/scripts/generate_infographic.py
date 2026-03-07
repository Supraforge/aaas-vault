#!/usr/bin/env python3
"""
Infographic Generator - Python Wrapper for Satori

Generates publication-grade infographics using the Satori Node.js pipeline.
Provides a Python interface for easy integration with the content system.

Usage:
    python generate_infographic.py stat-card --value "42%" --label "Risk Reduction" -o chart.png
    python generate_infographic.py comparison --data '{"left": {...}, "right": {...}}' -o comparison.png

    # From Python:
    from generate_infographic import generate
    generate("stat-card", {"value": "42%", "label": "Reduction"}, "output.png")
"""

import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, Optional, Union
import argparse


# Path to the Node.js renderer
SATORI_DIR = Path(__file__).parent.parent / "satori"
RENDERER_PATH = SATORI_DIR / "renderer.js"
OUTPUTS_DIR = Path(__file__).parent.parent / "outputs"


def check_dependencies() -> bool:
    """Check if Node.js and npm dependencies are installed."""
    # Check Node.js
    try:
        result = subprocess.run(
            ["node", "--version"],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print("Error: Node.js is not installed")
            return False
    except FileNotFoundError:
        print("Error: Node.js is not installed")
        return False

    # Check if node_modules exists
    node_modules = SATORI_DIR / "node_modules"
    if not node_modules.exists():
        print("Installing Satori dependencies...")
        result = subprocess.run(
            ["npm", "install"],
            cwd=SATORI_DIR,
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(f"Error installing dependencies: {result.stderr}")
            return False

    return True


def generate(
    template: str,
    data: Dict[str, Any],
    output: Union[str, Path],
    width: int = 1200,
    height: int = 630,
    save_svg: bool = False
) -> Dict[str, Any]:
    """
    Generate an infographic using a template.

    Args:
        template: Template name (stat-card, comparison, process-flow, trial-summary, key-finding)
        data: Template data dictionary
        output: Output file path (.png)
        width: Image width in pixels
        height: Image height in pixels
        save_svg: Also save SVG version

    Returns:
        Dict with success status and output path

    Example:
        >>> generate("stat-card", {"value": "42%", "label": "Risk Reduction"}, "chart.png")
        {'success': True, 'output': 'chart.png', 'size': 12345}
    """
    if not check_dependencies():
        return {"success": False, "error": "Dependencies not installed"}

    output = Path(output)

    # Ensure output directory exists
    output.parent.mkdir(parents=True, exist_ok=True)

    # Prepare input for Node.js
    input_data = {
        "template": template,
        "data": data,
        "output": str(output.absolute()),
        "width": width,
        "height": height,
    }

    # Run Node.js renderer
    try:
        result = subprocess.run(
            ["node", str(RENDERER_PATH), "--stdin"],
            input=json.dumps(input_data),
            capture_output=True,
            text=True,
            cwd=SATORI_DIR
        )

        if result.returncode != 0:
            return {
                "success": False,
                "error": result.stderr or "Unknown error",
                "stdout": result.stdout
            }

        return json.loads(result.stdout)

    except Exception as e:
        return {"success": False, "error": str(e)}


def generate_stat_card(
    value: str,
    label: str,
    sublabel: Optional[str] = None,
    source: Optional[str] = None,
    output: str = "stat-card.png",
    **kwargs
) -> Dict[str, Any]:
    """
    Generate a stat card infographic.

    Args:
        value: The main statistic (e.g., "42%", "0.74", "21")
        label: Description of the value (e.g., "Risk Reduction")
        sublabel: Additional context (e.g., "HR 0.58, 95% CI 0.45-0.75")
        source: Data source (e.g., "DAPA-HF Trial")
        output: Output file path

    Example:
        >>> generate_stat_card("26%", "Mortality Reduction", source="PARADIGM-HF")
    """
    data = {
        "value": value,
        "label": label,
        "sublabel": sublabel,
        "source": source,
    }
    return generate("stat-card", data, output, **kwargs)


def generate_comparison(
    title: str,
    left_value: str,
    left_label: str,
    right_value: str,
    right_label: str,
    metric: Optional[str] = None,
    source: Optional[str] = None,
    output: str = "comparison.png",
    **kwargs
) -> Dict[str, Any]:
    """
    Generate a comparison infographic.

    Args:
        title: Comparison title
        left_value: Left side value
        left_label: Left side label (e.g., "Treatment")
        right_value: Right side value
        right_label: Right side label (e.g., "Control")
        metric: What's being measured (e.g., "Event Rate")
        source: Data source
        output: Output file path

    Example:
        >>> generate_comparison(
        ...     "Treatment vs Control",
        ...     "12%", "Dapagliflozin",
        ...     "18%", "Placebo",
        ...     metric="CV Death or HF Hospitalization",
        ...     source="DAPA-HF"
        ... )
    """
    data = {
        "title": title,
        "left": {"value": left_value, "label": left_label, "color": "treatment"},
        "right": {"value": right_value, "label": right_label, "color": "control"},
        "metric": metric,
        "source": source,
    }
    return generate("comparison", data, output, **kwargs)


def generate_process_flow(
    title: str,
    steps: list,
    output: str = "process-flow.png",
    **kwargs
) -> Dict[str, Any]:
    """
    Generate a process flow diagram.

    Args:
        title: Flow diagram title
        steps: List of step dicts with 'title' and optional 'description'
        output: Output file path

    Example:
        >>> generate_process_flow(
        ...     "HFrEF Treatment Algorithm",
        ...     [
        ...         {"title": "Diagnose", "description": "Confirm HFrEF"},
        ...         {"title": "Initiate", "description": "Start foundational therapy"},
        ...         {"title": "Optimize", "description": "Titrate to target doses"},
        ...     ]
        ... )
    """
    # Add numbers to steps if not present
    for i, step in enumerate(steps):
        if "number" not in step:
            step["number"] = i + 1

    data = {"title": title, "steps": steps}
    return generate("process-flow", data, output, **kwargs)


def generate_trial_summary(
    trial_name: str,
    population: str,
    intervention: str,
    primary_endpoint: str,
    hr: float,
    ci: str,
    p_value: str,
    nnt: Optional[int] = None,
    output: str = "trial-summary.png",
    **kwargs
) -> Dict[str, Any]:
    """
    Generate a clinical trial summary card.

    Args:
        trial_name: Name of the trial (e.g., "DAPA-HF")
        population: Study population (e.g., "HFrEF patients")
        intervention: Treatment (e.g., "Dapagliflozin 10mg")
        primary_endpoint: Primary outcome (e.g., "CV death or HF hospitalization")
        hr: Hazard ratio
        ci: Confidence interval (e.g., "0.65-0.85")
        p_value: P-value (e.g., "<0.001")
        nnt: Number needed to treat (optional)
        output: Output file path

    Example:
        >>> generate_trial_summary(
        ...     "DAPA-HF",
        ...     "HFrEF patients",
        ...     "Dapagliflozin 10mg",
        ...     "CV death or HF hospitalization",
        ...     0.74, "0.65-0.85", "<0.001",
        ...     nnt=21
        ... )
    """
    data = {
        "trialName": trial_name,
        "population": population,
        "intervention": intervention,
        "primaryEndpoint": primary_endpoint,
        "result": {"hr": hr, "ci": ci, "pValue": p_value},
        "nnt": nnt,
    }
    return generate("trial-summary", data, output, **kwargs)


def generate_key_finding(
    finding: str,
    icon: str = "star",
    context: Optional[str] = None,
    evidence: Optional[str] = None,
    output: str = "key-finding.png",
    **kwargs
) -> Dict[str, Any]:
    """
    Generate a key finding highlight card.

    Args:
        finding: The main finding text
        icon: Icon type (heart, arrow-down, arrow-up, warning, check, star)
        context: Additional context
        evidence: Evidence level (e.g., "Class I, Level A")
        output: Output file path

    Example:
        >>> generate_key_finding(
        ...     "SGLT2 inhibitors reduce HF hospitalization by 30%",
        ...     icon="arrow-down",
        ...     context="Meta-analysis of 5 major trials",
        ...     evidence="Class I, Level A"
        ... )
    """
    data = {
        "finding": finding,
        "icon": icon,
        "context": context,
        "evidence": evidence,
    }
    return generate("key-finding", data, output, **kwargs)


def list_templates() -> list:
    """List available templates."""
    return [
        # World-class infographic templates (carousel visual language)
        "infographic-hero",       # Single key stat with maximum impact
        "infographic-dense",      # Multi-section information layout
        "infographic-comparison", # Two-column comparison
        "infographic-myth",       # Myth vs Truth split design
        "infographic-process",    # Workflow/steps with visual flow
        "infographic-checklist",  # Patient guide with styled checklist
        # Legacy templates
        "stat-card",
        "comparison",
        "process-flow",
        "trial-summary",
        "key-finding",
    ]


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Generate publication-grade infographics"
    )

    subparsers = parser.add_subparsers(dest="template", help="Template type")

    # stat-card
    stat_parser = subparsers.add_parser("stat-card", help="Big number with context")
    stat_parser.add_argument("--value", required=True, help="Main statistic")
    stat_parser.add_argument("--label", required=True, help="Description")
    stat_parser.add_argument("--sublabel", help="Additional context")
    stat_parser.add_argument("--source", help="Data source")
    stat_parser.add_argument("-o", "--output", default="stat-card.png")

    # comparison
    comp_parser = subparsers.add_parser("comparison", help="Side-by-side comparison")
    comp_parser.add_argument("--title", required=True)
    comp_parser.add_argument("--left-value", required=True)
    comp_parser.add_argument("--left-label", required=True)
    comp_parser.add_argument("--right-value", required=True)
    comp_parser.add_argument("--right-label", required=True)
    comp_parser.add_argument("--metric")
    comp_parser.add_argument("--source")
    comp_parser.add_argument("-o", "--output", default="comparison.png")

    # trial-summary
    trial_parser = subparsers.add_parser("trial-summary", help="Clinical trial results")
    trial_parser.add_argument("--name", required=True, help="Trial name")
    trial_parser.add_argument("--population", required=True)
    trial_parser.add_argument("--intervention", required=True)
    trial_parser.add_argument("--endpoint", required=True)
    trial_parser.add_argument("--hr", type=float, required=True)
    trial_parser.add_argument("--ci", required=True)
    trial_parser.add_argument("--pvalue", required=True)
    trial_parser.add_argument("--nnt", type=int)
    trial_parser.add_argument("-o", "--output", default="trial-summary.png")

    # key-finding
    finding_parser = subparsers.add_parser("key-finding", help="Highlighted finding")
    finding_parser.add_argument("--finding", required=True)
    finding_parser.add_argument("--icon", default="star",
                                choices=["heart", "arrow-down", "arrow-up", "warning", "check", "star"])
    finding_parser.add_argument("--context")
    finding_parser.add_argument("--evidence")
    finding_parser.add_argument("-o", "--output", default="key-finding.png")

    # Generic with JSON data
    json_parser = subparsers.add_parser("json", help="Generate from JSON data")
    json_parser.add_argument("--template", required=True)
    json_parser.add_argument("--data", required=True, help="JSON data string")
    json_parser.add_argument("-o", "--output", default="output.png")

    # List templates
    subparsers.add_parser("list", help="List available templates")

    # Common options
    for p in [stat_parser, comp_parser, trial_parser, finding_parser, json_parser]:
        p.add_argument("--width", type=int, default=1200)
        p.add_argument("--height", type=int, default=630)

    args = parser.parse_args()

    if args.template == "list" or args.template is None:
        print("Available templates:")
        for t in list_templates():
            print(f"  - {t}")
        return

    # Dispatch to appropriate function
    if args.template == "stat-card":
        result = generate_stat_card(
            args.value, args.label,
            sublabel=args.sublabel, source=args.source,
            output=args.output, width=args.width, height=args.height
        )
    elif args.template == "comparison":
        result = generate_comparison(
            args.title,
            args.left_value, args.left_label,
            args.right_value, args.right_label,
            metric=args.metric, source=args.source,
            output=args.output, width=args.width, height=args.height
        )
    elif args.template == "trial-summary":
        result = generate_trial_summary(
            args.name, args.population, args.intervention, args.endpoint,
            args.hr, args.ci, args.pvalue,
            nnt=args.nnt,
            output=args.output, width=args.width, height=args.height
        )
    elif args.template == "key-finding":
        result = generate_key_finding(
            args.finding,
            icon=args.icon, context=args.context, evidence=args.evidence,
            output=args.output, width=args.width, height=args.height
        )
    elif args.template == "json":
        data = json.loads(args.data)
        result = generate(
            args.template, data, args.output,
            width=args.width, height=args.height
        )
    else:
        print(f"Unknown template: {args.template}")
        sys.exit(1)

    if result.get("success"):
        print(f"Generated: {result.get('output')}")
        print(f"Size: {result.get('size', 0):,} bytes")
    else:
        print(f"Error: {result.get('error')}")
        sys.exit(1)


if __name__ == "__main__":
    main()
