---
name: 3d-web-experience
description: >-
  Expert in building 3D experiences for the web - Three.js, React Three Fiber,
  Spline, WebGL, and interactive 3D scenes for marketing and immersive content
version: 1.0.0
dependencies:
  - nodejs
  - npm
  - python3
inputs:
  - name: project_type
    description: >-
      Type of 3D project (product-configurator, portfolio, immersive-website,
      interactive-scene)
  - name: target_platform
    description: 'Target platform (web, mobile-web, desktop)'
outputs:
  - type: file
    description: 3D implementation plan with code examples and optimization recommendations
compatibility: 'agent-zero, claude-code, cursor'
---

# 3D Web Experience for Marketing & Content Creation

## 🎯 Triggers
- User wants to create immersive 3D marketing experiences
- Need interactive product configurators for e-commerce
- Building 3D portfolios or immersive websites
- Creating scroll-driven 3D content for storytelling
- Implementing 3D visualizations for marketing campaigns

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/3d-web-experience/test.sh`.
- [ ] Check `.env` contains required keys (if applicable).

## 📋 Workflow
1. **Context Load**: Analyze project requirements and constraints
2. **Stack Selection**: Choose appropriate 3D technology stack based on project needs
3. **Model Pipeline**: Guide through 3D model preparation and optimization
4. **Implementation**: Provide code examples and implementation patterns
5. **Optimization**: Ensure performance and mobile compatibility

## 🛠️ Script Reference
- Use `scripts/3d_stack_selector.py` for technology stack recommendations
- Use `scripts/model_optimizer.py` for 3D model preparation guidance
- Use `scripts/scroll_integration.py` for scroll-driven 3D implementations

## 📊 Technology Stack Selection

### Options Comparison
| Tool | Best For | Learning Curve | Control | Marketing Use Cases |
|------|----------|----------------|---------|-------------------|
| Spline | Quick prototypes, designers | Low | Medium | Interactive ads, quick demos |
| React Three Fiber | React apps, complex scenes | Medium | High | E-commerce configurators, portfolios |
| Three.js vanilla | Max control, non-React | High | Maximum | Custom marketing experiences |
| Babylon.js | Games, heavy 3D | High | Maximum | Immersive brand experiences |

### Decision Tree
```
Need quick marketing demo?
└── Yes → Spline
└── No → Continue

Using React for marketing site?
└── Yes → React Three Fiber
└── No → Continue

Need max performance/control for brand experience?
└── Yes → Three.js vanilla
└── No → Spline or R3F
```

## 🎨 Marketing-Focused Implementation Patterns

### Product Configurators (E-commerce)
- Interactive 3D product viewers
- Customization interfaces
- Real-time material/color changes
- Integration with shopping carts

### Immersive Storytelling
- Scroll-driven 3D narratives
- Interactive brand journeys
- Animated transitions between scenes
- Emotional engagement through 3D

### Portfolio Enhancement
- 3D project showcases
- Interactive case studies
- Dynamic background elements
- Engaging user interactions

## 📱 Mobile Optimization for Marketing
- Reduced quality on mobile devices
- Touch-friendly interactions
- Performance monitoring
- Battery consumption awareness

## ⚠️ Anti-Patterns for Marketing

### ❌ 3D For 3D's Sake
**Why bad**: Slows down conversion, confuses users, drains mobile battery
**Instead**: 3D should enhance message, not distract from it

### ❌ Desktop-Only Experiences
**Why bad**: Most traffic is mobile, excludes majority of audience
**Instead**: Mobile-first design with graceful degradation

### ❌ No Clear Call-to-Action
**Why bad**: Beautiful but ineffective marketing
**Instead**: Integrate CTAs naturally within 3D experience
