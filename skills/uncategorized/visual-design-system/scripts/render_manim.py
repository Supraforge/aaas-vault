"""
CLI helper to render Manim scenes in the visual design system.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
from pathlib import Path


CATALOG_PATH = Path(__file__).resolve().parents[1] / "manim_animations" / "scene_catalog.json"


def load_scene_catalog() -> dict:
    if not CATALOG_PATH.exists():
        raise SystemExit(f"Scene catalog not found: {CATALOG_PATH}")
    with open(CATALOG_PATH, "r") as handle:
        return json.load(handle)


def resolve_manim_bin(manim_bin: str | None) -> tuple[str, bool]:
    """
    Resolve the Manim executable path from args or environment.

    Priority: CLI arg -> MANIM_BIN -> MANIM_VENV -> local .venv-manim -> PATH

    Returns: (path, use_module) - path to executable and whether to use -m manim
    """
    # Check local .venv-manim first (most common case)
    local_venv = Path(__file__).resolve().parents[1] / ".venv-manim" / "bin" / "python"
    if local_venv.exists():
        return str(local_venv), True

    if manim_bin:
        candidate = Path(manim_bin)
        if candidate.is_dir():
            # It's a venv directory, use python -m manim
            python_path = candidate / "bin" / "python"
            if python_path.exists():
                return str(python_path), True
            candidate = candidate / "bin" / "manim"
        return (str(candidate), False) if candidate.exists() else (None, False)

    env_bin = os.getenv("MANIM_BIN")
    if env_bin:
        candidate = Path(env_bin)
        return (str(candidate), False) if candidate.exists() else (None, False)

    env_venv = os.getenv("MANIM_VENV")
    if env_venv:
        python_path = Path(env_venv) / "bin" / "python"
        if python_path.exists():
            return str(python_path), True
        candidate = Path(env_venv) / "bin" / "manim"
        return (str(candidate), False) if candidate.exists() else (None, False)

    manim_path = shutil.which("manim")
    return (manim_path, False) if manim_path else (None, False)


def build_command(
    scene_class: str,
    scene_file: Path,
    quality: str,
    output_dir: Path,
    preview: bool,
    fmt: str,
    manim_bin: str,
    use_module: bool = False,
) -> list[str]:
    quality_flags = {
        "l": "-ql",
        "m": "-qm",
        "h": "-qh",
        "k": "-qk",
    }

    if use_module:
        cmd = [manim_bin, "-m", "manim", quality_flags[quality], "--format", fmt, str(scene_file), scene_class]
    else:
        cmd = [manim_bin, quality_flags[quality], "--format", fmt, str(scene_file), scene_class]
    if preview:
        cmd.insert(3 if use_module else 1, "-p")
    cmd.extend(["--media_dir", str(output_dir)])
    return cmd


def main() -> int:
    parser = argparse.ArgumentParser(description="Render Manim scenes for cardiology visuals.")
    parser.add_argument("scene", nargs="?", help="Scene key to render")
    parser.add_argument("--quality", choices=["l", "m", "h", "k"], default="m", help="Manim quality preset")
    parser.add_argument("--format", choices=["mp4", "gif"], default="mp4", help="Output format")
    parser.add_argument("--preview", action="store_true", help="Open preview after render")
    parser.add_argument(
        "--output-dir",
        default=str(Path(__file__).resolve().parents[1] / "outputs" / "manim"),
        help="Directory for Manim media output",
    )
    parser.add_argument("--manim-bin", help="Path to Manim executable or venv directory")
    parser.add_argument("--list", action="store_true", help="List available scenes")
    parser.add_argument("--dry-run", action="store_true", help="Print command without running")

    args = parser.parse_args()

    catalog = load_scene_catalog()
    scenes = sorted(catalog.keys())

    if args.list:
        for key in scenes:
            entry = catalog[key]
            description = entry.get("description", "")
            category = entry.get("category", "uncategorized")
            print(f"{key} [{category}] - {description}")
        return 0

    if not args.scene:
        raise SystemExit("Scene key is required. Use --list to view available scenes.")

    if args.scene not in catalog:
        raise SystemExit(f"Unknown scene key: {args.scene}")

    manim_bin, use_module = resolve_manim_bin(args.manim_bin)
    if not manim_bin:
        raise SystemExit("manim is not installed. Install with: pip install manim")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    entry = catalog[args.scene]
    scene_class = entry["class"]
    scene_file = Path(__file__).resolve().parents[1] / "manim_animations" / entry.get("file", "scenes.py")

    cmd = build_command(scene_class, scene_file, args.quality, output_dir, args.preview, args.format, manim_bin, use_module)

    if args.dry_run:
        print(" ".join(cmd))
        return 0

    completed = subprocess.run(cmd, check=False)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
