#!/usr/bin/env python3
"""
Infographic CLI wrapper.

Defaults to 1080x1350 and routes generation through the visual-design-system
Satori pipeline.
"""

import argparse
import json
import sys
import importlib.util
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parents[4]
GENERATOR_PATH = ROOT / "skills/cardiology/visual-design-system/scripts/generate_infographic.py"
DEFAULT_OUT_DIR = ROOT / "skills/cardiology/visual-design-system/outputs/infographics"


def load_generator():
    if not GENERATOR_PATH.exists():
        raise FileNotFoundError(f"Missing generator script: {GENERATOR_PATH}")
    spec = importlib.util.spec_from_file_location("generate_infographic", GENERATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    if spec.loader is None:
        raise RuntimeError("Failed to load infographic generator module")
    spec.loader.exec_module(module)
    return module


def read_data(args):
    if args.data and args.data_file:
        raise ValueError("Use only one of --data or --data-file")
    if args.data_file:
        data_path = Path(args.data_file)
        return json.loads(data_path.read_text())
    if args.data:
        return json.loads(args.data)
    raise ValueError("Missing infographic data. Provide --data or --data-file")


def resolve_output(path_value: Optional[str], template: str) -> Path:
    if path_value:
        return Path(path_value)
    DEFAULT_OUT_DIR.mkdir(parents=True, exist_ok=True)
    return DEFAULT_OUT_DIR / f"{template}.png"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate infographic outputs using the visual-design-system."
    )
    parser.add_argument("--template", help="Template name (stat-card, comparison, process-flow, trial-summary, key-finding)")
    parser.add_argument("--data", help="JSON data string")
    parser.add_argument("--data-file", help="Path to JSON file")
    parser.add_argument("--output", help="Output PNG path")
    parser.add_argument("--width", type=int, default=1080)
    parser.add_argument("--height", type=int, default=1350)
    parser.add_argument("--list", action="store_true", help="List available templates")

    args = parser.parse_args()

    module = load_generator()

    if args.list:
        templates = module.list_templates()
        print("Available templates:")
        for name in templates:
            print(f"- {name}")
        return 0

    if not args.template:
        print("Error: --template is required (or use --list)", file=sys.stderr)
        return 1

    try:
        data = read_data(args)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    output_path = resolve_output(args.output, args.template)

    result = module.generate(
        args.template,
        data,
        str(output_path),
        width=args.width,
        height=args.height,
    )

    if result.get("success"):
        print(f"Generated: {result.get('output')}")
        return 0

    print(f"Error: {result.get('error')}", file=sys.stderr)
    if result.get("stdout"):
        print(result.get("stdout"), file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
