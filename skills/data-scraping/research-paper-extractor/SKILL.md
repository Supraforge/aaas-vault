---
name: research-paper-extractor
description: 'Extract text from cardiology research paper PDFs - **FREE, runs locally**.'
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---
# Research Paper Extractor

Extract text from cardiology research paper PDFs - **FREE, runs locally**.

## Cost: ZERO

- Text extraction: `pdfplumber` (free, local)
- Structuring: You ask me (Claude) in this conversation - you're already paying for the subscription

**No API calls. No extra costs.**

---

## How It Works

```
STEP 1: Extract text (free, local)
python scripts/extract_paper.py trial.pdf --output trial.md

STEP 2: Ask Claude (your existing subscription)
"Read trial.md and structure this for my content workflow"

DONE - No extra cost.
```

---

## Quick Start

### Install (one time)

```bash
pip3 install pdfplumber
```

### Extract text from PDF

```bash
# Save to file
python scripts/extract_paper.py paper.pdf --output extracted.md

# Just first 5 pages (faster)
python scripts/extract_paper.py paper.pdf --pages 5 --output extracted.md
```

### Then ask Claude Code

After extracting, just tell me:

> "Read /path/to/extracted.md and give me:
> - Study design, population, intervention
> - Primary/secondary endpoints with HR, CI, p-values
> - Safety data and conclusions
> - Content angles for YouTube, Twitter, Newsletter"

I'll structure it for your content workflow.

---

## Example Workflow

```bash
# 1. Download PDF from NEJM/JACC/Lancet

# 2. Extract text
python scripts/extract_paper.py ~/Downloads/declare-timi-58.pdf --output declare.md

# 3. In Claude Code:
#    "Read declare.md and structure the trial data.
#     Give me content angles for my YouTube channel."
```

**Output you'll get from me:**

```
DECLARE-TIMI 58 Summary:

Study: RCT, N=17,160, T2DM with CV risk
Intervention: Dapagliflozin 10mg vs placebo
Duration: 4.2 years median follow-up

Primary (MACE): HR 0.93 (0.84-1.03), p=0.17 - Non-inferior, not superior
Key Secondary (CV death/HF hosp): HR 0.83 (0.73-0.95), p=0.005 ✓

Content Angles:
🎬 YouTube: "SGLT2 inhibitors: The HF story hidden in a 'negative' trial"
🐦 Twitter: "DECLARE: Primary endpoint NS, but NNT 111 for HF hosp. Bury the lede much?"
📧 Newsletter: "Why 'negative' trials often have positive stories"
```

---

## Why This Approach?

| Approach | Cost |
|----------|------|
| ❌ Anthropic API per extraction | ~$0.05-0.15 per paper |
| ❌ OpenAI API per extraction | ~$0.05-0.20 per paper |
| ✅ **This approach** | **$0** - uses your subscription |

You're already paying for Claude Code. Use it.

---

## Integration with Your Skills

After I structure the data, you can use it with:

- `cardiology-trial-editorial` → Write 500-word editorial
- `x-post-creator-skill` → Generate tweets with accurate stats
- `youtube-script-master` → Script with verified data
- `cardiology-newsletter-writer` → Deep dive newsletter

---

## Limitations

- Works best with native PDFs (not scanned images)
- Very long papers: use `--pages 10` to extract key sections
- Tables may need manual review

---

*Zero cost. Maximum utility. Uses what you already pay for.*
