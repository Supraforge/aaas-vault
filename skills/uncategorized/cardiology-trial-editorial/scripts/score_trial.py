#!/usr/bin/env python3
"""
Trial importance scoring calculator.

This script takes trial metadata (extracted by LLM from abstract) and calculates
an importance score based on design, sample size, endpoints, topic, and novelty.

Usage:
    python score_trial.py --design large_RCT --sample_size 5000 --endpoints hard_clinical --topic coronary_intervention --novelty high --journal JACC

Output:
    JSON with breakdown of score components and total score
"""

import argparse
import json


def calculate_importance_score(design, sample_size, endpoints, topic, novelty, journal):
    """
    Calculate trial importance score based on multiple factors.
    
    Args:
        design: Study design type
        sample_size: Number of patients (or None)
        endpoints: Type of endpoints
        topic: Clinical topic area
        novelty: Level of novelty
        journal: Journal name
    
    Returns:
        dict: Score breakdown and total
    """
    score_breakdown = {
        "design_score": 0,
        "sample_size_score": 0,
        "endpoints_score": 0,
        "topic_score": 0,
        "novelty_score": 0,
        "venue_score": 0,
        "total_score": 0
    }
    
    # Design weight (5 points max)
    design_scores = {
        "large_RCT": 5,
        "small_RCT": 3,
        "meta_analysis": 3,
        "observational": 1,
        "registry": 1,
        "other": 0
    }
    score_breakdown["design_score"] = design_scores.get(design, 0)
    
    # Sample size weight (3 points max)
    if sample_size is not None:
        if sample_size >= 3000:
            score_breakdown["sample_size_score"] = 3
        elif sample_size >= 1000:
            score_breakdown["sample_size_score"] = 2
        elif sample_size >= 300:
            score_breakdown["sample_size_score"] = 1
    
    # Endpoints weight (3 points max)
    endpoint_scores = {
        "hard_clinical": 3,
        "surrogate": 1,
        "other": 0
    }
    score_breakdown["endpoints_score"] = endpoint_scores.get(endpoints, 0)
    
    # Topic relevance (2 points max)
    high_value_topics = ["coronary_intervention", "structural_intervention", "heart_failure"]
    if topic in high_value_topics:
        score_breakdown["topic_score"] = 2
    
    # Novelty weight (3 points max)
    novelty_scores = {
        "high": 3,
        "moderate": 1,
        "incremental": 0
    }
    score_breakdown["novelty_score"] = novelty_scores.get(novelty, 0)
    
    # Venue bonus (2 points max)
    journal_lower = journal.lower() if journal else ""
    top_journals = ["jacc", "circulation", "european heart journal", "nejm", "jama", "lancet"]
    if any(j in journal_lower for j in top_journals):
        score_breakdown["venue_score"] = 2
    
    # Calculate total
    score_breakdown["total_score"] = sum([
        score_breakdown["design_score"],
        score_breakdown["sample_size_score"],
        score_breakdown["endpoints_score"],
        score_breakdown["topic_score"],
        score_breakdown["novelty_score"],
        score_breakdown["venue_score"]
    ])
    
    return score_breakdown


def get_interpretation(score):
    """Provide interpretation of importance score."""
    if score >= 15:
        return "Likely landmark trial, strong editorial candidate"
    elif score >= 10:
        return "Important contribution, good editorial candidate"
    elif score >= 7:
        return "Moderate interest, editorial if slow news cycle"
    else:
        return "Usually skip unless special circumstances"


def main():
    parser = argparse.ArgumentParser(
        description="Calculate trial importance score",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("--design", required=True,
                       choices=["large_RCT", "small_RCT", "observational", "registry", 
                               "meta_analysis", "case_series", "basic_science", 
                               "review", "editorial", "other"],
                       help="Study design type")
    
    parser.add_argument("--sample_size", type=int, default=None,
                       help="Sample size (number of patients)")
    
    parser.add_argument("--endpoints", required=True,
                       choices=["hard_clinical", "surrogate", "procedural", 
                               "diagnostic", "other"],
                       help="Type of endpoints")
    
    parser.add_argument("--topic", required=True,
                       choices=["coronary_intervention", "structural_intervention", 
                               "EP", "heart_failure", "prevention", "imaging", "other"],
                       help="Clinical topic area")
    
    parser.add_argument("--novelty", required=True,
                       choices=["incremental", "moderate", "high"],
                       help="Level of novelty")
    
    parser.add_argument("--journal", required=True,
                       help="Journal name")
    
    parser.add_argument("--output", choices=["json", "text"], default="text",
                       help="Output format")
    
    args = parser.parse_args()
    
    # Calculate score
    score_breakdown = calculate_importance_score(
        design=args.design,
        sample_size=args.sample_size,
        endpoints=args.endpoints,
        topic=args.topic,
        novelty=args.novelty,
        journal=args.journal
    )
    
    # Add interpretation
    score_breakdown["interpretation"] = get_interpretation(score_breakdown["total_score"])
    
    # Output
    if args.output == "json":
        print(json.dumps(score_breakdown, indent=2))
    else:
        print(f"\nTrial Importance Score Breakdown:")
        print(f"{'='*50}")
        print(f"Design ({args.design}): {score_breakdown['design_score']}/5")
        print(f"Sample Size ({args.sample_size or 'N/A'}): {score_breakdown['sample_size_score']}/3")
        print(f"Endpoints ({args.endpoints}): {score_breakdown['endpoints_score']}/3")
        print(f"Topic ({args.topic}): {score_breakdown['topic_score']}/2")
        print(f"Novelty ({args.novelty}): {score_breakdown['novelty_score']}/3")
        print(f"Venue ({args.journal}): {score_breakdown['venue_score']}/2")
        print(f"{'='*50}")
        print(f"TOTAL SCORE: {score_breakdown['total_score']}/18")
        print(f"\nInterpretation: {score_breakdown['interpretation']}")
        print()


if __name__ == "__main__":
    main()
