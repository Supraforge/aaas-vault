---
id: nurture_sequence
name: 5-Email Nurture Sequence
category: email
tags: [nurture, b2b, sales, sequence]
description: A 5-email sequence to nurture prospects from awareness to consideration
variables:
  - name: prospect_name
    required: true
    description: Prospect's first name
  - name: company_name
    required: true
    description: Prospect's company name
  - name: pain_point
    required: true
    description: Primary pain point to address
  - name: product_name
    required: false
    default: [PROJECT_NAME]
  - name: booking_link
    required: false
    default: https://calendar.google.com
  - name: sender_name
    required: false
    default: Tobias
---

# 5-Email Nurture Sequence

## Email 1: Problem Awareness (Day 0)

**Subject:** {{ prospect_name }}, is {{ pain_point }} costing you more than you think?

Hi {{ prospect_name }},

I've been following {{ company_name }}'s work in the industry, and I noticed something that might resonate with you.

Most engineering teams we talk to spend 40% of their time on {{ pain_point }}. That's nearly half their capacity diverted from actual innovation.

The question isn't whether this is happening - it's what the hidden cost really is.

I put together a quick framework for calculating this. Would it be useful if I shared it with you?

Best,
{{ sender_name }}

---

## Email 2: Insight Share (Day 3)

**Subject:** The 40% tax nobody talks about

Hi {{ prospect_name }},

Following up on my last note about {{ pain_point }}.

Here's what we've learned from working with teams like yours:

**The Real Cost:**
- 40% of engineering time on administration
- 3-month feedback loops creating blind spots
- Critical issues discovered too late to fix efficiently

**The Pattern:**
Teams don't notice it because it's "just how things are done." But once you see it, you can't unsee it.

One VP of Engineering told us: "We thought compliance was just expensive. We didn't realize it was also making us blind."

Does this match what you're seeing at {{ company_name }}?

Best,
{{ sender_name }}

---

## Email 3: Solution Introduction (Day 7)

**Subject:** What if {{ pain_point }} became a by-product?

Hi {{ prospect_name }},

Imagine if {{ pain_point }} wasn't a separate activity - but happened automatically as a by-product of your existing workflow.

That's the approach behind {{ product_name }}.

Instead of manual documentation and periodic audits, you get:
- Continuous visibility into compliance status
- Automated traceability across your tools
- Real-time risk detection before issues compound

The teams using it describe it as having "Waze for compliance" - they see the risks before the risks see them.

Would a 15-minute demo be worth your time to see if this applies to {{ company_name }}?

Best,
{{ sender_name }}

---

## Email 4: Social Proof (Day 12)

**Subject:** How [Similar Company] reduced compliance overhead by 60%

Hi {{ prospect_name }},

Quick case study I thought you'd find relevant:

A Tier-1 automotive supplier was facing the same {{ pain_point }} challenge as most teams. They were spending 3+ months preparing for each audit, with engineers pulled off feature work to gather evidence.

After implementing {{ product_name }}:
- Audit prep time: 3 months → 2 days
- Engineering time reclaimed: 40% → available for innovation
- Compliance visibility: Quarterly → Real-time

The shift wasn't just efficiency - it was seeing risks early enough to actually prevent them.

I'd be happy to walk you through how this might look for {{ company_name }}.

[Book a conversation]({{ booking_link }})

Best,
{{ sender_name }}

---

## Email 5: Direct Ask (Day 18)

**Subject:** Quick question, {{ prospect_name }}

Hi {{ prospect_name }},

I've shared a few thoughts on {{ pain_point }} over the past few weeks. Before I assume this isn't a priority, I wanted to ask directly:

1. Is {{ pain_point }} something {{ company_name }} is actively trying to solve?
2. If so, would a 15-minute conversation make sense?

If the timing isn't right, just let me know - I won't keep filling your inbox.

Either way, I appreciate your time.

Best,
{{ sender_name }}

[Book a time that works]({{ booking_link }})

---

## Sequence Notes

**Timing:** Send emails on business days, ideally Tuesday-Thursday mornings
**Personalization:** Research company before sending - add specific references
**Tracking:** Monitor opens and clicks to gauge engagement
**Follow-up:** If no response after Email 5, add to monthly newsletter list
