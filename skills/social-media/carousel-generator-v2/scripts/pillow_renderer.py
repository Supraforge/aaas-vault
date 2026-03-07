"""
Pillow-based slide renderer for Carousel Generator v2

Renders slides using PIL/Pillow with professional design standards.
"""

import os
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
from PIL import Image, ImageDraw, ImageFont
import time

from .models import (
    SlideContent, SlideType, ColorMode, SlideRenderResult,
    CarouselConfig, AspectRatio
)
from .tokens import (
    get_color_rgb, get_color_mode, get_typography,
    get_dimensions, get_spacing, get_footer_specs,
    get_account, get_font_path, get_icon_path,
    hex_to_rgb
)


class PillowRenderer:
    """Render carousel slides using Pillow."""

    def __init__(self, config: CarouselConfig = None):
        self.config = config or CarouselConfig()
        self.fonts = self._load_fonts()
        self.spacing = get_spacing()
        self.photo = self._load_profile_photo()

    def _load_fonts(self) -> Dict[str, ImageFont.FreeTypeFont]:
        """Load Inter font family with fallbacks."""
        fonts = {}
        typography = get_typography()

        font_weights = {
            'headline': ('Bold', typography['headline']['fontSize']),
            'subheadline': ('SemiBold', typography['subheadline']['fontSize']),
            'body': ('Regular', typography['body']['fontSize']),
            'bodyLarge': ('Regular', typography['bodyLarge']['fontSize']),
            'caption': ('Medium', typography['caption']['fontSize']),
            'stat': ('Bold', typography['stat']['fontSize']),
            'statLabel': ('Medium', typography['statLabel']['fontSize']),
        }

        for key, (weight, size) in font_weights.items():
            font_path = get_font_path(weight)
            if font_path and font_path.exists():
                fonts[key] = ImageFont.truetype(str(font_path), size)
            else:
                # Fallback to system font
                try:
                    fonts[key] = ImageFont.truetype(
                        "/System/Library/Fonts/Helvetica.ttc", size
                    )
                except:
                    fonts[key] = ImageFont.load_default()

        return fonts

    def _load_profile_photo(self) -> Optional[Image.Image]:
        """Load profile photo from knowledge base."""
        skill_dir = Path(__file__).parent.parent
        # Check v1 location
        photo_path = skill_dir.parent / "carousel-generator" / "knowledge-base" / "brand" / "photo-shailesh.jpg"

        if photo_path.exists():
            photo = Image.open(photo_path)
            photo = photo.resize((100, 100), Image.Resampling.LANCZOS)
            # Create circular mask
            mask = Image.new('L', (100, 100), 0)
            mask_draw = ImageDraw.Draw(mask)
            mask_draw.ellipse([(0, 0), (100, 100)], fill=255)
            photo.putalpha(mask)
            return photo
        return None

    def _get_dimensions(self) -> Tuple[int, int]:
        """Get slide dimensions based on aspect ratio."""
        dims = get_dimensions(self.config.aspect_ratio.value)
        return dims['width'], dims['height']

    def _get_colors(self, slide: SlideContent) -> Dict[str, Tuple[int, int, int]]:
        """Get color scheme for a slide."""
        mode = slide.color_mode.value if slide.color_mode != ColorMode.AUTO else "light"
        color_scheme = get_color_mode(mode)
        return {k: hex_to_rgb(v) for k, v in color_scheme.items()}

    def _wrap_text(self, text: str, font: ImageFont.FreeTypeFont,
                   max_width: int, draw: ImageDraw.Draw) -> List[str]:
        """Wrap text to fit within max_width."""
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

    def _draw_footer(self, img: Image.Image, draw: ImageDraw.Draw,
                     colors: Dict[str, Tuple[int, int, int]]):
        """Draw footer with profile photo and handle."""
        width, height = img.size
        footer_specs = get_footer_specs()
        account = get_account(self.config.account)

        footer_y = height - footer_specs['height'] + 20

        # Draw separator line
        line_y = height - footer_specs['height']
        draw.line(
            [(self.spacing['margin'], line_y),
             (width - self.spacing['margin'], line_y)],
            fill=colors.get('border', (228, 241, 239)),
            width=2
        )

        # Position text
        text_x = self.spacing['margin']

        # Paste profile photo if available
        if self.photo:
            photo_x = self.spacing['margin']
            img.paste(self.photo, (photo_x, footer_y), self.photo)
            text_x = photo_x + 120

        # Draw name and handle
        name_y = footer_y + 20
        handle_y = name_y + 35

        draw.text(
            (text_x, name_y),
            account['name'],
            fill=colors.get('text', (51, 51, 51)),
            font=self.fonts['caption']
        )
        draw.text(
            (text_x, handle_y),
            account['handle'],
            fill=get_color_rgb('primary'),
            font=self.fonts['caption']
        )

    def _draw_icon(self, draw: ImageDraw.Draw, icon_name: str,
                   x: int, y: int, size: int,
                   color: Tuple[int, int, int]) -> None:
        """Draw a simple icon placeholder (SVG rendering would need cairosvg)."""
        # For now, draw a circle as placeholder
        # Full SVG rendering would require additional dependencies
        half = size // 2
        draw.ellipse(
            [(x, y), (x + size, y + size)],
            fill=color
        )

    def render_hook_slide(self, slide: SlideContent) -> Image.Image:
        """Render a hook/opening slide."""
        width, height = self._get_dimensions()
        colors = self._get_colors(slide)

        # Dark background for hook slides
        bg_color = get_color_rgb('primary')
        img = Image.new('RGB', (width, height), bg_color)
        draw = ImageDraw.Draw(img)

        margin = self.spacing['margin']
        content_width = width - (2 * margin)

        # Main title - centered, white text
        title = slide.title or "Hook Title"
        title_lines = self._wrap_text(title, self.fonts['headline'], content_width, draw)

        line_height = 70
        total_height = len(title_lines) * line_height
        start_y = (height - total_height) // 2 - 50

        for i, line in enumerate(title_lines):
            bbox = draw.textbbox((0, 0), line, font=self.fonts['headline'])
            text_width = bbox[2] - bbox[0]
            x = (width - text_width) // 2
            y = start_y + (i * line_height)
            draw.text((x, y), line, fill=(255, 255, 255), font=self.fonts['headline'])

        # Subtitle if provided
        if slide.subtitle:
            subtitle_y = start_y + total_height + 40
            subtitle_lines = self._wrap_text(slide.subtitle, self.fonts['body'], content_width, draw)
            for i, line in enumerate(subtitle_lines):
                bbox = draw.textbbox((0, 0), line, font=self.fonts['body'])
                text_width = bbox[2] - bbox[0]
                x = (width - text_width) // 2
                y = subtitle_y + (i * 45)
                draw.text((x, y), line, fill=get_color_rgb('secondary'), font=self.fonts['body'])

        return img

    def render_tips_slide(self, slide: SlideContent) -> Image.Image:
        """Render a tips slide with numbered list."""
        width, height = self._get_dimensions()
        colors = self._get_colors(slide)

        img = Image.new('RGB', (width, height), colors['background'])
        draw = ImageDraw.Draw(img)

        margin = self.spacing['margin']
        content_width = width - (2 * margin)
        footer_height = get_footer_specs()['height']

        current_y = margin

        # Title
        if slide.title:
            title_lines = self._wrap_text(slide.title, self.fonts['subheadline'], content_width, draw)
            for line in title_lines:
                draw.text((margin, current_y), line, fill=colors['heading'], font=self.fonts['subheadline'])
                current_y += 55
            current_y += 30

        # Bullet points
        if slide.bullet_points:
            accent_color = get_color_rgb('accent')
            max_y = height - footer_height - margin

            for i, point in enumerate(slide.bullet_points, 1):
                if current_y > max_y:
                    break

                # Draw bullet/number circle
                bullet_size = self.spacing['bulletSize']
                draw.ellipse(
                    [(margin, current_y + 8), (margin + bullet_size, current_y + 8 + bullet_size)],
                    fill=accent_color
                )

                # Draw text
                text_x = margin + 30
                wrapped = self._wrap_text(point, self.fonts['body'], content_width - 30, draw)
                for line in wrapped:
                    if current_y > max_y:
                        break
                    draw.text((text_x, current_y), line, fill=colors['text'], font=self.fonts['body'])
                    current_y += 45
                current_y += 15

        self._draw_footer(img, draw, colors)
        return img

    def render_stats_slide(self, slide: SlideContent) -> Image.Image:
        """Render a statistics slide with big number."""
        width, height = self._get_dimensions()
        colors = self._get_colors(slide)

        img = Image.new('RGB', (width, height), colors['background'])
        draw = ImageDraw.Draw(img)

        margin = self.spacing['margin']
        footer_height = get_footer_specs()['height']

        # Center the stat vertically (accounting for footer)
        content_height = height - footer_height
        center_y = content_height // 2 - 60

        # Big statistic number
        stat = slide.statistic or "85%"
        bbox = draw.textbbox((0, 0), stat, font=self.fonts['stat'])
        stat_width = bbox[2] - bbox[0]
        x = (width - stat_width) // 2
        draw.text((x, center_y), stat, fill=get_color_rgb('primary'), font=self.fonts['stat'])

        # Stat label
        if slide.stat_label:
            label_y = center_y + 90
            bbox = draw.textbbox((0, 0), slide.stat_label, font=self.fonts['subheadline'])
            label_width = bbox[2] - bbox[0]
            x = (width - label_width) // 2
            draw.text((x, label_y), slide.stat_label, fill=colors['text'], font=self.fonts['subheadline'])

        # Context text
        if slide.stat_context:
            context_y = center_y + 160
            context_lines = self._wrap_text(slide.stat_context, self.fonts['body'], width - (2 * margin), draw)
            for line in context_lines:
                bbox = draw.textbbox((0, 0), line, font=self.fonts['body'])
                line_width = bbox[2] - bbox[0]
                x = (width - line_width) // 2
                draw.text((x, context_y), line, fill=colors['textSecondary'], font=self.fonts['body'])
                context_y += 40

        self._draw_footer(img, draw, colors)
        return img

    def render_myth_slide(self, slide: SlideContent) -> Image.Image:
        """Render a myth-busting slide."""
        width, height = self._get_dimensions()
        colors = self._get_colors(slide)

        img = Image.new('RGB', (width, height), colors['background'])
        draw = ImageDraw.Draw(img)

        margin = self.spacing['margin']
        footer_height = get_footer_specs()['height']
        content_width = width - (2 * margin)

        # MYTH section (top half)
        myth_y = margin + 40

        # Myth label
        draw.text((margin, myth_y), "MYTH", fill=get_color_rgb('alert'), font=self.fonts['caption'])
        myth_y += 40

        # Myth text with strikethrough effect
        if slide.myth_text:
            myth_lines = self._wrap_text(slide.myth_text, self.fonts['body'], content_width, draw)
            for line in myth_lines:
                draw.text((margin, myth_y), line, fill=(150, 150, 150), font=self.fonts['body'])
                # Draw strikethrough
                bbox = draw.textbbox((margin, myth_y), line, font=self.fonts['body'])
                line_y = myth_y + 18
                draw.line([(margin, line_y), (bbox[2], line_y)], fill=get_color_rgb('alert'), width=3)
                myth_y += 50

        # Separator line
        sep_y = (height - footer_height) // 2
        draw.line([(margin, sep_y), (width - margin, sep_y)], fill=colors['border'], width=2)

        # TRUTH section (bottom half)
        truth_y = sep_y + 40

        # Truth label
        draw.text((margin, truth_y), "TRUTH", fill=get_color_rgb('primary'), font=self.fonts['caption'])
        truth_y += 40

        # Truth text
        if slide.truth_text:
            truth_lines = self._wrap_text(slide.truth_text, self.fonts['body'], content_width, draw)
            for line in truth_lines:
                draw.text((margin, truth_y), line, fill=colors['text'], font=self.fonts['body'])
                truth_y += 50

        self._draw_footer(img, draw, colors)
        return img

    def render_quote_slide(self, slide: SlideContent) -> Image.Image:
        """Render a quote slide."""
        width, height = self._get_dimensions()

        # Dark background for quotes
        bg_color = get_color_rgb('primary')
        img = Image.new('RGB', (width, height), bg_color)
        draw = ImageDraw.Draw(img)

        margin = self.spacing['margin']
        content_width = width - (2 * margin)
        footer_height = get_footer_specs()['height']

        # Large quote mark
        quote_mark = '"'
        draw.text((margin, margin), quote_mark, fill=get_color_rgb('accent'), font=self.fonts['stat'])

        # Quote text
        quote_y = margin + 100
        if slide.quote_text:
            quote_lines = self._wrap_text(slide.quote_text, self.fonts['bodyLarge'], content_width - 40, draw)
            for line in quote_lines:
                draw.text((margin + 20, quote_y), line, fill=(255, 255, 255), font=self.fonts['bodyLarge'])
                quote_y += 50

        # Author
        if slide.quote_author:
            author_y = height - footer_height - margin - 40
            draw.text((margin + 20, author_y), f"— {slide.quote_author}",
                     fill=get_color_rgb('secondary'), font=self.fonts['caption'])

        return img

    def render_cta_slide(self, slide: SlideContent) -> Image.Image:
        """Render a call-to-action slide."""
        width, height = self._get_dimensions()

        # Dark background for CTAs
        bg_color = get_color_rgb('primary')
        img = Image.new('RGB', (width, height), bg_color)
        draw = ImageDraw.Draw(img)

        margin = self.spacing['margin']

        # CTA text centered
        cta_text = slide.cta_text or "Follow for more"

        bbox = draw.textbbox((0, 0), cta_text, font=self.fonts['headline'])
        text_width = bbox[2] - bbox[0]
        x = (width - text_width) // 2
        y = height // 2 - 60

        draw.text((x, y), cta_text, fill=(255, 255, 255), font=self.fonts['headline'])

        # Handle
        handle = slide.cta_handle or get_account(self.config.account)['handle']
        bbox = draw.textbbox((0, 0), handle, font=self.fonts['subheadline'])
        handle_width = bbox[2] - bbox[0]
        x = (width - handle_width) // 2
        draw.text((x, y + 80), handle, fill=get_color_rgb('accent'), font=self.fonts['subheadline'])

        return img

    def render_steps_slide(self, slide: SlideContent) -> Image.Image:
        """Render a steps/process slide."""
        width, height = self._get_dimensions()
        colors = self._get_colors(slide)

        img = Image.new('RGB', (width, height), colors['background'])
        draw = ImageDraw.Draw(img)

        margin = self.spacing['margin']
        content_width = width - (2 * margin)
        footer_height = get_footer_specs()['height']

        current_y = margin

        # Title
        if slide.title:
            title_lines = self._wrap_text(slide.title, self.fonts['subheadline'], content_width, draw)
            for line in title_lines:
                draw.text((margin, current_y), line, fill=colors['heading'], font=self.fonts['subheadline'])
                current_y += 55
            current_y += 30

        # Steps with numbers and arrows
        if slide.steps:
            max_y = height - footer_height - margin
            accent = get_color_rgb('accent')
            primary = get_color_rgb('primary')

            for i, step in enumerate(slide.steps, 1):
                if current_y > max_y:
                    break

                # Draw number circle
                circle_size = 40
                draw.ellipse(
                    [(margin, current_y), (margin + circle_size, current_y + circle_size)],
                    fill=primary
                )
                # Number
                num_bbox = draw.textbbox((0, 0), str(i), font=self.fonts['caption'])
                num_width = num_bbox[2] - num_bbox[0]
                num_x = margin + (circle_size - num_width) // 2
                num_y = current_y + 8
                draw.text((num_x, num_y), str(i), fill=(255, 255, 255), font=self.fonts['caption'])

                # Step text
                text_x = margin + 60
                wrapped = self._wrap_text(step, self.fonts['body'], content_width - 60, draw)
                for line in wrapped:
                    draw.text((text_x, current_y + 5), line, fill=colors['text'], font=self.fonts['body'])
                    current_y += 45

                # Arrow (except for last step)
                if i < len(slide.steps):
                    arrow_x = margin + 18
                    draw.polygon(
                        [(arrow_x, current_y + 5), (arrow_x - 8, current_y + 20), (arrow_x + 8, current_y + 20)],
                        fill=accent
                    )
                    current_y += 35
                else:
                    current_y += 20

        self._draw_footer(img, draw, colors)
        return img

    def render_comparison_slide(self, slide: SlideContent) -> Image.Image:
        """Render a before/after comparison slide."""
        width, height = self._get_dimensions()
        colors = self._get_colors(slide)

        img = Image.new('RGB', (width, height), colors['background'])
        draw = ImageDraw.Draw(img)

        margin = self.spacing['margin']
        footer_height = get_footer_specs()['height']
        content_height = height - footer_height - (2 * margin)
        half_width = (width - (3 * margin)) // 2

        # Title
        current_y = margin
        if slide.title:
            bbox = draw.textbbox((0, 0), slide.title, font=self.fonts['subheadline'])
            title_width = bbox[2] - bbox[0]
            x = (width - title_width) // 2
            draw.text((x, current_y), slide.title, fill=colors['heading'], font=self.fonts['subheadline'])
            current_y += 70

        # Before section (left)
        before_x = margin
        draw.text((before_x, current_y), "BEFORE", fill=get_color_rgb('alert'), font=self.fonts['caption'])

        if slide.before_text:
            before_lines = self._wrap_text(slide.before_text, self.fonts['body'], half_width, draw)
            before_y = current_y + 40
            for line in before_lines:
                draw.text((before_x, before_y), line, fill=colors['text'], font=self.fonts['body'])
                before_y += 45

        # VS divider
        vs_x = width // 2
        vs_y = current_y + content_height // 3
        draw.text((vs_x - 20, vs_y), "VS", fill=get_color_rgb('accent'), font=self.fonts['subheadline'])

        # After section (right)
        after_x = width // 2 + margin // 2
        draw.text((after_x, current_y), "AFTER", fill=get_color_rgb('primary'), font=self.fonts['caption'])

        if slide.after_text:
            after_lines = self._wrap_text(slide.after_text, self.fonts['body'], half_width, draw)
            after_y = current_y + 40
            for line in after_lines:
                draw.text((after_x, after_y), line, fill=colors['text'], font=self.fonts['body'])
                after_y += 45

        self._draw_footer(img, draw, colors)
        return img

    def render_story_slide(self, slide: SlideContent) -> Image.Image:
        """Render a story/narrative slide."""
        width, height = self._get_dimensions()
        colors = self._get_colors(slide)

        img = Image.new('RGB', (width, height), colors['background'])
        draw = ImageDraw.Draw(img)

        margin = self.spacing['margin']
        content_width = width - (2 * margin)
        footer_height = get_footer_specs()['height']

        current_y = margin

        # Title
        if slide.title:
            title_lines = self._wrap_text(slide.title, self.fonts['subheadline'], content_width, draw)
            for line in title_lines:
                draw.text((margin, current_y), line, fill=colors['heading'], font=self.fonts['subheadline'])
                current_y += 55
            current_y += 20

        # Body text (story narrative)
        if slide.body:
            max_y = height - footer_height - margin
            body_lines = self._wrap_text(slide.body, self.fonts['body'], content_width, draw)
            for line in body_lines:
                if current_y > max_y:
                    break
                draw.text((margin, current_y), line, fill=colors['text'], font=self.fonts['body'])
                current_y += 45

        self._draw_footer(img, draw, colors)
        return img

    def render_data_slide(self, slide: SlideContent) -> Image.Image:
        """Render a data/chart slide (placeholder for Plotly integration)."""
        # For now, render as a stats slide
        # Full implementation would integrate with Plotly
        return self.render_stats_slide(slide)

    def render_slide(self, slide: SlideContent) -> SlideRenderResult:
        """Render a single slide based on its type."""
        start_time = time.time()

        renderers = {
            SlideType.HOOK: self.render_hook_slide,
            SlideType.TIPS: self.render_tips_slide,
            SlideType.STATS: self.render_stats_slide,
            SlideType.COMPARISON: self.render_comparison_slide,
            SlideType.STORY: self.render_story_slide,
            SlideType.DATA: self.render_data_slide,
            SlideType.STEPS: self.render_steps_slide,
            SlideType.MYTH: self.render_myth_slide,
            SlideType.QUOTE: self.render_quote_slide,
            SlideType.CTA: self.render_cta_slide,
        }

        renderer = renderers.get(slide.slide_type, self.render_tips_slide)
        img = renderer(slide)

        # Save to output directory
        output_dir = self.config.output_dir or Path(__file__).parent.parent / "output" / "carousels"
        output_dir.mkdir(parents=True, exist_ok=True)

        filename = f"slide-{slide.slide_number:02d}.png"
        output_path = output_dir / filename
        img.save(str(output_path), quality=95)

        render_time = (time.time() - start_time) * 1000

        return SlideRenderResult(
            slide_number=slide.slide_number,
            output_path=output_path,
            width=img.width,
            height=img.height,
            render_time_ms=render_time,
            renderer_used="pillow"
        )

    def render_carousel(self, slides: List[SlideContent],
                        topic: str = "carousel") -> List[SlideRenderResult]:
        """Render all slides in a carousel."""
        # Set up output directory
        output_dir = self.config.output_dir or (
            Path(__file__).parent.parent / "output" / "carousels" / topic.replace(" ", "-")
        )
        output_dir.mkdir(parents=True, exist_ok=True)
        self.config.output_dir = output_dir

        results = []
        for i, slide in enumerate(slides, 1):
            slide.slide_number = i
            result = self.render_slide(slide)
            results.append(result)
            print(f"  Rendered slide {i}/{len(slides)}: {result.output_path.name}")

        return results
