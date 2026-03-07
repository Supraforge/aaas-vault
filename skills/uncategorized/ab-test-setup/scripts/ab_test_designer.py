#!/usr/bin/env python3
"""
A/B Test Designer - Calculates sample size and test duration
"""

import math
import argparse
from scipy import stats

def calculate_sample_size(alpha=0.05, power=0.8, baseline=0.1, mde=0.02):
    """
    Calculate required sample size per variant for A/B test

    Args:
        alpha: Significance level (default 0.05)
        power: Statistical power (default 0.8)
        baseline: Baseline conversion rate (default 0.1)
        mde: Minimum detectable effect (default 0.02)

    Returns:
        Sample size per variant
    """
    # Z-scores
    z_alpha = stats.norm.ppf(1 - alpha/2)  # Two-tailed test
    z_beta = stats.norm.ppf(power)

    # Sample size formula for proportions
    p1 = baseline
    p2 = baseline + mde
    p_bar = (p1 + p2) / 2

    numerator = (z_alpha * math.sqrt(2 * p_bar * (1 - p_bar)) + 
                 z_beta * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    denominator = (p1 - p2) ** 2

    return math.ceil(numerator / denominator)

def main():
    parser = argparse.ArgumentParser(description='A/B Test Sample Size Calculator')
    parser.add_argument('--baseline', type=float, default=0.1, help='Baseline conversion rate')
    parser.add_argument('--mde', type=float, default=0.02, help='Minimum detectable effect')
    parser.add_argument('--alpha', type=float, default=0.05, help='Significance level')
    parser.add_argument('--power', type=float, default=0.8, help='Statistical power')
    parser.add_argument('--traffic', type=float, default=1000, help='Daily traffic per variant')

    args = parser.parse_args()

    sample_size = calculate_sample_size(
        alpha=args.alpha,
        power=args.power,
        baseline=args.baseline,
        mde=args.mde
    )

    days_needed = math.ceil(sample_size / args.traffic)

    print(f"
📊 A/B Test Design Parameters:")
    print(f"   Baseline conversion rate: {args.baseline:.1%}")
    print(f"   Minimum detectable effect: {args.mde:.1%}")
    print(f"   Significance level (alpha): {args.alpha}")
    print(f"   Statistical power: {args.power}")
    print(f"
📈 Results:")
    print(f"   Required sample size per variant: {sample_size:,}")
    print(f"   Total sample size (2 variants): {sample_size * 2:,}")
    print(f"   Days needed (at {args.traffic:,} visitors/day): {days_needed}")
    print(f"
💡 Recommendation: Run test for at least {days_needed} days")

if __name__ == "__main__":
    main()
