# Video Scriptwriting - Validations

## Script must have strong hook in first 3 seconds

### **Id**
hook-exists
### **Severity**
critical
### **Description**
First 3 seconds determine if anyone watches
### **Pattern**
  #### **File Glob**
**/*.{yaml,md,txt}
  #### **Match**
script|video.*content
  #### **Exclude**
hook|open|first.*second|attention|grab
### **Message**
Video script may lack hook strategy. Define first 3 seconds explicitly.
### **Autofix**


## Script should not exceed word limits for duration

### **Id**
not-word-heavy
### **Severity**
high
### **Description**
Too many words = too little visual storytelling
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
30.*sec|15.*sec|6.*sec
  #### **Exclude**
word.*count|limit|max
### **Message**
Short-form script may be word-heavy. Check against duration limits.
### **Autofix**


## Visual descriptions must be specific

### **Id**
visual-descriptions-specific
### **Severity**
high
### **Description**
Vague descriptions create production problems
### **Pattern**
  #### **File Glob**
**/*.{yaml,md,txt}
  #### **Match**
(show|visual).*product|lifestyle.*imagery|B-roll
  #### **Exclude**
specific|detail|describe|action
### **Message**
Visual descriptions may be vague. Add specific details for production.
### **Autofix**


## Script should work when muted

### **Id**
works-on-mute
### **Severity**
high
### **Description**
Most social platforms autoplay muted
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
video.*script|social.*video
  #### **Exclude**
mute|silent|caption|text.*overlay|visual.*story
### **Message**
Script may rely too heavily on audio. Design for mute viewing.
### **Autofix**


## Script should include call to action

### **Id**
cta-present
### **Severity**
medium
### **Description**
Videos without CTA waste engagement
### **Pattern**
  #### **File Glob**
**/*.{yaml,md,txt}
  #### **Match**
script|video.*content
  #### **Exclude**
CTA|call.*action|next.*step|learn.*more|sign.*up
### **Message**
Script may lack call to action. Add clear CTA at end.
### **Autofix**


## Content should match available duration

### **Id**
duration-appropriate
### **Severity**
medium
### **Description**
Too much content for time = rushed and confusing
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
(15|30|60).*sec.*script
  #### **Exclude**
duration|timing|fit|single.*message
### **Message**
Script content may exceed duration. Verify timing and cut if needed.
### **Autofix**


## Script should tell story, not list features

### **Id**
not-feature-list
### **Severity**
medium
### **Description**
Feature lists don't engage
### **Pattern**
  #### **File Glob**
**/*.{yaml,md,txt}
  #### **Match**
feature|capability|function
  #### **Exclude**
story|transform|problem|emotion|benefit
### **Message**
Script may be feature-focused. Transform features into stories.
### **Autofix**


## Script should include audio direction

### **Id**
audio-planned
### **Severity**
medium
### **Description**
Audio is half the video experience
### **Pattern**
  #### **File Glob**
**/*.{yaml,md,txt}
  #### **Match**
video.*script
  #### **Exclude**
music|audio|sound|VO|voiceover|SFX
### **Message**
Script may lack audio planning. Add music/sound direction.
### **Autofix**


## Script should consider target platform

### **Id**
platform-considered
### **Severity**
medium
### **Description**
Different platforms need different approaches
### **Pattern**
  #### **File Glob**
**/*.{yaml,md}
  #### **Match**
video.*script
  #### **Exclude**
platform|TikTok|YouTube|Instagram|LinkedIn|format
### **Message**
Script may not consider platform requirements. Specify target platform.
### **Autofix**


## Script should use production-ready format

### **Id**
format-correct
### **Severity**
low
### **Description**
Standard format enables clear production
### **Pattern**
  #### **File Glob**
**/*.{md,txt}
  #### **Match**
VISUAL|VO|SUPER
  #### **Exclude**
format|INT|EXT|scene
### **Message**
Script may not use standard format. Consider production-ready formatting.
### **Autofix**


## Script should include timing cues

### **Id**
timing-noted
### **Severity**
low
### **Description**
Timing helps production and review
### **Pattern**
  #### **File Glob**
**/*.{yaml,md,txt}
  #### **Match**
video.*script
  #### **Exclude**
timing|second|duration|:00|beat
### **Message**
Script may lack timing cues. Add second markers or duration notes.
### **Autofix**
