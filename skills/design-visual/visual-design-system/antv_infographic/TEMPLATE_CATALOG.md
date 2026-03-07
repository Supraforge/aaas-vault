# AntV Infographic Template Catalog

**11 Medical Templates** for common cardiology content

---

## Template Overview

| # | Template Name | Visual Style | Items | Best For |
|---|---------------|--------------|-------|----------|
| 1 | `trial_result_simple` | Horizontal timeline | 4 | Trial phases, study timelines |
| 2 | `mechanism_of_action` | Vertical steps | 5 | Drug MOA, biological pathways |
| 3 | `treatment_comparison` | Horizontal comparison | 4 | Treatment options, drug comparison |
| 4 | `patient_journey` | Horizontal pathway | 5 | Care pathways, patient experience |
| 5 | `guideline_recommendations` | Vertical classification | 4 | Guideline strength, evidence levels |
| 6 | `dosing_schedule` | Horizontal timeline | 4 | Medication titration, dosing protocols |
| 7 | `safety_profile` | Vertical list | 4 | Adverse events, safety data |
| 8 | `biomarker_progression` | Horizontal timeline | 4 | Biomarker trends, lab values |
| 9 | `trial_endpoints` | Vertical list | 4 | Primary/secondary outcomes |
| 10 | `risk_stratification` | Vertical levels | 4 | Risk classification, patient stratification |
| 11 | `diagnostic_pathway` | Horizontal workflow | 5 | Diagnostic algorithms, clinical workflows |

---

## Detailed Template Guide

### 1. Trial Result Simple

**Template:** `trial_result_simple`
**Visual:** Horizontal timeline with arrows
**Items:** 4 phases

**Use Cases:**
- Clinical trial timelines
- Study phase summaries
- Research project milestones

**Example Data:**
```
Enrollment → Randomization → Treatment → Results
4,744 screened | 1:1 ratio | 18 months | 26% reduction
```

**Render:**
```bash
python scripts/antv_cli.py render --template trial_result_simple
```

---

### 2. Mechanism of Action

**Template:** `mechanism_of_action`
**Visual:** Vertical step flow
**Items:** 5 steps

**Use Cases:**
- Drug mechanism explanations
- Biological pathway visualizations
- Pharmacodynamics education

**Example Data:**
```
Step 1: Oral Administration
Step 2: Systemic Distribution
Step 3: Receptor Binding
Step 4: Cellular Response
Step 5: Clinical Effect
```

**Render:**
```bash
python scripts/antv_cli.py render --template mechanism_of_action
```

---

### 3. Treatment Comparison

**Template:** `treatment_comparison`
**Visual:** Horizontal comparison
**Items:** 4 treatments

**Use Cases:**
- Side-by-side drug comparison
- Treatment option overview
- Therapy selection guidance

**Example Data:**
```
SGLT2i: 26% reduction | ARNI: 20% reduction | BB: 35% reduction | MRA: 30% reduction
```

**Render:**
```bash
python scripts/antv_cli.py render --template treatment_comparison
```

---

### 4. Patient Journey

**Template:** `patient_journey`
**Visual:** Horizontal pathway
**Items:** 5 stages

**Use Cases:**
- Patient care pathways
- Clinical workflow maps
- Patient education materials

**Example Data:**
```
Presentation → Diagnosis → Treatment → Monitoring → Long-term Care
Symptoms | ECG/Labs | GDMT | Follow-up | Lifestyle
```

**Render:**
```bash
python scripts/antv_cli.py render --template patient_journey
```

---

### 5. Guideline Recommendations

**Template:** `guideline_recommendations`
**Visual:** Vertical classification
**Items:** 4 classes

**Use Cases:**
- ACC/AHA guideline summaries
- Evidence-based recommendations
- Treatment strength classification

**Example Data:**
```
Class I: Recommended (Level A)
Class IIa: Reasonable (Level B)
Class IIb: May be considered (Level C)
Class III: Not recommended (Harm)
```

**Render:**
```bash
python scripts/antv_cli.py render --template guideline_recommendations
```

---

### 6. Dosing Schedule

**Template:** `dosing_schedule`
**Visual:** Horizontal timeline
**Items:** 4 time periods

**Use Cases:**
- Medication titration protocols
- Dosing schedules
- Treatment escalation plans

**Example Data:**
```
Week 1-2: 10mg daily
Week 3-4: 20mg daily
Week 5-8: 40mg daily
Ongoing: Maintenance dose
```

**Render:**
```bash
python scripts/antv_cli.py render --template dosing_schedule
```

---

### 7. Safety Profile

**Template:** `safety_profile`
**Visual:** Vertical list by frequency
**Items:** 4 frequency categories

**Use Cases:**
- Adverse event summaries
- Drug safety profiles
- Risk communication

**Example Data:**
```
Common (>10%): Dizziness, fatigue
Uncommon (1-10%): Hypotension, hyperkalemia
Rare (<1%): Angioedema, renal dysfunction
Serious: Monitor K+, Cr regularly
```

**Render:**
```bash
python scripts/antv_cli.py render --template safety_profile
```

---

### 8. Biomarker Progression

**Template:** `biomarker_progression`
**Visual:** Horizontal timeline
**Items:** 4 time points

**Use Cases:**
- Biomarker trend visualization
- Lab value tracking
- Treatment response monitoring

**Example Data:**
```
Baseline: BNP 850 pg/mL
3 Months: BNP 520 pg/mL
6 Months: BNP 280 pg/mL
12 Months: BNP 150 pg/mL
```

**Render:**
```bash
python scripts/antv_cli.py render --template biomarker_progression
```

---

### 9. Trial Endpoints

**Template:** `trial_endpoints`
**Visual:** Vertical list
**Items:** 4 outcomes

**Use Cases:**
- Trial outcome summaries
- Endpoint hierarchies
- Results visualization

**Example Data:**
```
Primary: CV death/HF hosp (HR 0.74)
Secondary 1: All-cause mortality (HR 0.83)
Secondary 2: HF hospitalization (HR 0.70)
Safety: AE similar to placebo
```

**Render:**
```bash
python scripts/antv_cli.py render --template trial_endpoints
```

---

### 10. Risk Stratification

**Template:** `risk_stratification`
**Visual:** Vertical risk levels
**Items:** 4 risk categories

**Use Cases:**
- CV risk classification
- Patient stratification
- Risk communication

**Example Data:**
```
Low Risk (0-2): <10% 10-year risk, lifestyle
Moderate (3-4): 10-20% risk, consider statin
High (≥5): >20% risk, intensive therapy
Very High: Known CVD, aggressive management
```

**Render:**
```bash
python scripts/antv_cli.py render --template risk_stratification
```

---

### 11. Diagnostic Pathway

**Template:** `diagnostic_pathway`
**Visual:** Horizontal workflow
**Items:** 5 steps

**Use Cases:**
- Diagnostic algorithms
- Clinical workflows
- Decision support

**Example Data:**
```
Suspicion → Testing → Stratification → Imaging → Decision
Symptoms | ECG/Trop/BNP | HEART score | Echo/CT | Medical vs PCI
```

**Render:**
```bash
python scripts/antv_cli.py render --template diagnostic_pathway
```

---

## Customization Guide

### Modifying Templates

1. **Locate template:** `templates/[template_name].txt`
2. **Edit content:** Change labels and descriptions
3. **Test render:** `python scripts/antv_cli.py render --template [template_name]`

### Example Customization

**Original:**
```
infographic list-row-simple-horizontal-arrow
data
  items:
    - label: Enrollment
      desc: 4,744 patients with HFrEF screened
```

**Customized:**
```
infographic list-row-simple-horizontal-arrow
data
  items:
    - label: Screening
      desc: 5,000 patients assessed for eligibility
    - label: Enrollment
      desc: 3,500 patients enrolled (70% of screened)
```

---

## Quick Reference

### List All Templates
```bash
python scripts/antv_cli.py list --verbose
```

### Render Specific Template
```bash
python scripts/antv_cli.py render --template [NAME] --output [FILE]
```

### Generate All Examples
```bash
python scripts/antv_cli.py examples
```

### Python API
```python
from scripts.antv_renderer import render_template

output = render_template('mechanism_of_action', 'output.html')
```

---

## Template Selection Guide

**Q: Which template for trial summaries?**
A: `trial_result_simple` or `trial_endpoints`

**Q: Which template for drug education?**
A: `mechanism_of_action` or `dosing_schedule`

**Q: Which template for patient materials?**
A: `patient_journey` or `safety_profile`

**Q: Which template for clinical guidelines?**
A: `guideline_recommendations` or `diagnostic_pathway`

**Q: Which template for risk communication?**
A: `risk_stratification` or `treatment_comparison`

---

## Next Steps

1. Browse templates: `python scripts/antv_cli.py list --verbose`
2. View samples: Open files in `outputs/` directory
3. Customize templates: Edit files in `templates/` directory
4. Create new templates: Add new `.txt` files following syntax
5. Generate content: Use CLI or Python API

---

*Template Catalog - AntV Infographic Integration*
*Last Updated: 2026-01-01*
