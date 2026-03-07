---
name: mass-producing-skills
description: >-
  Agent Zero's autonomous skill factory. Ingests raw documentation, URLs, or
  code repositories and compiles them into fully-functional Antigravity Skills
  (SKILL.md, test.sh, templates) with zero manual intervention.
version: 1.0.0
dependencies:
  - python3
  - bash
  - curl
compatibility: 'agent-zero, claude-code, cursor'
---
# Agent Zero: Skill Factory

## 🎯 Triggers
- "Process this documentation into a skill: [URL]"
- "Convert this folder into a capability."
- "Read [file] and create a skill for it."

## 📋 Automaton Workflow
1.  **Ingest Source**: 
    - **URL**: Fetch content, parse logic/API definitions.
    - **File**: Read content, extract workflows and constraints.
    - **Folder**: Traverse structure, map scripts to `scripts/`, templates to `templates/`.
2.  **Architect Skill**:
    - Determine **Gerund Name** (e.g., `deploying-kubeflow`).
    - Extract **Triggers** (User intents).
    - define **Dependencies** (e.g., `kubectl`, `python`).
3.  **Generate Artifacts** (using `skill-creator` standards):
    - `SKILL.md`: The brain and router.
    - `test.sh`: The autonomic health check.
    - `templates/`: Extracted code patterns.
4.  **Registration**:
    - Write to `.agent/skills/[name]/`.
    - Auto-verify with `test.sh`.

## 🤖 System Instructions (The Factory Logic)

### 1. Source Analysis Strategy
- **If Input is Code**: Look for `main()` functions, CLI arguments, and `requirements.txt`. These become `Executing` steps and `Dependencies`.
- **If Input is Docs**: Look for "How-to" sections. these become `Workflow` steps. Look for "Prerequisites". These become `Dependencies`.

### 2. Standardization Rules (Strict Enforcement)
- **Names**: ASCII, lowercase, kebab-case, must start with a verb ending in -ing.
- **Paths**: NEVER hardcode absolute paths. Use relative paths or context variables.
- **Safety**: `test.sh` MUST exist. If no obvious check exists, use `echo "Ready"`.

### 3. "Zero-Touch" Output Mode
- Do not ask for confirmation on file creation.
- Overwrite existing skills if the name collides (assume the new source is the latest truth).
- Output a single final report: "Skill [name] created and verified."

## 🛠️ Instruction Files (Templates)

### The Master Skill Template
Refer to `templates/MASTER_SKILL.md` for the rigorous structure required for the output `SKILL.md`.

### The Universal Health Check
Refer to `templates/HEALTH_CHECK.sh` for the baseline verification script.
