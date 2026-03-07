#!/usr/bin/env python3
"""
extract_paper.py - Extract text from research paper PDFs (FREE, runs locally)

NO API COSTS - Just extracts text, then you use Claude Code to structure it.

Usage:
    python extract_paper.py paper.pdf                    # Extract and print
    python extract_paper.py paper.pdf --output text.md   # Save to file
    python extract_paper.py paper.pdf --pages 5          # Just first 5 pages

Then in Claude Code, just say:
    "Read /path/to/text.md and structure this trial data for my content"

ZERO COST - Uses your existing Claude Code subscription.
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime
from typing import Optional

# Try to import PDF library
try:
    import pdfplumber
    HAS_PDFPLUMBER = True
except ImportError:
    HAS_PDFPLUMBER = False


def extract_text(pdf_path: str, max_pages: Optional[int] = None) -> str:
    """Extract text from PDF using pdfplumber (FREE, local)."""
    if not HAS_PDFPLUMBER:
        print("❌ pdfplumber not installed.")
        print("   Run: pip3 install pdfplumber")
        sys.exit(1)

    path = Path(pdf_path)
    if not path.exists():
        print(f"❌ File not found: {pdf_path}")
        sys.exit(1)

    print(f"📄 Extracting: {path.name}")

    try:
        text_parts = []
        with pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)
            pages_to_read = pdf.pages[:max_pages] if max_pages else pdf.pages

            print(f"   Pages: {len(pages_to_read)} of {total_pages}")

            for i, page in enumerate(pages_to_read):
                text = page.extract_text()
                if text:
                    text_parts.append(f"--- PAGE {i+1} ---\n\n{text}")

        if not text_parts:
            print("⚠️  No text extracted (might be a scanned PDF)")
            return ""

        full_text = "\n\n".join(text_parts)
        print(f"   ✅ Extracted {len(full_text):,} characters")
        return full_text

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Extract text from research paper PDFs (FREE, local)"
    )
    parser.add_argument("pdf", help="Path to PDF file")
    parser.add_argument("--output", "-o", help="Save text to file (default: print to screen)")
    parser.add_argument("--pages", "-p", type=int, help="Only extract first N pages")

    args = parser.parse_args()

    # Extract text
    text = extract_text(args.pdf, args.pages)

    if not text:
        sys.exit(1)

    # Add header for context
    header = f"""# Extracted Research Paper

**Source:** {Path(args.pdf).name}
**Extracted:** {datetime.now().strftime("%Y-%m-%d %H:%M")}
**Characters:** {len(text):,}

---

## Instructions for Claude Code

After extracting, tell Claude:

> "Read this paper and extract:
> - Study design, population, intervention
> - Primary/secondary endpoints and results (HR, CI, p-values)
> - Safety data and conclusions
> - Content angles for YouTube, Twitter, Newsletter"

---

"""

    full_output = header + text

    if args.output:
        # Save to file
        output_path = Path(args.output)
        output_path.write_text(full_output, encoding='utf-8')
        print(f"\n💾 Saved to: {output_path}")
        print(f"\n📋 Next step:")
        print(f"   In Claude Code, say: \"Read {output_path} and structure this trial data\"")
    else:
        # Print to screen (truncated preview)
        print("\n" + "=" * 60)
        print("EXTRACTED TEXT (first 2000 chars):")
        print("=" * 60)
        print(text[:2000])
        if len(text) > 2000:
            print(f"\n... [{len(text) - 2000:,} more characters] ...")
        print("=" * 60)
        print("\n💡 Tip: Use --output file.md to save full text")
        print("   Then tell Claude Code: \"Read file.md and structure this trial data\"")


if __name__ == "__main__":
    main()
