"""
Process Flows Module

Creates publication-quality flowcharts, algorithms, and process diagrams.
Designed for clinical pathways, treatment algorithms, and research methodologies.

Diagrams:
    - flowchart: General flowchart with decision nodes
    - treatment_algorithm: Clinical treatment pathway
    - patient_journey: Timeline of patient care
    - study_flow: CONSORT-style study flow diagram
    - decision_tree: Branching decision tree
"""

import drawsvg as draw
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
from dataclasses import dataclass
from enum import Enum

# Import design tokens
try:
    from tokens.index import (
        get_color, get_color_palette, get_accessible_pair,
        get_tokens, get_spacing, hex_to_rgb
    )
except ImportError:
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from tokens.index import (
        get_color, get_color_palette, get_accessible_pair,
        get_tokens, get_spacing, hex_to_rgb
    )


# Constants
DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600
FONT_FAMILY = "Helvetica, Arial, sans-serif"


class NodeType(Enum):
    """Types of flowchart nodes."""
    START = "start"
    END = "end"
    PROCESS = "process"
    DECISION = "decision"
    INPUT = "input"
    OUTPUT = "output"


@dataclass
class FlowNode:
    """Represents a node in a flowchart."""
    id: str
    label: str
    node_type: NodeType = NodeType.PROCESS
    x: float = 0
    y: float = 0
    width: float = 120
    height: float = 50
    color: Optional[str] = None
    sublabel: Optional[str] = None


@dataclass
class FlowConnection:
    """Represents a connection between nodes."""
    from_id: str
    to_id: str
    label: Optional[str] = None
    style: str = "solid"  # solid, dashed


def _get_flow_colors() -> Dict[str, str]:
    """Get standard colors for flow diagrams."""
    return {
        "start": get_color("semantic.success"),
        "end": get_color("semantic.danger"),
        "process": get_color("primary.blue"),
        "decision": get_color("primary.teal"),
        "input": get_color("text.muted"),
        "output": get_color("semantic.warning"),
        "arrow": get_color("text.secondary"),
        "label": get_color("text.primary"),
        "background": get_color("backgrounds.white"),
        "border": get_color("text.secondary"),
    }


def _draw_node(
    d: draw.Drawing,
    node: FlowNode,
    colors: Dict[str, str],
    scale: float = 1.0
) -> None:
    """Draw a single flowchart node."""
    x, y = node.x, node.y
    w, h = node.width * scale, node.height * scale

    # Get color
    fill_color = node.color or colors.get(node.node_type.value, colors["process"])

    if node.node_type == NodeType.START:
        # Rounded rectangle (pill shape)
        d.append(draw.Rectangle(
            x - w/2, y - h/2, w, h,
            rx=h/2, ry=h/2,
            fill=fill_color,
            stroke=colors["border"],
            stroke_width=1.5
        ))

    elif node.node_type == NodeType.END:
        # Rounded rectangle (pill shape)
        d.append(draw.Rectangle(
            x - w/2, y - h/2, w, h,
            rx=h/2, ry=h/2,
            fill=fill_color,
            stroke=colors["border"],
            stroke_width=1.5
        ))

    elif node.node_type == NodeType.DECISION:
        # Diamond shape
        diamond = draw.Path(
            fill=fill_color,
            stroke=colors["border"],
            stroke_width=1.5
        )
        diamond.M(x, y - h/2)  # Top
        diamond.L(x + w/2, y)  # Right
        diamond.L(x, y + h/2)  # Bottom
        diamond.L(x - w/2, y)  # Left
        diamond.Z()
        d.append(diamond)

    elif node.node_type == NodeType.INPUT:
        # Parallelogram (slanted left)
        offset = 10 * scale
        para = draw.Path(
            fill=fill_color,
            stroke=colors["border"],
            stroke_width=1.5
        )
        para.M(x - w/2 + offset, y - h/2)
        para.L(x + w/2 + offset, y - h/2)
        para.L(x + w/2 - offset, y + h/2)
        para.L(x - w/2 - offset, y + h/2)
        para.Z()
        d.append(para)

    elif node.node_type == NodeType.OUTPUT:
        # Parallelogram (slanted right)
        offset = 10 * scale
        para = draw.Path(
            fill=fill_color,
            stroke=colors["border"],
            stroke_width=1.5
        )
        para.M(x - w/2 - offset, y - h/2)
        para.L(x + w/2 - offset, y - h/2)
        para.L(x + w/2 + offset, y + h/2)
        para.L(x - w/2 + offset, y + h/2)
        para.Z()
        d.append(para)

    else:  # PROCESS - default rectangle
        d.append(draw.Rectangle(
            x - w/2, y - h/2, w, h,
            rx=4 * scale, ry=4 * scale,
            fill=fill_color,
            stroke=colors["border"],
            stroke_width=1.5
        ))

    # Label text
    # Wrap text if too long
    words = node.label.split()
    lines = []
    current_line = []
    max_chars = int(w / (7 * scale))

    for word in words:
        if len(' '.join(current_line + [word])) <= max_chars:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))

    # Draw text lines
    line_height = 12 * scale
    start_y = y - (len(lines) - 1) * line_height / 2

    for i, line in enumerate(lines):
        d.append(draw.Text(
            line,
            10 * scale,
            x, start_y + i * line_height,
            center=True,
            font_family=FONT_FAMILY,
            font_weight="bold" if node.node_type in [NodeType.START, NodeType.END] else "normal",
            fill="#ffffff" if node.node_type != NodeType.INPUT else colors["label"]
        ))

    # Sublabel
    if node.sublabel:
        d.append(draw.Text(
            node.sublabel,
            8 * scale,
            x, y + h/2 + 12 * scale,
            center=True,
            font_family=FONT_FAMILY,
            fill=colors["label"]
        ))


def _draw_arrow(
    d: draw.Drawing,
    x1: float, y1: float,
    x2: float, y2: float,
    colors: Dict[str, str],
    label: Optional[str] = None,
    style: str = "solid",
    scale: float = 1.0
) -> None:
    """Draw an arrow between two points."""
    import math

    # Calculate direction
    dx = x2 - x1
    dy = y2 - y1
    length = math.sqrt(dx*dx + dy*dy)

    if length == 0:
        return

    # Normalize
    ux, uy = dx/length, dy/length

    # Arrow head size
    head_size = 8 * scale

    # End point (slightly before to leave room for arrowhead)
    end_x = x2 - ux * head_size
    end_y = y2 - uy * head_size

    # Line style
    dash = "5,3" if style == "dashed" else None

    # Draw line
    d.append(draw.Line(
        x1, y1, end_x, end_y,
        stroke=colors["arrow"],
        stroke_width=1.5 * scale,
        stroke_dasharray=dash
    ))

    # Arrow head
    angle = math.atan2(dy, dx)
    head_angle = math.pi / 6  # 30 degrees

    # Arrow head points
    ax1 = x2 - head_size * math.cos(angle - head_angle)
    ay1 = y2 - head_size * math.sin(angle - head_angle)
    ax2 = x2 - head_size * math.cos(angle + head_angle)
    ay2 = y2 - head_size * math.sin(angle + head_angle)

    arrow = draw.Path(
        fill=colors["arrow"],
        stroke="none"
    )
    arrow.M(x2, y2)
    arrow.L(ax1, ay1)
    arrow.L(ax2, ay2)
    arrow.Z()
    d.append(arrow)

    # Label
    if label:
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2

        # Offset label slightly
        offset = 10 * scale
        label_x = mid_x + uy * offset
        label_y = mid_y - ux * offset

        d.append(draw.Text(
            label,
            9 * scale,
            label_x, label_y,
            center=True,
            font_family=FONT_FAMILY,
            fill=colors["label"]
        ))


def flowchart(
    nodes: List[FlowNode],
    connections: List[FlowConnection],
    width: int = DEFAULT_WIDTH,
    height: int = DEFAULT_HEIGHT,
    title: Optional[str] = None,
    auto_layout: bool = True
) -> draw.Drawing:
    """
    Create a general flowchart.

    Args:
        nodes: List of FlowNode objects
        connections: List of FlowConnection objects
        width: Canvas width
        height: Canvas height
        title: Optional title
        auto_layout: Auto-arrange nodes if positions are (0,0)

    Returns:
        drawsvg.Drawing object
    """
    d = draw.Drawing(width, height)
    colors = _get_flow_colors()

    # Background
    d.append(draw.Rectangle(0, 0, width, height, fill=colors["background"]))

    # Title
    if title:
        d.append(draw.Text(
            title, 16,
            width / 2, 30,
            center=True,
            font_family=FONT_FAMILY,
            font_weight="bold",
            fill=colors["label"]
        ))

    # Auto-layout if needed
    if auto_layout:
        margin_top = 60 if title else 40
        margin_bottom = 40
        margin_sides = 80

        available_height = height - margin_top - margin_bottom
        vertical_spacing = available_height / max(len(nodes), 1)

        for i, node in enumerate(nodes):
            if node.x == 0 and node.y == 0:
                node.x = width / 2
                node.y = margin_top + i * vertical_spacing + vertical_spacing / 2

    # Create node lookup
    node_map = {node.id: node for node in nodes}

    # Draw connections first (so they're behind nodes)
    for conn in connections:
        from_node = node_map.get(conn.from_id)
        to_node = node_map.get(conn.to_id)

        if from_node and to_node:
            # Calculate connection points
            y1 = from_node.y + from_node.height / 2
            y2 = to_node.y - to_node.height / 2

            _draw_arrow(
                d,
                from_node.x, y1,
                to_node.x, y2,
                colors,
                label=conn.label,
                style=conn.style
            )

    # Draw nodes
    for node in nodes:
        _draw_node(d, node, colors)

    return d


def treatment_algorithm(
    steps: List[str],
    decisions: Optional[List[Tuple[int, str, str, str]]] = None,
    width: int = 600,
    height: int = None,
    title: Optional[str] = None
) -> draw.Drawing:
    """
    Create a clinical treatment algorithm.

    Args:
        steps: List of treatment steps in order
        decisions: List of (after_step_index, question, yes_label, no_label) tuples
        width: Canvas width
        height: Auto-calculated if None
        title: Algorithm title

    Returns:
        drawsvg.Drawing object
    """
    # Calculate height
    n_steps = len(steps)
    n_decisions = len(decisions) if decisions else 0
    row_height = 80
    margin_top = 60 if title else 40
    margin_bottom = 40

    if height is None:
        height = margin_top + (n_steps + n_decisions) * row_height + margin_bottom

    d = draw.Drawing(width, height)
    colors = _get_flow_colors()

    # Background
    d.append(draw.Rectangle(0, 0, width, height, fill=colors["background"]))

    # Title
    if title:
        d.append(draw.Text(
            title, 16,
            width / 2, 30,
            center=True,
            font_family=FONT_FAMILY,
            font_weight="bold",
            fill=colors["label"]
        ))

    # Build nodes and connections
    nodes = []
    connections = []

    current_y = margin_top + 50
    center_x = width / 2

    for i, step in enumerate(steps):
        node_type = NodeType.START if i == 0 else (NodeType.END if i == len(steps) - 1 else NodeType.PROCESS)

        node = FlowNode(
            id=f"step_{i}",
            label=step,
            node_type=node_type,
            x=center_x,
            y=current_y,
            width=200,
            height=50
        )
        nodes.append(node)

        # Connect to previous step
        if i > 0:
            connections.append(FlowConnection(f"step_{i-1}", f"step_{i}"))

        current_y += row_height

        # Check for decision after this step
        if decisions:
            for dec_idx, question, yes_label, no_label in decisions:
                if dec_idx == i:
                    # Add decision node
                    dec_node = FlowNode(
                        id=f"decision_{i}",
                        label=question,
                        node_type=NodeType.DECISION,
                        x=center_x,
                        y=current_y,
                        width=160,
                        height=60
                    )
                    nodes.append(dec_node)

                    # Update connection to go through decision
                    connections[-1] = FlowConnection(f"step_{i}", f"decision_{i}")
                    connections.append(FlowConnection(f"decision_{i}", f"step_{i+1}", label=yes_label))

                    current_y += row_height

    # Draw connections
    node_map = {node.id: node for node in nodes}

    for conn in connections:
        from_node = node_map.get(conn.from_id)
        to_node = node_map.get(conn.to_id)

        if from_node and to_node:
            # Determine exit and entry points based on node types
            if from_node.node_type == NodeType.DECISION:
                y1 = from_node.y + from_node.height / 2
            else:
                y1 = from_node.y + from_node.height / 2

            y2 = to_node.y - to_node.height / 2

            _draw_arrow(
                d,
                from_node.x, y1,
                to_node.x, y2,
                colors,
                label=conn.label
            )

    # Draw nodes
    for node in nodes:
        _draw_node(d, node, colors)

    return d


def patient_journey(
    stages: List[Dict],
    width: int = 900,
    height: int = 250,
    title: Optional[str] = None
) -> draw.Drawing:
    """
    Create a patient journey timeline.

    Args:
        stages: List of dicts with:
                - name: Stage name
                - duration: Optional duration text
                - events: Optional list of events
                - color: Optional custom color
        width: Canvas width
        height: Canvas height
        title: Timeline title

    Returns:
        drawsvg.Drawing object
    """
    d = draw.Drawing(width, height)
    colors = _get_flow_colors()
    palette = get_color_palette("categorical")

    # Background
    d.append(draw.Rectangle(0, 0, width, height, fill=colors["background"]))

    # Title
    if title:
        d.append(draw.Text(
            title, 16,
            width / 2, 25,
            center=True,
            font_family=FONT_FAMILY,
            font_weight="bold",
            fill=colors["label"]
        ))

    # Margins
    margin_left = 60
    margin_right = 60
    margin_top = 60 if title else 40
    timeline_y = margin_top + 60

    plot_width = width - margin_left - margin_right
    n_stages = len(stages)
    stage_width = plot_width / n_stages

    # Timeline base line
    d.append(draw.Line(
        margin_left, timeline_y,
        width - margin_right, timeline_y,
        stroke=colors["border"],
        stroke_width=3
    ))

    # Draw stages
    for i, stage in enumerate(stages):
        stage_x = margin_left + i * stage_width
        center_x = stage_x + stage_width / 2
        stage_color = stage.get("color", palette[i % len(palette)])

        # Stage marker (circle on timeline)
        d.append(draw.Circle(
            center_x, timeline_y, 12,
            fill=stage_color,
            stroke=colors["background"],
            stroke_width=3
        ))

        # Stage number
        d.append(draw.Text(
            str(i + 1), 10,
            center_x, timeline_y + 4,
            center=True,
            font_family=FONT_FAMILY,
            font_weight="bold",
            fill="#ffffff"
        ))

        # Stage name
        d.append(draw.Text(
            stage["name"], 11,
            center_x, timeline_y - 25,
            center=True,
            font_family=FONT_FAMILY,
            font_weight="bold",
            fill=colors["label"]
        ))

        # Duration
        if stage.get("duration"):
            d.append(draw.Text(
                stage["duration"], 9,
                center_x, timeline_y + 30,
                center=True,
                font_family=FONT_FAMILY,
                fill=colors["border"]
            ))

        # Events below
        if stage.get("events"):
            for j, event in enumerate(stage["events"][:3]):  # Max 3 events
                d.append(draw.Text(
                    f"• {event}", 8,
                    center_x, timeline_y + 50 + j * 14,
                    center=True,
                    font_family=FONT_FAMILY,
                    fill=colors["label"]
                ))

        # Arrow to next stage
        if i < n_stages - 1:
            arrow_start = center_x + 15
            arrow_end = center_x + stage_width - 15

            d.append(draw.Line(
                arrow_start, timeline_y,
                arrow_end - 8, timeline_y,
                stroke=colors["border"],
                stroke_width=2
            ))

    return d


def study_flow(
    enrollment: int,
    randomized: int,
    groups: List[Dict],
    width: int = 700,
    height: int = 500,
    title: str = "CONSORT Flow Diagram"
) -> draw.Drawing:
    """
    Create a CONSORT-style study flow diagram.

    Args:
        enrollment: Number screened/enrolled
        randomized: Number randomized
        groups: List of dicts with:
                - name: Group name (e.g., "Treatment", "Control")
                - allocated: Number allocated
                - discontinued: Number discontinued (optional)
                - analyzed: Number analyzed
        width: Canvas width
        height: Canvas height
        title: Diagram title

    Returns:
        drawsvg.Drawing object
    """
    d = draw.Drawing(width, height)
    colors = _get_flow_colors()

    # Background
    d.append(draw.Rectangle(0, 0, width, height, fill=colors["background"]))

    # Title
    d.append(draw.Text(
        title, 16,
        width / 2, 30,
        center=True,
        font_family=FONT_FAMILY,
        font_weight="bold",
        fill=colors["label"]
    ))

    # Box dimensions
    box_width = 160
    box_height = 45
    margin_top = 60

    center_x = width / 2

    # Enrollment box
    enroll_y = margin_top + 30
    d.append(draw.Rectangle(
        center_x - box_width/2, enroll_y - box_height/2,
        box_width, box_height,
        rx=4, ry=4,
        fill=colors["process"],
        stroke=colors["border"],
        stroke_width=1.5
    ))
    d.append(draw.Text(
        f"Enrolled (n={enrollment})", 10,
        center_x, enroll_y + 4,
        center=True,
        font_family=FONT_FAMILY,
        fill="#ffffff"
    ))

    # Randomization box
    random_y = enroll_y + 80
    d.append(draw.Rectangle(
        center_x - box_width/2, random_y - box_height/2,
        box_width, box_height,
        rx=4, ry=4,
        fill=colors["decision"],
        stroke=colors["border"],
        stroke_width=1.5
    ))
    d.append(draw.Text(
        f"Randomized (n={randomized})", 10,
        center_x, random_y + 4,
        center=True,
        font_family=FONT_FAMILY,
        fill="#ffffff"
    ))

    # Arrow from enrollment to randomization
    _draw_arrow(d, center_x, enroll_y + box_height/2,
               center_x, random_y - box_height/2, colors)

    # Groups
    n_groups = len(groups)
    group_spacing = (width - 100) / n_groups
    group_y = random_y + 100

    for i, group in enumerate(groups):
        gx = 50 + (i + 0.5) * group_spacing

        # Allocation box
        d.append(draw.Rectangle(
            gx - box_width/2, group_y - box_height/2,
            box_width, box_height,
            rx=4, ry=4,
            fill=colors["process"],
            stroke=colors["border"],
            stroke_width=1.5
        ))
        d.append(draw.Text(
            group["name"], 10,
            gx, group_y - 8,
            center=True,
            font_family=FONT_FAMILY,
            font_weight="bold",
            fill="#ffffff"
        ))
        d.append(draw.Text(
            f"n={group['allocated']}", 9,
            gx, group_y + 8,
            center=True,
            font_family=FONT_FAMILY,
            fill="#ffffff"
        ))

        # Arrow from randomization
        _draw_arrow(d, center_x, random_y + box_height/2,
                   gx, group_y - box_height/2, colors)

        # Discontinued (if any)
        if group.get("discontinued", 0) > 0:
            disc_y = group_y + 70
            disc_x = gx + box_width/2 + 50

            d.append(draw.Rectangle(
                disc_x - 60, disc_y - 20,
                120, 40,
                rx=4, ry=4,
                fill=colors["end"],
                fill_opacity=0.8,
                stroke=colors["border"],
                stroke_width=1
            ))
            d.append(draw.Text(
                f"Discontinued", 8,
                disc_x, disc_y - 5,
                center=True,
                font_family=FONT_FAMILY,
                fill="#ffffff"
            ))
            d.append(draw.Text(
                f"n={group['discontinued']}", 8,
                disc_x, disc_y + 8,
                center=True,
                font_family=FONT_FAMILY,
                fill="#ffffff"
            ))

            # Arrow to discontinued
            d.append(draw.Line(
                gx + box_width/2, group_y,
                disc_x - 60, disc_y,
                stroke=colors["arrow"],
                stroke_width=1,
                stroke_dasharray="4,2"
            ))

        # Analysis box
        analysis_y = group_y + 140
        d.append(draw.Rectangle(
            gx - box_width/2, analysis_y - box_height/2,
            box_width, box_height,
            rx=4, ry=4,
            fill=colors["start"],
            stroke=colors["border"],
            stroke_width=1.5
        ))
        d.append(draw.Text(
            f"Analyzed", 10,
            gx, analysis_y - 8,
            center=True,
            font_family=FONT_FAMILY,
            font_weight="bold",
            fill="#ffffff"
        ))
        d.append(draw.Text(
            f"n={group['analyzed']}", 9,
            gx, analysis_y + 8,
            center=True,
            font_family=FONT_FAMILY,
            fill="#ffffff"
        ))

        # Arrow to analysis
        _draw_arrow(d, gx, group_y + box_height/2,
                   gx, analysis_y - box_height/2, colors)

    return d


def simple_process_flow(
    steps: List[str],
    width: int = 800,
    height: int = 120,
    orientation: str = "horizontal",
    title: Optional[str] = None,
    colors: Optional[List[str]] = None
) -> draw.Drawing:
    """
    Create a simple linear process flow.

    Args:
        steps: List of step labels
        width: Canvas width
        height: Canvas height
        orientation: "horizontal" or "vertical"
        title: Optional title
        colors: Optional list of step colors

    Returns:
        drawsvg.Drawing object
    """
    flow_colors = _get_flow_colors()

    if orientation == "vertical":
        width, height = height, width

    d = draw.Drawing(width, height)

    # Background
    d.append(draw.Rectangle(0, 0, width, height, fill=flow_colors["background"]))

    # Get step colors
    if colors is None:
        palette = get_color_palette("categorical")
        colors = [palette[i % len(palette)] for i in range(len(steps))]

    n_steps = len(steps)

    if orientation == "horizontal":
        margin = 40
        step_width = (width - 2 * margin) / n_steps
        step_height = 50
        y = height / 2

        for i, (step, color) in enumerate(zip(steps, colors)):
            x = margin + (i + 0.5) * step_width

            # Chevron shape for all except last
            if i < n_steps - 1:
                chevron = draw.Path(fill=color, stroke=flow_colors["border"], stroke_width=1)
                hw = step_width * 0.4
                hh = step_height / 2
                tip = 15

                chevron.M(x - hw, y - hh)
                chevron.L(x + hw - tip, y - hh)
                chevron.L(x + hw, y)
                chevron.L(x + hw - tip, y + hh)
                chevron.L(x - hw, y + hh)
                if i > 0:
                    chevron.L(x - hw + tip, y)
                chevron.Z()
                d.append(chevron)
            else:
                # Last step: rounded rectangle
                d.append(draw.Rectangle(
                    x - step_width * 0.4, y - step_height/2,
                    step_width * 0.8, step_height,
                    rx=step_height/2, ry=step_height/2,
                    fill=color,
                    stroke=flow_colors["border"],
                    stroke_width=1
                ))

            # Label
            d.append(draw.Text(
                step, 10,
                x, y + 4,
                center=True,
                font_family=FONT_FAMILY,
                font_weight="bold",
                fill="#ffffff"
            ))

    return d


if __name__ == "__main__":
    # Demo: Generate sample process flows
    output_dir = Path(__file__).parent.parent / "outputs"
    output_dir.mkdir(exist_ok=True)

    print("Generating process flows...")

    # Treatment algorithm
    algorithm = treatment_algorithm(
        steps=[
            "Patient presents with chest pain",
            "ECG and cardiac biomarkers",
            "Risk stratification",
            "Initiate treatment",
            "Follow-up"
        ],
        decisions=[
            (1, "STEMI?", "Yes", "No"),
        ],
        title="Acute Coronary Syndrome Algorithm"
    )
    algorithm.save_png(str(output_dir / "treatment_algorithm.png"))
    print("  -> treatment_algorithm.png")

    # Patient journey
    journey = patient_journey(
        stages=[
            {"name": "Diagnosis", "duration": "Day 1", "events": ["ECG", "Blood tests"]},
            {"name": "Treatment", "duration": "Days 2-7", "events": ["Medication", "Monitoring"]},
            {"name": "Recovery", "duration": "Weeks 2-4", "events": ["Cardiac rehab"]},
            {"name": "Follow-up", "duration": "Ongoing", "events": ["Regular checkups"]},
        ],
        title="Heart Failure Patient Journey"
    )
    journey.save_png(str(output_dir / "patient_journey.png"))
    print("  -> patient_journey.png")

    # Study flow
    study = study_flow(
        enrollment=1500,
        randomized=1200,
        groups=[
            {"name": "Treatment", "allocated": 600, "discontinued": 45, "analyzed": 555},
            {"name": "Control", "allocated": 600, "discontinued": 52, "analyzed": 548},
        ],
        title="DAPA-HF Study Flow"
    )
    study.save_png(str(output_dir / "study_flow.png"))
    print("  -> study_flow.png")

    # Simple process flow
    simple = simple_process_flow(
        steps=["Screening", "Enrollment", "Randomization", "Treatment", "Analysis"],
        title="Study Process"
    )
    simple.save_png(str(output_dir / "simple_process.png"))
    print("  -> simple_process.png")

    print("\nDone! Check outputs/ directory.")
