#!/usr/bin/env python3
"""
AaaS Skill Vault — Clean & Score Pipeline
==========================================
Strips copyright/attribution from skills, scores quality,
and rebuilds SKILLS_MANIFEST.json with publish-ready metadata.

Usage:
    python scripts/clean_and_score.py              # Dry run (report only)
    python scripts/clean_and_score.py --apply      # Apply changes
    python scripts/clean_and_score.py --apply --min-score 6.0  # Custom threshold
"""

import os
import re
import json
import argparse
import hashlib
from pathlib import Path
from datetime import datetime, timezone

# ─── Config ──────────────────────────────────────────────────────────────────

SKILLS_ROOT = Path(__file__).parent.parent / "skills"
MANIFEST_PATH = Path(__file__).parent.parent / "SKILLS_MANIFEST.json"

# Patterns to strip from SKILL.md frontmatter and content
STRIP_PATTERNS = {
    "name_prefix": re.compile(r'^(jack-\w+-)', re.IGNORECASE),
    "source_line": re.compile(r'^source:\s*["\']?.*?["\']?\s*$', re.MULTILINE),
    "license_line": re.compile(r'^license:\s*["\']?.*?["\']?\s*$', re.MULTILINE),
    "author_line": re.compile(r'^author:\s*["\']?.*?["\']?\s*$', re.MULTILINE),
    "credit_line": re.compile(r'^credit:\s*["\']?.*?["\']?\s*$', re.MULTILINE),
    "copyright_line": re.compile(r'^copyright:\s*["\']?.*?["\']?\s*$', re.MULTILINE),
    "attribution_line": re.compile(r'^attribution:\s*["\']?.*?["\']?\s*$', re.MULTILINE),
}

# Words that indicate copyright concerns in file content
COPYRIGHT_MARKERS = [
    "©", "all rights reserved", "proprietary", "do not distribute",
    "confidential", "trade secret", "patent pending",
]

# Quality scoring weights
QUALITY_WEIGHTS = {
    "has_skill_md": 2.0,        # Has a SKILL.md file
    "has_description": 1.5,     # Has a description in frontmatter
    "has_instructions": 2.0,    # Has actionable instructions (>100 chars of content)
    "has_examples": 1.0,        # Contains example blocks or code
    "has_references": 0.5,      # Has a references/ directory
    "content_depth": 2.0,       # Content length score (0-2 based on word count)
    "no_copyright_issues": 1.0, # Clean of copyright markers
}

MAX_SCORE = sum(QUALITY_WEIGHTS.values())

# Tier thresholds (percentage of max score)
# Aligned with GitHub README distribution:
#   Gold   = perfect score (all criteria met incl. references)
#   Silver = solid quality, well-structured skills
#   Bronze = basic quality, usable but minimal
TIER_THRESHOLDS = {
    "gold": 1.00,       # 100% of max — all quality criteria met
    "silver": 0.665,    # ≥ 66.5% of max — good quality
    "bronze": 0.45,     # ≥ 45% of max — basic quality
    "unrated": 0.0,     # Below 45%
}

# ─── Scoring Engine ──────────────────────────────────────────────────────────

def score_skill(skill_path: Path) -> dict:
    """Score a skill directory and return detailed quality metrics."""
    scores = {}
    issues = []

    skill_md = skill_path / "SKILL.md"
    content = ""
    frontmatter = ""

    if skill_md.is_file():
        scores["has_skill_md"] = QUALITY_WEIGHTS["has_skill_md"]
        raw = skill_md.read_text(errors="replace")

        # Split frontmatter from content
        fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', raw, re.DOTALL)
        if fm_match:
            frontmatter = fm_match.group(1)
            content = fm_match.group(2)
        else:
            content = raw

        # Check description
        if re.search(r'^description:', frontmatter, re.MULTILINE):
            scores["has_description"] = QUALITY_WEIGHTS["has_description"]
        else:
            scores["has_description"] = 0
            issues.append("Missing description in frontmatter")

        # Check instructions depth
        if len(content.strip()) > 100:
            scores["has_instructions"] = QUALITY_WEIGHTS["has_instructions"]
        else:
            scores["has_instructions"] = 0
            issues.append("Thin content (<100 chars)")

        # Check examples
        if re.search(r'```|<example|## Example|## Usage', content, re.IGNORECASE):
            scores["has_examples"] = QUALITY_WEIGHTS["has_examples"]
        else:
            scores["has_examples"] = 0

        # Content depth (word count)
        word_count = len(content.split())
        depth_ratio = min(word_count / 500, 1.0)  # Max at 500 words
        scores["content_depth"] = round(depth_ratio * QUALITY_WEIGHTS["content_depth"], 2)

        # Copyright check
        content_lower = content.lower() + frontmatter.lower()
        has_copyright = any(marker in content_lower for marker in COPYRIGHT_MARKERS)
        if has_copyright:
            scores["no_copyright_issues"] = 0
            issues.append("Contains copyright markers")
        else:
            scores["no_copyright_issues"] = QUALITY_WEIGHTS["no_copyright_issues"]
    else:
        scores["has_skill_md"] = 0
        issues.append("Missing SKILL.md")
        for key in QUALITY_WEIGHTS:
            if key not in scores:
                scores[key] = 0

    # Check references
    refs_dir = skill_path / "references"
    if refs_dir.is_dir() and any(refs_dir.iterdir()):
        scores["has_references"] = QUALITY_WEIGHTS["has_references"]
    else:
        scores["has_references"] = 0

    total = sum(scores.values())
    percentage = total / MAX_SCORE

    # Determine tier
    tier = "unrated"
    for t, threshold in sorted(TIER_THRESHOLDS.items(), key=lambda x: -x[1]):
        if percentage >= threshold:
            tier = t
            break

    # Determine context_enhanced eligibility
    # Requires: Gold tier + ≥2 code blocks + ≥500 words + references + clean copyright
    code_blocks = len(re.findall(r'```', content)) // 2  # Count paired code fences
    word_count = len(content.split())
    context_enhanced = (
        tier == "gold"
        and code_blocks >= 2
        and word_count >= 500
        and scores.get("has_references", 0) > 0
        and scores.get("no_copyright_issues", 0) > 0
    )

    return {
        "total_score": round(total, 2),
        "max_score": MAX_SCORE,
        "percentage": round(percentage * 100, 1),
        "tier": tier,
        "context_enhanced": context_enhanced,
        "breakdown": scores,
        "issues": issues,
    }


# ─── Copyright Stripper ─────────────────────────────────────────────────────

def strip_copyright(skill_path: Path, dry_run: bool = True) -> list:
    """Strip copyright/attribution from a skill. Returns list of changes made."""
    changes = []
    skill_md = skill_path / "SKILL.md"

    if not skill_md.is_file():
        return changes

    content = skill_md.read_text(errors="replace")
    original = content

    # Strip frontmatter attribution lines
    for pattern_name, pattern in STRIP_PATTERNS.items():
        if pattern_name == "name_prefix":
            # Handle name prefix separately — rename the name field value
            name_match = re.search(r'^name:\s*["\']?(jack-\w+-)(.*?)["\']?\s*$', content, re.MULTILINE)
            if name_match:
                old_name = name_match.group(0)
                clean_name = f'name: "{name_match.group(2).strip()}"'
                content = content.replace(old_name, clean_name)
                changes.append(f"Renamed: {old_name.strip()} → {clean_name}")
        else:
            matches = pattern.findall(content)
            if matches:
                content = pattern.sub('', content)
                # Clean up double newlines left behind
                content = re.sub(r'\n{3,}', '\n\n', content)
                changes.append(f"Removed {pattern_name}: {matches[0].strip()}")

    # Strip copyright markers from body
    for marker in COPYRIGHT_MARKERS:
        if marker.lower() in content.lower():
            # Remove lines containing the marker
            lines = content.split('\n')
            clean_lines = [l for l in lines if marker.lower() not in l.lower()]
            if len(clean_lines) != len(lines):
                content = '\n'.join(clean_lines)
                changes.append(f"Removed line(s) containing '{marker}'")

    if changes and not dry_run:
        skill_md.write_text(content)

    return changes


# ─── Manifest Builder ───────────────────────────────────────────────────────

def build_manifest(skills_root: Path, scores: dict) -> dict:
    """Build a fresh SKILLS_MANIFEST.json from the scored skills."""
    categories = {}
    tier_counts = {"gold": 0, "silver": 0, "bronze": 0, "unrated": 0}
    context_enhanced_count = 0

    for cat_dir in sorted(skills_root.iterdir()):
        if not cat_dir.is_dir() or cat_dir.name.startswith('.'):
            continue

        cat_name = cat_dir.name
        cat_skills = []

        for skill_dir in sorted(cat_dir.iterdir()):
            if not skill_dir.is_dir() or skill_dir.name.startswith('.'):
                continue

            skill_key = f"{cat_name}/{skill_dir.name}"
            score_info = scores.get(skill_key, {})
            tier = score_info.get("tier", "unrated")
            tier_counts[tier] = tier_counts.get(tier, 0) + 1

            # Read description from SKILL.md frontmatter
            skill_md = skill_dir / "SKILL.md"
            description = ""
            if skill_md.is_file():
                raw = skill_md.read_text(errors="replace")
                desc_match = re.search(r'^description:\s*["\']?(.*?)["\']?\s*$', raw, re.MULTILINE)
                if desc_match:
                    description = desc_match.group(1).strip()
                # Try multiline description
                if not description:
                    desc_match = re.search(r'description:\s*>\s*\n\s*(.*?)(?:\n\w|\n---)', raw, re.DOTALL)
                    if desc_match:
                        description = ' '.join(desc_match.group(1).split())

            is_context_enhanced = score_info.get("context_enhanced", False)
            if is_context_enhanced:
                context_enhanced_count += 1

            cat_skills.append({
                "id": skill_dir.name,
                "name": skill_dir.name.replace('-', ' ').title(),
                "description": description,
                "category": cat_name,
                "path": f"skills/{cat_name}/{skill_dir.name}",
                "quality_tier": tier,
                "quality_score": score_info.get("total_score", 0),
                "quality_percentage": score_info.get("percentage", 0),
                "tags": [],
                "source": "aaas-vault",
                "publishable": tier in ("gold", "silver"),
                "context_enhanced": is_context_enhanced,
            })

        if cat_skills:
            categories[cat_name] = {
                "description": cat_name.replace('-', ' ').title(),
                "skill_count": len(cat_skills),
                "skills": cat_skills,
            }

    total = sum(info["skill_count"] for info in categories.values())
    publishable = sum(
        1 for info in categories.values()
        for s in info["skills"]
        if s.get("publishable")
    )

    return {
        "version": "3.0.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_skills": total,
        "publishable_skills": publishable,
        "context_enhanced_count": context_enhanced_count,
        "quality_distribution": tier_counts,
        "categories": categories,
    }


# ─── Main Pipeline ──────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="AaaS Skill Vault — Clean & Score Pipeline")
    parser.add_argument("--apply", action="store_true", help="Apply changes (default is dry run)")
    parser.add_argument("--min-score", type=float, default=0.0, help="Minimum score to keep (0 = keep all)")
    parser.add_argument("--json-report", type=str, help="Write JSON report to file")
    args = parser.parse_args()

    # ANSI colors
    G, R, Y, B, W, RESET = '\033[92m', '\033[91m', '\033[93m', '\033[94m', '\033[97m', '\033[0m'

    print(f"\n{Y}{'='*60}{RESET}")
    print(f"{W}  AaaS Skill Vault — Clean & Score Pipeline{RESET}")
    print(f"{Y}{'='*60}{RESET}")
    print(f"  Mode: {'APPLY' if args.apply else 'DRY RUN (use --apply to commit changes)'}")
    print()

    if not SKILLS_ROOT.is_dir():
        print(f"{R}[FATAL] Skills directory not found: {SKILLS_ROOT}{RESET}")
        return

    # Phase 1: Score all skills
    print(f"{Y}── Phase 1: Scoring all skills ──{RESET}")
    all_scores = {}
    copyright_issues = []
    total_skills = 0

    for cat_dir in sorted(SKILLS_ROOT.iterdir()):
        if not cat_dir.is_dir() or cat_dir.name.startswith('.'):
            continue
        for skill_dir in sorted(cat_dir.iterdir()):
            if not skill_dir.is_dir() or skill_dir.name.startswith('.'):
                continue

            total_skills += 1
            key = f"{cat_dir.name}/{skill_dir.name}"
            score = score_skill(skill_dir)
            all_scores[key] = score

            if "Contains copyright markers" in score.get("issues", []):
                copyright_issues.append(key)

    # Print tier summary
    tiers = {"gold": 0, "silver": 0, "bronze": 0, "unrated": 0}
    for s in all_scores.values():
        tiers[s["tier"]] = tiers.get(s["tier"], 0) + 1

    # Count context-enhanced skills
    ce_count = sum(1 for s in all_scores.values() if s.get("context_enhanced", False))

    print(f"  Total skills scanned: {total_skills}")
    print(f"  {G}Gold   (100%): {tiers['gold']}{RESET}")
    print(f"  {B}Silver (≥66.5%): {tiers['silver']}{RESET}")
    print(f"  {Y}Bronze (≥45%): {tiers['bronze']}{RESET}")
    print(f"  {R}Unrated (<45%): {tiers['unrated']}{RESET}")
    print(f"  {G}Context-Enhanced (AaaS): {ce_count}{RESET}")
    print(f"  Copyright issues: {len(copyright_issues)}")
    print()

    # Phase 2: Strip copyright/attribution
    print(f"{Y}── Phase 2: Copyright stripping ──{RESET}")
    strip_count = 0

    for cat_dir in sorted(SKILLS_ROOT.iterdir()):
        if not cat_dir.is_dir() or cat_dir.name.startswith('.'):
            continue
        for skill_dir in sorted(cat_dir.iterdir()):
            if not skill_dir.is_dir() or skill_dir.name.startswith('.'):
                continue

            changes = strip_copyright(skill_dir, dry_run=not args.apply)
            if changes:
                strip_count += 1
                key = f"{cat_dir.name}/{skill_dir.name}"
                if not args.apply:
                    print(f"  {Y}[WOULD STRIP]{RESET} {key}")
                    for c in changes[:3]:
                        print(f"    ↳ {c}")
                else:
                    print(f"  {G}[STRIPPED]{RESET} {key}")

    print(f"\n  Skills {'to strip' if not args.apply else 'stripped'}: {strip_count}")
    print()

    # Phase 3: Rebuild manifest
    print(f"{Y}── Phase 3: Rebuilding manifest ──{RESET}")
    manifest = build_manifest(SKILLS_ROOT, all_scores)

    if args.apply:
        with open(MANIFEST_PATH, 'w') as f:
            json.dump(manifest, f, indent=2)
        print(f"  {G}[WRITTEN]{RESET} {MANIFEST_PATH}")
    else:
        print(f"  {Y}[WOULD WRITE]{RESET} {MANIFEST_PATH}")

    print(f"  Total skills: {manifest['total_skills']}")
    print(f"  Publishable (gold+silver): {manifest['publishable_skills']}")
    print()

    # Phase 4: Report
    print(f"{Y}{'='*60}{RESET}")
    publishable_pct = round(manifest['publishable_skills'] / max(manifest['total_skills'], 1) * 100, 1)
    print(f"  {W}Publishable: {manifest['publishable_skills']}/{manifest['total_skills']} ({publishable_pct}%){RESET}")

    if not args.apply:
        print(f"\n  {Y}This was a dry run. Use --apply to commit changes.{RESET}")
    else:
        print(f"\n  {G}All changes applied successfully.{RESET}")
    print(f"{Y}{'='*60}{RESET}\n")

    # Optional JSON report
    if args.json_report:
        report = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "total_skills": total_skills,
            "quality_distribution": tiers,
            "copyright_issues": copyright_issues,
            "strips_applied": strip_count,
            "publishable": manifest["publishable_skills"],
            "scores": {k: {"score": v["total_score"], "tier": v["tier"], "issues": v["issues"]}
                       for k, v in all_scores.items()},
        }
        with open(args.json_report, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"  Report written to {args.json_report}")


if __name__ == "__main__":
    main()
