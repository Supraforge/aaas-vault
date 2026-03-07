#!/usr/bin/env python3
"""
Skill Proposer - Generates skill specifications from identified gaps.

This script creates SKILL.md proposals that can be reviewed and approved
before being built into actual skills.

Usage:
    python skill_proposer.py --gap-id "gap_2024_001"
    python skill_proposer.py --name "ecg-analyzer" --purpose "Analyze ECG images"
    python skill_proposer.py --interactive
"""

import json
import os
import argparse
from datetime import datetime
from pathlib import Path
from typing import Optional

# Paths
SCRIPT_DIR = Path(__file__).parent.parent
DATA_DIR = SCRIPT_DIR / "data"
TEMPLATES_DIR = DATA_DIR / "skill-templates"
GAP_LOG_PATH = DATA_DIR / "gap-log.json"
BACKLOG_PATH = DATA_DIR / "skill-backlog.json"
REGISTRY_PATH = DATA_DIR / "capability-registry.json"


def load_json(path: Path) -> dict:
    """Load JSON file or return empty structure."""
    if path.exists():
        with open(path, 'r') as f:
            return json.load(f)
    return {}


def save_json(path: Path, data: dict) -> None:
    """Save data to JSON file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)


def get_gap_by_id(gap_id: str) -> Optional[dict]:
    """Retrieve a gap by its ID."""
    gap_data = load_json(GAP_LOG_PATH)
    for gap in gap_data.get("gaps", []):
        if gap["id"] == gap_id:
            return gap
    return None


def suggest_similar_skills(category: str, request: str) -> list:
    """Find similar existing skills to learn from."""
    registry = load_json(REGISTRY_PATH)

    # Category-based suggestions
    category_map = {
        "content-creation": ["youtube-script-master", "x-post-creator-skill", "cardiology-newsletter-writer"],
        "research": ["knowledge-pipeline", "pubmed-database", "social-media-trends-research"],
        "visual": ["cardiology-visual-system", "gemini-imagegen"],
        "analysis": ["viral-content-predictor", "cardiology-trial-editorial"],
        "medical-imaging": ["cardiology-visual-system"],
        "quality": ["authentic-voice", "content-reflection"],
        "automation": ["multi-model-writer", "browser-automation"],
    }

    suggestions = category_map.get(category, [])

    # Keyword-based suggestions from request
    request_lower = request.lower()
    keyword_skills = {
        "tweet": ["x-post-creator-skill", "cardiology-tweet-writer"],
        "youtube": ["youtube-script-master", "hook-generator"],
        "image": ["cardiology-visual-system", "gemini-imagegen"],
        "research": ["knowledge-pipeline", "pubmed-database"],
        "pubmed": ["pubmed-database"],
        "trial": ["cardiology-trial-editorial"],
        "newsletter": ["cardiology-newsletter-writer"]
    }

    for keyword, skills in keyword_skills.items():
        if keyword in request_lower:
            suggestions.extend(skills)

    # Remove duplicates while preserving order
    seen = set()
    return [s for s in suggestions if not (s in seen or seen.add(s))][:5]


def estimate_complexity(purpose: str, has_scripts: bool = False, has_api: bool = False) -> str:
    """Estimate skill complexity based on requirements."""
    complexity_indicators = {
        "high": ["ml", "model", "train", "api", "database", "pipeline", "integrate", "automation"],
        "medium": ["analyze", "process", "generate", "extract", "parse"],
        "low": ["format", "template", "guide", "reference", "checklist"]
    }

    purpose_lower = purpose.lower()

    for level, keywords in complexity_indicators.items():
        if any(kw in purpose_lower for kw in keywords):
            return level

    if has_api or has_scripts:
        return "medium"

    return "low"


def generate_skill_proposal(
    name: str,
    purpose: str,
    category: str,
    inputs: list = None,
    outputs: list = None,
    dependencies: list = None,
    gap_id: str = None,
    context: str = None
) -> str:
    """Generate a SKILL.md proposal document."""

    inputs = inputs or ["topic", "query"]
    outputs = outputs or ["result", "formatted_output"]
    dependencies = dependencies or []

    similar_skills = suggest_similar_skills(category, purpose)
    complexity = estimate_complexity(purpose)

    # Format skill name
    skill_name_formatted = name.replace("-", " ").title()

    proposal = f"""# Proposed Skill: {name}

> **Status**: PROPOSAL - Pending Approval
> **Generated**: {datetime.now().strftime("%Y-%m-%d %H:%M")}
> **Gap ID**: {gap_id or "N/A"}

---

## Gap Analysis

### Origin
{f"This skill was proposed to address gap `{gap_id}`" if gap_id else "Manual proposal"}

### Problem Statement
{purpose}

### Context
{context or "User encountered a capability gap during normal usage."}

### Frequency
- Request frequency: (to be filled from gap log)
- User impact: (assess based on workflow blockage)

---

## Skill Specification

### Purpose
{purpose}

### Category
`{category}`

### Inputs
{chr(10).join(f"- **{inp}**: [describe type and format]" for inp in inputs)}

### Outputs
{chr(10).join(f"- **{out}**: [describe type and format]" for out in outputs)}

### Dependencies
{chr(10).join(f"- [ ] {dep}" for dep in dependencies) if dependencies else "- [ ] None identified"}

---

## Use Cases

1. **Primary Use Case**
   - [Describe the main scenario where this skill is used]

2. **Secondary Use Case**
   - [Describe additional scenarios]

3. **Edge Cases**
   - [Describe unusual but valid uses]

---

## Similar Skills (Learn From)

{chr(10).join(f"- **{skill}**: [what patterns to borrow]" for skill in similar_skills) if similar_skills else "- No similar skills identified"}

---

## Implementation Plan

### Complexity Assessment
- [ ] **Simple** (documentation only) - SKILL.md + references/
- [{"x" if complexity == "medium" else " "}] **Medium** (docs + reference files) - Above + structured references
- [{"x" if complexity == "high" else " "}] **Complex** (docs + scripts + API) - Above + Python scripts + API integration

### Estimated Complexity: `{complexity.upper()}`

### Files to Create
```
skills/cardiology/{name}/
├── SKILL.md                    # Main documentation
├── references/                 # Reference files (if needed)
│   └── [reference-files].md
└── scripts/                    # Python scripts (if needed)
    └── [script-files].py
```

### Implementation Steps
1. [ ] Create directory structure
2. [ ] Write SKILL.md with full documentation
3. [ ] Create reference files (if applicable)
4. [ ] Implement Python scripts (if applicable)
5. [ ] Test with sample inputs
6. [ ] Update capability registry
7. [ ] Document in SKILL-CATALOG.md

---

## Review Checklist

Before approving this skill, verify:

- [ ] **Need**: Is this capability truly needed? (frequency >= 2)
- [ ] **Unique**: Does this not duplicate existing skills?
- [ ] **Feasible**: Can this be built with available resources?
- [ ] **Maintainable**: Can this be kept updated?
- [ ] **Scoped**: Is the scope well-defined and not too broad?

---

## Decision

**Recommendation**: [ ] BUILD | [ ] DEFER | [ ] MERGE with existing skill | [ ] REJECT

**Rationale**: (to be filled by reviewer)

**Approved by**: (signature)
**Date**: (approval date)

---

## Post-Approval Actions

After approval:
1. Create skill directory
2. Implement according to plan
3. Update `capability-registry.json`
4. Update `SKILL-CATALOG.md`
5. Mark gap as "resolved" in gap log
6. Remove from skill backlog

---

*Generated by System Awareness - Skill Proposer*
"""
    return proposal


def interactive_proposal():
    """Interactive skill proposal mode."""
    print("\n🛠️  Skill Proposer - Interactive Mode")
    print("=" * 50)

    name = input("\nSkill name (kebab-case, e.g., 'ecg-analyzer'):\n> ").strip()
    if not name:
        print("❌ Name is required")
        return

    purpose = input("\nWhat does this skill do? (one sentence):\n> ").strip()
    if not purpose:
        print("❌ Purpose is required")
        return

    categories = ["content-creation", "research", "visual", "analysis",
                  "medical-imaging", "audio-video", "automation", "integration",
                  "data-extraction", "quality", "other"]
    print(f"\nCategories: {', '.join(categories)}")
    category = input("Category: ").strip()
    if category not in categories:
        category = "other"

    inputs_raw = input("\nInputs (comma-separated, e.g., 'topic, query'):\n> ").strip()
    inputs = [i.strip() for i in inputs_raw.split(",")] if inputs_raw else None

    outputs_raw = input("\nOutputs (comma-separated):\n> ").strip()
    outputs = [o.strip() for o in outputs_raw.split(",")] if outputs_raw else None

    deps_raw = input("\nDependencies (comma-separated, or press Enter for none):\n> ").strip()
    dependencies = [d.strip() for d in deps_raw.split(",")] if deps_raw else None

    context = input("\nAdditional context (optional):\n> ").strip()

    # Generate proposal
    proposal = generate_skill_proposal(
        name=name,
        purpose=purpose,
        category=category,
        inputs=inputs,
        outputs=outputs,
        dependencies=dependencies,
        context=context or None
    )

    # Save proposal
    TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)
    output_path = TEMPLATES_DIR / f"{name}-proposal.md"
    with open(output_path, 'w') as f:
        f.write(proposal)

    print("\n" + "=" * 50)
    print(f"✅ Proposal saved to: {output_path}")
    print("\nNext steps:")
    print("1. Review the proposal")
    print("2. Mark decision: BUILD / DEFER / REJECT")
    print("3. If approved, create the skill directory")
    print("=" * 50 + "\n")


def propose_from_gap(gap_id: str) -> None:
    """Generate a proposal from an existing gap."""
    gap = get_gap_by_id(gap_id)

    if not gap:
        print(f"❌ Gap not found: {gap_id}")
        return

    name = gap.get("potential_skill", gap_id.replace("gap_", "skill-"))
    purpose = gap.get("request", "")
    category = gap.get("category", "other")
    context = gap.get("context", "")

    proposal = generate_skill_proposal(
        name=name,
        purpose=purpose,
        category=category,
        gap_id=gap_id,
        context=context
    )

    # Save proposal
    TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)
    output_path = TEMPLATES_DIR / f"{name}-proposal.md"
    with open(output_path, 'w') as f:
        f.write(proposal)

    print(f"\n✅ Proposal generated from gap: {gap_id}")
    print(f"   Saved to: {output_path}")
    print(f"   Skill name: {name}")
    print(f"   Category: {category}")
    print("\nReview the proposal and mark your decision.\n")


def list_proposals() -> None:
    """List all existing proposals."""
    TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)
    proposals = list(TEMPLATES_DIR.glob("*-proposal.md"))

    if not proposals:
        print("\n📭 No proposals yet.")
        print("Use 'python skill_proposer.py --interactive' to create one.\n")
        return

    print(f"\n📋 Skill Proposals ({len(proposals)})")
    print("=" * 60)

    for proposal_path in proposals:
        skill_name = proposal_path.stem.replace("-proposal", "")
        mod_time = datetime.fromtimestamp(proposal_path.stat().st_mtime)
        print(f"  • {skill_name}")
        print(f"    Last modified: {mod_time.strftime('%Y-%m-%d %H:%M')}")
        print(f"    Path: {proposal_path}")

    print("=" * 60 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Generate skill proposals from gaps or manual input"
    )
    parser.add_argument("--gap-id", "-g", help="Generate proposal from gap ID")
    parser.add_argument("--name", "-n", help="Skill name (for manual proposal)")
    parser.add_argument("--purpose", "-p", help="Skill purpose")
    parser.add_argument("--category", "-c", help="Skill category")
    parser.add_argument("--interactive", "-i", action="store_true", help="Interactive mode")
    parser.add_argument("--list", "-l", action="store_true", help="List existing proposals")

    args = parser.parse_args()

    if args.list:
        list_proposals()
        return

    if args.gap_id:
        propose_from_gap(args.gap_id)
        return

    if args.name and args.purpose:
        proposal = generate_skill_proposal(
            name=args.name,
            purpose=args.purpose,
            category=args.category or "other"
        )
        TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)
        output_path = TEMPLATES_DIR / f"{args.name}-proposal.md"
        with open(output_path, 'w') as f:
            f.write(proposal)
        print(f"\n✅ Proposal saved to: {output_path}\n")
        return

    # Default to interactive mode
    interactive_proposal()


if __name__ == "__main__":
    main()
