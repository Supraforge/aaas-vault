# Ai Audio Production - Validations

## No API keys in code

### **Id**
no-api-keys-hardcoded
### **Severity**
critical
### **Description**
Audio API keys must use environment variables
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py,yaml,json}
  #### **Match**
(ELEVENLABS_API|SUNO_API|UDIO_|MURF_|PLAY_HT).*=.*['"][^'"]{20,}['"]
  #### **Exclude**
process\.env|import\.meta\.env|os\.environ|\$\{
### **Message**
API key hardcoded. Use environment variables.
### **Autofix**


## Voice cloning requires consent documentation

### **Id**
voice-consent-check
### **Severity**
critical
### **Description**
Any voice cloning should reference consent documentation
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
(clone|voice_id|add_voice|instant_voice)
  #### **Exclude**
consent|agreement|permission|authorized|licensed
### **Message**
Voice cloning without consent reference. Add consent documentation.
### **Autofix**


## No celebrity voice cloning

### **Id**
no-celebrity-voice-cloning
### **Severity**
critical
### **Description**
Cloning celebrity or public figure voices is prohibited
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py,yaml,json}
  #### **Match**
clone.*(celebrity|famous|[A-Z][a-z]+ [A-Z][a-z]+.*(voice|clone))
  #### **Exclude**
example of what NOT|avoid|don't
### **Message**
Celebrity voice cloning attempt. This is illegal without explicit license.
### **Autofix**


## Audio output needs normalization

### **Id**
audio-output-normalization
### **Severity**
high
### **Description**
AI audio should be normalized before delivery
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
(elevenlabs|suno|udio).*generate|synthesize|text_to_speech
  #### **Exclude**
normalize|lufs|loudness|master|process
### **Message**
Audio generation without normalization step. Add LUFS normalization (-14 LUFS).
### **Autofix**


## Audio API calls need error handling

### **Id**
error-handling-audio-api
### **Severity**
high
### **Description**
AI audio API calls should handle failures gracefully
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
await.*(elevenlabs|suno|generate.*audio|text_to_speech)
  #### **Exclude**
try|catch|error|Error|except|finally|\.catch
### **Message**
Audio API call without error handling. Wrap in try/catch.
### **Autofix**


## Voice settings should be explicit

### **Id**
voice-settings-explicit
### **Severity**
medium
### **Description**
ElevenLabs and similar should have explicit stability/similarity settings
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
elevenlabs.*generate|text_to_speech
  #### **Exclude**
stability|similarity|style|settings|voice_settings
### **Message**
Voice generation without explicit settings. Set stability and similarity for consistency.
### **Autofix**


## Track audio generation costs

### **Id**
cost-tracking-audio
### **Severity**
medium
### **Description**
Audio API calls should log character counts or generation costs
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
(elevenlabs|suno|udio|murf)\.(generate|synthesize|create)
  #### **Exclude**
cost|chars|character|count|track|log|budget
### **Message**
Audio generation without cost tracking. Log character counts for budget management.
### **Autofix**


## Music prompts need sufficient detail

### **Id**
music-prompt-detail
### **Severity**
medium
### **Description**
AI music prompts should specify genre, tempo, mood, instruments
### **Pattern**
  #### **File Glob**
**/*.{ts,js,yaml}
  #### **Match**
music.*prompt.*[:=].*["\''][^"\'']{1,50}["\'']
  #### **Exclude**
BPM|tempo|genre|instrument|mood|style
### **Message**
Music prompt too vague. Include genre, tempo, mood, and instruments.
### **Autofix**


## Specify audio output format

### **Id**
audio-format-specification
### **Severity**
medium
### **Description**
Audio generation should specify format (mp3, wav, etc.)
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
generate.*audio|text_to_speech|synthesize
  #### **Exclude**
format|mp3|wav|ogg|m4a|output_format
### **Message**
Audio generation without format specification. Specify output format.
### **Autofix**


## Batch audio needs rate limiting

### **Id**
rate-limiting-audio
### **Severity**
high
### **Description**
Multiple audio generations should respect rate limits
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
Promise\.all.*(audio|voice|speech)|for.*await.*(generate|synthesize)
  #### **Exclude**
queue|limit|throttle|batch|PQueue|p-limit|concurrent|delay
### **Message**
Batch audio generation without rate limiting. Add concurrency control.
### **Autofix**


## Save audio generation metadata

### **Id**
audio-metadata-saved
### **Severity**
low
### **Description**
Audio outputs should be saved with generation settings
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
(save|write|store).*\.mp3|\.wav|audio
  #### **Exclude**
metadata|settings|prompt|voice_id|json
### **Message**
Saving audio without metadata. Store settings for reproducibility.
### **Autofix**


## Maintain consistent sample rates

### **Id**
sample-rate-consistency
### **Severity**
low
### **Description**
Audio files should use consistent sample rates for mixing
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
sample_rate|sampleRate
  #### **Exclude**
48000|44100|consistent|match
### **Message**
Non-standard sample rate. Use 44100 or 48000 Hz for consistency.
### **Autofix**


## Consider stereo vs mono for use case

### **Id**
stereo-mono-consideration
### **Severity**
low
### **Description**
Voice content often works better in mono, music in stereo
### **Pattern**
  #### **File Glob**
**/*.{ts,js,py}
  #### **Match**
text_to_speech|voice.*generate
  #### **Exclude**
mono|stereo|channels
### **Message**
Voice generation without channel specification. Consider mono for voice.
### **Autofix**
