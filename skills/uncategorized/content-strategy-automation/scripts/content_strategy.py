#!/usr/bin/env python3
"""
Content Strategy Automation - Main Strategy Script
"""

import os
import json
import pandas as pd
from datetime import datetime, timedelta
from typing import List, Dict, Any
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ContentStrategy:
    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        if self.openai_api_key:
            openai.api_key = self.openai_api_key

    def analyze_topic(self, topic: str, audience: str) -> Dict[str, Any]:
        """Analyze topic and audience to create content pillars"""

        prompt = f"""As a content strategist, analyze the topic '{topic}' for audience '{audience}'.
        Provide:
        1. 3-5 content pillars (main themes)
        2. Content formats for each pillar (blog, video, social, etc.)
        3. Recommended publishing frequency
        4. Key performance indicators (KPIs)
        5. Competitor analysis insights

        Format as JSON with keys: pillars, formats, frequency, kpis, competitors."""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )

            analysis = json.loads(response.choices[0].message.content)
            return analysis

        except Exception as e:
            print(f"Error in topic analysis: {e}")
            # Return default structure
            return {
                "pillars": [f"{topic} Fundamentals", f"Advanced {topic}", f"{topic} Case Studies"],
                "formats": {"blog": 60, "social": 30, "video": 10},
                "frequency": "3 posts per week",
                "kpis": ["engagement", "traffic", "conversions"],
                "competitors": ["Industry leader 1", "Industry leader 2"]
            }

    def create_content_calendar(self, pillars: List[str], weeks: int = 4) -> pd.DataFrame:
        """Create a content calendar for the given pillars"""

        calendar_data = []
        start_date = datetime.now()

        for week in range(weeks):
            week_start = start_date + timedelta(days=week * 7)

            for i, pillar in enumerate(pillars):
                post_date = week_start + timedelta(days=i * 2)  # Spread posts

                calendar_data.append({
                    "Date": post_date.strftime("%Y-%m-%d"),
                    "Pillar": pillar,
                    "Topic": f"{pillar} - Week {week + 1}",
                    "Format": "Blog Post" if week % 2 == 0 else "Social Media",
                    "Channel": "Website" if week % 2 == 0 else "LinkedIn",
                    "Status": "Planned",
                    "Assignee": "Content Team",
                    "Notes": ""
                })

        df = pd.DataFrame(calendar_data)
        return df

    def generate_content_ideas(self, pillar: str, count: int = 5) -> List[str]:
        """Generate content ideas for a specific pillar"""

        prompt = f"Generate {count} engaging content ideas about '{pillar}' for a business audience."

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.8,
                n=count
            )

            ideas = [choice.message.content.strip() for choice in response.choices]
            return ideas

        except Exception as e:
            print(f"Error generating ideas: {e}")
            return [f"{pillar} idea {i+1}" for i in range(count)]

    def calculate_roi(self, investment: float, revenue: float) -> Dict[str, Any]:
        """Calculate ROI for content marketing"""

        if investment == 0:
            return {"roi": 0, "roi_percentage": 0, "break_even": 0}

        roi = revenue - investment
        roi_percentage = (roi / investment) * 100
        break_even = investment / (revenue / 30) if revenue > 0 else float('inf')

        return {
            "roi": roi,
            "roi_percentage": roi_percentage,
            "break_even_days": break_even,
            "investment": investment,
            "revenue": revenue
        }


def main():
    """Main execution function"""

    print("=== Content Strategy Automation ===
")

    # Example usage
    strategy = ContentStrategy()

    # Analyze topic
    print("1. Analyzing topic and audience...")
    analysis = strategy.analyze_topic(
        topic="Artificial Intelligence in Marketing",
        audience="Marketing professionals and business owners"
    )

    print(f"Content Pillars: {analysis.get('pillars', [])}")
    print(f"Recommended Formats: {analysis.get('formats', {})}")

    # Create content calendar
    print("
2. Creating content calendar...")
    calendar_df = strategy.create_content_calendar(analysis.get('pillars', []))

    # Save calendar to CSV
    calendar_path = "content_calendar.csv"
    calendar_df.to_csv(calendar_path, index=False)
    print(f"Calendar saved to: {calendar_path}")
    print(f"Total posts planned: {len(calendar_df)}")

    # Generate content ideas
    print("
3. Generating content ideas...")
    if analysis.get('pillars'):
        ideas = strategy.generate_content_ideas(analysis['pillars'][0])
        print(f"Ideas for '{analysis['pillars'][0]}':")
        for i, idea in enumerate(ideas, 1):
            print(f"  {i}. {idea}")

    # Calculate example ROI
    print("
4. ROI Analysis...")
    roi_data = strategy.calculate_roi(investment=5000, revenue=15000)
    print(f"Investment: ${roi_data['investment']:,.2f}")
    print(f"Revenue: ${roi_data['revenue']:,.2f}")
    print(f"ROI: ${roi_data['roi']:,.2f} ({roi_data['roi_percentage']:.1f}%)")
    print(f"Break-even: {roi_data['break_even_days']:.1f} days")

    print("
=== Strategy Complete ===")
    print("Next steps:")
    print("1. Review content calendar")
    print("2. Assign tasks to team members")
    print("3. Set up distribution automation")
    print("4. Configure analytics tracking")


if __name__ == "__main__":
    main()
