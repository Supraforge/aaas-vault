#!/usr/bin/env python3
"""
Research Protocol — Phase Runner

Orchestrates the 11-phase Universal Agentic Production Protocol.
Each phase reads inputs from previous phases and writes structured output.

Usage:
  python3 skills/research-protocol/scripts/run_phase.py 1 --project="My SaaS App"
  python3 skills/research-protocol/scripts/run_phase.py 2 --project="My SaaS App"
  python3 skills/research-protocol/scripts/run_phase.py all-pre --project="My SaaS App"
  python3 skills/research-protocol/scripts/run_phase.py all-post --project="My SaaS App"
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Resolve project root (2 levels up from scripts/)
SKILL_DIR = Path(__file__).parent.parent
PROJECT_ROOT = SKILL_DIR.parent.parent
CONTEXT_DIR = PROJECT_ROOT / "context"
TMP_DIR = PROJECT_ROOT / ".tmp"
TEMPLATES_DIR = SKILL_DIR / "templates"

# Phase definitions
PHASES = {
    1: {"name": "Goal Definition", "block": "pre", "output": "context/goals.md"},
    2: {"name": "Proposal Research", "block": "pre", "output": ".tmp/research_phase2.md"},
    3: {"name": "Strategy Routes", "block": "pre", "output": ".tmp/strategy_routes.md"},
    4: {"name": "Requirements Engineering", "block": "pre", "output": ".tmp/PROJECT_REQUIREMENTS.md"},
    5: {"name": "Proposal Generation", "block": "pre", "output": ".tmp/proposal_draft.md"},
    6: {"name": "Client Activation", "block": "pre", "output": None},
    7: {"name": "Competitive Research", "block": "post", "output": ".tmp/competitive_research.md"},
    8: {"name": "Industry Knowledge", "block": "post", "output": ".tmp/industry_knowledge.md"},
    9: {"name": "Context Synthesis", "block": "post", "output": "context/CLIENT_CONTEXT_FRAMEWORK.md"},
    10: {"name": "Sub-Project Goals", "block": "post", "output": ".tmp/sub_project_goals.md"},
    11: {"name": "Tool Selection", "block": "post", "output": ".tmp/tool_selection.md"},
}

PRE_PHASES = [1, 2, 3, 4, 5, 6]
POST_PHASES = [7, 8, 9, 10, 11]


def ensure_dirs():
    """Ensure required directories exist."""
    TMP_DIR.mkdir(exist_ok=True)
    CONTEXT_DIR.mkdir(exist_ok=True)


def get_phase_status():
    """Check which phases have been completed."""
    status = {}
    for num, phase in PHASES.items():
        if phase["output"] is None:
            status[num] = "manual"
        elif (PROJECT_ROOT / phase["output"]).exists():
            status[num] = "done"
        else:
            status[num] = "pending"
    return status


def print_status(project_name: str):
    """Print current protocol status."""
    status = get_phase_status()
    print(f"\n{'='*60}")
    print(f"  Research Protocol — {project_name}")
    print(f"{'='*60}\n")

    print("  PRE-ACTIVATION (Think Before Building)")
    print("  " + "-" * 40)
    for num in PRE_PHASES:
        phase = PHASES[num]
        icon = {"done": "done", "pending": "    ", "manual": "GATE"}.get(status[num], "    ")
        print(f"  [{icon}] Phase {num}: {phase['name']}")

    print(f"\n  POST-ACTIVATION (Build With Intelligence)")
    print("  " + "-" * 40)
    for num in POST_PHASES:
        phase = PHASES[num]
        icon = {"done": "done", "pending": "    ", "manual": "GATE"}.get(status[num], "    ")
        print(f"  [{icon}] Phase {num}: {phase['name']}")

    print()


def run_phase(phase_num: int, project_name: str):
    """Run a specific phase."""
    if phase_num not in PHASES:
        print(f"  Unknown phase: {phase_num}")
        return False

    phase = PHASES[phase_num]
    print(f"\n  Phase {phase_num}: {phase['name']}")
    print(f"  {'='*40}")

    if phase_num == 6:
        print("  HUMAN GATE: Present proposal to human for approval.")
        print("  NO production work begins until this gate is passed.")
        print("  Mark as complete by creating: .tmp/phase6_approved.txt")
        return True

    output_path = PROJECT_ROOT / phase["output"]

    if output_path.exists():
        print(f"  Output already exists: {phase['output']}")
        overwrite = input("  Overwrite? (y/n): ").strip().lower()
        if overwrite != "y":
            print("  Skipped.")
            return True

    # Create output stub with instructions for the agent
    instructions = _get_phase_instructions(phase_num, project_name)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(instructions)
    print(f"  Template created: {phase['output']}")
    print(f"  Next: Have your agent fill in this template with real research.")
    return True


def _get_phase_instructions(phase_num: int, project_name: str) -> str:
    """Generate phase-specific template content."""
    date = datetime.now().strftime("%Y-%m-%d")

    templates = {
        1: f"""# {project_name} — Goal Brief
> Phase 1 | Generated: {date}

## Primary Objective
- **What:** [clear statement of what we're building]
- **Why:** [business justification]
- **For Whom:** [target audience]

## Success Criteria
- [ ] [Measurable criterion 1]
- [ ] [Measurable criterion 2]
- [ ] [Measurable criterion 3]

## Constraints
- **Budget:** [amount or range]
- **Timeline:** [deadline]
- **Technical:** [stack requirements, integrations]

## Scope Boundaries
- **IN scope:** [explicit list]
- **OUT of scope:** [explicit list]

## KPIs
| Metric | Current | Target | Deadline |
|--------|---------|--------|----------|
| [metric] | [value] | [target] | [date] |
""",
        2: f"""# {project_name} — Proposal Research
> Phase 2 (Fast Mode) | Generated: {date}

## Market Scan
[What exists? Who are the competitors?]

## Technology Scan
[What tools/frameworks fit the requirements?]

## Reference Implementations
[GitHub repos, open-source projects, templates that solve 80%+ of the problem]

## Pricing & Positioning
[How do competitors price similar offerings?]

## Key Findings
1. [Finding 1]
2. [Finding 2]
3. [Finding 3]

## Research Sources
- [Source 1]
- [Source 2]
""",
        3: f"""# {project_name} — Strategy Routes
> Phase 3 | Generated: {date}

## Route 1: [Name]
### Approach
[2-3 sentence description]
### Pros
- [advantage]
### Cons
- [disadvantage]
### Estimated Effort
- Time: [duration] | Cost: [estimate] | Complexity: [Low/Medium/High]
### Tech Stack
- [choices]

## Route 2: [Name]
### Approach
[2-3 sentence description]
### Pros
- [advantage]
### Cons
- [disadvantage]
### Estimated Effort
- Time: [duration] | Cost: [estimate] | Complexity: [Low/Medium/High]
### Tech Stack
- [choices]

## Recommended Route
[Which route and why]
""",
        4: f"""# {project_name} — Project Requirements
> Phase 4 | Generated: {date}

## Part A: Execution Requirements

### Resource Plan
[People, tools, infrastructure needed]

### Skill Mapping
[Which skills from vault/local are needed]

### Dependency Chain
[What depends on what — ordered sequence]

### Timeline
| Phase | Task | Duration | Dependencies |
|-------|------|----------|-------------|
| [phase] | [task] | [days] | [deps] |

### Risk Register
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| [risk] | [H/M/L] | [H/M/L] | [action] |

## Part B: Client Deliverable Spec

### Deliverables
| # | Deliverable | Format | Quality Criteria |
|---|------------|--------|-----------------|
| 1 | [item] | [format] | [criteria] |

### Acceptance Process
[How deliverables are reviewed and accepted]
""",
        5: f"""# {project_name} — Proposal Draft
> Phase 5 | Generated: {date}

## Executive Summary
[One paragraph overview]

## Problem Statement
[What problem are we solving]

## Proposed Solution
[How we solve it — reference chosen strategy route]

## Deliverables
[What the client gets]

## Timeline & Milestones
[Key dates and checkpoints]

## Investment
[Pricing]

## Why Us
[Differentiators]
""",
        7: f"""# {project_name} — Competitive Research
> Phase 7 (Deep Mode) | Generated: {date}

## Competitor 1: [Name]
### Overview
### Strengths
### Weaknesses
### Pricing
### Tech Stack
### Market Position

## Competitor 2: [Name]
[same structure]

## Competitive Matrix
| Feature | Us | Comp 1 | Comp 2 |
|---------|-----|--------|--------|
| [feature] | [score] | [score] | [score] |

## Strategic Opportunities
[Where competitors are weak and we can differentiate]
""",
        8: f"""# {project_name} — Industry Knowledge
> Phase 8 (Deep Mode) | Generated: {date}

## Industry Overview
[Size, growth, trends]

## Key Trends
1. [Trend 1]
2. [Trend 2]
3. [Trend 3]

## Regulatory Landscape
[Relevant regulations, compliance requirements]

## Technology Landscape
[Emerging tech, standard stacks, innovation areas]

## Customer Behavior
[How target audience makes decisions, buys, uses products]
""",
        9: f"""# {project_name} — Client Context Framework
> Phase 9 (Synthesis) | Generated: {date}
> Overall Maturity: 0.9

[See context-engineering skill for full template]
""",
        10: f"""# {project_name} — Sub-Project Goals
> Phase 10 | Generated: {date}

## Execution Sequence

### Sub-Project 1: [Name]
- **Goal:** [what]
- **Dependencies:** [none / sub-project X]
- **Skills Needed:** [list]
- **Estimated Duration:** [time]

### Sub-Project 2: [Name]
- **Goal:** [what]
- **Dependencies:** [sub-project 1]
- **Skills Needed:** [list]
- **Estimated Duration:** [time]

## Dependency Graph
[Sub-Project 1] → [Sub-Project 2] → [Sub-Project 3]
""",
        11: f"""# {project_name} — Tool Selection
> Phase 11 | Generated: {date}

## Selected Tools

### Prompts (from prompt-library)
| Prompt | Phase | Purpose |
|--------|-------|---------|
| [id] | [phase] | [why] |

### Skills (from vault + local)
| Skill | Source | Purpose |
|-------|--------|---------|
| [name] | [local/vault/remote] | [why] |

### Models (LLM selection)
| Task | Model | Reasoning |
|------|-------|-----------|
| [task] | [model] | [why this model] |

### MCP Servers
| Server | Purpose |
|--------|---------|
| [name] | [what it provides] |
""",
    }

    return templates.get(phase_num, f"# Phase {phase_num}\n\n[Template not available]")


def main():
    parser = argparse.ArgumentParser(description="Research Protocol Phase Runner")
    parser.add_argument(
        "phase",
        help="Phase number (1-11), 'all-pre', 'all-post', or 'status'",
    )
    parser.add_argument("--project", default="Untitled Project", help="Project name")
    args = parser.parse_args()

    ensure_dirs()

    if args.phase == "status":
        print_status(args.project)
        return

    if args.phase == "all-pre":
        for num in PRE_PHASES:
            run_phase(num, args.project)
        return

    if args.phase == "all-post":
        # Check Phase 6 gate
        gate_file = TMP_DIR / "phase6_approved.txt"
        if not gate_file.exists():
            print("  Phase 6 (Client Activation) has not been approved.")
            print("  Create .tmp/phase6_approved.txt to proceed.")
            return
        for num in POST_PHASES:
            run_phase(num, args.project)
        return

    try:
        phase_num = int(args.phase)
    except ValueError:
        print(f"  Unknown command: {args.phase}")
        print("  Usage: run_phase.py [1-11|all-pre|all-post|status]")
        return

    run_phase(phase_num, args.project)


if __name__ == "__main__":
    main()
