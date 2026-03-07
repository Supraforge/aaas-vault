# Antigravity Skills Tutorial

This repository contains a collection of example **Skills** for [Google Antigravity](https://antigravity.google). These examples demonstrate the "Agentic Command Line" concept, showing how to package expertise, workflows, and tools into modular units that an AI agent can use.

## Overview

Antigravity Skills allow you to define *how* an agent should behave, what tools it should use, and what context it should reference. This project breaks down skill development into 5 levels of complexity.

## The Skills

The `skills_tutorial/` directory contains the following examples:

### Level 1: Basic Routing
**`git-commit-formatter`**
*   **Concept**: Pure Prompt Engineering.
*   **Function**: Intercepts "commit" requests and formats the message according to the Conventional Commits specification.
*   **Key File**: `SKILL.md`

### Level 2: Asset Utilization
**`license-header-adder`**
*   **Concept**: Loading static resources.
*   **Function**: Adds a standard Apache 2.0 license header to source files by reading a template from the `resources/` folder.
*   **Key Files**: `SKILL.md`, `resources/HEADER_TEMPLATE.txt`

### Level 3: Few-Shot Learning
**`json-to-pydantic`**
*   **Concept**: Learning by Example.
*   **Function**: Converts JSON data into Pydantic models by referencing a "Golden Example" pair (Input JSON -> Output Python) instead of using complex instructions.
*   **Key Files**: `SKILL.md`, `examples/`

### Level 4: Tool Use & Validation
**`database-schema-validator`**
*   **Concept**: Delegating to deterministic scripts.
*   **Function**: Validates SQL schema files for safety and naming conventions by running a Python script, ensuring 100% accuracy.
*   **Key Files**: `SKILL.md`, `scripts/validate_schema.py`

### Level 5: Composition (The "Batteries-Included" Skill)
**`adk-tool-scaffold`**
*   **Concept**: Combining scripts, templates, and examples.
*   **Function**: Orchestrates a full workflow to scaffold a new Antigravity ADK Tool. It generates the file using a script, populates it from a Jinja2 template, and guides the implementation using a reference example.
*   **Key Files**: `SKILL.md`, `scripts/scaffold_tool.py`, `resources/ToolTemplate.py.hbs`, `examples/WeatherTool.py`

## Usage

To use these skills in your Antigravity environment:

1.  Clone this repository.
2.  Copy the desired folders from `skills_tutorial/` into your workspace's `.agent/skills/` directory (or your global `~/.gemini/antigravity/skills/` directory).
3.  Restart your agent session.

## License

Apache 2.0
