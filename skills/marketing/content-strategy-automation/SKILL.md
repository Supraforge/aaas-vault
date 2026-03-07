---
name: content-strategy-automation
description: >-
  Automates content strategy, creation, distribution, and analytics using AI and
  marketing APIs
version: 1.0.0
dependencies:
  - python3
  - openai
  - requests
  - pandas
  - schedule
  - google-api-python-client
inputs:
  - name: topic
    description: Main topic or keyword for content strategy
  - name: target_audience
    description: Target audience description
  - name: content_channels
    description: 'Comma-separated list of content channels (blog,social,email,etc.)'
outputs:
  - type: file
    description: Content calendar CSV file
  - type: file
    description: Content performance report
  - type: stdout
    description: Strategy recommendations and next steps
compatibility: 'agent-zero, claude-code, cursor'
---

# Content Strategy Automation

## 🎯 Triggers
- User needs a comprehensive content marketing strategy
- User wants to automate content creation and distribution
- User needs content performance analytics
- User wants AI-powered content recommendations

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/content-strategy-automation/test.sh`.
- [ ] Check `.env` contains required API keys (OpenAI, Google Analytics, etc.).
- [ ] Ensure Python dependencies are installed via `install.sh`.

## 📋 Workflow
1. **Strategy Development**: Analyze topic and audience to create content pillars
2. **Content Creation**: Generate AI-powered content for different formats
3. **Calendar Planning**: Schedule content across channels with optimal timing
4. **Distribution Automation**: Post to social media, blogs, and email
5. **Performance Tracking**: Monitor analytics and optimize strategy

## 🛠️ Script Reference
- Use `scripts/content_strategy.py` for strategy development
- Use `scripts/content_generator.py` for AI content creation
- Use `scripts/calendar_planner.py` for scheduling
- Use `scripts/distribution_automation.py` for posting
- Use `scripts/analytics_tracker.py` for performance monitoring

## 🔧 API Integration
- **OpenAI API**: For content generation and optimization
- **Google Analytics API**: For performance tracking
- **Social Media APIs**: For automated posting (Twitter, LinkedIn, Facebook)
- **Email Marketing APIs**: For newsletter distribution

## 📊 Output Examples
- Content calendar with publishing schedule
- Performance dashboard with key metrics
- ROI analysis and optimization recommendations
- Competitor content analysis
