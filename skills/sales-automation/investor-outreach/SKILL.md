---
name: investor-outreach
description: >-
  Automated email outreach for investor relations, using A/B-tested templates
  and autonomous AI proxy integration.
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---
# 📧 Investor Outreach Skill

Automated email outreach for investor relations, using A/B-tested templates and autonomous AI proxy integration.

## 🛠️ Configuration

1. **Credentials**: Ensure the following are set in your `.env` file:
   - `INVESTOR_GMAIL_USER`: The Gmail address used for outreach.
   - `INVESTOR_GMAIL_PASSWORD`: The Gmail **App Password** (not your regular password).
2. **Templates**: Managed in `resources/templates.json`.
3. **Drafts**: (Future) Review generated drafts in the `output/` folder before sending.

## 📋 Available Templates (A/B Testing)

| ID | Name | Focus |
| :--- | :--- | :--- |
| `traction-first` | Traction First | Credibility via big logos (VW/Audi). Strongest for cold outreach. |
| `tech-forward` | Tech-Forward | The Avatar/Proxy as the curiosity hook. Proves AI-native capability. |
| `problem-solution` | Problem/Solution | Specific pain point of manual compliance documentation. |

## 🚀 Execution

### 1. Send an Individual Email

```bash
python3 skills/investor-outreach/scripts/investor_mailer.py \
  --to "investor@example.com" \
  --template "traction-first" \
  --name "Sarah" \
  --attach "path/to/pitch_deck_v2.pdf"
```

### 2. Batch Sending (Coming Soon)

A script to iterate over a CSV of discovered investors and rotate templates for A/B testing.

## ⚠️ Best Practices

- **Tone**: Keep it "Vitreous, Authoritative, and Calm" as per the [PROJECT_NAME] Brand Strategy.
- **Testing**: Always send a test email to yourself first to verify formatting.
- **Spam**: Use a dedicated account and limit volume to avoid Gmail's spam filters.

## 🔗 Integrated Context

- **Avatar**: All emails link to the [Interactive Pitch Deck](https://www.supra-forge.com/pitch-deck.html).
- **Persona**: Follows the "Split Persona - Investor" logic (Analytical, Skeptical-friendly).
