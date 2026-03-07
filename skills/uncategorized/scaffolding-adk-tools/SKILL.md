---
name: scaffolding-adk-tools
description: Scaffolds a new custom Tool class for the Agent Development Kit (ADK).
version: 1.0.0
dependencies:
  - python3
compatibility: 'agent-zero, claude-code, cursor'
---

# ADK Tool Scaffold Skill

This skill automates the creation of standard `BaseTool` implementations for the Agent Development Kit.

## 🎯 Triggers
- "Create a new ADK tool for..."
- "Scaffold a tool to..."
- "Generate a BaseTool class for..."

## ⚡ Quick Start (Self-Check)
Before running complex logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/scaffolding-adk-tools/test.sh` to check dependencies.

## 📋 Workflow
1. **Ingest**: Analyze the user's request to identify the tool name and purpose.
2. **Execute**: Run the scaffold script to generate the initial tool class.
3. **Verify**: Review the generated file and guide the user to implement the logic.

## 🤖 System Instructions
When using this skill:

1. **Identify the Tool Name**:
   Extract the name of the tool the user wants to build (e.g., "StockPrice", "EmailSender").
   
2. **Review the Example**:
   Check `examples/WeatherTool.py` to understand the expected structure of an ADK tool (imports, inheritance, schema).

3. **Run the Scaffolder**:
   Execute the python script to generate the initial file.
   
   ```bash
   python scripts/scaffold_tool.py <ToolName>
   ```

4. **Refine**:
   After generation, you must edit the file to:
   - Update the `execute` method with real logic.
   - Define the JSON schema in `get_schema`.
   
## Example Usage
User: "Create a tool to search Wikipedia."
Agent:
1. Runs `python scripts/scaffold_tool.py WikipediaSearch`
2. Editing `WikipediaSearchTool.py` to add the `requests` logic and `query` argument schema.

## 🛠️ Script Reference
- Use `scripts/scaffold_tool.py` to generate new tool classes.
- Refer to `templates/ToolTemplate.py.hbs` for the template structure.
- Check `examples/WeatherTool.py` for a complete example.
