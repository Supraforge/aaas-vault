"""
Medical Diagrams Module

Creates publication-quality medical illustrations using drawsvg.
Designed for cardiology content but extensible to other specialties.

Diagrams:
    - heart_simple: Simplified 4-chamber heart view
    - heart_coronary: Coronary artery anatomy
    - cardiac_conduction: Conduction system diagram
    - ecg_wave: ECG waveform template
    - blood_pressure: BP illustration with vessels
    - organ_icon: Simple organ icons for infographics
"""

import drawsvg as draw
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

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
DEFAULT_WIDTH = 400
DEFAULT_HEIGHT = 400
FONT_FAMILY = "Helvetica, Arial, sans-serif"


def _get_colors() -> Dict[str, str]:
    """Get standard colors for medical diagrams."""
    return {
        "blood_oxygenated": "#e63946",  # Bright red for oxygenated blood
        "blood_deoxygenated": "#457b9d",  # Blue for deoxygenated blood
        "muscle": "#f4a261",  # Cardiac muscle
        "vessel_artery": "#e63946",
        "vessel_vein": "#457b9d",
        "conduction": "#2a9d8f",  # Electrical conduction
        "label": get_color("text.primary"),
        "background": get_color("backgrounds.white"),
        "highlight": get_color("primary.teal"),
        "border": get_color("text.secondary"),
    }


def heart_simple(
    width: int = DEFAULT_WIDTH,
    height: int = DEFAULT_HEIGHT,
    highlight_chamber: Optional[str] = None,
    show_labels: bool = True,
    show_vessels: bool = True,
    title: Optional[str] = None
) -> draw.Drawing:
    """
    Create a simplified 4-chamber heart diagram.

    Args:
        width: Canvas width in pixels
        height: Canvas height in pixels
        highlight_chamber: Optional chamber to highlight ("ra", "la", "rv", "lv")
        show_labels: Whether to show chamber labels
        show_vessels: Whether to show major vessels
        title: Optional title text

    Returns:
        drawsvg.Drawing object

    Usage:
        svg = heart_simple(highlight_chamber="lv", show_labels=True)
        svg.save_png("heart.png")
    """
    d = draw.Drawing(width, height, origin='center')
    colors = _get_colors()

    # Background
    d.append(draw.Rectangle(-width/2, -height/2, width, height, fill=colors["background"]))

    # Title
    if title:
        d.append(draw.Text(
            title, 14, 0, -height/2 + 30,
            center=True,
            font_family=FONT_FAMILY,
            font_weight="bold",
            fill=colors["label"]
        ))

    # Scale factor based on canvas size
    scale = min(width, height) / 400

    # Heart outline (simplified shape using paths)
    heart_path = draw.Path(
        stroke=colors["border"],
        stroke_width=2 * scale,
        fill="none"
    )

    # Simplified heart shape
    cx, cy = 0, 20 * scale

    # Left side of heart
    heart_path.M(-80 * scale, -40 * scale)
    heart_path.Q(-120 * scale, -100 * scale, -60 * scale, -100 * scale)
    heart_path.Q(0, -100 * scale, 0, -60 * scale)

    # Right side of heart
    heart_path.Q(0, -100 * scale, 60 * scale, -100 * scale)
    heart_path.Q(120 * scale, -100 * scale, 80 * scale, -40 * scale)

    # Bottom (apex)
    heart_path.Q(100 * scale, 40 * scale, 0, 100 * scale)
    heart_path.Q(-100 * scale, 40 * scale, -80 * scale, -40 * scale)

    d.append(heart_path)

    # Chamber definitions
    chambers = {
        "ra": {"x": 40 * scale, "y": -50 * scale, "color": colors["blood_deoxygenated"], "label": "RA"},
        "la": {"x": -40 * scale, "y": -50 * scale, "color": colors["blood_oxygenated"], "label": "LA"},
        "rv": {"x": 30 * scale, "y": 20 * scale, "color": colors["blood_deoxygenated"], "label": "RV"},
        "lv": {"x": -30 * scale, "y": 20 * scale, "color": colors["blood_oxygenated"], "label": "LV"},
    }

    # Draw chambers
    for chamber_id, chamber in chambers.items():
        # Determine fill color
        if highlight_chamber and highlight_chamber.lower() == chamber_id:
            fill_color = colors["highlight"]
            opacity = 0.9
        else:
            fill_color = chamber["color"]
            opacity = 0.6

        # Chamber ellipse
        d.append(draw.Ellipse(
            chamber["x"], chamber["y"],
            30 * scale, 35 * scale,
            fill=fill_color,
            fill_opacity=opacity,
            stroke=colors["border"],
            stroke_width=1.5 * scale
        ))

        # Labels
        if show_labels:
            d.append(draw.Text(
                chamber["label"],
                12 * scale,
                chamber["x"], chamber["y"] + 4 * scale,
                center=True,
                font_family=FONT_FAMILY,
                font_weight="bold",
                fill="#ffffff"
            ))

    # Draw major vessels if enabled
    if show_vessels:
        vessel_width = 12 * scale

        # Superior vena cava (to RA)
        d.append(draw.Line(
            50 * scale, -90 * scale,
            50 * scale, -130 * scale,
            stroke=colors["vessel_vein"],
            stroke_width=vessel_width
        ))
        d.append(draw.Text("SVC", 8 * scale, 70 * scale, -110 * scale,
                          font_family=FONT_FAMILY, fill=colors["label"]))

        # Inferior vena cava (to RA)
        d.append(draw.Line(
            50 * scale, 60 * scale,
            50 * scale, 90 * scale,
            stroke=colors["vessel_vein"],
            stroke_width=vessel_width
        ))
        d.append(draw.Text("IVC", 8 * scale, 70 * scale, 80 * scale,
                          font_family=FONT_FAMILY, fill=colors["label"]))

        # Pulmonary artery (from RV)
        d.append(draw.Line(
            30 * scale, -30 * scale,
            60 * scale, -70 * scale,
            stroke=colors["vessel_vein"],
            stroke_width=vessel_width
        ))
        d.append(draw.Text("PA", 8 * scale, 80 * scale, -60 * scale,
                          font_family=FONT_FAMILY, fill=colors["label"]))

        # Pulmonary veins (to LA)
        d.append(draw.Line(
            -50 * scale, -90 * scale,
            -80 * scale, -110 * scale,
            stroke=colors["vessel_artery"],
            stroke_width=vessel_width
        ))
        d.append(draw.Text("PV", 8 * scale, -100 * scale, -100 * scale,
                          font_family=FONT_FAMILY, fill=colors["label"]))

        # Aorta (from LV)
        d.append(draw.Line(
            -20 * scale, -60 * scale,
            -50 * scale, -100 * scale,
            stroke=colors["vessel_artery"],
            stroke_width=vessel_width * 1.2
        ))
        # Aortic arch
        arch = draw.Path(
            stroke=colors["vessel_artery"],
            stroke_width=vessel_width * 1.2,
            fill="none"
        )
        arch.M(-50 * scale, -100 * scale)
        arch.Q(-80 * scale, -130 * scale, -60 * scale, -140 * scale)
        arch.Q(-30 * scale, -150 * scale, 0, -140 * scale)
        d.append(arch)
        d.append(draw.Text("Aorta", 8 * scale, -30 * scale, -155 * scale,
                          font_family=FONT_FAMILY, fill=colors["label"]))

    # Legend
    if show_labels:
        legend_y = height/2 - 40 * scale
        d.append(draw.Rectangle(-90 * scale, legend_y - 8 * scale, 12 * scale, 12 * scale,
                               fill=colors["blood_oxygenated"]))
        d.append(draw.Text("Oxygenated", 9 * scale, -70 * scale, legend_y,
                          font_family=FONT_FAMILY, fill=colors["label"]))

        d.append(draw.Rectangle(20 * scale, legend_y - 8 * scale, 12 * scale, 12 * scale,
                               fill=colors["blood_deoxygenated"]))
        d.append(draw.Text("Deoxygenated", 9 * scale, 40 * scale, legend_y,
                          font_family=FONT_FAMILY, fill=colors["label"]))

    return d


def ecg_wave(
    width: int = 600,
    height: int = 200,
    wave_type: str = "normal",
    highlight_segment: Optional[str] = None,
    show_labels: bool = True,
    title: Optional[str] = None
) -> draw.Drawing:
    """
    Create an ECG waveform diagram.

    Args:
        width: Canvas width
        height: Canvas height
        wave_type: "normal", "afib", "stemi", "vfib"
        highlight_segment: Optional segment to highlight ("p", "qrs", "t", "st")
        show_labels: Whether to show wave labels
        title: Optional title

    Returns:
        drawsvg.Drawing object
    """
    d = draw.Drawing(width, height)
    colors = _get_colors()

    # Background with grid
    d.append(draw.Rectangle(0, 0, width, height, fill=colors["background"]))

    # ECG grid
    grid_color = "#ffcccc"
    small_grid = 5
    large_grid = 25

    # Small grid
    for x in range(0, width, small_grid):
        d.append(draw.Line(x, 0, x, height, stroke=grid_color, stroke_width=0.3))
    for y in range(0, height, small_grid):
        d.append(draw.Line(0, y, width, y, stroke=grid_color, stroke_width=0.3))

    # Large grid
    for x in range(0, width, large_grid):
        d.append(draw.Line(x, 0, x, height, stroke=grid_color, stroke_width=0.8))
    for y in range(0, height, large_grid):
        d.append(draw.Line(0, y, width, y, stroke=grid_color, stroke_width=0.8))

    # Title
    if title:
        d.append(draw.Text(
            title, 14, 10, 20,
            font_family=FONT_FAMILY,
            font_weight="bold",
            fill=colors["label"]
        ))

    # Baseline
    baseline = height * 0.6
    trace_color = "#000000"

    # Create ECG trace based on wave type
    path = draw.Path(stroke=trace_color, stroke_width=1.5, fill="none")

    if wave_type == "normal":
        # Start point
        x = 30
        path.M(x, baseline)

        # Cycle through 3 heartbeats
        for beat in range(3):
            start_x = x

            # P wave
            x += 10
            path.L(x, baseline)
            p_start = x
            path.Q(x + 15, baseline - 20, x + 30, baseline)
            x += 30
            p_end = x

            # PR segment
            path.L(x + 20, baseline)
            x += 20

            # Q wave
            q_start = x
            path.L(x + 5, baseline + 10)
            x += 5

            # R wave
            path.L(x + 10, baseline - 80)
            x += 10

            # S wave
            path.L(x + 10, baseline + 20)
            x += 10
            qrs_end = x

            # ST segment
            st_start = x
            path.L(x + 30, baseline)
            x += 30
            st_end = x

            # T wave
            t_start = x
            path.Q(x + 20, baseline - 40, x + 40, baseline)
            x += 40
            t_end = x

            # Isoelectric line
            path.L(x + 40, baseline)
            x += 40

            # Add labels for first beat
            if beat == 0 and show_labels:
                label_y = baseline + 50
                d.append(draw.Text("P", 10, (p_start + p_end)/2, baseline - 30,
                                  center=True, font_family=FONT_FAMILY, fill=colors["label"]))
                d.append(draw.Text("QRS", 10, (q_start + qrs_end)/2, baseline - 90,
                                  center=True, font_family=FONT_FAMILY, fill=colors["label"]))
                d.append(draw.Text("T", 10, (t_start + t_end)/2, baseline - 50,
                                  center=True, font_family=FONT_FAMILY, fill=colors["label"]))

                # Interval labels
                d.append(draw.Line(p_start, label_y - 5, qrs_end, label_y - 5,
                                  stroke=colors["border"], stroke_width=0.5))
                d.append(draw.Text("PR interval", 8, (p_start + q_start)/2, label_y + 5,
                                  center=True, font_family=FONT_FAMILY, fill=colors["label"]))

    elif wave_type == "afib":
        # Atrial fibrillation - irregular rhythm, no P waves
        x = 30
        path.M(x, baseline)

        import random
        random.seed(42)  # Reproducible

        for _ in range(4):
            # Fibrillatory waves instead of P wave
            for _ in range(8):
                path.L(x + 5, baseline + random.uniform(-5, 5))
                x += 5

            # Irregular R-R interval
            delay = random.randint(20, 60)
            path.L(x + delay/2, baseline)
            x += delay/2

            # QRS complex
            path.L(x + 5, baseline + 8)
            path.L(x + 10, baseline - 70)
            path.L(x + 15, baseline + 15)
            path.L(x + 20, baseline)
            x += 20

            # T wave
            path.Q(x + 15, baseline - 30, x + 30, baseline)
            x += 30

    d.append(path)

    return d


def cardiac_conduction(
    width: int = 500,
    height: int = 400,
    highlight_structure: Optional[str] = None,
    show_timing: bool = True,
    title: Optional[str] = None
) -> draw.Drawing:
    """
    Create a cardiac conduction system diagram.

    Args:
        width: Canvas width
        height: Canvas height
        highlight_structure: Structure to highlight ("sa_node", "av_node", "bundle_his",
                           "bundle_branches", "purkinje")
        show_timing: Show conduction timing annotations
        title: Optional title

    Returns:
        drawsvg.Drawing object
    """
    d = draw.Drawing(width, height)
    colors = _get_colors()

    # Background
    d.append(draw.Rectangle(0, 0, width, height, fill=colors["background"]))

    # Title
    if title:
        d.append(draw.Text(
            title, 16, width/2, 25,
            center=True,
            font_family=FONT_FAMILY,
            font_weight="bold",
            fill=colors["label"]
        ))

    # Simplified heart outline
    cx, cy = width/2, height/2
    scale = min(width, height) / 400

    # Heart shape
    heart = draw.Path(stroke=colors["border"], stroke_width=2, fill=colors["muscle"], fill_opacity=0.3)
    heart.M(cx, cy - 80 * scale)
    heart.Q(cx - 100 * scale, cy - 120 * scale, cx - 80 * scale, cy - 40 * scale)
    heart.Q(cx - 100 * scale, cy + 60 * scale, cx, cy + 100 * scale)
    heart.Q(cx + 100 * scale, cy + 60 * scale, cx + 80 * scale, cy - 40 * scale)
    heart.Q(cx + 100 * scale, cy - 120 * scale, cx, cy - 80 * scale)
    d.append(heart)

    # Conduction structures
    structures = {
        "sa_node": {
            "x": cx + 30 * scale, "y": cy - 60 * scale,
            "r": 12 * scale, "label": "SA Node",
            "timing": "0 ms"
        },
        "av_node": {
            "x": cx, "y": cy - 20 * scale,
            "r": 10 * scale, "label": "AV Node",
            "timing": "50 ms"
        },
        "bundle_his": {
            "x": cx, "y": cy + 10 * scale,
            "r": 8 * scale, "label": "Bundle of His",
            "timing": "100 ms"
        },
    }

    # Draw structures
    for struct_id, struct in structures.items():
        is_highlighted = highlight_structure and highlight_structure.lower().replace(" ", "_") == struct_id
        fill_color = colors["highlight"] if is_highlighted else colors["conduction"]

        d.append(draw.Circle(
            struct["x"], struct["y"], struct["r"],
            fill=fill_color,
            stroke=colors["border"],
            stroke_width=1.5
        ))

        # Labels
        d.append(draw.Text(
            struct["label"], 10 * scale,
            struct["x"] + 20 * scale, struct["y"] + 4,
            font_family=FONT_FAMILY,
            fill=colors["label"]
        ))

        if show_timing:
            d.append(draw.Text(
                struct["timing"], 8 * scale,
                struct["x"] + 20 * scale, struct["y"] + 16,
                font_family=FONT_FAMILY,
                fill=colors["border"]
            ))

    # Conduction pathways (arrows)
    arrow_color = colors["conduction"]

    # SA to AV
    d.append(draw.Line(
        structures["sa_node"]["x"], structures["sa_node"]["y"] + structures["sa_node"]["r"],
        structures["av_node"]["x"], structures["av_node"]["y"] - structures["av_node"]["r"],
        stroke=arrow_color, stroke_width=3,
        stroke_dasharray="5,3"
    ))

    # AV to Bundle of His
    d.append(draw.Line(
        structures["av_node"]["x"], structures["av_node"]["y"] + structures["av_node"]["r"],
        structures["bundle_his"]["x"], structures["bundle_his"]["y"] - structures["bundle_his"]["r"],
        stroke=arrow_color, stroke_width=3
    ))

    # Bundle branches
    bb_y = cy + 40 * scale
    # Left bundle
    d.append(draw.Line(cx, cy + 18 * scale, cx - 40 * scale, bb_y,
                      stroke=arrow_color, stroke_width=2))
    d.append(draw.Text("LBB", 9 * scale, cx - 60 * scale, bb_y,
                      font_family=FONT_FAMILY, fill=colors["label"]))

    # Right bundle
    d.append(draw.Line(cx, cy + 18 * scale, cx + 40 * scale, bb_y,
                      stroke=arrow_color, stroke_width=2))
    d.append(draw.Text("RBB", 9 * scale, cx + 45 * scale, bb_y,
                      font_family=FONT_FAMILY, fill=colors["label"]))

    # Purkinje fibers (simplified)
    purkinje_y = cy + 70 * scale
    for offset in [-50, -30, -10, 10, 30, 50]:
        x = cx + offset * scale
        d.append(draw.Line(
            cx - 40 * scale if offset < 0 else cx + 40 * scale, bb_y,
            x, purkinje_y,
            stroke=arrow_color, stroke_width=1, stroke_opacity=0.6
        ))

    d.append(draw.Text("Purkinje fibers", 9 * scale, cx, purkinje_y + 15,
                      center=True, font_family=FONT_FAMILY, fill=colors["label"]))

    if show_timing:
        d.append(draw.Text("150-200 ms", 8 * scale, cx, purkinje_y + 28,
                          center=True, font_family=FONT_FAMILY, fill=colors["border"]))

    return d


def organ_icon(
    organ: str,
    size: int = 100,
    color: Optional[str] = None,
    style: str = "filled"
) -> draw.Drawing:
    """
    Create a simple organ icon for infographics.

    Args:
        organ: "heart", "brain", "lungs", "kidney", "liver"
        size: Icon size in pixels
        color: Optional custom color (uses design tokens by default)
        style: "filled", "outline", or "minimal"

    Returns:
        drawsvg.Drawing object
    """
    d = draw.Drawing(size, size, origin='center')
    colors = _get_colors()

    fill_color = color or get_color("primary.blue")
    stroke_color = colors["border"]

    if style == "outline":
        fill_color = "none"
        stroke_width = 2
    elif style == "minimal":
        stroke_color = fill_color
        stroke_width = 1.5
        fill_color = "none"
    else:
        stroke_width = 1

    scale = size / 100

    if organ.lower() == "heart":
        # Heart shape
        path = draw.Path(fill=fill_color, stroke=stroke_color, stroke_width=stroke_width)
        path.M(0, 15 * scale)
        path.C(-30 * scale, -30 * scale, -45 * scale, 15 * scale, 0, 40 * scale)
        path.C(45 * scale, 15 * scale, 30 * scale, -30 * scale, 0, 15 * scale)
        path.Z()
        d.append(path)

    elif organ.lower() == "brain":
        # Simplified brain (two hemispheres)
        d.append(draw.Ellipse(-12 * scale, 0, 25 * scale, 30 * scale,
                             fill=fill_color, stroke=stroke_color, stroke_width=stroke_width))
        d.append(draw.Ellipse(12 * scale, 0, 25 * scale, 30 * scale,
                             fill=fill_color, stroke=stroke_color, stroke_width=stroke_width))
        # Central division
        d.append(draw.Line(0, -30 * scale, 0, 30 * scale,
                          stroke=stroke_color, stroke_width=stroke_width))

    elif organ.lower() == "lungs":
        # Left lung
        d.append(draw.Ellipse(-20 * scale, 5 * scale, 18 * scale, 30 * scale,
                             fill=fill_color, stroke=stroke_color, stroke_width=stroke_width))
        # Right lung
        d.append(draw.Ellipse(20 * scale, 5 * scale, 18 * scale, 30 * scale,
                             fill=fill_color, stroke=stroke_color, stroke_width=stroke_width))
        # Trachea
        d.append(draw.Rectangle(-4 * scale, -35 * scale, 8 * scale, 20 * scale,
                               fill=fill_color, stroke=stroke_color, stroke_width=stroke_width))

    elif organ.lower() == "kidney":
        # Bean shape
        path = draw.Path(fill=fill_color, stroke=stroke_color, stroke_width=stroke_width)
        path.M(0, -30 * scale)
        path.Q(35 * scale, -20 * scale, 30 * scale, 10 * scale)
        path.Q(25 * scale, 35 * scale, 0, 35 * scale)
        path.Q(-25 * scale, 35 * scale, -30 * scale, 10 * scale)
        path.Q(-35 * scale, -20 * scale, 0, -30 * scale)
        path.Z()
        d.append(path)
        # Notch
        d.append(draw.Ellipse(-5 * scale, 0, 8 * scale, 15 * scale,
                             fill=colors["background"], stroke=stroke_color, stroke_width=stroke_width * 0.5))

    elif organ.lower() == "liver":
        # Simplified liver shape
        path = draw.Path(fill=fill_color, stroke=stroke_color, stroke_width=stroke_width)
        path.M(-35 * scale, 0)
        path.Q(-35 * scale, -25 * scale, 0, -20 * scale)
        path.Q(35 * scale, -15 * scale, 35 * scale, 5 * scale)
        path.Q(30 * scale, 25 * scale, 0, 20 * scale)
        path.Q(-35 * scale, 25 * scale, -35 * scale, 0)
        path.Z()
        d.append(path)

    return d


def save_drawing(drawing: draw.Drawing, output_path: str, format: str = "png", dpi: int = 300):
    """
    Save a drawing to file.

    Args:
        drawing: drawsvg.Drawing object
        output_path: Output file path
        format: "png", "svg", or "pdf"
        dpi: Resolution for raster output (default 300 for publication)
    """
    output_path = Path(output_path)

    if format.lower() == "svg":
        drawing.save_svg(str(output_path))
    elif format.lower() == "png":
        # Calculate pixel dimensions for DPI
        scale = dpi / 96  # Default SVG is 96 DPI
        drawing.save_png(str(output_path))
    elif format.lower() == "pdf":
        drawing.save_svg(str(output_path.with_suffix('.svg')))
        # Could add PDF conversion here using cairosvg
    else:
        raise ValueError(f"Unsupported format: {format}")


if __name__ == "__main__":
    # Demo: Generate sample diagrams
    output_dir = Path(__file__).parent.parent / "outputs"
    output_dir.mkdir(exist_ok=True)

    print("Generating medical diagrams...")

    # Heart diagram
    heart = heart_simple(
        highlight_chamber="lv",
        show_labels=True,
        show_vessels=True,
        title="Four-Chamber Heart View"
    )
    heart.save_png(str(output_dir / "heart_diagram.png"))
    print("  -> heart_diagram.png")

    # ECG waveform
    ecg = ecg_wave(
        wave_type="normal",
        show_labels=True,
        title="Normal Sinus Rhythm"
    )
    ecg.save_png(str(output_dir / "ecg_normal.png"))
    print("  -> ecg_normal.png")

    # Conduction system
    conduction = cardiac_conduction(
        highlight_structure="sa_node",
        show_timing=True,
        title="Cardiac Conduction System"
    )
    conduction.save_png(str(output_dir / "conduction_system.png"))
    print("  -> conduction_system.png")

    # Organ icons
    for organ in ["heart", "brain", "lungs", "kidney", "liver"]:
        icon = organ_icon(organ, size=100, style="filled")
        icon.save_png(str(output_dir / f"icon_{organ}.png"))
        print(f"  -> icon_{organ}.png")

    print("\nDone! Check outputs/ directory.")
