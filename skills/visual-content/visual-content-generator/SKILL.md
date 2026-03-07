---
name: visual-content-generator
description: Generate visual content assets for social media. Includes carousel PDF generator and multi-platform social asset batch generator. Creates LinkedIn carousels, Instagram posts, Twitter images from content briefs. Use for visual content creation, carousel design, or social media asset batches.
license: MIT
metadata:
  version: 1.0.0
  author: [PROJECT_NAME] AI
  category: marketing
  domain: visual-content
  updated: 2026-02-12
  node-tools: carousel_generator.js, social_asset_batch.js
  tech-stack: Node.js, Sharp, Puppeteer, PDFKit
  integrations: visual-designer, content-operations
---

# Visual Content Generator

Generate visual content assets for social media at scale.

## Keywords

carousel, social media assets, LinkedIn carousel, PDF generator, image batch, social graphics, visual content, instagram posts, twitter images

## Quick Start

### Generate Carousel PDF
```bash
node scripts/carousel_generator.js content_brief.md --theme dark --brand [PROJECT_NAME]
```

### Generate Multi-Platform Assets
```bash
node scripts/social_asset_batch.js content_brief.md --platforms "linkedin,twitter,instagram"
```

## Key Scripts

### carousel_generator.js
Generate LinkedIn carousel PDFs from content briefs.

**Usage:**
```bash
node scripts/carousel_generator.js <brief.md> [options]

Options:
  --theme     dark|light (default: dark)
  --brand     Brand slug (default: [PROJECT_NAME])
  --output    Output directory
  --slides    Number of slides (default: auto)
```

### social_asset_batch.js
Generate assets for multiple platforms from single brief.

**Usage:**
```bash
node scripts/social_asset_batch.js <brief.md> [options]

Options:
  --platforms  Comma-separated list (linkedin,twitter,instagram)
  --output     Output directory
  --brand      Brand slug
```

## Platform Dimensions

| Platform | Post | Story | Header |
|----------|------|-------|--------|
| LinkedIn | 1200x1200 | 1080x1920 | 1584x396 |
| Twitter | 1200x675 | - | 1500x500 |
| Instagram | 1080x1080 | 1080x1920 | - |

## Integration

Extends the `visual-designer` skill with specialized generators.
Uses `content-operations` templates for carousel content.
