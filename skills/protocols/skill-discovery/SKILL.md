---
name: "skill-discovery-protocol"
description: "Guides the process of identifying and selecting the appropriate skill for a given task during the planning phase. Helps decide when to use an existing skill, propose a new one, or build a custom solution."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["skill discovery","planning","skill selection","tooling","automation"]
triggers:
  - "when planning a solution"
  - "when requirements exceed capabilities"
  - "when facing a complex task"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "directive"
  original_file: "skill_discovery.md"
---

# Skill Discovery Protocol

## When to Use

During the planning phase of a task.,When the required functionality exceeds your immediate capabilities.,Before resorting to custom scripting or declaring failure.

## What This Does

Guides the process of identifying and selecting the appropriate skill for a given task during the planning phase. Helps decide when to use an existing skill, propose a new one, or build a custom solution.

## Workflow

Initiate the skill discovery process upon encountering a task exceeding built-in capabilities.,Perform an internal scan for existing skills using `python3 skills/find-skills/scripts/discover.py "[capability]"`.,If a local skill with Relevance > 0 is found, use it and review its `SKILL.md` file.,If no local match is found, the script automatically queries `skills.sh` for remote skills.,If a remote skill is found, propose it to the user, including `npx skills add [skill]` in the implementation plan.,Obtain user permission before installing any remote skill.,If no skill is found either locally or remotely, proceed to build a custom script or a new skill.

## Constraints

Always check for existing skills before writing custom code.,Do not automatically install remote skills; always ask for user permission first.,Prioritize using existing local skills when available.
