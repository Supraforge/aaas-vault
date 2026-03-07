---
id: investor_update
name: Monthly Investor Update
category: email
tags: [investor, monthly, update, fundraising]
description: Monthly investor update email template
variables:
  - name: month
    required: true
    description: Month name (e.g., January 2026)
  - name: highlights
    required: true
    description: 3-5 key highlights from the month
  - name: metrics
    required: true
    description: Key metrics (MRR, customers, pipeline, etc.)
  - name: challenges
    required: false
    description: Current challenges
  - name: asks
    required: false
    description: Specific asks from investors
  - name: sender_name
    required: false
    default: Tobias
  - name: company_name
    required: false
    default: SUPRA FORGE
---

# Monthly Investor Update

**Subject:** {{ company_name }} | {{ month }} Update

Dear Investors,

Here's your monthly update on {{ company_name }} progress.

---

## TL;DR

{{ highlights }}

---

## Key Metrics

{{ metrics }}

---

## Highlights

### Product
[Product developments this month]

### Customers
[Customer wins, expansion, churn]

### Team
[Hiring, organizational updates]

---

{% if challenges %}
## Challenges

{{ challenges }}

{% endif %}

---

{% if asks %}
## Asks

How you can help this month:

{{ asks }}

{% endif %}

---

## What's Next

[Key priorities for next month]

---

Thank you for your continued support.

Best,
{{ sender_name }}
Founder & CEO, {{ company_name }}

---

## Template Notes

- Send on first Monday of each month
- Keep TL;DR to 3-5 bullet points
- Be honest about challenges - investors appreciate transparency
- Make asks specific and actionable
- Include one thing investors can share/help with
