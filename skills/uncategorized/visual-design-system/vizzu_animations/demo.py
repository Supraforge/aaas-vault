#!/usr/bin/env python3
"""
Demo script showing Vizzu animated visualizations.

Run this to see all 5 medical animation templates in action.
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from templates import (
    create_animated_kaplan_meier,
    create_animated_forest_plot,
    create_animated_bar_comparison,
    create_animated_trend_line,
    create_animated_trial_enrollment,
)


def demo_kaplan_meier():
    """Demo: Animated Kaplan-Meier survival curves."""
    print("\n📊 Demo 1: Kaplan-Meier Survival Curves")
    print("-" * 50)

    treatment = [(0, 100), (6, 94), (12, 88), (18, 83), (24, 78)]
    control = [(0, 100), (6, 91), (12, 83), (18, 76), (24, 69)]

    output = create_animated_kaplan_meier(
        treatment,
        control,
        treatment_name="Dapagliflozin",
        control_name="Placebo",
        title="DAPA-HF: Event-Free Survival",
        hr_text="HR 0.74 (95% CI 0.65-0.85)",
    )

    print(f"✅ Created: {output}")
    print("   Use case: Trial survival curves, event-free survival")
    return output


def demo_forest_plot():
    """Demo: Animated forest plot for meta-analysis."""
    print("\n📊 Demo 2: Forest Plot Meta-Analysis")
    print("-" * 50)

    studies = [
        {"name": "DAPA-HF", "estimate": 0.74, "lower": 0.65, "upper": 0.85, "weight": 60},
        {"name": "EMPEROR-Reduced", "estimate": 0.75, "lower": 0.65, "upper": 0.86, "weight": 50},
        {"name": "SOLOIST-WHF", "estimate": 0.67, "lower": 0.52, "upper": 0.85, "weight": 30},
        {"name": "DELIVER", "estimate": 0.82, "lower": 0.73, "upper": 0.92, "weight": 70},
    ]

    output = create_animated_forest_plot(
        studies,
        title="SGLT2 Inhibitors in Heart Failure",
        show_pooled=True,
    )

    print(f"✅ Created: {output}")
    print("   Use case: Meta-analyses, systematic reviews")
    return output


def demo_bar_comparison():
    """Demo: Animated bar comparison."""
    print("\n📊 Demo 3: Bar Chart Comparison")
    print("-" * 50)

    output = create_animated_bar_comparison(
        categories=["Primary Endpoint", "CV Death", "HF Hospitalization"],
        group1_values=[16.3, 11.6, 10.0],
        group2_values=[21.2, 14.5, 15.6],
        group1_name="Dapagliflozin",
        group2_name="Placebo",
        title="DAPA-HF Trial Results",
        y_label="Event Rate (%)",
    )

    print(f"✅ Created: {output}")
    print("   Use case: Treatment comparisons, before/after")
    return output


def demo_trend_line():
    """Demo: Animated trend line."""
    print("\n📊 Demo 4: Trend Line Over Time")
    print("-" * 50)

    data = {
        "Pre-GDMT": [(1990, 32.5), (1995, 30.2), (2000, 28.1)],
        "GDMT Era": [(2000, 28.1), (2005, 25.3), (2010, 22.8)],
        "SGLT2i Era": [(2010, 22.8), (2015, 19.5), (2020, 16.2), (2024, 14.5)],
    }

    output = create_animated_trend_line(
        data,
        title="Heart Failure Mortality Trends (1990-2024)",
        x_label="Year",
        y_label="Age-Adjusted Mortality (per 100,000)",
    )

    print(f"✅ Created: {output}")
    print("   Use case: Epidemiological trends, longitudinal outcomes")
    return output


def demo_trial_enrollment():
    """Demo: Animated trial enrollment dashboard."""
    print("\n📊 Demo 5: Trial Enrollment Progress")
    print("-" * 50)

    enrollment = [
        ("Month 1", 142),
        ("Month 3", 456),
        ("Month 6", 1024),
        ("Month 9", 2187),
        ("Month 12", 3456),
        ("Month 15", 4320),
        ("Month 18", 4744),
    ]

    output = create_animated_trial_enrollment(
        enrollment,
        target=4744,
        title="DAPA-HF Enrollment Progress",
    )

    print(f"✅ Created: {output}")
    print("   Use case: Trial dashboards, recruitment tracking")
    return output


def main():
    """Run all demos."""
    print("\n" + "=" * 60)
    print("🎬 Vizzu Animated Data Visualizations - Demo Suite")
    print("=" * 60)

    outputs = []

    try:
        outputs.append(demo_kaplan_meier())
        outputs.append(demo_forest_plot())
        outputs.append(demo_bar_comparison())
        outputs.append(demo_trend_line())
        outputs.append(demo_trial_enrollment())

        print("\n" + "=" * 60)
        print("✅ All demos completed successfully!")
        print("=" * 60)

        print("\n📁 Generated Files:")
        for output in outputs:
            print(f"   • {output}")

        print("\n💡 Next Steps:")
        print("   1. Open HTML files in browser to view animations")
        print("   2. Export to video: python vizzu_cli.py export <file.html> --format mp4")
        print("   3. See SKILL.md for full documentation")

    except Exception as e:
        print(f"\n❌ Demo failed: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
