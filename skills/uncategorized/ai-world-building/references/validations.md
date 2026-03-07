# Ai World Building - Validations

## World building should have documented world bible

### **Id**
world-bible-exists
### **Severity**
critical
### **Description**
Systematic world building requires documentation
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py,yaml}
  #### **Match**
world.*build|brand.*universe|character.*system
  #### **Exclude**
bible|document|rules|system
### **Message**
World building without world bible. Create systematic documentation first.
### **Autofix**


## Recurring characters should have reference sheets

### **Id**
character-has-reference
### **Severity**
high
### **Description**
Characters need visual documentation for consistency
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py,yaml}
  #### **Match**
character.*generat|create.*character|protagonist|main.*character
  #### **Exclude**
reference|sheet|model|documentation
### **Message**
Creating character without reference sheet. Document before generating.
### **Autofix**


## World rules should include exclusions

### **Id**
exclusions-defined
### **Severity**
high
### **Description**
What's NOT in the world is as important as what IS
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
world.*rules|style.*guide|brand.*guidelines
  #### **Exclude**
never|exclude|forbidden|not.*allowed
### **Message**
World rules without exclusions. Define what NEVER appears.
### **Autofix**


## World documentation should be visual-first

### **Id**
visual-documentation
### **Severity**
high
### **Description**
Visual consistency requires visual documentation
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
world.*bible|style.*guide|brand.*universe
  #### **Exclude**
image|visual|reference|example|screenshot
### **Message**
World documentation may lack visuals. Add reference images.
### **Autofix**


## World should be defined tool-agnostically

### **Id**
tool-agnostic-definition
### **Severity**
medium
### **Description**
Tool-specific worlds break when tools change
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
(world|universe|brand).*definition
  #### **Exclude**
universal|agnostic|translation|adapter
### **Message**
World definition may be tool-specific. Create universal rules with tool translations.
### **Autofix**


## Key environments should have documentation

### **Id**
environment-documentation
### **Severity**
medium
### **Description**
Environments need the same rigor as characters
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
environment|location|setting|scene
  #### **Exclude**
sheet|reference|documentation|rules
### **Message**
Environment without documentation. Create environment sheets.
### **Autofix**


## World should have prompt library

### **Id**
prompt-library-exists
### **Severity**
medium
### **Description**
Prompts enable consistent generation at scale
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
world.*bible|brand.*system|generation.*rules
  #### **Exclude**
prompt.*library|template|formula
### **Message**
World system without prompt library. Create reusable prompts.
### **Autofix**


## World elements should be tiered by importance

### **Id**
complexity-tiered
### **Severity**
medium
### **Description**
Flat worlds become too complex to maintain
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
world.*elements|character.*list|asset.*types
  #### **Exclude**
tier|priority|core|extended
### **Message**
World elements not tiered. Define core vs extended vs temporary.
### **Autofix**


## World rules should be tested

### **Id**
consistency-testing
### **Severity**
medium
### **Description**
Rules need validation before production use
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
world.*rule|style.*guide.*apply
  #### **Exclude**
test|verify|validate|check
### **Message**
Applying world rules without testing. Generate test batch first.
### **Autofix**


## World bible should have version control

### **Id**
version-control
### **Severity**
low
### **Description**
Living documents need version tracking
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
world.*bible|brand.*guide
  #### **Exclude**
version|v\d|date|changelog
### **Message**
World bible without versioning. Add version tracking.
### **Autofix**


## Successful generations should be documented

### **Id**
generation-documentation
### **Severity**
low
### **Description**
Learning from successes improves future generation
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
generate.*asset|create.*content
  #### **Exclude**
log|document|record|save.*settings
### **Message**
Generation without documentation. Log successful approaches.
### **Autofix**


## AI generation should track seeds for reproducibility

### **Id**
seed-tracking
### **Severity**
low
### **Description**
Seed tracking enables consistency and iteration
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
midjourney|stable.*diffusion|generate.*image
  #### **Exclude**
seed|reproducible
### **Message**
AI generation without seed tracking. Save seeds for consistent results.
### **Autofix**
