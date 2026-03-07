#!/usr/bin/env python3
"""
Scientific Skills Router for Cardiology

Maps cardiology content creation needs to the 135 scientific skills.
Provides intelligent routing based on use case, topic, and data needs.

Usage:
    from scientific_skills_router import ScientificSkillsRouter

    router = ScientificSkillsRouter()

    # Find skills for a specific use case
    skills = router.get_skills_for_use_case("find clinical trials for SGLT2")

    # Get skills for a cardiology topic
    skills = router.get_skills_for_topic("statins")

    # Get all database skills
    skills = router.get_database_skills()
"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, field


@dataclass
class ScientificSkill:
    """Represents a scientific skill with cardiology relevance."""
    id: str
    name: str
    description: str
    category: str
    cardiology_use_cases: List[str] = field(default_factory=list)
    related_topics: List[str] = field(default_factory=list)
    has_scripts: bool = False
    skill_path: str = ""


# Cardiology-relevant scientific skill mappings
CARDIOLOGY_SKILL_MAPPINGS = {
    # === CLINICAL DATABASES ===
    "clinicaltrials-database": {
        "category": "clinical-database",
        "cardiology_use_cases": [
            "Find ongoing trials for heart failure drugs",
            "Research SGLT2 inhibitor trial data",
            "Find recruiting cardiology studies",
            "Track landmark trial status",
            "Find trials for specific patient populations"
        ],
        "related_topics": [
            "clinical trials", "heart failure", "statins", "PCSK9",
            "SGLT2", "GLP-1", "ARNI", "anticoagulants"
        ]
    },
    "clinvar-database": {
        "category": "clinical-database",
        "cardiology_use_cases": [
            "Find genetic variants linked to cardiomyopathy",
            "Research familial hypercholesterolemia variants",
            "Identify arrhythmia-related mutations",
            "Long QT syndrome genetics"
        ],
        "related_topics": [
            "genetics", "cardiomyopathy", "arrhythmia", "familial hypercholesterolemia",
            "long QT", "Brugada syndrome", "hypertrophic cardiomyopathy"
        ]
    },
    "drugbank-database": {
        "category": "clinical-database",
        "cardiology_use_cases": [
            "Research drug interactions for cardiac medications",
            "Find mechanism of action for statins",
            "Check drug-drug interactions",
            "Research new cardiac drug targets"
        ],
        "related_topics": [
            "statins", "anticoagulants", "antihypertensives", "beta blockers",
            "ACE inhibitors", "ARBs", "calcium channel blockers", "antiarrhythmics"
        ]
    },
    "fda-database": {
        "category": "clinical-database",
        "cardiology_use_cases": [
            "Check FDA approvals for new cardiac drugs",
            "Research drug safety alerts",
            "Find black box warnings",
            "Track drug approval history"
        ],
        "related_topics": [
            "drug approvals", "safety alerts", "black box warnings",
            "drug recalls", "new indications"
        ]
    },
    "pubmed-database": {
        "category": "research-database",
        "cardiology_use_cases": [
            "Literature search for cardiac topics",
            "Find systematic reviews",
            "Research evidence for treatments",
            "Find recent publications"
        ],
        "related_topics": [
            "all cardiology topics"
        ]
    },
    "gwas-database": {
        "category": "research-database",
        "cardiology_use_cases": [
            "Find genetic associations with CVD",
            "Research polygenic risk scores",
            "Identify CAD risk variants"
        ],
        "related_topics": [
            "genetics", "CAD", "heart failure", "atrial fibrillation",
            "hypertension", "lipids"
        ]
    },
    "opentargets-database": {
        "category": "research-database",
        "cardiology_use_cases": [
            "Find drug targets for CVD",
            "Research target-disease associations",
            "Identify new therapeutic targets"
        ],
        "related_topics": [
            "drug targets", "therapeutic targets", "CVD", "heart failure"
        ]
    },

    # === DATA ANALYSIS ===
    "plotly": {
        "category": "visualization",
        "cardiology_use_cases": [
            "Create interactive trial result charts",
            "Visualize forest plots",
            "Generate Kaplan-Meier curves",
            "Create risk factor comparison charts"
        ],
        "related_topics": [
            "data visualization", "charts", "graphs", "trial results"
        ]
    },
    "matplotlib": {
        "category": "visualization",
        "cardiology_use_cases": [
            "Create publication-quality figures",
            "Generate ECG visualizations",
            "Create statistical plots"
        ],
        "related_topics": [
            "figures", "plots", "ECG", "statistics"
        ]
    },
    "scikit-learn": {
        "category": "machine-learning",
        "cardiology_use_cases": [
            "Build CVD risk prediction models",
            "Classify patient risk categories",
            "Analyze trial outcome predictors"
        ],
        "related_topics": [
            "machine learning", "risk prediction", "classification", "clustering"
        ]
    },
    "statsmodels": {
        "category": "statistics",
        "cardiology_use_cases": [
            "Perform survival analysis",
            "Calculate hazard ratios",
            "Statistical modeling for trials"
        ],
        "related_topics": [
            "statistics", "survival analysis", "regression", "hazard ratios"
        ]
    },
    "scikit-survival": {
        "category": "statistics",
        "cardiology_use_cases": [
            "Survival analysis for trial data",
            "Time-to-event modeling",
            "Risk stratification"
        ],
        "related_topics": [
            "survival analysis", "Kaplan-Meier", "Cox regression", "time-to-event"
        ]
    },

    # === BIOINFORMATICS ===
    "biopython": {
        "category": "bioinformatics",
        "cardiology_use_cases": [
            "Analyze cardiac gene sequences",
            "Process genomic data",
            "Protein structure analysis"
        ],
        "related_topics": [
            "genomics", "proteomics", "sequences", "genetics"
        ]
    },
    "bioservices": {
        "category": "bioinformatics",
        "cardiology_use_cases": [
            "Access multiple biological databases",
            "Cross-reference gene data",
            "Pathway analysis"
        ],
        "related_topics": [
            "databases", "pathways", "genes", "proteins"
        ]
    },
    "neurokit2": {
        "category": "signal-processing",
        "cardiology_use_cases": [
            "Analyze ECG signals",
            "Heart rate variability analysis",
            "Process cardiac waveforms"
        ],
        "related_topics": [
            "ECG", "HRV", "cardiac signals", "waveform analysis"
        ]
    },

    # === LITERATURE & WRITING ===
    "literature-review": {
        "category": "writing",
        "cardiology_use_cases": [
            "Systematic literature reviews",
            "Evidence synthesis",
            "Research summaries"
        ],
        "related_topics": [
            "literature", "reviews", "evidence", "synthesis"
        ]
    },
    "citation-management": {
        "category": "writing",
        "cardiology_use_cases": [
            "Manage references for articles",
            "Format citations",
            "Build bibliographies"
        ],
        "related_topics": [
            "citations", "references", "bibliography"
        ]
    },
    "peer-review": {
        "category": "writing",
        "cardiology_use_cases": [
            "Review manuscript quality",
            "Identify methodological issues",
            "Assess statistical validity"
        ],
        "related_topics": [
            "peer review", "manuscripts", "quality", "methodology"
        ]
    },
    "clinical-decision-support": {
        "category": "clinical",
        "cardiology_use_cases": [
            "Generate GRADE evidence summaries",
            "Create clinical guidelines content",
            "Develop decision support tools"
        ],
        "related_topics": [
            "GRADE", "guidelines", "evidence", "clinical decisions"
        ]
    },
    "clinical-reports": {
        "category": "clinical",
        "cardiology_use_cases": [
            "Create case reports",
            "Generate clinical documentation",
            "Write diagnostic reports"
        ],
        "related_topics": [
            "case reports", "documentation", "diagnosis"
        ]
    },

    # === DATA PROCESSING ===
    "polars": {
        "category": "data-processing",
        "cardiology_use_cases": [
            "Process large clinical datasets",
            "Fast data manipulation",
            "Trial data analysis"
        ],
        "related_topics": [
            "data processing", "dataframes", "large datasets"
        ]
    },
    "dask": {
        "category": "data-processing",
        "cardiology_use_cases": [
            "Parallel processing of trial data",
            "Large-scale data analysis",
            "Distributed computing"
        ],
        "related_topics": [
            "parallel processing", "big data", "distributed"
        ]
    },

    # === SPECIALIZED ===
    "pydicom": {
        "category": "imaging",
        "cardiology_use_cases": [
            "Process cardiac imaging data",
            "Read DICOM echocardiograms",
            "Analyze CT/MRI cardiac scans"
        ],
        "related_topics": [
            "imaging", "DICOM", "echocardiography", "cardiac CT", "cardiac MRI"
        ]
    },
    "pyhealth": {
        "category": "clinical-ml",
        "cardiology_use_cases": [
            "Build clinical NLP models",
            "Process EHR data",
            "Clinical prediction models"
        ],
        "related_topics": [
            "EHR", "clinical NLP", "prediction models"
        ]
    },
    "exploratory-data-analysis": {
        "category": "analysis",
        "cardiology_use_cases": [
            "Explore trial datasets",
            "Identify data patterns",
            "Generate summary statistics"
        ],
        "related_topics": [
            "EDA", "data exploration", "statistics", "patterns"
        ]
    },
    "perplexity-search": {
        "category": "research",
        "cardiology_use_cases": [
            "Quick research on cardiac topics",
            "Find recent news and updates",
            "Fact-checking"
        ],
        "related_topics": [
            "search", "research", "news", "updates"
        ]
    }
}

# Category to skill IDs mapping
CATEGORY_SKILLS = {
    "clinical-database": [
        "clinicaltrials-database", "clinvar-database", "drugbank-database",
        "fda-database", "hmdb-database", "clinpgx-database"
    ],
    "research-database": [
        "pubmed-database", "gwas-database", "opentargets-database",
        "biorxiv-database", "openalex-database", "gene-database"
    ],
    "visualization": [
        "plotly", "matplotlib", "networkx"
    ],
    "statistics": [
        "statsmodels", "scikit-survival", "pymc"
    ],
    "machine-learning": [
        "scikit-learn", "pytorch-lightning", "deepchem"
    ],
    "bioinformatics": [
        "biopython", "bioservices", "scanpy", "anndata", "scvi-tools"
    ],
    "signal-processing": [
        "neurokit2"
    ],
    "writing": [
        "literature-review", "citation-management", "peer-review",
        "clinical-decision-support", "clinical-reports"
    ],
    "data-processing": [
        "polars", "dask", "geopandas"
    ],
    "imaging": [
        "pydicom", "pathml", "histolab"
    ],
    "clinical-ml": [
        "pyhealth"
    ],
    "analysis": [
        "exploratory-data-analysis"
    ],
    "research": [
        "perplexity-search"
    ]
}


class ScientificSkillsRouter:
    """Routes cardiology content needs to scientific skills."""

    def __init__(self, skills_root: Optional[Path] = None):
        """Initialize the router."""
        if skills_root:
            self.skills_root = skills_root
        else:
            # Default relative to this script
            self.skills_root = Path(__file__).parent.parent.parent.parent / "scientific"

        self.skills: Dict[str, ScientificSkill] = {}
        self._load_skills()

    def _load_skills(self):
        """Load and index all scientific skills."""
        if not self.skills_root.exists():
            print(f"Warning: Scientific skills directory not found: {self.skills_root}")
            return

        for skill_dir in self.skills_root.iterdir():
            if not skill_dir.is_dir():
                continue

            skill_id = skill_dir.name
            skill_md = skill_dir / "SKILL.md"

            if not skill_md.exists():
                continue

            # Get description from SKILL.md
            description = self._extract_description(skill_md)

            # Check for scripts
            has_scripts = (skill_dir / "scripts").exists()

            # Get cardiology mappings if available
            mapping = CARDIOLOGY_SKILL_MAPPINGS.get(skill_id, {})

            self.skills[skill_id] = ScientificSkill(
                id=skill_id,
                name=skill_id.replace("-", " ").title(),
                description=description,
                category=mapping.get("category", "general"),
                cardiology_use_cases=mapping.get("cardiology_use_cases", []),
                related_topics=mapping.get("related_topics", []),
                has_scripts=has_scripts,
                skill_path=str(skill_dir)
            )

    def _extract_description(self, skill_md: Path) -> str:
        """Extract description from SKILL.md frontmatter."""
        try:
            content = skill_md.read_text()
            # Look for description in frontmatter
            if content.startswith("---"):
                end = content.find("---", 3)
                if end > 0:
                    frontmatter = content[3:end]
                    for line in frontmatter.split("\n"):
                        if line.startswith("description:"):
                            return line.split(":", 1)[1].strip().strip('"')
            # Fallback: first paragraph after header
            lines = content.split("\n")
            for i, line in enumerate(lines):
                if line.startswith("## ") or line.startswith("# "):
                    # Get next non-empty line
                    for j in range(i+1, min(i+5, len(lines))):
                        if lines[j].strip() and not lines[j].startswith("#"):
                            return lines[j].strip()[:200]
            return "Scientific skill for data analysis and research"
        except Exception:
            return "Scientific skill"

    def get_skills_for_use_case(self, query: str) -> List[ScientificSkill]:
        """Find skills matching a use case query."""
        query_lower = query.lower()
        results = []

        for skill in self.skills.values():
            score = 0

            # Check use cases
            for use_case in skill.cardiology_use_cases:
                if any(word in use_case.lower() for word in query_lower.split()):
                    score += 3

            # Check related topics
            for topic in skill.related_topics:
                if topic.lower() in query_lower or query_lower in topic.lower():
                    score += 2

            # Check description
            if any(word in skill.description.lower() for word in query_lower.split() if len(word) > 3):
                score += 1

            if score > 0:
                results.append((score, skill))

        # Sort by score descending
        results.sort(key=lambda x: x[0], reverse=True)
        return [skill for _, skill in results[:10]]

    def get_skills_for_topic(self, topic: str) -> List[ScientificSkill]:
        """Get skills relevant to a cardiology topic."""
        topic_lower = topic.lower()
        results = []

        for skill in self.skills.values():
            if any(topic_lower in t.lower() or t.lower() in topic_lower
                   for t in skill.related_topics):
                results.append(skill)
            elif "all cardiology topics" in skill.related_topics:
                results.append(skill)

        return results

    def get_database_skills(self) -> List[ScientificSkill]:
        """Get all database access skills."""
        db_ids = set(CATEGORY_SKILLS.get("clinical-database", []) +
                     CATEGORY_SKILLS.get("research-database", []))
        return [self.skills[sid] for sid in db_ids if sid in self.skills]

    def get_skills_by_category(self, category: str) -> List[ScientificSkill]:
        """Get skills by category."""
        skill_ids = CATEGORY_SKILLS.get(category, [])
        return [self.skills[sid] for sid in skill_ids if sid in self.skills]

    def get_cardiology_relevant_skills(self) -> List[ScientificSkill]:
        """Get all skills with cardiology mappings."""
        return [skill for skill in self.skills.values()
                if skill.cardiology_use_cases]

    def generate_routing_guide(self) -> str:
        """Generate a human-readable routing guide."""
        lines = [
            "# Scientific Skills Routing Guide for Cardiology",
            "",
            "## Quick Reference",
            "",
            "| Need | Skill | Example Use Case |",
            "|------|-------|------------------|"
        ]

        for skill in self.get_cardiology_relevant_skills():
            use_case = skill.cardiology_use_cases[0] if skill.cardiology_use_cases else "-"
            lines.append(f"| {skill.category} | `{skill.id}` | {use_case} |")

        lines.extend([
            "",
            "## By Category",
            ""
        ])

        for category, skill_ids in CATEGORY_SKILLS.items():
            lines.append(f"### {category.replace('-', ' ').title()}")
            lines.append("")
            for sid in skill_ids:
                if sid in self.skills:
                    skill = self.skills[sid]
                    lines.append(f"- **{skill.id}**: {skill.description[:100]}...")
            lines.append("")

        return "\n".join(lines)

    def to_json(self) -> str:
        """Export skills mapping to JSON."""
        data = {
            "cardiology_relevant_skills": [
                {
                    "id": s.id,
                    "name": s.name,
                    "category": s.category,
                    "use_cases": s.cardiology_use_cases,
                    "topics": s.related_topics,
                    "has_scripts": s.has_scripts
                }
                for s in self.get_cardiology_relevant_skills()
            ],
            "category_index": CATEGORY_SKILLS
        }
        return json.dumps(data, indent=2)


def main():
    """CLI for testing the router."""
    import argparse

    parser = argparse.ArgumentParser(description="Scientific Skills Router for Cardiology")
    parser.add_argument("--query", help="Search for skills by use case")
    parser.add_argument("--topic", help="Get skills for a cardiology topic")
    parser.add_argument("--category", help="Get skills by category")
    parser.add_argument("--list-databases", action="store_true", help="List all database skills")
    parser.add_argument("--generate-guide", action="store_true", help="Generate routing guide")
    parser.add_argument("--export-json", action="store_true", help="Export to JSON")

    args = parser.parse_args()
    router = ScientificSkillsRouter()

    if args.query:
        skills = router.get_skills_for_use_case(args.query)
        print(f"\nSkills matching '{args.query}':\n")
        for skill in skills:
            print(f"  {skill.id}")
            if skill.cardiology_use_cases:
                print(f"    Use cases: {', '.join(skill.cardiology_use_cases[:2])}")
            print()

    elif args.topic:
        skills = router.get_skills_for_topic(args.topic)
        print(f"\nSkills for topic '{args.topic}':\n")
        for skill in skills:
            print(f"  {skill.id}: {skill.description[:80]}...")

    elif args.category:
        skills = router.get_skills_by_category(args.category)
        print(f"\nSkills in category '{args.category}':\n")
        for skill in skills:
            print(f"  {skill.id}")

    elif args.list_databases:
        skills = router.get_database_skills()
        print("\nDatabase skills:\n")
        for skill in skills:
            print(f"  {skill.id}: {skill.description[:80]}...")

    elif args.generate_guide:
        print(router.generate_routing_guide())

    elif args.export_json:
        print(router.to_json())

    else:
        # Default: show summary
        print(f"\nScientific Skills Router")
        print(f"========================")
        print(f"Total skills loaded: {len(router.skills)}")
        print(f"Cardiology-relevant: {len(router.get_cardiology_relevant_skills())}")
        print(f"\nCategories: {', '.join(CATEGORY_SKILLS.keys())}")
        print(f"\nRun with --help for usage options")


if __name__ == "__main__":
    main()
