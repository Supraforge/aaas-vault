#!/usr/bin/env python3
"""
Content SEO Optimizer - Three-agent SEO audit pipeline.

Scrapes your content → analyzes SERP competitors → generates prioritized
optimization report with P0/P1/P2 recommendations.

Usage:
    python seo_audit.py --url "https://yoursite.com/article"
    python seo_audit.py -u "https://yoursite.com/article" --keyword "statins"

Requirements:
    pip install anthropic python-dotenv rich requests beautifulsoup4

Optional (for better scraping):
    pip install firecrawl-py
"""

import os
import sys
import re
import json
import argparse
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
from dotenv import load_dotenv

try:
    import requests
    from bs4 import BeautifulSoup
    SCRAPING_AVAILABLE = True
except ImportError:
    SCRAPING_AVAILABLE = False

try:
    from rich.console import Console
    from rich.markdown import Markdown
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

# Load environment variables
load_dotenv()

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


def scrape_page(url: str) -> dict:
    """
    Scrape a webpage and extract SEO-relevant elements.

    Returns a dict with title, meta_description, headings, word_count, links, etc.
    """
    if not SCRAPING_AVAILABLE:
        return {
            "error": "requests/beautifulsoup4 not installed",
            "url": url,
            "title": "[Could not scrape - install requests beautifulsoup4]",
            "meta_description": "",
            "h1": "",
            "headings": [],
            "word_count": 0,
            "internal_links": 0,
            "external_links": 0,
            "content_preview": ""
        }

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract title
        title_tag = soup.find('title')
        title = title_tag.get_text().strip() if title_tag else ""

        # Extract meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        meta_description = meta_desc.get('content', '').strip() if meta_desc else ""

        # Extract H1
        h1_tag = soup.find('h1')
        h1 = h1_tag.get_text().strip() if h1_tag else ""

        # Extract all headings
        headings = []
        for tag in ['h1', 'h2', 'h3', 'h4']:
            for heading in soup.find_all(tag):
                headings.append({
                    "tag": tag,
                    "text": heading.get_text().strip()[:100]
                })

        # Count words in main content
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.decompose()

        text = soup.get_text()
        words = text.split()
        word_count = len(words)

        # Count links
        parsed_url = urlparse(url)
        base_domain = parsed_url.netloc

        internal_links = 0
        external_links = 0

        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('http'):
                link_domain = urlparse(href).netloc
                if base_domain in link_domain:
                    internal_links += 1
                else:
                    external_links += 1
            elif href.startswith('/'):
                internal_links += 1

        # Content preview (first 500 chars)
        content_preview = ' '.join(words[:100])

        return {
            "url": url,
            "title": title,
            "title_length": len(title),
            "meta_description": meta_description,
            "meta_description_length": len(meta_description),
            "h1": h1,
            "headings": headings,
            "heading_count": {
                "h1": len([h for h in headings if h["tag"] == "h1"]),
                "h2": len([h for h in headings if h["tag"] == "h2"]),
                "h3": len([h for h in headings if h["tag"] == "h3"]),
                "h4": len([h for h in headings if h["tag"] == "h4"]),
            },
            "word_count": word_count,
            "internal_links": internal_links,
            "external_links": external_links,
            "content_preview": content_preview
        }

    except Exception as e:
        return {
            "error": str(e),
            "url": url,
            "title": "",
            "meta_description": "",
            "h1": "",
            "headings": [],
            "word_count": 0,
            "internal_links": 0,
            "external_links": 0,
            "content_preview": ""
        }


def infer_primary_keyword(page_data: dict) -> str:
    """Infer the primary keyword from page data."""
    # Combine title, h1, and meta for keyword inference
    text = f"{page_data.get('title', '')} {page_data.get('h1', '')} {page_data.get('meta_description', '')}"

    # Simple keyword extraction - in production, use TF-IDF or Claude
    words = text.lower().split()

    # Filter common words
    stop_words = {'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been',
                  'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
                  'would', 'could', 'should', 'may', 'might', 'must', 'shall',
                  'can', 'to', 'of', 'in', 'for', 'on', 'with', 'at', 'by',
                  'from', 'as', 'into', 'through', 'during', 'before', 'after',
                  'above', 'below', 'between', 'under', 'again', 'further',
                  'then', 'once', 'here', 'there', 'when', 'where', 'why',
                  'how', 'all', 'each', 'few', 'more', 'most', 'other', 'some',
                  'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so',
                  'than', 'too', 'very', 'just', 'and', 'but', 'if', 'or',
                  'because', 'until', 'while', 'about', 'against', 'what',
                  'which', 'who', 'whom', 'this', 'that', 'these', 'those',
                  'am', 'your', 'you', 'my', 'me', 'we', 'our', 'us', 'it',
                  'its', 'they', 'them', 'their', '-', '|', '–', '—'}

    filtered = [w for w in words if w not in stop_words and len(w) > 2]

    # Get most common 2-3 word phrase
    if len(filtered) >= 2:
        return ' '.join(filtered[:3])
    elif filtered:
        return filtered[0]
    else:
        return "content optimization"


def generate_audit_prompt(page_data: dict, primary_keyword: str) -> str:
    """Generate the prompt for Claude to create the SEO audit report."""

    headings_text = "\n".join([f"  - {h['tag'].upper()}: {h['text']}" for h in page_data.get('headings', [])[:15]])

    prompt = f"""You are an expert SEO consultant creating an audit report for medical/cardiology content.

PAGE DATA:
- URL: {page_data.get('url', 'Unknown')}
- Title: {page_data.get('title', 'Missing')} ({page_data.get('title_length', 0)} chars)
- Meta Description: {page_data.get('meta_description', 'MISSING')} ({page_data.get('meta_description_length', 0)} chars)
- H1: {page_data.get('h1', 'Missing')}
- Headings Structure:
{headings_text}
- Word Count: {page_data.get('word_count', 0)}
- Internal Links: {page_data.get('internal_links', 0)}
- External Links: {page_data.get('external_links', 0)}

INFERRED PRIMARY KEYWORD: {primary_keyword}

TASK: Generate a comprehensive SEO audit report with:

1. **Executive Summary** (2-3 paragraphs)
   - Overall assessment
   - Key strengths and weaknesses
   - Quick wins available

2. **Technical & On-Page Findings**
   - Title tag analysis + recommendation
   - Meta description analysis + recommendation
   - Heading structure analysis
   - Word count vs competitor benchmarks (medical content: 1,500-2,500 words)
   - Link profile assessment

3. **Keyword Analysis**
   - Primary keyword assessment
   - Secondary keyword suggestions (medical/cardiology focused)
   - Search intent analysis

4. **Competitive Insights**
   - What top-ranking medical content typically includes
   - Common patterns in successful health content
   - Differentiation opportunities for a cardiologist

5. **Prioritized Recommendations**
   - P0 (Critical - do this week): 2-3 items
   - P1 (Important - do this month): 3-4 items
   - P2 (Nice to have): 2-3 items

   For each recommendation include:
   - Specific action
   - Rationale (reference the data)
   - Expected impact (High/Medium/Low)
   - Effort required (Low/Medium/High)

6. **Next Steps**
   - Measurement plan
   - Timeline suggestions

FORMAT: Return as clean Markdown, starting with "# SEO Audit Report"

MEDICAL CONTENT CONTEXT:
- This is for a cardiologist's content
- Authority signals (MD, cardiologist) are important
- Citing medical studies (PMIDs) adds credibility
- Accuracy trumps virality for medical content
- Consider E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)
"""
    return prompt


def run_seo_audit_with_claude(page_data: dict, primary_keyword: str) -> str:
    """Execute the SEO audit using Claude API."""
    try:
        import anthropic

        client = anthropic.Anthropic()
        prompt = generate_audit_prompt(page_data, primary_keyword)

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
        return generate_manual_audit_template(page_data, primary_keyword)
    except Exception as e:
        print_output(f"Error calling Claude API: {e}", style="red")
        return generate_manual_audit_template(page_data, primary_keyword)


def generate_manual_audit_template(page_data: dict, primary_keyword: str) -> str:
    """Generate a template when API is not available."""

    template = f"""# SEO Audit Report

**URL:** {page_data.get('url', 'Unknown')}
**Audit Date:** {datetime.now().strftime("%Y-%m-%d")}
**Primary Keyword:** {primary_keyword}

---

## Page Analysis (Raw Data)

### Title Tag
- **Current:** {page_data.get('title', 'MISSING')}
- **Length:** {page_data.get('title_length', 0)} characters
- **Optimal:** 50-60 characters
- **Status:** {"✅ Good length" if 50 <= page_data.get('title_length', 0) <= 60 else "⚠️ Needs adjustment"}

### Meta Description
- **Current:** {page_data.get('meta_description', 'MISSING') or 'MISSING'}
- **Length:** {page_data.get('meta_description_length', 0)} characters
- **Optimal:** 150-160 characters
- **Status:** {"✅ Present" if page_data.get('meta_description') else "❌ MISSING - Critical issue"}

### Heading Structure
- H1 count: {page_data.get('heading_count', {}).get('h1', 0)} {"✅" if page_data.get('heading_count', {}).get('h1', 0) == 1 else "⚠️"}
- H2 count: {page_data.get('heading_count', {}).get('h2', 0)} {"✅" if page_data.get('heading_count', {}).get('h2', 0) >= 3 else "⚠️ Add more H2s"}
- H3 count: {page_data.get('heading_count', {}).get('h3', 0)}

### Content Depth
- **Word count:** {page_data.get('word_count', 0)}
- **Medical content benchmark:** 1,500-2,500 words
- **Status:** {"✅ Good depth" if page_data.get('word_count', 0) >= 1500 else "⚠️ Consider expanding"}

### Link Profile
- **Internal links:** {page_data.get('internal_links', 0)} {"✅" if page_data.get('internal_links', 0) >= 5 else "⚠️ Add more internal links"}
- **External links:** {page_data.get('external_links', 0)} {"✅" if page_data.get('external_links', 0) >= 2 else "⚠️ Add authoritative sources"}

---

## Quick Wins (P0)

1. {"Add meta description" if not page_data.get('meta_description') else "Optimize meta description"}
2. {"Add more H2 headings" if page_data.get('heading_count', {}).get('h2', 0) < 3 else "Review heading structure"}
3. {"Expand content to 1,500+ words" if page_data.get('word_count', 0) < 1500 else "Optimize for primary keyword"}

---

## Next Steps

For a complete audit with competitor analysis and detailed recommendations:

1. Open Claude Code with web access
2. Run: "Audit SEO for {page_data.get('url', 'your-url')}"
3. Claude will perform SERP analysis and generate full report

---

*Template generated by content-seo-optimizer CLI*
*For full analysis, run in Claude Code with Perplexity/WebSearch access*
"""
    return template


def save_report(report: str, url: str, output_dir: str = None) -> str:
    """Save the SEO audit report to a file."""

    if output_dir is None:
        output_dir = os.path.expanduser("~/seo_audits")

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Clean URL for filename
    parsed = urlparse(url)
    safe_name = f"{parsed.netloc}_{parsed.path}".replace('/', '_').replace('.', '_')[:50]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"seo_audit_{safe_name}_{timestamp}.md"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, 'w') as f:
        f.write(report)

    return filepath


def main():
    parser = argparse.ArgumentParser(
        description="Content SEO Optimizer - Audit your content for search optimization"
    )
    parser.add_argument(
        "-u", "--url",
        required=True,
        help="URL to audit (e.g., https://yoursite.com/article)"
    )
    parser.add_argument(
        "-k", "--keyword",
        help="Primary keyword (optional - will be inferred if not provided)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output directory for saving the report (default: ~/seo_audits/)"
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="Don't save the report to a file"
    )
    parser.add_argument(
        "--scrape-only",
        action="store_true",
        help="Only scrape the page, don't generate full report"
    )

    args = parser.parse_args()

    # Header
    print_output("\n" + "="*60, style="blue")
    print_output("CONTENT SEO OPTIMIZER", style="bold blue")
    print_output("="*60 + "\n", style="blue")

    print_output(f"URL: {args.url}", style="cyan")

    # Step 1: Scrape page
    print_output("\nStep 1: Scraping page...", style="yellow")
    page_data = scrape_page(args.url)

    if page_data.get("error"):
        print_output(f"Warning: {page_data['error']}", style="red")

    print_output(f"  Title: {page_data.get('title', 'N/A')[:60]}...", style="dim")
    print_output(f"  Word count: {page_data.get('word_count', 0)}", style="dim")
    print_output(f"  Headings: H1={page_data.get('heading_count', {}).get('h1', 0)}, "
                 f"H2={page_data.get('heading_count', {}).get('h2', 0)}, "
                 f"H3={page_data.get('heading_count', {}).get('h3', 0)}", style="dim")

    if args.scrape_only:
        print_output("\n" + json.dumps(page_data, indent=2))
        return

    # Step 2: Infer keyword
    primary_keyword = args.keyword or infer_primary_keyword(page_data)
    print_output(f"\nStep 2: Primary keyword: {primary_keyword}", style="yellow")

    # Step 3: Generate report
    print_output("\nStep 3: Generating SEO audit report...", style="yellow")
    print_output("(This may take 30-60 seconds)\n", style="dim")

    report = run_seo_audit_with_claude(page_data, primary_keyword)

    # Step 4: Display results
    print_output("\n" + "="*60, style="green")
    print_output("SEO AUDIT REPORT", style="bold green")
    print_output("="*60 + "\n", style="green")

    print_markdown(report)

    # Step 5: Save if requested
    if not args.no_save:
        filepath = save_report(report, args.url, args.output)
        print_output(f"\nReport saved to: {filepath}", style="green")

    print_output("\n" + "="*60, style="blue")
    print_output("Audit complete!", style="bold blue")
    print_output("="*60 + "\n", style="blue")


if __name__ == "__main__":
    main()
