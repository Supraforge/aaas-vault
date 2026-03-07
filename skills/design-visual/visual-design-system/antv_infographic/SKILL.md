# AntV Infographic Integration

**Purpose:** Template-driven medical infographics using the AntV Infographic framework
**Status:** ✅ Complete - Integrated into visual-design-system
**Priority:** P0 (fills critical template gap)

---

## Overview

AntV Infographic is a declarative infographic visualization engine with 200+ built-in templates, optimized for AI generation. This integration provides:

- **11 medical-specific templates** for common cardiology content
- **Python API** for programmatic generation
- **CLI tools** for quick rendering
- **Visual router integration** for automatic tool selection
- **SVG/PNG export** via browser-based workflow

---

## Quick Start

### 1. List Available Templates

```bash
cd skills/cardiology/visual-design-system/antv_infographic
python scripts/antv_cli.py list --verbose
```

**Available Templates:**
1. `trial_result_simple` - Clinical trial timeline (4 phases)
2. `mechanism_of_action` - Drug mechanism steps (5 steps)
3. `treatment_comparison` - Side-by-side treatment comparison
4. `patient_journey` - Patient care pathway (5 stages)
5. `guideline_recommendations` - Guideline strength classification
6. `dosing_schedule` - Medication dosing schedule (4 weeks)
7. `safety_profile` - Adverse events by frequency
8. `biomarker_progression` - Biomarker changes over time
9. `trial_endpoints` - Primary and secondary endpoints
10. `risk_stratification` - Risk level classification
11. `diagnostic_pathway` - Diagnostic workflow (5 steps)

### 2. Render a Template

```bash
python scripts/antv_cli.py render --template mechanism_of_action --output my_infographic.html
```

This generates an HTML file that opens in your browser. You can then:
- View the infographic
- Download as SVG (vector, editable)
- Download as PNG (raster, 2x resolution)

### 3. Python API

```python
from scripts.antv_renderer import render_template, AntvRenderer

# Quick render
output = render_template('trial_result_simple', 'output.html')

# Advanced usage
renderer = AntvRenderer()
renderer.render_template_to_html(
    'mechanism_of_action',
    'mechanism.html',
    width=1000,
    height=800,
    title='Drug Mechanism of Action'
)
```

---

## Medical Use Cases

| Use Case | Template | Output Type |
|----------|----------|-------------|
| **Trial summaries** | `trial_result_simple`, `trial_endpoints` | Timeline infographic |
| **Drug education** | `mechanism_of_action`, `dosing_schedule` | Step-by-step visual |
| **Patient education** | `patient_journey`, `safety_profile` | Pathway/process flow |
| **Clinical guidelines** | `guideline_recommendations`, `diagnostic_pathway` | Classification visual |
| **Risk communication** | `risk_stratification`, `biomarker_progression` | Stratification graphic |
| **Treatment decisions** | `treatment_comparison` | Comparison infographic |

---

## Template Catalog

### Trial Result Timeline

**File:** `templates/trial_result_simple.txt`

**Use for:** Clinical trial phases, study timelines

**Example:**
```
infographic list-row-simple-horizontal-arrow
data
  items:
    - label: Enrollment
      desc: 4,744 patients with HFrEF screened
    - label: Randomization
      desc: 1:1 ratio to treatment or placebo
    - label: Treatment
      desc: 18 month median follow-up
    - label: Results
      desc: 26% reduction in primary endpoint
```

**Visual:** Horizontal timeline with arrows connecting phases

---

### Mechanism of Action

**File:** `templates/mechanism_of_action.txt`

**Use for:** Drug mechanisms, biological pathways

**Example:**
```
infographic list-row-simple-vertical
data
  items:
    - label: Oral Administration
      desc: Drug taken orally, absorbed in GI tract
    - label: Systemic Distribution
      desc: Reaches target organs via bloodstream
    - label: Receptor Binding
      desc: Binds to specific receptors at cellular level
    - label: Cellular Response
      desc: Triggers cascade of intracellular signaling
    - label: Clinical Effect
      desc: Measurable improvement in symptoms/outcomes
```

**Visual:** Vertical step-by-step flow with labels and descriptions

---

### Patient Journey

**File:** `templates/patient_journey.txt`

**Use for:** Care pathways, patient experience timelines

**Example:**
```
infographic list-row-simple-horizontal-arrow
data
  items:
    - label: Presentation
      desc: Patient presents with symptoms at clinic
    - label: Diagnosis
      desc: ECG, biomarkers, imaging performed
    - label: Treatment Initiation
      desc: Evidence-based therapy started
    - label: Monitoring
      desc: Regular follow-up and dose optimization
    - label: Long-term Management
      desc: Continued care and lifestyle modification
```

**Visual:** Horizontal journey with 5 connected stages

---

### Risk Stratification

**File:** `templates/risk_stratification.txt`

**Use for:** Risk classification, patient stratification

**Example:**
```
infographic list-row-simple-vertical
data
  items:
    - label: Low Risk (0-2 factors)
      desc: 10-year CV risk <10%, lifestyle modification
    - label: Moderate Risk (3-4 factors)
      desc: 10-year CV risk 10-20%, consider statin
    - label: High Risk (≥5 factors)
      desc: 10-year CV risk >20%, intensive therapy
    - label: Very High Risk
      desc: Known CVD or diabetes, aggressive management
```

**Visual:** Vertical risk levels with descriptions

---

### Dosing Schedule

**File:** `templates/dosing_schedule.txt`

**Use for:** Medication titration, dosing protocols

**Example:**
```
infographic list-row-simple-horizontal-arrow
data
  items:
    - label: Week 1-2
      desc: Initial dose 10mg daily
    - label: Week 3-4
      desc: Titrate to 20mg daily if tolerated
    - label: Week 5-8
      desc: Target dose 40mg daily
    - label: Ongoing
      desc: Maintenance dose with monitoring
```

**Visual:** Timeline showing dose escalation

---

## Custom Spec Syntax

AntV Infographic uses a YAML-like declarative syntax:

```
infographic [TEMPLATE_TYPE]
data
  items:
    - label: [LABEL_TEXT]
      desc: [DESCRIPTION_TEXT]
    - label: [LABEL_TEXT]
      desc: [DESCRIPTION_TEXT]
```

**Available Template Types:**
- `list-row-simple-horizontal-arrow` - Horizontal timeline with arrows
- `list-row-simple-vertical` - Vertical list with connectors
- (200+ more templates available - see AntV documentation)

**Rendering Custom Specs:**

```bash
python scripts/antv_cli.py render --spec "infographic list-row-simple-horizontal-arrow
data
  items:
    - label: Step 1
      desc: First action
    - label: Step 2
      desc: Second action"
```

---

## Visual Router Integration

The visual router automatically selects AntV when you request template-driven infographics:

```python
from cardiology_visual_system.scripts.visual_router import VisualRouter

router = VisualRouter()

# These requests route to AntV:
router.route("Create a template infographic showing trial timeline")
router.route("Generate a structured infographic for mechanism of action")
router.route("Make a step-by-step treatment pathway infographic")

# These route to other tools:
router.route("Create a custom infographic")  # → Gemini
router.route("Generate a forest plot")       # → Plotly
router.route("Make a flowchart")             # → Mermaid
```

**Routing Keywords:**
- "template infographic"
- "structured infographic"
- "step-by-step infographic"
- "trial timeline"
- "mechanism steps"
- "treatment pathway infographic"

---

## CLI Reference

### List Templates

```bash
python scripts/antv_cli.py list              # Simple list
python scripts/antv_cli.py list --verbose    # With descriptions
```

### Render Template

```bash
python scripts/antv_cli.py render \
  --template mechanism_of_action \
  --output outputs/mechanism.html \
  --width 1000 \
  --height 800 \
  --title "Drug Mechanism"
```

### Render Custom Spec

```bash
python scripts/antv_cli.py render \
  --spec "infographic list-row-simple..." \
  --output custom.html
```

### Generate All Examples

```bash
python scripts/antv_cli.py examples
# Generates HTML files for all 11 templates in outputs/examples/
```

### Show Integration Info

```bash
python scripts/antv_cli.py info
```

---

## Python API Reference

### Quick Functions

```python
from scripts.antv_renderer import render_template, list_templates

# List templates
templates = list_templates()
# ['trial_result_simple', 'mechanism_of_action', ...]

# Quick render
output = render_template('trial_result_simple', 'output.html')
# Returns: Path object to generated HTML file
```

### AntvRenderer Class

```python
from scripts.antv_renderer import AntvRenderer

renderer = AntvRenderer()

# List templates
templates = renderer.list_templates()

# Load template spec
spec = renderer.load_template('mechanism_of_action')

# Render to HTML
output = renderer.render_to_html(
    spec,
    output_path='output.html',
    width=800,
    height=600,
    title='My Infographic'
)

# Render template directly
output = renderer.render_template_to_html(
    'trial_result_simple',
    'trial.html',
    width=1000,
    height=800
)

# Generate spec programmatically
spec = renderer.generate_spec(
    template_type='trial-timeline',
    data={
        'items': [
            {'label': 'Phase 1', 'desc': 'Enrollment'},
            {'label': 'Phase 2', 'desc': 'Treatment'},
        ]
    },
    theme='default'
)
```

---

## Workflow

### Standard Workflow

1. **Choose template**
   ```bash
   python scripts/antv_cli.py list --verbose
   ```

2. **Render to HTML**
   ```bash
   python scripts/antv_cli.py render --template mechanism_of_action
   ```

3. **Open in browser**
   - File is saved to `outputs/` directory
   - Opens automatically in default browser (or open manually)

4. **Download output**
   - Click "Download SVG" for vector graphics (editable in Illustrator, Inkscape)
   - Click "Download PNG" for raster images (2x resolution, publication quality)

5. **Use in content**
   - Add to blog posts, presentations, social media
   - Edit SVG if needed
   - Convert PNG to other formats as needed

### Programmatic Workflow

```python
from scripts.antv_renderer import AntvRenderer

# Initialize
renderer = AntvRenderer()

# Generate multiple infographics
templates = ['trial_result_simple', 'mechanism_of_action', 'patient_journey']

for template in templates:
    output = renderer.render_template_to_html(
        template,
        f'outputs/{template}.html',
        width=1200,
        height=900
    )
    print(f"Generated: {output}")

# Use in content pipeline
# (SVG extraction would require browser automation like Playwright)
```

---

## Comparison with Other Tools

| Feature | AntV Infographic | Gemini | Satori | Plotly |
|---------|------------------|--------|--------|--------|
| **Template library** | 200+ built-in | None | 5 custom | None |
| **Customization** | Declarative spec | AI prompt | React code | Python API |
| **Output** | SVG (via HTML) | PNG/JPG | PNG/SVG | PNG/HTML |
| **Best for** | Structured data | Custom designs | Social cards | Data viz |
| **Speed** | Fast (template) | Slow (AI) | Fast | Fast |
| **Editability** | High (SVG) | Low (raster) | Medium (SVG) | Medium |
| **AI-friendly** | Yes (syntax) | Yes (prompt) | No (code) | Partial |

**When to use AntV:**
- ✅ You have structured data (steps, timelines, comparisons)
- ✅ You want consistent, template-based output
- ✅ You need editable SVG graphics
- ✅ You're generating content at scale

**When to use other tools:**
- Gemini: Custom, one-off infographics with unique layouts
- Satori: Social media cards (Twitter, Instagram)
- Plotly: Statistical charts, trial data visualization
- Mermaid: Flowcharts, decision trees, clinical algorithms

---

## Limitations

1. **Browser-based export:** SVG/PNG export requires opening HTML in browser
   - Automated export would need Playwright or similar
   - Current workflow is semi-manual (click to download)

2. **Limited template variety:** Currently using 2 AntV templates
   - `list-row-simple-horizontal-arrow` (horizontal)
   - `list-row-simple-vertical` (vertical)
   - 198+ more templates available but not yet explored

3. **No direct SVG API:** Node.js renderer requires browser environment
   - JSDOM approach failed due to dependency issues
   - HTML-based approach is more reliable but less automated

4. **Medical templates are generic:** Templates use general AntV layouts
   - Medical content is in the data, not the template design
   - Future: Create custom medical-specific AntV templates

---

## Future Enhancements

### Phase 1: Template Expansion
- [ ] Explore and integrate 20+ more AntV template types
- [ ] Create custom medical-specific layouts
- [ ] Add theme support (colors, fonts matching design tokens)

### Phase 2: Automation
- [ ] Add Playwright integration for automated SVG extraction
- [ ] Direct SVG export without browser interaction
- [ ] Batch rendering pipeline

### Phase 3: Content Integration
- [ ] Integrate with carousel-generator-v2
- [ ] Add to content-os production pipeline
- [ ] Template recommendation system (AI suggests best template)

### Phase 4: Customization
- [ ] Custom medical themes (cardiology, oncology, etc.)
- [ ] Design token integration (colors, fonts from visual-design-system)
- [ ] Interactive editing in HTML preview

---

## Directory Structure

```
antv_infographic/
├── SKILL.md                    # This file
├── package.json                # NPM dependencies
├── node_modules/               # @antv/infographic + dependencies
├── scripts/
│   ├── renderer.js             # Node.js renderer (JSDOM - deprecated)
│   ├── html_renderer.js        # HTML generator (active)
│   ├── antv_renderer.py        # Python wrapper
│   └── antv_cli.py             # CLI tool
├── templates/                  # Medical infographic templates
│   ├── trial_result_simple.txt
│   ├── mechanism_of_action.txt
│   ├── treatment_comparison.txt
│   ├── patient_journey.txt
│   ├── guideline_recommendations.txt
│   ├── dosing_schedule.txt
│   ├── safety_profile.txt
│   ├── biomarker_progression.txt
│   ├── trial_endpoints.txt
│   ├── risk_stratification.txt
│   └── diagnostic_pathway.txt
├── examples/                   # Example specs and usage
├── outputs/                    # Generated HTML/SVG/PNG files
│   ├── sample_trial_timeline.html
│   ├── sample_mechanism.html
│   ├── sample_patient_journey.html
│   ├── sample_risk_stratification.html
│   └── sample_dosing_schedule.html
└── outputs/examples/           # Batch-generated examples
```

---

## Installation

Already integrated! No additional setup needed.

**Dependencies installed:**
- `@antv/infographic@0.2.3` - Core framework
- `jsdom` - For Node.js DOM environment (renderer.js)

**To reinstall:**
```bash
cd skills/cardiology/visual-design-system/antv_infographic
npm install
```

---

## Troubleshooting

### HTML file doesn't open automatically
- Manually open the file in your browser
- Path is printed in CLI output

### SVG download button doesn't work
- Ensure you're using a modern browser (Chrome, Firefox, Safari)
- Check browser console for errors

### Python import errors
```bash
# Ensure you're in the correct directory
cd skills/cardiology/visual-design-system/antv_infographic
python3 scripts/antv_cli.py list
```

### Template not found
- Check template name spelling
- Use `--list` to see available templates
- Templates are in `templates/` directory with `.txt` extension

---

## Contributing

### Adding New Templates

1. Create template file: `templates/your_template.txt`
2. Use AntV declarative syntax
3. Test rendering: `python scripts/antv_cli.py render --template your_template`
4. Update template catalog in this file

### Template Guidelines

- Use clear, descriptive labels
- Keep descriptions concise (under 50 characters)
- Use medical terminology appropriately
- Test with 3-7 items (optimal for readability)
- Consider mobile/social media dimensions

---

## References

- [AntV Infographic GitHub](https://github.com/antvis/Infographic)
- [AntV Documentation](https://antv.vision/en)
- [Visual Design System](../SKILL.md)
- [Visual Router](../../cardiology-visual-system/scripts/visual_router.py)

---

*Last Updated: 2026-01-01*
*Maintainer: Dr. Shailesh Singh*
*Integration Status: ✅ Complete - Production Ready*
