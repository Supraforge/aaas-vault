# AntV Infographic Integration

Template-driven medical infographics for the Integrated Content OS

---

## Quick Start (30 seconds)

```bash
# List templates
python scripts/antv_cli.py list

# Render an infographic
python scripts/antv_cli.py render --template mechanism_of_action

# Open the generated HTML in your browser → Download SVG/PNG
```

---

## What This Does

Creates professional medical infographics using 200+ AntV templates:

- **11 medical presets** for common cardiology content
- **Template-driven** for consistent branding
- **AI-optimized** declarative syntax
- **SVG/PNG export** for publications
- **Zero cost** to use

---

## Documentation

| Document | Purpose |
|----------|---------|
| `SKILL.md` | **Complete documentation** (read this first) |
| `TEMPLATE_CATALOG.md` | **Template reference** with examples |
| `INTEGRATION_REPORT.md` | **Technical details** and implementation |
| `README.md` | This file - quick orientation |

---

## Common Tasks

### List Templates
```bash
python scripts/antv_cli.py list --verbose
```

### Render Template
```bash
python scripts/antv_cli.py render --template trial_result_simple --output trial.html
```

### Python API
```python
from scripts.antv_renderer import render_template
output = render_template('mechanism_of_action', 'moa.html')
```

### Visual Router
```python
from cardiology_visual_system.scripts.visual_router import VisualRouter
router = VisualRouter()
tool = router.route("Create a trial timeline infographic")  # → 'antv'
```

---

## Available Templates

1. `trial_result_simple` - Trial phases
2. `mechanism_of_action` - Drug MOA steps
3. `treatment_comparison` - Side-by-side comparison
4. `patient_journey` - Care pathway
5. `guideline_recommendations` - Guideline classes
6. `dosing_schedule` - Medication titration
7. `safety_profile` - Adverse events
8. `biomarker_progression` - Lab trends
9. `trial_endpoints` - Primary/secondary outcomes
10. `risk_stratification` - Risk levels
11. `diagnostic_pathway` - Diagnostic workflow

See `TEMPLATE_CATALOG.md` for detailed descriptions and examples.

---

## File Structure

```
antv_infographic/
├── README.md                   # This file
├── SKILL.md                    # Full documentation
├── TEMPLATE_CATALOG.md         # Template reference
├── INTEGRATION_REPORT.md       # Technical report
├── package.json                # NPM config
├── scripts/
│   ├── antv_cli.py             # CLI tool (start here)
│   ├── antv_renderer.py        # Python API
│   └── html_renderer.js        # Node.js renderer
├── templates/                  # 11 medical templates
└── outputs/                    # Generated HTML/SVG/PNG
```

---

## Examples

See `outputs/sample_*.html` for 5 working examples:
- Trial timeline
- Mechanism of action
- Patient journey
- Risk stratification
- Dosing schedule

---

## Integration Status

✅ **Production Ready**

- Fully functional
- Tested and validated
- Documented
- Integrated with visual router
- Ready for content creation

---

## Support

- **Full docs:** See `SKILL.md`
- **Template guide:** See `TEMPLATE_CATALOG.md`
- **Technical details:** See `INTEGRATION_REPORT.md`
- **CLI help:** `python scripts/antv_cli.py --help`

---

*AntV Infographic Integration - 2026-01-01*
