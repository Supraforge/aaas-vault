#!/usr/bin/env python3
"""
Ensemble Content Scorer - Multi-model consensus scoring for content ideas.

Scores content ideas using Claude, GPT-4o, and Gemini in parallel,
then aggregates for a balanced verdict.

Usage:
    python score_content.py --idea "Statins myth-busting for Indian audience"
    python score_content.py --ideas "GLP-1 explained" "Statin myths" "CAC scoring"
    python score_content.py --idea "Topic" --models claude,gpt4o,gemini
"""

import argparse
import asyncio
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from typing import Optional, List

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.markdown import Markdown
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

from dotenv import load_dotenv

# Load environment variables
env_path = Path(__file__).parent.parent.parent.parent.parent / ".env"
if env_path.exists():
    load_dotenv(env_path)

# Scoring prompt template
SCORING_PROMPT = """You are a content strategist helping Dr. Shailesh Singh, an interventional cardiologist
who creates Hinglish YouTube content (70% Hindi, 30% English) about cardiology for Indian audience.

Score this content idea on 6 dimensions (1-10 each):

CONTENT IDEA: {idea}

SCORING DIMENSIONS:
1. RELEVANCE (1-10): How relevant to target audience (Indian patients and doctors)?
2. NOVELTY (1-10): How fresh is the angle? Has this been covered extensively before?
3. EXPERTISE MATCH (1-10): Does it match his expertise as an interventional cardiologist?
4. ENGAGEMENT POTENTIAL (1-10): Will it capture and hold attention?
5. SHAREABILITY (1-10): Will people share this? Is there controversy potential?
6. EVERGREEN FACTOR (1-10): Will this be relevant in 6+ months?

Respond in this exact JSON format:
{{
    "relevance": {{"score": X, "reasoning": "brief explanation"}},
    "novelty": {{"score": X, "reasoning": "brief explanation"}},
    "expertise": {{"score": X, "reasoning": "brief explanation"}},
    "engagement": {{"score": X, "reasoning": "brief explanation"}},
    "shareability": {{"score": X, "reasoning": "brief explanation"}},
    "evergreen": {{"score": X, "reasoning": "brief explanation"}},
    "total": X,
    "verdict": "one line summary",
    "suggestions": ["suggestion 1", "suggestion 2"]
}}

Be critical and honest. Not every idea is a winner.
"""


class EnsembleContentScorer:
    """Score content ideas using multiple AI models."""

    def __init__(self):
        self.console = Console() if RICH_AVAILABLE else None
        self.models = {}
        self._init_clients()

    def _init_clients(self):
        """Initialize available model clients."""

        # Claude (Anthropic)
        if os.getenv("ANTHROPIC_API_KEY"):
            try:
                from anthropic import Anthropic
                self.models["claude"] = {
                    "name": "Claude Sonnet",
                    "provider": "Anthropic",
                    "client": Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
                }
            except ImportError:
                pass

        # GPT-4o (OpenAI)
        if os.getenv("OPENAI_API_KEY"):
            try:
                from openai import OpenAI
                self.models["gpt4o"] = {
                    "name": "GPT-4o",
                    "provider": "OpenAI",
                    "client": OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
                }
            except ImportError:
                pass

        # Gemini (Google)
        if os.getenv("GOOGLE_API_KEY"):
            try:
                import google.generativeai as genai
                genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
                self.models["gemini"] = {
                    "name": "Gemini Pro",
                    "provider": "Google",
                    "client": genai.GenerativeModel('gemini-pro')
                }
            except ImportError:
                pass

        if not self.models:
            print("ERROR: No model API keys found. Need at least ANTHROPIC_API_KEY.")
            sys.exit(1)

    def _print(self, message: str, style: str = None):
        """Print with optional rich formatting."""
        if RICH_AVAILABLE and self.console:
            self.console.print(message, style=style)
        else:
            print(message)

    def _print_panel(self, content: str, title: str):
        """Print content in a panel."""
        if RICH_AVAILABLE and self.console:
            self.console.print(Panel(Markdown(content), title=title))
        else:
            print(f"\n{'='*60}")
            print(f"  {title}")
            print('='*60)
            print(content)
            print('='*60 + "\n")

    def _score_with_claude(self, idea: str) -> dict:
        """Score idea with Claude."""
        try:
            client = self.models["claude"]["client"]
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1000,
                messages=[{"role": "user", "content": SCORING_PROMPT.format(idea=idea)}]
            )
            content = response.content[0].text
            # Extract JSON
            start = content.find('{')
            end = content.rfind('}') + 1
            if start != -1 and end > start:
                result = json.loads(content[start:end])
                result["model"] = "claude"
                result["model_name"] = "Claude Sonnet"
                return result
        except Exception as e:
            return {"error": str(e), "model": "claude", "model_name": "Claude Sonnet"}

        return {"error": "Failed to parse", "model": "claude", "model_name": "Claude Sonnet"}

    def _score_with_gpt4o(self, idea: str) -> dict:
        """Score idea with GPT-4o."""
        try:
            client = self.models["gpt4o"]["client"]
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": SCORING_PROMPT.format(idea=idea)}],
                max_tokens=1000
            )
            content = response.choices[0].message.content
            # Extract JSON
            start = content.find('{')
            end = content.rfind('}') + 1
            if start != -1 and end > start:
                result = json.loads(content[start:end])
                result["model"] = "gpt4o"
                result["model_name"] = "GPT-4o"
                return result
        except Exception as e:
            return {"error": str(e), "model": "gpt4o", "model_name": "GPT-4o"}

        return {"error": "Failed to parse", "model": "gpt4o", "model_name": "GPT-4o"}

    def _score_with_gemini(self, idea: str) -> dict:
        """Score idea with Gemini."""
        try:
            model = self.models["gemini"]["client"]
            response = model.generate_content(SCORING_PROMPT.format(idea=idea))
            content = response.text
            # Extract JSON
            start = content.find('{')
            end = content.rfind('}') + 1
            if start != -1 and end > start:
                result = json.loads(content[start:end])
                result["model"] = "gemini"
                result["model_name"] = "Gemini Pro"
                return result
        except Exception as e:
            return {"error": str(e), "model": "gemini", "model_name": "Gemini Pro"}

        return {"error": "Failed to parse", "model": "gemini", "model_name": "Gemini Pro"}

    def score_idea(self, idea: str, models: List[str] = None) -> dict:
        """Score a content idea with multiple models in parallel."""

        if models is None:
            models = list(self.models.keys())

        self._print(f"\nScoring: {idea}", "cyan bold")
        self._print(f"Models: {', '.join(models)}", "yellow")
        self._print("=" * 50)

        # Map model names to scoring functions
        score_functions = {
            "claude": self._score_with_claude,
            "gpt4o": self._score_with_gpt4o,
            "gemini": self._score_with_gemini
        }

        results = []

        # Execute scoring in parallel
        with ThreadPoolExecutor(max_workers=len(models)) as executor:
            futures = {}
            for model in models:
                if model in score_functions and model in self.models:
                    self._print(f"  → Scoring with {self.models[model]['name']}...", "yellow")
                    futures[executor.submit(score_functions[model], idea)] = model

            for future in as_completed(futures):
                model = futures[future]
                try:
                    result = future.result()
                    if "error" not in result:
                        results.append(result)
                        self._print(f"  ✓ {model} complete (Score: {result.get('total', 'N/A')}/60)", "green")
                    else:
                        self._print(f"  ✗ {model} error: {result['error']}", "red")
                except Exception as e:
                    self._print(f"  ✗ {model} failed: {e}", "red")

        return {
            "idea": idea,
            "timestamp": datetime.now().isoformat(),
            "results": results
        }

    def aggregate_scores(self, scoring_result: dict) -> str:
        """Aggregate individual model scores into consensus verdict."""

        results = scoring_result.get("results", [])
        idea = scoring_result.get("idea", "Unknown")

        if not results:
            return "ERROR: No valid scores received from any model."

        # Calculate averages
        totals = [r.get("total", 0) for r in results if "total" in r]
        avg_total = sum(totals) / len(totals) if totals else 0

        import statistics
        std_dev = statistics.stdev(totals) if len(totals) > 1 else 0

        # Determine verdict
        if avg_total >= 50:
            verdict = "🟢 STRONG PURSUE"
            action = "High priority, create immediately"
        elif avg_total >= 40:
            verdict = "🟡 WORTH PURSUING"
            action = "Good idea, add to calendar"
        elif avg_total >= 30:
            verdict = "🟠 NEEDS REFINEMENT"
            action = "Has potential, needs angle work"
        elif avg_total >= 20:
            verdict = "🔴 RECONSIDER"
            action = "Weak idea, low priority"
        else:
            verdict = "⛔ SKIP"
            action = "Not worth the effort"

        # Consensus interpretation
        if std_dev < 3:
            consensus = "High consensus - models agree"
        elif std_dev < 5:
            consensus = "Moderate consensus - some disagreement"
        else:
            consensus = "Low consensus - divisive idea (may be worth exploring!)"

        # Build report
        report = f"""# ENSEMBLE CONTENT SCORE

**Idea:** {idea}

**Date:** {datetime.now().strftime("%Y-%m-%d %H:%M")}

---

## INDIVIDUAL MODEL SCORES

"""

        for result in results:
            model_name = result.get("model_name", result.get("model", "Unknown"))
            report += f"### {model_name}\n\n"
            report += "| Dimension | Score | Reasoning |\n"
            report += "|-----------|-------|------------|\n"

            for dim in ["relevance", "novelty", "expertise", "engagement", "shareability", "evergreen"]:
                if dim in result:
                    score = result[dim].get("score", "N/A")
                    reasoning = result[dim].get("reasoning", "No reasoning")
                    report += f"| {dim.capitalize()} | {score}/10 | {reasoning} |\n"

            report += f"| **Total** | **{result.get('total', 'N/A')}/60** | |\n\n"
            report += f"**Verdict:** {result.get('verdict', 'No verdict')}\n\n"

            if result.get("suggestions"):
                report += "**Suggestions:**\n"
                for sugg in result.get("suggestions", []):
                    report += f"- {sugg}\n"
                report += "\n"

        # Consensus section
        report += f"""---

## CONSENSUS SCORE

| Model | Total Score |
|-------|-------------|
"""
        for result in results:
            report += f"| {result.get('model_name', 'Unknown')} | {result.get('total', 'N/A')}/60 |\n"

        report += f"""| **Average** | **{avg_total:.1f}/60 ({(avg_total/60*100):.1f}%)** |
| **Std Dev** | {std_dev:.1f} ({consensus}) |

---

## VERDICT

{verdict}

**Score:** {avg_total:.1f}/60
**Action:** {action}

---

## RECOMMENDATIONS

Based on consensus analysis:

"""
        # Aggregate suggestions
        all_suggestions = []
        for result in results:
            all_suggestions.extend(result.get("suggestions", []))

        # Deduplicate and list
        unique_suggestions = list(set(all_suggestions))[:5]
        for i, sugg in enumerate(unique_suggestions, 1):
            report += f"{i}. {sugg}\n"

        return report

    def score_batch(self, ideas: List[str], models: List[str] = None) -> str:
        """Score multiple ideas and rank them."""

        self._print(f"\nBatch scoring {len(ideas)} ideas...\n", "cyan bold")

        all_results = []
        for idea in ideas:
            result = self.score_idea(idea, models)
            totals = [r.get("total", 0) for r in result.get("results", []) if "total" in r]
            avg = sum(totals) / len(totals) if totals else 0
            all_results.append((idea, avg))

        # Sort by score
        all_results.sort(key=lambda x: x[1], reverse=True)

        # Build ranking table
        report = "# BATCH CONTENT SCORING\n\n"
        report += f"**Ideas scored:** {len(ideas)}\n"
        report += f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        report += "| Rank | Idea | Score | Verdict |\n"
        report += "|------|------|-------|--------|\n"

        for i, (idea, score) in enumerate(all_results, 1):
            if score >= 50:
                verdict = "🟢 STRONG"
            elif score >= 40:
                verdict = "🟡 GOOD"
            elif score >= 30:
                verdict = "🟠 REFINE"
            else:
                verdict = "🔴 SKIP"

            # Truncate long ideas
            display_idea = idea[:50] + "..." if len(idea) > 50 else idea
            report += f"| {i} | {display_idea} | {score:.1f}/60 | {verdict} |\n"

        report += "\n---\n\n**Recommendation:** Focus on the top-ranked ideas first.\n"

        return report


def main():
    parser = argparse.ArgumentParser(
        description="Score content ideas using multiple AI models"
    )

    parser.add_argument(
        "--idea", "-i",
        type=str,
        help="Single content idea to score"
    )

    parser.add_argument(
        "--ideas",
        type=str,
        nargs="+",
        help="Multiple ideas to score and rank"
    )

    parser.add_argument(
        "--models", "-m",
        type=str,
        default="claude,gpt4o,gemini",
        help="Comma-separated list of models: claude,gpt4o,gemini"
    )

    parser.add_argument(
        "--output", "-o",
        type=str,
        help="Output directory for report"
    )

    args = parser.parse_args()

    scorer = EnsembleContentScorer()

    # Show available models
    print("\nAvailable Models:")
    for model_id, info in scorer.models.items():
        print(f"  ✓ {info['name']} ({info['provider']})")
    print()

    # Parse models
    models = [m.strip().lower() for m in args.models.split(",")]

    # Run scoring
    if args.idea:
        result = scorer.score_idea(args.idea, models)
        report = scorer.aggregate_scores(result)
        scorer._print_panel(report, "ENSEMBLE CONTENT SCORE")
    elif args.ideas:
        report = scorer.score_batch(args.ideas, models)
        scorer._print_panel(report, "BATCH CONTENT SCORING")
    else:
        parser.print_help()
        return

    # Save to file if output specified
    if args.output and (args.idea or args.ideas):
        output_dir = Path(args.output)
        output_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"content_score_{timestamp}.md"
        output_path = output_dir / filename

        with open(output_path, "w") as f:
            f.write(report)

        print(f"\nReport saved to: {output_path}")


if __name__ == "__main__":
    main()
