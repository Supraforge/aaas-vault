#!/usr/bin/env python3
"""
YouTube Comment Analyzer

Analyzes YouTube video comments to extract audience insights, questions,
myths, pain points, and content recommendations.

Based on: https://github.com/drshailesh88/youtube-analyzer

Usage:
    python analyze_comments.py VIDEO_URL_OR_ID
    python analyze_comments.py https://youtube.com/watch?v=abc123
    python analyze_comments.py abc123xyz --max-comments 500
    python analyze_comments.py VIDEO_ID --output output/analysis.json
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict

# Load environment variables
try:
    from dotenv import load_dotenv
    env_path = Path(__file__).parent.parent.parent.parent.parent / ".env"
    if env_path.exists():
        load_dotenv(env_path)
except ImportError:
    pass

# Try to import required libraries
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("Error: requests package required. Install with: pip install requests")
    sys.exit(1)

try:
    from anthropic import Anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

try:
    import httpx
    HTTPX_AVAILABLE = True
except ImportError:
    HTTPX_AVAILABLE = False


@dataclass
class CommentInsight:
    """Structured insight from comment analysis."""
    text: str
    urgency: str  # HIGH, MEDIUM, LOW
    category: str  # question, myth, pain_point, praise, request


@dataclass
class AnalysisResult:
    """Complete analysis result."""
    video_id: str
    video_title: Optional[str]
    comment_count: int
    analysis_time: float
    top_questions: List[Dict[str, str]]
    top_myths: List[Dict[str, str]]
    pain_points: List[Dict[str, str]]
    content_recommendations: Dict[str, List[str]]
    sentiment: Dict[str, Any]
    raw_themes: List[str]
    timestamp: str


class YouTubeCommentFetcher:
    """Fetch comments from YouTube videos using Data API v3 or scraping."""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("YOUTUBE_API_KEY") or os.getenv("GOOGLE_API_KEY")
        self.base_url = "https://www.googleapis.com/youtube/v3"

    @staticmethod
    def extract_video_id(url_or_id: str) -> str:
        """Extract video ID from various URL formats."""
        # Already an ID (11 chars, alphanumeric with - and _)
        if re.match(r'^[a-zA-Z0-9_-]{11}$', url_or_id):
            return url_or_id

        # YouTube URL patterns
        patterns = [
            r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([a-zA-Z0-9_-]{11})',
            r'youtube\.com/shorts/([a-zA-Z0-9_-]{11})',
        ]

        for pattern in patterns:
            match = re.search(pattern, url_or_id)
            if match:
                return match.group(1)

        raise ValueError(f"Could not extract video ID from: {url_or_id}")

    def get_video_info(self, video_id: str) -> Dict[str, Any]:
        """Get basic video information."""
        if not self.api_key:
            return {"title": f"Video {video_id}", "channelTitle": "Unknown"}

        try:
            response = requests.get(
                f"{self.base_url}/videos",
                params={
                    "part": "snippet,statistics",
                    "id": video_id,
                    "key": self.api_key
                },
                timeout=30
            )
            response.raise_for_status()
            data = response.json()

            if data.get("items"):
                item = data["items"][0]
                return {
                    "title": item["snippet"]["title"],
                    "channelTitle": item["snippet"]["channelTitle"],
                    "viewCount": item["statistics"].get("viewCount", 0),
                    "commentCount": item["statistics"].get("commentCount", 0),
                }
        except Exception as e:
            print(f"Warning: Could not fetch video info: {e}")

        return {"title": f"Video {video_id}", "channelTitle": "Unknown"}

    def fetch_comments(self, video_id: str, max_comments: int = 500) -> List[str]:
        """Fetch comments from YouTube video."""
        comments = []

        # Try API first
        if self.api_key:
            comments = self._fetch_via_api(video_id, max_comments)

        # Fallback to scraping if no API key or API failed
        if not comments:
            comments = self._fetch_via_scraping(video_id, max_comments)

        return comments

    def _fetch_via_api(self, video_id: str, max_comments: int) -> List[str]:
        """Fetch comments using YouTube Data API v3."""
        comments = []
        next_page_token = None

        try:
            while len(comments) < max_comments:
                params = {
                    "part": "snippet",
                    "videoId": video_id,
                    "maxResults": min(100, max_comments - len(comments)),
                    "order": "relevance",
                    "key": self.api_key
                }
                if next_page_token:
                    params["pageToken"] = next_page_token

                response = requests.get(
                    f"{self.base_url}/commentThreads",
                    params=params,
                    timeout=30
                )
                response.raise_for_status()
                data = response.json()

                for item in data.get("items", []):
                    comment_text = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
                    # Clean HTML tags
                    comment_text = re.sub(r'<[^>]+>', '', comment_text)
                    comments.append(comment_text)

                next_page_token = data.get("nextPageToken")
                if not next_page_token:
                    break

                time.sleep(0.1)  # Rate limiting

            print(f"Fetched {len(comments)} comments via YouTube API")
        except Exception as e:
            print(f"API fetch failed: {e}")

        return comments

    def _fetch_via_scraping(self, video_id: str, max_comments: int) -> List[str]:
        """Fallback: Try to fetch comments via scraping (limited)."""
        print("Note: Using limited scraping method. Set YOUTUBE_API_KEY for better results.")

        # This is a simplified approach - in production you'd use a proper scraper
        # For now, return empty and let the user know
        print("Scraping not implemented. Please set YOUTUBE_API_KEY environment variable.")
        return []


class CommentAnalyzer:
    """Analyze comments using AI to extract insights."""

    ANALYSIS_PROMPT = """You are analyzing YouTube video comments for a cardiology content creator.

Analyze these comments and extract:

1. **TOP QUESTIONS** (5-7): What are viewers asking? Rate urgency (HIGH/MEDIUM/LOW).
   - HIGH: Critical health questions that need expert answers
   - MEDIUM: Common questions about the topic
   - LOW: General curiosity

2. **TOP MYTHS** (3-5): What misconceptions or dangerous beliefs appear? Rate danger level.
   - HIGH: Could lead to harmful health decisions
   - MEDIUM: Common misunderstanding
   - LOW: Minor confusion

3. **PAIN POINTS** (3-5): What frustrations do viewers express?
   - About the topic itself
   - About healthcare system
   - About conflicting information

4. **CONTENT RECOMMENDATIONS**:
   - "must_address": Topics that MUST be covered in future videos
   - "content_gaps": What viewers want but isn't covered
   - "viral_potential": Topics with high engagement potential

5. **SENTIMENT ANALYSIS**:
   - positive_count: Number of positive comments
   - negative_count: Number of negative comments
   - neutral_count: Number of neutral comments
   - overall: Brief summary (1 sentence)

6. **RAW THEMES**: List 5-10 recurring themes/topics

Comments to analyze:
---
{comments}
---

Respond with valid JSON in this exact format:
{{
    "top_questions": [
        {{"text": "question text", "urgency": "HIGH/MEDIUM/LOW"}}
    ],
    "top_myths": [
        {{"text": "myth text", "danger": "HIGH/MEDIUM/LOW"}}
    ],
    "pain_points": [
        {{"text": "pain point text", "category": "topic/healthcare/information"}}
    ],
    "content_recommendations": {{
        "must_address": ["topic1", "topic2"],
        "content_gaps": ["gap1", "gap2"],
        "viral_potential": ["topic1", "topic2"]
    }},
    "sentiment": {{
        "positive_count": 0,
        "negative_count": 0,
        "neutral_count": 0,
        "overall": "summary"
    }},
    "raw_themes": ["theme1", "theme2"]
}}"""

    def __init__(self):
        self.client = None
        self._init_client()

    def _init_client(self):
        """Initialize AI client."""
        if ANTHROPIC_AVAILABLE:
            api_key = os.getenv("ANTHROPIC_API_KEY")
            if api_key:
                self.client = Anthropic(api_key=api_key)
                self.client_type = "anthropic"
                return

        # Fallback to OpenRouter
        openrouter_key = os.getenv("OPENROUTER_API_KEY")
        if openrouter_key:
            self.openrouter_key = openrouter_key
            self.client_type = "openrouter"
            return

        print("Warning: No AI API key found. Set ANTHROPIC_API_KEY or OPENROUTER_API_KEY")
        self.client_type = None

    def analyze(self, comments: List[str], chunk_size: int = 100) -> Dict[str, Any]:
        """Analyze comments using map-reduce for large sets."""
        if not comments:
            return self._empty_result()

        # For small sets, analyze directly
        if len(comments) <= chunk_size:
            return self._analyze_chunk(comments)

        # Map-reduce for large sets
        print(f"Analyzing {len(comments)} comments in {(len(comments) // chunk_size) + 1} chunks...")

        chunk_results = []
        for i in range(0, len(comments), chunk_size):
            chunk = comments[i:i + chunk_size]
            print(f"  Analyzing chunk {i // chunk_size + 1}...")
            result = self._analyze_chunk(chunk)
            if result:
                chunk_results.append(result)
            time.sleep(1)  # Rate limiting

        # Reduce: Merge results
        return self._merge_results(chunk_results)

    def _analyze_chunk(self, comments: List[str]) -> Dict[str, Any]:
        """Analyze a single chunk of comments."""
        comments_text = "\n".join(f"- {c[:500]}" for c in comments[:100])  # Limit context
        prompt = self.ANALYSIS_PROMPT.format(comments=comments_text)

        try:
            if self.client_type == "anthropic":
                response = self.client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=2000,
                    messages=[{"role": "user", "content": prompt}]
                )
                response_text = response.content[0].text

            elif self.client_type == "openrouter":
                response = requests.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {self.openrouter_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": "google/gemini-2.0-flash-001",  # Free model
                        "messages": [{"role": "user", "content": prompt}]
                    },
                    timeout=60
                )
                response.raise_for_status()
                response_text = response.json()["choices"][0]["message"]["content"]

            else:
                return self._empty_result()

            # Parse JSON from response
            json_match = re.search(r'\{[\s\S]*\}', response_text)
            if json_match:
                return json.loads(json_match.group())

        except Exception as e:
            print(f"Analysis error: {e}")

        return self._empty_result()

    def _merge_results(self, results: List[Dict]) -> Dict[str, Any]:
        """Merge multiple chunk results into one."""
        if not results:
            return self._empty_result()

        if len(results) == 1:
            return results[0]

        merged = {
            "top_questions": [],
            "top_myths": [],
            "pain_points": [],
            "content_recommendations": {
                "must_address": [],
                "content_gaps": [],
                "viral_potential": []
            },
            "sentiment": {
                "positive_count": 0,
                "negative_count": 0,
                "neutral_count": 0,
                "overall": ""
            },
            "raw_themes": []
        }

        for result in results:
            # Merge lists (deduplicate by text)
            for q in result.get("top_questions", []):
                if q not in merged["top_questions"]:
                    merged["top_questions"].append(q)

            for m in result.get("top_myths", []):
                if m not in merged["top_myths"]:
                    merged["top_myths"].append(m)

            for p in result.get("pain_points", []):
                if p not in merged["pain_points"]:
                    merged["pain_points"].append(p)

            # Merge recommendations
            recs = result.get("content_recommendations", {})
            for key in ["must_address", "content_gaps", "viral_potential"]:
                for item in recs.get(key, []):
                    if item not in merged["content_recommendations"][key]:
                        merged["content_recommendations"][key].append(item)

            # Sum sentiment counts
            sent = result.get("sentiment", {})
            merged["sentiment"]["positive_count"] += sent.get("positive_count", 0)
            merged["sentiment"]["negative_count"] += sent.get("negative_count", 0)
            merged["sentiment"]["neutral_count"] += sent.get("neutral_count", 0)

            # Merge themes
            for theme in result.get("raw_themes", []):
                if theme not in merged["raw_themes"]:
                    merged["raw_themes"].append(theme)

        # Sort and limit
        merged["top_questions"] = sorted(
            merged["top_questions"],
            key=lambda x: {"HIGH": 0, "MEDIUM": 1, "LOW": 2}.get(x.get("urgency", "LOW"), 2)
        )[:7]

        merged["top_myths"] = sorted(
            merged["top_myths"],
            key=lambda x: {"HIGH": 0, "MEDIUM": 1, "LOW": 2}.get(x.get("danger", "LOW"), 2)
        )[:5]

        merged["pain_points"] = merged["pain_points"][:5]
        merged["raw_themes"] = merged["raw_themes"][:10]

        # Calculate overall sentiment
        total = (merged["sentiment"]["positive_count"] +
                 merged["sentiment"]["negative_count"] +
                 merged["sentiment"]["neutral_count"])
        if total > 0:
            pos_pct = merged["sentiment"]["positive_count"] / total * 100
            neg_pct = merged["sentiment"]["negative_count"] / total * 100
            merged["sentiment"]["overall"] = f"{pos_pct:.0f}% positive, {neg_pct:.0f}% negative"

        return merged

    def _empty_result(self) -> Dict[str, Any]:
        """Return empty result structure."""
        return {
            "top_questions": [],
            "top_myths": [],
            "pain_points": [],
            "content_recommendations": {
                "must_address": [],
                "content_gaps": [],
                "viral_potential": []
            },
            "sentiment": {
                "positive_count": 0,
                "negative_count": 0,
                "neutral_count": 0,
                "overall": "No data"
            },
            "raw_themes": []
        }


def format_report(result: AnalysisResult) -> str:
    """Format analysis result as readable report."""
    lines = [
        f"## Comment Analysis: {result.video_title or result.video_id}",
        "",
        f"**Analyzed:** {result.comment_count} comments | **Time:** {result.analysis_time:.1f} seconds",
        "",
        "### Top Questions (What viewers want to know)",
    ]

    for i, q in enumerate(result.top_questions, 1):
        lines.append(f"{i}. {q.get('text', 'N/A')} — {q.get('urgency', 'N/A')} urgency")

    lines.extend(["", "### Top Myths (Misconceptions to address)"])
    for i, m in enumerate(result.top_myths, 1):
        lines.append(f"{i}. {m.get('text', 'N/A')} — {m.get('danger', 'N/A')} danger")

    lines.extend(["", "### Pain Points (Viewer frustrations)"])
    for i, p in enumerate(result.pain_points, 1):
        lines.append(f"{i}. {p.get('text', 'N/A')}")

    lines.extend(["", "### Content Recommendations"])
    recs = result.content_recommendations
    lines.append(f"- **Must Address:** {', '.join(recs.get('must_address', [])) or 'None identified'}")
    lines.append(f"- **Content Gaps:** {', '.join(recs.get('content_gaps', [])) or 'None identified'}")
    lines.append(f"- **Viral Potential:** {', '.join(recs.get('viral_potential', [])) or 'None identified'}")

    lines.extend(["", "### Sentiment"])
    sent = result.sentiment
    lines.append(f"Positive: {sent.get('positive_count', 0)} | "
                 f"Negative: {sent.get('negative_count', 0)} | "
                 f"Neutral: {sent.get('neutral_count', 0)}")
    lines.append(f"Summary: {sent.get('overall', 'N/A')}")

    if result.raw_themes:
        lines.extend(["", "### Recurring Themes"])
        lines.append(", ".join(result.raw_themes))

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Analyze YouTube video comments for audience insights"
    )
    parser.add_argument(
        "video",
        help="YouTube video URL or ID (e.g., https://youtube.com/watch?v=abc123 or abc123)"
    )
    parser.add_argument(
        "--max-comments", "-m",
        type=int,
        default=500,
        help="Maximum comments to fetch (default: 500)"
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        help="Output file path (default: output/analysis_VIDEO_ID.json)"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output raw JSON instead of formatted report"
    )

    args = parser.parse_args()

    print("\n🎬 YouTube Comment Analyzer")
    print("=" * 50)

    # Extract video ID
    try:
        video_id = YouTubeCommentFetcher.extract_video_id(args.video)
        print(f"Video ID: {video_id}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Initialize components
    fetcher = YouTubeCommentFetcher()
    analyzer = CommentAnalyzer()

    # Get video info
    print("Fetching video info...")
    video_info = fetcher.get_video_info(video_id)
    print(f"Title: {video_info.get('title', 'Unknown')}")

    # Fetch comments
    print(f"\nFetching up to {args.max_comments} comments...")
    start_time = time.time()
    comments = fetcher.fetch_comments(video_id, args.max_comments)

    if not comments:
        print("\nNo comments found. The video may have comments disabled.")
        print("Tip: Set YOUTUBE_API_KEY environment variable for best results.")
        sys.exit(1)

    print(f"Found {len(comments)} comments")

    # Analyze
    print("\nAnalyzing comments with AI...")
    analysis = analyzer.analyze(comments)
    analysis_time = time.time() - start_time

    # Build result
    result = AnalysisResult(
        video_id=video_id,
        video_title=video_info.get("title"),
        comment_count=len(comments),
        analysis_time=analysis_time,
        top_questions=analysis.get("top_questions", []),
        top_myths=analysis.get("top_myths", []),
        pain_points=analysis.get("pain_points", []),
        content_recommendations=analysis.get("content_recommendations", {}),
        sentiment=analysis.get("sentiment", {}),
        raw_themes=analysis.get("raw_themes", []),
        timestamp=datetime.now().isoformat()
    )

    # Output
    if args.json:
        print(json.dumps(asdict(result), indent=2))
    else:
        print("\n" + "=" * 50)
        print(format_report(result))

    # Save to file
    output_dir = Path(__file__).parent.parent / "output"
    output_dir.mkdir(exist_ok=True)

    output_path = args.output or (output_dir / f"analysis_{video_id}_{int(time.time())}.json")
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(asdict(result), f, indent=2)

    print(f"\n📁 Full analysis saved to: {output_path}")
    print("=" * 50)


if __name__ == "__main__":
    main()
