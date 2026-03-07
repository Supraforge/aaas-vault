#!/usr/bin/env python3
"""
Boilerplate Manager - Manage company boilerplate text.
"""

import argparse
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent
BOILERPLATE_DIR = SKILL_DIR / "resources" / "boilerplate"


def ensure_dir():
    """Ensure boilerplate directory exists."""
    BOILERPLATE_DIR.mkdir(parents=True, exist_ok=True)


def get_boilerplate(brand: str) -> str:
    """Get boilerplate for a brand."""
    ensure_dir()
    path = BOILERPLATE_DIR / f"{brand}.md"

    if not path.exists():
        # Return default
        return f"""[{brand.upper()}] develops innovative solutions for engineering teams.

For more information, visit [{brand}.com](https://{brand}.com)."""

    with open(path) as f:
        return f.read()


def update_boilerplate(brand: str, content: str):
    """Update boilerplate for a brand."""
    ensure_dir()
    path = BOILERPLATE_DIR / f"{brand}.md"

    with open(path, "w") as f:
        f.write(content)

    return path


def list_boilerplates():
    """List all available boilerplates."""
    ensure_dir()
    boilerplates = list(BOILERPLATE_DIR.glob("*.md"))
    return [bp.stem for bp in boilerplates]


def main():
    parser = argparse.ArgumentParser(description="Manage company boilerplate")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Get command
    get_parser = subparsers.add_parser("get", help="Get boilerplate for a brand")
    get_parser.add_argument("brand", help="Brand slug")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update boilerplate")
    update_parser.add_argument("brand", help="Brand slug")
    update_parser.add_argument("--file", "-f", help="File containing new boilerplate")
    update_parser.add_argument("--text", "-t", help="Boilerplate text")

    # List command
    subparsers.add_parser("list", help="List all boilerplates")

    args = parser.parse_args()

    if args.command == "get":
        content = get_boilerplate(args.brand)
        print(content)

    elif args.command == "update":
        if args.file:
            with open(args.file) as f:
                content = f.read()
        elif args.text:
            content = args.text
        else:
            print("Error: Provide --file or --text", file=sys.stderr)
            sys.exit(1)

        path = update_boilerplate(args.brand, content)
        print(f"Updated: {path}")

    elif args.command == "list":
        brands = list_boilerplates()
        if brands:
            print("Available boilerplates:")
            for b in brands:
                print(f"  - {b}")
        else:
            print("No boilerplates found. Create one with 'update' command.")


if __name__ == "__main__":
    main()
