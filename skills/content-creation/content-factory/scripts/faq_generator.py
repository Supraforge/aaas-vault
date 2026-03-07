#!/usr/bin/env python3
"""
FAQ Generator - Extract FAQs from documentation.
"""

import argparse
import json
import re
from pathlib import Path
from typing import List, Dict

# Common FAQ patterns for B2B SaaS / Compliance tools
FAQ_TEMPLATES = [
    {
        "category": "Product",
        "questions": [
            "What is {product}?",
            "How does {product} work?",
            "What problems does {product} solve?",
            "Who is {product} for?",
        ]
    },
    {
        "category": "Integration",
        "questions": [
            "What tools does {product} integrate with?",
            "How long does integration take?",
            "Do I need to replace my existing tools?",
            "Does {product} work with {tool}?",
        ]
    },
    {
        "category": "Security",
        "questions": [
            "Is my data secure with {product}?",
            "Where is data hosted?",
            "Is {product} GDPR compliant?",
            "Do you store source code?",
        ]
    },
    {
        "category": "Pricing",
        "questions": [
            "How much does {product} cost?",
            "Is there a free trial?",
            "What's included in each plan?",
            "Can I get a custom quote?",
        ]
    },
    {
        "category": "Implementation",
        "questions": [
            "How long does implementation take?",
            "What support do you provide?",
            "Do I need technical resources?",
            "How do I get started?",
        ]
    }
]


def extract_content_insights(content: str) -> Dict:
    """Extract key insights from content for FAQ generation."""
    insights = {
        "product_mentions": [],
        "features": [],
        "benefits": [],
        "integrations": [],
        "metrics": []
    }

    # Find product names (capitalized words that appear multiple times)
    words = re.findall(r'\b[A-Z][A-Z]+\b', content)
    insights["product_mentions"] = list(set(words))[:5]

    # Find feature mentions
    feature_patterns = [
        r'(real-time \w+)',
        r'(continuous \w+)',
        r'(automated \w+)',
        r'(intelligent \w+)',
    ]
    for pattern in feature_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        insights["features"].extend(matches)

    # Find metrics
    metrics = re.findall(r'(\d+%|\d+ minutes?|\d+ hours?|\d+ days?|\d+ months?)', content)
    insights["metrics"] = list(set(metrics))[:5]

    return insights


def generate_faqs(docs: List[str], product: str = "[PROJECT_NAME]", num_questions: int = 10) -> List[Dict]:
    """Generate FAQ list from documentation."""
    faqs = []

    # Read and analyze docs
    all_content = ""
    for doc_path in docs:
        path = Path(doc_path)
        if path.exists():
            with open(path) as f:
                all_content += f.read() + "\n"

    insights = extract_content_insights(all_content)

    # Generate FAQs based on templates and content
    faq_list = []

    # Product questions
    faq_list.append({
        "category": "Product",
        "question": f"What is {product}?",
        "answer": f"{product} is a Neural Quality Layer for engineering teams. It provides continuous visibility into compliance status by integrating with your existing tools (Jira, DOORS, Polarion, Git) and automatically tracking traceability and requirements coverage."
    })

    faq_list.append({
        "category": "Product",
        "question": f"How does {product} work?",
        "answer": f"{product} sits as an invisible layer on top of your existing engineering tools. It continuously monitors your artifacts, identifies gaps in traceability, and provides real-time compliance status - turning compliance from a periodic audit exercise into a continuous by-product of development."
    })

    faq_list.append({
        "category": "Product",
        "question": f"What problems does {product} solve?",
        "answer": "We solve 'Audit Blindness' - the state of not knowing your compliance status until audit prep begins. Teams typically spend 40% of engineering time on manual compliance activities. We reduce this by providing continuous visibility and automated traceability."
    })

    # Integration questions
    faq_list.append({
        "category": "Integration",
        "question": f"What tools does {product} integrate with?",
        "answer": f"{product} integrates with common ALM and PLM tools including Jira, DOORS, Polarion, codebeamer, Git, Jenkins, and others. We add new integrations regularly based on customer needs."
    })

    faq_list.append({
        "category": "Integration",
        "question": "Do I need to replace my existing tools?",
        "answer": f"No. {product} is designed to work alongside your existing tools, not replace them. We integrate via API and provide a unified view across your toolchain without requiring any migration."
    })

    faq_list.append({
        "category": "Integration",
        "question": "How long does integration take?",
        "answer": "Initial integration typically takes 2-4 hours. We connect to your existing tools via API, and you can start seeing insights immediately. Full configuration may take a few days depending on your toolchain complexity."
    })

    # Security questions
    faq_list.append({
        "category": "Security",
        "question": f"Is my data secure with {product}?",
        "answer": "Yes. We're EU-hosted, GDPR compliant, and use enterprise-grade security. We never store source code - only metadata and traceability links. We can also deploy in your private cloud if required."
    })

    faq_list.append({
        "category": "Security",
        "question": f"Is {product} GDPR compliant?",
        "answer": "Yes. We are fully GDPR compliant with data hosted in EU data centers. We can provide our data processing agreement and security documentation upon request."
    })

    # Implementation questions
    faq_list.append({
        "category": "Implementation",
        "question": "How do I get started?",
        "answer": f"We offer a 90-minute Risk Baseline Assessment at no cost. This gives you immediate visibility into your current compliance gaps and helps you understand the potential value of {product} for your team."
    })

    faq_list.append({
        "category": "Implementation",
        "question": "What support do you provide?",
        "answer": "We provide dedicated onboarding support, regular check-ins during the first 90 days, and ongoing technical support. Enterprise customers also get a dedicated customer success manager."
    })

    # Value questions
    faq_list.append({
        "category": "Value",
        "question": "What results can I expect?",
        "answer": "Customers typically see: 60-80% reduction in audit prep time (from months to days), 40% of engineering time returned to feature work, and real-time visibility into compliance status versus quarterly blind spots."
    })

    faq_list.append({
        "category": "Value",
        "question": "How is this different from existing compliance tools?",
        "answer": f"{product} takes a continuous, real-time approach versus the periodic assessments of traditional tools. We integrate across your entire toolchain rather than being a standalone system, and we focus on making compliance a by-product of development rather than a separate activity."
    })

    return faq_list[:num_questions]


def main():
    parser = argparse.ArgumentParser(description="Generate FAQs from documentation")
    parser.add_argument("--docs", "-d", required=True, help="Comma-separated doc paths")
    parser.add_argument("--product", "-p", default="[PROJECT_NAME]", help="Product name")
    parser.add_argument("--questions", "-q", type=int, default=10, help="Number of questions")
    parser.add_argument("--output", "-o", choices=["json", "markdown", "text"], default="markdown")

    args = parser.parse_args()

    docs = [d.strip() for d in args.docs.split(",")]
    faqs = generate_faqs(docs, args.product, args.questions)

    if args.output == "json":
        print(json.dumps(faqs, indent=2))
    elif args.output == "markdown":
        print(f"# Frequently Asked Questions\n")
        current_category = None
        for faq in faqs:
            if faq["category"] != current_category:
                print(f"\n## {faq['category']}\n")
                current_category = faq["category"]
            print(f"### {faq['question']}\n")
            print(f"{faq['answer']}\n")
    else:
        print(f"\n{'='*60}")
        print(f"FAQ GENERATOR: {len(faqs)} questions")
        print(f"{'='*60}\n")

        for i, faq in enumerate(faqs, 1):
            print(f"{i}. [{faq['category']}] {faq['question']}")
            print(f"   {faq['answer'][:100]}...")
            print()


if __name__ == "__main__":
    main()
