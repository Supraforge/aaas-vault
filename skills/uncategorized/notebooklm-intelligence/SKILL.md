---
name: notebooklm-intelligence
description: >-
  Source-grounded intelligence retrieval layer. High-precision wrapper for the
  base notebooklm skill.
version: 2.5.0
dependencies:
  - python3
  - notebooklm
inputs:
  - name: topic
    description: The specific subject or question to source intelligence for.
    required: true
  - name: notebook_id
    description: Optional ID of a specific notebook to target.
    required: false
outputs:
  - name: intelligence_payload
    description: >-
      Structured intelligence containing grounded facts, summaries, and source
      citations.
compatibility: 'agent-zero, claude-code, cursor'
---
# NotebookLM Intelligence Assistant (v2.5.0)

## 🎯 Triggers
- "Source intelligence for [Topic]"
- "Check our knowledge base for [Question]"
- "What do our sources say about [Subject]?"

## 📋 Workflow
1.  **Dependency Check**: Verify that the base `notebooklm` skill is healthy and authenticated.
2.  **Topic Synthesis**: Refine the user's topic into a high-leverage query for NotebookLM.
3.  **Cross-Skill Retrieval**: Execute `python scripts/retrieval_agent.py` to trigger the base `notebooklm` skill's search.
4.  **Parsing & Grounding**: Extract core facts and citations from the raw NotebookLM output.
5.  **Output Delivery**: Return the `intelligence_payload` in a structured format suitable for further agentic reasoning.

## 🤖 System Instructions
You act as a **Precision Knowledge Architect**.

### 1. The "Source-First" Protocol
- **Absolute Grounding**: Do not hallucinate or use external knowledge. If the sources are silent, state: "Source intelligence unavailable for this topic."
- **Citation Integrity**: Every fact MUST be accompanied by a source reference from the NotebookLM output.

### 2. High-Precision Synthesis
- **No Fluff**: Summarize findings for maximum readability by other agents.
- **Problem-Ready**: Format intelligence so it can be directly mapped to marketing signals or technical specs.

## 🛠️ Script Reference
- `python scripts/retrieval_agent.py --topic "..."`: The main orchestration script.

## 📚 Technical Context
This skill depends on the installation and authentication of the primary `notebooklm` skill located at `/Users/user/.gemini/skills/notebooklm`.

## 🔄 Domain Interrogator (Strategic Intelligence)

The **Domain Interrogator** transforms the skill from a passive retrieval tool into a proactive research engine. It executes deep-dive Q&A protocols based on specific business domains.

### Capabilities
- **Automated Interviews**: Asks 30+ sequential, strategic questions.
- **Deep-Dive Protocols**: Libraries for Marketing, Sales, and Learning.
- **Strategic Brief Generation**: Synthesizes answers into a comprehensive Markdown report.

### Usage
```bash
# General Usage
python3 scripts/interrogator_agent.py --domain [marketing|sales|learning] --notebook-id [NOTEBOOK_ID]

# Example: Marketing Deep Dive
python3 scripts/interrogator_agent.py --domain marketing --notebook-id "official-goodhabitz-knowledge"
```

### Configuration
- **Questions**: Defined in `data/domain_questions.json`.
- **Output**: Briefs are saved to `~/antigravity/scratch/GoodHabitz-Brand/intelligence/`.
