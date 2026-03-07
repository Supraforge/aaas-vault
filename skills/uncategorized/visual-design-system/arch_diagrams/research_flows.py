"""
Research Flows - Study Methodology Diagrams

Creates visual representations of research methodology flows
using mingrammer/diagrams library. Designed for:
- CONSORT diagrams (clinical trial enrollment)
- PRISMA diagrams (systematic review flow)
- General study methodology flows
- Data pipeline visualizations

Uses design tokens for consistent publication-quality styling.
"""

import os
import sys
from typing import Optional, List, Dict, Any

# Add parent directory for token access
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from diagrams import Diagram, Cluster, Edge
from diagrams.generic.blank import Blank
from diagrams.custom import Custom

# Color palette (consistent with design tokens)
COLORS = {
    "primary.navy": "#1e3a5f",
    "primary.blue": "#2d6a9f",
    "primary.teal": "#2d7a77",
    "semantic.success": "#2e7d32",
    "semantic.warning": "#e65100",
    "semantic.danger": "#c62828",
    "text.primary": "#212529",
    "backgrounds.light_gray": "#f8f9fa",
    "backgrounds.white": "#ffffff",
}


def get_color(path: str) -> str:
    """Get color from the local palette."""
    return COLORS.get(path, "#666666")


# Default output directory
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")


def _get_graph_attrs() -> Dict[str, str]:
    """Get publication-quality graph attributes."""
    return {
        "fontname": "Helvetica",
        "fontsize": "10",
        "bgcolor": get_color("backgrounds.light_gray"),
        "pad": "0.5",
        "splines": "ortho",
        "nodesep": "0.5",
        "ranksep": "0.6",
    }


def _get_node_attrs() -> Dict[str, str]:
    """Get publication-quality node attributes."""
    return {
        "fontname": "Helvetica",
        "fontsize": "9",
        "style": "filled",
        "fillcolor": "white",
        "color": get_color("primary.navy"),
        "penwidth": "1.5",
    }


def _get_edge_attrs() -> Dict[str, str]:
    """Get publication-quality edge attributes."""
    return {
        "fontname": "Helvetica",
        "fontsize": "8",
        "color": get_color("text.primary"),
        "penwidth": "1.2",
    }


def create_study_flow(
    title: str,
    stages: List[Dict[str, Any]],
    output_path: Optional[str] = None,
    format: str = "png",
    show: bool = False,
) -> str:
    """
    Create a generic study flow diagram.

    Args:
        title: Diagram title
        stages: List of stage dictionaries with keys:
            - name: Stage name
            - n: Number of subjects/items (optional)
            - type: 'enrollment', 'allocation', 'followup', 'analysis'
            - exclusions: List of exclusion reasons with counts (optional)
        output_path: Output file path (without extension)
        format: Output format ('png', 'svg', 'pdf')
        show: Whether to open the diagram after creation

    Returns:
        Path to the generated diagram
    """
    if output_path is None:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        output_path = os.path.join(OUTPUT_DIR, f"study_flow_{title.lower().replace(' ', '_')}")

    # Remove extension if provided
    if output_path.endswith(('.png', '.svg', '.pdf')):
        output_path = output_path.rsplit('.', 1)[0]

    # Stage type colors
    type_colors = {
        "enrollment": get_color("primary.blue"),
        "allocation": get_color("semantic.warning"),
        "followup": get_color("primary.teal"),
        "analysis": get_color("semantic.success"),
        "exclusion": get_color("semantic.danger"),
        "default": get_color("primary.navy"),
    }

    with Diagram(
        title,
        filename=output_path,
        outformat=format,
        show=show,
        graph_attr={
            **_get_graph_attrs(),
            "rankdir": "TB",
        },
        node_attr=_get_node_attrs(),
        edge_attr=_get_edge_attrs(),
        direction="TB",
    ):
        prev_node = None

        for stage in stages:
            name = stage.get("name", "Stage")
            n = stage.get("n")
            stage_type = stage.get("type", "default")
            color = type_colors.get(stage_type, type_colors["default"])

            # Create label with count
            label = name if n is None else f"{name}\n(n={n})"

            # Create main node
            node = Blank(label)
            node._attrs["color"] = color
            node._attrs["fillcolor"] = "white"
            node._attrs["penwidth"] = "2"

            if prev_node:
                prev_node >> node

            # Handle exclusions
            exclusions = stage.get("exclusions", [])
            for excl in exclusions:
                excl_label = f"{excl.get('reason', 'Excluded')}\n(n={excl.get('n', '?')})"
                excl_node = Blank(excl_label)
                excl_node._attrs["color"] = type_colors["exclusion"]
                excl_node._attrs["fillcolor"] = "#ffebee"
                excl_node._attrs["penwidth"] = "1.5"
                excl_node._attrs["style"] = "filled,dashed"

                node >> Edge(style="dashed") >> excl_node

            prev_node = node

    return f"{output_path}.{format}"


def create_consort_diagram(
    enrolled: int = 500,
    randomized: int = 400,
    treatment_n: int = 200,
    control_n: int = 200,
    treatment_completed: int = 180,
    control_completed: int = 175,
    treatment_analyzed: int = 200,
    control_analyzed: int = 200,
    output_path: Optional[str] = None,
    format: str = "png",
    show: bool = False,
) -> str:
    """
    Create a CONSORT diagram for clinical trial reporting.

    Based on CONSORT 2010 guidelines for RCT reporting.

    Args:
        enrolled: Number of participants assessed for eligibility
        randomized: Number randomized
        treatment_n: Number allocated to treatment
        control_n: Number allocated to control
        treatment_completed: Number completing treatment arm
        control_completed: Number completing control arm
        treatment_analyzed: Number analyzed in treatment arm
        control_analyzed: Number analyzed in control arm
        output_path: Output file path
        format: Output format
        show: Whether to open after creation

    Returns:
        Path to the generated diagram
    """
    if output_path is None:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        output_path = os.path.join(OUTPUT_DIR, "consort_diagram")

    excluded = enrolled - randomized
    treatment_lost = treatment_n - treatment_completed
    control_lost = control_n - control_completed

    with Diagram(
        "CONSORT Flow Diagram",
        filename=output_path,
        outformat=format,
        show=show,
        graph_attr={
            **_get_graph_attrs(),
            "rankdir": "TB",
        },
        node_attr=_get_node_attrs(),
        edge_attr=_get_edge_attrs(),
        direction="TB",
    ):
        # Enrollment
        with Cluster("Enrollment"):
            assessed = Blank(f"Assessed for eligibility\n(n={enrolled})")
            assessed._attrs["color"] = get_color("primary.blue")
            assessed._attrs["fillcolor"] = "#e3f2fd"
            assessed._attrs["penwidth"] = "2"

            excluded_node = Blank(f"Excluded (n={excluded})\n- Not meeting criteria\n- Declined to participate\n- Other reasons")
            excluded_node._attrs["color"] = get_color("semantic.danger")
            excluded_node._attrs["fillcolor"] = "#ffebee"
            excluded_node._attrs["penwidth"] = "1.5"
            excluded_node._attrs["style"] = "filled,dashed"

        # Allocation
        with Cluster("Allocation"):
            random = Blank(f"Randomized\n(n={randomized})")
            random._attrs["color"] = get_color("semantic.warning")
            random._attrs["fillcolor"] = "#fff3e0"
            random._attrs["penwidth"] = "2"

            treatment_alloc = Blank(f"Allocated to Treatment\n(n={treatment_n})")
            treatment_alloc._attrs["color"] = get_color("semantic.success")
            treatment_alloc._attrs["fillcolor"] = "#e8f5e9"
            treatment_alloc._attrs["penwidth"] = "2"

            control_alloc = Blank(f"Allocated to Control\n(n={control_n})")
            control_alloc._attrs["color"] = get_color("primary.teal")
            control_alloc._attrs["fillcolor"] = "#e0f2f1"
            control_alloc._attrs["penwidth"] = "2"

        # Follow-up
        with Cluster("Follow-up"):
            treatment_fu = Blank(f"Completed follow-up\n(n={treatment_completed})")
            treatment_fu._attrs["color"] = get_color("semantic.success")
            treatment_fu._attrs["fillcolor"] = "#e8f5e9"
            treatment_fu._attrs["penwidth"] = "2"

            treatment_lost_node = Blank(f"Lost to follow-up\n(n={treatment_lost})")
            treatment_lost_node._attrs["color"] = get_color("semantic.danger")
            treatment_lost_node._attrs["fillcolor"] = "#ffebee"
            treatment_lost_node._attrs["penwidth"] = "1.5"
            treatment_lost_node._attrs["style"] = "filled,dashed"

            control_fu = Blank(f"Completed follow-up\n(n={control_completed})")
            control_fu._attrs["color"] = get_color("primary.teal")
            control_fu._attrs["fillcolor"] = "#e0f2f1"
            control_fu._attrs["penwidth"] = "2"

            control_lost_node = Blank(f"Lost to follow-up\n(n={control_lost})")
            control_lost_node._attrs["color"] = get_color("semantic.danger")
            control_lost_node._attrs["fillcolor"] = "#ffebee"
            control_lost_node._attrs["penwidth"] = "1.5"
            control_lost_node._attrs["style"] = "filled,dashed"

        # Analysis
        with Cluster("Analysis"):
            treatment_analysis = Blank(f"Analyzed (ITT)\n(n={treatment_analyzed})")
            treatment_analysis._attrs["color"] = get_color("primary.navy")
            treatment_analysis._attrs["fillcolor"] = "#e8eaf6"
            treatment_analysis._attrs["penwidth"] = "2"

            control_analysis = Blank(f"Analyzed (ITT)\n(n={control_analyzed})")
            control_analysis._attrs["color"] = get_color("primary.navy")
            control_analysis._attrs["fillcolor"] = "#e8eaf6"
            control_analysis._attrs["penwidth"] = "2"

        # Connect nodes
        assessed >> Edge(style="dashed") >> excluded_node
        assessed >> random

        random >> treatment_alloc
        random >> control_alloc

        treatment_alloc >> treatment_fu
        treatment_alloc >> Edge(style="dashed") >> treatment_lost_node

        control_alloc >> control_fu
        control_alloc >> Edge(style="dashed") >> control_lost_node

        treatment_fu >> treatment_analysis
        control_fu >> control_analysis

    return f"{output_path}.{format}"


def create_prisma_diagram(
    records_identified: int = 1500,
    duplicates_removed: int = 200,
    records_screened: int = 1300,
    records_excluded: int = 800,
    full_text_assessed: int = 500,
    full_text_excluded: int = 350,
    studies_included: int = 150,
    output_path: Optional[str] = None,
    format: str = "png",
    show: bool = False,
) -> str:
    """
    Create a PRISMA diagram for systematic review reporting.

    Based on PRISMA 2020 guidelines.

    Args:
        records_identified: Records from database searching
        duplicates_removed: Duplicates removed
        records_screened: Records screened
        records_excluded: Records excluded based on title/abstract
        full_text_assessed: Full-text articles assessed
        full_text_excluded: Full-text articles excluded
        studies_included: Final studies included
        output_path: Output file path
        format: Output format
        show: Whether to open after creation

    Returns:
        Path to the generated diagram
    """
    if output_path is None:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        output_path = os.path.join(OUTPUT_DIR, "prisma_diagram")

    with Diagram(
        "PRISMA Flow Diagram",
        filename=output_path,
        outformat=format,
        show=show,
        graph_attr={
            **_get_graph_attrs(),
            "rankdir": "TB",
        },
        node_attr=_get_node_attrs(),
        edge_attr=_get_edge_attrs(),
        direction="TB",
    ):
        # Identification
        with Cluster("Identification"):
            identified = Blank(f"Records identified\n(n={records_identified})")
            identified._attrs["color"] = get_color("primary.blue")
            identified._attrs["fillcolor"] = "#e3f2fd"
            identified._attrs["penwidth"] = "2"

            duplicates = Blank(f"Duplicates removed\n(n={duplicates_removed})")
            duplicates._attrs["color"] = get_color("semantic.warning")
            duplicates._attrs["fillcolor"] = "#fff3e0"
            duplicates._attrs["penwidth"] = "1.5"
            duplicates._attrs["style"] = "filled,dashed"

        # Screening
        with Cluster("Screening"):
            screened = Blank(f"Records screened\n(n={records_screened})")
            screened._attrs["color"] = get_color("primary.teal")
            screened._attrs["fillcolor"] = "#e0f2f1"
            screened._attrs["penwidth"] = "2"

            excluded_screening = Blank(f"Records excluded\n(n={records_excluded})")
            excluded_screening._attrs["color"] = get_color("semantic.danger")
            excluded_screening._attrs["fillcolor"] = "#ffebee"
            excluded_screening._attrs["penwidth"] = "1.5"
            excluded_screening._attrs["style"] = "filled,dashed"

        # Eligibility
        with Cluster("Eligibility"):
            full_text = Blank(f"Full-text assessed\n(n={full_text_assessed})")
            full_text._attrs["color"] = get_color("semantic.warning")
            full_text._attrs["fillcolor"] = "#fff3e0"
            full_text._attrs["penwidth"] = "2"

            excluded_ft = Blank(f"Full-text excluded\n(n={full_text_excluded})\n- Wrong population\n- Wrong intervention\n- Wrong outcome")
            excluded_ft._attrs["color"] = get_color("semantic.danger")
            excluded_ft._attrs["fillcolor"] = "#ffebee"
            excluded_ft._attrs["penwidth"] = "1.5"
            excluded_ft._attrs["style"] = "filled,dashed"

        # Included
        with Cluster("Included"):
            included = Blank(f"Studies included\n(n={studies_included})")
            included._attrs["color"] = get_color("semantic.success")
            included._attrs["fillcolor"] = "#e8f5e9"
            included._attrs["penwidth"] = "2"

        # Connect nodes
        identified >> Edge(style="dashed") >> duplicates
        identified >> screened

        screened >> Edge(style="dashed") >> excluded_screening
        screened >> full_text

        full_text >> Edge(style="dashed") >> excluded_ft
        full_text >> included

    return f"{output_path}.{format}"


def create_methodology_flow(
    title: str = "Study Methodology",
    phases: Optional[List[Dict[str, Any]]] = None,
    output_path: Optional[str] = None,
    format: str = "png",
    show: bool = False,
) -> str:
    """
    Create a general research methodology flow diagram.

    Args:
        title: Diagram title
        phases: List of phase dictionaries with:
            - name: Phase name
            - steps: List of step names
            - color: Optional custom color
        output_path: Output file path
        format: Output format
        show: Whether to open after creation

    Returns:
        Path to the generated diagram
    """
    if output_path is None:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        output_path = os.path.join(OUTPUT_DIR, "methodology_flow")

    # Default phases if none provided
    if phases is None:
        phases = [
            {
                "name": "Phase 1: Study Design",
                "steps": ["Literature Review", "Hypothesis Formation", "Protocol Development"],
            },
            {
                "name": "Phase 2: Data Collection",
                "steps": ["Participant Recruitment", "Baseline Assessment", "Follow-up Visits"],
            },
            {
                "name": "Phase 3: Analysis",
                "steps": ["Data Cleaning", "Statistical Analysis", "Sensitivity Analysis"],
            },
            {
                "name": "Phase 4: Reporting",
                "steps": ["Manuscript Preparation", "Peer Review", "Publication"],
            },
        ]

    with Diagram(
        title,
        filename=output_path,
        outformat=format,
        show=show,
        graph_attr={
            **_get_graph_attrs(),
            "rankdir": "LR",
        },
        node_attr=_get_node_attrs(),
        edge_attr=_get_edge_attrs(),
        direction="LR",
    ):
        phase_colors = [
            get_color("primary.blue"),
            get_color("primary.teal"),
            get_color("semantic.success"),
            get_color("primary.navy"),
        ]
        phase_fills = ["#e3f2fd", "#e0f2f1", "#e8f5e9", "#e8eaf6"]

        prev_cluster_last = None

        for i, phase in enumerate(phases):
            color = phase.get("color", phase_colors[i % len(phase_colors)])
            fill = phase_fills[i % len(phase_fills)]

            with Cluster(phase["name"]):
                steps = phase.get("steps", [])
                cluster_first = None
                prev_step = None

                for step in steps:
                    node = Blank(step)
                    node._attrs["color"] = color
                    node._attrs["fillcolor"] = fill
                    node._attrs["penwidth"] = "2"

                    if cluster_first is None:
                        cluster_first = node

                    if prev_step:
                        prev_step >> node

                    prev_step = node

                # Connect to previous phase
                if prev_cluster_last and cluster_first:
                    prev_cluster_last >> Edge(penwidth="2") >> cluster_first

                prev_cluster_last = prev_step

    return f"{output_path}.{format}"


def demo():
    """Generate demo diagrams to test the module."""
    print("Generating research flow diagrams...")

    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Generate all research flow diagrams
    diagrams_to_create = [
        ("CONSORT Diagram", lambda: create_consort_diagram()),
        ("PRISMA Diagram", lambda: create_prisma_diagram()),
        ("Methodology Flow", lambda: create_methodology_flow()),
    ]

    for name, func in diagrams_to_create:
        try:
            output = func()
            print(f"  Created: {output}")
        except Exception as e:
            print(f"  Error creating {name}: {e}")

    print("\nDone!")


if __name__ == "__main__":
    demo()
