---
name: ce-research-agent
description: Autonomous Context Engineering research agent. Takes a company name, runs 6 research dimensions via web search, validates quality, and synthesizes into a SQUR-pattern contextual framework document. Use for company research, competitive intelligence, market analysis, and contextual framework generation.
license: MIT
metadata:
  version: 1.0.0
  author: [PROJECT_NAME] AI
  category: research
  domain: context-engineering
  updated: 2026-02-13
  python-tools: research_company.py, research_competitors.py, research_market.py, research_audience.py, research_brand.py, research_strategy.py, validate_research.py, synthesize_framework.py
  tech-stack: Python, WebSearch
  integrations: content-factory, sales-enablement, brand-qa
---

# CE Research Agent

Autonomous Context Engineering research agent that produces SQUR-pattern contextual framework documents for any company.

## Keywords

context engineering, company research, competitive intelligence, market analysis, audience research, brand voice, SQUR framework, contextual framework, research automation, CE research

## Triggers

Use this skill when:
- User asks to "research a company"
- User mentions "context engineering" or "CE research"
- User wants a "contextual framework" or "SQUR document"
- User needs competitive intelligence or market analysis
- User wants to understand a company's positioning, audience, or strategy

## Quick Start

### Full Research Pipeline (Recommended)

```bash
# Step 1: Generate and execute research for each dimension
python scripts/run.py research_company.py --company 'Acme Inc' --generate-prompt
# Execute the web searches in the prompt, save results

python scripts/run.py research_competitors.py --company 'Acme Inc' --generate-prompt
python scripts/run.py research_market.py --company 'Acme Inc' --generate-prompt
python scripts/run.py research_audience.py --company 'Acme Inc' --generate-prompt
python scripts/run.py research_brand.py --company 'Acme Inc' --generate-prompt
python scripts/run.py research_strategy.py --company 'Acme Inc' --generate-prompt

# Step 2: Validate research quality
python scripts/run.py validate_research.py --company 'Acme Inc'

# Step 3: Synthesize framework
python scripts/run.py synthesize_framework.py --company 'Acme Inc'
```

## Core Workflow

### Phase 1: Research (6 Dimensions)

Each research dimension generates a prompt for Claude to execute via WebSearch:

| Script | Dimension | Key Outputs |
|--------|-----------|-------------|
| `research_company.py` | Company Snapshot | Overview, product, features, use-cases, pricing |
| `research_competitors.py` | Competitor Intelligence | Competitor list, profiles, positioning, strengths |
| `research_market.py` | Market Intelligence | Market definition, trends, size, insights |
| `research_audience.py` | Audience Intelligence | Segments, JTBD, pains, desires, objections |
| `research_brand.py` | Brand Voice Forensics | Tone, style, messages, examples |
| `research_strategy.py` | Strategy Pattern Scan | GTM, growth loops, AI strategy, angles |

**Usage Pattern:**

```bash
# Generate research prompt
python scripts/run.py research_company.py --company 'Target Company' --generate-prompt

# The script outputs a structured prompt with:
# - Role definition
# - Sources to check
# - Search queries to execute
# - Required output format
```

**Output Format:**

Research results use the block pattern:
```
===== ce.{company}.{key} =====
[Content for this block]

===== reliability-report =====
- confidence: HIGH/MEDIUM/LOW
- sources_checked: [count]
- gaps: [list]
```

### Phase 2: Validate

Score research completeness and identify gaps:

```bash
python scripts/run.py validate_research.py --company 'Target Company'
```

**Output:**
- Dimension scores (0-100%)
- SQUR section coverage
- Gaps requiring additional research
- Overall assessment

**Passing threshold:** 60% overall score

### Phase 3: Synthesize

Generate the final SQUR-pattern framework document:

```bash
python scripts/run.py synthesize_framework.py --company 'Target Company'
```

**Output:** `output/{company}/context_framework.md`

## SQUR Framework Structure

The output document follows the 10-section SQUR pattern:

1. **Company Overview** - Name, offering, mission, key promise
2. **Product Highlights** - Core capabilities, differentiators
3. **Target Audience** - Roles, company types, industries
4. **Market Focus** - Primary/secondary regions, market segment
5. **AI & Governance** - AI capabilities, safety, compliance
6. **Competitive Landscape** - Primary competitors, differentiators
7. **Strategic Positioning** - Messaging pillars, emotional appeal
8. **Demand Gen Themes** - Themes, channels, tactics
9. **Use Case Scenarios** - Primary use cases, buyer scenarios
10. **Source Material Anchors** - Primary and secondary sources

**Formatting Rules:**
- 80-110 lines total
- Emoji headers per section
- Bold-label bullets
- Concrete specifics, no fluff
- Low confidence data marked with `[LOW CONFIDENCE]`

## Output Structure

```
output/{company}/
├── research/
│   ├── company.md
│   ├── competitors.md
│   ├── market.md
│   ├── audience.md
│   ├── brand.md
│   └── strategy.md
├── validation_report.md
└── context_framework.md
```

## Resource Files

### ce_prompts.json

Defines research instructions per dimension:
- Search queries
- Output blocks
- Source types
- Confidence scoring

### section_map.json

Maps research blocks to SQUR sections:
- Source file mappings
- Required elements per section
- Formatting rules

### squr_template.md

Reference SQUR framework showing ideal output structure.

## Integration Points

This skill outputs feed into:
- **content-factory**: Uses framework for content generation
- **sales-enablement**: Uses positioning for sales materials
- **brand-qa**: Validates against framework voice
- **pr-communications**: Uses messaging for press releases

## Best Practices

### Do's
- Run all 6 research dimensions for complete coverage
- Validate before synthesizing
- Re-research gaps identified in validation
- Include source URLs in research
- Mark uncertain data with confidence levels

### Don'ts
- Don't synthesize with major gaps (< 60% score)
- Don't skip dimensions
- Don't use placeholder text in research
- Don't mix multiple companies in one research set

## Troubleshooting

### No research found
Ensure research files are saved to:
`output/{company}/research/{dimension}.md`

### Low validation score
- Check which dimensions are missing
- Re-run research prompts for gaps
- Ensure output uses the block format

### Empty synthesis output
- Verify research files exist
- Check block format matches pattern
- Run validation to identify issues

## Manual Research Workflow

If running without scripts:

1. **Search** using queries from `resources/ce_prompts.json`
2. **Format** findings using the block pattern:
   ```
   ===== ce.{company}.{key} =====
   [Your findings here]
   ```
3. **Save** to `output/{company}/research/{dimension}.md`
4. **Validate** with validation script
5. **Synthesize** with synthesis script
