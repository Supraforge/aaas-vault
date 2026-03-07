---
id: press_release
name: Press Release Template
category: documents
tags: [pr, press-release, announcement]
description: Standard press release format for company announcements
variables:
  - name: headline
    required: true
    description: Main announcement headline (max 10 words)
  - name: subheadline
    required: false
    description: Supporting headline
  - name: city
    required: true
    description: City for dateline
  - name: date
    required: true
    description: Release date
  - name: lead_paragraph
    required: true
    description: The most important information (who, what, when, where, why)
  - name: key_facts
    required: true
    description: 3-5 supporting facts or features
  - name: quote_name
    required: true
    description: Name of person quoted
  - name: quote_title
    required: true
    description: Title of person quoted
  - name: quote_text
    required: true
    description: The quote itself
  - name: availability
    required: false
    description: Availability information
  - name: company_name
    required: false
    default: SUPRA FORGE
  - name: contact_name
    required: false
    default: Media Relations
  - name: contact_email
    required: false
    default: press@supra-forge.com
---

# {{ headline }}

{% if subheadline %}
*{{ subheadline }}*
{% endif %}

**{{ city }}, {{ date }}** — {{ lead_paragraph }}

## Key Highlights

{{ key_facts }}

## Executive Commentary

"{{ quote_text }}" said {{ quote_name }}, {{ quote_title }} at {{ company_name }}.

{% if availability %}
## Availability

{{ availability }}
{% endif %}

## About {{ company_name }}

{{ company_name }} develops [PROJECT_NAME], the Neural Quality Layer for automotive engineering. [PROJECT_NAME] enables automotive teams to achieve compliance at the speed of code by providing continuous visibility into ASPICE and ISO 26262 requirements. Unlike traditional compliance tools, [PROJECT_NAME] integrates as an invisible layer across existing engineering workflows, transforming compliance from a periodic burden into a continuous by-product of development.

For more information, visit [supra-forge.com](https://supra-forge.com).

## Media Contact

{{ contact_name }}
{{ company_name }}
{{ contact_email }}

###

---

## Press Release Guidelines

### Format
- Use inverted pyramid structure (most important first)
- Keep headline to 10 words or less
- Lead paragraph answers: Who, What, When, Where, Why
- Total length: 400-600 words

### Style
- Write in third person
- Use active voice
- Avoid jargon (or explain it)
- Include one strong quote

### Distribution
1. Post on company newsroom
2. Distribute via PR wire (if budget allows)
3. Send to relevant journalists directly
4. Share on LinkedIn with commentary
