---
name: cardiology-newsletter-writer
description: >-
  Create evidence-based cardiology newsletters for thought leadership in Eric
  Topol's authoritative Ground Truths style. Use when the user wants to analyze
  trending medical topics with engagement predictions, conduct data-driven topic
  selection, research medical literature using PubMed, or write comprehensive
  well-referenced newsletters that build professional authority as an
  interventional cardiologist. Handles complete workflow from trend analysis to
  final draft with smooth analytical flow between topics.
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---

# Cardiology Newsletter Writer

Write thought leadership newsletters for interventional cardiologists in Eric Topol's authoritative, evidence-based style from Ground Truths.

## Workflow

### Phase 1: Topic Discovery and Trend Analysis

1. **Search target journals** for recent publications (last 2-4 weeks):
   - High-impact general: NEJM, JAMA, Lancet, BMJ
   - Cardiology tier-1: JACC, EHJ, Circulation, JAMA Cardiology
   - Interventional focus: JACC: Cardiovascular Interventions, Circulation: Cardiovascular Interventions, EuroIntervention, Catheterization and Cardiovascular Interventions, JSCAI

2. **Identify trending topics** using web_search:
   - Search for cardiology news trends in India
   - Check Google Trends, YouTube, social media discussions
   - Look for topics with high engagement potential

3. **Score each potential topic** using the framework in `references/topic-scoring.md`

4. **Present findings** to user in a structured table showing:
   - Topic/trial name
   - Journal and publication date
   - Predicted engagement score (0-100)
   - Key findings (1-2 sentences)
   - Why it matters for interventional cardiology

5. **Get user approval** on which topics to include before proceeding

### Phase 2: Deep Research

For each approved topic:

1. **Retrieve full articles** using PubMed MCP tools:
   - Get PMIDs from search
   - Convert to PMCIDs if available
   - Fetch full text or detailed abstracts
   - Get related trials for context

2. **Build contextual foundation**:
   - Identify landmark prior trials (e.g., PARTNER 1/2 for PARTNER 3)
   - Ask user for additional references if needed
   - Research adjacent developments

3. **Analyze evidence**:
   - Trial design and methodology
   - Primary and secondary endpoints
   - Results with specific numbers
   - Limitations and biases
   - Clinical implications
   - How this fits into existing literature

### Phase 3: Newsletter Drafting

Follow the style guide in `references/topol-style-guide.md` meticulously.

**Key principles:**
- Write as Eric Topol would: authoritative, analytical, accessible
- Dense scientific content for physician readers
- Smooth transitions between topics (coronary → structural via shared risk profiles)
- Ground every claim in cited research
- Use specific data points, not vague claims
- Natural prose paragraphs, minimal formatting
- Position user as trusted authority

**Structure:**
- Opening: Hook with most important development
- Body: 2-4 major topics with analytical depth
- Each topic: Context → Study details → Results → Implications
- Transitions: Link topics via shared themes (tech, populations, risk factors)
- Closing: Forward-looking perspective or open question

**Citations:**
- Use PubMed citations with DOIs
- Format: "A recent NEJM study showed..." with proper attribution
- Include trial acronyms in natural flow

**Anti-AI guidelines** (critical - see references/anti-ai-guidelines.md):
- No promotional phrases ("stands as," "plays a vital role")
- No editorializing ("it's important to note")
- No summary endings ("In conclusion")
- Sentence case headings only
- Minimal bold text
- No formulaic lists unless essential
- Varied sentence structures
- Direct contrast requires 2-3 sentence spacing

### Phase 4: Review and Refinement

1. **Self-check against anti-AI guidelines**
2. **Verify all citations** are accurate
3. **Check flow** between sections
4. **Ensure Topol voice** is consistent
5. Present draft to user for feedback

## When to Use References

- `references/topic-scoring.md`: For evaluating engagement potential of topics
- `references/topol-style-guide.md`: Before and during drafting
- `references/anti-ai-guidelines.md`: During drafting and final review
- `references/journal-list.md`: For comprehensive journal coverage

## Important Notes

- **Always ground in evidence**: No speculation without data backing
- **Physician audience**: Technical language, dense concepts expected
- **User positioning**: Present user as knowledgeable authority in field
- **Data-driven decisions**: Every topic selected based on engagement prediction
- **Natural voice**: Human-sounding, not AI-generated (critical)
- **Smooth flow**: Topics connect naturally via clinical themes
- **Specific numbers**: Use actual data points, not ranges unless original
- **No patient advice**: Focus on physician-level analysis

## Output Format

Final newsletter as markdown document with:
- Compelling title (Topol-style)
- 500-1500 words depending on complexity
- 2-4 major topics
- Full citations with DOIs
- Natural paragraph structure
- Analytical depth throughout
