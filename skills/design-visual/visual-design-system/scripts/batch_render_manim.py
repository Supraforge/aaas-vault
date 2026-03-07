#!/usr/bin/env python3
"""
Batch render all Manim scenes for QA purposes.

Usage:
    python scripts/batch_render_manim.py                # Render all at medium quality
    python scripts/batch_render_manim.py --quality l    # Render all at low quality (faster)
    python scripts/batch_render_manim.py --quality h    # Render all at high quality
    python scripts/batch_render_manim.py --category arrhythmia  # Only render one category
    python scripts/batch_render_manim.py --scenes ecg_wave kaplan_meier  # Only specific scenes
    python scripts/batch_render_manim.py --parallel 4   # Render 4 scenes in parallel
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import Optional

SCRIPT_DIR = Path(__file__).resolve().parent
VISUAL_SYSTEM_ROOT = SCRIPT_DIR.parent
CATALOG_PATH = VISUAL_SYSTEM_ROOT / "manim_animations" / "scene_catalog.json"
RENDER_SCRIPT = SCRIPT_DIR / "render_manim.py"
VENV_PYTHON = VISUAL_SYSTEM_ROOT / ".venv-manim" / "bin" / "python"


def load_catalog() -> dict:
    """Load the scene catalog."""
    with open(CATALOG_PATH) as f:
        return json.load(f)


def render_scene(
    scene_key: str,
    quality: str = "m",
    fmt: str = "mp4",
    output_dir: Optional[Path] = None,
) -> tuple[str, bool, str]:
    """
    Render a single scene.

    Returns: (scene_key, success, message)
    """
    cmd = [
        str(VENV_PYTHON),
        str(RENDER_SCRIPT),
        scene_key,
        "--quality", quality,
        "--format", fmt,
    ]
    if output_dir:
        cmd.extend(["--output-dir", str(output_dir)])

    start_time = time.time()
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300,  # 5 minutes max per scene
            cwd=str(VISUAL_SYSTEM_ROOT),
        )
        elapsed = time.time() - start_time

        if result.returncode == 0:
            return (scene_key, True, f"Rendered in {elapsed:.1f}s")
        else:
            error_lines = result.stderr.split("\n")[-5:]
            return (scene_key, False, f"Failed: {' '.join(error_lines)[:200]}")
    except subprocess.TimeoutExpired:
        return (scene_key, False, "Timeout after 5 minutes")
    except Exception as e:
        return (scene_key, False, f"Error: {str(e)[:200]}")


def main():
    parser = argparse.ArgumentParser(description="Batch render all Manim scenes.")
    parser.add_argument("--quality", choices=["l", "m", "h", "k"], default="m",
                        help="Render quality: l=low (480p), m=medium (720p), h=high (1080p), k=4K")
    parser.add_argument("--format", choices=["mp4", "gif"], default="mp4",
                        help="Output format")
    parser.add_argument("--output-dir", type=str, default=None,
                        help="Custom output directory")
    parser.add_argument("--category", type=str, default=None,
                        help="Only render scenes from this category")
    parser.add_argument("--scenes", nargs="+", type=str, default=None,
                        help="Only render specific scenes")
    parser.add_argument("--parallel", type=int, default=1,
                        help="Number of parallel renders (default: 1)")
    parser.add_argument("--dry-run", action="store_true",
                        help="List scenes to render without rendering")

    args = parser.parse_args()

    catalog = load_catalog()

    # Filter scenes
    scenes_to_render = list(catalog.keys())

    if args.category:
        scenes_to_render = [
            k for k, v in catalog.items()
            if v.get("category") == args.category
        ]

    if args.scenes:
        scenes_to_render = [s for s in args.scenes if s in catalog]

    if not scenes_to_render:
        print("No scenes to render.")
        return 1

    # Sort by category for nicer output
    scenes_to_render.sort(key=lambda k: (catalog[k].get("category", ""), k))

    print(f"{'=' * 60}")
    print(f"Manim Batch Renderer - {len(scenes_to_render)} scenes")
    print(f"Quality: {args.quality} | Format: {args.format}")
    print(f"Parallel: {args.parallel}")
    print(f"{'=' * 60}")

    # Group by category for display
    by_category = {}
    for scene in scenes_to_render:
        cat = catalog[scene].get("category", "uncategorized")
        by_category.setdefault(cat, []).append(scene)

    for cat, scenes in sorted(by_category.items()):
        print(f"\n[{cat}]")
        for s in scenes:
            desc = catalog[s].get("description", "")[:50]
            print(f"  - {s}: {desc}")

    if args.dry_run:
        print(f"\n[DRY RUN] Would render {len(scenes_to_render)} scenes.")
        return 0

    print(f"\n{'=' * 60}")
    print("Starting batch render...")
    print(f"{'=' * 60}\n")

    output_dir = Path(args.output_dir) if args.output_dir else None

    results = []
    start_time = time.time()

    if args.parallel > 1:
        # Parallel rendering
        with ProcessPoolExecutor(max_workers=args.parallel) as executor:
            futures = {
                executor.submit(render_scene, scene, args.quality, args.format, output_dir): scene
                for scene in scenes_to_render
            }
            for future in as_completed(futures):
                scene_key, success, message = future.result()
                status = "✓" if success else "✗"
                print(f"  [{status}] {scene_key}: {message}")
                results.append((scene_key, success, message))
    else:
        # Sequential rendering
        for i, scene in enumerate(scenes_to_render, 1):
            print(f"[{i}/{len(scenes_to_render)}] Rendering {scene}...", end=" ", flush=True)
            scene_key, success, message = render_scene(scene, args.quality, args.format, output_dir)
            status = "✓" if success else "✗"
            print(f"[{status}] {message}")
            results.append((scene_key, success, message))

    # Summary
    elapsed = time.time() - start_time
    success_count = sum(1 for _, s, _ in results if s)
    fail_count = len(results) - success_count

    print(f"\n{'=' * 60}")
    print(f"Batch render complete in {elapsed:.1f}s")
    print(f"  Success: {success_count}/{len(results)}")
    print(f"  Failed:  {fail_count}/{len(results)}")
    print(f"{'=' * 60}")

    if fail_count > 0:
        print("\nFailed scenes:")
        for scene_key, success, message in results:
            if not success:
                print(f"  - {scene_key}: {message}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
