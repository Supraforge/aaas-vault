---
name: composable-ui-development
description: >-
  Build modular, reusable UI components that can be composed into complex
  interfaces across multiple frameworks.
version: 2.5.0
dependencies:
  - node
  - npm
inputs:
  - name: component_type
    description: 'Type of component to create (button, card, form, layout, etc.)'
  - name: framework
    description: 'Target framework (react, vue, svelte, web-components)'
  - name: design_system
    description: 'Design system to follow (material, bootstrap, tailwind, custom)'
outputs:
  - type: file
    description: Generated component files in target framework
  - type: stdout
    description: Component usage instructions and API documentation
compatibility: 'agent-zero, claude-code, cursor'
---

# Composable UI Development

You are a **Modular Interface Architect**. Use this skill to design and implement highly reusable, framework-agnostic (where possible), and composable UI components that empower non-technical builders.

## 🎯 Triggers
- "Create a reusable button component for our design system"
- "Build a composable form component with validation"
- "Implement a card component that works across frameworks"
- "Generate a dashboard layout component library"

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash .agent/skills/composable-ui-development/test.sh` to check dependencies.
- [ ] Confirm Node.js and NPM are installed.

## 📋 Workflow
1. **Context Load**: Scan `context/` for project-specific design tokens or component guidelines.
2. **Analyze Requirements**: Determine component type, framework, and design system constraints.
3. **Phase 2: Leverage Analysis (RESEARCH)**:
   - Search for existing patterns in `templates/`.
   - Before building, check for high-leverage libraries (e.g., Radix UI, Headless UI).
4. **Execute**: Generate modular components using `scripts/compose-ui.js`.
5. **Verify**: Use `scripts/validate-composition.js` to test interoperability.
6. **Self-Annealing**: If composition fails, update the best practices below.

## 🤖 System Instructions (Composability Rules)
- **Single Responsibility**: Each component must solve exactly one structural or functional problem.
- **Atomic Design**: Structure components into Atoms, Molecules, and Organisms.
- **Accessibility First**: Every component MUST include aria labels and keyboard navigation support.
- **Theme Support**: Use CSS variables or design tokens for easy restyling.

## 🛠️ Script Reference
- `scripts/compose-ui.js`: Interactive component generator.
- `scripts/validate-composition.js`: Test runner for component suites.

---

# 📚 Original Reference

---
name: composable-ui-development
description: Build modular, reusable UI components that can be composed into complex interfaces
version: 1.0.0
dependencies: ["node", "npm", "react", "vue", "svelte"]
inputs:
  - name: component_type
    description: Type of component to create (button, card, form, layout, etc.)
  - name: framework
    description: Target framework (react, vue, svelte, web-components)
  - name: design_system
    description: Design system to follow (material, bootstrap, tailwind, custom)
outputs:
  - type: file
    description: Generated component files in target framework
  - type: stdout
    description: Component usage instructions and API documentation
---

# Composable UI Development

## 🎯 Triggers
- "Create a reusable button component for our design system"
- "Build a composable form component with validation"
- "Generate a dashboard layout component library"
- "Implement a card component that works across frameworks"

## ⚡ Quick Start (Self-Check)
Before running logic, verify readiness:
- [ ] Run `bash ~/.gemini/skills/composable-ui-development/test.sh`.
- [ ] Check `.env` contains required keys (if applicable).

## 📋 Workflow
1. **Analyze Requirements**: Determine component type, framework, and design system constraints
2. **Research Patterns**: Search for best practices and existing implementations
3. **Generate Component**: Create modular, reusable component with proper props/API
4. **Test Composition**: Verify component works in different contexts and combinations
5. **Document API**: Generate usage examples and integration guidelines

## 🛠️ Script Reference
- Use `scripts/compose-ui.js` for generating UI components
- Use `scripts/ai-assist.py` for AI-assisted component design
- Use `scripts/validate-composition.js` for testing component interoperability

## 📚 Key Concepts from "The Composability Era"
- **Democratization of Interface Creation**: Anyone can build UI, not just engineers
- **Structural Shift**: Breaking the bottleneck for non-technical builders
- **Front-end Revolution**: New tools and frameworks enabling visual composition
- **Modular Architecture**: Components as building blocks for complex interfaces

## 🔧 Best Practices
1. **Single Responsibility**: Each component should do one thing well
2. **Props Interface**: Clear, typed props with sensible defaults
3. **Composition Over Inheritance**: Prefer composition for flexibility
4. **Accessibility First**: Built-in accessibility features
5. **Theme Support**: Configurable styling via design tokens
6. **Framework Agnostic**: Where possible, create portable components

## 📁 Project Structure
```
components/
├── atoms/           # Basic building blocks (Button, Input, Icon)
├── molecules/       # Simple combinations (FormField, Card, Alert)
├── organisms/       # Complex sections (Header, Sidebar, DataTable)
├── templates/       # Page layouts
└── pages/          # Complete views
```
