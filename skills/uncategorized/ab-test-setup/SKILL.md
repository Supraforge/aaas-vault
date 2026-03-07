---
name: ab-test-setup
description: Expert in A/B testing and experimentation
version: 1.0.0
dependencies:
  - python3
  - pandas
  - numpy
  - scipy
  - matplotlib
inputs:
  - name: hypothesis
    description: >-
      The hypothesis to test (e.g., "Changing button color increases
      conversions")
  - name: metrics
    description: 'Key metrics to track (e.g., "conversion_rate, click_through_rate")'
  - name: audience
    description: Target audience for the test
outputs:
  - type: file
    description: A/B test plan document
  - type: file
    description: Statistical analysis report
compatibility: 'agent-zero, claude-code, cursor'
---

# A/B Test Setup

## 🎯 Triggers
- User wants to plan, design, or implement an A/B test
- User mentions "A/B test", "split test", "experiment", "test this change"
- User needs help with "variant copy" or "multivariate test"
- User wants to validate a hypothesis with data

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/ab-test-setup/test.sh`.
- [ ] Ensure Python dependencies are installed.

## 📋 Workflow
1. **Hypothesis Formulation**: Define clear null and alternative hypotheses
2. **Test Design**: Determine sample size, duration, and success metrics
3. **Implementation Planning**: Create technical specifications for developers
4. **Analysis Preparation**: Set up statistical tests and reporting framework
5. **Results Interpretation**: Analyze data and make recommendations

## 🛠️ Script Reference
- Use `scripts/ab_test_designer.py` for calculating sample sizes and test duration
- Use `scripts/statistical_analyzer.py` for analyzing test results

## 📊 Templates
- Find test plan templates in `templates/` folder
- Use `templates/test_plan.md` for documenting your experiment

## 📈 Best Practices
- Always calculate required sample size before running tests
- Use proper randomization techniques
- Monitor for statistical significance, not just raw differences
- Consider practical significance alongside statistical significance
- Document everything for reproducibility
