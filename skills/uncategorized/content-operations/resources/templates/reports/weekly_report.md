---
id: weekly_report
name: Weekly Activity Report
category: reports
tags: [report, weekly, summary]
description: Weekly activity and progress report template
variables:
  - name: week_of
    required: true
    description: Week start date
  - name: accomplishments
    required: true
    description: Key accomplishments this week
  - name: in_progress
    required: false
    description: Work currently in progress
  - name: blockers
    required: false
    description: Current blockers or challenges
  - name: next_week
    required: true
    description: Priorities for next week
  - name: metrics
    required: false
    description: Key metrics or KPIs
  - name: author
    required: false
    default: Team
---

# Weekly Report

**Week of:** {{ week_of }}
**Author:** {{ author }}
**Generated:** {{ date }}

---

## Summary

[One-paragraph summary of the week]

---

## Accomplishments

{{ accomplishments }}

---

{% if in_progress %}
## In Progress

{{ in_progress }}

{% endif %}

---

{% if blockers %}
## Blockers & Challenges

{{ blockers }}

{% endif %}

---

## Next Week Priorities

{{ next_week }}

---

{% if metrics %}
## Key Metrics

{{ metrics }}

{% endif %}

---

## Notes

[Any additional notes or context]

---

*Report template from Content Operations skill*
