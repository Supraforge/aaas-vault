---
name: content-factory
description: Transform and generate marketing content at scale. Includes A/B variant generator, FAQ generator from docs, platform-optimized ad copy generator, and content repurposing pipeline (1 piece to 5 formats). Use for generating copy variations, extracting FAQs, creating ads, or repurposing content across channels.
license: MIT
metadata:
  version: 1.0.0
  author: [PROJECT_NAME] AI
  category: marketing
  domain: content-generation
  updated: 2026-02-12
  python-tools: ab_variant_generator.py, faq_generator.py, ad_copy_generator.py, content_repurposer.py
  tech-stack: Python, JSON
  integrations: brand-qa, content-operations
---

# Content Factory

Content generation and transformation tools for marketing teams.

## Keywords

content generation, A/B testing, FAQ, ad copy, content repurposing, headlines, copy variants, LinkedIn ads, Google ads, content transformation

## Quick Start

### Generate A/B Variants
```bash
python scripts/ab_variant_generator.py \
  --copy "See the Risk Before It Sees You" \
  --type headline \
  --variants 3
```

### Extract FAQ from Docs
```bash
python scripts/faq_generator.py \
  --docs "context/brand_strategy.md" \
  --questions 10
```

### Generate Ad Copy
```bash
python scripts/ad_copy_generator.py \
  --product "[PROJECT_NAME]" \
  --platform linkedin_sponsored \
  --offer "Free Risk Baseline"
```

### Repurpose Content
```bash
python scripts/content_repurposer.py \
  --source blog_post.md \
  --formats "linkedin,twitter,email,carousel,video"
```

## Key Scripts

### ab_variant_generator.py
Generate A/B test variants for headlines, CTAs, or body copy.

### faq_generator.py
Extract frequently asked questions from documentation.

### ad_copy_generator.py
Generate platform-optimized ad copy within character limits.

### content_repurposer.py
Transform one piece of content into 5 different formats.

## Output Formats

Content repurposer creates:
1. LinkedIn post (1300 chars)
2. Twitter/X thread (10 tweets)
3. Email newsletter snippet
4. Carousel slide outline (8-10 slides)
5. Video script (60-90 seconds)
