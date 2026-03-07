---
name: visual-design-system
description: >-
  **Purpose:** Publication-grade design tokens and utilities for
  Nature/JACC/NEJM quality graphics.
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---
# Visual Design System

**Purpose:** Publication-grade design tokens and utilities for Nature/JACC/NEJM quality graphics.

**Status:** Phase 3.1 In Progress - Manim Animations

---

## Quick Start

```python
from skills.cardiology.visual_design_system.tokens import (
    get_tokens,
    get_color,
    get_accessible_pair,
    validate_contrast,
)

# Get a specific color
navy = get_color("primary.navy")  # "#1e3a5f"

# Get a colorblind-safe pair for treatment vs control
treatment, control = get_accessible_pair("treatment_control")

# Validate accessibility
is_safe = validate_contrast("#1e3a5f", "#ffffff")  # True (9.2:1 ratio)

# Get full tokens object
tokens = get_tokens()
palette = tokens.get_color_palette("categorical")  # 7 colorblind-safe colors
```

---

## Design Philosophy

This system enforces **Nature journal standards** for all visual output:

| Standard | Requirement | How We Enforce |
|----------|-------------|----------------|
| **Fonts** | Helvetica/Arial only | Token system + validation |
| **Font sizes** | 5-8pt for figures | Pre-defined size scale |
| **Contrast** | WCAG AA (4.5:1 min) | Automated validation |
| **Colorblind** | No red-green only | Paul Tol palettes |
| **Resolution** | 300 DPI minimum | Export presets |
| **Shadows** | None in figures | Disabled by default |

---

## Token Categories

### Colors (`tokens/colors.json`)

#### Primary Colors
```python
get_color("primary.navy")    # "#1e3a5f" - Main brand, high contrast
get_color("primary.blue")    # "#2d6a9f" - Data viz, secondary
get_color("primary.teal")    # "#48a9a6" - Accent, highlights
```

#### Semantic Colors
```python
get_color("semantic.success")  # "#2e7d32" - Positive outcomes
get_color("semantic.warning")  # "#e65100" - Caution
get_color("semantic.danger")   # "#c62828" - Negative outcomes
get_color("semantic.neutral")  # "#546e7a" - Control groups
```

#### Data Visualization Palettes
```python
# Categorical (7 colorblind-safe colors)
tokens.get_color_palette("categorical")
# → ['#4477AA', '#66CCEE', '#228833', '#CCBB44', '#EE6677', '#AA3377', '#BBBBBB']

# Sequential (low to high)
tokens.get_color_palette("sequential_blue")
# → ['#deebf7', '#9ecae1', '#4292c6', '#2171b5', '#084594']

# Diverging (negative ← neutral → positive)
tokens.get_color_palette("diverging")
# → ['#2166ac', '#92c5de', '#f7f7f7', '#f4a582', '#b2182b']
```

#### Pre-Validated Accessible Pairs
```python
# Treatment vs Control
t, c = get_accessible_pair("treatment_control")  # ('#0077bb', '#ee7733')

# Benefit vs Risk
b, r = get_accessible_pair("benefit_risk")  # ('#009988', '#cc3311')

# Before vs After
before, after = get_accessible_pair("before_after")  # ('#33bbee', '#ee3377')

# Intervention vs Placebo
i, p = get_accessible_pair("intervention_placebo")  # ('#0077bb', '#bbbbbb')
```

#### Clinical Outcome Colors
```python
tokens.get_clinical_color("mortality")           # "#b2182b"
tokens.get_clinical_color("hospitalization")     # "#ef8a62"
tokens.get_clinical_color("symptom_improvement") # "#67a9cf"
tokens.get_clinical_color("biomarker")           # "#2166ac"
tokens.get_clinical_color("safety_event")        # "#d6604d"
```

#### Forest Plot Colors
```python
colors = tokens.get_forest_plot_colors()
# {
#   "point_estimate": "#1e3a5f",
#   "confidence_interval": "#1e3a5f",
#   "null_line": "#6c757d",
#   "summary_diamond": "#2d6a9f",
#   "heterogeneity_low": "#4daf4a",
#   "heterogeneity_moderate": "#ff7f00",
#   "heterogeneity_high": "#e41a1c"
# }
```

---

### Typography (`tokens/typography.json`)

#### Font Families
```python
tokens.get_font_family("primary")    # "Helvetica, Arial, sans-serif"
tokens.get_font_family("monospace")  # "Courier New, Courier, monospace"
```

#### Font Sizes

**For Figures (Nature standard 5-8pt):**
```python
tokens.get_font_size("figure_elements", "panel_label")  # 8pt - bold lowercase
tokens.get_font_size("figure_elements", "axis_title")   # 7pt
tokens.get_font_size("figure_elements", "axis_tick")    # 6pt
tokens.get_font_size("figure_elements", "legend")       # 6pt
tokens.get_font_size("figure_elements", "caption")      # 7pt
```

**For Infographics:**
```python
tokens.get_font_size("infographic_elements", "headline")     # 24pt
tokens.get_font_size("infographic_elements", "subheadline")  # 14pt
tokens.get_font_size("infographic_elements", "body")         # 10pt
```

**For Social Media:**
```python
tokens.get_font_size("social_media", "carousel_stat")   # 48pt - big numbers
tokens.get_font_size("social_media", "carousel_title")  # 28pt
tokens.get_font_size("social_media", "carousel_body")   # 16pt
```

---

### Spacing (`tokens/spacing.json`)

#### Base Scale (4px grid)
```python
tokens.get_spacing("xs")   # "4px"
tokens.get_spacing("sm")   # "8px"
tokens.get_spacing("md")   # "12px"
tokens.get_spacing("lg")   # "16px"
tokens.get_spacing("xl")   # "20px"
tokens.get_spacing("2xl")  # "24px"
```

#### Layout-Specific Spacing
```python
# Figure layout
tokens.get_layout_spacing("figure_layout", "panel_gap")      # "8px"
tokens.get_layout_spacing("figure_layout", "panel_padding")  # "12px"

# Chart layout
tokens.get_layout_spacing("chart_layout", "title_to_plot")   # "12px"
tokens.get_layout_spacing("chart_layout", "axis_label_offset") # "8px"

# Carousel layout
tokens.get_layout_spacing("carousel_layout", "slide_padding")  # "40px"
```

#### Stroke Widths
```python
tokens.get_stroke_width("hairline")  # "0.5px"
tokens.get_stroke_width("thin")      # "1px"
tokens.get_stroke_width("regular")   # "1.5px"
tokens.get_stroke_width("medium")    # "2px"
```

---

### Shadows (`tokens/shadows.json`)

**Note:** Shadows are disabled by default for scientific figures per journal guidelines.

```python
# For infographics and social media only
tokens.get_shadow("xs")   # "0 1px 2px rgba(0, 0, 0, 0.05)"
tokens.get_shadow("md")   # "0 4px 8px rgba(0, 0, 0, 0.1)"
tokens.get_shadow("none") # Scientific figures - no shadow
```

---

## Validation

### Run Token Validation

```bash
# Full validation
python scripts/token_validator.py

# Contrast report
python scripts/token_validator.py --contrast-report

# JSON output
python scripts/token_validator.py --json
```

### Programmatic Validation

```python
from tokens.index import validate_contrast, get_contrast_ratio

# Check if colors pass WCAG AA
validate_contrast("#1e3a5f", "#ffffff")  # True (4.5:1 minimum)
validate_contrast("#1e3a5f", "#ffffff", level="AAA")  # True (7:1 minimum)

# Get exact ratio
get_contrast_ratio("#1e3a5f", "#ffffff")  # 9.2
```

---

## Integration with Existing Tools

### Plotly (Phase 1.4 - Complete)

The `cardiology-visual-system/scripts/plotly_charts.py` now integrates with design tokens:

```python
# Standard usage - tokens are automatically applied
from cardiology_visual_system.scripts.plotly_charts import (
    create_bar_chart,
    create_forest_plot,
    create_comparison_bars,
    save_chart,
)

# Create chart (uses design tokens automatically)
fig = create_comparison_bars(
    categories=["Primary", "Secondary"],
    group1_values=[12.3, 8.5],
    group2_values=[18.7, 14.2],
    group1_name="Treatment",
    group2_name="Placebo",
    title="Clinical Trial Results"
)

# Save at 300 DPI (publication quality)
save_chart(fig, "results.png")  # Automatically exports at 4x scale
```

#### CLI Usage

```bash
cd skills/cardiology/cardiology-visual-system/scripts

# Generate demo charts with quality report
python plotly_charts.py demo --quality-report

# Export at 300 DPI
python plotly_charts.py demo --png --output-dir ../outputs

# Custom data
python plotly_charts.py bar -d data.csv -o chart.png
```

#### Quality Report

```bash
python plotly_charts.py demo --quality-report
```

Output:
```
📊 PLOTLY PUBLICATION QUALITY REPORT
============================================================
✅ Design Tokens: IMPORTED
✅ Export DPI: 300
✅ Export Scale: 4x
✅ Default Size: 800x600px

📎 Color Palette (Colorblind-Safe):
   [1] #4477AA  [2] #66CCEE  [3] #228833  [4] #CCBB44
   [5] #EE6677  [6] #AA3377  [7] #BBBBBB

🎨 Treatment vs Control Colors:
   Treatment: #0077bb
   Control:   #ee7733

♿ WCAG Accessibility Check:
   Text on background: 15.4:1 ✅ PASS (AA requires 4.5:1)
```

#### Key Features

| Feature | Description |
|---------|-------------|
| **Automatic Token Import** | Loads from `visual-design-system/tokens/` |
| **300 DPI Export** | `scale=4` for publication quality (3200×2400px) |
| **WCAG Validation** | Contrast checks on every export |
| **Colorblind-Safe** | Paul Tol palette, accessible pairs |
| **Modern Plotly API** | Compatible with Plotly 6.x |

#### Direct Token Usage

```python
from tokens.index import get_plotly_template
import plotly.io as pio

# Register the template
pio.templates["publication"] = get_plotly_template()

# Use in figures
fig = px.bar(data, template="publication")
fig.write_image("chart.png", scale=4)  # 300 DPI
```

### Matplotlib

```python
from tokens.index import get_matplotlib_style
import matplotlib.pyplot as plt

plt.rcParams.update(get_matplotlib_style())

# All subsequent plots use publication styling
```

### Pillow (Carousel Generator)

```python
from tokens import get_tokens

tokens = get_tokens()

# Get colors for slides
bg_color = tokens.get_color("backgrounds.light_gray")
text_color = tokens.get_color("text.primary")
accent = tokens.get_color("primary.navy")

# Get dimensions
slide_padding = int(tokens.get_layout_spacing("carousel_layout", "slide_padding").replace("px", ""))
```

---

## Directory Structure

```
visual-design-system/
├── SKILL.md                       # This file
├── tokens/
│   ├── __init__.py                # Package exports
│   ├── index.py                   # Main token loader
│   ├── colors.json                # Color definitions
│   ├── typography.json            # Font specifications
│   ├── spacing.json               # Grid and spacing
│   └── shadows.json               # Shadow definitions
├── scripts/
│   ├── token_validator.py         # WCAG validation
│   └── generate_infographic.py    # Satori Python wrapper
├── satori/                        # Phase 1.2 - React → SVG → PNG
│   ├── renderer.js                # Main renderer (5 templates)
│   ├── package.json
│   └── fonts/                     # Bundled fonts
├── svg_diagrams/                  # Phase 1.3 - Pure Python SVG
│   ├── medical_diagrams.py        # Heart, ECG, organs
│   ├── data_charts.py             # Bar, line, forest plots
│   └── process_flows.py           # Algorithms, journeys
├── components/                    # Phase 2.1 - Component Library
│   ├── base.py                    # Abstract Component class
│   ├── stat_card.py
│   ├── comparison.py
│   ├── forest_plot.py
│   ├── timeline.py
│   ├── process_flow.py
│   └── data_table.py
├── svglue_templates/              # Phase 2.2 - SVG Templates
│   ├── __init__.py
│   ├── template_renderer.py       # lxml-based renderer
│   └── templates/
│       ├── trial_results.svg
│       ├── drug_mechanism.svg
│       ├── patient_stats.svg
│       ├── before_after.svg
│       └── risk_factors.svg
├── arch_diagrams/                 # Phase 2.3 - Architecture Diagrams
│   ├── __init__.py
│   ├── treatment_pathways.py      # HF, ACS, AF clinical algorithms
│   ├── research_flows.py          # CONSORT, PRISMA, methodology
│   └── healthcare_arch.py         # System architecture, data pipelines
├── references/
│   ├── nature_guidelines.md
│   └── color_palettes.md
└── outputs/                       # Generated files
```

---

---

## Satori Pipeline (Phase 1.2)

Generate publication-grade infographics from structured data.

### Available Templates

| Template | Description | Use Case |
|----------|-------------|----------|
| `stat-card` | Big number with context | Trial results, key statistics |
| `comparison` | Side-by-side comparison | Treatment vs control |
| `process-flow` | Step-by-step diagram | Treatment algorithms |
| `trial-summary` | Clinical trial results card | Study summaries |
| `key-finding` | Highlighted finding with icon | Key takeaways |

### Node.js CLI

```bash
cd satori/

# List templates
node renderer.js --list

# Generate stat card
node renderer.js --template stat-card \
  --data '{"value": "26%", "label": "Mortality Reduction", "source": "PARADIGM-HF"}' \
  -o ../outputs/stat-card.png

# Generate comparison
node renderer.js --template comparison \
  --data '{"title": "Treatment vs Control", "left": {"value": "11.4%", "label": "Treatment"}, "right": {"value": "15.6%", "label": "Control"}}' \
  -o ../outputs/comparison.png

# Generate trial summary
node renderer.js --template trial-summary \
  --data '{"trialName": "DAPA-HF", "population": "HFrEF", "intervention": "Dapagliflozin", "primaryEndpoint": "CV death/HF hosp", "result": {"hr": 0.74, "ci": "0.65-0.85", "pValue": "<0.001"}, "nnt": 21}' \
  -o ../outputs/trial.png
```

### Python Interface

```python
from scripts.generate_infographic import (
    generate_stat_card,
    generate_comparison,
    generate_trial_summary,
    generate_process_flow,
    generate_key_finding,
)

# Generate stat card
generate_stat_card(
    "26%", "Mortality Reduction",
    sublabel="HR 0.74, 95% CI 0.65-0.85",
    source="PARADIGM-HF",
    output="outputs/stat-card.png"
)

# Generate comparison
generate_comparison(
    "DAPA-HF Results",
    "11.4%", "Dapagliflozin",
    "15.6%", "Placebo",
    metric="Primary Endpoint",
    source="DAPA-HF Trial",
    output="outputs/comparison.png"
)

# Generate trial summary
generate_trial_summary(
    "DAPA-HF", "HFrEF patients", "Dapagliflozin 10mg",
    "CV death or HF hospitalization",
    0.74, "0.65-0.85", "<0.001",
    nnt=21,
    output="outputs/trial.png"
)

# Generate process flow
generate_process_flow(
    "HFrEF Treatment Algorithm",
    [
        {"title": "Diagnose", "description": "Confirm EF ≤40%"},
        {"title": "Initiate", "description": "Start GDMT"},
        {"title": "Optimize", "description": "Titrate to target"},
    ],
    output="outputs/process.png"
)

# Generate key finding
generate_key_finding(
    "SGLT2 inhibitors reduce HF hospitalization by 30%",
    icon="arrow-down",
    context="Meta-analysis of 5 major trials",
    evidence="Class I, Level A",
    output="outputs/finding.png"
)
```

### Output Formats

- **PNG** (default): 1200×630px at 2x scale (print quality)
- **SVG**: Vector format, saved alongside PNG

### Custom Dimensions

```bash
node renderer.js --template stat-card --data '...' --width 1080 --height 1080 -o square.png
```

```python
generate_stat_card(..., width=1080, height=1080)
```

---

## drawsvg Pipeline (Phase 1.3)

Pure Python SVG generation for medical diagrams, charts, and process flows.
No external dependencies beyond `drawsvg` and `cairosvg`.

### Installation

```bash
pip install drawsvg cairosvg
```

### Available Modules

| Module | Description | Functions |
|--------|-------------|-----------|
| `medical_diagrams` | Heart anatomy, ECG, organs | `heart_simple`, `ecg_wave`, `cardiac_conduction`, `organ_icon` |
| `data_charts` | Charts without Plotly | `bar_chart`, `grouped_bar_chart`, `line_chart`, `forest_plot` |
| `process_flows` | Flowcharts, algorithms | `treatment_algorithm`, `patient_journey`, `study_flow`, `simple_process_flow` |

### Medical Diagrams

```python
# Run from visual-design-system directory
cd drawsvg/
python medical_diagrams.py  # Generates all demo diagrams

# Or import directly
import sys
sys.path.insert(0, '/path/to/visual-design-system')
from drawsvg.medical_diagrams import heart_simple, ecg_wave, cardiac_conduction, organ_icon

# Heart diagram
svg = heart_simple(
    highlight_chamber="lv",  # ra, la, rv, lv
    show_labels=True,
    show_vessels=True,
    title="Four-Chamber Heart View"
)
svg.save_png("heart.png")

# ECG waveform
svg = ecg_wave(
    wave_type="normal",  # normal, afib, stemi, vfib
    show_labels=True,
    title="Normal Sinus Rhythm"
)
svg.save_png("ecg.png")

# Cardiac conduction system
svg = cardiac_conduction(
    highlight_structure="sa_node",  # sa_node, av_node, bundle_his
    show_timing=True,
    title="Cardiac Conduction System"
)
svg.save_png("conduction.png")

# Organ icons for infographics
svg = organ_icon("heart", size=100, style="filled")  # heart, brain, lungs, kidney, liver
svg.save_png("heart_icon.png")
```

### Data Charts

```python
from drawsvg.data_charts import bar_chart, grouped_bar_chart, line_chart, forest_plot

# Bar chart
svg = bar_chart(
    data=[45.2, 32.1, 28.5, 21.3],
    labels=["Treatment A", "Treatment B", "Control", "Placebo"],
    title="Primary Endpoint by Treatment Arm",
    y_label="Event Rate (%)",
    show_values=True,
    error_bars=[(2.1, 2.3), (1.8, 2.0), (1.5, 1.7), (1.2, 1.4)]  # optional
)
svg.save_png("bar_chart.png")

# Grouped bar chart
svg = grouped_bar_chart(
    data=[[45, 32, 28], [38, 29, 25]],  # Two series
    labels=["6 Months", "12 Months", "24 Months"],
    series_names=["Treatment", "Control"],
    title="Event Rates Over Time",
    y_label="Event Rate (%)"
)
svg.save_png("grouped_bar.png")

# Line chart
svg = line_chart(
    data=[
        [(0, 100), (6, 85), (12, 72), (18, 65), (24, 58)],  # Treatment
        [(0, 100), (6, 90), (12, 82), (18, 76), (24, 71)]   # Control
    ],
    series_names=["Treatment", "Control"],
    title="Kaplan-Meier Survival Curve",
    x_label="Months",
    y_label="Survival (%)"
)
svg.save_png("line_chart.png")

# Forest plot
studies = [
    {"name": "DAPA-HF", "estimate": 0.74, "lower": 0.65, "upper": 0.85, "weight": 60},
    {"name": "EMPEROR-Reduced", "estimate": 0.75, "lower": 0.65, "upper": 0.86, "weight": 50},
    {"name": "SOLOIST-WHF", "estimate": 0.67, "lower": 0.52, "upper": 0.85, "weight": 30},
    {"name": "DELIVER", "estimate": 0.82, "lower": 0.73, "upper": 0.92, "weight": 70},
]
svg = forest_plot(
    studies=studies,
    title="SGLT2 Inhibitors in Heart Failure",
    x_label="Hazard Ratio (95% CI)",
    show_pooled=True
)
svg.save_png("forest_plot.png")
```

### Process Flows

```python
from drawsvg.process_flows import treatment_algorithm, patient_journey, study_flow, simple_process_flow

# Treatment algorithm with decision nodes
svg = treatment_algorithm(
    steps=[
        "Patient presents with chest pain",
        "ECG and cardiac biomarkers",
        "Risk stratification",
        "Initiate treatment",
        "Follow-up"
    ],
    decisions=[
        (1, "STEMI?", "Yes", "No"),  # (after_step_index, question, yes_label, no_label)
    ],
    title="Acute Coronary Syndrome Algorithm"
)
svg.save_png("algorithm.png")

# Patient journey timeline
svg = patient_journey(
    stages=[
        {"name": "Diagnosis", "duration": "Day 1", "events": ["ECG", "Blood tests"]},
        {"name": "Treatment", "duration": "Days 2-7", "events": ["Medication", "Monitoring"]},
        {"name": "Recovery", "duration": "Weeks 2-4", "events": ["Cardiac rehab"]},
        {"name": "Follow-up", "duration": "Ongoing", "events": ["Regular checkups"]},
    ],
    title="Heart Failure Patient Journey"
)
svg.save_png("patient_journey.png")

# CONSORT-style study flow
svg = study_flow(
    enrollment=1500,
    randomized=1200,
    groups=[
        {"name": "Treatment", "allocated": 600, "discontinued": 45, "analyzed": 555},
        {"name": "Control", "allocated": 600, "discontinued": 52, "analyzed": 548},
    ],
    title="DAPA-HF Study Flow"
)
svg.save_png("study_flow.png")

# Simple horizontal process flow
svg = simple_process_flow(
    steps=["Screening", "Enrollment", "Randomization", "Treatment", "Analysis"],
    orientation="horizontal"
)
svg.save_png("simple_process.png")
```

### Output Files Generated

```
outputs/
├── heart_diagram.png      # Heart anatomy with chambers
├── ecg_normal.png         # Normal ECG waveform
├── conduction_system.png  # Cardiac conduction
├── icon_heart.png         # Organ icons
├── icon_brain.png
├── icon_lungs.png
├── icon_kidney.png
├── icon_liver.png
├── bar_chart.png          # Data charts
├── grouped_bar_chart.png
├── line_chart.png
├── forest_plot.png        # Meta-analysis
├── treatment_algorithm.png # Process flows
├── patient_journey.png
├── study_flow.png
└── simple_process.png
```

---

## Component Library (Phase 2.1)

A unified, shadcn-inspired component library that wraps all rendering backends (Satori, Plotly, drawsvg) with a consistent Python API.

### Available Components

| Component | Description | Best Backend |
|-----------|-------------|--------------|
| `StatCard` | Big numbers with context | Satori, drawsvg |
| `ComparisonChart` | Side-by-side treatment vs control | Satori, Plotly |
| `ForestPlot` | Meta-analysis visualization | Plotly, drawsvg |
| `Timeline` | Patient journeys, progressions | drawsvg, Satori |
| `ProcessFlow` | Treatment algorithms, workflows | Satori, drawsvg |
| `DataTable` | Publication-ready tables | drawsvg, Plotly |

### Quick Start

```python
from components import StatCard, ForestPlot, Timeline, ComparisonChart, ProcessFlow, DataTable

# StatCard - Key statistics
card = StatCard(
    value="26%",
    label="Mortality Reduction",
    sublabel="HR 0.74, 95% CI 0.65-0.85",
    source="PARADIGM-HF"
)
card.render("stat_card.png")

# ComparisonChart - Treatment vs Control
chart = ComparisonChart(
    title="DAPA-HF Primary Endpoint",
    left_value="11.4%",
    left_label="Dapagliflozin",
    right_value="15.6%",
    right_label="Placebo",
    difference="26% reduction"
)
chart.render("comparison.png")

# ForestPlot - Meta-analysis
studies = [
    {"name": "DAPA-HF", "estimate": 0.74, "lower": 0.65, "upper": 0.85, "weight": 60},
    {"name": "EMPEROR-Reduced", "estimate": 0.75, "lower": 0.65, "upper": 0.86, "weight": 50},
    {"name": "SOLOIST-WHF", "estimate": 0.67, "lower": 0.52, "upper": 0.85, "weight": 30},
]
plot = ForestPlot(
    studies=studies,
    title="SGLT2 Inhibitors in Heart Failure",
    x_label="Hazard Ratio (95% CI)"
)
plot.render("forest.png", backend="plotly")  # or "drawsvg"

# Timeline - Patient Journey
timeline = Timeline(
    title="Heart Failure Patient Journey",
    stages=[
        {"name": "Diagnosis", "duration": "Day 1", "events": ["ECG", "BNP"]},
        {"name": "Treatment", "duration": "Days 2-7", "events": ["GDMT", "Monitor"]},
        {"name": "Recovery", "duration": "Weeks 2-4", "events": ["Cardiac Rehab"]},
        {"name": "Follow-up", "duration": "Ongoing", "events": ["Clinic"]},
    ],
    orientation="horizontal"  # or "vertical"
)
timeline.render("journey.png")

# ProcessFlow - Treatment Algorithm
flow = ProcessFlow(
    title="HFrEF Treatment Algorithm",
    steps=["Diagnose", "Initiate GDMT", "Titrate to Target", "Monitor"],
    style="chevron"  # or "boxes", "circles"
)
flow.render("algorithm.png")

# DataTable - Baseline Characteristics
table = DataTable(
    title="Baseline Characteristics",
    headers=["Characteristic", "Treatment (n=500)", "Control (n=500)", "P-value"],
    rows=[
        ["Age, years", "65.2 ± 12.1", "64.8 ± 11.9", "0.62"],
        ["Male, n (%)", "320 (64%)", "318 (64%)", "0.91"],
        ["Diabetes, n (%)", "175 (35%)", "180 (36%)", "0.74"],
    ],
    alignment=["left", "center", "center", "center"],
    footer="Values are mean ± SD or n (%)"
)
table.render("baseline.png")
```

### Choosing a Backend

Each component can render with multiple backends. Choose based on your needs:

| Backend | Best For | Output |
|---------|----------|--------|
| `satori` | Infographic-style cards, social media | PNG, SVG |
| `plotly` | Interactive charts, data viz | PNG, HTML |
| `drawsvg` | Publication figures, diagrams | PNG, SVG |

```python
# Explicit backend selection
card.render("output.png", backend="satori")  # Infographic style
card.render("output.png", backend="drawsvg") # Publication style

# Auto-selection (uses component's default)
card.render("output.png")  # Uses best backend for component type
```

### Configuration Options

```python
from components.base import RenderConfig

# Custom configuration
config = RenderConfig(
    width=1200,
    height=630,
    quality="print",  # "web" (150 DPI) or "print" (300 DPI)
)

card = StatCard(value="42%", label="Test", config=config)
card.render("high_res.png")
```

---

## SVG Infographic Templates (Phase 2.2)

Template-based SVG generation for common medical infographic layouts.
Uses lxml for direct SVG manipulation with placeholder replacement.

### Available Templates

| Template | Description | Use Case |
|----------|-------------|----------|
| `trial_results` | Clinical trial summary card | Trial publications, presentations |
| `drug_mechanism` | Mechanism of action explainer | Drug education, patient materials |
| `patient_stats` | Patient demographics dashboard | Study characteristics, baseline data |
| `before_after` | Before/after comparison | Intervention effects, treatment outcomes |
| `risk_factors` | Risk factor breakdown | Risk stratification, population analysis |

### CLI Usage

```bash
cd svglue_templates/

# List available templates
python template_renderer.py --list

# Render all templates with demo data
python template_renderer.py --demo-all

# Render specific template with demo data
python template_renderer.py trial_results --demo -o output.svg

# Render with custom data
python template_renderer.py trial_results --data '{"trial_name": "MY-TRIAL", "primary_hr": "0.75"}' -o output.svg

# Export as PNG (2x scale = 1600x1200)
python template_renderer.py trial_results --demo --png --scale 2 -o output.svg

# High quality export (3x scale for print)
python template_renderer.py trial_results --demo --png --scale 3 -o output.svg
```

### Python API

```python
from svglue_templates.template_renderer import render_template, get_demo_data, list_templates

# List available templates
for tpl in list_templates():
    print(f"{tpl['name']}: {tpl['description']}")

# Render with demo data
demo_data = get_demo_data("trial_results")
svg_content = render_template("trial_results", demo_data)

# Render with custom data
custom_data = {
    "trial_name": "PARADIGM-HF",
    "trial_subtitle": "Sacubitril/Valsartan vs Enalapril in HFrEF",
    "primary_hr": "0.80",
    "primary_ci": "95% CI: 0.73-0.87",
    "primary_p": "P < 0.001",
    "stat1_value": "8,442",
    "stat1_label": "Patients enrolled",
    "source": "McMurray JJV et al. N Engl J Med. 2014",
}
svg_content = render_template("trial_results", custom_data)

# Save outputs
from svglue_templates.template_renderer import save_svg, save_png
from pathlib import Path

save_svg(svg_content, Path("trial_results.svg"))
save_png(svg_content, Path("trial_results.svg"), scale=2)  # 1600x1200 PNG
```

### Template Data Fields

#### trial_results

| Field | Description | Example |
|-------|-------------|---------|
| `trial_name` | Trial name | "DAPA-HF Trial" |
| `trial_subtitle` | Description | "Dapagliflozin in HFrEF" |
| `primary_endpoint_name` | Primary outcome | "CV Death or HF Hospitalization" |
| `primary_hr` | Hazard ratio | "0.74" |
| `primary_ci` | Confidence interval | "95% CI: 0.65-0.85" |
| `primary_p` | P-value | "P < 0.001" |
| `secondary_endpoint_name` | Secondary outcome | "All-Cause Mortality" |
| `stat1_value` - `stat4_value` | Key statistics | "4,744", "18.2", "21", "4.9%" |
| `stat1_label` - `stat4_label` | Stat labels | "Patients enrolled" |
| `source` | Citation | "McMurray JJV et al. NEJM 2019" |

#### drug_mechanism

| Field | Description | Example |
|-------|-------------|---------|
| `drug_name` | Drug name | "Dapagliflozin (SGLT2i)" |
| `drug_class` | Drug class | "SGLT2 Inhibitor" |
| `step1_title` - `step4_title` | Pathway steps | "Oral Administration" |
| `target_name` | Primary target | "SGLT2 Receptor" |
| `target_mechanism` | MOA description | "Blocks SGLT2 in kidney" |
| `effect1` - `effect4` | Clinical effects | "Reduced HF hospitalization" |
| `bioavail_value` | Bioavailability | "78%" |
| `halflife_value` | Half-life | "12.9h" |

#### patient_stats

| Field | Description | Example |
|-------|-------------|---------|
| `title` | Dashboard title | "PATIENT DEMOGRAPHICS" |
| `total_patients` | Total N | "4,744" |
| `treatment_n` | Treatment arm N | "2,373" |
| `control_n` | Control arm N | "2,371" |
| `mean_age` | Mean age | "66.3 years" |
| `male_pct` | Male percentage | "77%" |
| `diabetes_pct` | Diabetes prevalence | "42%" |
| `egfr_value` | eGFR value | "66 mL/min/1.73m2" |

#### before_after

| Field | Description | Example |
|-------|-------------|---------|
| `title` | Comparison title | "TREATMENT EFFECTS" |
| `metric1_label` | Metric name | "HF HOSPITALIZATION" |
| `metric1_before` | Baseline value | "9.8%" |
| `metric1_after` | Follow-up value | "5.6%" |
| `metric1_change` | Change | "-4.2%" |
| `stat1_value` | Summary stat | "18 mo" |
| `stat2_value` | Response rate | "74%" |

#### risk_factors

| Field | Description | Example |
|-------|-------------|---------|
| `title` | Dashboard title | "RISK PROFILE" |
| `overall_risk_score` | Overall risk | "HIGH" |
| `overall_risk_value` | Risk quantification | "5-year risk: 18.5%" |
| `rf1_name` - `rf8_name` | Risk factor names | "Hypertension" |
| `rf1_pct` - `rf8_pct` | Prevalence | "72%" |
| `high_pct` | High risk % | "35%" |
| `moderate_pct` | Moderate risk % | "40%" |

### Output Files

```
outputs/
├── demo_trial_results.svg      # Trial summary infographic
├── demo_trial_results.png      # 1600x1200 PNG (2x scale)
├── demo_drug_mechanism.svg     # MOA explainer
├── demo_drug_mechanism.png
├── demo_patient_stats.svg      # Demographics dashboard
├── demo_patient_stats.png
├── demo_before_after.svg       # Before/after comparison
├── demo_before_after.png
├── demo_risk_factors.svg       # Risk factor breakdown
└── demo_risk_factors.png
```

---

## Architecture Diagrams (Phase 2.3)

Create publication-grade architecture diagrams using the `mingrammer/diagrams` library.
Perfect for clinical pathways, research flows, and healthcare system visualizations.

### Installation

```bash
pip install diagrams
brew install graphviz  # macOS - required for diagram rendering
```

### Available Modules

| Module | Description | Functions |
|--------|-------------|-----------|
| `treatment_pathways` | Clinical algorithms | `create_heart_failure_pathway`, `create_acs_pathway`, `create_af_pathway` |
| `research_flows` | Study methodology | `create_consort_diagram`, `create_prisma_diagram`, `create_methodology_flow` |
| `healthcare_arch` | System architecture | `create_healthcare_system`, `create_cardiology_department`, `create_data_pipeline` |

### Treatment Pathways

Clinical guideline-based treatment algorithms with color-coded decision points.

```python
from arch_diagrams.treatment_pathways import (
    create_heart_failure_pathway,
    create_acs_pathway,
    create_af_pathway,
    create_treatment_pathway,
)

# Heart Failure (HFrEF) Algorithm - ACC/AHA Guidelines
output = create_heart_failure_pathway(
    output_path="outputs/hf_pathway",
    format="png"
)
# Generates: GDMT initiation → ACEi/ARNi → Beta-blocker → MRA → SGLT2i → Device therapy

# Acute Coronary Syndrome (ACS) Algorithm
output = create_acs_pathway(
    output_path="outputs/acs_pathway",
    format="png"
)
# Generates: Chest pain → ECG → STEMI/NSTEMI pathways → PCI/Fibrinolysis → Medical therapy

# Atrial Fibrillation (AF) Algorithm
output = create_af_pathway(
    output_path="outputs/af_pathway",
    format="png"
)
# Generates: Diagnosis → CHA2DS2-VASc → Anticoagulation → Rate vs Rhythm control

# Custom treatment pathway
output = create_treatment_pathway(
    title="Custom Protocol",
    steps=[
        {"name": "Assessment", "type": "assessment"},
        {"name": "Decision Point", "type": "decision"},
        {"name": "Treatment A", "type": "treatment"},
        {"name": "Outcome", "type": "outcome"},
    ],
    output_path="outputs/custom_pathway",
    format="png"
)
```

### Research Flows

Standard research methodology diagrams for publications.

```python
from arch_diagrams.research_flows import (
    create_consort_diagram,
    create_prisma_diagram,
    create_methodology_flow,
    create_study_flow,
)

# CONSORT Diagram - Clinical Trial Flow
output = create_consort_diagram(
    enrolled=500,
    randomized=400,
    treatment_n=200,
    control_n=200,
    treatment_completed=180,
    control_completed=175,
    treatment_analyzed=200,  # ITT
    control_analyzed=200,
    output_path="outputs/consort",
    format="png"
)

# PRISMA Diagram - Systematic Review Flow
output = create_prisma_diagram(
    records_identified=1500,
    duplicates_removed=200,
    records_screened=1300,
    records_excluded=800,
    full_text_assessed=500,
    full_text_excluded=350,
    studies_included=150,
    output_path="outputs/prisma",
    format="png"
)

# Custom Methodology Flow
output = create_methodology_flow(
    title="Study Methodology",
    phases=[
        {"name": "Phase 1: Design", "steps": ["Literature Review", "Protocol Development"]},
        {"name": "Phase 2: Data Collection", "steps": ["Recruitment", "Assessment"]},
        {"name": "Phase 3: Analysis", "steps": ["Statistical Analysis", "Sensitivity Analysis"]},
        {"name": "Phase 4: Reporting", "steps": ["Manuscript", "Publication"]},
    ],
    output_path="outputs/methodology",
    format="png"
)
```

### Healthcare Architecture

System-level diagrams for healthcare organizations and data pipelines.

```python
from arch_diagrams.healthcare_arch import (
    create_healthcare_system,
    create_cardiology_department,
    create_data_pipeline,
)

# Hospital System Architecture
output = create_healthcare_system(
    output_path="outputs/hospital_system",
    format="png"
)
# Generates: Patient entry → Clinical services → Support services → Data systems

# Cardiology Department Structure
output = create_cardiology_department(
    output_path="outputs/cardio_dept",
    format="png"
)
# Generates: Referral → Clinics → Diagnostics → Interventional → Cardiac Surgery → CCU

# Clinical Data Pipeline
output = create_data_pipeline(
    title="Cardiology Data Pipeline",
    sources=["EHR/EMR", "Lab Results", "PACS", "Wearables"],
    processing=["Extraction", "Cleaning", "NLP", "Feature Engineering"],
    storage=["Data Lake", "Clinical DW", "FHIR Server"],
    outputs=["Dashboards", "ML Models", "Research Analytics"],
    output_path="outputs/data_pipeline",
    format="png"
)
```

### Output Files (Phase 2.3)

```
outputs/
├── heart_failure_pathway.png    (67KB) - HFrEF treatment algorithm
├── acs_pathway.png              (82KB) - ACS management pathway
├── af_pathway.png               (79KB) - AF treatment algorithm
├── consort_diagram.png          (52KB) - Clinical trial CONSORT flow
├── prisma_diagram.png           (47KB) - Systematic review PRISMA flow
├── methodology_flow.png         (31KB) - Study methodology
├── healthcare_system.png        (55KB) - Hospital system architecture
├── cardiology_department.png    (77KB) - Cardiology dept structure
└── data_pipeline.png            (56KB) - Clinical data pipeline
```

### Color Coding

All diagrams use consistent, publication-quality colors from design tokens:

| Element Type | Color | Description |
|--------------|-------|-------------|
| **Assessment** | Blue (#2d6a9f) | Initial evaluations, diagnostics |
| **Decision** | Orange (#e65100) | Decision points, stratification |
| **Treatment** | Green (#2e7d32) | Active interventions, therapies |
| **Outcome** | Teal (#2d7a77) | Results, endpoints |
| **Danger/Critical** | Red (#c62828) | ICU, emergency, exclusions |
| **Administrative** | Navy (#1e3a5f) | Data systems, analysis |

### CLI Usage

```bash
cd skills/cardiology/visual-design-system

# Generate all treatment pathways
python arch_diagrams/treatment_pathways.py

# Generate all research flows
python arch_diagrams/research_flows.py

# Generate all healthcare architecture diagrams
python arch_diagrams/healthcare_arch.py
```

---

## Manim Animations (Phase 3.1)

Educational animations for mechanisms, survival curves, and ECG fundamentals.

### Installation

```bash
python -m venv skills/cardiology/visual-design-system/.venv-manim
skills/cardiology/visual-design-system/.venv-manim/bin/python -m pip install manim
```

### Location

```
skills/cardiology/visual-design-system/
├── manim_animations/
│   ├── scenes.py       # Mechanism, Kaplan-Meier, ECG scenes
│   └── theme.py        # Tokens-based colors + fonts
└── scripts/
    └── render_manim.py # CLI wrapper for Manim renders
```

### Sample Scenes (see catalog for full list)

| Key | Scene Class | Description |
|-----|-------------|-------------|
| `mechanism` | `MechanismOfActionScene` | 4-step mechanism flow with outcome callout |
| `kaplan_meier` | `KaplanMeierScene` | Stepwise survival curves + HR label |
| `ecg_wave` | `ECGWaveScene` | Normal sinus rhythm waveform with labels |

### Scene Catalog

All scenes are registered in `manim_animations/scene_catalog.json`. Use the CLI to list:

```bash
python scripts/render_manim.py --list
```

Categories include: cardiometabolic, acs_cad, arrhythmia, imaging_dx, statistics, devices, anatomy, core.

### CLI Usage

```bash
cd skills/cardiology/visual-design-system

# Render the mechanism animation (medium quality)
python scripts/render_manim.py mechanism --quality m --format mp4

# Render Kaplan-Meier (high quality, preview)
python scripts/render_manim.py kaplan_meier --quality h --preview

# Use a dedicated Manim venv
python scripts/render_manim.py ecg_wave --quality l --manim-bin skills/cardiology/visual-design-system/.venv-manim
```

### Notes

- Manim uses the design tokens for colors and font defaults.
- Outputs are written to `skills/cardiology/visual-design-system/outputs/manim`.
- Set `MANIM_VENV` or pass `--manim-bin` to target the dedicated venv.
- Carousel integration: slides with `animation_scene` route to Manim via `carousel-generator-v2` visual router.
- The render CLI uses the scene catalog, so new scenes only need a catalog entry.

---

## Roadmap

| Phase | Status | Components |
|-------|--------|------------|
| **1.1 Design Tokens** | ✅ Complete | colors, typography, spacing, shadows, validation |
| **1.2 Satori Integration** | ✅ Complete | React → SVG → PNG pipeline, 5 templates |
| **1.3 drawsvg Integration** | ✅ Complete | medical_diagrams, data_charts, process_flows |
| **1.4 Plotly Standardization** | ✅ Complete | 300 DPI export, WCAG validation, colorblind-safe |
| **2.1 Component Library** | ✅ Complete | StatCard, ComparisonChart, ForestPlot, Timeline, ProcessFlow, DataTable |
| **2.2 SVG Templates** | ✅ Complete | trial_results, drug_mechanism, patient_stats, before_after, risk_factors |
| **2.3 Architecture Diagrams** | ✅ Complete | treatment_pathways, research_flows, healthcare_arch (9 diagram types) |
| **3.1 Manim Animations** | 🚧 In progress | Educational animations |
| **4.1 Visual Router Upgrade** | Pending | Content-type routing |

---

## References

- [Nature Figure Guidelines](https://www.nature.com/nature/for-authors/preparing-your-submission)
- [Paul Tol's Colorblind-Safe Palettes](https://personal.sron.nl/~pault/)
- [WCAG 2.1 Contrast Requirements](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum)
- [Satori Documentation](https://github.com/vercel/satori)

---

*Last Updated: 2026-01-01*
*Maintainer: Dr. Shailesh Singh*
