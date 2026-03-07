---
name: pr-communications
description: Generate press releases and investor communications. Includes press release generator with AP style formatting and boilerplate, and monthly investor update generator with metrics templates. Use for company announcements, product launches, funding news, or investor updates.
license: MIT
metadata:
  version: 1.0.0
  author: [PROJECT_NAME] AI
  category: marketing
  domain: pr-communications
  updated: 2026-02-12
  python-tools: press_release_generator.py, investor_update_generator.py, boilerplate_manager.py
  tech-stack: Python, Markdown
  integrations: brand-qa, content-operations
---

# PR Communications

Generate professional press releases and investor communications.

## Keywords

press release, PR, investor update, company announcement, product launch, funding news, boilerplate, media relations, investor relations

## Quick Start

### Generate Press Release
```bash
python scripts/press_release_generator.py \
  --type product_launch \
  --headline "[PROJECT_NAME] Launches Real-Time Compliance" \
  --city "Munich"
```

### Generate Investor Update
```bash
python scripts/investor_update_generator.py \
  --period "February 2026" \
  --highlights "Signed first enterprise customer, Launched beta"
```

### Manage Boilerplate
```bash
python scripts/boilerplate_manager.py get [PROJECT_NAME]
python scripts/boilerplate_manager.py update [PROJECT_NAME] --file new_about.md
```

## Key Scripts

### press_release_generator.py
Generate AP-style press releases with boilerplate.

**Types:** product_launch, partnership, funding, milestone, event

### investor_update_generator.py
Generate monthly/quarterly investor update emails.

**Sections:** TL;DR, Metrics, Highlights, Challenges, Asks, Next Steps

### boilerplate_manager.py
Manage company boilerplate text for press releases.

## Press Release Format

1. **Headline** (max 10 words)
2. **Subheadline** (optional)
3. **Dateline** (City, Date)
4. **Lead Paragraph** (who, what, when, where, why)
5. **Key Highlights** (3-5 bullets)
6. **Quote** (executive commentary)
7. **Availability** (optional)
8. **About Section** (boilerplate)
9. **Media Contact**

## Investor Update Format

1. **TL;DR** (3-5 bullets)
2. **Key Metrics** (MRR, customers, pipeline, runway)
3. **Highlights** (product, customers, team)
4. **Challenges** (optional, be transparent)
5. **Asks** (how investors can help)
6. **What's Next** (priorities)
