---
name: brand-qa
description: Validate content against brand voice guidelines and terminology. Includes voice checker, terminology validator, and consistency scorer. Use when reviewing marketing content, checking brand compliance, validating copy before publishing, or ensuring brand consistency across materials.
license: MIT
metadata:
  version: 1.0.0
  author: [PROJECT_NAME] AI
  category: marketing
  domain: brand-quality
  updated: 2026-02-12
  python-tools: voice_checker.py, terminology_validator.py, consistency_scorer.py
  tech-stack: Python, JSON
  integrations: content-creator, content-factory, sales-enablement
---

# Brand QA

Validate content against brand voice guidelines, terminology requirements, and consistency standards. Foundation skill used by other content-generating skills.

## Keywords

brand voice, brand consistency, content validation, quality assurance, terminology check, brand guidelines, voice analysis, content review, brand compliance, copywriting review, marketing QA

## Quick Start

### Validate Content Against Brand
```bash
python scripts/voice_checker.py content.md --brand [PROJECT_NAME]
```

### Check Terminology Usage
```bash
python scripts/terminology_validator.py content.md --brand [PROJECT_NAME]
```

### Get Full Consistency Score
```bash
python scripts/consistency_scorer.py content.md --brand [PROJECT_NAME] --output json
```

## Core Workflows

### 1. Pre-Publication Content Review

**Goal**: Ensure content meets brand standards before publishing

**Process**:
1. Run consistency scorer for overall assessment
2. Review any terminology violations
3. Address voice misalignments
4. Re-validate after edits

```bash
# Full review pipeline
python scripts/consistency_scorer.py draft.md --brand [PROJECT_NAME]
# Fix issues based on output
python scripts/voice_checker.py draft.md --brand [PROJECT_NAME] --verify
```

### 2. Brand Voice Calibration

**Goal**: Establish baseline for new content types

**Process**:
1. Analyze existing high-performing content
2. Extract voice patterns
3. Document in brand resources
4. Use as reference for future validation

### 3. Batch Content Validation

**Goal**: Review multiple pieces at once

```bash
# Validate all content briefs
for f in context/content_briefs/*.md; do
  python scripts/consistency_scorer.py "$f" --brand [PROJECT_NAME] --output json
done
```

## Key Scripts

### voice_checker.py

Analyzes content for brand voice alignment.

**Usage**: `python scripts/voice_checker.py <file> --brand <brand_slug> [--output json|text]`

**Returns**:
- Voice alignment score (0-100)
- Tone analysis (matches brand tone attributes)
- Style assessment
- Specific recommendations

**Example**:
```bash
python scripts/voice_checker.py linkedin_post.md --brand [PROJECT_NAME] --output json
```

### terminology_validator.py

Checks for required brand terminology and flags anti-patterns.

**Usage**: `python scripts/terminology_validator.py <file> --brand <brand_slug>`

**Returns**:
- Required terms found/missing
- Anti-patterns detected
- Suggested replacements
- Terminology score

**Key Validations**:
- Required lexicon present (e.g., "Neural Quality Layer", "Golden Thread")
- Anti-patterns avoided (e.g., "AI tool" instead of "Neural Quality Layer")
- Industry terminology correct

### consistency_scorer.py

Generates comprehensive brand consistency score.

**Usage**: `python scripts/consistency_scorer.py <file> --brand <brand_slug> [--output json|text] [--threshold 80]`

**Returns**:
- Overall score (0-100)
- Voice score component
- Terminology score component
- Readability score
- Pass/fail against threshold
- Detailed breakdown

**Example**:
```bash
python scripts/consistency_scorer.py content.md --brand supra-forge --threshold 85
```

## Brand Configuration

The skill reads brand configuration from `context/brand_configs/{brand}.json`:

```json
{
  "brand_name": "[PROJECT_NAME]",
  "voice": {
    "tone": "Innovative, Precise, Empowering",
    "style": "Clear and forward-thinking"
  },
  "context_docs": ["context/brand_strategy.md"]
}
```

## Validation Criteria

### Voice Alignment (40% of score)
- Tone matches brand attributes
- Formality level appropriate
- Perspective consistent (authoritative vs conversational)
- Sentence variety and rhythm

### Terminology Compliance (35% of score)
- Required terms present (minimum 2)
- No anti-pattern violations
- Industry terminology accurate
- Key phrases used correctly

### Readability (25% of score)
- Appropriate for target audience
- Sentence length variety
- Clear structure
- Scannable formatting

### Passing Thresholds
- **Publishing**: Score >= 80
- **Draft review**: Score >= 60
- **Needs revision**: Score < 60

## Resources

### [PROJECT_NAME]_lexicon.json
Required terminology for [PROJECT_NAME] brand:
- "Neural Quality Layer"
- "Golden Thread"
- "See the Risk Before It Sees You"
- "Audit Blindness"
- "Manual Compliance Tax"
- "Real-Time Audit Companion"

### supra_forge_lexicon.json
Required terminology for SUPRA FORGE brand:
- All [PROJECT_NAME] terms plus:
- "Waze for Compliance"
- "Benevolent Omniscience"
- "Quality. Engineered. Not Administered."

### anti_patterns.json
Terms to avoid and their replacements:
- "AI tool" -> "Neural Quality Layer"
- "Problem" -> "Systemic failure" (in context)
- "Delayed feedback" -> "Late visibility"
- "Fast compliance" -> "Compliance at the speed of code"

## Integration Points

This skill is called by:
- **content-factory**: Validates generated content
- **sales-enablement**: Checks email sequences
- **pr-communications**: Reviews press releases
- **visual-content-generator**: Validates carousel text

## Best Practices

### Do's
- Run validation before publishing
- Address all anti-pattern violations
- Ensure minimum required terminology
- Check readability for target audience

### Don'ts
- Ignore low scores without review
- Over-stuff content with terminology
- Sacrifice readability for terminology
- Skip validation for "quick posts"

## Troubleshooting

### Low Voice Score
- Check tone matches brand attributes
- Review sentence structure variety
- Ensure appropriate formality level

### Missing Terminology
- Review required lexicon for brand
- Add natural mentions of key terms
- Don't force terminology unnaturally

### Anti-Pattern Violations
- Check resources/anti_patterns.json for replacements
- Update content with correct terminology
- Re-run validation after fixes
