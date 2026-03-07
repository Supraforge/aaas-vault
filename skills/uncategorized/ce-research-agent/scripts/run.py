#!/usr/bin/env python3
"""
Universal runner for CE Research Agent skill scripts
Ensures all scripts run with the correct virtual environment
"""

import os
import sys
import subprocess
from pathlib import Path


def get_venv_python():
    """Get the virtual environment Python executable"""
    skill_dir = Path(__file__).parent.parent
    venv_dir = skill_dir / ".venv"

    if os.name == 'nt':  # Windows
        venv_python = venv_dir / "Scripts" / "python.exe"
    else:  # Unix/Linux/Mac
        venv_python = venv_dir / "bin" / "python"

    return venv_python


def ensure_venv():
    """Ensure virtual environment exists and dependencies are installed"""
    skill_dir = Path(__file__).parent.parent
    venv_dir = skill_dir / ".venv"
    requirements_file = skill_dir / "requirements.txt"

    venv_python = get_venv_python()

    # Check if venv exists
    if not venv_dir.exists():
        print("Setting up virtual environment...")

        # Create venv
        result = subprocess.run([sys.executable, "-m", "venv", str(venv_dir)])
        if result.returncode != 0:
            print("Failed to create virtual environment")
            sys.exit(1)

        # Install dependencies if requirements.txt exists
        if requirements_file.exists():
            print("Installing dependencies...")
            pip_cmd = [str(venv_python), "-m", "pip", "install", "-r", str(requirements_file)]
            result = subprocess.run(pip_cmd, capture_output=True)
            if result.returncode != 0:
                print(f"Warning: Some dependencies may not have installed: {result.stderr.decode()}")

        print("Environment ready!")

    return venv_python


def main():
    """Main runner"""
    if len(sys.argv) < 2:
        print("CE Research Agent - Script Runner")
        print("\nUsage: python run.py <script_name> [args...]")
        print("\nAvailable scripts:")
        print("  research_company.py      - Company snapshot research")
        print("  research_competitors.py  - Competitor intelligence")
        print("  research_market.py       - Market intelligence")
        print("  research_audience.py     - Audience intelligence")
        print("  research_brand.py        - Brand/voice forensics")
        print("  research_strategy.py     - Strategy pattern scan")
        print("  validate_research.py     - Validate research quality")
        print("  synthesize_framework.py  - Generate SQUR framework")
        print("\nExample:")
        print("  python run.py research_company.py --company 'Acme Inc'")
        sys.exit(1)

    script_name = sys.argv[1]
    script_args = sys.argv[2:]

    # Handle both "scripts/script.py" and "script.py" formats
    if script_name.startswith('scripts/'):
        script_name = script_name[8:]

    # Ensure .py extension
    if not script_name.endswith('.py'):
        script_name += '.py'

    # Get script path
    skill_dir = Path(__file__).parent.parent
    script_path = skill_dir / "scripts" / script_name

    if not script_path.exists():
        print(f"Script not found: {script_name}")
        print(f"Looked for: {script_path}")
        sys.exit(1)

    # Ensure venv exists and get Python executable
    venv_python = ensure_venv()

    # Build command
    cmd = [str(venv_python), str(script_path)] + script_args

    # Run the script
    try:
        result = subprocess.run(cmd)
        sys.exit(result.returncode)
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
