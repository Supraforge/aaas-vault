---
name: "skill-activation-protocol"
description: "This outlines the process for safely integrating new skills into the system, including dependency checks, testing, and storage conventions."
version: "1.0.0"
author: "Antigravity Vault"
license: "proprietary"
tags: ["skills","testing","dependency-management","onboarding","security"]
triggers:
  - "when importing a new skill"
  - "when adding a skill to the library"
  - "when a skill requires verification"
compatibility: "agent-zero, claude-code, cursor"
metadata:
  source: "antigravity-doe"
  asset_type: "directive"
  original_file: "activations_protocol.md"
---

# Skill Activation Protocol

## When to Use

When importing a skill from an external source.,When adding a new skill to the permanent skills library.,When verifying the functionality of a skill.,When a skill has dependencies that need to be managed.,When ensuring skills adhere to system standards and avoid code fragmentation.

## What This Does

This outlines the process for safely integrating new skills into the system, including dependency checks, testing, and storage conventions.

## Workflow

1. **Isolation Check:** Determine if the skill relies on global npm packages or hidden dependencies.,2. **Dependency Scan:** Examine the skill's `package.json`, `requirements.txt`, or `install.sh` files.,3. **Dependency Action:** If external dependencies are required, prefer a local `node_modules` directory within the skill or utilize a container.,4. **Sanity Test:** Execute the `test.sh` script located within the skill's directory. Ensure it exits with code 0 and prints '✅'.,5. **Interface Audit:** Review the skill's `SKILL.md` file and ensure it adheres to the system standard; rewrite if necessary.,6. **Duplicate Detection:** Before adding, check if a similar skill already exists.,7. **Storage:** Approved skills should be stored in `skills/`, quarantined skills in `.tmp/skills/`, and skills should never be located in `.agent/` or `.agents/`.,8. **Pruning:** Remove skills that fail the Sanity Test and cannot be easily fixed.

## Constraints

All imported skills must be verified before being added to the `skills/` library.,Skills should avoid relying on global npm packages whenever possible.,A `test.sh` script must exist and pass for all skills before they are considered valid.,`SKILL.md` files must adhere to the system standard defined by the `skill-creator` template.,Approved skills should reside in the `skills/` directory to ensure a single source of truth.
