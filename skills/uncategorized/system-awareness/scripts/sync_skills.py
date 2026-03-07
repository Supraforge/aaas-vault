#!/usr/bin/env python3
"""
sync_skills.py - Auto-discover skills from disk and update capability-registry.json

Scans skills/cardiology/ and skills/scientific/ directories for SKILL.md files,
parses metadata, compares with the capability registry, and optionally updates it.

Usage:
    python sync_skills.py                         # Dry-run: scan and report differences
    python sync_skills.py --update                # Actually update the registry
    python sync_skills.py --verbose               # Show detailed output
    python sync_skills.py --dry-run --report      # Generate detailed report file
    python sync_skills.py --check-discrepancies   # Show changes in existing skills
"""

import os
import re
import json
import argparse
import logging
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any

# Configure logging
LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / f"sync_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Paths
SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR.parent / "data"
REGISTRY_PATH = DATA_DIR / "capability-registry.json"
REPORTS_DIR = DATA_DIR / "sync-reports"
# Skill directories - resolve relative to this script's location
# scripts/ -> system-awareness/ -> cardiology/ -> skills/
SKILLS_ROOT = SCRIPT_DIR.parent.parent.parent

CARDIOLOGY_DIR = SKILLS_ROOT / "cardiology"
SCIENTIFIC_DIR = SKILLS_ROOT / "scientific"


def parse_yaml_frontmatter(content: str) -> Tuple[Dict, str]:
    """Extract YAML frontmatter and remaining markdown content."""
    frontmatter = {}
    markdown_content = content

    # Check for YAML frontmatter (starts with ---)
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1]) or {}
                markdown_content = parts[2].strip()
            except yaml.YAMLError as e:
                logger.warning(f"Failed to parse YAML frontmatter: {e}")

    return frontmatter, markdown_content


def extract_inputs_outputs(content: str) -> Tuple[List[str], List[str]]:
    """Extract inputs and outputs from markdown content."""
    inputs = []
    outputs = []

    # Look for ## Inputs or ## Input section
    input_match = re.search(r'##\s*Inputs?\s*\n(.*?)(?=\n##|\Z)', content, re.IGNORECASE | re.DOTALL)
    if input_match:
        section = input_match.group(1)
        # Extract bullet points or list items
        items = re.findall(r'[-*]\s*\*?\*?`?([^`\n*]+)`?\*?\*?', section)
        inputs = [item.strip().lower().replace(' ', '_')[:50] for item in items if item.strip()][:10]

    # Look for ## Outputs or ## Output section
    output_match = re.search(r'##\s*Outputs?\s*\n(.*?)(?=\n##|\Z)', content, re.IGNORECASE | re.DOTALL)
    if output_match:
        section = output_match.group(1)
        items = re.findall(r'[-*]\s*\*?\*?`?([^`\n*]+)`?\*?\*?', section)
        outputs = [item.strip().lower().replace(' ', '_')[:50] for item in items if item.strip()][:10]

    return inputs, outputs


def extract_use_cases(content: str) -> List[str]:
    """Extract use cases from markdown content."""
    use_cases = []

    # Look for ## When to Use, ## Use Cases, ## Triggers
    pattern = r'##\s*(?:When to Use|Use Cases?|Triggers?|Usage)\s*\n(.*?)(?=\n##|\Z)'
    match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
    if match:
        section = match.group(1)
        # Extract bullet points or table rows
        items = re.findall(r'[-*|]\s*\*?\*?`?([^`\n*|]+)`?\*?\*?', section)
        for item in items:
            cleaned = item.strip().lower().replace(' ', '_')[:50]
            if cleaned and len(cleaned) > 3 and not cleaned.startswith('--'):
                use_cases.append(cleaned)

    return use_cases[:10]


def extract_dependencies(content: str) -> List[str]:
    """Extract dependencies from markdown content."""
    dependencies = []

    # Look for ## Dependencies, ## Requires, ## Prerequisites
    pattern = r'##\s*(?:Dependencies|Requires|Prerequisites)\s*\n(.*?)(?=\n##|\Z)'
    match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
    if match:
        section = match.group(1)
        items = re.findall(r'[-*]\s*\*?\*?`?([a-z0-9_-]+)`?\*?\*?', section, re.IGNORECASE)
        dependencies = [item.strip().lower() for item in items if item.strip()][:10]

    return dependencies


def infer_subcategory(skill_id: str, description: str, content: str) -> str:
    """Infer subcategory from skill ID, description, and content."""
    text = f"{skill_id} {description} {content[:500]}".lower()

    # Content creation subcategories
    if any(kw in text for kw in ['youtube', 'script', 'video']):
        return "content-creation/youtube"
    if any(kw in text for kw in ['tweet', 'twitter', 'x-post', 'social media']):
        return "content-creation/twitter"
    if any(kw in text for kw in ['newsletter', 'email']):
        return "content-creation/newsletter"
    if any(kw in text for kw in ['editorial', 'opinion', 'topol']):
        return "content-creation/editorial"
    if any(kw in text for kw in ['carousel', 'instagram', 'slide']):
        return "content-creation/visual"

    # Research subcategories
    if any(kw in text for kw in ['pubmed', 'literature', 'research paper']):
        return "research/pubmed"
    if any(kw in text for kw in ['trend', 'viral', 'social listening']):
        return "research/trends"
    if any(kw in text for kw in ['rag', 'knowledge', 'pipeline']):
        return "research/rag"

    # Quality subcategories
    if any(kw in text for kw in ['voice', 'authentic', 'anti-ai']):
        return "quality/voice"
    if any(kw in text for kw in ['review', 'reflection', 'critical']):
        return "quality/accuracy"

    # Visual subcategories
    if any(kw in text for kw in ['image', 'visual', 'infographic', 'chart']):
        return "visual/images"

    # Analysis subcategories
    if any(kw in text for kw in ['score', 'predict', 'analyzer']):
        return "analysis/ml"
    if any(kw in text for kw in ['statistic', 'data analysis']):
        return "analysis/statistics"

    # Utilities
    if any(kw in text for kw in ['extract', 'scrape', 'fetch']):
        return "utilities/extraction"
    if any(kw in text for kw in ['automat', 'browser', 'mcp']):
        return "utilities/automation"

    return "general"


def parse_skill_md(skill_path: Path) -> Optional[Dict]:
    """Parse a SKILL.md file to extract metadata using YAML frontmatter and markdown parsing."""
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        logger.debug(f"No SKILL.md found in {skill_path}")
        return None

    try:
        content = skill_md.read_text(encoding='utf-8')
    except Exception as e:
        logger.warning(f"Could not read {skill_md}: {e}")
        return None

    skill_id = skill_path.name
    logger.debug(f"Parsing skill: {skill_id}")

    # Parse YAML frontmatter
    frontmatter, markdown_content = parse_yaml_frontmatter(content)

    # Get name from frontmatter or first heading
    name = frontmatter.get('name', '')
    if not name:
        name_match = re.search(r'^#\s+(.+?)(?:\s*[-–—]\s*.+)?$', markdown_content, re.MULTILINE)
        name = name_match.group(1).strip() if name_match else skill_id.replace('-', ' ').title()

    # Get description from frontmatter or first paragraph
    description = frontmatter.get('description', '')
    if isinstance(description, str):
        description = ' '.join(description.split())[:300]  # Clean whitespace, limit length
    else:
        description = str(description)[:300]

    if not description:
        desc_match = re.search(r'^#.+?\n+(?:>\s*.+?\n+)?(.+?)(?:\n\n|\n#)', markdown_content, re.MULTILINE | re.DOTALL)
        if desc_match:
            description = ' '.join(desc_match.group(1).split())[:300]

    # Extract inputs, outputs, use cases, dependencies from markdown
    inputs, outputs = extract_inputs_outputs(markdown_content)
    use_cases = extract_use_cases(markdown_content)
    dependencies = extract_dependencies(markdown_content)

    # Check for scripts directory
    scripts_dir = skill_path / "scripts"
    has_scripts = scripts_dir.exists() and any(scripts_dir.glob("*.py"))
    scripts = [f.name for f in scripts_dir.glob("*.py")] if has_scripts else []

    # Determine category from parent directory
    if "cardiology" in str(skill_path):
        category = "cardiology"
    elif "scientific" in str(skill_path):
        category = "scientific"
    else:
        category = "other"

    # Infer subcategory
    subcategory = infer_subcategory(skill_id, description, markdown_content)

    # Estimate complexity
    complexity = "low"
    if has_scripts:
        complexity = "medium"
        if len(scripts) > 2:
            complexity = "high"
    if len(markdown_content) > 5000:
        complexity = "high"

    # Check for references directory
    refs_dir = skill_path / "references"
    has_references = refs_dir.exists() and any(refs_dir.iterdir()) if refs_dir.exists() else False

    # Build coverage list
    coverage = [category]
    if 'cardiology' in skill_id or 'cardio' in description.lower():
        if 'cardiology' not in coverage:
            coverage.append('cardiology')

    return {
        "id": skill_id,
        "name": name,
        "category": category,
        "subcategory": subcategory,
        "description": description if description else f"Skill for {skill_id}",
        "inputs": inputs,
        "outputs": outputs,
        "dependencies": dependencies,
        "use_cases": use_cases,
        "coverage": coverage,
        "has_scripts": has_scripts,
        "scripts": scripts,
        "has_references": has_references,
        "complexity": complexity,
        "usage_count": 0,
        "last_used": None,
        "auto_discovered": True,
        "discovered_at": datetime.now().isoformat()
    }


def scan_skills_directory(directory: Path) -> List[Dict]:
    """Scan a directory for skills (directories containing SKILL.md)."""
    skills = []

    if not directory.exists():
        logger.warning(f"Directory does not exist: {directory}")
        return skills

    for item in directory.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            skill_data = parse_skill_md(item)
            if skill_data:
                skills.append(skill_data)
                logger.debug(f"Found skill: {skill_data['id']}")

    return skills


def load_registry() -> Dict:
    """Load the current capability registry."""
    if REGISTRY_PATH.exists():
        with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    logger.warning("No registry found, starting fresh")
    return {"metadata": {}, "categories": {}, "skills": [], "coverage_matrix": {}, "gap_indicators": {}}


def save_registry(registry: Dict) -> None:
    """Save the capability registry."""
    with open(REGISTRY_PATH, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)
    logger.info(f"Registry saved to {REGISTRY_PATH}")


def compare_skills(disk_skills: List[Dict], registry_skills: List[Dict]) -> Tuple[List[Dict], List[Dict], List[str]]:
    """Compare disk skills with registry skills."""
    disk_ids = {s['id'] for s in disk_skills}
    registry_ids = {s['id'] for s in registry_skills}

    new_skills = [s for s in disk_skills if s['id'] not in registry_ids]
    missing_from_disk = [s['id'] for s in registry_skills if s['id'] not in disk_ids]
    existing = [s for s in disk_skills if s['id'] in registry_ids]

    return new_skills, existing, missing_from_disk


def detect_discrepancies(disk_skills: List[Dict], registry_skills: List[Dict]) -> List[Dict]:
    """
    Detect discrepancies between disk skills and registry skills.
    Returns a list of discrepancy records with details of what changed.
    """
    discrepancies = []
    registry_by_id = {s['id']: s for s in registry_skills}

    # Fields to compare for discrepancies
    compare_fields = ['name', 'description', 'subcategory', 'has_scripts', 'complexity']

    for disk_skill in disk_skills:
        skill_id = disk_skill['id']
        if skill_id not in registry_by_id:
            continue  # New skill, not a discrepancy

        registry_skill = registry_by_id[skill_id]
        changes = []

        for field in compare_fields:
            disk_value = disk_skill.get(field)
            registry_value = registry_skill.get(field)

            # For strings, compare ignoring minor whitespace
            if isinstance(disk_value, str) and isinstance(registry_value, str):
                if disk_value.strip()[:100] != registry_value.strip()[:100]:
                    changes.append({
                        'field': field,
                        'disk_value': disk_value[:100] if len(str(disk_value)) > 100 else disk_value,
                        'registry_value': registry_value[:100] if len(str(registry_value)) > 100 else registry_value
                    })
            elif disk_value != registry_value:
                changes.append({
                    'field': field,
                    'disk_value': disk_value,
                    'registry_value': registry_value
                })

        # Check for new scripts
        disk_scripts = set(disk_skill.get('scripts', []))
        registry_scripts = set(registry_skill.get('scripts', []))
        if disk_scripts != registry_scripts:
            new_scripts = disk_scripts - registry_scripts
            removed_scripts = registry_scripts - disk_scripts
            if new_scripts:
                changes.append({
                    'field': 'scripts (added)',
                    'disk_value': list(new_scripts),
                    'registry_value': None
                })
            if removed_scripts:
                changes.append({
                    'field': 'scripts (removed)',
                    'disk_value': None,
                    'registry_value': list(removed_scripts)
                })

        if changes:
            discrepancies.append({
                'id': skill_id,
                'changes': changes
            })

    return discrepancies


def generate_report(
    new_skills: List[Dict],
    existing: List[Dict],
    missing: List[str],
    discrepancies: List[Dict],
    dry_run: bool = True
) -> str:
    """Generate a detailed sync report."""
    REPORTS_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_path = REPORTS_DIR / f"sync_report_{timestamp}.md"

    lines = [
        "# Skill Sync Report",
        f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Mode:** {'DRY RUN' if dry_run else 'UPDATE MODE'}",
        f"**Log file:** {LOG_FILE}",
        "",
        "---",
        "",
        "## Summary",
        "",
        f"| Metric | Count |",
        f"|--------|-------|",
        f"| Skills on disk | {len(new_skills) + len(existing)} |",
        f"| New skills (not in registry) | {len(new_skills)} |",
        f"| Existing skills (matched) | {len(existing)} |",
        f"| Missing from disk | {len(missing)} |",
        f"| Skills with discrepancies | {len(discrepancies)} |",
        "",
    ]

    if new_skills:
        lines.extend([
            "---",
            "",
            "## New Skills (To Be Added)",
            "",
        ])
        for s in new_skills:
            lines.extend([
                f"### {s['id']}",
                f"- **Name:** {s['name']}",
                f"- **Category:** {s['category']}",
                f"- **Subcategory:** {s['subcategory']}",
                f"- **Description:** {s['description'][:150]}...",
                f"- **Has scripts:** {s['has_scripts']}",
                f"- **Complexity:** {s['complexity']}",
                "",
            ])

    if missing:
        lines.extend([
            "---",
            "",
            "## Missing From Disk (In Registry Only)",
            "",
            "These skills exist in the registry but no SKILL.md was found on disk:",
            "",
        ])
        for sid in missing:
            lines.append(f"- ⚠️ `{sid}`")
        lines.append("")

    if discrepancies:
        lines.extend([
            "---",
            "",
            "## Discrepancies Detected",
            "",
            "These skills exist in both but have differences:",
            "",
        ])
        for disc in discrepancies:
            lines.append(f"### {disc['id']}")
            lines.append("")
            lines.append("| Field | Disk Value | Registry Value |")
            lines.append("|-------|------------|----------------|")
            for change in disc['changes']:
                disk_val = str(change['disk_value'])[:50] if change['disk_value'] else "(none)"
                reg_val = str(change['registry_value'])[:50] if change['registry_value'] else "(none)"
                lines.append(f"| {change['field']} | {disk_val} | {reg_val} |")
            lines.append("")

    lines.extend([
        "---",
        "",
        "## Actions",
        "",
    ])

    if dry_run:
        lines.extend([
            "This was a **dry run**. No changes were made.",
            "",
            "To apply changes, run:",
            "```bash",
            "python sync_skills.py --update",
            "```",
        ])
    else:
        lines.extend([
            f"- ✅ Added {len(new_skills)} new skills to registry",
            f"- ℹ️ {len(discrepancies)} discrepancies were logged but not auto-fixed",
            "- ⚠️ {len(missing)} skills in registry have no disk presence",
        ])

    report_content = '\n'.join(lines)
    report_path.write_text(report_content)
    logger.info(f"Report saved to {report_path}")

    return str(report_path)


def merge_skill_updates(existing_skill: Dict, disk_skill: Dict) -> Dict:
    """Merge disk skill data into existing registry skill, preserving usage stats."""
    # Start with disk data
    merged = disk_skill.copy()

    # Preserve usage statistics from registry
    merged['usage_count'] = existing_skill.get('usage_count', 0)
    merged['last_used'] = existing_skill.get('last_used')

    # Preserve auto_discovered flag if it was False (manually added)
    if not existing_skill.get('auto_discovered', True):
        merged['auto_discovered'] = False

    # Update discovered_at only if it's a new discovery
    if 'discovered_at' in existing_skill:
        merged['discovered_at'] = existing_skill['discovered_at']

    return merged


def main():
    parser = argparse.ArgumentParser(
        description="Sync skills from disk to capability registry",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python sync_skills.py                         # Dry-run: show what would change
  python sync_skills.py --update                # Actually update the registry
  python sync_skills.py --verbose               # Show detailed output
  python sync_skills.py --report                # Generate detailed report file
  python sync_skills.py --check-discrepancies   # Show changes in existing skills
  python sync_skills.py --update --sync-changes # Update registry AND apply discrepancy fixes
        """
    )
    parser.add_argument('--update', action='store_true',
                        help="Actually update the registry (add new skills)")
    parser.add_argument('--verbose', '-v', action='store_true',
                        help="Verbose output with debug logging")
    parser.add_argument('--report', action='store_true',
                        help="Generate a detailed markdown report")
    parser.add_argument('--check-discrepancies', action='store_true',
                        help="Check for discrepancies in existing skills")
    parser.add_argument('--sync-changes', action='store_true',
                        help="Also sync discrepancy changes (requires --update)")
    parser.add_argument('--dry-run', action='store_true',
                        help="Explicit dry-run mode (default behavior)")
    args = parser.parse_args()

    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    logger.info("=" * 60)
    logger.info("SKILL SYNC - Automatic Skill Discovery")
    logger.info("=" * 60)
    logger.info(f"Log file: {LOG_FILE}")

    # Scan directories
    logger.info("\n📂 Scanning cardiology skills...")
    cardiology_skills = scan_skills_directory(CARDIOLOGY_DIR)
    logger.info(f"   Found: {len(cardiology_skills)} skills")

    logger.info("\n📂 Scanning scientific skills...")
    scientific_skills = scan_skills_directory(SCIENTIFIC_DIR)
    logger.info(f"   Found: {len(scientific_skills)} skills")

    all_disk_skills = cardiology_skills + scientific_skills
    logger.info(f"\n📊 Total skills on disk: {len(all_disk_skills)}")

    # Load registry
    logger.info("\n📋 Loading capability registry...")
    registry = load_registry()
    registry_skills = registry.get('skills', [])
    logger.info(f"   Registry has: {len(registry_skills)} skills")

    # Compare
    new_skills, existing, missing = compare_skills(all_disk_skills, registry_skills)

    # Check for discrepancies if requested or in verbose mode
    discrepancies = []
    if args.check_discrepancies or args.verbose or args.report:
        logger.info("\n🔍 Checking for discrepancies...")
        discrepancies = detect_discrepancies(all_disk_skills, registry_skills)
        logger.info(f"   Found {len(discrepancies)} skills with discrepancies")

    print("\n" + "=" * 60)
    print("COMPARISON RESULTS")
    print("=" * 60)

    print(f"\n✅ Skills in registry and on disk: {len(existing)}")
    print(f"🆕 NEW skills (on disk, not in registry): {len(new_skills)}")
    print(f"⚠️  MISSING from disk (in registry only): {len(missing)}")
    if discrepancies:
        print(f"🔄 Skills with discrepancies: {len(discrepancies)}")

    if args.verbose or new_skills:
        print("\n--- NEW SKILLS ---")
        for s in new_skills:
            print(f"  + {s['id']} ({s['category']}) - {s['subcategory']}")
            if args.verbose:
                print(f"    Description: {s['description'][:80]}...")
                if s.get('scripts'):
                    print(f"    Scripts: {', '.join(s['scripts'])}")

    if args.verbose and missing:
        print("\n--- MISSING FROM DISK ---")
        for sid in missing:
            print(f"  - {sid}")

    if args.check_discrepancies and discrepancies:
        print("\n--- DISCREPANCIES ---")
        for disc in discrepancies:
            print(f"\n  📝 {disc['id']}:")
            for change in disc['changes']:
                print(f"     • {change['field']}: {change['registry_value']} → {change['disk_value']}")

    # Generate report if requested
    if args.report:
        is_dry_run = not args.update
        report_path = generate_report(new_skills, existing, missing, discrepancies, dry_run=is_dry_run)
        print(f"\n📄 Report saved: {report_path}")

    # Update if requested
    if args.update:
        print("\n" + "=" * 60)
        print("UPDATING REGISTRY")
        print("=" * 60)

        changes_made = 0

        # Add new skills
        for skill in new_skills:
            registry['skills'].append(skill)
            logger.info(f"Added new skill: {skill['id']}")
            print(f"  ✅ Added: {skill['id']}")
            changes_made += 1

        # Sync discrepancy changes if requested
        if args.sync_changes and discrepancies:
            registry_by_id = {s['id']: s for s in registry['skills']}
            disk_by_id = {s['id']: s for s in all_disk_skills}

            for disc in discrepancies:
                skill_id = disc['id']
                if skill_id in registry_by_id and skill_id in disk_by_id:
                    # Find the skill in the registry list and update it
                    for i, s in enumerate(registry['skills']):
                        if s['id'] == skill_id:
                            registry['skills'][i] = merge_skill_updates(s, disk_by_id[skill_id])
                            logger.info(f"Updated skill with discrepancies: {skill_id}")
                            print(f"  🔄 Updated: {skill_id}")
                            changes_made += 1
                            break

        if changes_made > 0:
            # Update metadata
            registry['metadata']['last_sync'] = datetime.now().strftime('%Y-%m-%d')
            registry['metadata']['total_skills'] = len(registry['skills'])
            registry['metadata']['cardiology_skills'] = len(
                [s for s in registry['skills'] if s.get('category') == 'cardiology']
            )
            registry['metadata']['scientific_skills'] = len(
                [s for s in registry['skills'] if s.get('category') == 'scientific']
            )
            registry['metadata']['auto_sync_enabled'] = True

            # Save
            save_registry(registry)
            print(f"\n💾 Registry saved with {len(registry['skills'])} skills")
            print(f"   Changes made: {changes_made}")
        else:
            print("\n✨ No changes needed - registry is up to date!")

    elif new_skills or discrepancies:
        print("\n💡 This was a DRY RUN. No changes made.")
        if new_skills:
            print(f"   Run with --update to add {len(new_skills)} new skills")
        if discrepancies:
            print(f"   Run with --update --sync-changes to apply {len(discrepancies)} discrepancy fixes")

    print(f"\n📝 Log saved: {LOG_FILE}")
    print("✨ Sync complete!")
    return 0


if __name__ == "__main__":
    exit(main())
