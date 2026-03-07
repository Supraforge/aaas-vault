#!/usr/bin/env python3
"""
Template Manager - CRUD operations for content templates.
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

SKILL_DIR = Path(__file__).parent.parent
TEMPLATES_DIR = SKILL_DIR / "resources" / "templates"
INDEX_PATH = SKILL_DIR / "data" / "template_index.json"


def ensure_data_dir():
    """Ensure data directory exists."""
    (SKILL_DIR / "data").mkdir(exist_ok=True)


def load_template_index() -> Dict:
    """Load or create template index."""
    ensure_data_dir()
    if INDEX_PATH.exists():
        with open(INDEX_PATH) as f:
            return json.load(f)
    return {"templates": [], "last_updated": None}


def save_template_index(index: Dict):
    """Save template index."""
    ensure_data_dir()
    index["last_updated"] = datetime.now().isoformat()
    with open(INDEX_PATH, "w") as f:
        json.dump(index, f, indent=2)


def parse_template_frontmatter(content: str) -> tuple:
    """Parse YAML frontmatter from template content."""
    if not content.startswith("---"):
        return {}, content

    # Find end of frontmatter
    end_match = re.search(r'\n---\n', content[3:])
    if not end_match:
        return {}, content

    frontmatter_text = content[3:end_match.start() + 3]
    body = content[end_match.end() + 3:]

    # Simple YAML parsing (basic key: value)
    metadata = {}
    current_key = None
    current_list = None

    for line in frontmatter_text.split('\n'):
        line = line.rstrip()
        if not line:
            continue

        # List item
        if line.startswith('  - '):
            if current_list is not None:
                item = line[4:].strip()
                # Check if it's a dict item (has nested properties)
                if ':' in item and not item.startswith('"'):
                    # Parse as simple dict
                    parts = item.split(':', 1)
                    current_list.append({parts[0].strip(): parts[1].strip()})
                else:
                    current_list.append(item.strip('"\''))
            continue

        # Dict item under list
        if line.startswith('    ') and current_list is not None and current_list:
            if isinstance(current_list[-1], dict):
                parts = line.strip().split(':', 1)
                if len(parts) == 2:
                    current_list[-1][parts[0].strip()] = parts[1].strip().strip('"\'')
            continue

        # New key
        if ':' in line:
            parts = line.split(':', 1)
            key = parts[0].strip()
            value = parts[1].strip()

            if value == '':
                # Could be a list or nested structure
                metadata[key] = []
                current_key = key
                current_list = metadata[key]
            elif value.startswith('[') and value.endswith(']'):
                # Inline list
                items = value[1:-1].split(',')
                metadata[key] = [i.strip().strip('"\'') for i in items if i.strip()]
                current_list = None
            else:
                metadata[key] = value.strip('"\'')
                current_list = None

    return metadata, body


def scan_templates() -> List[Dict]:
    """Scan template directories and build index."""
    templates = []

    for category_dir in TEMPLATES_DIR.iterdir():
        if not category_dir.is_dir():
            continue

        category = category_dir.name

        for template_file in category_dir.glob("*.md"):
            with open(template_file) as f:
                content = f.read()

            metadata, body = parse_template_frontmatter(content)

            template_id = metadata.get("id", template_file.stem)

            templates.append({
                "id": template_id,
                "name": metadata.get("name", template_id.replace("_", " ").title()),
                "category": category,
                "path": str(template_file.relative_to(SKILL_DIR)),
                "tags": metadata.get("tags", []),
                "variables": metadata.get("variables", []),
                "description": metadata.get("description", "")
            })

    return templates


def rebuild_index():
    """Rebuild template index from files."""
    templates = scan_templates()
    index = {
        "templates": templates,
        "last_updated": datetime.now().isoformat()
    }
    save_template_index(index)
    return index


def list_templates(category: Optional[str] = None, tag: Optional[str] = None) -> List[Dict]:
    """List templates with optional filtering."""
    index = load_template_index()

    # Rebuild if empty
    if not index.get("templates"):
        index = rebuild_index()

    templates = index.get("templates", [])

    # Filter by category
    if category:
        templates = [t for t in templates if t.get("category") == category]

    # Filter by tag
    if tag:
        templates = [t for t in templates if tag in t.get("tags", [])]

    return templates


def get_template(template_id: str) -> Optional[Dict]:
    """Get template by ID with full content."""
    index = load_template_index()

    # Find template in index
    template_info = None
    for t in index.get("templates", []):
        if t["id"] == template_id:
            template_info = t
            break

    if not template_info:
        # Try to find by scanning
        index = rebuild_index()
        for t in index.get("templates", []):
            if t["id"] == template_id:
                template_info = t
                break

    if not template_info:
        return None

    # Load full content
    template_path = SKILL_DIR / template_info["path"]
    if not template_path.exists():
        return None

    with open(template_path) as f:
        content = f.read()

    metadata, body = parse_template_frontmatter(content)

    return {
        **template_info,
        "metadata": metadata,
        "content": body.strip()
    }


def instantiate_template(template_id: str, variables: Dict, output_path: Optional[str] = None) -> str:
    """Fill template with variables using simple substitution."""
    template = get_template(template_id)
    if not template:
        raise ValueError(f"Template not found: {template_id}")

    content = template["content"]

    # Simple variable substitution {{ var }}
    for key, value in variables.items():
        content = content.replace("{{ " + key + " }}", str(value))
        content = content.replace("{{" + key + "}}", str(value))

    # Handle conditionals {% if var %}...{% endif %}
    # Simple implementation - just include block if var is truthy
    def replace_conditional(match):
        var_name = match.group(1).strip()
        block_content = match.group(2)
        if variables.get(var_name):
            return block_content
        return ""

    content = re.sub(
        r'\{%\s*if\s+(\w+)\s*%\}(.*?)\{%\s*endif\s*%\}',
        replace_conditional,
        content,
        flags=re.DOTALL
    )

    # Clean up any remaining unfilled variables (mark them)
    content = re.sub(r'\{\{\s*(\w+)\s*\}\}', r'[MISSING: \1]', content)

    if output_path:
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)
        with open(output, "w") as f:
            f.write(content)

    return content


def main():
    parser = argparse.ArgumentParser(description="Manage content templates")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # List command
    list_parser = subparsers.add_parser("list", help="List templates")
    list_parser.add_argument("--category", "-c", help="Filter by category")
    list_parser.add_argument("--tag", "-t", help="Filter by tag")
    list_parser.add_argument("--output", "-o", choices=["json", "text"], default="text")

    # Get command
    get_parser = subparsers.add_parser("get", help="Get template details")
    get_parser.add_argument("template_id", help="Template ID")
    get_parser.add_argument("--output", "-o", choices=["json", "text"], default="text")

    # Instantiate command
    inst_parser = subparsers.add_parser("instantiate", help="Fill template with variables")
    inst_parser.add_argument("template_id", help="Template ID")
    inst_parser.add_argument("--vars", "-v", required=True, help="JSON object of variables")
    inst_parser.add_argument("--output", "-o", help="Output file path")

    # Rebuild command
    subparsers.add_parser("rebuild", help="Rebuild template index")

    args = parser.parse_args()

    if args.command == "list":
        templates = list_templates(args.category, args.tag)

        if args.output == "json":
            print(json.dumps(templates, indent=2))
        else:
            print(f"\n{'='*60}")
            print(f"CONTENT TEMPLATES ({len(templates)} found)")
            print(f"{'='*60}\n")

            # Group by category
            by_category = {}
            for t in templates:
                cat = t.get("category", "other")
                by_category.setdefault(cat, []).append(t)

            for cat, cat_templates in sorted(by_category.items()):
                print(f"--- {cat.upper()} ---")
                for t in cat_templates:
                    tags = ", ".join(t.get("tags", [])[:3])
                    print(f"  {t['id']:30} {t['name'][:30]:30} [{tags}]")
                print()

    elif args.command == "get":
        template = get_template(args.template_id)

        if not template:
            print(f"Error: Template not found: {args.template_id}", file=sys.stderr)
            sys.exit(1)

        if args.output == "json":
            print(json.dumps(template, indent=2))
        else:
            print(f"\n{'='*60}")
            print(f"TEMPLATE: {template['name']}")
            print(f"{'='*60}\n")
            print(f"ID: {template['id']}")
            print(f"Category: {template['category']}")
            print(f"Tags: {', '.join(template.get('tags', []))}")

            if template.get("variables"):
                print(f"\nVariables:")
                for var in template["variables"]:
                    if isinstance(var, dict):
                        req = "(required)" if var.get("required") else "(optional)"
                        print(f"  - {var.get('name', 'unknown')} {req}")
                    else:
                        print(f"  - {var}")

            print(f"\nContent Preview:")
            print("-" * 40)
            preview = template["content"][:500]
            if len(template["content"]) > 500:
                preview += "\n... [truncated]"
            print(preview)
            print()

    elif args.command == "instantiate":
        try:
            variables = json.loads(args.vars)
        except json.JSONDecodeError as e:
            print(f"Error parsing variables JSON: {e}", file=sys.stderr)
            sys.exit(1)

        try:
            result = instantiate_template(args.template_id, variables, args.output)
            if args.output:
                print(f"Template instantiated to: {args.output}")
            else:
                print(result)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "rebuild":
        index = rebuild_index()
        print(f"Index rebuilt with {len(index['templates'])} templates")


if __name__ == "__main__":
    main()
