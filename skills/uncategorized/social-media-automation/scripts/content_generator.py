#!/usr/bin/env python3
"""
AI Content Generator for Social Media
Generates posts, images, and videos using various AI models
"""

import os
import sys
import json
import random
from typing import Dict, List, Any, Optional
import logging
from dotenv import load_dotenv

# Add scripts directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.utils import setup_logging, load_config

class ContentGenerator:
    """Generates social media content using AI"""

    def __init__(self):
        """Initialize content generator"""
        load_dotenv()
        self.logger = setup_logging(__name__)
        self.config = load_config()

        # Load templates and libraries
        self.templates = self._load_templates()
        self.hashtags = self._load_hashtags()

        # Initialize AI clients (would be implemented based on API keys)
        self.ai_clients = self._init_ai_clients()

    def _load_templates(self) -> Dict[str, Any]:
        """Load content templates"""
        templates_path = os.path.join('templates', 'content_templates.json')
        if os.path.exists(templates_path):
            with open(templates_path, 'r') as f:
                return json.load(f)
        return {}

    def _load_hashtags(self) -> Dict[str, List[str]]:
        """Load hashtag libraries"""
        hashtags_path = os.path.join('templates', 'hashtag_libraries.json')
        if os.path.exists(hashtags_path):
            with open(hashtags_path, 'r') as f:
                return json.load(f)
        return {"general": ["#socialmedia", "#marketing", "#business"]}

    def _init_ai_clients(self) -> Dict[str, Any]:
        """Initialize AI API clients"""
        clients = {}

        # Check for OpenAI API key
        if os.getenv('OPENAI_API_KEY'):
            try:
                import openai
                openai.api_key = os.getenv('OPENAI_API_KEY')
                clients['openai'] = openai
                self.logger.info("OpenAI client initialized")
            except ImportError:
                self.logger.warning("OpenAI package not installed")

        # Check for Anthropic API key
        if os.getenv('ANTHROPIC_API_KEY'):
            try:
                import anthropic
                clients['anthropic'] = anthropic.Anthropic(
                    api_key=os.getenv('ANTHROPIC_API_KEY')
                )
                self.logger.info("Anthropic client initialized")
            except ImportError:
                self.logger.warning("Anthropic package not installed")

        return clients

    def generate_post(self, platform: str, theme: str, time_of_day: str = None) -> str:
        """Generate a social media post"""
        self.logger.info(f"Generating {platform} post about {theme}")

        # Get platform-specific constraints
        constraints = self._get_platform_constraints(platform)

        # Generate content using AI or templates
        if 'openai' in self.ai_clients:
            content = self._generate_with_openai(platform, theme, constraints)
        elif 'anthropic' in self.ai_clients:
            content = self._generate_with_anthropic(platform, theme, constraints)
        else:
            content = self._generate_with_template(platform, theme)

        # Add hashtags
        content = self._add_hashtags(content, theme)

        # Format for platform
        content = self._format_for_platform(content, platform, constraints)

        return content

    def _get_platform_constraints(self, platform: str) -> Dict[str, Any]:
        """Get character limits and constraints for platform"""
        constraints = {
            "twitter": {"max_chars": 280, "hashtags": True, "mentions": True},
            "linkedin": {"max_chars": 3000, "hashtags": True, "formatting": True},
            "facebook": {"max_chars": 63206, "hashtags": True, "emojis": True},
            "instagram": {"max_chars": 2200, "hashtags": True, "line_breaks": True},
            "tiktok": {"max_chars": 2200, "hashtags": True, "trending": True}
        }

        return constraints.get(platform, {"max_chars": 280, "hashtags": True})

    def _generate_with_openai(self, platform: str, theme: str, constraints: Dict[str, Any]) -> str:
        """Generate content using OpenAI"""
        try:
            prompt = f"""Write a {platform} post about {theme}. 
            Constraints: Maximum {constraints.get('max_chars', 280)} characters.
            Make it engaging and appropriate for the platform.
            """

            response = self.ai_clients['openai'].ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a social media expert creating engaging posts."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=constraints.get('max_chars', 280) // 4,
                temperature=0.7
            )

            return response.choices[0].message.content.strip()
        except Exception as e:
            self.logger.error(f"OpenAI generation failed: {e}")
            return self._generate_with_template(platform, theme)

    def _generate_with_anthropic(self, platform: str, theme: str, constraints: Dict[str, Any]) -> str:
        """Generate content using Anthropic"""
        try:
            prompt = f"""Write a {platform} post about {theme}. Maximum {constraints.get('max_chars', 280)} characters. Make it engaging."""

            response = self.ai_clients['anthropic'].messages.create(
                model="claude-3-opus-20240229",
                max_tokens=constraints.get('max_chars', 280) // 4,
                temperature=0.7,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            return response.content[0].text.strip()
        except Exception as e:
            self.logger.error(f"Anthropic generation failed: {e}")
            return self._generate_with_template(platform, theme)

    def _generate_with_template(self, platform: str, theme: str) -> str:
        """Generate content using templates"""
        templates = self.templates.get(platform, {})
        theme_templates = templates.get(theme, templates.get('general', []))

        if theme_templates:
            template = random.choice(theme_templates)
            # Replace placeholders
            template = template.replace('{theme}', theme)
            template = template.replace('{platform}', platform)
            return template
        else:
            # Fallback template
            return f"Exciting news about {theme}! Stay tuned for more updates. #{theme.replace(' ', '')}"

    def _add_hashtags(self, content: str, theme: str) -> str:
        """Add relevant hashtags to content"""
        # Get hashtags for theme
        theme_hashtags = self.hashtags.get(theme, [])
        general_hashtags = self.hashtags.get('general', [])

        # Combine and select 3-5 hashtags
        all_hashtags = list(set(theme_hashtags + general_hashtags))
        selected_hashtags = random.sample(all_hashtags, min(5, len(all_hashtags)))

        # Add hashtags if not already at end
        if selected_hashtags and not content.endswith(tuple(selected_hashtags)):
            content += '

' + ' '.join(selected_hashtags)

        return content

    def _format_for_platform(self, content: str, platform: str, constraints: Dict[str, Any]) -> str:
        """Format content for specific platform"""
        # Truncate if too long
        max_chars = constraints.get('max_chars', 280)
        if len(content) > max_chars:
            content = content[:max_chars-3] + '...'

        # Platform-specific formatting
        if platform == 'twitter':
            # Ensure it fits with thread if needed
            if len(content) > 280:
                # Split into thread (simplified)
                pass
        elif platform == 'linkedin':
            # Add professional tone
            if not content.startswith(('I', 'We', 'Our', 'The')):
                content = f"I'm excited to share: {content}"
        elif platform == 'instagram':
            # Add line breaks for readability
            content = content.replace('. ', '.

')

        return content

    def generate_image_prompt(self, theme: str) -> str:
        """Generate prompt for image generation"""
        prompts = [
            f"Professional illustration about {theme}, clean design, modern style",
            f"Abstract representation of {theme}, vibrant colors, digital art",
            f"Minimalist design for {theme}, white background, elegant typography",
            f"Infographic about {theme}, data visualization, corporate style"
        ]

        return random.choice(prompts)

    def generate_video_idea(self, theme: str) -> Dict[str, Any]:
        """Generate video content idea"""
        ideas = [
            {
                "title": f"The Future of {theme}",
                "description": f"Exploring how {theme} is changing our industry",
                "duration": "60 seconds",
                "style": "explainer"
            },
            {
                "title": f"5 Tips for Mastering {theme}",
                "description": f"Quick tips to improve your {theme} skills",
                "duration": "45 seconds",
                "style": "tutorial"
            },
            {
                "title": f"Behind the Scenes: {theme}",
                "description": f"See how we approach {theme} at our company",
                "duration": "90 seconds",
                "style": "documentary"
            }
        ]

        return random.choice(ideas)


def main():
    """Test content generation"""
    import argparse

    parser = argparse.ArgumentParser(description='Content Generator')
    parser.add_argument('--platform', required=True, help='Social media platform')
    parser.add_argument('--theme', required=True, help='Content theme')
    parser.add_argument('--count', type=int, default=3, help='Number of posts to generate')

    args = parser.parse_args()

    generator = ContentGenerator()

    print(f"Generating {args.count} {args.platform} posts about {args.theme}:
")

    for i in range(args.count):
        post = generator.generate_post(args.platform, args.theme)
        print(f"Post {i+1}:
{post}
")
        print("-" * 50)

if __name__ == '__main__':
    main()
