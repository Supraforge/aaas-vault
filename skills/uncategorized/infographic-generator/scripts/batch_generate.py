#!/usr/bin/env python3
"""
Batch Infographic Generator

Generate multiple infographics from a batch configuration file.
Useful for creating complete content sets for articles, social media campaigns,
or systematic documentation.

Usage:
    # From JSON file
    python batch_generate.py --config batch_config.json

    # From YAML file
    python batch_generate.py --config batch_config.yaml --parallel 4

    # From inline JSON
    python batch_generate.py --json '[{"template": "infographic-hero", "data": {...}, "output": "hero.png"}]'

Example Config (JSON):
    [
        {
            "template": "infographic-hero",
            "data": {
                "stat": "26%",
                "label": "Mortality Reduction",
                "source": "PARADIGM-HF",
                "icon": "chart-down",
                "tag": "CLINICAL TRIAL"
            },
            "output": "outputs/hero-paradigm.png"
        },
        {
            "template": "infographic-comparison",
            "data": {
                "tag": "TREATMENT CHOICE",
                "title": "ACE-I vs ARB",
                "left": {...},
                "right": {...}
            },
            "output": "outputs/comparison-acei.png"
        }
    ]

Example Config (YAML):
    - template: infographic-hero
      data:
        stat: "26%"
        label: "Mortality Reduction"
        source: "PARADIGM-HF"
      output: "outputs/hero.png"

    - template: infographic-myth
      data:
        tag: "MYTH BUSTED"
        title: "Statins cause muscle damage"
        myth:
          text: "Taking statins will give you muscle pain"
        truth:
          text: "Only 5-10% experience symptoms"
      output: "outputs/myth-statins.png"
"""

import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, List
import importlib.util

# Import the generator
ROOT = Path(__file__).resolve().parents[1]
GENERATOR_PATH = ROOT.parent / "visual-design-system/scripts/generate_infographic.py"


def load_generator():
    """Load the infographic generator module."""
    if not GENERATOR_PATH.exists():
        raise FileNotFoundError(f"Missing generator: {GENERATOR_PATH}")

    spec = importlib.util.spec_from_file_location("generate_infographic", GENERATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    if spec.loader is None:
        raise RuntimeError("Failed to load generator module")
    spec.loader.exec_module(module)
    return module


def load_config(config_path: Path) -> List[Dict[str, Any]]:
    """
    Load batch configuration from JSON or YAML file.

    Args:
        config_path: Path to config file (.json or .yaml/.yml)

    Returns:
        List of infographic configs
    """
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    content = config_path.read_text()

    if config_path.suffix == '.json':
        return json.loads(content)
    elif config_path.suffix in ['.yaml', '.yml']:
        try:
            import yaml
            return yaml.safe_load(content)
        except ImportError:
            print("Error: PyYAML not installed. Install with: pip install pyyaml")
            sys.exit(1)
    else:
        raise ValueError(f"Unsupported config format: {config_path.suffix}")


def validate_item(item: Dict[str, Any], index: int) -> Dict[str, str]:
    """
    Validate a single batch item.

    Args:
        item: Batch item config
        index: Item index (for error messages)

    Returns:
        Dict with validation errors (empty if valid)
    """
    errors = {}

    if 'template' not in item:
        errors['template'] = f"Item {index}: Missing 'template' field"

    if 'data' not in item:
        errors['data'] = f"Item {index}: Missing 'data' field"

    if 'output' not in item:
        errors['output'] = f"Item {index}: Missing 'output' field"

    return errors


def generate_one(generator, item: Dict[str, Any], index: int) -> Dict[str, Any]:
    """
    Generate a single infographic.

    Args:
        generator: Generator module
        item: Batch item config
        index: Item index

    Returns:
        Result dict with success status
    """
    template = item['template']
    data = item['data']
    output = item['output']
    width = item.get('width', 1080)
    height = item.get('height', 1350)

    print(f"[{index + 1}] Generating {template} → {output}")

    result = generator.generate(
        template,
        data,
        output,
        width=width,
        height=height
    )

    result['index'] = index
    result['template'] = template
    result['output'] = output

    return result


def generate_batch(
    items: List[Dict[str, Any]],
    parallel: int = 1,
    stop_on_error: bool = False
) -> Dict[str, Any]:
    """
    Generate multiple infographics.

    Args:
        items: List of batch item configs
        parallel: Number of parallel workers (1 = sequential)
        stop_on_error: Stop on first error if True

    Returns:
        Summary dict with success/failure counts
    """
    generator = load_generator()

    # Validate all items first
    print(f"Validating {len(items)} items...")
    all_errors = []
    for i, item in enumerate(items):
        errors = validate_item(item, i)
        if errors:
            all_errors.extend(errors.values())

    if all_errors:
        print("\nValidation errors:")
        for error in all_errors:
            print(f"  ❌ {error}")
        return {
            'success': False,
            'total': len(items),
            'completed': 0,
            'failed': len(items),
            'errors': all_errors
        }

    # Generate infographics
    print(f"\nGenerating {len(items)} infographics (parallel={parallel})...")

    results = {
        'success': True,
        'total': len(items),
        'completed': 0,
        'failed': 0,
        'items': []
    }

    if parallel == 1:
        # Sequential generation
        for i, item in enumerate(items):
            result = generate_one(generator, item, i)
            results['items'].append(result)

            if result.get('success'):
                results['completed'] += 1
                print(f"  ✅ {result['output']}")
            else:
                results['failed'] += 1
                print(f"  ❌ {result['output']}: {result.get('error')}")
                if stop_on_error:
                    results['success'] = False
                    break
    else:
        # Parallel generation
        with ThreadPoolExecutor(max_workers=parallel) as executor:
            futures = {
                executor.submit(generate_one, generator, item, i): i
                for i, item in enumerate(items)
            }

            for future in as_completed(futures):
                result = future.result()
                results['items'].append(result)

                if result.get('success'):
                    results['completed'] += 1
                    print(f"  ✅ {result['output']}")
                else:
                    results['failed'] += 1
                    print(f"  ❌ {result['output']}: {result.get('error')}")
                    if stop_on_error:
                        results['success'] = False
                        executor.shutdown(wait=False, cancel_futures=True)
                        break

    # Sort results by index
    results['items'].sort(key=lambda x: x.get('index', 0))

    return results


def main() -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Generate multiple infographics from a batch config",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    parser.add_argument(
        '--config',
        type=Path,
        help='Path to batch config file (.json or .yaml)'
    )
    parser.add_argument(
        '--json',
        help='Inline JSON config string'
    )
    parser.add_argument(
        '--parallel',
        type=int,
        default=1,
        help='Number of parallel workers (default: 1 = sequential)'
    )
    parser.add_argument(
        '--stop-on-error',
        action='store_true',
        help='Stop on first error'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Validate config without generating'
    )

    args = parser.parse_args()

    # Load config
    if args.config and args.json:
        print("Error: Specify only one of --config or --json")
        return 1

    if args.config:
        items = load_config(args.config)
    elif args.json:
        items = json.loads(args.json)
    else:
        print("Error: Must specify --config or --json")
        return 1

    if not items:
        print("Error: Config is empty")
        return 1

    # Dry run - validate only
    if args.dry_run:
        print(f"Validating {len(items)} items...")
        all_errors = []
        for i, item in enumerate(items):
            errors = validate_item(item, i)
            if errors:
                all_errors.extend(errors.values())

        if all_errors:
            print("\nValidation errors:")
            for error in all_errors:
                print(f"  ❌ {error}")
            return 1
        else:
            print(f"✅ All {len(items)} items valid")
            return 0

    # Generate
    results = generate_batch(
        items,
        parallel=args.parallel,
        stop_on_error=args.stop_on_error
    )

    # Print summary
    print("\n" + "=" * 60)
    print(f"Batch Generation Summary")
    print("=" * 60)
    print(f"Total:     {results['total']}")
    print(f"Completed: {results['completed']} ✅")
    print(f"Failed:    {results['failed']} ❌")
    print("=" * 60)

    if results['failed'] > 0:
        print("\nFailed items:")
        for item in results['items']:
            if not item.get('success'):
                print(f"  ❌ {item['template']} → {item['output']}")
                print(f"     {item.get('error')}")

    return 0 if results['success'] and results['failed'] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
