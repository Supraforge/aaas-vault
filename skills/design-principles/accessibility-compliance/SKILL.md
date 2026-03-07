---
name: accessibility-compliance
description: >-
  Implements WCAG 2.2 compliant interfaces with mobile accessibility, inclusive
  design patterns, and assistive technology support.
version: 1.0.0
dependencies:
  - node
  - python3
  - axe-core
  - lighthouse
compatibility: 'agent-zero, claude-code, cursor'
---

# Accessibility Compliance Skill

This skill ensures web interfaces comply with WCAG 2.2 standards, providing accessibility auditing, ARIA pattern implementation, and inclusive design guidance.

## 🎯 Triggers
- "Audit this website for accessibility compliance"
- "Check if my interface follows WCAG 2.2 standards"
- "Implement ARIA patterns for screen reader support"
- "Fix accessibility violations in my web application"
- "Test mobile accessibility for VoiceOver/TalkBack"

## ⚡ Quick Start (Self-Check)
- [ ] Run `bash ~/.gemini/skills/accessibility-compliance/test.sh`

## 📋 Workflow
1. **Ingest**: Analyze the user's request for accessibility compliance needs.
2. **Execute**: Run appropriate accessibility testing tools and provide implementation guidance.
3. **Verify**: Review test results and provide actionable fixes for violations.

## Core Capabilities

### 1. WCAG 2.2 Guidelines Implementation
- **Perceivable**: Ensure content is presentable in different ways
- **Operable**: Make interfaces navigable with keyboard and assistive tech
- **Understandable**: Ensure content and operation are clear
- **Robust**: Ensure content works with current and future assistive technologies

### 2. ARIA Pattern Implementation
- **Roles**: Define element purpose (button, dialog, navigation)
- **States**: Indicate current condition (expanded, selected, disabled)
- **Properties**: Describe relationships and additional info (labelledby, describedby)
- **Live regions**: Announce dynamic content changes

### 3. Keyboard Navigation Support
- Focus order and tab sequence management
- Focus indicators and visible focus states
- Keyboard shortcuts and hotkeys
- Focus trapping for modals and dialogs

### 4. Screen Reader Compatibility
- Semantic HTML structure
- Alternative text for images
- Proper heading hierarchy
- Skip links and landmarks

### 5. Mobile Accessibility
- Touch target sizing (44x44dp minimum)
- VoiceOver and TalkBack compatibility
- Gesture alternatives
- Dynamic Type support

## WCAG 2.2 Success Criteria Checklist

| Level | Criterion | Description                                          |
| ----- | --------- | ---------------------------------------------------- |
| A     | 1.1.1     | Non-text content has text alternatives               |
| A     | 1.3.1     | Info and relationships programmatically determinable |
| A     | 2.1.1     | All functionality keyboard accessible                |
| A     | 2.4.1     | Skip to main content mechanism                       |
| AA    | 1.4.3     | Contrast ratio 4.5:1 (text), 3:1 (large text)        |
| AA    | 1.4.11    | Non-text contrast 3:1                                |
| AA    | 2.4.7     | Focus visible                                        |
| AA    | 2.5.8     | Target size minimum 24x24px (NEW in 2.2)             |
| AAA   | 1.4.6     | Enhanced contrast 7:1                                |
| AAA   | 2.5.5     | Target size minimum 44x44px                          |

## 🤖 System Instructions

1. **Use Automated Testing Tools**:
   - For web accessibility: Use axe-core or Lighthouse
   - For mobile: Use iOS Accessibility Inspector or Android Accessibility Scanner
   
2. **Provide Implementation Guidance**:
   - When violations are found, provide specific code examples to fix them
   - Include both HTML/JSX examples and testing commands
   
3. **Check Color Contrast**:
   - Use contrast ratio calculators for text and UI elements
   - Ensure minimum ratios: 4.5:1 (AA), 7:1 (AAA)
   
4. **Verify Keyboard Navigation**:
   - Test tab order matches visual layout
   - Ensure all interactive elements are reachable via keyboard
   
5. **Screen Reader Testing**:
   - Verify semantic structure with screen reader emulators
   - Check ARIA attributes and live regions

## 🛠️ Testing Tools Reference
- **axe-core**: Automated accessibility testing for web
- **Lighthouse**: Google's auditing tool with accessibility checks
- **WAVE**: Web Accessibility Evaluation Tool
- **iOS Accessibility Inspector**: For VoiceOver compatibility
- **Android Accessibility Scanner**: For TalkBack compatibility

## Common Accessibility Anti-Patterns to Avoid
- **Missing alt text**: Images without descriptive alternatives
- **Poor color contrast**: Text that doesn't meet WCAG ratios
- **Keyboard traps**: Elements that can't be exited via keyboard
- **Missing focus indicators**: No visible focus for keyboard users
- **Auto-playing media**: Content that plays without user initiation
- **Inaccessible custom controls**: Recreating native functionality poorly
- **Missing skip links**: No way to bypass repetitive content
- **Focus order issues**: Tab order doesn't match visual order
