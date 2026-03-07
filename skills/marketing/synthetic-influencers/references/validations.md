# Synthetic Influencers - Validations

## Synthetic influencer must have clear disclosure

### **Id**
disclosure-present
### **Severity**
critical
### **Description**
Transparency about AI nature is legally and ethically required
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py,yaml,md}
  #### **Match**
synthetic.*influencer|virtual.*influencer|AI.*persona
  #### **Exclude**
disclosure|transparent|AI.*generated|virtual.*character
### **Message**
Synthetic influencer without disclosure mentioned. Add transparency requirements.
### **Autofix**


## Promotional content needs FTC-compliant disclosure

### **Id**
ad-disclosure-present
### **Severity**
critical
### **Description**
Ads require disclosure even from synthetic influencers
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py,yaml}
  #### **Match**
sponsored|ad|promotion|partner|affiliate
  #### **Exclude**
#ad|#sponsored|paid.*partnership|disclosure
### **Message**
Promotional content without ad disclosure. Add FTC-compliant labels.
### **Autofix**


## Synthetic influencer should have persona bible

### **Id**
persona-bible-exists
### **Severity**
high
### **Description**
Consistent character requires comprehensive documentation
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py,yaml}
  #### **Match**
synthetic.*influencer|virtual.*influencer|AI.*character
  #### **Exclude**
persona.*bible|character.*document|identity.*guide
### **Message**
Synthetic influencer without persona bible. Create comprehensive documentation.
### **Autofix**


## Synthetic influencer should have voice guidelines

### **Id**
voice-guidelines-defined
### **Severity**
high
### **Description**
Consistent voice requires explicit rules
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
persona|character|influencer.*content
  #### **Exclude**
voice|tone|language|speaking.*style
### **Message**
Persona documentation may lack voice guidelines. Define speaking style explicitly.
### **Autofix**


## Visual identity should have consistency system

### **Id**
visual-consistency-planned
### **Severity**
high
### **Description**
Recurring visuals need systematic approach
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
virtual.*influencer|synthetic.*content
  #### **Exclude**
reference|consistency|style.*guide|visual.*identity
### **Message**
Synthetic influencer without visual consistency system. Create reference sheets.
### **Autofix**


## Content should balance promotion with value

### **Id**
content-ratio-planned
### **Severity**
medium
### **Description**
All-promotion content fails; value must dominate
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
content.*strategy|post.*plan
  #### **Exclude**
ratio|balance|entertainment|value|80.*20
### **Message**
Content plan may lack promotion/value balance. Define content ratio.
### **Autofix**


## Synthetic influencer should have engagement plan

### **Id**
engagement-strategy-exists
### **Severity**
medium
### **Description**
Posting without engaging wastes the influencer relationship
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
influencer.*strategy|content.*plan
  #### **Exclude**
engage|respond|comment|community
### **Message**
Influencer plan without engagement strategy. Add community building approach.
### **Autofix**


## Character should have evolution plan

### **Id**
evolution-planned
### **Severity**
medium
### **Description**
Static characters lose audience interest
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
persona|character.*plan
  #### **Exclude**
evolution|growth|development|arc
### **Message**
Character without evolution plan. Define how character grows over time.
### **Autofix**


## Multi-platform presence should have adaptation guidelines

### **Id**
platform-adaptation
### **Severity**
medium
### **Description**
Same character, adapted format for each platform
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
multi.*platform|cross.*platform
  #### **Exclude**
adapt|format|platform.*specific|consistent.*identity
### **Message**
Multi-platform without adaptation guidelines. Define consistent-but-adapted approach.
### **Autofix**


## Synthetic influencer should have controversy response plan

### **Id**
controversy-plan-exists
### **Severity**
medium
### **Description**
Every public figure faces criticism eventually
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
influencer.*strategy|risk|reputation
  #### **Exclude**
controversy|crisis|response|backlash
### **Message**
Influencer strategy without controversy plan. Add crisis response framework.
### **Autofix**


## Platform rules should be documented

### **Id**
platform-compliance-checked
### **Severity**
low
### **Description**
Each platform has rules about synthetic content
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
platform|social.*media
  #### **Exclude**
compliance|rules|policy|terms
### **Message**
Platform strategy may lack compliance consideration. Document platform rules.
### **Autofix**


## Synthetic influencer should have metrics

### **Id**
performance-tracking
### **Severity**
low
### **Description**
Performance data drives improvement
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
post|publish|content
  #### **Exclude**
metric|track|analytics|performance
### **Message**
Posting without performance tracking. Add metrics collection.
### **Autofix**


## Strategy should consider synthetic influencer landscape

### **Id**
competitor-awareness
### **Severity**
low
### **Description**
Understanding competitors helps differentiate
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
influencer.*strategy|positioning
  #### **Exclude**
competitor|landscape|differentiate|unique
### **Message**
Strategy may lack competitive awareness. Research synthetic influencer landscape.
### **Autofix**
