# Ai Video Generation - Validations

## No API keys in prompt files

### **Id**
no-api-keys-in-prompts
### **Severity**
critical
### **Description**
API keys must never be hardcoded in prompt templates or generation scripts
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py,yaml,json}
  #### **Match**
(RUNWAY_API|VEO3_API|SORA_API|KLING_API|PIKA_API|FAL_API).*=.*['"][^'"]{20,}['"]
  #### **Exclude**
process\.env|import\.meta\.env|os\.environ
### **Message**
API key hardcoded in file. Use environment variables instead.
### **Autofix**


## API calls need rate limit handling

### **Id**
rate-limit-handling
### **Severity**
high
### **Description**
AI video API calls should have retry logic for rate limits
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
(runway|fal|replicate)\.generate|fetch.*api\.(runway|fal|replicate)
  #### **Exclude**
retry|backoff|RateLimit|sleep|delay
### **Message**
API call without rate limit handling. Add exponential backoff retry logic.
### **Autofix**


## Track generation costs

### **Id**
generation-cost-tracking
### **Severity**
medium
### **Description**
Video generations should log estimated costs for budget tracking
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
generate.*video|createVideo|runway\.run|fal\.subscribe
  #### **Exclude**
cost|budget|track|log.*price|estimate
### **Message**
Video generation without cost tracking. Add cost logging for budget management.
### **Autofix**


## Prompts need sufficient detail

### **Id**
prompt-minimum-detail
### **Severity**
high
### **Description**
AI video prompts under 50 characters are too vague for quality output
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py,yaml,json}
  #### **Match**
prompt["\'']?\\s*[:=]\\s*["\''][^"\'']{1,50}["\'']
  #### **Exclude**
example|test|mock|placeholder
### **Message**
Prompt too short. Include camera, action, lighting, subject, and duration details.
### **Autofix**


## Prompts should specify duration

### **Id**
prompt-has-duration
### **Severity**
medium
### **Description**
AI video prompts should include target duration for better results
### **Pattern**
  #### **File Glob**
**/*.{ts,js,yaml}
  #### **Match**
prompt.*[:=].*"[^"]*"
  #### **Exclude**
second|duration|\ds\b|\d\s*sec
### **Message**
Prompt missing duration. Add '4 seconds' or similar for consistent output.
### **Autofix**


## Prompts should specify camera

### **Id**
prompt-has-camera
### **Severity**
medium
### **Description**
Specifying camera movement/angle improves AI video consistency
### **Pattern**
  #### **File Glob**
**/*.{ts,js,yaml}
  #### **Match**
prompt.*video.*[:=]
  #### **Exclude**
camera|shot|pan|zoom|dolly|tracking|wide|close|medium|POV|angle
### **Message**
Prompt missing camera specification. Add camera type/movement for better control.
### **Autofix**


## Aspect ratio should be explicit

### **Id**
aspect-ratio-specified
### **Severity**
medium
### **Description**
Generation calls should specify aspect ratio for target platform
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
generate.*video|createVideo
  #### **Exclude**
aspect|ratio|16:9|9:16|1:1|4:5|width|height
### **Message**
Generation without explicit aspect ratio. Specify for target platform.
### **Autofix**


## Save generation metadata with output

### **Id**
output-saved-with-metadata
### **Severity**
medium
### **Description**
Video outputs should be saved with prompt, seed, and settings for reproducibility
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
download.*video|save.*output|writeFile.*\.mp4
  #### **Exclude**
metadata|prompt|seed|settings|log|json
### **Message**
Saving video without metadata. Store prompt, seed, and settings for reproducibility.
### **Autofix**


## Long-running generations need status handling

### **Id**
webhook-or-polling
### **Severity**
high
### **Description**
AI video generation is async; implement webhook or polling for status
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
(runway|fal|replicate)\.(generate|run|subscribe)
  #### **Exclude**
webhook|poll|status|await.*complete|onComplete|callback
### **Message**
Async generation without completion handling. Add webhook or polling.
### **Autofix**


## Consider negative prompts

### **Id**
negative-prompt-used
### **Severity**
low
### **Description**
Negative prompts help exclude unwanted elements from generations
### **Pattern**
  #### **File Glob**
**/*.{ts,js,yaml}
  #### **Match**
prompt.*[:=].*"[^"]{100,}"
  #### **Exclude**
negative|avoid|without|no text|no watermark|not
### **Message**
Long prompt without negative specifications. Consider adding what to avoid.
### **Autofix**


## Batch generation needs queue management

### **Id**
batch-uses-queue
### **Severity**
medium
### **Description**
Multiple generations should use a queue to respect rate limits
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
Promise\.all.*generate|for.*await.*generate|\.map.*generate
  #### **Exclude**
queue|PQueue|limit|concurrent|batch|throttle
### **Message**
Batch generation without queue. Use PQueue or similar for rate limiting.
### **Autofix**


## Generation calls need error handling

### **Id**
error-handling-present
### **Severity**
high
### **Description**
AI generation calls should handle failures gracefully
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
await.*(generate|runway|fal|replicate)
  #### **Exclude**
try|catch|error|Error|except|finally
### **Message**
Generation call without error handling. Wrap in try/catch.
### **Autofix**


## Save seeds for reproducibility

### **Id**
seed-saved-for-consistency
### **Severity**
low
### **Description**
When seed is used, it should be logged for future reference
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
seed.*[:=].*\d+
  #### **Exclude**
log|save|store|console|metadata
### **Message**
Seed used but not logged. Save for reproducibility.
### **Autofix**
