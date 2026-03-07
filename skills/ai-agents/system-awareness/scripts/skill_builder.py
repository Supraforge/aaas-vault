#!/usr/bin/env python3
"""
skill_builder.py - Build skills from approved proposals (completes the HR loop)

This is the missing piece that connects:
  proposal → actual skill → registry → context files

Usage:
    python skill_builder.py --proposal ecg-analyzer-proposal.md    # Build from proposal
    python skill_builder.py --name "ecg-analyzer" --purpose "..."  # Build directly
    python skill_builder.py --from-gap gap_20251231_162226_89a758  # Build from gap
    python skill_builder.py --list-proposals                        # List pending proposals
"""

import os
import re
import json
import argparse
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, List

# Paths
SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR.parent / "data"
TEMPLATES_DIR = DATA_DIR / "skill-templates"
GAP_LOG_PATH = DATA_DIR / "gap-log.json"
BACKLOG_PATH = DATA_DIR / "skill-backlog.json"
REGISTRY_PATH = DATA_DIR / "capability-registry.json"

# Skill directories - resolve relative to this script's location
# scripts/ -> system-awareness/ -> cardiology/ -> skills/
SKILLS_ROOT = SCRIPT_DIR.parent.parent.parent
CARDIOLOGY_DIR = SKILLS_ROOT / "cardiology"
SCIENTIFIC_DIR = SKILLS_ROOT / "scientific"


def load_json(path: Path) -> dict:
    """Load JSON file."""
    if path.exists():
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def save_json(path: Path, data: dict) -> None:
    """Save JSON file."""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def parse_proposal(proposal_path: Path) -> Dict:
    """Parse a proposal markdown file to extract skill details."""
    if not proposal_path.exists():
        raise FileNotFoundError(f"Proposal not found: {proposal_path}")

    content = proposal_path.read_text(encoding='utf-8')

    # Extract skill name from title
    name_match = re.search(r'^# Proposed Skill: (.+)$', content, re.MULTILINE)
    name = name_match.group(1).strip() if name_match else proposal_path.stem.replace('-proposal', '')

    # Extract gap ID
    gap_match = re.search(r'\*\*Gap ID\*\*: (.+)$', content, re.MULTILINE)
    gap_id = gap_match.group(1).strip() if gap_match else None
    if gap_id == "N/A":
        gap_id = None

    # Extract purpose/problem statement
    purpose_match = re.search(r'### Problem Statement\n(.+?)(?:\n\n|\n###)', content, re.DOTALL)
    purpose = purpose_match.group(1).strip() if purpose_match else ""

    # If no problem statement, try Purpose section
    if not purpose:
        purpose_match = re.search(r'### Purpose\n(.+?)(?:\n\n|\n###)', content, re.DOTALL)
        purpose = purpose_match.group(1).strip() if purpose_match else "Skill description"

    # Extract category
    cat_match = re.search(r'### Category\n`(.+?)`', content)
    category = cat_match.group(1).strip() if cat_match else "cardiology"

    # Extract complexity
    complexity = "medium"
    if "**Complex**" in content and "[x]" in content.split("**Complex**")[0].split("\n")[-1]:
        complexity = "high"
    elif "**Simple**" in content and "[x]" in content.split("**Simple**")[0].split("\n")[-1]:
        complexity = "low"

    # Extract inputs
    inputs_match = re.search(r'### Inputs\n((?:- .+\n)+)', content)
    inputs = []
    if inputs_match:
        for line in inputs_match.group(1).strip().split('\n'):
            inp_match = re.match(r'- \*\*(.+?)\*\*:', line)
            if inp_match:
                inputs.append(inp_match.group(1))

    # Extract outputs
    outputs_match = re.search(r'### Outputs\n((?:- .+\n)+)', content)
    outputs = []
    if outputs_match:
        for line in outputs_match.group(1).strip().split('\n'):
            out_match = re.match(r'- \*\*(.+?)\*\*:', line)
            if out_match:
                outputs.append(out_match.group(1))

    # Extract dependencies
    deps_match = re.search(r'### Dependencies\n((?:- .+\n)+)', content)
    dependencies = []
    if deps_match:
        for line in deps_match.group(1).strip().split('\n'):
            dep_match = re.match(r'- \[.\] (.+)', line)
            if dep_match and dep_match.group(1) != "None identified":
                dependencies.append(dep_match.group(1))

    return {
        "name": name,
        "purpose": purpose,
        "category": category,
        "complexity": complexity,
        "inputs": inputs or ["query"],
        "outputs": outputs or ["result"],
        "dependencies": dependencies,
        "gap_id": gap_id,
        "proposal_path": str(proposal_path)
    }


def generate_skill_md(skill_data: Dict) -> str:
    """Generate SKILL.md content from skill data."""
    name = skill_data["name"]
    name_formatted = name.replace("-", " ").title()
    purpose = skill_data["purpose"]
    category = skill_data["category"]
    complexity = skill_data["complexity"]
    inputs = skill_data.get("inputs", ["query"])
    outputs = skill_data.get("outputs", ["result"])
    dependencies = skill_data.get("dependencies", [])

    # Build inputs/outputs sections
    inputs_section = "\n".join([f"- **{inp}**: [description]" for inp in inputs])
    outputs_section = "\n".join([f"- **{out}**: [description]" for out in outputs])
    deps_section = "\n".join([f"- `{dep}`" for dep in dependencies]) if dependencies else "None"

    skill_md = f"""# {name_formatted}

{purpose}

## Overview

This skill provides capabilities for {purpose.lower() if purpose else 'the specified task'}.

**Category:** `{category}`
**Complexity:** `{complexity}`
**Created:** {datetime.now().strftime("%Y-%m-%d")}
**Source:** Auto-generated by skill_builder.py

---

## Quick Start

### Basic Usage

```
# Example usage pattern
"Use {name} to [describe task]"
```

### Inputs

{inputs_section}

### Outputs

{outputs_section}

---

## Dependencies

{deps_section}

---

## Use Cases

1. **Primary Use Case**
   - [Describe main scenario]

2. **Secondary Use Case**
   - [Describe additional scenario]

---

## Implementation Notes

- [Add implementation details here]
- [Add any special considerations]

---

## References

See `references/` directory for supporting documentation.

---

## Examples

### Example 1: Basic Usage

```
[Add example here]
```

### Example 2: Advanced Usage

```
[Add example here]
```

---

*Auto-generated by System Awareness - Skill Builder*
*Build date: {datetime.now().strftime("%Y-%m-%d %H:%M")}*
"""
    return skill_md


def create_skill_directory(skill_data: Dict, target_category: str = "cardiology") -> Path:
    """Create the skill directory structure."""
    name = skill_data["name"]

    # Determine target directory
    if target_category == "scientific":
        skill_dir = SCIENTIFIC_DIR / name
    else:
        skill_dir = CARDIOLOGY_DIR / name

    # Check if already exists
    if skill_dir.exists():
        print(f"  ⚠️  Skill directory already exists: {skill_dir}")
        return skill_dir

    # Create directories
    skill_dir.mkdir(parents=True, exist_ok=True)
    (skill_dir / "references").mkdir(exist_ok=True)
    (skill_dir / "scripts").mkdir(exist_ok=True)

    # Generate and write SKILL.md
    skill_md_content = generate_skill_md(skill_data)
    (skill_dir / "SKILL.md").write_text(skill_md_content, encoding='utf-8')

    # Create placeholder files
    (skill_dir / "references" / ".gitkeep").touch()

    # Create a basic script template if complexity is medium or high
    if skill_data.get("complexity", "low") in ["medium", "high"]:
        script_name = name.replace("-", "_") + ".py"
        script_template = f'''#!/usr/bin/env python3
"""
{name} - Main script

Auto-generated by skill_builder.py
"""

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="{skill_data.get('purpose', name)}")
    parser.add_argument("--input", "-i", help="Input parameter")
    parser.add_argument("--output", "-o", help="Output path")

    args = parser.parse_args()

    print(f"Running {name}...")
    # TODO: Implement skill logic

    print("Done!")


if __name__ == "__main__":
    main()
'''
        (skill_dir / "scripts" / script_name).write_text(script_template, encoding='utf-8')

    return skill_dir


def mark_gap_resolved(gap_id: str) -> bool:
    """Mark a gap as resolved in the gap log."""
    if not gap_id:
        return False

    gap_log = load_json(GAP_LOG_PATH)

    for gap in gap_log.get("gaps", []):
        if gap["id"] == gap_id:
            gap["status"] = "resolved"
            gap["resolved_at"] = datetime.now().isoformat()
            gap["notes"].append(f"Skill built on {datetime.now().strftime('%Y-%m-%d')}")
            save_json(GAP_LOG_PATH, gap_log)
            return True

    return False


def run_sync_pipeline() -> bool:
    """Run sync_skills.py and generate_context.py."""
    print("\n🔄 Running sync pipeline...")

    sync_script = SCRIPT_DIR / "sync_skills.py"
    context_script = SCRIPT_DIR / "generate_context.py"

    try:
        # Run sync_skills.py --update
        print("  Running sync_skills.py --update...")
        result = subprocess.run(
            ["python", str(sync_script), "--update"],
            capture_output=True,
            text=True,
            cwd=str(SCRIPT_DIR)
        )
        if result.returncode != 0:
            print(f"  ⚠️  sync_skills.py warning: {result.stderr}")

        # Run generate_context.py --update (optional, may need markers)
        print("  Running generate_context.py --update...")
        result = subprocess.run(
            ["python", str(context_script), "--update"],
            capture_output=True,
            text=True,
            cwd=str(SCRIPT_DIR)
        )
        if result.returncode != 0:
            print(f"  ⚠️  generate_context.py note: {result.stderr}")

        return True
    except Exception as e:
        print(f"  ❌ Sync pipeline error: {e}")
        return False


def archive_proposal(proposal_path: Path) -> None:
    """Move proposal to an 'approved' subdirectory."""
    approved_dir = TEMPLATES_DIR / "approved"
    approved_dir.mkdir(exist_ok=True)

    new_path = approved_dir / proposal_path.name
    proposal_path.rename(new_path)
    print(f"  📁 Proposal archived to: {new_path}")


def build_from_proposal(proposal_path: Path, auto_sync: bool = True) -> bool:
    """Build a skill from a proposal file."""
    print(f"\n🏗️  Building skill from proposal: {proposal_path.name}")
    print("=" * 60)

    # Parse proposal
    print("\n📖 Parsing proposal...")
    try:
        skill_data = parse_proposal(proposal_path)
    except Exception as e:
        print(f"  ❌ Failed to parse proposal: {e}")
        return False

    print(f"  Name: {skill_data['name']}")
    print(f"  Category: {skill_data['category']}")
    print(f"  Complexity: {skill_data['complexity']}")
    print(f"  Gap ID: {skill_data.get('gap_id', 'N/A')}")

    # Create skill directory
    print("\n📂 Creating skill directory...")
    try:
        skill_dir = create_skill_directory(skill_data)
        print(f"  ✅ Created: {skill_dir}")
    except Exception as e:
        print(f"  ❌ Failed to create directory: {e}")
        return False

    # Mark gap as resolved
    if skill_data.get("gap_id"):
        print("\n📝 Marking gap as resolved...")
        if mark_gap_resolved(skill_data["gap_id"]):
            print(f"  ✅ Gap {skill_data['gap_id']} marked as resolved")
        else:
            print(f"  ⚠️  Could not find gap {skill_data['gap_id']}")

    # Archive proposal
    print("\n📦 Archiving proposal...")
    try:
        archive_proposal(proposal_path)
    except Exception as e:
        print(f"  ⚠️  Could not archive: {e}")

    # Run sync pipeline
    if auto_sync:
        run_sync_pipeline()

    print("\n" + "=" * 60)
    print("✅ SKILL BUILT SUCCESSFULLY")
    print("=" * 60)
    print(f"\n  Skill: {skill_data['name']}")
    print(f"  Location: {skill_dir}")
    print(f"  SKILL.md: {skill_dir / 'SKILL.md'}")
    print("\nNext steps:")
    print("  1. Edit SKILL.md to add detailed documentation")
    print("  2. Add reference files to references/")
    print("  3. Implement scripts in scripts/ (if needed)")
    print("=" * 60 + "\n")

    return True


def build_directly(name: str, purpose: str, category: str = "cardiology",
                   complexity: str = "medium", auto_sync: bool = True) -> bool:
    """Build a skill directly without a proposal."""
    print(f"\n🏗️  Building skill directly: {name}")
    print("=" * 60)

    skill_data = {
        "name": name,
        "purpose": purpose,
        "category": category,
        "complexity": complexity,
        "inputs": ["query"],
        "outputs": ["result"],
        "dependencies": [],
        "gap_id": None
    }

    # Create skill directory
    print("\n📂 Creating skill directory...")
    try:
        skill_dir = create_skill_directory(skill_data, category)
        print(f"  ✅ Created: {skill_dir}")
    except Exception as e:
        print(f"  ❌ Failed to create directory: {e}")
        return False

    # Run sync pipeline
    if auto_sync:
        run_sync_pipeline()

    print("\n" + "=" * 60)
    print("✅ SKILL BUILT SUCCESSFULLY")
    print("=" * 60)
    print(f"\n  Skill: {name}")
    print(f"  Location: {skill_dir}")
    print("=" * 60 + "\n")

    return True


def build_from_gap(gap_id: str, auto_sync: bool = True) -> bool:
    """Build a skill directly from a gap (propose + build in one step)."""
    print(f"\n🏗️  Building skill from gap: {gap_id}")
    print("=" * 60)

    # Load gap
    gap_log = load_json(GAP_LOG_PATH)
    gap = None
    for g in gap_log.get("gaps", []):
        if g["id"] == gap_id:
            gap = g
            break

    if not gap:
        print(f"  ❌ Gap not found: {gap_id}")
        return False

    skill_data = {
        "name": gap.get("potential_skill", gap_id.replace("gap_", "skill-")),
        "purpose": gap.get("request", ""),
        "category": gap.get("category", "cardiology"),
        "complexity": "medium" if gap.get("urgency") == "high" else "low",
        "inputs": ["query"],
        "outputs": ["result"],
        "dependencies": [],
        "gap_id": gap_id
    }

    print(f"  Name: {skill_data['name']}")
    print(f"  Purpose: {skill_data['purpose'][:60]}...")
    print(f"  Category: {skill_data['category']}")

    # Determine target category
    target_category = "cardiology"
    if skill_data["category"] in ["scientific", "genomics", "chemistry", "bioinformatics"]:
        target_category = "scientific"

    # Create skill directory
    print("\n📂 Creating skill directory...")
    try:
        skill_dir = create_skill_directory(skill_data, target_category)
        print(f"  ✅ Created: {skill_dir}")
    except Exception as e:
        print(f"  ❌ Failed to create directory: {e}")
        return False

    # Mark gap as resolved
    print("\n📝 Marking gap as resolved...")
    if mark_gap_resolved(gap_id):
        print(f"  ✅ Gap marked as resolved")

    # Run sync pipeline
    if auto_sync:
        run_sync_pipeline()

    print("\n" + "=" * 60)
    print("✅ SKILL BUILT FROM GAP")
    print("=" * 60)
    print(f"\n  Gap: {gap_id}")
    print(f"  Skill: {skill_data['name']}")
    print(f"  Location: {skill_dir}")
    print("=" * 60 + "\n")

    return True


def list_proposals() -> None:
    """List all pending proposals."""
    TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)
    proposals = list(TEMPLATES_DIR.glob("*-proposal.md"))

    # Exclude approved folder
    proposals = [p for p in proposals if "approved" not in str(p)]

    if not proposals:
        print("\n📭 No pending proposals.")
        print("\nOptions:")
        print("  1. Create a proposal: python skill_proposer.py --interactive")
        print("  2. Build directly: python skill_builder.py --name 'skill-name' --purpose 'description'")
        print("  3. Build from gap: python skill_builder.py --from-gap gap_id\n")
        return

    print(f"\n📋 Pending Proposals ({len(proposals)})")
    print("=" * 60)

    for i, proposal_path in enumerate(proposals, 1):
        skill_name = proposal_path.stem.replace("-proposal", "")
        mod_time = datetime.fromtimestamp(proposal_path.stat().st_mtime)
        print(f"\n  {i}. {skill_name}")
        print(f"     File: {proposal_path.name}")
        print(f"     Modified: {mod_time.strftime('%Y-%m-%d %H:%M')}")
        print(f"     Build: python skill_builder.py --proposal {proposal_path.name}")

    print("\n" + "=" * 60)
    print("To build a proposal: python skill_builder.py --proposal <filename>")
    print("=" * 60 + "\n")


def list_open_gaps() -> None:
    """List all open gaps that could be built."""
    gap_log = load_json(GAP_LOG_PATH)
    open_gaps = [g for g in gap_log.get("gaps", []) if g.get("status") == "open"]

    if not open_gaps:
        print("\n📭 No open gaps.")
        return

    print(f"\n🔍 Open Gaps ({len(open_gaps)})")
    print("=" * 60)

    for gap in open_gaps:
        print(f"\n  ID: {gap['id']}")
        print(f"  Request: {gap['request'][:60]}...")
        print(f"  Category: {gap.get('category', 'unknown')}")
        print(f"  Urgency: {gap.get('urgency', 'medium')}")
        print(f"  Potential skill: {gap.get('potential_skill', 'N/A')}")
        print(f"  Build: python skill_builder.py --from-gap {gap['id']}")

    print("\n" + "=" * 60 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Build skills from proposals or directly (completes the HR loop)"
    )
    parser.add_argument("--proposal", "-p", help="Build from proposal file")
    parser.add_argument("--name", "-n", help="Skill name (for direct build)")
    parser.add_argument("--purpose", help="Skill purpose (for direct build)")
    parser.add_argument("--category", "-c", default="cardiology",
                        help="Category: cardiology or scientific")
    parser.add_argument("--complexity", default="medium",
                        choices=["low", "medium", "high"], help="Skill complexity")
    parser.add_argument("--from-gap", "-g", help="Build directly from gap ID")
    parser.add_argument("--list-proposals", "-l", action="store_true",
                        help="List pending proposals")
    parser.add_argument("--list-gaps", action="store_true", help="List open gaps")
    parser.add_argument("--no-sync", action="store_true",
                        help="Skip running sync pipeline after build")

    args = parser.parse_args()

    # List modes
    if args.list_proposals:
        list_proposals()
        return

    if args.list_gaps:
        list_open_gaps()
        return

    # Build from proposal
    if args.proposal:
        proposal_path = TEMPLATES_DIR / args.proposal
        if not proposal_path.exists():
            # Try without .md extension
            proposal_path = TEMPLATES_DIR / f"{args.proposal}.md"
        if not proposal_path.exists():
            # Try with -proposal suffix
            proposal_path = TEMPLATES_DIR / f"{args.proposal}-proposal.md"

        if not proposal_path.exists():
            print(f"❌ Proposal not found: {args.proposal}")
            print(f"   Searched in: {TEMPLATES_DIR}")
            list_proposals()
            return

        build_from_proposal(proposal_path, auto_sync=not args.no_sync)
        return

    # Build from gap
    if args.from_gap:
        build_from_gap(args.from_gap, auto_sync=not args.no_sync)
        return

    # Direct build
    if args.name and args.purpose:
        build_directly(
            name=args.name,
            purpose=args.purpose,
            category=args.category,
            complexity=args.complexity,
            auto_sync=not args.no_sync
        )
        return

    # Interactive mode - show options
    print("\n🛠️  Skill Builder")
    print("=" * 60)
    print("\nUsage:")
    print("  Build from proposal:  python skill_builder.py --proposal <file>")
    print("  Build from gap:       python skill_builder.py --from-gap <gap_id>")
    print("  Build directly:       python skill_builder.py --name <name> --purpose <desc>")
    print("\nList options:")
    print("  List proposals:       python skill_builder.py --list-proposals")
    print("  List open gaps:       python skill_builder.py --list-gaps")
    print("=" * 60)

    # Show current status
    list_proposals()
    list_open_gaps()


if __name__ == "__main__":
    main()
