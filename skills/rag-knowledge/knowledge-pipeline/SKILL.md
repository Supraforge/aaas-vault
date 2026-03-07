---
name: knowledge-pipeline
description: >-
  - **Name**: knowledge-pipeline - **Version**: 1.1 - **Purpose**: Build rich
  knowledge context using RAG + PubMed before writing - **Trigger**: Any content
  creation task requiring evidence-based writing
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---
# Knowledge Pipeline Skill

## Metadata
- **Name**: knowledge-pipeline
- **Version**: 1.1
- **Purpose**: Build rich knowledge context using RAG + PubMed before writing
- **Trigger**: Any content creation task requiring evidence-based writing

## Overview

This skill implements a **parallel knowledge building pipeline** that queries BOTH:

1. **RAG Pipeline** - Your AstraDB vector store containing cardiology textbooks and guidelines
2. **PubMed Pipeline** - Latest research via NCBI E-utilities API

**NOTE**: Perplexity is used SEPARATELY for social listening and demand assessment (YouTube workflow), NOT for research/evidence gathering.

## When to Use

**ALWAYS use this skill BEFORE writing content that requires:**
- Evidence-based claims
- Statistics or study citations
- Guideline references
- Current best practices
- Recent trial results

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                 KNOWLEDGE PIPELINE (Research)                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Question ──┬──► RAG Pipeline ──────────────────────────────│
│             │    (AstraDB Vector Store)                      │
│             │    - YOUR textbooks (Braunwald, etc.)          │
│             │    - Guidelines (ESC, ACC, AHA)                │
│             │    - Reference materials                       │
│             │    Tech: Vector + BM25 + RRF + Cohere rerank   │
│             │                                                │
│             └──► PubMed Pipeline ───────────────────────────│
│                  (NCBI E-utilities API)                      │
│                  - Latest research articles                  │
│                  - Systematic reviews                        │
│                  - Meta-analyses                             │
│                  - Clinical trials                           │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                       SYNTHESIS                              │
│  Combined context ──► GPT-4o-mini ──► Knowledge Brief       │
│                                                              │
│  Output:                                                     │
│  1. Established Knowledge (guidelines)                       │
│  2. Latest Research (PubMed)                                 │
│  3. Key Data Points                                          │
│  4. Areas of Consensus                                       │
│  5. Areas of Uncertainty                                     │
│  6. Citation Summary                                         │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│              SEPARATE: DEMAND ASSESSMENT (YouTube)           │
├─────────────────────────────────────────────────────────────┤
│  Perplexity ──► Social listening, trends, what people ask   │
│  Free LLMs  ──► Demand analysis from YouTube comments       │
│                                                              │
│  This is NOT research. This is audience intelligence.        │
└─────────────────────────────────────────────────────────────┘
```

## Usage

### Python Integration

```python
from rag_pipeline.src.knowledge_pipeline import KnowledgePipeline

pipeline = KnowledgePipeline(verbose=True)

# Option 1: Get raw combined context
context = pipeline.build_knowledge_context(
    "What are optimal LDL targets for high-risk patients?"
)

# Option 2: Get synthesized knowledge brief
brief = pipeline.synthesize_knowledge(
    "What are optimal LDL targets for high-risk patients?"
)
```

### CLI Usage

```bash
cd "/Users/shaileshsingh/cowriting system/rag-pipeline"
python src/knowledge_pipeline.py
```

## Configuration

### Environment Variables (in .env)

```bash
# RAG Pipeline (AstraDB)
ASTRA_DB_APPLICATION_TOKEN=your_token
ASTRA_DB_API_ENDPOINT=your_endpoint
ASTRA_DB_COLLECTION=documents
OPENAI_API_KEY=your_key
COHERE_API_KEY=your_key

# PubMed Pipeline
NCBI_API_key=your_key
```

## Output Format

### Raw Context (build_knowledge_context)

```
## FROM TEXTBOOKS & GUIDELINES (RAG)
--------------------------------------------------
[Source 1: ESC Guidelines 2021.pdf, Page 45] (Score: 0.892)
LDL-C targets for patients with established CVD...

[Source 2: Braunwald Cardiology.pdf, Page 1203] (Score: 0.856)
The evidence for aggressive LDL lowering...

## FROM PUBMED (Latest Research)
--------------------------------------------------
[1] PMID: 38123456
    Smith, Jones, Brown et al. (2024)
    Novel LDL-C targets in high-risk populations
    Journal of the American College of Cardiology
    Abstract: Recent meta-analysis of 15 trials...

==================================================
KNOWLEDGE SUMMARY
- RAG chunks (textbooks/guidelines): 8
- PubMed articles (latest research): 5
- Total sources: 13
==================================================
```

## Priority When Sources Conflict

1. **Highest**: Established guidelines from RAG (ESC, ACC, AHA)
2. **High**: Major trials and meta-analyses (RAG + PubMed)
3. **Medium**: Recent updates not yet in guidelines (PubMed)
4. **Lower**: Single studies, expert opinion

## Integration with Writing Skills

This skill feeds into ALL writing skills:

1. **cardiology-writer** - Uses knowledge brief for factual grounding
2. **cardiology-newsletter-writer** - Research phase uses this pipeline
3. **cardiology-editorial** - Evidence synthesis from both sources
4. **youtube-script-master** - Educational sections use RAG + PubMed context

## Cost Estimates

| Component | Model/Service | Cost per Query |
|-----------|---------------|----------------|
| RAG Embeddings | text-embedding-3-small | ~$0.001 |
| RAG Reranking | Cohere rerank-english-v3.0 | ~$0.01 |
| PubMed API | NCBI E-utilities | Free |
| Synthesis | GPT-4o-mini | ~$0.002 |
| **Total** | | **~$0.013/query** |

## Maintenance

### Adding New Documents to RAG

```bash
cd "/Users/shaileshsingh/cowriting system/rag-pipeline"
python src/ingest_documents.py --folder /path/to/new/pdfs
```

### Rebuilding BM25 Index

Delete cache files to force rebuild:
```bash
rm .bm25_cache.pkl .doc_cache.json
```
