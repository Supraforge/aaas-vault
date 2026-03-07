#!/usr/bin/env python3
"""
Quick Topic Researcher - Rapid topic mastery for video/content prep.

Takes a topic → generates 5 research questions → parallel PubMed search →
outputs McKinsey-style brief in 5 minutes.

Usage:
    python quick_research.py --topic "GLP-1 agonists in heart failure" --domain "Cardiology"
    python quick_research.py -t "SGLT2 inhibitors" -d "Cardiology" --output ~/briefs/

Requirements:
    pip install anthropic python-dotenv rich

Environment:
    ANTHROPIC_API_KEY - Claude API key (required)
    NCBI_API_KEY - For PubMed searches (optional, improves rate limits)
"""

import os
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

try:
    from rich.console import Console
    from rich.markdown import Markdown
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    print("Note: Install 'rich' for better output: pip install rich")

# Load environment variables
load_dotenv()

# Import PubMed client
try:
    sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent / "scripts"))
    from pubmed_client import PubMedClient
    PUBMED_CLIENT_AVAILABLE = True
except ImportError:
    PUBMED_CLIENT_AVAILABLE = False

# Initialize console
console = Console() if RICH_AVAILABLE else None

def print_output(text, style=None):
    """Print with or without rich formatting."""
    if RICH_AVAILABLE and console:
        if style:
            console.print(text, style=style)
        else:
            console.print(text)
    else:
        print(text)

def print_markdown(md_text):
    """Print markdown with or without rich formatting."""
    if RICH_AVAILABLE and console:
        console.print(Markdown(md_text))
    else:
        print(md_text)

def generate_research_questions(topic: str, domain: str) -> list:
    """
    Generate 5 specific research questions about the topic.

    In the full implementation, this would call Claude to generate questions.
    For now, returns a template that Claude will customize.
    """
    # These are template questions - Claude will customize them
    question_templates = [
        f"What is the primary clinical evidence for {topic}?",
        f"What are the key randomized controlled trials for {topic}?",
        f"What is the mechanism of action/pathophysiology related to {topic}?",
        f"What are the safety concerns and contraindications for {topic}?",
        f"What do current clinical guidelines (ACC/ESC/ADA) recommend for {topic}?"
    ]
    return question_templates

def create_research_prompt(topic: str, domain: str, questions: list) -> str:
    """Create the prompt for Claude to execute the research."""

    questions_text = "\n".join([f"{i+1}. {q}" for i, q in enumerate(questions)])

    prompt = f"""You are a medical research assistant helping Dr. Shailesh Singh prepare for content creation.

TOPIC: {topic}
DOMAIN: {domain}

RESEARCH QUESTIONS:
{questions_text}

INSTRUCTIONS:

1. For each question, search PubMed using the pubmed_search_articles tool with appropriate queries.
   Execute searches in parallel where possible.

2. For key findings, fetch full article details using pubmed_fetch_contents.

3. Use perplexity_ask for quick context and guideline information (but cite only PubMed sources).

4. Compile findings into a McKinsey-style brief with:
   - Executive Summary (2-3 sentences + key takeaway with PMID)
   - Research Questions & Findings (answer each with evidence)
   - Clinical Context (guidelines + practice implications)
   - Content Hooks (3 angles for video/content)
   - Citation-Ready References (5-7 PMIDs)
   - Gaps & Caveats

OUTPUT FORMAT:
Return the brief in markdown format, ready to display.

Remember:
- CITE only PubMed sources (with PMIDs)
- Include specific stats (HR, CI, p-values) where available
- Focus on what's most relevant for creating content
- Keep it concise - this is a QUICK research brief, not a literature review
"""
    return prompt

def fetch_pubmed_evidence(topic: str, questions: list) -> str:
    """Fetch real PubMed evidence for the topic and questions."""

    if not PUBMED_CLIENT_AVAILABLE:
        return ""

    try:
        client = PubMedClient()
        evidence_text = ""

        # Search for main topic
        print_output("  → Searching PubMed for main topic...", style="yellow")
        articles = client.search_and_fetch(
            query=f"{topic} randomized controlled trial OR meta-analysis",
            max_results=5,
            sort="relevance"
        )

        if articles:
            evidence_text += "\n## PUBMED EVIDENCE (REAL DATA)\n\n"
            evidence_text += f"### Search: {topic}\n\n"
            for article in articles:
                evidence_text += f"**{article.title}**\n"
                evidence_text += f"- PMID: {article.pmid}\n"
                evidence_text += f"- Journal: {article.journal} ({article.pub_date[:4] if article.pub_date else 'N/A'})\n"
                evidence_text += f"- Authors: {', '.join(article.authors[:3])}{', et al.' if len(article.authors) > 3 else ''}\n"
                if article.abstract:
                    evidence_text += f"- Abstract: {article.abstract[:400]}...\n"
                evidence_text += "\n"

        # Search for guidelines
        print_output("  → Searching PubMed for guidelines...", style="yellow")
        guideline_articles = client.search_and_fetch(
            query=f"{topic} guideline OR practice recommendation",
            max_results=3,
            sort="pub_date"
        )

        if guideline_articles:
            evidence_text += "\n### Guidelines Found:\n\n"
            for article in guideline_articles:
                evidence_text += f"- **{article.title}** (PMID: {article.pmid})\n"
                evidence_text += f"  {article.journal}, {article.pub_date[:4] if article.pub_date else 'N/A'}\n\n"

        return evidence_text

    except Exception as e:
        print_output(f"  ⚠️  PubMed search error: {e}", style="yellow")
        return ""


def run_research_with_claude(topic: str, domain: str, questions: list) -> str:
    """
    Execute the research using Claude API with real PubMed data.
    """
    try:
        import anthropic

        client = anthropic.Anthropic()

        # First, fetch real PubMed evidence
        pubmed_evidence = ""
        if PUBMED_CLIENT_AVAILABLE:
            print_output("\nStep 2a: Fetching real PubMed evidence...", style="yellow")
            pubmed_evidence = fetch_pubmed_evidence(topic, questions)
            if pubmed_evidence:
                print_output("  ✓ PubMed evidence retrieved", style="green")
            else:
                print_output("  ⚠️  No PubMed evidence found, using Claude's knowledge", style="yellow")

        prompt = create_research_prompt(topic, domain, questions)

        # Add real PubMed evidence if available
        if pubmed_evidence:
            prompt += f"\n\n---\n\nHere is REAL PubMed evidence I retrieved. Use these PMIDs and findings in your brief:\n{pubmed_evidence}\n\nIMPORTANT: Cite the PMIDs provided above. These are real, verified references."
        else:
            prompt += "\n\nNote: PubMed API was not available. Provide your best research based on your knowledge, and include realistic PMIDs where possible. Flag that user should verify."

        print_output("\nStep 2b: Synthesizing with Claude...", style="yellow")
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return message.content[0].text

    except ImportError:
        return generate_manual_research_template(topic, domain, questions)
    except Exception as e:
        print_output(f"Error calling Claude API: {e}", style="red")
        return generate_manual_research_template(topic, domain, questions)

def generate_manual_research_template(topic: str, domain: str, questions: list) -> str:
    """Generate a template when API is not available."""

    questions_md = "\n\n".join([
        f"### Q{i+1}: {q}\n**Answer:** [Research needed]\n**Evidence:** [PMID needed]\n**PubMed Query:** `{topic} {q.split()[-1]} RCT`"
        for i, q in enumerate(questions)
    ])

    template = f"""# Quick Research Brief: {topic}

**Domain:** {domain}
**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M")}
**Status:** Template - requires PubMed verification

---

## Executive Summary

[To be filled after PubMed research]

Key takeaway: [ONE sentence with strongest PMID]

---

## Research Questions & Findings

{questions_md}

---

## Suggested PubMed Searches

Run these in Claude Code with PubMed MCP:

```
pubmed_search_articles(queryTerm="{topic} randomized controlled trial", maxResults=10)
pubmed_search_articles(queryTerm="{topic} meta-analysis", maxResults=5)
pubmed_search_articles(queryTerm="{topic} guidelines", maxResults=5)
```

---

## Clinical Context

### What Guidelines Say
[ACC/ESC/ADA recommendations - verify at guidelines sites]

### Practice Implications
[To be filled]

---

## Content Hooks

1. [Potential hook based on topic]
2. [Potential hook based on controversy/newness]
3. [Potential hook based on patient impact]

---

## Citation-Ready References

[To be filled with 5-7 PMIDs after research]

---

## Next Steps

1. Open Claude Code with PubMed MCP access
2. Run: "Use quick-topic-researcher for {topic} in {domain}"
3. Claude will execute the PubMed searches and fill this template

---

*Template generated by quick-topic-researcher CLI*
"""
    return template

def save_brief(brief: str, topic: str, output_dir: str = None) -> str:
    """Save the research brief to a file."""

    if output_dir is None:
        output_dir = os.path.expanduser("~/research_briefs")

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Clean topic for filename
    safe_topic = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in topic)
    safe_topic = safe_topic.replace(' ', '_')[:50]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"{safe_topic}_{timestamp}.md"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, 'w') as f:
        f.write(brief)

    return filepath

def main():
    parser = argparse.ArgumentParser(
        description="Quick Topic Researcher - Rapid topic mastery for video/content prep"
    )
    parser.add_argument(
        "-t", "--topic",
        required=True,
        help="Research topic (e.g., 'GLP-1 agonists in heart failure')"
    )
    parser.add_argument(
        "-d", "--domain",
        default="Cardiology",
        help="Domain/specialty (default: Cardiology)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output directory for saving the brief (default: ~/research_briefs/)"
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="Don't save the brief to a file"
    )
    parser.add_argument(
        "--questions-only",
        action="store_true",
        help="Only generate research questions, don't execute research"
    )

    args = parser.parse_args()

    # Header
    print_output("\n" + "="*60, style="blue")
    print_output("QUICK TOPIC RESEARCHER", style="bold blue")
    print_output("="*60 + "\n", style="blue")

    print_output(f"Topic: {args.topic}", style="cyan")
    print_output(f"Domain: {args.domain}", style="cyan")
    print_output("")

    # Step 1: Generate research questions
    print_output("Step 1: Generating research questions...", style="yellow")
    questions = generate_research_questions(args.topic, args.domain)

    print_output("\nResearch Questions:", style="bold")
    for i, q in enumerate(questions, 1):
        print_output(f"  {i}. {q}")
    print_output("")

    if args.questions_only:
        print_output("Questions generated. Use --questions-only=false to run full research.", style="green")
        return

    # Step 2: Execute research
    print_output("Step 2: Executing research...", style="yellow")
    print_output("(This may take 30-60 seconds)\n", style="dim")

    brief = run_research_with_claude(args.topic, args.domain, questions)

    # Step 3: Display results
    print_output("\n" + "="*60, style="green")
    print_output("RESEARCH BRIEF", style="bold green")
    print_output("="*60 + "\n", style="green")

    print_markdown(brief)

    # Step 4: Save if requested
    if not args.no_save:
        filepath = save_brief(brief, args.topic, args.output)
        print_output(f"\nBrief saved to: {filepath}", style="green")

    print_output("\n" + "="*60, style="blue")
    print_output("Ready for your content!", style="bold blue")
    print_output("="*60 + "\n", style="blue")

if __name__ == "__main__":
    main()
