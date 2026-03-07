---
name: carousel-generator-v2
description: >-
  **World-class Instagram carousel generator** with AI content intelligence,
  multi-tool visual generation, and professional design systems.
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---
# Carousel Generator v2

**World-class Instagram carousel generator** with AI content intelligence, multi-tool visual generation, and professional design systems.

---

## Quick Start

```bash
# Generate from topic
python -m scripts.carousel_generator "GLP-1 for weight loss" --template tips_5

# Generate from JSON structure
python -m scripts.carousel_generator input.json --output ./my-carousel/

# Generate from long-form content (backward mode)
python -m scripts.carousel_generator newsletter.txt

# Generate both 4:5 and 1:1 outputs
python -m scripts.carousel_generator "Statin myths" --template myth_busting --both-ratios
```

Or use in Claude Code:
```
"Create a carousel about statins myth-busting"
"Generate Instagram slides for GLP-1 benefits"
"Turn this newsletter into carousel slides: [paste content]"
```

---

## Architecture

```
INPUT LAYER
├── Topic only ("GLP-1 for weight loss")
├── Long-form content (newsletter, script, thread)
└── Structured JSON (slides already defined)
        ↓
CONTENT INTELLIGENCE (Claude/GPT-4o-mini)
├── Research via PubMed MCP + AstraDB RAG
├── Classify: 4A Framework (Actionable/Analytical/etc.)
├── Select template type (Tips/Stats/Story/Compare)
├── Structure into 8-10 slides with hook + CTA
└── Output: Structured JSON with slide specs
        ↓
VISUAL GENERATION (Multi-Tool Routing)
├── Standard slides → React + Puppeteer (default, high fidelity)
├── Pillow → Fallback renderer if Puppeteer unavailable
├── Infographics → Gemini API (medical accuracy)
├── Data slides → Plotly (charts, forest plots)
└── Icons → Health Icons (free, SVG, medical)
        ↓
QUALITY GATES
├── WCAG AA contrast check (4.5:1 ratio)
├── Text density check (≤15 words per slide)
├── Anti-AI voice verification
├── Brand consistency (design tokens)
└── Mobile preview generation
        ↓
OUTPUT
├── 8-10 PNG slides (1080×1350 or 1080×1080)
├── Dual ratio naming: slide_01_4x5.png, slide_01_1x1.png
├── Caption suggestions per slide
├── Alt text for accessibility
├── Hashtag recommendations
└── Quality report
```

---

## 10 Slide Types

| Type | Purpose | Best For |
|------|---------|----------|
| **HOOK** | Bold opening, curiosity gap | First slide, grab attention |
| **TIPS** | Numbered tips with icons | Actionable content, lists |
| **STATS** | Big number + context | Data-driven insights |
| **COMPARISON** | Before/after, vs layout | Contrasts, improvements |
| **STORY** | Patient narrative, quote | Human interest, case studies |
| **DATA** | Chart, graph, forest plot | Research results, evidence |
| **STEPS** | Process with numbered steps | How-to guides, procedures |
| **MYTH** | Crossed-out myth + truth | Myth-busting, corrections |
| **QUOTE** | Expert opinion | Authority, credibility |
| **CTA** | Call to action | Last slide, follow prompt |

---

## Template Presets

### tips_5 (Default)
```
HOOK → TIPS → TIPS → TIPS → TIPS → TIPS → STATS → CTA
```
Best for: Actionable advice, numbered lists, practical content

### myth_busting
```
HOOK → MYTH → MYTH → MYTH → STATS → CTA
```
Best for: Correcting misconceptions, debunking myths

### patient_story
```
HOOK → STORY → STORY → DATA → TIPS → QUOTE → CTA
```
Best for: Case studies, patient journeys, human interest

### data_driven
```
HOOK → STATS → DATA → COMPARISON → TIPS → CTA
```
Best for: Clinical trials, research findings, evidence-based content

### how_to
```
HOOK → STEPS → STEPS → STEPS → TIPS → CTA
```
Best for: Tutorials, procedures, step-by-step guides

---

## CLI Options

```bash
python -m scripts.carousel_generator INPUT [OPTIONS]

Arguments:
  INPUT                    Topic string, JSON file, or text file

Options:
  -t, --template TEXT      Template preset (tips_5, myth_busting, etc.)
  -a, --account INTEGER    Account: 1=@heartdocshailesh, 2=@dr.shailesh.singh
  -r, --ratio TEXT         Aspect ratio: 4:5 (Instagram) or 1:1 (square)
  --both-ratios            Generate both 4:5 and 1:1 outputs
  -o, --output PATH        Output directory
  --no-ai                  Skip AI content structuring (uses curated database if available)
```

### Examples

```bash
# Basic usage
python -m scripts.carousel_generator "5 signs of heart attack"

# Myth-busting format
python -m scripts.carousel_generator "Statin myths" --template myth_busting

# Use secondary account
python -m scripts.carousel_generator "CAC scoring" --account 2

# Square format for multi-platform
python -m scripts.carousel_generator "BP monitoring" --ratio 1:1

# Dual ratio output
python -m scripts.carousel_generator "Hypertension myths" --both-ratios

# Custom output directory
python -m scripts.carousel_generator "GLP-1" -o ./client-carousel/
```

---

## Python API

```python
from scripts.carousel_generator import CarouselGenerator
from scripts.models import CarouselConfig, AspectRatio

# Configure
config = CarouselConfig(
    account=1,
    aspect_ratio=AspectRatio.INSTAGRAM_4X5,
    max_slides=10,
    check_contrast=True,
    check_anti_ai=True
)

# Initialize generator
generator = CarouselGenerator(config)

# Generate from topic
result = generator.generate_from_topic(
    "GLP-1 for weight loss",
    template="tips_5",
    use_ai=True
)

print(f"Generated {len(result.slides)} slides to {result.output_directory}")
```

### Generate from JSON Structure

```python
# Create structured input
carousel_json = {
    "topic": "Heart Health Tips",
    "slides": [
        {
            "type": "hook",
            "title": "5 Things Your Cardiologist Wishes You Knew",
            "subtitle": "Evidence-based insights"
        },
        {
            "type": "tips",
            "title": "Tip #1",
            "bullet_points": [
                "LDL target matters more than total cholesterol",
                "Below 100 mg/dL for most, below 70 for high risk"
            ]
        },
        {
            "type": "cta",
            "cta_text": "Follow for more",
            "cta_handle": "@heartdocshailesh"
        }
    ]
}

import json
with open("input.json", "w") as f:
    json.dump(carousel_json, f)

result = generator.generate_from_json(Path("input.json"))
```

### Generate from Long-form Content (Backward Mode)

```python
newsletter_content = """
# The Truth About Statins

Recent meta-analyses have conclusively shown that statins reduce
cardiovascular events by 25-30%. The most common side effect,
muscle pain, occurs in only 5-10% of patients...
"""

result = generator.generate_from_longform(
    newsletter_content,
    content_type="newsletter"
)
```

---

## Quality Checker

The generator automatically runs quality checks:

```python
from scripts.quality_checker import QualityChecker
from scripts.models import Carousel

checker = QualityChecker()

# Run all checks
results = checker.run_all_checks(carousel)

# Generate report
report = checker.generate_report(results)
print(report)
```

### Quality Checks Performed

| Check | Threshold | Description |
|-------|-----------|-------------|
| **text_density** | ≤15 words/slide | Ensures scannability |
| **contrast_ratio** | ≥4.5:1 | WCAG AA compliance |
| **anti_ai** | No AI patterns | Detects AI-generated phrases |
| **slide_count** | 8-10 slides | Optimal engagement |
| **hook_quality** | Question or number | Engaging first slide |
| **cta_presence** | Last slide is CTA | Clear call to action |

### Anti-AI Detection

The checker flags these patterns:
- "It's important to note"
- "In conclusion"
- "Stands as a testament"
- "Groundbreaking" / "Game-changing"
- "Vibrant tapestry"
- Em dash overuse (more than 1 per paragraph)

---

## Brand Tokens

Design tokens are stored in `tokens/brand-tokens.json`:

### Colors
| Token | Value | Use |
|-------|-------|-----|
| primary | #207178 | Titles, CTAs, primary brand |
| secondary | #E4F1EF | Backgrounds, soft elements |
| accent | #F28C81 | Icons, highlights, bullets |
| neutralLight | #F8F9FA | Alternative backgrounds |
| neutralDark | #333333 | Body text |
| alert | #E63946 | Emphasis, danger, alerts |

### Typography
| Element | Font | Size | Weight |
|---------|------|------|--------|
| headline | Inter | 48px | Bold |
| subheadline | Inter | 36px | SemiBold |
| body | Inter | 28px | Regular |
| bodyLarge | Inter | 32px | Regular |
| caption | Inter | 22px | Medium |
| stat | Inter | 72px | Bold |

### Dimensions
| Ratio | Size | Use |
|-------|------|-----|
| 4:5 | 1080×1350px | Instagram (10% higher engagement) |
| 1:1 | 1080×1080px | Multi-platform |

---

## Accounts

Two accounts are configured:

| Account | Handle | Use For |
|---------|--------|---------|
| 1 (default) | @heartdocshailesh | Primary cardiology content |
| 2 | @dr.shailesh.singh | Professional/clinical content |

---

## Available Icons

21 medical icons included in `assets/icons/`:

**Cardiology:** heart-filled, heart-outline, heartbeat, blood-drop
**Lifestyle:** running, apple, sleep, scale, stress
**Medical:** pill, stethoscope, brain, chart-up, warning
**UI:** checkmark, cross, arrow-right, quote, lightbulb, follow

---

## Integration with Content OS

### Forward Mode (Topic → Carousel)
```
"Content OS: Statins myth-busting - include carousel"
```

### Backward Mode (Long-form → Carousel)
```
"Turn my latest newsletter into Instagram carousel slides"
```

---

## Output Structure

```
output/carousels/GLP-1-for-weight-loss/
├── slide-01.png  # Hook
├── slide-02.png  # Tips
├── slide-03.png  # Tips
├── slide-04.png  # Tips
├── slide-05.png  # Tips
├── slide-06.png  # Tips
├── slide-07.png  # Stats
├── slide-08.png  # CTA
├── caption.txt   # Suggested captions
├── alt-text.txt  # Accessibility descriptions
├── hashtags.txt  # Recommended hashtags
└── report.txt    # Quality check report
```

---

## Dependencies

```
pillow>=10.0.0      # Image rendering
pydantic>=2.0.0     # Data validation
plotly>=5.0.0       # Charts (optional)
kaleido>=0.2.0      # Plotly export (optional)
```

---

## Research-Backed Design Standards

| Standard | Value | Source |
|----------|-------|--------|
| Optimal Aspect Ratio | 4:5 | 10% higher engagement than 1:1 |
| Slide Count | 8-10 | Highest average engagement |
| First Slide Impact | 80% | Hook determines carousel success |
| Contrast Ratio | 4.5:1+ | WCAG AA compliance |
| Typography | 36px+ headlines | Mobile readability |
| Text Density | ≤15 words | Optimal scannability |

---

## Roadmap

### Completed
- [x] Pillow rendering for all 10 slide types
- [x] Brand token system
- [x] Quality checking (WCAG, anti-AI, density)
- [x] CLI interface
- [x] Template presets
- [x] AI content structuring (Claude/GPT-4o-mini) - `content_structurer.py`
- [x] PubMed integration for research - `hooks_generator.py` uses `pubmed_client.py`
- [x] 4A Framework classifier - `content_structurer.py:44-133`
- [x] Satori React rendering (optional) - `satori_renderer.py`
- [x] Visual router (Pillow/Gemini/Plotly/Puppeteer) - `visual_router.py`
- [x] Caption and hashtag generator - `caption_generator.py`
- [x] Content-OS integration - `content-os/scripts/orchestrator.py`
- [x] Batch generation - `carousel_generator.py --batch`
- [x] Puppeteer React rendering - `puppeteer_renderer.py` + `renderer/`

### In Progress
- [ ] Additional Manim animation scenes
- [ ] Interactive point selection for data slides

### Planned
- [ ] Video export (animated carousels)
- [ ] A/B testing integration

---

*Part of Dr. Shailesh Singh's Integrated Cowriting System*
