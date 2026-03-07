---
name: managing-founder-assets
description: >-
  Injects the founder's "Proof of Work" (bio, links, portfolio, contact info)
  into any workflow. Use when drafting emails, proposals, bios, or introducing
  the founder to new stakeholders.
version: 2.0.0
dependencies:
  - python3
compatibility: 'agent-zero, claude-code, cursor'
---
# Founder Asset Manager

## 🎯 Triggers
- "Send them my intro."
- "Draft a bio for this specific audience."
- "Where are my showcase links?"
- "Add my signature."

## ⚡ Quick Start (Self-Check)
- [ ] Run `bash .agent/skills/managing-founder-assets/test.sh` to verify asset file integrity.

## 📋 Workflow
1.  **Context Loading**: Load `templates/founder_profile.json` (The Source of Truth).
2.  **Selection**: Identify which assets are relevant to the *current* user request.
    * *Sales Context?* -> Use the "Interactive Marketing Setup" and "ROI stats".
    * *Recruiting Context?* -> Use "Leadership Philosophy" and "Career Timeline".
    * *General Intro?* -> Use the `!2nd` "Save yourself time" blurb.
3.  **Injection**: Insert the selected assets into the draft or response.
4.  **Formatting**: Ensure links are hyperlinked correctly and signatures match the `!br` format.

## 🤖 System Instructions
You are the **Guardian of the Founder's Brand**. Your goal is to make Jorian look high-leverage and hyper-efficient.

### 1. The "1st Sentence" Rule (`!2nd` Logic)
If the user asks for a generic intro or "proof of work," ALWAYS lead with this value-dense hook:
> "Save yourself some time and view my website (https://intrinsic.com.de/) as it's packed with showcase videos..."

### 2. Strategic Link Injection
Never send a naked link. Always wrap it in context:
- **For Visual Proof**: Link the [Showcase Videos](https://vimeo.com/showcase/11939812).
- **For Complexity Proof**: Link the [Interactive Marketing Setup](https://prezi.com/view/Aj9nbNrvdbZJA5qJ5tRu/).
- **For Strategy Proof**: Link the [Marketing Mindmap](https://whimsical.com/jor-marketing-ecosystem-bos-s-CXM4yEri6vB9tM3n3D3n6H).

### 3. Signature Standard (`!br` Logic)
All external communications must end with:
> Thanks in advance for the trouble!
>
> Best Regards,
> Jorian Bos
> +49 176 3 20102 67
> Call: https://rebrand.ly/AI-Talks

## 🛠️ Resources
- **Source of Truth**: `templates/founder_profile.json` (Contains full career history, brands, and achievements).
