---
name: sales-enablement
description: Generate sales emails, meeting briefs, follow-ups, and handle objections. Includes email sequence writer, follow-up generator, meeting prep with company intel, and searchable objection database. Use for nurture sequences, pre-call research, post-meeting follow-ups, or finding responses to common objections.
license: MIT
metadata:
  version: 1.0.0
  author: [PROJECT_NAME] AI
  category: sales
  domain: sales-enablement
  updated: 2026-02-12
  python-tools: email_sequence_writer.py, follow_up_writer.py, meeting_brief_generator.py, objection_handler.py
  tech-stack: Python, JSON
  integrations: brand-qa, content-operations
---

# Sales Enablement

Sales support tools for email sequences, meeting preparation, follow-ups, and objection handling.

## Keywords

sales emails, nurture sequence, follow-up, meeting prep, objection handling, sales enablement, b2b sales, email outreach, pre-call research, sales collateral

## Quick Start

### Generate Email Sequence
```bash
python scripts/email_sequence_writer.py \
  --prospect '{"name": "John", "company": "Acme", "pain_point": "compliance overhead"}' \
  --type nurture
```

### Generate Meeting Brief
```bash
python scripts/meeting_brief_generator.py \
  --company "BMW Group" \
  --contact "Hans Mueller" \
  --type discovery
```

### Search Objections
```bash
python scripts/objection_handler.py search "too expensive"
```

### Generate Follow-Up
```bash
python scripts/follow_up_writer.py \
  --prospect "John" \
  --meeting-notes "Discussed compliance challenges, interested in demo"
```

## Core Workflows

### 1. Pre-Meeting Preparation
1. Generate meeting brief with company intel
2. Review likely pain points
3. Prepare discovery questions
4. Know objection responses

### 2. Post-Meeting Follow-Up
1. Generate follow-up email from notes
2. Include key discussion points
3. Propose clear next steps
4. Send within 2 hours

### 3. Nurture Sequence Creation
1. Define prospect profile
2. Generate 5-email sequence
3. Validate with brand-qa
4. Load into email tool

## Key Scripts

### email_sequence_writer.py
Generate multi-email nurture sequences.

**Usage:**
```bash
python scripts/email_sequence_writer.py \
  --prospect '{"name": "John", "company": "Acme", "pain_point": "audit prep"}' \
  --type nurture \
  --emails 5 \
  --brand [PROJECT_NAME]
```

### meeting_brief_generator.py
Generate pre-call intelligence briefs.

**Usage:**
```bash
python scripts/meeting_brief_generator.py \
  --company "Target Company" \
  --contact "Contact Name" \
  --type discovery \
  --context "Met at conference"
```

### follow_up_writer.py
Generate post-meeting follow-up emails.

**Usage:**
```bash
python scripts/follow_up_writer.py \
  --prospect "John" \
  --meeting-notes "Key discussion points" \
  --next-steps "Schedule demo"
```

### objection_handler.py
Search and manage objection responses.

**Usage:**
```bash
# Search objections
python scripts/objection_handler.py search "budget"

# Add new objection
python scripts/objection_handler.py add \
  --objection "We need to check with IT" \
  --response "Happy to include them..." \
  --category authority
```

## Objection Categories

- **price**: Budget and cost concerns
- **timing**: Not the right time
- **competition**: Using another solution
- **technical**: Technical requirements
- **authority**: Need approval from others

## Integration

Uses Google Calendar booking link for meeting scheduling.
Validates content with brand-qa skill.
Uses templates from content-operations skill.
