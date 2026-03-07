#!/usr/bin/env python3
"""
Analyze content ideas from text and generate viral potential scores.
This script provides the computational backbone for scoring content ideas.
"""

import re
import json
from typing import List, Dict, Tuple
from dataclasses import dataclass
from enum import Enum


class EmotionalTrigger(Enum):
    FEAR = "fear"
    HOPE = "hope"
    CURIOSITY = "curiosity"
    EMPOWERMENT = "empowerment"
    RELIEF = "relief"
    SURPRISE = "surprise"


@dataclass
class ContentIdea:
    title: str
    description: str
    category: str
    emotional_triggers: List[EmotionalTrigger]
    keywords: List[str]
    viral_score: float = 0.0
    
    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'emotional_triggers': [t.value for t in self.emotional_triggers],
            'keywords': self.keywords,
            'viral_score': self.viral_score
        }


class ViralScorer:
    """Calculate viral potential scores for content ideas."""
    
    # High-value keywords in medical content
    HIGH_VALUE_KEYWORDS = [
        'warning signs', 'symptoms', 'causes', 'treatment', 'prevent',
        'diagnosis', 'risk factors', 'what to expect', 'how to', 'vs',
        'truth about', 'myths', 'misconceptions', 'actually happens',
        'don\'t know', 'should know', 'need to know'
    ]
    
    # Emotional trigger keywords
    EMOTIONAL_KEYWORDS = {
        EmotionalTrigger.FEAR: ['warning', 'danger', 'risk', 'serious', 'emergency', 'fatal', 'deadly'],
        EmotionalTrigger.HOPE: ['recover', 'cure', 'prevent', 'better', 'improve', 'heal', 'reverse'],
        EmotionalTrigger.CURIOSITY: ['why', 'how', 'what', 'secret', 'surprising', 'unknown', 'discover'],
        EmotionalTrigger.EMPOWERMENT: ['you can', 'take control', 'manage', 'yourself', 'understand', 'know'],
        EmotionalTrigger.RELIEF: ['explain', 'normal', 'common', 'okay', 'not alone', 'understand'],
        EmotionalTrigger.SURPRISE: ['actually', 'really', 'truth', 'fact', 'surprising', 'myth', 'believe']
    }
    
    def __init__(self):
        self.base_score = 50  # Start from middle
        
    def detect_emotional_triggers(self, text: str) -> List[EmotionalTrigger]:
        """Detect emotional triggers in text."""
        text_lower = text.lower()
        triggers = []
        
        for trigger, keywords in self.EMOTIONAL_KEYWORDS.items():
            if any(keyword in text_lower for keyword in keywords):
                triggers.append(trigger)
        
        return triggers
    
    def extract_keywords(self, text: str) -> List[str]:
        """Extract relevant keywords from text."""
        text_lower = text.lower()
        found_keywords = []
        
        for keyword in self.HIGH_VALUE_KEYWORDS:
            if keyword in text_lower:
                found_keywords.append(keyword)
        
        return found_keywords
    
    def score_topic_factors(self, idea: ContentIdea) -> float:
        """Score topic-related factors (40 points max)."""
        score = 0.0
        
        # Search demand (15 pts) - based on keywords
        high_value_count = len(idea.keywords)
        score += min(high_value_count * 3, 15)
        
        # Emotional resonance (10 pts) - based on triggers
        emotional_count = len(idea.emotional_triggers)
        score += min(emotional_count * 2.5, 10)
        
        # Timeliness (10 pts) - check for trending keywords
        trending_keywords = ['2024', '2025', 'new', 'recent', 'latest', 'update', 'current']
        has_trending = any(kw in idea.title.lower() or kw in idea.description.lower() 
                          for kw in trending_keywords)
        score += 8 if has_trending else 5
        
        # Novelty (5 pts) - check for unique angles
        novelty_keywords = ['secret', 'hidden', 'surprising', 'truth', 'actually', 'don\'t know']
        has_novelty = any(kw in idea.title.lower() or kw in idea.description.lower() 
                         for kw in novelty_keywords)
        score += 5 if has_novelty else 2
        
        return min(score, 40)
    
    def score_engagement_factors(self, idea: ContentIdea) -> float:
        """Score engagement-related factors (30 points max)."""
        score = 0.0
        text_combined = f"{idea.title} {idea.description}".lower()
        
        # Shareability (10 pts) - family-relevant content
        shareable_terms = ['family', 'loved ones', 'parents', 'children', 'everyone', 
                          'warning', 'important', 'need to know']
        shareability = sum(1 for term in shareable_terms if term in text_combined)
        score += min(shareability * 2, 10)
        
        # Comment-worthiness (10 pts) - discussion-inducing
        discussion_terms = ['controversial', 'debate', 'opinion', 'experience', 'vs', 
                           'better', 'worse', 'should', 'myth']
        discussion_value = sum(1 for term in discussion_terms if term in text_combined)
        score += min(discussion_value * 2, 10)
        
        # Practical value (10 pts) - actionable content
        action_terms = ['how to', 'what to do', 'steps', 'guide', 'prevent', 
                       'manage', 'treatment', 'cure']
        practical_value = sum(1 for term in action_terms if term in text_combined)
        score += min(practical_value * 2, 10)
        
        return min(score, 30)
    
    def score_retention_factors(self, idea: ContentIdea) -> float:
        """Score retention-related factors (30 points max)."""
        score = 0.0
        text_combined = f"{idea.title} {idea.description}".lower()
        
        # Hook potential (10 pts) - compelling opening possibilities
        hook_terms = ['shocking', 'surprising', 'warning', 'don\'t know', 'secret', 
                     'truth', 'what really', 'actually']
        hook_value = sum(1 for term in hook_terms if term in text_combined)
        score += min(hook_value * 2.5, 10)
        
        # Information density (10 pts) - value per minute potential
        # Check for numbered lists, multiple subtopics
        has_numbers = bool(re.search(r'\d+\s+(signs|symptoms|ways|steps|types|causes)', text_combined))
        has_multiple_aspects = len(text_combined.split()) > 20  # Longer descriptions suggest depth
        score += 5 if has_numbers else 2
        score += 5 if has_multiple_aspects else 3
        
        # Narrative flow (10 pts) - story potential
        narrative_terms = ['story', 'case', 'patient', 'experience', 'journey', 
                          'before', 'after', 'what happened']
        has_narrative = any(term in text_combined for term in narrative_terms)
        # Medical content naturally has clear progression (symptoms -> diagnosis -> treatment)
        medical_progression = any(term in text_combined for term in ['diagnosis', 'treatment', 'recovery'])
        score += 6 if has_narrative else 3
        score += 4 if medical_progression else 2
        
        return min(score, 30)
    
    def calculate_viral_score(self, idea: ContentIdea) -> float:
        """Calculate total viral score (0-100)."""
        topic_score = self.score_topic_factors(idea)
        engagement_score = self.score_engagement_factors(idea)
        retention_score = self.score_retention_factors(idea)
        
        total = topic_score + engagement_score + retention_score
        return round(total, 1)


class ContentAnalyzer:
    """Main content analysis engine."""
    
    def __init__(self):
        self.scorer = ViralScorer()
    
    def parse_content_ideas(self, text: str) -> List[ContentIdea]:
        """Parse content ideas from text (bullet points, numbered lists, etc.)."""
        ideas = []
        
        # Split by common delimiters
        lines = text.strip().split('\n')
        
        current_idea = None
        current_description = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Check if this is a new idea (starts with number, bullet, or is a heading)
            is_new_idea = (
                re.match(r'^\d+[\.)]\s+', line) or  # "1. " or "1) "
                re.match(r'^[-*•]\s+', line) or      # "- " or "* " or "• "
                re.match(r'^#+\s+', line) or         # "## " (markdown heading)
                (len(line) < 100 and current_idea is None)  # Short line, possibly a title
            )
            
            if is_new_idea:
                # Save previous idea if exists
                if current_idea:
                    idea_obj = self._create_content_idea(current_idea, ' '.join(current_description))
                    ideas.append(idea_obj)
                
                # Start new idea
                current_idea = re.sub(r'^(\d+[\.)]\s+|[-*•#]\s+)', '', line)
                current_description = []
            else:
                # This is a continuation/description
                current_description.append(line)
        
        # Don't forget the last idea
        if current_idea:
            idea_obj = self._create_content_idea(current_idea, ' '.join(current_description))
            ideas.append(idea_obj)
        
        return ideas
    
    def _create_content_idea(self, title: str, description: str) -> ContentIdea:
        """Create a ContentIdea object from title and description."""
        combined_text = f"{title} {description}"
        
        # Detect emotional triggers
        triggers = self.scorer.detect_emotional_triggers(combined_text)
        
        # Extract keywords
        keywords = self.scorer.extract_keywords(combined_text)
        
        # Determine category (basic categorization)
        category = self._categorize_content(combined_text)
        
        # Create idea object
        idea = ContentIdea(
            title=title,
            description=description,
            category=category,
            emotional_triggers=triggers,
            keywords=keywords
        )
        
        # Calculate viral score
        idea.viral_score = self.scorer.calculate_viral_score(idea)
        
        return idea
    
    def _categorize_content(self, text: str) -> str:
        """Categorize content based on keywords."""
        text_lower = text.lower()
        
        if any(word in text_lower for word in ['procedure', 'surgery', 'operation', 'stent', 'bypass']):
            return 'Procedures & Treatments'
        elif any(word in text_lower for word in ['symptom', 'sign', 'warning', 'recognize']):
            return 'Symptoms & Diagnosis'
        elif any(word in text_lower for word in ['prevent', 'risk', 'lifestyle', 'diet', 'exercise']):
            return 'Prevention & Risk Factors'
        elif any(word in text_lower for word in ['medication', 'drug', 'pill', 'prescription']):
            return 'Medications'
        elif any(word in text_lower for word in ['test', 'scan', 'ecg', 'echo', 'mri', 'ct']):
            return 'Tests & Diagnostics'
        elif any(word in text_lower for word in ['myth', 'truth', 'misconception', 'believe']):
            return 'Myths & Facts'
        else:
            return 'General Education'
    
    def analyze_and_rank(self, text: str, top_n: int = None) -> List[ContentIdea]:
        """Analyze content and return ranked ideas."""
        ideas = self.parse_content_ideas(text)
        
        # Sort by viral score (descending)
        ideas.sort(key=lambda x: x.viral_score, reverse=True)
        
        if top_n:
            return ideas[:top_n]
        return ideas


def main():
    """Example usage of the content analyzer."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python analyze_content_ideas.py <text_file>")
        print("Or provide text via stdin")
        text = sys.stdin.read()
    else:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            text = f.read()
    
    analyzer = ContentAnalyzer()
    ideas = analyzer.analyze_and_rank(text)
    
    # Output as JSON
    output = {
        'total_ideas': len(ideas),
        'ideas': [idea.to_dict() for idea in ideas]
    }
    
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    main()
