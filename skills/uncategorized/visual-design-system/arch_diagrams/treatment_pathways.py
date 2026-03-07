"""
Treatment Pathways - Clinical Algorithm Diagrams

Creates visual representations of clinical treatment pathways
using mingrammer/diagrams library. Designed for:
- Heart Failure management
- Acute Coronary Syndrome pathways
- Atrial Fibrillation algorithms
- Custom treatment flows

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
# Using direct values to avoid import issues with the diagrams package
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


def create_treatment_pathway(
    title: str,
    steps: List[Dict[str, Any]],
    output_path: Optional[str] = None,
    format: str = "png",
    show: bool = False,
) -> str:
    """
    Create a generic treatment pathway diagram.

    Args:
        title: Diagram title
        steps: List of step dictionaries with keys:
            - name: Step name
            - type: 'assessment', 'decision', 'treatment', 'outcome'
            - children: Optional list of child steps
            - color: Optional custom color
        output_path: Output file path (without extension)
        format: Output format ('png', 'svg', 'pdf')
        show: Whether to open the diagram after creation

    Returns:
        Path to the generated diagram
    """
    if output_path is None:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        output_path = os.path.join(OUTPUT_DIR, f"pathway_{title.lower().replace(' ', '_')}")

    # Remove extension if provided
    if output_path.endswith(('.png', '.svg', '.pdf')):
        output_path = output_path.rsplit('.', 1)[0]

    # Node type colors
    type_colors = {
        "assessment": get_color("primary.blue"),
        "decision": get_color("semantic.warning"),
        "treatment": get_color("semantic.success"),
        "outcome": get_color("primary.teal"),
        "default": get_color("primary.navy"),
    }

    # Node type shapes
    type_shapes = {
        "assessment": "box",
        "decision": "diamond",
        "treatment": "box",
        "outcome": "ellipse",
        "default": "box",
    }

    with Diagram(
        title,
        filename=output_path,
        outformat=format,
        show=show,
        graph_attr=_get_graph_attrs(),
        node_attr=_get_node_attrs(),
        edge_attr=_get_edge_attrs(),
    ):
        nodes = {}

        def create_node(step_data, parent=None):
            """Recursively create nodes from step data."""
            name = step_data.get("name", "Unnamed")
            step_type = step_data.get("type", "default")
            color = step_data.get("color", type_colors.get(step_type, type_colors["default"]))
            shape = type_shapes.get(step_type, "box")

            # Create node using Blank with custom attributes
            # Note: diagrams library uses Graphviz under the hood
            node = Blank(name)
            node._attrs["shape"] = shape
            node._attrs["fillcolor"] = "white"
            node._attrs["color"] = color
            node._attrs["penwidth"] = "2"

            nodes[name] = node

            if parent:
                parent >> Edge(label=step_data.get("edge_label", "")) >> node

            # Process children
            children = step_data.get("children", [])
            for child in children:
                create_node(child, node)

            return node

        # Create root nodes
        prev_node = None
        for step in steps:
            node = create_node(step, prev_node)
            if step.get("type") != "decision":  # Decisions branch, don't chain
                prev_node = node

    return f"{output_path}.{format}"


def create_heart_failure_pathway(
    output_path: Optional[str] = None,
    format: str = "png",
    show: bool = False,
) -> str:
    """
    Create a heart failure treatment pathway (2024 guidelines).

    Based on ACC/AHA/HFSA Heart Failure Guidelines.

    Args:
        output_path: Output file path
        format: Output format
        show: Whether to open after creation

    Returns:
        Path to the generated diagram
    """
    if output_path is None:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        output_path = os.path.join(OUTPUT_DIR, "heart_failure_pathway")

    with Diagram(
        "Heart Failure with Reduced EF (HFrEF) Treatment Algorithm",
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
        # Stage definitions using clusters
        with Cluster("Assessment"):
            diagnosis = Blank("Confirm HFrEF\n(EF <= 40%)")
            diagnosis._attrs["shape"] = "box"
            diagnosis._attrs["color"] = get_color("primary.blue")
            diagnosis._attrs["fillcolor"] = "#e3f2fd"
            diagnosis._attrs["penwidth"] = "2"

        with Cluster("Foundational Therapy (GDMT)"):
            acei = Blank("ACEi/ARNi")
            acei._attrs["color"] = get_color("semantic.success")
            acei._attrs["fillcolor"] = "#e8f5e9"
            acei._attrs["penwidth"] = "2"

            bb = Blank("Beta-blocker")
            bb._attrs["color"] = get_color("semantic.success")
            bb._attrs["fillcolor"] = "#e8f5e9"
            bb._attrs["penwidth"] = "2"

            mra = Blank("MRA")
            mra._attrs["color"] = get_color("semantic.success")
            mra._attrs["fillcolor"] = "#e8f5e9"
            mra._attrs["penwidth"] = "2"

            sglt2 = Blank("SGLT2i")
            sglt2._attrs["color"] = get_color("semantic.success")
            sglt2._attrs["fillcolor"] = "#e8f5e9"
            sglt2._attrs["penwidth"] = "2"

        with Cluster("Additional Therapy"):
            reassess = Blank("Reassess\nEF & Symptoms")
            reassess._attrs["shape"] = "diamond"
            reassess._attrs["color"] = get_color("semantic.warning")
            reassess._attrs["fillcolor"] = "#fff3e0"
            reassess._attrs["penwidth"] = "2"

            icd = Blank("ICD\nif EF <= 35%")
            icd._attrs["color"] = get_color("primary.teal")
            icd._attrs["fillcolor"] = "#e0f2f1"
            icd._attrs["penwidth"] = "2"

            crt = Blank("CRT\nif LBBB & QRS >= 150ms")
            crt._attrs["color"] = get_color("primary.teal")
            crt._attrs["fillcolor"] = "#e0f2f1"
            crt._attrs["penwidth"] = "2"

        with Cluster("Advanced Therapy"):
            advanced = Blank("Refer for\nAdvanced HF Therapy")
            advanced._attrs["color"] = get_color("semantic.danger")
            advanced._attrs["fillcolor"] = "#ffebee"
            advanced._attrs["penwidth"] = "2"

            lvad = Blank("LVAD")
            lvad._attrs["color"] = get_color("semantic.danger")
            lvad._attrs["fillcolor"] = "#ffebee"
            lvad._attrs["penwidth"] = "2"

            transplant = Blank("Heart\nTransplant")
            transplant._attrs["color"] = get_color("semantic.danger")
            transplant._attrs["fillcolor"] = "#ffebee"
            transplant._attrs["penwidth"] = "2"

        # Connect nodes
        diagnosis >> Edge(label="Start GDMT") >> acei
        acei >> bb
        bb >> mra
        mra >> sglt2

        sglt2 >> Edge(label="After 3-6 months") >> reassess

        reassess >> Edge(label="EF improved") >> icd
        reassess >> Edge(label="Persistent symptoms") >> advanced

        icd >> crt

        advanced >> lvad
        advanced >> transplant

    return f"{output_path}.{format}"


def create_acs_pathway(
    output_path: Optional[str] = None,
    format: str = "png",
    show: bool = False,
) -> str:
    """
    Create an Acute Coronary Syndrome (ACS) management pathway.

    Based on ACC/AHA STEMI and NSTE-ACS Guidelines.

    Args:
        output_path: Output file path
        format: Output format
        show: Whether to open after creation

    Returns:
        Path to the generated diagram
    """
    if output_path is None:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        output_path = os.path.join(OUTPUT_DIR, "acs_pathway")

    with Diagram(
        "Acute Coronary Syndrome Management Algorithm",
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
        # Initial assessment
        with Cluster("Initial Presentation"):
            chest_pain = Blank("Chest Pain/\nACS Suspected")
            chest_pain._attrs["shape"] = "box"
            chest_pain._attrs["color"] = get_color("semantic.danger")
            chest_pain._attrs["fillcolor"] = "#ffebee"
            chest_pain._attrs["penwidth"] = "2"

            ecg = Blank("12-Lead ECG\n(within 10 min)")
            ecg._attrs["color"] = get_color("primary.blue")
            ecg._attrs["fillcolor"] = "#e3f2fd"
            ecg._attrs["penwidth"] = "2"

        # ECG findings
        with Cluster("ECG Classification"):
            ste = Blank("ST Elevation")
            ste._attrs["shape"] = "diamond"
            ste._attrs["color"] = get_color("semantic.danger")
            ste._attrs["fillcolor"] = "#ffebee"
            ste._attrs["penwidth"] = "2"

            nste = Blank("No ST Elevation")
            nste._attrs["shape"] = "diamond"
            nste._attrs["color"] = get_color("semantic.warning")
            nste._attrs["fillcolor"] = "#fff3e0"
            nste._attrs["penwidth"] = "2"

        # STEMI pathway
        with Cluster("STEMI Management"):
            primary_pci = Blank("Primary PCI\n(within 90 min)")
            primary_pci._attrs["color"] = get_color("semantic.success")
            primary_pci._attrs["fillcolor"] = "#e8f5e9"
            primary_pci._attrs["penwidth"] = "2"

            fibrinolysis = Blank("Fibrinolysis\n(if PCI not available)")
            fibrinolysis._attrs["color"] = get_color("semantic.success")
            fibrinolysis._attrs["fillcolor"] = "#e8f5e9"
            fibrinolysis._attrs["penwidth"] = "2"

        # NSTEMI pathway
        with Cluster("NSTEMI/UA Management"):
            risk = Blank("Risk Stratification\n(GRACE/TIMI)")
            risk._attrs["color"] = get_color("primary.blue")
            risk._attrs["fillcolor"] = "#e3f2fd"
            risk._attrs["penwidth"] = "2"

            invasive_early = Blank("Early Invasive\n(<24h)")
            invasive_early._attrs["color"] = get_color("semantic.success")
            invasive_early._attrs["fillcolor"] = "#e8f5e9"
            invasive_early._attrs["penwidth"] = "2"

            invasive_delayed = Blank("Delayed Invasive\n(25-72h)")
            invasive_delayed._attrs["color"] = get_color("semantic.success")
            invasive_delayed._attrs["fillcolor"] = "#e8f5e9"
            invasive_delayed._attrs["penwidth"] = "2"

            conservative = Blank("Conservative\nManagement")
            conservative._attrs["color"] = get_color("primary.teal")
            conservative._attrs["fillcolor"] = "#e0f2f1"
            conservative._attrs["penwidth"] = "2"

        # Medical therapy
        with Cluster("Medical Therapy (All)"):
            dapt = Blank("DAPT\n(Aspirin + P2Y12)")
            dapt._attrs["color"] = get_color("primary.navy")
            dapt._attrs["fillcolor"] = "#e8eaf6"
            dapt._attrs["penwidth"] = "2"

            anticoag = Blank("Anticoagulation")
            anticoag._attrs["color"] = get_color("primary.navy")
            anticoag._attrs["fillcolor"] = "#e8eaf6"
            anticoag._attrs["penwidth"] = "2"

            statin = Blank("High-Intensity\nStatin")
            statin._attrs["color"] = get_color("primary.navy")
            statin._attrs["fillcolor"] = "#e8eaf6"
            statin._attrs["penwidth"] = "2"

        # Connect nodes
        chest_pain >> ecg
        ecg >> ste
        ecg >> nste

        ste >> Edge(label="PCI capable") >> primary_pci
        ste >> Edge(label="No PCI") >> fibrinolysis

        nste >> risk
        risk >> Edge(label="High risk") >> invasive_early
        risk >> Edge(label="Intermediate") >> invasive_delayed
        risk >> Edge(label="Low risk") >> conservative

        # Medical therapy connections
        primary_pci >> dapt
        fibrinolysis >> dapt
        invasive_early >> dapt
        invasive_delayed >> dapt
        conservative >> dapt

        dapt >> anticoag
        anticoag >> statin

    return f"{output_path}.{format}"


def create_af_pathway(
    output_path: Optional[str] = None,
    format: str = "png",
    show: bool = False,
) -> str:
    """
    Create an Atrial Fibrillation management pathway.

    Based on 2023 ACC/AHA/ACCP/HRS AF Guidelines.

    Args:
        output_path: Output file path
        format: Output format
        show: Whether to open after creation

    Returns:
        Path to the generated diagram
    """
    if output_path is None:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        output_path = os.path.join(OUTPUT_DIR, "af_pathway")

    with Diagram(
        "Atrial Fibrillation Management Algorithm",
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
        # Initial assessment
        with Cluster("Diagnosis & Assessment"):
            af_dx = Blank("AF Diagnosed")
            af_dx._attrs["color"] = get_color("primary.blue")
            af_dx._attrs["fillcolor"] = "#e3f2fd"
            af_dx._attrs["penwidth"] = "2"

            chads = Blank("CHA2DS2-VASc\nScore")
            chads._attrs["shape"] = "diamond"
            chads._attrs["color"] = get_color("semantic.warning")
            chads._attrs["fillcolor"] = "#fff3e0"
            chads._attrs["penwidth"] = "2"

        # Anticoagulation
        with Cluster("Stroke Prevention"):
            doac = Blank("DOAC\n(Preferred)")
            doac._attrs["color"] = get_color("semantic.success")
            doac._attrs["fillcolor"] = "#e8f5e9"
            doac._attrs["penwidth"] = "2"

            warfarin = Blank("Warfarin\n(Mechanical valve)")
            warfarin._attrs["color"] = get_color("primary.teal")
            warfarin._attrs["fillcolor"] = "#e0f2f1"
            warfarin._attrs["penwidth"] = "2"

            laao = Blank("LAAO\n(If AC contraindicated)")
            laao._attrs["color"] = get_color("primary.teal")
            laao._attrs["fillcolor"] = "#e0f2f1"
            laao._attrs["penwidth"] = "2"

        # Rate vs Rhythm
        with Cluster("Rate vs Rhythm Control"):
            rate_rhythm = Blank("Rate vs Rhythm\nDecision")
            rate_rhythm._attrs["shape"] = "diamond"
            rate_rhythm._attrs["color"] = get_color("semantic.warning")
            rate_rhythm._attrs["fillcolor"] = "#fff3e0"
            rate_rhythm._attrs["penwidth"] = "2"

        # Rate control
        with Cluster("Rate Control"):
            bb_rate = Blank("Beta-blocker/\nCCB")
            bb_rate._attrs["color"] = get_color("primary.navy")
            bb_rate._attrs["fillcolor"] = "#e8eaf6"
            bb_rate._attrs["penwidth"] = "2"

            digoxin = Blank("Digoxin\n(If needed)")
            digoxin._attrs["color"] = get_color("primary.navy")
            digoxin._attrs["fillcolor"] = "#e8eaf6"
            digoxin._attrs["penwidth"] = "2"

            avj_ablation = Blank("AVJ Ablation\n+ Pacemaker")
            avj_ablation._attrs["color"] = get_color("semantic.danger")
            avj_ablation._attrs["fillcolor"] = "#ffebee"
            avj_ablation._attrs["penwidth"] = "2"

        # Rhythm control
        with Cluster("Rhythm Control"):
            aad = Blank("Antiarrhythmic\nDrug")
            aad._attrs["color"] = get_color("semantic.success")
            aad._attrs["fillcolor"] = "#e8f5e9"
            aad._attrs["penwidth"] = "2"

            cardioversion = Blank("Cardioversion")
            cardioversion._attrs["color"] = get_color("semantic.success")
            cardioversion._attrs["fillcolor"] = "#e8f5e9"
            cardioversion._attrs["penwidth"] = "2"

            ablation = Blank("Catheter\nAblation")
            ablation._attrs["color"] = get_color("semantic.success")
            ablation._attrs["fillcolor"] = "#e8f5e9"
            ablation._attrs["penwidth"] = "2"

        # Connect nodes
        af_dx >> chads

        chads >> Edge(label="Score >= 2\n(Men >= 1 Women)") >> doac
        chads >> Edge(label="Mechanical valve") >> warfarin
        chads >> Edge(label="Bleeding risk high") >> laao

        af_dx >> rate_rhythm

        rate_rhythm >> Edge(label="Rate control") >> bb_rate
        bb_rate >> Edge(label="Inadequate") >> digoxin
        digoxin >> Edge(label="Refractory") >> avj_ablation

        rate_rhythm >> Edge(label="Rhythm control") >> aad
        aad >> cardioversion
        aad >> Edge(label="First-line option") >> ablation
        cardioversion >> Edge(label="Recurrence") >> ablation

    return f"{output_path}.{format}"


def demo():
    """Generate demo diagrams to test the module."""
    print("Generating treatment pathway diagrams...")

    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Generate all pathway diagrams
    diagrams = [
        ("Heart Failure Pathway", create_heart_failure_pathway),
        ("ACS Pathway", create_acs_pathway),
        ("AF Pathway", create_af_pathway),
    ]

    for name, func in diagrams:
        try:
            output = func()
            print(f"  Created: {output}")
        except Exception as e:
            print(f"  Error creating {name}: {e}")

    print("\nDone!")


if __name__ == "__main__":
    demo()
