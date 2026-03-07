# G2 Grammar-Based Charts

**Purpose:** Declarative, grammar-based charting using AntV G2 for complex medical visualizations.

**Status:** ✅ Production Ready

**Repository:** https://github.com/antvis/G2 (12.5k ⭐)

---

## Quick Start

```python
from g2_charts.medical_grammars import forest_plot_grammar
from g2_charts.grammar_renderer import G2Chart

# Create grammar specification
grammar = forest_plot_grammar(
    studies=['DAPA-HF', 'EMPEROR-Reduced'],
    estimates=[0.74, 0.75],
    lower_ci=[0.65, 0.65],
    upper_ci=[0.85, 0.86],
    title="SGLT2i Trials"
)

# Render chart
chart = G2Chart(width=800, height=600)
chart.grammar = grammar
chart.render('forest.png')
```

---

## What is Grammar-Based Charting?

Instead of imperative "draw this, then this", you declare **what the data means**:

```python
# Imperative (Plotly style)
fig = go.Figure()
fig.add_trace(go.Scatter(x=..., y=...))
fig.add_trace(go.Bar(x=..., y=...))
fig.update_layout(...)

# Declarative (G2 grammar)
grammar = {
    'data': [...],
    'marks': [
        {'type': 'point', 'encode': {'x': 'time', 'y': 'survival'}},
        {'type': 'line', 'encode': {'x': 'time', 'y': 'survival'}}
    ],
    'scales': {'y': {'domain': [0, 1]}}
}
```

**Benefits:**
- Composable: Combine multiple marks/layers
- Reproducible: Grammar specs are JSON (version control, templates)
- Flexible: Easy to modify specific aspects
- Publication-grade: Based on Leland Wilkinson's Grammar of Graphics

---

## When to Use G2 vs Plotly

### Use G2 When:
✅ **Complex multi-layer compositions** (e.g., forest plot with CI bars + diamonds)
✅ **Custom chart types** not available in Plotly
✅ **Multi-panel figures** with faceting
✅ **Template-driven workflows** (same grammar, different data)
✅ **Publication figures** requiring precise control
✅ **Research papers** with custom requirements

### Use Plotly When:
✅ **Standard charts** (bar, line, scatter)
✅ **Interactive dashboards** (web-based, hover, zoom)
✅ **Quick prototyping** (simpler API)
✅ **Built-in chart types** work out of the box

### Decision Tree:
```
Does Plotly have a built-in chart type that works?
├─ YES → Use Plotly (faster, simpler)
└─ NO → Do you need custom composition?
    ├─ YES → Use G2 (grammar-based)
    └─ NO → Use drawsvg (pure Python SVG)
```

---

## Available Medical Grammars

### 1. Forest Plot
```python
from medical_grammars import forest_plot_grammar

grammar = forest_plot_grammar(
    studies=['Study A', 'Study B', 'Study C'],
    estimates=[0.80, 0.74, 0.92],
    lower_ci=[0.73, 0.65, 0.86],
    upper_ci=[0.87, 0.85, 0.99],
    weights=[84, 60, 35],  # For sizing
    null_value=1.0,
    log_scale=True,
    title="Meta-Analysis Results"
)
```

**Features:**
- Confidence interval bars with transparency
- Diamond-shaped point estimates sized by weight
- Null hypothesis line (dashed)
- Log scale for ratio metrics
- Automatic transposition (studies on y-axis)

### 2. Kaplan-Meier Survival Curve
```python
from medical_grammars import kaplan_meier_grammar

grammar = kaplan_meier_grammar(
    time_data=[
        [0, 6, 12, 18, 24],  # Treatment
        [0, 6, 12, 18, 24]   # Control
    ],
    survival_data=[
        [1.0, 0.90, 0.82, 0.78, 0.75],  # Treatment
        [1.0, 0.85, 0.72, 0.65, 0.58]   # Control
    ],
    group_names=['Treatment', 'Control'],
    title="Overall Survival"
)
```

**Features:**
- Step function (hv shape) for survival curves
- Shaded area below curves (10% opacity)
- Colorblind-safe treatment/control colors
- Y-axis fixed at [0, 1]

### 3. Grouped Bar Chart
```python
from medical_grammars import grouped_comparison_grammar

grammar = grouped_comparison_grammar(
    categories=['Primary', 'Secondary', 'Safety'],
    groups=['Treatment', 'Placebo'],
    values=[
        [12.3, 8.5, 3.2],  # Treatment
        [18.7, 14.2, 2.8]   # Placebo
    ],
    title="Trial Results"
)
```

**Features:**
- Dodged bars for side-by-side comparison
- Colorblind-safe group colors
- Rounded corners (2px radius)

### 4. Multi-Panel Figure
```python
from medical_grammars import multi_panel_grammar

grammar = multi_panel_grammar(
    data=[
        {'x': 0, 'y': 10, 'category': 'A', 'panel': 'Baseline'},
        {'x': 1, 'y': 12, 'category': 'A', 'panel': 'Baseline'},
        {'x': 0, 'y': 15, 'category': 'A', 'panel': 'Follow-up'},
        # ...
    ],
    x_field='x',
    y_field='y',
    color_field='category',
    facet_field='panel',
    title="Longitudinal Analysis"
)
```

**Features:**
- Faceted subplots (small multiples)
- Points + smoothed lines
- Shared scales across panels
- Categorical color palette

### 5. Scatter with Regression
```python
from medical_grammars import scatter_regression_grammar

grammar = scatter_regression_grammar(
    x_data=[25, 30, 35, 40, 45],
    y_data=[2800, 2200, 1800, 1200, 900],
    regression_line=True,
    title="LVEF vs NT-proBNP Correlation"
)
```

**Features:**
- Scatter points with transparency
- Optional regression line (dashed)
- Optional grouping by category

### 6. Heatmap
```python
from medical_grammars import heatmap_grammar

grammar = heatmap_grammar(
    data=[
        {'marker1': 'BNP', 'marker2': 'Troponin', 'correlation': 0.65},
        # ...
    ],
    x_field='marker1',
    y_field='marker2',
    value_field='correlation',
    title="Biomarker Correlations"
)
```

**Features:**
- Cell-based heatmap
- Sequential color scale
- White gridlines between cells

---

## CLI Usage

### Quick Commands

```bash
# List available templates
python g2_cli.py list-templates

# Generate forest plot
python g2_cli.py forest \
  --studies "DAPA-HF,EMPEROR-Reduced,VICTORIA" \
  --estimates "0.74,0.75,0.90" \
  --lower "0.65,0.65,0.82" \
  --upper "0.85,0.86,0.98" \
  -o forest.png

# Generate Kaplan-Meier from data file
python g2_cli.py kaplan --data survival.json -o km.svg --format svg

# Generate grouped bars from data
python g2_cli.py grouped --data trial_results.json -o bars.png

# Generate all demo charts
python g2_cli.py demo --all
```

### Data File Formats

**Kaplan-Meier (survival.json):**
```json
{
  "groups": ["Treatment", "Control"],
  "time": [
    [0, 6, 12, 18, 24],
    [0, 6, 12, 18, 24]
  ],
  "survival": [
    [1.0, 0.90, 0.82, 0.78, 0.75],
    [1.0, 0.85, 0.72, 0.65, 0.58]
  ]
}
```

**Grouped Bars (trial_results.json):**
```json
{
  "categories": ["Primary", "Secondary", "Safety"],
  "groups": ["Treatment", "Placebo"],
  "values": [
    [12.3, 8.5, 3.2],
    [18.7, 14.2, 2.8]
  ]
}
```

---

## Custom Grammars

Build custom charts from scratch using the grammar API:

```python
from grammar_renderer import G2Chart

chart = G2Chart(width=800, height=600)

# Set data
chart.data([
    {'category': 'A', 'value': 23},
    {'category': 'B', 'value': 45},
    {'category': 'C', 'value': 31}
])

# Add interval mark (bars)
chart.add_mark(
    'interval',
    encode={'x': 'category', 'y': 'value'},
    style={'fill': '#1e3a5f', 'radius': 2}
)

# Configure scales
chart.scale('y', {'nice': True})

# Set axes
chart.axis('x', title='Category')
chart.axis('y', title='Value', grid=True)

# Render
chart.render('custom.png')
```

### Grammar Components

| Component | Description | Example |
|-----------|-------------|---------|
| **data** | Chart data | `chart.data([{...}, {...}])` |
| **marks** | Geometry layers | `chart.add_mark('point', encode={...})` |
| **scales** | Data-to-visual mapping | `chart.scale('y', {'type': 'log'})` |
| **coordinate** | Coordinate transformation | `chart.coordinate('transpose')` |
| **axes** | Axis configuration | `chart.axis('x', title='Time')` |
| **legend** | Legend configuration | `chart.legend(position='top')` |

### Mark Types

| Mark | Description | Use Case |
|------|-------------|----------|
| `point` | Scatter points | Scatter plots, estimates |
| `line` | Lines | Trends, survival curves |
| `interval` | Bars/rectangles | Bar charts, CI intervals |
| `area` | Filled areas | Area under curve |
| `cell` | Grid cells | Heatmaps |
| `text` | Text labels | Annotations |
| `rect` | Rectangles | Custom shapes |

---

## Integration with Visual System

G2 charts automatically use design tokens from `visual-design-system`:

```python
# Colors (from tokens/colors.json)
COLORS = {
    'primary': '#1e3a5f',
    'categorical': ['#4477AA', '#66CCEE', '#228833', ...],
    'treatment_control': ['#0077bb', '#ee7733']
}

# Typography (from tokens/typography.json)
TYPOGRAPHY = {
    'family': 'Helvetica, Arial, sans-serif',
    'sizes': {
        'title': 14,
        'axis': 8,
        'legend': 9
    }
}

# Spacing (from tokens/spacing.json)
PADDING = [40, 60, 40, 60]  # top, right, bottom, left
```

All grammars apply these tokens automatically for consistency with Plotly, drawsvg, and Satori outputs.

---

## Output Formats

### PNG (Default)
```python
chart.render('output.png', format='png')
```
- Publication quality
- 800×600px default (configurable)
- Suitable for papers, presentations

### SVG (Vector)
```python
chart.render('output.svg', format='svg')
```
- Scalable vector graphics
- Editable in Illustrator/Inkscape
- Smaller file size
- Perfect for journals requiring vector formats

---

## Demo Charts

Generate all demo charts:

```bash
cd skills/cardiology/visual-design-system/g2_charts
python examples/demo_charts.py --all
```

**Generated:**
1. `demo_forest_plot.png` - Meta-analysis with 5 trials
2. `demo_kaplan_meier.png` - Treatment vs control survival
3. `demo_grouped_bars.png` - Trial outcomes comparison
4. `demo_scatter.png` - EF vs BNP correlation
5. `demo_heatmap.png` - Biomarker correlation matrix

Plus grammar JSON files for each chart (for reference/modification).

---

## Directory Structure

```
g2_charts/
├── SKILL.md                       # This file
├── package.json                   # npm dependencies
├── node_modules/                  # G2, canvas, jsdom
├── renderer.js                    # Node.js renderer
├── grammar_renderer.py            # Python API
├── medical_grammars.py            # Pre-built grammars
├── g2_cli.py                      # CLI interface
├── templates/                     # JSON grammar templates
│   ├── forest_plot.json
│   ├── kaplan_meier.json
│   ├── grouped_bars.json
│   ├── multi_panel.json
│   └── consort_flow.json
├── examples/
│   └── demo_charts.py             # Demo generator
└── outputs/                       # Generated charts
    ├── demo_forest_plot.png
    ├── demo_kaplan_meier.png
    └── ...
```

---

## G2 vs Plotly Comparison

| Feature | G2 | Plotly |
|---------|----|----|
| **API Style** | Declarative (grammar) | Imperative (method calls) |
| **Composability** | ⭐⭐⭐⭐⭐ Excellent | ⭐⭐⭐ Good |
| **Custom Charts** | ⭐⭐⭐⭐⭐ Full control | ⭐⭐⭐ Limited by built-ins |
| **Interactivity** | ⭐⭐ Static exports | ⭐⭐⭐⭐⭐ Built-in zoom/hover |
| **Learning Curve** | ⭐⭐ Steeper (grammar concepts) | ⭐⭐⭐⭐ Easier (familiar API) |
| **Speed** | ⭐⭐⭐⭐ Fast | ⭐⭐⭐⭐ Fast |
| **File Size** | ⭐⭐⭐⭐ Small | ⭐⭐⭐ Larger |
| **Publication Quality** | ⭐⭐⭐⭐⭐ Excellent | ⭐⭐⭐⭐ Very good |
| **Forest Plots** | ⭐⭐⭐⭐⭐ Native grammar | ⭐⭐⭐ Manual construction |
| **Multi-Panel** | ⭐⭐⭐⭐⭐ Faceting built-in | ⭐⭐⭐ Subplots |

**Bottom Line:**
- **Simple charts:** Plotly (faster, easier)
- **Complex compositions:** G2 (more flexible, composable)
- **Both work:** Use whichever you prefer

---

## Troubleshooting

### Node.js not found
```bash
# Install Node.js
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### npm packages not installed
```bash
cd skills/cardiology/visual-design-system/g2_charts
npm install
```

### Canvas rendering errors
```bash
# Install canvas dependencies (Linux)
sudo apt-get install build-essential libcairo2-dev libpango1.0-dev libjpeg-dev libgif-dev librsvg2-dev

# Reinstall canvas
npm rebuild canvas
```

### Python import errors
```bash
# Ensure you're in the right directory
cd skills/cardiology/visual-design-system/g2_charts

# Or add to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:/path/to/visual-design-system/g2_charts"
```

---

## Grammar Cookbook

### Example 1: Add Annotations to Forest Plot

```python
grammar = forest_plot_grammar(...)

# Add vertical line at HR=1.5
grammar['annotations'] = [
    {
        'type': 'line',
        'encode': {
            'x': 1.5,
            'style': {
                'stroke': '#ff9800',
                'strokeWidth': 2,
                'lineDash': [4, 4]
            }
        }
    }
]
```

### Example 2: Customize Colors

```python
grammar = kaplan_meier_grammar(...)

# Override default colors
grammar['scales']['color'] = {
    'range': ['#e74c3c', '#3498db', '#2ecc71']
}
```

### Example 3: Add Confidence Bands

```python
chart.add_mark(
    'area',
    encode={
        'x': 'time',
        'y': ['lower_ci', 'upper_ci'],
        'color': 'group'
    },
    style={'fillOpacity': 0.2}
)
```

---

## References

- [AntV G2 Documentation](https://g2.antv.antgroup.com/en)
- [Grammar of Graphics (Wilkinson)](https://www.springer.com/gp/book/9780387245447)
- [Design Tokens](../tokens/)
- [Plotly Charts](../../cardiology-visual-system/scripts/plotly_charts.py)

---

*Last Updated: 2026-01-01*
*Maintainer: Dr. Shailesh Singh*
