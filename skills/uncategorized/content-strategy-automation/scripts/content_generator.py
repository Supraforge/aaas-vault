#!/usr/bin/env python3
"""
AI Content Generator for Content Strategy Automation
"""

import os
import openai
from dotenv import load_dotenv

load_dotenv()

class ContentGenerator:
    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        if self.openai_api_key:
            openai.api_key = self.openai_api_key

    def generate_blog_post(self, topic: str, tone: str = "professional", length: str = "medium") -> str:
        """Generate a blog post on the given topic"""

        length_map = {
            "short": "300-500 words",
            "medium": "800-1200 words",
            "long": "1500-2000 words"
        }

        prompt = f"""Write a {tone} blog post about '{topic}'.
        Length: {length_map.get(length, '800-1200 words')}
        Structure:
        1. Engaging introduction
        2. 3-5 main points with examples
        3. Practical tips or actionable advice
        4. Conclusion with key takeaways
        5. Call-to-action

        Use markdown formatting with headings, bullet points, and bold text where appropriate."""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=2000
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"Error generating content: {e}"

    def generate_social_media_post(self, topic: str, platform: str = "linkedin") -> Dict[str, str]:
        """Generate social media posts for different platforms"""

        platform_guides = {
            "linkedin": "professional, industry insights, 3-5 sentences",
            "twitter": "concise, engaging, 1-2 sentences, include hashtags",
            "facebook": "conversational, community-focused, include questions",
            "instagram": "visual-focused, short captions, emojis"
        }

        guide = platform_guides.get(platform.lower(), "professional, engaging")

        prompt = f"""Write a {platform} post about '{topic}'.
        Style: {guide}
        Include relevant hashtags.
        Provide the post content and 3 suggested hashtags."""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.8
            )

            content = response.choices[0].message.content

            # Extract hashtags
            hashtags = [word for word in content.split() if word.startswith('#')]
            if not hashtags:
                hashtags = [f"#{topic.replace(' ', '').lower()}", "#contentmarketing", "#digitalmarketing"]

            return {
                "platform": platform,
                "content": content,
                "hashtags": hashtags[:3],
                "character_count": len(content)
            }

        except Exception as e:
            return {"error": str(e)}

    def generate_email_newsletter(self, topic: str, audience: str = "subscribers") -> str:
        """Generate an email newsletter"""

        prompt = f"""Write an email newsletter about '{topic}' for {audience}.
        Include:
        1. Subject line (attention-grabbing)
        2. Preheader text
        3. Engaging introduction
        4. 2-3 main sections with value
        5. Call-to-action
        6. Professional closing

        Use friendly but professional tone."""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"Error generating newsletter: {e}"


def main():
    """Example usage"""
    generator = ContentGenerator()

    print("=== AI Content Generator ===
")

    # Generate blog post
    print("1. Generating blog post...")
    blog_post = generator.generate_blog_post(
        topic="The Future of AI in Content Marketing",
        tone="insightful",
        length="medium"
    )
    print(f"Blog Post Preview: {blog_post[:200]}...
")

    # Generate social media posts
    print("2. Generating social media posts...")
    for platform in ["linkedin", "twitter", "facebook"]:
        post = generator.generate_social_media_post(
            topic="AI Content Tools",
            platform=platform
        )
        if "error" not in post:
            print(f"{platform.upper()}: {post['content'][:100]}...")
            print(f"Hashtags: {', '.join(post['hashtags'])}")
        print()

    # Generate newsletter
    print("3. Generating email newsletter...")
    newsletter = generator.generate_email_newsletter(
        topic="Monthly Marketing Insights",
        audience="marketing professionals"
    )
    print(f"Newsletter Preview: {newsletter[:200]}...")


if __name__ == "__main__":
    main()
