#!/usr/bin/env python3
"""
Template Downloader - Download free pitch deck templates from open repositories

Downloads templates from SlidesCarnival, SlidesGo, and other free sources.

Usage:
    python3 download_template.py                    # Interactive selection
    python3 download_template.py --list             # List available templates
    python3 download_template.py --name "business"  # Download matching template

Requirements:
    pip install requests beautifulsoup4
"""

import argparse
import sys
from pathlib import Path

# Template sources and their direct download links
# These are curated, reliably available templates
TEMPLATES = {
    "startup-pitch-minimal": {
        "name": "Startup Pitch (Minimal)",
        "description": "Clean, minimal design perfect for tech startups",
        "source": "SlidesCarnival",
        "license": "CC BY 4.0",
        "style": "minimal",
        "url": "https://www.slidescarnival.com/category/pitch-deck",
        "download_instructions": "Visit URL, click template, download PPTX",
    },
    "business-blue": {
        "name": "Business Blue Professional",
        "description": "Traditional blue corporate style",
        "source": "PresentationGO",
        "license": "Free",
        "style": "corporate",
        "url": "https://www.presentationgo.com/presentation/business-blue/",
        "download_instructions": "Visit URL, click Download PPTX",
    },
    "modern-gradient": {
        "name": "Modern Gradient",
        "description": "Contemporary gradient design for tech companies",
        "source": "SlidesGo",
        "license": "Free with attribution",
        "style": "modern",
        "url": "https://slidesgo.com/theme/startup-pitch-deck",
        "download_instructions": "Visit URL, click Download, select PPTX",
    },
    "creative-startup": {
        "name": "Creative Startup",
        "description": "Colorful, creative design for consumer products",
        "source": "SlidesMania",
        "license": "Free",
        "style": "creative",
        "url": "https://slidesmania.com/free-templates/",
        "download_instructions": "Visit URL, browse templates, download",
    },
    "investor-deck": {
        "name": "Investor Deck Pro",
        "description": "Professional investor presentation template",
        "source": "Pitch.com",
        "license": "Free",
        "style": "professional",
        "url": "https://pitch.com/templates",
        "download_instructions": "Sign up free, browse templates, export to PPTX",
    },
}

# Direct download URLs for specific free templates (when available)
DIRECT_DOWNLOADS = {
    # These would be actual direct download URLs
    # Most template sites require clicking through their site
}


def list_templates():
    """Display available templates."""
    print("\n📋 Available Pitch Deck Templates\n")
    print("=" * 60)
    
    for key, template in TEMPLATES.items():
        print(f"\n🎨 {template['name']}")
        print(f"   ID: {key}")
        print(f"   Style: {template['style']}")
        print(f"   Source: {template['source']} ({template['license']})")
        print(f"   {template['description']}")
    
    print("\n" + "=" * 60)
    print("\n💡 To download, visit the source URLs and follow instructions.")
    print("   Most free templates require manual download from their sites.")


def download_instructions(template_id: str):
    """Show download instructions for a specific template."""
    template = TEMPLATES.get(template_id)
    
    if not template:
        print(f"❌ Template not found: {template_id}")
        print("   Use --list to see available templates")
        return
    
    print(f"\n📥 Download Instructions: {template['name']}")
    print("=" * 50)
    print(f"\n1. Visit: {template['url']}")
    print(f"2. {template['download_instructions']}")
    print(f"3. Save to: skills/pitch-deck-generator/assets/templates/")
    print(f"\n📝 License: {template['license']}")
    if "attribution" in template['license'].lower():
        print("   ⚠️  Attribution required when using this template")


def search_templates(query: str):
    """Search templates by keyword."""
    query = query.lower()
    matches = []
    
    for key, template in TEMPLATES.items():
        searchable = f"{key} {template['name']} {template['description']} {template['style']}".lower()
        if query in searchable:
            matches.append((key, template))
    
    return matches


def interactive_select():
    """Interactive template selection."""
    print("\n🎯 Pitch Deck Template Selector")
    print("=" * 40)
    print("\nWhat style are you looking for?\n")
    
    styles = ["minimal", "corporate", "modern", "creative", "professional"]
    for i, style in enumerate(styles, 1):
        print(f"  {i}. {style.title()}")
    
    choice = input("\nEnter number or search term: ").strip()
    
    if choice.isdigit() and 1 <= int(choice) <= len(styles):
        style = styles[int(choice) - 1]
        matches = search_templates(style)
    else:
        matches = search_templates(choice)
    
    if not matches:
        print("No matching templates found. Showing all:")
        list_templates()
        return
    
    print(f"\n✅ Found {len(matches)} matching template(s):\n")
    for key, template in matches:
        print(f"  📎 {template['name']} ({key})")
        print(f"     {template['description']}")
        print(f"     URL: {template['url']}\n")
    
    if len(matches) == 1:
        download_instructions(matches[0][0])


def main():
    parser = argparse.ArgumentParser(
        description="Download free pitch deck templates"
    )
    parser.add_argument("--list", "-l", action="store_true",
                        help="List all available templates")
    parser.add_argument("--name", "-n", type=str,
                        help="Search/download template by name")
    parser.add_argument("--download", "-d", type=str,
                        help="Get download instructions for template ID")
    
    args = parser.parse_args()
    
    if args.list:
        list_templates()
    elif args.download:
        download_instructions(args.download)
    elif args.name:
        matches = search_templates(args.name)
        if matches:
            print(f"\n✅ Found {len(matches)} match(es):\n")
            for key, template in matches:
                download_instructions(key)
        else:
            print(f"❌ No templates matching '{args.name}'")
            list_templates()
    else:
        interactive_select()


if __name__ == "__main__":
    main()
