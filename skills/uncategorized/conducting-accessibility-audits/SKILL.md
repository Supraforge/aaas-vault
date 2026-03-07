---
name: conducting-accessibility-audits
description: >-
  Conducts comprehensive WCAG 2.2 accessibility audits with automated testing,
  manual verification, screen reader testing, and remediation guidance. Use when
  auditing websites for accessibility compliance, fixing WCAG violations, or
  implementing accessible design patterns.
version: 1.0.0
dependencies:
  - node
  - axe-core
  - puppeteer
  - screen-reader-testing
  - wcag-audit-patterns
compatibility: 'agent-zero, claude-code, cursor'
---

# Accessibility Compliance Auditing

Comprehensive accessibility auditing skill combining automated WCAG testing, manual verification, screen reader testing, and remediation guidance.

## 🎯 Triggers
- "Audit this website for accessibility compliance"
- "Check if this page meets WCAG 2.2 standards"
- "Test screen reader compatibility"
- "Find and fix accessibility violations"
- "Generate accessibility remediation report"
- "Verify ARIA implementations"
- "Test with VoiceOver/NVDA/JAWS"

## ⚡ Quick Start (Self-Check)
Before running complex audits, verify readiness:
- [ ] Run `bash ~/.gemini/skills/conducting-accessibility-audits/test.sh` to check dependencies
- [ ] Ensure Node.js and axe-core are installed
- [ ] Verify browser automation tools are available

## 📋 Workflow

### 1. Ingest: Analyze Accessibility Requirements
- Determine WCAG conformance level needed (A, AA, AAA)
- Identify target platforms (desktop, mobile, specific screen readers)
- Review existing accessibility statements or VPATs
- Gather user personas with disabilities for testing scenarios

### 2. Execute: Comprehensive Accessibility Testing

#### Phase 1: Automated Testing with axe-core
```bash
# Run automated accessibility scan
npx axe https://example.com --save results.json
# Or programmatically:
const axe = require('axe-core');
const puppeteer = require('puppeteer');
```

#### Phase 2: Manual WCAG Verification
- **Perceivable**: Check text alternatives, time-based media, adaptable content
- **Operable**: Verify keyboard accessibility, enough time, seizures
- **Understandable**: Test readable text, predictable operation, input assistance
- **Robust**: Validate compatibility with assistive technologies

#### Phase 3: Screen Reader Testing
- **NVDA + Firefox** (Windows, ~31% usage)
- **VoiceOver + Safari** (macOS/iOS, ~15% usage)
- **JAWS + Chrome** (Windows, ~40% usage)
- **TalkBack + Chrome** (Android, ~10% usage)
- **Narrator + Edge** (Windows, ~4% usage)

#### Phase 4: Visual Validation
- Color contrast ratios (minimum 4.5:1 for normal text)
- Focus indicators and tab order
- Responsive design at different zoom levels
- Text resizing without loss of content

### 3. Verify: Generate Compliance Report
- Summarize violations by WCAG success criteria
- Prioritize fixes by impact and effort
- Provide specific remediation code examples
- Include before/after screenshots
- Generate VPAT-ready documentation

## 🤖 System Instructions

### Core Principles
1. **Automate First**: Use axe-core for ~30-50% of detectable issues
2. **Manual Verification Required**: Automated tools miss context-dependent issues
3. **Real User Testing**: Include disabled users in testing process
4. **Semantic HTML First**: Use native HTML elements before ARIA
5. **Progressive Enhancement**: Ensure core functionality works without JavaScript

### Testing Priority Matrix
| Priority | Test Type | Tools | Coverage |
|----------|-----------|-------|----------|
| **P1** | Automated | axe-core, Lighthouse | 30-50% |
| **P2** | Manual Keyboard | Manual testing | 100% |
| **P3** | Screen Readers | NVDA, VoiceOver, JAWS | Critical flows |
| **P4** | Color/Contrast | Color contrast analyzers | Visual elements |
| **P5** | Mobile/Responsive | Device emulators, real devices | All breakpoints |

### Common Violations & Fixes

#### 1. Missing Alternative Text
```html
<!-- Violation -->
<img src="chart.png">

<!-- Fix -->
<img src="chart.png" alt="Sales growth chart showing 15% increase Q3 2024">
```

#### 2. Insufficient Color Contrast
```css
/* Violation */
.button { color: #888; background: #eee; } /* 2.3:1 ratio */

/* Fix */
.button { color: #555; background: #fff; } /* 7.4:1 ratio */
```

#### 3. Missing Form Labels
```html
<!-- Violation -->
<input type="text" name="email">

<!-- Fix -->
<label for="email">Email address</label>
<input type="text" id="email" name="email">
```

#### 4. Keyboard Trap
```javascript
// Violation: Modal traps keyboard focus
modal.addEventListener('keydown', (e) => {
  if (e.key === 'Tab') {
    e.preventDefault(); // DON'T DO THIS
  }
});

// Fix: Manage focus properly
const focusableElements = modal.querySelectorAll('button, [href], input, select, textarea, [tabindex="0"]');
const firstElement = focusableElements[0];
const lastElement = focusableElements[focusableElements.length - 1];

modal.addEventListener('keydown', (e) => {
  if (e.key === 'Tab') {
    if (e.shiftKey) {
      if (document.activeElement === firstElement) {
        lastElement.focus();
        e.preventDefault();
      }
    } else {
      if (document.activeElement === lastElement) {
        firstElement.focus();
        e.preventDefault();
      }
    }
  }
  if (e.key === 'Escape') {
    closeModal();
  }
});
```

#### 5. Missing ARIA Landmarks
```html
<!-- Violation -->
<div class="header">...</div>
<div class="main">...</div>
<div class="footer">...</div>

<!-- Fix -->
<header role="banner">...</header>
<main role="main">...</main>
<footer role="contentinfo">...</footer>
```

## 🛠️ Script Reference

### Automated Testing Script
```javascript
// scripts/accessibility-scan.js
const axe = require('axe-core');
const puppeteer = require('puppeteer');

async function runAccessibilityScan(url) {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto(url);
  
  // Inject axe-core
  await page.addScriptTag({ path: require.resolve('axe-core') });
  
  // Run analysis
  const results = await page.evaluate(() => {
    return axe.run();
  });
  
  await browser.close();
  
  // Generate report
  const violations = results.violations.map(v => ({
    id: v.id,
    impact: v.impact,
    description: v.description,
    help: v.help,
    helpUrl: v.helpUrl,
    nodes: v.nodes.length
  }));
  
  return {
    url,
    timestamp: new Date().toISOString(),
    violations,
    passes: results.passes.length,
    incomplete: results.incomplete.length,
    inapplicable: results.inapplicable.length
  };
}

module.exports = { runAccessibilityScan };
```

### Screen Reader Testing Checklist
```bash
# test.sh includes:
echo "Testing with NVDA..."
echo "1. Navigate page with Tab/Shift+Tab"
echo "2. Use arrow keys to navigate lists"
echo "3. Test form controls with Space/Enter"
echo "4. Verify landmarks with screen reader shortcuts"
echo "5. Check dynamic content announcements"
```

### WCAG Compliance Report Template
```markdown
# Accessibility Compliance Report

## Executive Summary
- **Website**: {{URL}}
- **Audit Date**: {{DATE}}
- **WCAG Version**: 2.2
- **Target Level**: AA
- **Overall Score**: {{SCORE}}/100

## Critical Issues (P0)
1. **Missing form labels** - 15 instances
   - Impact: High
   - WCAG: 3.3.2 Labels or Instructions
   - Fix: Add <label> elements with for attributes

2. **Insufficient color contrast** - 8 instances
   - Impact: High
   - WCAG: 1.4.3 Contrast (Minimum)
   - Fix: Increase contrast ratio to at least 4.5:1

## Recommended Improvements (P1)
1. **Add skip navigation link**
2. **Improve focus indicators**
3. **Add ARIA landmarks**

## Testing Methodology
- Automated: axe-core v4.7.2
- Manual: Keyboard testing, screen reader testing
- Platforms: Windows 11, macOS Ventura, iOS 17
- Screen Readers: NVDA 2023.3, VoiceOver (macOS), JAWS 2023

## Appendix: Detailed Findings
{{DETAILED_FINDINGS}}
```

## 📊 Success Metrics
- **Automated Test Coverage**: >40% of WCAG success criteria
- **Manual Test Coverage**: 100% of critical user journeys
- **Screen Reader Coverage**: NVDA, VoiceOver, JAWS minimum
- **Remediation Rate**: >90% of critical issues resolved
- **VPAT Compliance**: Ready for legal documentation

## 🔗 Resources
- [WCAG 2.2 Guidelines](https://www.w3.org/TR/WCAG22/)
- [axe-core Documentation](https://github.com/dequelabs/axe-core)
- [WebAIM Checklist](https://webaim.org/standards/wcag/checklist)
- [Screen Reader User Survey](https://webaim.org/projects/screenreadersurvey/)
- [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
- [Color Contrast Checker](https://webaim.org/resources/contrastchecker/)
