---
name: routing-llm
description: >-
  Dynamically selects the best available Google LLM (Gemini) based on task
  requirements (speed vs. reasoning).
version: 1.0.0
dependencies:
  - python3
  - requests
inputs:
  - name: strategy
    description: '''speed'' (Flash), ''reasoning'' (Pro), or ''vision'' (Multimodal).'
outputs:
  - type: stdout
    description: 'A model ID string (e.g., ''gemini-1.5-flash'').'
compatibility: 'agent-zero, claude-code, cursor'
---

# LLM Router (Google Optimized)

**PURPOSE:**
This skill queries the Google API to find the optimal model for a task. It ensures we always use the latest "state-of-the-art" model without hardcoding versions.

**STRATEGIES:**
- **speed:** Prioritizes low latency (e.g., Flash 2.0, 1.5). Use for simple tasks, summaries, JSON fixing.
- **reasoning:** Prioritizes intelligence (e.g., Pro, Ultra, Thinking). Use for coding, planning, architecture.
- **vision:** Prioritizes multimodal capabilities.

---

## Usage

### Get the Best Model
```bash
MODEL_ID=$(python3 skills/routing-llm/scripts/router.py --strategy "reasoning")
echo "Selected Model: $MODEL_ID"
```
