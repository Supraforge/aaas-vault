---
name: analytics-tracking
description: >-
  When the user wants to set up, improve, or audit analytics tracking and
  measurement
version: 1.0.0
dependencies:
  - python3
  - curl
  - jq
inputs:
  - name: analytics_provider
    description: 'Analytics provider (google-analytics, amplitude, mixpanel, etc.)'
  - name: website_url
    description: URL of the website to track
outputs:
  - type: file
    description: Analytics implementation plan and code snippets
  - type: stdout
    description: Configuration instructions and verification steps
compatibility: 'agent-zero, claude-code, cursor'
---

# Analytics Tracking

## 🎯 Triggers
- When user wants to set up analytics tracking
- When user mentions "GA4", "Google Analytics", "conversion tracking"
- When user needs event tracking or UTM parameters
- When user wants to implement tag manager (GTM)
- When user needs analytics implementation or tracking plan

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/analytics-tracking/test.sh`.
- [ ] Check `.env` contains required API keys (if applicable).

## 📋 Workflow
1. **Context Load**: Scan `context/` for project-specific analytics requirements.
2. **Ingest**: Analyze current analytics setup and identify gaps.
3. **Execute**: Generate implementation plan with code snippets.
4. **Verify**: Provide verification steps to ensure tracking works.

## 🛠️ Script Reference
- Use `scripts/analytics_setup.py` for generating analytics implementation.
- Use `scripts/tracking_verifier.py` for verifying tracking implementation.

## 📊 Supported Analytics Providers
- Google Analytics 4 (GA4)
- Google Tag Manager (GTM)
- Amplitude
- Mixpanel
- Segment
- Matomo
- Plausible Analytics

## 🔧 Implementation Steps
1. **Assessment**: Review current analytics setup
2. **Planning**: Create tracking plan with events and parameters
3. **Implementation**: Generate code snippets for selected provider
4. **Testing**: Create verification scripts
5. **Documentation**: Provide setup instructions

## 📁 Templates
- `templates/google_analytics.html` - Google Analytics implementation template
- `templates/google_tag_manager.html` - Google Tag Manager template
- `templates/tracking_plan.md` - Tracking plan template
