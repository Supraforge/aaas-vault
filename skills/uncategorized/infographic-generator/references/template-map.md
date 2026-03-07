# Infographic Template Map

Use these templates with `infographic_cli.py`. Keep copy short and data-specific.

## Satori Templates (React -> SVG -> PNG)

### stat-card
**Use:** Single metric highlight
**Fields:** value, label, sublabel (optional), source (optional)
```json
{"value":"26%","label":"Mortality reduction","sublabel":"HR 0.74 (95% CI 0.65-0.85)","source":"PARADIGM-HF"}
```

### comparison
**Use:** Two-column comparison
**Fields:** title, left{value,label}, right{value,label}, metric (optional), source (optional)
```json
{"title":"Treatment vs Control","left":{"value":"11.4%","label":"Dapagliflozin"},"right":{"value":"15.6%","label":"Placebo"},"metric":"CV death or HF hospitalization","source":"DAPA-HF"}
```

### process-flow
**Use:** Step-by-step pathway
**Fields:** title, steps[{title,description,number(optional)}]
```json
{"title":"HFrEF Treatment Algorithm","steps":[{"title":"Diagnose","description":"EF <= 40%"},{"title":"Initiate","description":"Start foundational therapy"},{"title":"Optimize","description":"Titrate to target"}]}
```

### trial-summary
**Use:** Trial result card
**Fields:** trialName, population, intervention, primaryEndpoint, result{hr,ci,pValue}, nnt(optional)
```json
{"trialName":"DAPA-HF","population":"HFrEF patients","intervention":"Dapagliflozin 10mg","primaryEndpoint":"CV death or HF hospitalization","result":{"hr":0.74,"ci":"0.65-0.85","pValue":"<0.001"},"nnt":21}
```

### key-finding
**Use:** Single key takeaway
**Fields:** finding, icon(optional), context(optional), evidence(optional)
```json
{"finding":"SGLT2 inhibitors reduce HF hospitalization by 30%","icon":"arrow-down","context":"Meta-analysis of 5 major trials","evidence":"Class I, Level A"}
```

### infographic-dense
**Use:** Information-dense, multi-section infographic
**Fields:** tag, title, subtitle, sections[{title, bullets[], accent(optional)}], callout{label,text}, footer
```json
{
  "tag": "PATIENT GUIDE",
  "title": "GLP-1 Roll-Off in Heart Patients",
  "subtitle": "A practical tapering infographic",
  "sections": [
    {"title": "Who this is for", "bullets": ["Stable HF patients on GLP-1", "No active ischemia or decompensation"]},
    {"title": "Why consider roll-off", "bullets": ["GI intolerance or weight plateau", "Cost/coverage issues", "Need to reassess baseline symptoms"]},
    {"title": "Taper plan (6-8 weeks)", "bullets": ["Reduce dose stepwise every 2 weeks", "Pause if HF symptoms worsen", "Maintain nutrition/activity support"]},
    {"title": "Monitor weekly", "bullets": ["Weight, edema, BP", "Dyspnea/exertional capacity", "Glucose trends if diabetic"]},
    {"title": "Red flags", "bullets": ["Rapid weight gain", "Orthopnea or PND", "Resting HR >110 or new arrhythmia"], "accent": "danger"},
    {"title": "Follow-up", "bullets": ["Clinic or tele-visit at 2-4 weeks", "Adjust diuretics/RAASi if needed"]}
  ],
  "callout": {"label": "Bottom line", "text": "Taper slowly, monitor symptoms, and re-titrate HF therapy as needed."},
  "footer": "Educational infographic. Not medical advice."
}
```

## SVG Templates (Structured SVGs)

Use when you need multi-section layouts or complex visuals. Render via
`skills/cardiology/visual-design-system/svglue_templates/template_renderer.py`.

Templates available:
- `trial_results.svg`
- `drug_mechanism.svg`
- `patient_stats.svg`
- `before_after.svg`
- `risk_factors.svg`

Tip: Start with Satori templates for speed; move to SVG templates when you
need a denser layout or diagram.
