---
name: pitch-deck-generator
description: >-
  Generate professional investor pitch decks from templates. Downloads free
  templates from open repositories, populates with company data, and exports to
  PPTX. Keywords: pitch deck, investor presentation, fundraising, slides, PPTX.
version: 1.0.0
metadata:
  author: user
  category: business
  complexity: complex
triggers:
  - create pitch deck
  - generate investor deck
  - build fundraising presentation
  - pitch deck from template
tags:
  - pitch-deck
  - fundraising
  - presentations
  - pptx
  - investors
compatibility: 'agent-zero, claude-code, cursor'
---

# Pitch Deck Generator

Generate professional investor pitch decks using free templates from open repositories. This skill provides a complete workflow from template selection to final PPTX export.

## Overview

This skill automates the pitch deck creation process:
1. **Select Template** - Choose from curated free templates
2. **Gather Information** - Collect company/product data
3. **Generate Content** - Create slide content using proven frameworks
4. **Populate Template** - Fill template with generated content
5. **Export** - Produce final PPTX file

## Template Sources

### Free Template Repositories

| Source | Format | License | Best For |
|--------|--------|---------|----------|
| [SlidesCarnival](https://www.slidescarnival.com/) | PPTX, Google Slides | CC BY 4.0 | Modern, creative designs |
| [SlidesGo](https://slidesgo.com/) | PPTX, Google Slides | Free with attribution | Professional business |
| [PresentationGO](https://www.presentationgo.com/) | PPTX, Google Slides | Free | Clean diagrams |
| [SlidesMania](https://slidesmania.com/) | PPTX, Google Slides | Free | Educational style |
| [Canva](https://www.canva.com/) | PPTX export | Free tier | Quick customization |

### Recommended Templates for Pitch Decks

1. **Startup Pitch Deck** - Clean, minimal, investor-focused
2. **Business Proposal** - Professional, data-heavy layouts
3. **Modern Gradient** - Contemporary, tech-focused
4. **Corporate Blue** - Traditional, trustworthy feel

## Standard Procedure

### Phase 1: Information Gathering

Before creating the deck, collect:

```yaml
Company Info:
  name: ""
  tagline: ""
  logo_path: ""
  website: ""
  founded: ""
  
Problem:
  pain_point: ""
  who_affected: ""
  current_solutions: ""
  cost_of_problem: ""
  
Solution:
  product_name: ""
  how_it_works: ""
  key_features: []
  differentiators: []
  
Market:
  tam: ""       # Total Addressable Market
  sam: ""       # Serviceable Addressable Market
  som: ""       # Serviceable Obtainable Market
  growth_rate: ""
  why_now: ""
  
Traction:
  revenue: ""
  users: ""
  growth_rate: ""
  key_metrics: []
  logos: []
  
Business Model:
  pricing: ""
  unit_economics:
    cac: ""
    ltv: ""
    payback: ""
  
Competition:
  competitors: []
  positioning: ""
  moat: ""
  
Team:
  founders: []
  key_hires: []
  advisors: []
  
The Ask:
  amount: ""
  use_of_funds: []
  runway: ""
  milestones: []
```

### Phase 2: Template Selection

Run the template selector:

```bash
python3 skills/pitch-deck-generator/scripts/select_template.py
```

Or manually download from:
- https://www.slidescarnival.com/category/business
- https://slidesgo.com/theme/startup-pitch-deck

### Phase 3: Content Generation

For each slide section, generate content following the proven framework:

1. **Title Slide**
   - Company name + tagline
   - Optional: Traction headline ("$2M ARR | 50K users")

2. **Problem Slide**
   - 3 bullet points max
   - Quantify the pain
   - Make it relatable

3. **Solution Slide**
   - How you solve the problem
   - Key benefits (not features)
   - "Aha moment"

4. **Product/Demo Slide**
   - Screenshot or mockup
   - 3 key capabilities
   - User flow highlight

5. **Market Slide**
   - TAM/SAM/SOM circles
   - Market growth rate
   - "Why now" timing

6. **Business Model Slide**
   - Revenue model
   - Pricing tiers
   - Unit economics

7. **Traction Slide**
   - Growth chart
   - Key metrics
   - Customer logos

8. **Competition Slide**
   - 2x2 positioning matrix
   - Your unique position
   - Key differentiators

9. **Team Slide**
   - Headshots + names
   - Relevant backgrounds
   - "Why us" narrative

10. **The Ask Slide**
    - Amount raising
    - Use of funds pie chart
    - Key milestones

### Phase 4: PPTX Generation

Generate the final deck:

```bash
python3 skills/pitch-deck-generator/scripts/generate_pptx.py \
    --template assets/templates/startup-pitch.pptx \
    --data company_data.yaml \
    --output pitch_deck_final.pptx
```

## Quick Commands

| Action | Command |
|--------|---------|
| Select template | `python3 scripts/select_template.py` |
| Create data file | `cp assets/pitch_data_template.yaml my_pitch.yaml` |
| Generate deck | `python3 scripts/generate_pptx.py --data my_pitch.yaml` |
| Validate deck | `python3 scripts/validate_deck.py pitch_deck.pptx` |

## File Structure

```
pitch-deck-generator/
├── SKILL.md                    # This file
├── scripts/
│   ├── select_template.py      # Interactive template selector
│   ├── download_template.py    # Download from repositories
│   ├── generate_pptx.py        # Generate PPTX from data
│   └── validate_deck.py        # Check slide completeness
├── assets/
│   ├── pitch_data_template.yaml    # Data collection template
│   └── templates/                  # Downloaded templates
├── references/
│   ├── slide_frameworks.md     # Content frameworks per slide
│   ├── design_principles.md    # Visual design guidelines
│   └── investor_expectations.md # What investors look for
└── examples/
    └── sample_pitch_data.yaml  # Example filled data
```

## Best Practices

### Content
- **One idea per slide** - Don't overcrowd
- **Lead with traction** - If metrics are strong, show early
- **Quantify everything** - Numbers build credibility
- **Tell a story** - Connect slides into a narrative

### Design
- **10-15 slides** - Respect investor time
- **Minimal text** - Headlines + visuals
- **Consistent branding** - Your colors, fonts
- **High-quality images** - No pixelated logos

### Delivery
- **PDF for email** - PPTX can break formatting
- **Practice 10+ times** - Know your deck cold
- **15-20 minute presentation** - Leave time for Q&A

## Dependencies

```bash
pip install python-pptx pyyaml requests
```

## Related Skills

- `pitch-deck-creator` - Conceptual frameworks
- `pptx-official` - PPTX manipulation
- `investor-discovery` - Finding investors
- `brand-identity` - Logo and brand guidelines

---

*Part of the centralized skills vault. Sync with: `python3 execution/vault_sync.py skills`*
