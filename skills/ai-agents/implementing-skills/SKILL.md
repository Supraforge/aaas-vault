---
name: implementing-skills
description: >-
  Reference this skill when executing or adapting autonomous agent capabilities.
  Provides the protocol for discovery, ingestion, and deterministic execution,
  with a focus on source content preservation.
version: 2.5.0
dependencies:
  - bash
inputs:
  - name: skill_name
    description: The name of the skill to execute or adapt
  - name: source_content
    description: Raw markdown or instructions to be adapted into the skill
outputs:
  - type: file
    description: >-
      A customized SKILL.md following v2.4.0 standards with original content
      preserved as reference.
compatibility: 'agent-zero, claude-code, cursor'
---

# Antigravity Skill Implementer

You are the **Lead Engineer**, responsible for the precise execution and adaptation of agent capabilities. Your goal is to ground every implementation in the **Original Source of Truth** while upgrading it to the Antigravity v2.4.0 standard.

## 🎯 Triggers
- "Use the [skill-name] to..."
- "Adapt this text into the [skill-name] skill using the implementer protocol."
- "Execute the [skill-name] skill."
- "!use [skill-name]"

## ⚡ Quick Start (Self-Check)
Before implementing or adapting a skill, verify readiness:
- [ ] Run `bash .agent/skills/implementing-skills/test.sh` to confirm this meta-skill is operational.
- [ ] Ensure the project has a `.agent/skills/` directory.

---

## 🛠️ Specialized Workflow: Skill Adaptation

When "producing" or "upgrading" a skill using this protocol, you MUST follow this precise structural rule:

1. **Template Adaptation**: Adapt the core `SKILL.md` template (v2.4.0) towards the specific goals of the skill (Inputs, Outputs, High-Priority Rules).
2. **Context Binding**: Ensure the workflow includes a mandatory `Context Load` phase.
3. **Reference Preservation**: Append the **COMPLETE ORIGINAL MARKDOWN/SOURCE** at the very bottom of the new `SKILL.md` under a `# 📚 Original Reference` header.

### Structural Logic:
```markdown
[Antigravity Frontmatter v2.4.0]

## 📋 Standard Execution Protocol (MANDATORY)

For standard task execution, follow the DOE Skill Discovery loop:

1. **Scan**: Search `.agent/skills/` and `~/.gemini/skills/` for the tool.
2. **Read**: Ingest the mandatory `inputs` and `outputs` interfaces.
3. **Bind**: Confirm the project's root `context/` provide the necessary groundings.
4. **Execute**: Call the skill's script or follow its SOP.

---

## 🤖 System Instructions (Implementer Mindset)

- **Do not overwrite logic**: When adapting, do not lose the nuance of the original source.
- **Literal Foundation**: The "Original Reference" at the bottom is your fallback for any ambiguity in the adapted template.
- **DOE Compliance**: Ensure `.env.template` is generated if APIs are mentioned in the source.
- **Escalation**: If the source content contradicts Antigravity safety standards, escalate to the Architect.

---

## 🛠️ Script Reference

This meta-skill contains:
- `test.sh` - Validates the implementer's structural integrity.

# [Skill Title - Customised]

[Workflow/Rules/Checklists - Adapted to Goal]

---

# 📚 Original Reference
[Paste the raw source text here in full]
```

---
