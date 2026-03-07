# Ai Content Qa - Validations

## Content review should reference the brief

### **Id**
brief-referenced
### **Severity**
critical
### **Description**
QA without brief = guessing
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
review|QA|quality.*check
  #### **Exclude**
brief|requirement|objective|goal
### **Message**
Review may not reference brief. Always check content against documented requirements.
### **Autofix**


## QA reviewer should differ from creator

### **Id**
reviewer-not-creator
### **Severity**
critical
### **Description**
Fresh eyes find what tired eyes miss
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
self.*review|review.*own|I.*checked
  #### **Exclude**
peer|different|fresh.*eyes|another
### **Message**
Self-review detected. Content should be reviewed by someone other than the creator.
### **Autofix**


## Factual claims should be verified

### **Id**
facts-verified
### **Severity**
high
### **Description**
AI hallucinates; humans verify
### **Pattern**
  #### **File Glob**
**/*.{yaml,md,txt}
  #### **Match**
\d+%|studies.*show|research.*indicates|according.*to
  #### **Exclude**
source|verified|confirmed|citation
### **Message**
Content may contain unverified claims. Verify all statistics and facts before approval.
### **Autofix**


## Content should meet platform requirements

### **Id**
platform-compliance
### **Severity**
high
### **Description**
Truncated content wastes spend
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
headline|primary.*text|description
  #### **Exclude**
char|limit|platform|truncat|length
### **Message**
Content may not verify platform requirements. Check character limits and specs.
### **Autofix**


## Call to action should be present and functional

### **Id**
cta-verified
### **Severity**
high
### **Description**
No CTA = wasted attention
### **Pattern**
  #### **File Glob**
**/*.{yaml,md,txt}
  #### **Match**
ad|content|copy
  #### **Exclude**
CTA|call.*action|get|start|download|book|sign.*up|learn.*more
### **Message**
Content may lack verified CTA. Ensure call to action is present and functional.
### **Autofix**


## Content should align with brand guidelines

### **Id**
brand-consistency
### **Severity**
high
### **Description**
Off-brand content confuses customers
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
content|copy|messaging
  #### **Exclude**
brand|voice|guideline|tone|style.*guide
### **Message**
Content may not be checked against brand guidelines. Verify brand compliance.
### **Autofix**


## QA feedback should be specific and actionable

### **Id**
feedback-specific
### **Severity**
medium
### **Description**
Vague feedback doesn't improve content
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
doesn.*work|not.*right|needs.*improvement|could.*better
  #### **Exclude**
specific|example|instead|try|change.*to
### **Message**
QA feedback may be vague. Provide specific, actionable feedback with examples.
### **Autofix**


## Review should cover multiple levels

### **Id**
multi-level-review
### **Severity**
medium
### **Description**
Surface-only review misses strategic errors
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
spell|grammar|typo
  #### **Exclude**
message|strategy|brand|objective|brief
### **Message**
Review may be surface-level only. Check strategic alignment, not just grammar.
### **Autofix**


## QA should use objective criteria

### **Id**
objective-standards
### **Severity**
medium
### **Description**
Subjective blocking kills velocity
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
don.*like|would.*differently|not.*right
  #### **Exclude**
standard|requirement|guideline|brief|criteria
### **Message**
QA may be using subjective criteria. Base decisions on documented standards.
### **Autofix**


## All links and functionality should be verified

### **Id**
links-checked
### **Severity**
medium
### **Description**
Broken links damage credibility
### **Pattern**
  #### **File Glob**
**/*.{yaml,md,txt}
  #### **Match**
http|link|url|CTA
  #### **Exclude**
test|verify|check|functional
### **Message**
Content may contain unchecked links. Verify all links are functional.
### **Autofix**


## Common issues should be documented

### **Id**
patterns-documented
### **Severity**
low
### **Description**
Catching without teaching wastes effort
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
common.*error|repeat.*issue|same.*mistake
  #### **Exclude**
document|checklist|training|pattern|learning
### **Message**
Repeated issues may not be documented. Track patterns for systemic improvement.
### **Autofix**


## QA turnaround should be tracked

### **Id**
turnaround-tracked
### **Severity**
low
### **Description**
Bottleneck QA fails the system
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
waiting.*review|QA.*delay|slow.*review
  #### **Exclude**
SLA|turnaround|track|deadline
### **Message**
QA turnaround may not be tracked. Monitor and maintain SLAs.
### **Autofix**


## QA standards should be calibrated across reviewers

### **Id**
calibration-exists
### **Severity**
low
### **Description**
Inconsistent QA erodes trust
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
depend.*reviewer|different.*standard|inconsistent
  #### **Exclude**
calibrat|standard|document|align
### **Message**
QA standards may be inconsistent. Regular calibration ensures reliability.
### **Autofix**
