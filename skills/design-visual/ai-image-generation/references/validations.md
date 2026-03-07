# Ai Image Generation - Validations

## No API keys in code

### **Id**
no-api-keys-hardcoded
### **Severity**
critical
### **Description**
API keys must use environment variables, never hardcoded
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py,yaml,json}
  #### **Match**
(OPENAI_API|MIDJOURNEY|REPLICATE|FAL_KEY|STABILITY|IDEOGRAM).*=.*['"][^'"]{20,}['"]
  #### **Exclude**
process\.env|import\.meta\.env|os\.environ|\$\{
### **Message**
API key hardcoded. Use environment variables.
### **Autofix**


## Avoid copyrighted artist style references

### **Id**
no-copyrighted-artist-names
### **Severity**
high
### **Description**
Referencing living artists by name creates legal risk
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py,yaml,json,md}
  #### **Match**
style of (Greg Rutkowski|Artgerm|Wlop|Sakimichan|Ross Tran)
  #### **Exclude**
avoid|don't|not|example of what NOT
### **Message**
Living artist name in prompt creates legal risk. Describe style instead.
### **Autofix**


## Sanitize user input in prompts

### **Id**
user-input-sanitization
### **Severity**
critical
### **Description**
User input concatenated into prompts needs sanitization
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
prompt.*\+.*\b(user|input|req\.body|params)
  #### **Exclude**
sanitize|escape|clean|filter|validate
### **Message**
User input in prompt without sanitization. Add input validation.
### **Autofix**


## Prompts need structural elements

### **Id**
prompt-has-structure
### **Severity**
high
### **Description**
Quality prompts should specify medium, subject, and style
### **Pattern**
  #### **File Glob**
**/*.{ts,js,yaml}
  #### **Match**
prompt\\s*[:=]\\s*["\''][^"\'']{1,80}["\'']
  #### **Exclude**
photograph|render|painting|illustration|drawing|3d|digital art
### **Message**
Prompt lacks medium type. Add 'photograph of', 'illustration of', etc.
### **Autofix**


## Use negative prompts for human subjects

### **Id**
negative-prompt-for-people
### **Severity**
medium
### **Description**
Human subjects should have anatomy-related negative prompts
### **Pattern**
  #### **File Glob**
**/*.{ts,js,yaml}
  #### **Match**
(person|woman|man|human|portrait|face)
  #### **Exclude**
negative|bad anatomy|extra fingers|deformed
### **Message**
Human subject without anatomy negative prompts. Add 'no extra fingers, proper anatomy'.
### **Autofix**


## Specify output resolution

### **Id**
resolution-specified
### **Severity**
medium
### **Description**
Generation calls should specify resolution for predictable output
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
(generate|create).*image
  #### **Exclude**
size|resolution|width|height|1024|1792|aspect
### **Message**
Generation without resolution specified. Set width/height or aspect ratio.
### **Autofix**


## Use seeds for reproducibility

### **Id**
seed-for-reproducibility
### **Severity**
medium
### **Description**
Important generations should use explicit seeds for reproducibility
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
generate.*\{[^}]*prompt
  #### **Exclude**
seed|reproducible|random.*false
### **Message**
Consider using explicit seed for reproducibility.
### **Autofix**


## Track generation costs

### **Id**
cost-tracking-present
### **Severity**
medium
### **Description**
API calls should log cost estimates for budget management
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
(openai|replicate|fal)\.(generate|images|run)
  #### **Exclude**
cost|price|budget|track|log|estimate
### **Message**
Image generation without cost tracking. Add cost logging.
### **Autofix**


## Generation calls need error handling

### **Id**
error-handling-for-generation
### **Severity**
high
### **Description**
AI generation API calls should handle failures gracefully
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
await.*(generate|openai\.images|replicate\.run|fal\.)
  #### **Exclude**
try|catch|error|Error|except|finally|\.catch
### **Message**
Generation call without error handling. Wrap in try/catch.
### **Autofix**


## Batch generation needs rate limiting

### **Id**
batch-has-rate-limiting
### **Severity**
high
### **Description**
Multiple simultaneous generations should respect rate limits
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
Promise\.all.*generate|for.*await.*generate|\.map.*generate
  #### **Exclude**
queue|limit|throttle|batch|PQueue|p-limit|concurrent
### **Message**
Batch generation without rate limiting. Add concurrency control.
### **Autofix**


## Save generation metadata

### **Id**
output-metadata-saved
### **Severity**
low
### **Description**
Generation outputs should be saved with prompt and settings
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
(save|write|store).*\.png|\.jpg|image
  #### **Exclude**
metadata|prompt|seed|settings|json|log
### **Message**
Saving image without metadata. Store prompt and settings for reference.
### **Autofix**


## Match aspect ratio to platform

### **Id**
aspect-ratio-platform-match
### **Severity**
medium
### **Description**
Social media content should use platform-appropriate aspect ratios
### **Pattern**
  #### **File Glob**
**/*.{ts,js,yaml}
  #### **Match**
(instagram|tiktok|twitter|linkedin|facebook)
  #### **Exclude**
1:1|4:5|9:16|16:9|aspect|ratio
### **Message**
Platform mentioned without aspect ratio specification.
### **Autofix**


## Use style references for image series

### **Id**
style-reference-for-series
### **Severity**
low
### **Description**
Multiple related images should use style reference for consistency
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
for.*\{.*generate|series|batch|multiple.*image
  #### **Exclude**
style_reference|reference_image|consistent|ip_adapter|seed
### **Message**
Generating series without style reference. Use IP-Adapter or consistent seeds.
### **Autofix**
