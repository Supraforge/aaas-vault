---
name: research-protocol
description: "11-Phase Universal Agentic Production Protocol — research, strategize, and define before building"
version: "1.0.0"
dependencies: []
triggers:
  - "new project"
  - "research"
  - "strategy"
  - "requirements"
  - "proposal"
  - "phase"
---

# Research Protocol — Universal Agentic Production Protocol

> **MANDATORY:** Before building ANYTHING, run at minimum Phases 1-3.
> This protocol ensures every project starts with intelligence, not assumptions.

## The 11-Phase Flow

### PRE-ACTIVATION Block (Think Before Building)

| Phase | Name | Output | Duration |
|-------|------|--------|----------|
| 1 | **Goal Definition** | Structured goal brief with success criteria | 30 min |
| 2 | **Proposal Research** | Fast-mode research summary (proposal-grade) | 2-4 hours |
| 3 | **Strategy Routes** | 2-3 viable execution approaches with trade-offs | 1-2 hours |
| 4 | **Requirements Engineering** | Execution blueprint + client deliverable spec | 2-4 hours |
| 5 | **Proposal Generation** | Client-facing proposal document | 1-2 hours |
| 6 | **Client Activation** | HUMAN GATE — mandatory approval before production | Manual |

### POST-ACTIVATION Block (Build With Intelligence)

| Phase | Name | Output | Duration |
|-------|------|--------|----------|
| 7 | **Competitive Research** | Deep competitive analysis | 1-2 days |
| 8 | **Industry Knowledge** | Deep industry intelligence | 1-2 days |
| 9 | **Context Synthesis** | `CLIENT_CONTEXT_FRAMEWORK.md` | 4-8 hours |
| 10 | **Sub-Project Goals** | Ordered execution sequence with dependencies | 2-4 hours |
| 11 | **Tool Selection** | Unified scoring: prompts + skills + models + MCP servers | 2-4 hours |

## Two-Pass Research Model

| Pass | Phases | Depth | Purpose | When |
|------|--------|-------|---------|------|
| **Proposal-grade** | 1-5 | Shallow/fast | Enough for a credible proposal | Before client approval |
| **Production-grade** | 7-8 | Deep/thorough | Full competitive + industry intel | After client approval |

## Usage

### Quick Start (Minimum Viable Research)
```bash
# Phase 1: Define the goal
python3 skills/research-protocol/scripts/run_phase.py 1 --project="My Project"

# Phase 2: Fast research
python3 skills/research-protocol/scripts/run_phase.py 2 --project="My Project"

# Phase 3: Strategy routes
python3 skills/research-protocol/scripts/run_phase.py 3 --project="My Project"
```

### Full Protocol
```bash
# Run all pre-activation phases
python3 skills/research-protocol/scripts/run_phase.py all-pre --project="My Project"

# After human approval, run post-activation
python3 skills/research-protocol/scripts/run_phase.py all-post --project="My Project"
```

## Phase Details

### Phase 1: Goal Definition

**Input:** Project name, initial description
**Output:** `context/goals.md` populated with:

```markdown
# [Project] — Goal Brief

## Primary Objective
- What: [clear statement]
- Why: [business justification]
- For Whom: [target audience]

## Success Criteria
- [ ] Criterion 1 (measurable)
- [ ] Criterion 2 (measurable)
- [ ] Criterion 3 (measurable)

## Constraints
- Budget: [amount or range]
- Timeline: [deadline]
- Technical: [stack requirements, integrations]

## Scope Boundaries
- IN scope: [explicit list]
- OUT of scope: [explicit list]
```

### Phase 2: Proposal Research (Fast Mode)

**Input:** Goal brief from Phase 1
**Output:** `.tmp/research_phase2.md`

Research targets:
1. **Market scan** — What exists? Who are the competitors?
2. **Technology scan** — What tools/frameworks fit the requirements?
3. **Reference implementations** — GitHub repos, open-source projects, templates
4. **Pricing/positioning** — How do competitors price similar offerings?

Tools used: Tavily API, GitHub search, web scraping, vault skill lookup

### Phase 3: Strategy Routes

**Input:** Goal brief + research summary
**Output:** `.tmp/strategy_routes.md`

For each route (minimum 2, maximum 3):
```markdown
## Route [N]: [Name]

### Approach
[2-3 sentence description]

### Pros
- [advantage 1]
- [advantage 2]

### Cons
- [disadvantage 1]
- [disadvantage 2]

### Estimated Effort
- Time: [duration]
- Cost: [estimate]
- Complexity: [Low/Medium/High]

### Tech Stack
- [technology choices]

### Risk Level
[Low/Medium/High] — [brief justification]
```

### Phase 4: Requirements Engineering

**Input:** Chosen strategy route
**Output:** `.tmp/PROJECT_REQUIREMENTS.md`

Two parts:
- **Part A: Execution Requirements** — Resource plan, skill mapping, dependency chains, timeline, risk register
- **Part B: Client Deliverable Spec** — Deliverables list, format specs, quality criteria, acceptance process

### Phase 5: Proposal Generation

**Input:** Requirements document + brand context
**Output:** `.tmp/proposal_draft.md`

### Phase 6: Client Activation (HUMAN GATE)

**Action:** Present proposal to human for approval.
**Rule:** NO production work begins until this gate is passed.

### Phases 7-8: Deep Research (Parallel)

Run competitive and industry research in parallel using subagents.
**Output:** `.tmp/competitive_research.md` + `.tmp/industry_knowledge.md`

### Phase 9: Context Synthesis

**Input:** All research artifacts
**Output:** `context/CLIENT_CONTEXT_FRAMEWORK.md`

Merges all intelligence into a unified context document with 6 sections:
1. Core Identity
2. Brand Voice & Persona
3. Target Audience
4. Product/Service Offering
5. Market Landscape
6. Visual Guidelines (MANUAL — never auto-generated)

### Phase 10: Sub-Project Goals

**Input:** Requirements + context framework
**Output:** `.tmp/sub_project_goals.md`

Ordered execution sequence with dependency chains.

### Phase 11: Tool Selection

**Input:** Sub-project goals + available skills
**Output:** `.tmp/tool_selection.md`

Unified scoring matrix for:
- Prompts (from prompt library)
- Skills (from local + vault + remote)
- Models (LLM selection per task)
- MCP servers (external tool integrations)

## Context Template Accretion

Each section of `CLIENT_CONTEXT_FRAMEWORK.md` evolves progressively:

| Maturity | Score | Source Phase |
|----------|-------|-------------|
| Stub | 0.2 | Phase 1 (Goal Definition) |
| Shallow | 0.5 | Phase 2 (Proposal Research) |
| Adequate | 0.7 | Phases 7-8 (Deep Research) |
| Deep | 0.9 | Phase 9 (Context Synthesis) |

Never claim 1.0 — there's always more to learn.

## Integration with AntiGravity Base

This skill integrates with:
- `skills/find-skills/` — Discovers tools during Phase 11
- `skills/prompt-library/` — Selects prompts during Phase 11
- `skills/context-engineering/` — Builds context framework in Phase 9
- `context/goals.md` — Written by Phase 1
- `context/brand.md` — Enriched by Phase 9
- `directives/security_protocol.md` — Checked before any execution
