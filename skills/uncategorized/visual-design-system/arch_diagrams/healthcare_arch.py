"""
Healthcare Architecture - System and Department Diagrams

Creates visual representations of healthcare systems and data flows
using mingrammer/diagrams library. Designed for:
- Healthcare system architecture
- Cardiology department organization
- Data pipeline visualizations
- Hospital workflow diagrams

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


def create_healthcare_system(
    output_path: Optional[str] = None,
    format: str = "png",
    show: bool = False,
) -> str:
    """
    Create a healthcare system architecture diagram.

    Shows the high-level organization of a hospital/healthcare system
    including clinical, administrative, and support functions.

    Args:
        output_path: Output file path
        format: Output format
        show: Whether to open after creation

    Returns:
        Path to the generated diagram
    """
    if output_path is None:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        output_path = os.path.join(OUTPUT_DIR, "healthcare_system")

    with Diagram(
        "Healthcare System Architecture",
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
        # Patient Entry
        with Cluster("Patient Entry Points"):
            emergency = Blank("Emergency\nDepartment")
            emergency._attrs["color"] = get_color("semantic.danger")
            emergency._attrs["fillcolor"] = "#ffebee"
            emergency._attrs["penwidth"] = "2"

            outpatient = Blank("Outpatient\nClinics")
            outpatient._attrs["color"] = get_color("primary.blue")
            outpatient._attrs["fillcolor"] = "#e3f2fd"
            outpatient._attrs["penwidth"] = "2"

            referral = Blank("External\nReferrals")
            referral._attrs["color"] = get_color("primary.teal")
            referral._attrs["fillcolor"] = "#e0f2f1"
            referral._attrs["penwidth"] = "2"

        # Clinical Services
        with Cluster("Clinical Services"):
            inpatient = Blank("Inpatient\nWards")
            inpatient._attrs["color"] = get_color("semantic.success")
            inpatient._attrs["fillcolor"] = "#e8f5e9"
            inpatient._attrs["penwidth"] = "2"

            icu = Blank("Intensive Care\nUnit")
            icu._attrs["color"] = get_color("semantic.danger")
            icu._attrs["fillcolor"] = "#ffebee"
            icu._attrs["penwidth"] = "2"

            surgery = Blank("Surgical\nServices")
            surgery._attrs["color"] = get_color("semantic.warning")
            surgery._attrs["fillcolor"] = "#fff3e0"
            surgery._attrs["penwidth"] = "2"

            cardiology = Blank("Cardiology\nDepartment")
            cardiology._attrs["color"] = get_color("primary.navy")
            cardiology._attrs["fillcolor"] = "#e8eaf6"
            cardiology._attrs["penwidth"] = "2"

        # Support Services
        with Cluster("Support Services"):
            lab = Blank("Laboratory")
            lab._attrs["color"] = get_color("primary.teal")
            lab._attrs["fillcolor"] = "#e0f2f1"
            lab._attrs["penwidth"] = "2"

            imaging = Blank("Radiology/\nImaging")
            imaging._attrs["color"] = get_color("primary.teal")
            imaging._attrs["fillcolor"] = "#e0f2f1"
            imaging._attrs["penwidth"] = "2"

            pharmacy = Blank("Pharmacy")
            pharmacy._attrs["color"] = get_color("primary.teal")
            pharmacy._attrs["fillcolor"] = "#e0f2f1"
            pharmacy._attrs["penwidth"] = "2"

        # Data Systems
        with Cluster("Health Information Systems"):
            ehr = Blank("Electronic\nHealth Record")
            ehr._attrs["color"] = get_color("primary.navy")
            ehr._attrs["fillcolor"] = "#e8eaf6"
            ehr._attrs["penwidth"] = "2"

            pacs = Blank("PACS/\nImaging Archive")
            pacs._attrs["color"] = get_color("primary.navy")
            pacs._attrs["fillcolor"] = "#e8eaf6"
            pacs._attrs["penwidth"] = "2"

            analytics = Blank("Clinical\nAnalytics")
            analytics._attrs["color"] = get_color("primary.navy")
            analytics._attrs["fillcolor"] = "#e8eaf6"
            analytics._attrs["penwidth"] = "2"

        # Connect entry points to clinical
        emergency >> inpatient
        emergency >> icu
        outpatient >> inpatient
        outpatient >> surgery
        referral >> cardiology

        # Clinical to support
        inpatient >> lab
        inpatient >> imaging
        icu >> lab
        surgery >> lab
        surgery >> imaging
        cardiology >> imaging
        cardiology >> lab

        # Support to pharmacy
        lab >> pharmacy
        imaging >> pharmacy

        # All to EHR
        inpatient >> ehr
        icu >> ehr
        surgery >> ehr
        cardiology >> ehr
        lab >> ehr
        imaging >> pacs
        pacs >> ehr
        ehr >> analytics

    return f"{output_path}.{format}"


def create_cardiology_department(
    output_path: Optional[str] = None,
    format: str = "png",
    show: bool = False,
) -> str:
    """
    Create a cardiology department organization diagram.

    Shows the structure and workflow of a cardiology department.

    Args:
        output_path: Output file path
        format: Output format
        show: Whether to open after creation

    Returns:
        Path to the generated diagram
    """
    if output_path is None:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        output_path = os.path.join(OUTPUT_DIR, "cardiology_department")

    with Diagram(
        "Cardiology Department Structure",
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
        # Patient Referral
        with Cluster("Patient Referral"):
            primary = Blank("Primary Care\nReferral")
            primary._attrs["color"] = get_color("primary.blue")
            primary._attrs["fillcolor"] = "#e3f2fd"
            primary._attrs["penwidth"] = "2"

            er = Blank("Emergency\nDepartment")
            er._attrs["color"] = get_color("semantic.danger")
            er._attrs["fillcolor"] = "#ffebee"
            er._attrs["penwidth"] = "2"

        # Outpatient Clinics
        with Cluster("Outpatient Clinics"):
            general = Blank("General\nCardiology")
            general._attrs["color"] = get_color("semantic.success")
            general._attrs["fillcolor"] = "#e8f5e9"
            general._attrs["penwidth"] = "2"

            hf = Blank("Heart Failure\nClinic")
            hf._attrs["color"] = get_color("semantic.success")
            hf._attrs["fillcolor"] = "#e8f5e9"
            hf._attrs["penwidth"] = "2"

            arrhythmia = Blank("Arrhythmia/\nEP Clinic")
            arrhythmia._attrs["color"] = get_color("semantic.success")
            arrhythmia._attrs["fillcolor"] = "#e8f5e9"
            arrhythmia._attrs["penwidth"] = "2"

            preventive = Blank("Preventive\nCardiology")
            preventive._attrs["color"] = get_color("semantic.success")
            preventive._attrs["fillcolor"] = "#e8f5e9"
            preventive._attrs["penwidth"] = "2"

        # Diagnostic Services
        with Cluster("Diagnostic Services"):
            echo = Blank("Echocardiography")
            echo._attrs["color"] = get_color("primary.teal")
            echo._attrs["fillcolor"] = "#e0f2f1"
            echo._attrs["penwidth"] = "2"

            stress = Blank("Stress Testing")
            stress._attrs["color"] = get_color("primary.teal")
            stress._attrs["fillcolor"] = "#e0f2f1"
            stress._attrs["penwidth"] = "2"

            holter = Blank("Holter/Event\nMonitoring")
            holter._attrs["color"] = get_color("primary.teal")
            holter._attrs["fillcolor"] = "#e0f2f1"
            holter._attrs["penwidth"] = "2"

            cath = Blank("Cardiac Cath\nLab")
            cath._attrs["color"] = get_color("semantic.warning")
            cath._attrs["fillcolor"] = "#fff3e0"
            cath._attrs["penwidth"] = "2"

        # Interventional
        with Cluster("Interventional Cardiology"):
            pci = Blank("PCI/\nAngioplasty")
            pci._attrs["color"] = get_color("semantic.warning")
            pci._attrs["fillcolor"] = "#fff3e0"
            pci._attrs["penwidth"] = "2"

            structural = Blank("Structural\nHeart")
            structural._attrs["color"] = get_color("semantic.warning")
            structural._attrs["fillcolor"] = "#fff3e0"
            structural._attrs["penwidth"] = "2"

            ep_lab = Blank("EP Lab/\nAblation")
            ep_lab._attrs["color"] = get_color("semantic.warning")
            ep_lab._attrs["fillcolor"] = "#fff3e0"
            ep_lab._attrs["penwidth"] = "2"

        # Cardiac Surgery
        with Cluster("Cardiac Surgery"):
            cabg = Blank("CABG")
            cabg._attrs["color"] = get_color("semantic.danger")
            cabg._attrs["fillcolor"] = "#ffebee"
            cabg._attrs["penwidth"] = "2"

            valve = Blank("Valve Surgery")
            valve._attrs["color"] = get_color("semantic.danger")
            valve._attrs["fillcolor"] = "#ffebee"
            valve._attrs["penwidth"] = "2"

            transplant = Blank("Transplant/\nMCS")
            transplant._attrs["color"] = get_color("semantic.danger")
            transplant._attrs["fillcolor"] = "#ffebee"
            transplant._attrs["penwidth"] = "2"

        # CCU
        with Cluster("Cardiac Care"):
            ccu = Blank("CCU/\nCardiac ICU")
            ccu._attrs["color"] = get_color("primary.navy")
            ccu._attrs["fillcolor"] = "#e8eaf6"
            ccu._attrs["penwidth"] = "2"

            rehab = Blank("Cardiac\nRehabilitation")
            rehab._attrs["color"] = get_color("primary.navy")
            rehab._attrs["fillcolor"] = "#e8eaf6"
            rehab._attrs["penwidth"] = "2"

        # Connections
        primary >> general
        er >> ccu

        general >> echo
        general >> stress
        general >> holter
        general >> cath

        hf >> echo
        hf >> transplant

        arrhythmia >> holter
        arrhythmia >> ep_lab

        cath >> pci
        cath >> structural

        pci >> ccu
        ep_lab >> ccu
        cabg >> ccu
        valve >> ccu

        ccu >> rehab

    return f"{output_path}.{format}"


def create_data_pipeline(
    title: str = "Clinical Data Pipeline",
    sources: Optional[List[str]] = None,
    processing: Optional[List[str]] = None,
    storage: Optional[List[str]] = None,
    outputs: Optional[List[str]] = None,
    output_path: Optional[str] = None,
    format: str = "png",
    show: bool = False,
) -> str:
    """
    Create a data pipeline visualization diagram.

    Shows data flow from sources through processing to outputs.

    Args:
        title: Diagram title
        sources: List of data source names
        processing: List of processing step names
        storage: List of storage/database names
        outputs: List of output/application names
        output_path: Output file path
        format: Output format
        show: Whether to open after creation

    Returns:
        Path to the generated diagram
    """
    if output_path is None:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        output_path = os.path.join(OUTPUT_DIR, "data_pipeline")

    # Default values
    if sources is None:
        sources = ["EHR/EMR", "Lab Results", "Imaging (PACS)", "Wearables/Devices", "Clinical Notes"]
    if processing is None:
        processing = ["Data Extraction", "Cleaning/Validation", "NLP Processing", "Feature Engineering"]
    if storage is None:
        storage = ["Data Lake", "Clinical Data Warehouse", "FHIR Server"]
    if outputs is None:
        outputs = ["Clinical Dashboards", "ML/AI Models", "Research Analytics", "Population Health"]

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
        # Data Sources
        with Cluster("Data Sources"):
            source_nodes = []
            for src in sources:
                node = Blank(src)
                node._attrs["color"] = get_color("primary.blue")
                node._attrs["fillcolor"] = "#e3f2fd"
                node._attrs["penwidth"] = "2"
                source_nodes.append(node)

        # Processing
        with Cluster("Data Processing"):
            proc_nodes = []
            prev = None
            for proc in processing:
                node = Blank(proc)
                node._attrs["color"] = get_color("semantic.warning")
                node._attrs["fillcolor"] = "#fff3e0"
                node._attrs["penwidth"] = "2"
                if prev:
                    prev >> node
                proc_nodes.append(node)
                prev = node

        # Storage
        with Cluster("Data Storage"):
            storage_nodes = []
            for store in storage:
                node = Blank(store)
                node._attrs["color"] = get_color("primary.teal")
                node._attrs["fillcolor"] = "#e0f2f1"
                node._attrs["penwidth"] = "2"
                storage_nodes.append(node)

        # Outputs
        with Cluster("Applications"):
            output_nodes = []
            for out in outputs:
                node = Blank(out)
                node._attrs["color"] = get_color("semantic.success")
                node._attrs["fillcolor"] = "#e8f5e9"
                node._attrs["penwidth"] = "2"
                output_nodes.append(node)

        # Connect sources to processing
        for src in source_nodes:
            if proc_nodes:
                src >> proc_nodes[0]

        # Connect processing to storage
        if proc_nodes and storage_nodes:
            for store in storage_nodes:
                proc_nodes[-1] >> store

        # Connect storage to outputs
        for store in storage_nodes:
            for out in output_nodes:
                store >> out

    return f"{output_path}.{format}"


def demo():
    """Generate demo diagrams to test the module."""
    print("Generating healthcare architecture diagrams...")

    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Generate all architecture diagrams
    diagrams_to_create = [
        ("Healthcare System", lambda: create_healthcare_system()),
        ("Cardiology Department", lambda: create_cardiology_department()),
        ("Data Pipeline", lambda: create_data_pipeline()),
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
