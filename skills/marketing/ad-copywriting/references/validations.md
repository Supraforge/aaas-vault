# Ad Copywriting - Validations

## Ad must have clear call to action

### **Id**
cta-present
### **Severity**
critical
### **Description**
Ads without CTA waste attention
### **Pattern**
  #### **File Glob**
**/*.{yaml,md,txt}
  #### **Match**
ad.*copy|headline|primary.*text
  #### **Exclude**
CTA|call.*action|get|start|download|book|sign.*up|learn.*more
### **Message**
Ad copy may lack CTA. Add clear call to action.
### **Autofix**


## Ad should lead with benefits, not features

### **Id**
benefit-over-feature
### **Severity**
high
### **Description**
Benefits connect; features inform
### **Pattern**
  #### **File Glob**
**/*.{yaml,md,txt}
  #### **Match**
our.*product|we.*offer|features|capabilities
  #### **Exclude**
benefit|result|outcome|you.*can|you.*get
### **Message**
Ad copy may be feature-focused. Lead with benefit to customer.
### **Autofix**


## Ad should have one clear message

### **Id**
single-message
### **Severity**
high
### **Description**
Multiple messages = no message
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
ad.*copy.*and.*and|multiple.*benefits|several.*features
  #### **Exclude**
single|one.*message|focus
### **Message**
Ad may have multiple messages. Focus on one key point per ad.
### **Autofix**


## Ad copy should respect platform character limits

### **Id**
character-limits-respected
### **Severity**
high
### **Description**
Truncated copy fails
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
headline|primary.*text|description
  #### **Exclude**
char|limit|length|truncat
### **Message**
Ad copy may exceed platform limits. Verify character counts.
### **Autofix**


## Ad copy should prioritize clarity

### **Id**
clarity-over-clever
### **Severity**
medium
### **Description**
Clear copy converts; clever copy confuses
### **Pattern**
  #### **File Glob**
**/*.{yaml,md,txt}
  #### **Match**
pun|wordplay|clever|creative.*copy
  #### **Exclude**
clear|simple|direct|understand
### **Message**
Ad copy may prioritize cleverness. Ensure clarity first.
### **Autofix**


## Ad claims should have supporting proof

### **Id**
proof-included
### **Severity**
medium
### **Description**
Unsupported claims aren't believed
### **Pattern**
  #### **File Glob**
**/*.{yaml,md,txt}
  #### **Match**
best|#1|leading|guaranteed|proven
  #### **Exclude**
data|number|percent|testimonial|case.*study
### **Message**
Ad makes claims without proof. Add supporting evidence.
### **Autofix**


## Ad should use customer language

### **Id**
audience-language-used
### **Severity**
medium
### **Description**
Their words resonate more than yours
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
ad.*copy|messaging
  #### **Exclude**
voice.*customer|customer.*language|their.*words
### **Message**
Ad copy may use marketer language. Research and use customer language.
### **Autofix**


## Ad should differentiate from competitors

### **Id**
differentiation-present
### **Severity**
medium
### **Description**
Generic copy could be anyone's
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
ad.*copy|value.*prop
  #### **Exclude**
unique|different|unlike|only|specific
### **Message**
Ad copy may be generic. Add differentiation from competitors.
### **Autofix**


## Ad urgency should be legitimate

### **Id**
urgency-legitimate
### **Severity**
medium
### **Description**
Fake urgency damages trust
### **Pattern**
  #### **File Glob**
**/*.{yaml,md,txt}
  #### **Match**
limited.*time|act.*now|hurry|last.*chance
  #### **Exclude**
deadline|date|specific|ends.*on
### **Message**
Ad urgency may not be legitimate. Add specific deadline or remove.
### **Autofix**


## Ad copy should have multiple variations for testing

### **Id**
variations-planned
### **Severity**
low
### **Description**
Testing improves performance
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
ad.*copy|headline
  #### **Exclude**
variation|test|A/B|alternative
### **Message**
Ad copy may lack variations. Create multiple versions for testing.
### **Autofix**


## Ad copy should be platform-optimized

### **Id**
platform-specific
### **Severity**
low
### **Description**
Each platform has different requirements
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
ad.*copy
  #### **Exclude**
platform|meta|google|linkedin|tiktok|specific
### **Message**
Ad copy may not be platform-specific. Adapt for target platform.
### **Autofix**
