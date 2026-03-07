#!/usr/bin/env python3
"""
generate_context.py - Generate skill sections for context files from capability-registry.json

Reads capability-registry.json as the source of truth and updates skill inventory
sections in CLAUDE.md, GEMINI.md, AGENTS.md, and SKILL-CATALOG.md while preserving
all other content.

Usage:
    python generate_context.py                    # Preview what would change
    python generate_context.py --update           # Actually update context files
    python generate_context.py --file CLAUDE.md   # Update specific file only
    python generate_context.py --preview          # Show generated content
    python generate_context.py --verbose          # Show detailed output
"""

import json
import re
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from collections import defaultdict

# Paths
SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR.parent / "data"
REGISTRY_PATH = DATA_DIR / "capability-registry.json"
# Project root - resolve relative to this script's location
# scripts/ -> system-awareness/ -> cardiology/ -> skills/ -> project_root/
PROJECT_ROOT = SCRIPT_DIR.parent.parent.parent.parent

# Context files to update
CONTEXT_FILES = {
    "CLAUDE.md": PROJECT_ROOT / "CLAUDE.md",
    "GEMINI.md": PROJECT_ROOT / "GEMINI.md",
    "AGENTS.md": PROJECT_ROOT / "AGENTS.md",
    "SKILL-CATALOG.md": PROJECT_ROOT / "SKILL-CATALOG.md"
}

# Section detection patterns for each file
# These are the sections we'll replace while preserving everything else
SECTION_PATTERNS = {
    "CLAUDE.md": {
        "start": r"^## COMPLETE SKILLS INVENTORY.*$",
        "end": r"^---\s*\n\n## PIPELINES",  # Section ends before PIPELINES
        "marker_type": "skills_inventory"
    },
    "GEMINI.md": {
        "start": r"^## COMPLETE SKILLS INVENTORY.*$",
        "end": r"^---\s*\n\n## ",  # Section ends at next major section with ---
        "marker_type": "skills_inventory"
    },
    "AGENTS.md": {
        "start": r"^## USING SKILLS$",  # Uses a different section name
        "end": r"^---\s*\n\n## VOICE STANDARDS",  # Ends before VOICE STANDARDS
        "marker_type": "using_skills"
    },
    "SKILL-CATALOG.md": {
        "start": None,  # Full file replacement
        "end": None,
        "marker_type": "full_replace"
    }
}

# Purpose-based routing categories for SKILL-CATALOG.md
PURPOSE_ROUTING = {
    "write_youtube": {
        "label": "Write YouTube Scripts",
        "keywords": ["youtube", "script", "hinglish", "video", "hook"],
        "skills": []
    },
    "write_twitter": {
        "label": "Write Twitter/X Content",
        "keywords": ["tweet", "twitter", "x-post", "thread"],
        "skills": []
    },
    "write_newsletter": {
        "label": "Write Newsletters",
        "keywords": ["newsletter", "email", "digest"],
        "skills": []
    },
    "write_editorial": {
        "label": "Write Editorials/Long-form",
        "keywords": ["editorial", "topol", "chapter", "long-form", "academic"],
        "skills": []
    },
    "research_pubmed": {
        "label": "Research PubMed/Literature",
        "keywords": ["pubmed", "literature", "research", "papers", "citation"],
        "skills": []
    },
    "research_trends": {
        "label": "Find Trends/Viral Topics",
        "keywords": ["trend", "viral", "social listening", "competitor"],
        "skills": []
    },
    "create_visuals": {
        "label": "Create Images/Visuals",
        "keywords": ["image", "visual", "infographic", "carousel", "chart"],
        "skills": []
    },
    "optimize_quality": {
        "label": "Improve Quality/Voice",
        "keywords": ["voice", "authentic", "quality", "review", "reflection"],
        "skills": []
    },
    "analyze_data": {
        "label": "Analyze Data/Score Content",
        "keywords": ["score", "analyze", "predict", "ensemble", "seo"],
        "skills": []
    }
}

# Curated groupings for better presentation (used in CLAUDE.md style)
CURATED_GROUPS = {
    "cardiology": {
        "YouTube & Hinglish Content": {
            "skills": ["youtube-script-master", "youtube-script-hinglish", "debunk-script-writer",
                       "hook-generator", "cardiology-youtube-scriptwriter"],
            "priority": 1
        },
        "Twitter/X & Social Media": {
            "skills": ["x-post-creator-skill", "cardiology-tweet-writer", "cremieux-cardio",
                       "twitter-longform-medical", "cardiology-content-repurposer"],
            "priority": 2
        },
        "Newsletters & Editorials": {
            "skills": ["cardiology-newsletter-writer", "medical-newsletter-writer",
                       "cardiology-editorial", "cardiology-trial-editorial",
                       "cardiology-topol-writer", "academic-chapter-writer",
                       "cardiology-science-for-people", "cardiology-writer"],
            "priority": 3
        },
        "Research & Discovery": {
            "skills": ["social-media-trends-research", "viral-content-predictor",
                       "content-trend-researcher", "content-marketing-social-listening",
                       "perplexity-search", "deep-researcher", "content-research-writer",
                       "knowledge-pipeline", "pubmed-database", "clinicaltrials-database",
                       "literature-review", "research-synthesizer", "citation-management"],
            "priority": 4
        },
        "Research Amplification": {
            "skills": ["quick-topic-researcher", "parallel-literature-search",
                       "influencer-analyzer", "content-seo-optimizer",
                       "video-delivery-coach", "ensemble-content-scorer",
                       "research-paper-extractor"],
            "priority": 5
        },
        "Quality & Voice": {
            "skills": ["authentic-voice", "content-reflection", "scientific-critical-thinking"],
            "priority": 6
        },
        "Visual Content": {
            "skills": ["cardiology-visual-system", "gemini-imagegen", "carousel-generator",
                       "carousel-generator-v2"],
            "priority": 7
        },
        "Multi-Model & Utilities": {
            "skills": ["multi-model-writer", "browser-automation", "article-extractor",
                       "mcp-management", "content-os", "system-awareness"],
            "priority": 8
        }
    },
    "scientific": {
        "Databases": {
            "keywords": ["database", "-db", "alphafold", "biorxiv", "chembl",
                        "clinvar", "cosmic", "drugbank", "ensembl", "gnomad",
                        "gwas", "kegg", "pdb", "pubmed", "reactome", "string", "uniprot"],
            "priority": 1
        },
        "Bioinformatics": {
            "keywords": ["biopython", "scanpy", "anndata", "cellxgene", "deepchem",
                        "genomics", "mafft", "nextflow", "samtools", "scvi"],
            "priority": 2
        },
        "Data Science": {
            "keywords": ["dask", "pandas", "plotly", "polars", "pytorch",
                        "scikit", "scipy", "seaborn", "statsmodels", "shap"],
            "priority": 3
        }
    }
}


def load_registry() -> Dict:
    """Load the capability registry."""
    with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_skill_description(skill: Dict, max_len: int = 80) -> str:
    """Get skill description, truncated if needed."""
    desc = skill.get('description', '')
    # Clean up common markdown
    desc = re.sub(r'^#+\s*', '', desc)
    desc = re.sub(r'\*\*([^*]+)\*\*', r'\1', desc)
    desc = re.sub(r'\n.*', '', desc)  # Just first line
    desc = desc.strip()

    if len(desc) > max_len:
        desc = desc[:max_len-3] + "..."
    return desc


def categorize_skill_for_purpose(skill: Dict) -> List[str]:
    """Determine which purpose categories a skill belongs to."""
    purposes = []
    skill_text = f"{skill['id']} {skill.get('description', '')} {' '.join(skill.get('use_cases', []))}".lower()

    for purpose_id, purpose_info in PURPOSE_ROUTING.items():
        if any(kw in skill_text for kw in purpose_info['keywords']):
            purposes.append(purpose_id)

    return purposes if purposes else ['general']


def group_skills_by_curated(skills: List[Dict], category: str) -> Dict[str, List[Dict]]:
    """Group skills according to curated groupings."""
    groups = defaultdict(list)
    grouped_ids = set()

    category_groups = CURATED_GROUPS.get(category, {})

    # First, try to place skills in curated groups
    for group_name, group_info in category_groups.items():
        if 'skills' in group_info:
            # Explicit skill list
            for skill in skills:
                if skill['id'] in group_info['skills']:
                    groups[group_name].append(skill)
                    grouped_ids.add(skill['id'])
        elif 'keywords' in group_info:
            # Keyword-based grouping
            for skill in skills:
                skill_text = f"{skill['id']} {skill.get('description', '')}".lower()
                if any(kw in skill_text for kw in group_info['keywords']):
                    if skill['id'] not in grouped_ids:
                        groups[group_name].append(skill)
                        grouped_ids.add(skill['id'])

    # Put remaining skills in "Other" group
    for skill in skills:
        if skill['id'] not in grouped_ids:
            # Try to infer from subcategory
            subcat = skill.get('subcategory', 'general')
            if '/' in subcat:
                subcat = subcat.split('/')[0]
            group_name = subcat.replace('-', ' ').title()
            if group_name not in groups:
                group_name = "Other"
            groups[group_name].append(skill)

    return groups


def generate_curated_skills_section(skills: List[Dict], category: str, style: str = "full") -> str:
    """Generate skills section with curated groupings."""
    filtered = [s for s in skills if s.get('category') == category]
    groups = group_skills_by_curated(filtered, category)

    # Get priority order
    category_groups = CURATED_GROUPS.get(category, {})
    def get_priority(group_name):
        if group_name in category_groups:
            return category_groups[group_name].get('priority', 99)
        return 100

    sorted_groups = sorted(groups.items(), key=lambda x: get_priority(x[0]))

    lines = []
    for group_name, group_skills in sorted_groups:
        if not group_skills:
            continue

        lines.append(f"\n#### {group_name}")
        lines.append("| Skill | Purpose |")
        lines.append("|-------|---------|")

        for skill in sorted(group_skills, key=lambda x: x['id']):
            desc = get_skill_description(skill, 60 if style == "compact" else 80)
            lines.append(f"| `{skill['id']}` | {desc} |")

    return "\n".join(lines)


def generate_scientific_summary(skills: List[Dict]) -> str:
    """Generate compact summary for scientific skills."""
    filtered = [s for s in skills if s.get('category') == 'scientific']

    # Group by subcategory keywords
    databases = []
    bioinformatics = []
    data_science = []
    other = []

    for skill in filtered:
        skill_text = f"{skill['id']} {skill.get('subcategory', '')}".lower()
        if 'database' in skill_text or skill['id'].endswith('-database'):
            databases.append(skill['id'])
        elif any(kw in skill_text for kw in ['bio', 'genomics', 'scvi', 'scanpy', 'anndata']):
            bioinformatics.append(skill['id'])
        elif any(kw in skill_text for kw in ['dask', 'pandas', 'plotly', 'torch', 'scikit', 'stats']):
            data_science.append(skill['id'])
        else:
            other.append(skill['id'])

    lines = [
        f"Located in `skills/scientific/`",
        "",
        f"**Databases:** {', '.join(sorted(databases)[:16])}",
        "",
        f"**Bioinformatics:** {', '.join(sorted(bioinformatics)[:9])}",
        "",
        f"**Data Science:** {', '.join(sorted(data_science)[:9])}"
    ]

    return "\n".join(lines)


def generate_skills_inventory_claude(skills: List[Dict]) -> str:
    """Generate skills inventory section for CLAUDE.md."""
    cardiology = [s for s in skills if s.get('category') == 'cardiology']
    scientific = [s for s in skills if s.get('category') == 'scientific']

    lines = [
        f"## COMPLETE SKILLS INVENTORY ({len(skills)}+ Skills)",
        "",
        f"### Cardiology Skills ({len(cardiology)} Skills)",
        ""
    ]

    lines.append(generate_curated_skills_section(skills, 'cardiology', 'full'))

    lines.extend([
        "",
        f"### Scientific Skills ({len(scientific)} Skills)",
        generate_scientific_summary(skills),
        ""
    ])

    return "\n".join(lines)


def generate_skills_inventory_gemini(skills: List[Dict]) -> str:
    """Generate skills inventory section for GEMINI.md."""
    cardiology = [s for s in skills if s.get('category') == 'cardiology']
    scientific = [s for s in skills if s.get('category') == 'scientific']

    lines = [
        f"## COMPLETE SKILLS INVENTORY ({len(skills)}+ Skills)",
        "",
        f"### Cardiology Skills ({len(cardiology)} Skills)",
        "**Location:** `skills/cardiology/`",
        ""
    ]

    # Slightly more compact for Gemini
    lines.append(generate_curated_skills_section(skills, 'cardiology', 'compact'))

    lines.extend([
        "",
        f"### Scientific Skills ({len(scientific)} Skills)",
        "**Location:** `skills/scientific/`",
        "",
        generate_scientific_summary(skills),
        ""
    ])

    return "\n".join(lines)


def generate_using_skills_agents(skills: List[Dict]) -> str:
    """Generate USING SKILLS section for AGENTS.md."""
    cardiology = [s for s in skills if s.get('category') == 'cardiology']

    lines = [
        "## USING SKILLS",
        "",
        "### Invoke Skills with $",
        "You can invoke skills by mentioning them:",
        "- `$youtube-script-master` - Generate YouTube script",
        "- `$cardiology-tweet-writer` - Write tweets",
        "- `$viral-content-predictor` - Analyze content ideas",
        "",
        "### Skill Locations",
        "All skills are in `skills/cardiology/` with this structure:",
        "```",
        "skills/cardiology/",
        "├── youtube-script-master/",
        "│   ├── SKILL.md           # Read this for instructions",
        "│   ├── references/        # Voice guides, examples",
        "│   └── scripts/           # Executable helpers",
        "├── x-post-creator-skill/",
        "├── cardiology-newsletter-writer/",
        f"└── ... ({len(cardiology)} total skills)",
        "```",
        "",
        "### Key Skills for You",
        "| Skill | Best For |",
        "|-------|----------|",
        "| `cardiology-trial-editorial` | Analyzing clinical trials |",
        "| `x-post-creator-skill` | Batch tweet generation |",
        "| `viral-content-predictor` | Scoring content ideas |",
        "| `knowledge-pipeline` | RAG + PubMed synthesis |",
        "| `perplexity-search` | Web research |",
        ""
    ]

    return "\n".join(lines)


def generate_skill_catalog(skills: List[Dict]) -> str:
    """Generate complete SKILL-CATALOG.md with purpose-based routing."""
    lines = [
        "# Skill Catalog - Purpose-Based Lookup",
        "",
        "> **Quick Reference:** Find the right skill for your task",
        "",
        f"_Auto-generated from capability-registry.json on {datetime.now().strftime('%Y-%m-%d')}_",
        "",
        "---",
        "",
        "## How to Use This Catalog",
        "",
        "**By Purpose:** \"I want to write tweets\" → Find in Twitter/X section",
        "**By Name:** Search for skill ID like `youtube-script-master`",
        "**By Category:** Browse Cardiology or Scientific sections",
        "",
        "---",
        "",
        "## Purpose-Based Quick Routing",
        "",
        "| I want to... | Use this skill |",
        "|--------------|----------------|",
    ]

    # Build purpose routing table
    purpose_map = defaultdict(list)
    for skill in skills:
        purposes = categorize_skill_for_purpose(skill)
        for purpose in purposes:
            if purpose != 'general':
                purpose_map[purpose].append(skill['id'])

    routing_examples = {
        "write_youtube": ("Write YouTube scripts", "youtube-script-master"),
        "write_twitter": ("Create Twitter content", "x-post-creator-skill"),
        "write_newsletter": ("Write newsletters", "cardiology-newsletter-writer"),
        "write_editorial": ("Write editorials/long-form", "cardiology-editorial"),
        "research_pubmed": ("Research literature", "knowledge-pipeline, pubmed-database"),
        "research_trends": ("Find trending topics", "social-media-trends-research"),
        "create_visuals": ("Generate images/carousels", "cardiology-visual-system"),
        "optimize_quality": ("Improve voice/quality", "authentic-voice"),
        "analyze_data": ("Score/analyze content", "ensemble-content-scorer")
    }

    for purpose_id, (label, skill_example) in routing_examples.items():
        lines.append(f"| {label} | `{skill_example}` |")

    lines.extend([
        "",
        "---",
        "",
        "## Cardiology Skills",
        ""
    ])

    # Add cardiology skills by subcategory
    lines.append(generate_curated_skills_section(skills, 'cardiology', 'full'))

    lines.extend([
        "",
        "---",
        "",
        "## Scientific Skills",
        ""
    ])

    # Add scientific skills by subcategory
    scientific = [s for s in skills if s.get('category') == 'scientific']

    # Group by subcategory
    by_subcat = defaultdict(list)
    for skill in scientific:
        subcat = skill.get('subcategory', 'general')
        if '/' in subcat:
            subcat = subcat.split('/')[-1]
        subcat = subcat.replace('-', ' ').title()
        by_subcat[subcat].append(skill)

    for subcat, subcat_skills in sorted(by_subcat.items()):
        lines.append(f"\n#### {subcat}")
        lines.append("| Skill | Purpose |")
        lines.append("|-------|---------|")
        for skill in sorted(subcat_skills, key=lambda x: x['id']):
            desc = get_skill_description(skill, 60)
            lines.append(f"| `{skill['id']}` | {desc} |")

    return "\n".join(lines)


def find_section_bounds(content: str, file_type: str) -> Optional[Tuple[int, int]]:
    """Find the start and end positions of the section to replace."""
    pattern_info = SECTION_PATTERNS.get(file_type, {})

    if pattern_info.get('marker_type') == 'full_replace':
        return (0, len(content))

    start_pattern = pattern_info.get('start')
    end_pattern = pattern_info.get('end')

    if not start_pattern:
        return None

    # Find start
    start_match = re.search(start_pattern, content, re.MULTILINE)
    if not start_match:
        return None

    start_pos = start_match.start()

    # Find end
    if end_pattern:
        # Search for end pattern after start
        search_content = content[start_match.end():]
        end_match = re.search(end_pattern, search_content, re.MULTILINE | re.DOTALL)
        if end_match:
            end_pos = start_match.end() + end_match.start()
        else:
            # If no end pattern found, go to end of file
            end_pos = len(content)
    else:
        end_pos = len(content)

    return (start_pos, end_pos)


def update_context_file(file_path: Path, file_type: str, skills: List[Dict], verbose: bool = False) -> Tuple[bool, str]:
    """Update a context file with new skills section."""
    if not file_path.exists():
        return False, f"File does not exist: {file_path}"

    content = file_path.read_text(encoding='utf-8')

    # Generate new section
    if file_type == "SKILL-CATALOG.md":
        new_section = generate_skill_catalog(skills)
        file_path.write_text(new_section, encoding='utf-8')
        return True, "Full file regenerated"

    elif file_type == "CLAUDE.md":
        new_section = generate_skills_inventory_claude(skills)

    elif file_type == "GEMINI.md":
        new_section = generate_skills_inventory_gemini(skills)

    elif file_type == "AGENTS.md":
        new_section = generate_using_skills_agents(skills)

    else:
        return False, f"Unknown file type: {file_type}"

    # Find section bounds
    bounds = find_section_bounds(content, file_type)

    if bounds is None:
        return False, f"Could not find section markers for {file_type}"

    start_pos, end_pos = bounds

    # Build new content
    before = content[:start_pos]
    after = content[end_pos:]

    # Ensure proper spacing
    if not before.endswith('\n\n'):
        if before.endswith('\n'):
            before = before + '\n'
        else:
            before = before + '\n\n'

    if not after.startswith('\n'):
        after = '\n' + after

    new_content = before + new_section + after

    if verbose:
        print(f"  Section bounds: {start_pos} - {end_pos}")
        print(f"  New section length: {len(new_section)}")

    file_path.write_text(new_content, encoding='utf-8')
    return True, "Section updated"


def main():
    parser = argparse.ArgumentParser(
        description="Generate skills sections for context files from capability-registry.json",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_context.py                    # Preview what would change
  python generate_context.py --update           # Actually update context files
  python generate_context.py --file CLAUDE.md   # Update specific file only
  python generate_context.py --preview          # Show generated content
  python generate_context.py --verbose          # Show detailed output
        """
    )
    parser.add_argument('--update', action='store_true', help="Actually update the files")
    parser.add_argument('--file', type=str, help="Update specific file only")
    parser.add_argument('--preview', type=str, nargs='?', const='CLAUDE.md',
                       help="Preview generated content for a file (default: CLAUDE.md)")
    parser.add_argument('--verbose', '-v', action='store_true', help="Verbose output")
    args = parser.parse_args()

    print("=" * 60)
    print("GENERATE CONTEXT - Building skills sections from registry")
    print("=" * 60)

    # Load registry
    print("\n📋 Loading capability registry...")
    try:
        registry = load_registry()
    except FileNotFoundError:
        print(f"  ❌ Registry not found at {REGISTRY_PATH}")
        print("     Run sync_skills.py first to build the registry")
        return 1

    skills = registry.get('skills', [])
    metadata = registry.get('metadata', {})

    print(f"   Registry version: {metadata.get('version', 'unknown')}")
    print(f"   Last sync: {metadata.get('last_sync', 'unknown')}")
    print(f"   Total skills: {len(skills)}")

    cardiology_count = len([s for s in skills if s.get('category') == 'cardiology'])
    scientific_count = len([s for s in skills if s.get('category') == 'scientific'])
    print(f"   Cardiology: {cardiology_count}, Scientific: {scientific_count}")

    # Preview mode
    if args.preview:
        preview_file = args.preview
        print(f"\n📝 Generating preview for {preview_file}...")
        print("\n" + "=" * 40)
        print("PREVIEW:")
        print("=" * 40 + "\n")

        if preview_file == "SKILL-CATALOG.md":
            print(generate_skill_catalog(skills))
        elif preview_file == "CLAUDE.md":
            print(generate_skills_inventory_claude(skills))
        elif preview_file == "GEMINI.md":
            print(generate_skills_inventory_gemini(skills))
        elif preview_file == "AGENTS.md":
            print(generate_using_skills_agents(skills))
        else:
            print(f"Unknown file type: {preview_file}")
            return 1

        return 0

    # Update mode
    if args.update:
        print("\n📂 Updating context files...")

        files_to_update = CONTEXT_FILES
        if args.file:
            if args.file in CONTEXT_FILES:
                files_to_update = {args.file: CONTEXT_FILES[args.file]}
            else:
                print(f"  ❌ Unknown file: {args.file}")
                print(f"  Available: {', '.join(CONTEXT_FILES.keys())}")
                return 1

        results = []
        for name, path in files_to_update.items():
            success, message = update_context_file(path, name, skills, verbose=args.verbose)
            results.append((name, success, message))

            if success:
                print(f"  ✅ {name}: {message}")
            else:
                print(f"  ⚠️ {name}: {message}")

        successful = sum(1 for _, s, _ in results if s)
        print(f"\n💾 Updated {successful}/{len(results)} files")

    else:
        # Dry run - just show what would happen
        print("\n📝 Checking context files (dry run)...")

        for name, path in CONTEXT_FILES.items():
            if not path.exists():
                print(f"  ⚠️ {name}: File does not exist")
                continue

            content = path.read_text(encoding='utf-8')
            bounds = find_section_bounds(content, name)

            if bounds:
                start, end = bounds
                section_len = end - start
                print(f"  📄 {name}: Section found ({section_len} chars at pos {start}-{end})")
            elif name == "SKILL-CATALOG.md":
                print(f"  📄 {name}: Full file replacement")
            else:
                print(f"  ⚠️ {name}: No section markers found")

        print("\n💡 Run with --update to modify files")
        print("   Run with --preview [FILE] to see generated content")

    print("\n✨ Complete!")
    return 0


if __name__ == "__main__":
    exit(main())
