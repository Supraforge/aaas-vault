#!/usr/bin/env python3
"""
LIDA Quick Visualization - AI-Driven Prototyping Tool
=====================================================

⚠️  **PROTOTYPING ONLY - NOT FOR PRODUCTION USE**

Microsoft LIDA integration for rapid visualization prototyping from natural language.
Automatically generates visualization code using LLMs (OpenAI, Gemini, Claude, etc.).

**Limitations:**
- Works best with ≤10 columns (LLM context constraints)
- Quality varies - ALWAYS review for medical accuracy
- No specialized medical charts documented (forest plots, Kaplan-Meier)
- Requires manual validation before any publication

**Use Cases:**
✅ Quick exploration ("Show me mortality rates by treatment arm")
✅ Multiple visualization candidates for exploratory analysis
✅ Content research (visualize PubMed search results)
✅ Automated reporting for internal review

❌ NOT for publication-ready charts (use plotly_charts.py instead)
❌ NOT for patient-facing materials without expert review
❌ NOT for regulatory submissions

Usage:
    # Basic usage
    python lida_quick_viz.py "Show mortality by treatment group" trial_data.csv

    # Generate multiple candidates
    python lida_quick_viz.py "Compare outcomes" data.csv --candidates 3

    # Specify visualization library
    python lida_quick_viz.py "Line chart of trends" data.csv --library plotly

    # Use medical template
    python lida_quick_viz.py "Trial results" data.csv --template trial_comparison

    # Interactive mode
    python lida_quick_viz.py --interactive data.csv

Medical Templates:
    trial_comparison    - Compare treatment arms (bar/forest plot style)
    patient_demographics - Age, gender, comorbidities (pie/bar charts)
    outcome_comparison  - Primary/secondary endpoints (grouped bars)
    trend_analysis      - Trends over time (line charts)
    survival_curve      - Time-to-event data (line chart, NOT true Kaplan-Meier)

Dependencies:
    pip install lida llmx openai pandas --break-system-packages

Environment Variables:
    OPENAI_API_KEY      - Required for OpenAI models
    ANTHROPIC_API_KEY   - For Claude models
    GOOGLE_API_KEY      - For Gemini models (FREE tier available)

Author: Dr. Shailesh Singh
Version: 1.0
Priority: P2 (prototyping tool)
"""

import argparse
import sys
import os
import json
import warnings
from pathlib import Path
from typing import Optional, List, Dict, Any
from datetime import datetime

# Suppress warnings
warnings.filterwarnings('ignore')

try:
    from lida import Manager, TextGenerationConfig, llm
    import pandas as pd
except ImportError:
    print("❌ Install dependencies:")
    print("   pip install lida llmx openai pandas --break-system-packages")
    sys.exit(1)


# Medical prompt templates for common cardiology visualizations
MEDICAL_TEMPLATES = {
    "trial_comparison": {
        "description": "Compare treatment arms in clinical trial",
        "prompt_template": """
Create a publication-quality visualization comparing {metric} across treatment groups.

Data columns: {columns}

Requirements:
- Clear group labels (Treatment A, B, Placebo)
- Error bars or confidence intervals if available
- Statistical significance indicators (p-values)
- Professional medical color scheme
- Legend and axis labels
- Title: {metric} by Treatment Group

Use bar chart or forest plot style. Keep it clean and publication-ready.
""",
        "suggested_columns": ["treatment_group", "outcome", "ci_lower", "ci_upper", "p_value"]
    },

    "patient_demographics": {
        "description": "Visualize patient baseline characteristics",
        "prompt_template": """
Create a clean visualization of patient demographics.

Data columns: {columns}

Requirements:
- Show distribution of age, gender, comorbidities
- Use appropriate chart types (pie for categorical, histogram for continuous)
- Professional medical styling
- Clear labels and percentages
- Title: Patient Demographics and Baseline Characteristics

Keep it simple and informative for a medical audience.
""",
        "suggested_columns": ["age", "gender", "comorbidity", "count", "percentage"]
    },

    "outcome_comparison": {
        "description": "Compare primary and secondary endpoints",
        "prompt_template": """
Create a grouped bar chart comparing outcomes across endpoints.

Data columns: {columns}

Requirements:
- Group by endpoint type (primary, secondary)
- Show treatment vs control
- Include confidence intervals or standard errors
- Professional color scheme (blues/teals for medical)
- Clear legend and axis labels
- Title: Clinical Outcomes Comparison

Make it suitable for a medical presentation or publication.
""",
        "suggested_columns": ["endpoint", "treatment", "outcome_rate", "ci_lower", "ci_upper"]
    },

    "trend_analysis": {
        "description": "Show trends over time",
        "prompt_template": """
Create a line chart showing {metric} trends over time.

Data columns: {columns}

Requirements:
- Time on x-axis, metric on y-axis
- Multiple lines for different groups/treatments if applicable
- Smooth lines with data points
- Professional medical styling
- Clear legend
- Title: {metric} Trends Over Time

Use a clean, publication-ready style.
""",
        "suggested_columns": ["time_point", "metric", "group", "value"]
    },

    "survival_curve": {
        "description": "Time-to-event visualization (simplified, NOT true Kaplan-Meier)",
        "prompt_template": """
Create a survival-style curve showing time-to-event data.

⚠️  NOTE: This is a simplified visualization, NOT a true Kaplan-Meier curve.
For publication, use proper survival analysis tools (lifelines, statsmodels).

Data columns: {columns}

Requirements:
- Time on x-axis (days/months/years)
- Survival probability or event-free probability on y-axis (0-100%)
- Multiple curves for different treatment groups
- Step function if possible
- At-risk numbers if available
- Professional medical styling
- Title: Event-Free Survival by Treatment Group

This is for EXPLORATION ONLY. Use proper survival analysis for final results.
""",
        "suggested_columns": ["time", "survival_probability", "group", "at_risk"]
    }
}


# Quality validation checklist
QUALITY_CHECKLIST = """
⚠️  QUALITY VALIDATION CHECKLIST - REVIEW BEFORE USE

Medical Accuracy:
[ ] Data interpretation is correct (no flipped axes, wrong scales)
[ ] Statistical measures are appropriate (means vs medians, etc.)
[ ] Confidence intervals/error bars are correct
[ ] P-values and significance are accurate
[ ] Sample sizes are represented correctly

Visual Design:
[ ] Chart type is appropriate for the data
[ ] Color scheme is professional and accessible
[ ] Labels are clear and complete
[ ] Legend is present and accurate
[ ] Title accurately describes the content

Medical Standards:
[ ] Follows publication standards (Nature/JACC/NEJM style)
[ ] No misleading visualizations (truncated axes, etc.)
[ ] Appropriate precision (no false precision)
[ ] Context is provided (N, time period, etc.)
[ ] Source attribution if needed

Limitations:
[ ] Aware this is AI-generated and needs review
[ ] Not using for patient-facing materials without expert review
[ ] Not using for regulatory submissions
[ ] Will recreate in production tools (Plotly) if publishing
"""


class LIDAQuickViz:
    """Wrapper for LIDA visualization generation with medical context."""

    def __init__(self, model: str = "openai", api_key: Optional[str] = None):
        """
        Initialize LIDA manager.

        Args:
            model: LLM provider ("openai", "gemini", "anthropic")
            api_key: API key (if not in environment)
        """
        self.model = model

        # Set API key if provided
        if api_key:
            if model == "openai":
                os.environ["OPENAI_API_KEY"] = api_key
            elif model == "anthropic":
                os.environ["ANTHROPIC_API_KEY"] = api_key
            elif model == "gemini":
                os.environ["GOOGLE_API_KEY"] = api_key

        # Check for API key
        key_mapping = {
            "openai": "OPENAI_API_KEY",
            "anthropic": "ANTHROPIC_API_KEY",
            "gemini": "GOOGLE_API_KEY"
        }

        required_key = key_mapping.get(model)
        if required_key and not os.getenv(required_key):
            print(f"⚠️  Warning: {required_key} not found in environment")
            print(f"   Set it with: export {required_key}=your_key")
            print(f"   Or use --api-key flag")

        try:
            # Initialize LIDA manager
            self.lida = Manager(text_gen=llm(model))
            print(f"✅ LIDA initialized with {model} model")
        except Exception as e:
            print(f"❌ Failed to initialize LIDA: {e}")
            sys.exit(1)

    def load_data(self, data_path: str) -> pd.DataFrame:
        """Load data from CSV or JSON."""
        path = Path(data_path)

        if not path.exists():
            raise FileNotFoundError(f"Data file not found: {data_path}")

        # Check column count
        if path.suffix == '.csv':
            df = pd.read_csv(data_path)
        elif path.suffix == '.json':
            df = pd.read_json(data_path)
        else:
            raise ValueError(f"Unsupported file format: {path.suffix}. Use .csv or .json")

        # Warn if too many columns
        if len(df.columns) > 10:
            print(f"⚠️  Warning: Dataset has {len(df.columns)} columns")
            print("   LIDA works best with ≤10 columns due to LLM context limits")
            print("   Consider selecting relevant columns only")

        print(f"📊 Loaded data: {len(df)} rows × {len(df.columns)} columns")
        print(f"   Columns: {', '.join(df.columns)}")

        return df

    def generate_prompt(self,
                        user_prompt: str,
                        template: Optional[str] = None,
                        columns: Optional[List[str]] = None) -> str:
        """
        Generate enhanced prompt with medical context.

        Args:
            user_prompt: User's natural language description
            template: Medical template name (from MEDICAL_TEMPLATES)
            columns: Available data columns

        Returns:
            Enhanced prompt with medical context
        """
        if template and template in MEDICAL_TEMPLATES:
            template_config = MEDICAL_TEMPLATES[template]
            prompt = template_config["prompt_template"].format(
                metric=user_prompt,
                columns=", ".join(columns) if columns else "unknown"
            )

            # Add suggested columns note
            suggested = template_config.get("suggested_columns", [])
            if suggested:
                prompt += f"\n\nSuggested column mapping: {', '.join(suggested)}"

            return prompt
        else:
            # Basic prompt with medical context
            base_prompt = f"""
Create a professional medical visualization: {user_prompt}

Available data columns: {', '.join(columns) if columns else 'unknown'}

Requirements:
- Publication-quality styling
- Clear labels and legend
- Professional medical color scheme (blues, teals, grays)
- Appropriate chart type for the data
- Clean and informative

Target audience: Medical professionals and researchers.
"""
            return base_prompt

    def visualize(self,
                  data_path: str,
                  prompt: str,
                  template: Optional[str] = None,
                  library: str = "plotly",
                  n_candidates: int = 1,
                  output_dir: str = "lida_output") -> List[Dict[str, Any]]:
        """
        Generate visualizations using LIDA.

        Args:
            data_path: Path to CSV/JSON data
            prompt: Natural language description of desired viz
            template: Medical template name (optional)
            library: Viz library ("plotly", "matplotlib", "seaborn", "altair")
            n_candidates: Number of visualization candidates to generate
            output_dir: Output directory for generated visualizations

        Returns:
            List of generated visualization metadata
        """
        print("\n" + "="*70)
        print("🚀 LIDA QUICK VISUALIZATION - PROTOTYPING TOOL")
        print("="*70)
        print("\n⚠️  REMINDER: This is for PROTOTYPING ONLY")
        print("   - Review all outputs for medical accuracy")
        print("   - NOT for publication without expert review")
        print("   - Use plotly_charts.py for production visualizations\n")

        # Load data
        df = self.load_data(data_path)

        # Generate data summary
        print("\n📋 Generating data summary...")
        summary = self.lida.summarize(data_path)

        # Generate enhanced prompt
        enhanced_prompt = self.generate_prompt(
            user_prompt=prompt,
            template=template,
            columns=df.columns.tolist()
        )

        print(f"\n🎯 Enhanced Prompt:\n{enhanced_prompt}\n")

        # Generate visualization goals
        print(f"🎨 Generating {n_candidates} visualization candidate(s)...")
        goals = self.lida.goals(summary, n=n_candidates, persona="medical researcher")

        # Generate visualizations
        results = []
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True, parents=True)

        for i, goal in enumerate(goals):
            print(f"\n📊 Candidate {i+1}/{len(goals)}: {goal.question}")
            print(f"   Rationale: {goal.rationale}")

            try:
                # Generate visualization code
                charts = self.lida.visualize(
                    summary=summary,
                    goal=goal,
                    library=library
                )

                if charts:
                    chart = charts[0]  # Take first chart

                    # Save code
                    code_file = output_path / f"candidate_{i+1}_code.py"
                    with open(code_file, 'w') as f:
                        f.write(chart.code)

                    # Save chart (base64 or raster)
                    chart_file = output_path / f"candidate_{i+1}.png"

                    # Execute and save (if possible)
                    try:
                        # LIDA returns base64 image in chart.raster
                        if hasattr(chart, 'raster') and chart.raster:
                            import base64
                            img_data = base64.b64decode(chart.raster)
                            with open(chart_file, 'wb') as f:
                                f.write(img_data)
                            print(f"   ✅ Saved: {chart_file}")
                        else:
                            print(f"   ⚠️  No raster image generated, code saved only")
                    except Exception as e:
                        print(f"   ⚠️  Could not save image: {e}")

                    results.append({
                        "candidate": i + 1,
                        "goal": goal.question,
                        "rationale": goal.rationale,
                        "code_file": str(code_file),
                        "chart_file": str(chart_file) if chart_file.exists() else None,
                        "library": library
                    })

            except Exception as e:
                print(f"   ❌ Error generating candidate {i+1}: {e}")

        # Print summary
        print("\n" + "="*70)
        print(f"✅ Generated {len(results)} visualization(s)")
        print(f"📁 Output directory: {output_path.absolute()}")
        print("="*70)

        # Print quality checklist
        print(QUALITY_CHECKLIST)

        return results

    def interactive_mode(self, data_path: str):
        """Interactive mode for iterative visualization creation."""
        print("\n" + "="*70)
        print("🔄 LIDA INTERACTIVE MODE")
        print("="*70)
        print("\nCommands:")
        print("  viz <prompt>          - Generate visualization")
        print("  template <name>       - Use medical template")
        print("  list                  - List available templates")
        print("  library <name>        - Switch visualization library")
        print("  quit                  - Exit")
        print("="*70 + "\n")

        # Load data once
        df = self.load_data(data_path)
        summary = self.lida.summarize(data_path)

        current_library = "plotly"
        current_template = None

        while True:
            try:
                cmd = input("\n> ").strip()

                if not cmd:
                    continue

                if cmd.lower() in ['quit', 'exit', 'q']:
                    print("👋 Goodbye!")
                    break

                elif cmd.lower() == 'list':
                    print("\n📋 Available Medical Templates:")
                    for name, config in MEDICAL_TEMPLATES.items():
                        print(f"  {name:20s} - {config['description']}")

                elif cmd.lower().startswith('template '):
                    template_name = cmd.split(' ', 1)[1].strip()
                    if template_name in MEDICAL_TEMPLATES:
                        current_template = template_name
                        print(f"✅ Template set to: {template_name}")
                    else:
                        print(f"❌ Unknown template: {template_name}")
                        print("   Use 'list' to see available templates")

                elif cmd.lower().startswith('library '):
                    lib_name = cmd.split(' ', 1)[1].strip()
                    if lib_name in ['plotly', 'matplotlib', 'seaborn', 'altair']:
                        current_library = lib_name
                        print(f"✅ Library set to: {lib_name}")
                    else:
                        print(f"❌ Unsupported library: {lib_name}")
                        print("   Supported: plotly, matplotlib, seaborn, altair")

                elif cmd.lower().startswith('viz '):
                    prompt = cmd.split(' ', 1)[1].strip()
                    self.visualize(
                        data_path=data_path,
                        prompt=prompt,
                        template=current_template,
                        library=current_library,
                        n_candidates=1
                    )

                else:
                    # Assume it's a visualization prompt
                    self.visualize(
                        data_path=data_path,
                        prompt=cmd,
                        template=current_template,
                        library=current_library,
                        n_candidates=1
                    )

            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="LIDA Quick Visualization - AI-Driven Prototyping (⚠️  PROTOTYPING ONLY)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage
  %(prog)s "Show mortality by treatment" trial_data.csv

  # Multiple candidates
  %(prog)s "Compare outcomes" data.csv --candidates 3

  # Use medical template
  %(prog)s "Trial results" data.csv --template trial_comparison

  # Specify library
  %(prog)s "Line chart of trends" data.csv --library matplotlib

  # Interactive mode
  %(prog)s --interactive data.csv

Medical Templates:
  trial_comparison     - Compare treatment arms
  patient_demographics - Baseline characteristics
  outcome_comparison   - Primary/secondary endpoints
  trend_analysis       - Trends over time
  survival_curve       - Time-to-event (simplified)

⚠️  LIMITATIONS:
  - Works best with ≤10 columns
  - Quality varies - ALWAYS review outputs
  - NOT for publication without expert review
  - Use plotly_charts.py for production
        """
    )

    parser.add_argument("prompt", nargs="?", help="Natural language visualization description")
    parser.add_argument("data", nargs="?", help="Path to CSV or JSON data file")

    parser.add_argument("-t", "--template",
                        choices=list(MEDICAL_TEMPLATES.keys()),
                        help="Medical template to use")
    parser.add_argument("-l", "--library",
                        default="plotly",
                        choices=["plotly", "matplotlib", "seaborn", "altair"],
                        help="Visualization library (default: plotly)")
    parser.add_argument("-n", "--candidates",
                        type=int,
                        default=1,
                        help="Number of visualization candidates (default: 1)")
    parser.add_argument("-o", "--output",
                        default="lida_output",
                        help="Output directory (default: lida_output)")
    parser.add_argument("-m", "--model",
                        default="openai",
                        choices=["openai", "gemini", "anthropic"],
                        help="LLM model to use (default: openai)")
    parser.add_argument("--api-key",
                        help="API key (if not in environment)")
    parser.add_argument("-i", "--interactive",
                        action="store_true",
                        help="Interactive mode")
    parser.add_argument("--list-templates",
                        action="store_true",
                        help="List available medical templates")

    args = parser.parse_args()

    # List templates
    if args.list_templates:
        print("\n📋 Medical Templates:\n")
        for name, config in MEDICAL_TEMPLATES.items():
            print(f"{name}")
            print(f"  Description: {config['description']}")
            print(f"  Suggested columns: {', '.join(config['suggested_columns'])}")
            print()
        return

    # Initialize LIDA
    viz = LIDAQuickViz(model=args.model, api_key=args.api_key)

    # Interactive mode
    if args.interactive:
        if not args.data:
            print("❌ Error: Data file required for interactive mode")
            print("   Usage: lida_quick_viz.py --interactive data.csv")
            sys.exit(1)
        viz.interactive_mode(args.data)
        return

    # Standard mode
    if not args.prompt or not args.data:
        parser.print_help()
        print("\n❌ Error: Both prompt and data file are required")
        print("   Usage: lida_quick_viz.py 'your prompt' data.csv")
        sys.exit(1)

    # Generate visualizations
    results = viz.visualize(
        data_path=args.data,
        prompt=args.prompt,
        template=args.template,
        library=args.library,
        n_candidates=args.candidates,
        output_dir=args.output
    )

    # Print results summary
    print("\n📊 Results Summary:")
    for result in results:
        print(f"\nCandidate {result['candidate']}:")
        print(f"  Goal: {result['goal']}")
        print(f"  Code: {result['code_file']}")
        if result['chart_file']:
            print(f"  Chart: {result['chart_file']}")


if __name__ == "__main__":
    main()
