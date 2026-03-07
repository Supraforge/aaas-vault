#!/usr/bin/env python3
"""
Carousel Generator for Dr. Shailesh Singh
Generates 1080x1080px Instagram carousel slides from text content

Usage:
    python generate-carousel.py <input_file> <account_number> [options]

    account_number: 1 = @heartdocshailesh, 2 = @dr.shailesh.singh

Part of the Content-OS skill in the Integrated Cowriting System.
"""

import os
import sys
import argparse
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from typing import List, Dict, Tuple

# Get skill directory for relative paths
SKILL_DIR = Path(__file__).parent.parent
KNOWLEDGE_BASE = SKILL_DIR / "knowledge-base"
OUTPUT_DIR = SKILL_DIR / "output"

# Brand color palette
COLORS = {
    'primary': '#207178',      # Deep Teal - titles, CTAs
    'secondary': '#E4F1EF',    # Mist Aqua - backgrounds
    'accent': '#F28C81',       # Warm Coral - icons, highlights
    'neutral_light': '#F8F9FA', # Off-White - alt backgrounds
    'neutral_dark': '#333333',  # Charcoal - body text
    'alert': '#E63946'         # Heart Red - emphasis
}

# Image specifications
SLIDE_SIZE = (1080, 1080)
MARGIN = 80
FOOTER_HEIGHT = 150
CONTENT_WIDTH = SLIDE_SIZE[0] - (2 * MARGIN)
CONTENT_HEIGHT = SLIDE_SIZE[1] - FOOTER_HEIGHT - (2 * MARGIN)

# Account handles
ACCOUNTS = {
    1: "@heartdocshailesh",
    2: "@dr.shailesh.singh"
}


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def load_fonts():
    """Load Inter fonts or fallback to system fonts"""
    fonts = {}

    # Try to load Inter font (download if needed)
    try:
        fonts['title'] = ImageFont.truetype("Inter-Bold.ttf", 60)
        fonts['subtitle'] = ImageFont.truetype("Inter-SemiBold.ttf", 48)
        fonts['body'] = ImageFont.truetype("Inter-Regular.ttf", 36)
        fonts['footer'] = ImageFont.truetype("Inter-Medium.ttf", 28)
        fonts['footer_small'] = ImageFont.truetype("Inter-Regular.ttf", 24)
    except OSError:
        # Fallback to Helvetica/Arial
        try:
            fonts['title'] = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 60)
            fonts['subtitle'] = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
            fonts['body'] = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
            fonts['footer'] = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 28)
            fonts['footer_small'] = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
        except:
            # Final fallback to default
            fonts['title'] = ImageFont.load_default()
            fonts['subtitle'] = ImageFont.load_default()
            fonts['body'] = ImageFont.load_default()
            fonts['footer'] = ImageFont.load_default()
            fonts['footer_small'] = ImageFont.load_default()

    return fonts


def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int, draw: ImageDraw.Draw) -> List[str]:
    """Wrap text to fit within max_width"""
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        width = bbox[2] - bbox[0]

        if width <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line))

    return lines


def parse_content(input_file: str) -> List[Dict[str, str]]:
    """
    Parse input file into slide content
    Supports plain text, JSON, or markdown format
    """
    slides = []

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Try to parse as JSON first
    try:
        data = json.loads(content)
        if isinstance(data, list):
            return data
        elif isinstance(data, dict) and 'slides' in data:
            return data['slides']
    except json.JSONDecodeError:
        pass

    # Parse as plain text with slide separators
    # Format: lines starting with "##" are slide titles
    # Following lines are body text until next "##" or "---"

    lines = content.strip().split('\n')
    current_slide = {'title': '', 'body': '', 'type': 'content'}

    for line in lines:
        line = line.strip()

        if line.startswith('---'):
            if current_slide['title'] or current_slide['body']:
                slides.append(current_slide.copy())
                current_slide = {'title': '', 'body': '', 'type': 'content'}
        elif line.startswith('## '):
            if current_slide['title'] or current_slide['body']:
                slides.append(current_slide.copy())
            current_slide = {'title': line[3:], 'body': '', 'type': 'content'}
        elif line.startswith('# '):
            if current_slide['title'] or current_slide['body']:
                slides.append(current_slide.copy())
            current_slide = {'title': line[2:], 'body': '', 'type': 'title'}
        elif line:
            if current_slide['body']:
                current_slide['body'] += '\n' + line
            else:
                current_slide['body'] = line

    if current_slide['title'] or current_slide['body']:
        slides.append(current_slide)

    # If no structured content found, create a single slide
    if not slides and content.strip():
        slides = [{'title': 'Content', 'body': content.strip(), 'type': 'content'}]

    return slides


def draw_footer(draw: ImageDraw.Draw, fonts: Dict, account: int, photo_path: str = None):
    """Draw footer with profile photo and account handle"""
    footer_y = SLIDE_SIZE[1] - FOOTER_HEIGHT + 20

    # Draw subtle separator line
    line_y = SLIDE_SIZE[1] - FOOTER_HEIGHT
    draw.line([(MARGIN, line_y), (SLIDE_SIZE[0] - MARGIN, line_y)],
              fill=hex_to_rgb(COLORS['secondary']), width=2)

    # Try to load and paste profile photo
    photo_x = MARGIN
    text_x = MARGIN

    if photo_path and os.path.exists(photo_path):
        try:
            photo = Image.open(photo_path)
            photo = photo.resize((100, 100), Image.Resampling.LANCZOS)

            # Create circular mask
            mask = Image.new('L', (100, 100), 0)
            mask_draw = ImageDraw.Draw(mask)
            mask_draw.ellipse([(0, 0), (100, 100)], fill=255)

            # Paste with circular mask
            photo_pos = (photo_x, footer_y)
            # Create a temporary image to paste onto
            temp = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
            temp.paste(photo, (0, 0))

            text_x = photo_x + 120
        except Exception as e:
            print(f"Warning: Could not load profile photo: {e}")
            text_x = MARGIN

    # Draw name and handle
    name_text = "Dr. Shailesh Singh"
    handle_text = ACCOUNTS[account]

    name_y = footer_y + 20
    handle_y = name_y + 35

    draw.text((text_x, name_y), name_text,
              fill=hex_to_rgb(COLORS['neutral_dark']), font=fonts['footer'])
    draw.text((text_x, handle_y), handle_text,
              fill=hex_to_rgb(COLORS['primary']), font=fonts['footer_small'])


def create_title_slide(slide_data: Dict, fonts: Dict, account: int, photo_path: str = None) -> Image.Image:
    """Create opening title slide"""
    img = Image.new('RGB', SLIDE_SIZE, hex_to_rgb(COLORS['primary']))
    draw = ImageDraw.Draw(img)

    # Main title - centered, white text
    title = slide_data.get('title', 'Title')
    title_lines = wrap_text(title, fonts['title'], CONTENT_WIDTH, draw)

    # Calculate vertical centering
    line_height = 80
    total_height = len(title_lines) * line_height
    start_y = (SLIDE_SIZE[1] - total_height) // 2

    for i, line in enumerate(title_lines):
        bbox = draw.textbbox((0, 0), line, font=fonts['title'])
        text_width = bbox[2] - bbox[0]
        x = (SLIDE_SIZE[0] - text_width) // 2
        y = start_y + (i * line_height)
        draw.text((x, y), line, fill=(255, 255, 255), font=fonts['title'])

    # Subtitle if provided
    if slide_data.get('body'):
        subtitle_y = start_y + total_height + 40
        subtitle_lines = wrap_text(slide_data['body'], fonts['body'], CONTENT_WIDTH, draw)
        for i, line in enumerate(subtitle_lines):
            bbox = draw.textbbox((0, 0), line, font=fonts['body'])
            text_width = bbox[2] - bbox[0]
            x = (SLIDE_SIZE[0] - text_width) // 2
            y = subtitle_y + (i * 45)
            draw.text((x, y), line, fill=hex_to_rgb(COLORS['secondary']), font=fonts['body'])

    return img


def create_content_slide(slide_data: Dict, fonts: Dict, account: int, photo_path: str = None) -> Image.Image:
    """Create standard content slide"""
    img = Image.new('RGB', SLIDE_SIZE, hex_to_rgb(COLORS['neutral_light']))
    draw = ImageDraw.Draw(img)

    current_y = MARGIN

    # Draw title
    if slide_data.get('title'):
        title = slide_data['title']
        # Remove bullet points if present
        title = title.lstrip('•- ').strip()

        title_lines = wrap_text(title, fonts['subtitle'], CONTENT_WIDTH, draw)
        for line in title_lines:
            draw.text((MARGIN, current_y), line,
                     fill=hex_to_rgb(COLORS['primary']), font=fonts['subtitle'])
            current_y += 60

        current_y += 20  # Space after title

    # Draw body text
    if slide_data.get('body'):
        body = slide_data['body']

        # Handle bullet points
        body_lines = body.split('\n')
        max_content_y = SLIDE_SIZE[1] - FOOTER_HEIGHT - MARGIN

        for line in body_lines:
            if current_y > max_content_y:
                break

            line = line.strip()
            if not line:
                current_y += 20
                continue

            # Check for bullet points
            is_bullet = line.startswith(('•', '-', '*'))
            if is_bullet:
                line = line.lstrip('•-* ').strip()
                # Draw bullet point
                draw.ellipse([(MARGIN, current_y + 10), (MARGIN + 10, current_y + 20)],
                            fill=hex_to_rgb(COLORS['accent']))
                text_x = MARGIN + 25
            else:
                text_x = MARGIN

            # Wrap and draw text
            wrapped_lines = wrap_text(line, fonts['body'], CONTENT_WIDTH - (25 if is_bullet else 0), draw)
            for wrapped_line in wrapped_lines:
                if current_y > max_content_y:
                    break
                draw.text((text_x, current_y), wrapped_line,
                         fill=hex_to_rgb(COLORS['neutral_dark']), font=fonts['body'])
                current_y += 45

            current_y += 10  # Space between paragraphs

    # Draw footer
    draw_footer(draw, fonts, account, photo_path)

    return img


def generate_carousel(input_file: str, account: int, output_dir: str = None,
                     photo_path: str = None, max_slides: int = 10):
    """
    Main function to generate carousel slides

    Args:
        input_file: Path to input content file
        account: Account number (1 or 2)
        output_dir: Directory to save slides (default: skill output dir)
        photo_path: Path to profile photo
        max_slides: Maximum number of slides to generate
    """

    # Setup output directory
    if output_dir is None:
        base_name = Path(input_file).stem
        output_dir = OUTPUT_DIR / "carousels" / base_name / f"account-{account}"

    os.makedirs(output_dir, exist_ok=True)

    # Default photo path
    if photo_path is None:
        photo_path = KNOWLEDGE_BASE / "brand" / "photo-shailesh.jpg"

    # Load fonts
    fonts = load_fonts()

    # Parse content
    slides_data = parse_content(input_file)

    # Limit slides
    if len(slides_data) > max_slides:
        slides_data = slides_data[:max_slides]
        print(f"Note: Limited to {max_slides} slides")

    print(f"Generating {len(slides_data)} slides for {ACCOUNTS[account]}...")

    # Generate slides
    for i, slide_data in enumerate(slides_data, 1):
        slide_type = slide_data.get('type', 'content')

        if i == 1 or slide_type == 'title':
            img = create_title_slide(slide_data, fonts, account, photo_path)
        else:
            img = create_content_slide(slide_data, fonts, account, photo_path)

        # Save slide
        output_path = os.path.join(output_dir, f"slide-{i:02d}.png")
        img.save(output_path, quality=95)
        print(f"  Created: {output_path}")

    print(f"\nCarousel complete! {len(slides_data)} slides saved to {output_dir}")
    return output_dir


def main():
    parser = argparse.ArgumentParser(
        description='Generate Instagram carousel slides for Dr. Shailesh Singh'
    )
    parser.add_argument('input_file', help='Input content file (text, JSON, or markdown)')
    parser.add_argument('account', type=int, choices=[1, 2],
                       help='Account number: 1=@heartdocshailesh, 2=@dr.shailesh.singh')
    parser.add_argument('-o', '--output', help='Output directory')
    parser.add_argument('-p', '--photo', help='Path to profile photo')
    parser.add_argument('-m', '--max-slides', type=int, default=10,
                       help='Maximum number of slides (default: 10)')

    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"Error: Input file not found: {args.input_file}")
        sys.exit(1)

    try:
        generate_carousel(
            input_file=args.input_file,
            account=args.account,
            output_dir=args.output,
            photo_path=args.photo,
            max_slides=args.max_slides
        )
    except Exception as e:
        print(f"Error generating carousel: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
