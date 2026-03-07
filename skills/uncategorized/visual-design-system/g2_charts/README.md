# AntV G2 Grammar-Based Charts

Declarative charting for complex medical visualizations using AntV G2.

## Quick Start

```bash
# Install dependencies (one-time)
cd skills/cardiology/visual-design-system/g2_charts
npm install

# Generate demo charts
python examples/demo_charts.py --all

# Generate forest plot
python g2_cli.py forest \
  --studies "DAPA-HF,EMPEROR-Reduced" \
  --estimates "0.74,0.75" \
  --lower "0.65,0.65" \
  --upper "0.85,0.86" \
  -o forest.png
```

## Python API

```python
from g2_charts.medical_grammars import forest_plot_grammar
from g2_charts.grammar_renderer import G2Chart

grammar = forest_plot_grammar(
    studies=['Study A', 'Study B'],
    estimates=[0.74, 0.82],
    lower_ci=[0.65, 0.72],
    upper_ci=[0.85, 0.93]
)

chart = G2Chart(width=800, height=600)
chart.grammar = grammar
chart.render('forest.png')
```

## Available Grammars

1. **forest_plot_grammar** - Meta-analysis forest plots
2. **kaplan_meier_grammar** - Survival curves
3. **grouped_comparison_grammar** - Treatment comparisons
4. **multi_panel_grammar** - Faceted figures
5. **scatter_regression_grammar** - Correlation plots
6. **heatmap_grammar** - Correlation matrices

## When to Use

✅ **Use G2 for:**
- Complex multi-layer compositions (forest plots with CI + diamonds)
- Custom chart types not in Plotly
- Multi-panel figures with faceting
- Template-driven workflows
- Publication figures requiring precise control

✅ **Use Plotly for:**
- Standard charts (bar, line, scatter)
- Interactive dashboards
- Quick prototyping

## Documentation

See [SKILL.md](./SKILL.md) for complete documentation.

## Outputs

Charts are rendered to `outputs/` directory:
- PNG (default): Publication quality, 800×600px
- SVG: Vector format, scalable

## CLI Reference

```bash
# List templates
python g2_cli.py list-templates

# Forest plot
python g2_cli.py forest --studies "A,B" --estimates "0.8,0.7" \
  --lower "0.7,0.6" --upper "0.9,0.8" -o forest.png

# Kaplan-Meier
python g2_cli.py kaplan --data survival.json -o km.svg --format svg

# Grouped bars
python g2_cli.py grouped --data trial_results.json -o bars.png

# All demos
python g2_cli.py demo --all
```

## File Structure

```
g2_charts/
├── renderer.js              # Node.js G2 renderer
├── grammar_renderer.py      # Python API
├── medical_grammars.py      # Pre-built grammars
├── g2_cli.py                # CLI interface
├── templates/               # JSON grammar templates
├── examples/                # Demo charts
└── outputs/                 # Generated files
```

---

**Part of:** Visual Design System → Cardiology Skills → Integrated Content OS
