#!/usr/bin/env python3
"""
Find Skills - Three-Tier Discovery Protocol
Version: 2.0.0

Searches for skills across three tiers:
1. Local project skills (./skills/)
2. Central Vault (~/.gemini/antigravity-vault/skills)
3. Global Registry (skills.sh via npx)

Usage:
    python3 discover.py "query"
    python3 discover.py "brand identity"
    python3 discover.py "testing" --include-remote
"""

import os
import glob
import subprocess
import sys
import argparse
from pathlib import Path

# Configuration - scoped to ~/.gemini/
GEMINI_ROOT = Path.home() / ".gemini"
VAULT_SKILLS_DIR = GEMINI_ROOT / "antigravity-vault" / "skills"
GLOBAL_SKILLS_DIR = GEMINI_ROOT / "antigravity" / "global_skills"


def search_skills_in_path(query: str, directory: Path, max_depth: int = 2) -> list:
    """
    Scans SKILL.md files in a directory for keyword matches.
    
    Args:
        query: Search terms (space-separated)
        directory: Path to search
        max_depth: How deep to search for SKILL.md files
    
    Returns:
        List of (score, skill_name, skill_path) tuples, sorted by relevance
    """
    matches = []
    if not directory.exists():
        return matches
    
    query_terms = query.lower().split()
    
    # Search patterns for different directory structures
    patterns = [
        str(directory / "*" / "SKILL.md"),           # Direct children
        str(directory / "*" / "*" / "SKILL.md"),     # One level deeper (for nested skills)
    ]
    
    seen_skills = set()
    
    for pattern in patterns[:max_depth]:
        for skill_file in glob.glob(pattern):
            skill_path = Path(skill_file)
            skill_name = skill_path.parent.name
            
            # Avoid duplicates
            if skill_name in seen_skills:
                continue
            seen_skills.add(skill_name)
            
            try:
                content = skill_path.read_text().lower()
                score = 0
                
                # Keyword matching in content
                for term in query_terms:
                    if term in content:
                        score += 1
                
                # Boost score if skill name matches
                if any(term in skill_name.lower() for term in query_terms):
                    score += 2
                
                if score > 0:
                    matches.append((score, skill_name, str(skill_path)))
            except Exception:
                continue
    
    # Sort by score descending
    matches.sort(key=lambda x: x[0], reverse=True)
    return matches


def search_remote_skills(query: str, timeout: int = 15) -> str:
    """
    Executes 'npx skills find' to get remote suggestions from skills.sh.
    
    Args:
        query: Search terms
        timeout: Maximum seconds to wait
    
    Returns:
        CLI output as string
    """
    try:
        result = subprocess.run(
            ["npx", "--yes", "skills", "find", query],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        return result.stdout
    except subprocess.TimeoutExpired:
        return "⏱️ Remote search timed out. Try browsing https://skills.sh/"
    except FileNotFoundError:
        return "⚠️ npx not found. Install Node.js to use remote search."
    except Exception as e:
        return f"⚠️ Error searching remote skills: {str(e)}"


def get_project_skills_dir() -> Path:
    """
    Determines the local project's skills directory.
    Works whether called from the project root or from within the skill.
    """
    # Start from current working directory
    cwd = Path.cwd()
    
    # Check if we're in a project with a skills/ folder
    if (cwd / "skills").exists():
        return cwd / "skills"
    
    # Check parent directories (up to ~/.gemini/)
    for parent in cwd.parents:
        if parent == GEMINI_ROOT or parent == Path.home():
            break
        if (parent / "skills").exists():
            return parent / "skills"
    
    # Fallback: assume we're in a subdirectory of the project
    return cwd / "skills"


def print_results(tier_name: str, emoji: str, matches: list, max_results: int = 5):
    """Pretty-print search results for a tier."""
    if not matches:
        return
    
    print(f"\n{emoji} **{tier_name}:**")
    for score, name, path in matches[:max_results]:
        # Make path relative if possible
        try:
            rel_path = Path(path).relative_to(Path.cwd())
            display_path = str(rel_path)
        except ValueError:
            display_path = path
        
        print(f"- **{name}** (Relevance: {score})")
        print(f"  Path: `{display_path}`")


def main():
    parser = argparse.ArgumentParser(
        description="Three-Tier Skill Discovery Protocol",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python3 discover.py "brand identity"
    python3 discover.py "testing" --include-remote
    python3 discover.py "ui design" --vault-only
        """
    )
    parser.add_argument("query", help="Keywords to search for")
    parser.add_argument("--include-remote", action="store_true",
                        help="Always include remote search (Tier 3)")
    parser.add_argument("--vault-only", action="store_true",
                        help="Search only the vault")
    parser.add_argument("--max-results", type=int, default=5,
                        help="Maximum results per tier (default: 5)")
    
    args = parser.parse_args()
    query = args.query
    
    print(f"🔍 Searching capabilities for: '{query}'...")
    
    local_hits = []
    vault_hits = []
    found_any = False
    
    # Tier 1: Local Project Skills
    if not args.vault_only:
        local_skills_dir = get_project_skills_dir()
        local_hits = search_skills_in_path(query, local_skills_dir)
        if local_hits:
            print_results("FOUND IN LOCAL PROJECT", "✅", local_hits, args.max_results)
            found_any = True
    
    # Tier 2: The Vault
    vault_hits = search_skills_in_path(query, VAULT_SKILLS_DIR)
    if vault_hits:
        print_results("FOUND IN THE VAULT", "🏛️", vault_hits, args.max_results)
        found_any = True
    
    # Tier 2.5: Global Skills (symlinked from skills.sh)
    if not args.vault_only:
        global_hits = search_skills_in_path(query, GLOBAL_SKILLS_DIR)
        if global_hits:
            print_results("FOUND IN GLOBAL SKILLS", "🌍", global_hits, args.max_results)
            found_any = True
    
    # Summary and recommendations
    if found_any:
        print("\n" + "─" * 50)
        print("💡 **Recommendation:** Use existing skills before installing new ones.")
        if local_hits:
            print("   → Local skills have highest priority (project-specific).")
        if vault_hits:
            print("   → Vault skills are proven across multiple projects.")
    
    # Tier 3: Remote (only if no local matches or explicitly requested)
    if args.include_remote or not found_any:
        print("\n🌐 **SEARCHING SKILLS.SH (Remote)...**")
        remote_output = search_remote_skills(query)
        if remote_output.strip():
            print(remote_output)
        else:
            print("No remote matches found.")
            print("Browse: https://skills.sh/")
    
    if not found_any and not args.include_remote:
        print("\n" + "─" * 50)
        print("💡 No local/vault matches. Run with --include-remote to search skills.sh")


if __name__ == "__main__":
    main()
