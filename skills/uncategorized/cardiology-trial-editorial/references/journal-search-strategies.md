# Target Journals and Search Strategies

Prioritized list of cardiology journals for trial discovery, with PubMed search strategies.

## Journal Hierarchy by Impact Factor

### Tier 1: General Medicine (Highest Impact)
1. **New England Journal of Medicine (NEJM)** - IF: ~158
   - PubMed search: `"N Engl J Med"[Journal]`
   - Focus: Landmark trials, often multi-specialty
   - Cardiology frequency: 2-3 major trials/month

2. **The Lancet** - IF: ~168
   - PubMed search: `"Lancet"[Journal]`
   - Focus: International trials, public health angle
   - Cardiology frequency: 1-2 major trials/month

3. **JAMA** - IF: ~120
   - PubMed search: `"JAMA"[Journal]`
   - Focus: Practice-changing trials, US-centric
   - Cardiology frequency: 1-2 major trials/month

### Tier 1: Cardiology Specialist (Very High Impact)
4. **Journal of the American College of Cardiology (JACC)** - IF: ~24
   - PubMed search: `"J Am Coll Cardiol"[Journal]`
   - Focus: Broad cardiology, high-quality trials
   - Editorial sweet spot: 3-4 landmark trials/month

5. **European Heart Journal (EHJ)** - IF: ~39
   - PubMed search: `"Eur Heart J"[Journal]`
   - Focus: European trials, imaging, prevention
   - Editorial sweet spot: 2-3 landmark trials/month

6. **Circulation** - IF: ~37
   - PubMed search: `"Circulation"[Journal]`
   - Focus: AHA journal, mechanistic + clinical
   - Editorial sweet spot: 2-3 major trials/month

### Tier 2: Subspecialty High Impact
7. **JACC: Cardiovascular Interventions** - IF: ~12
   - PubMed search: `"JACC Cardiovasc Interv"[Journal]`
   - Focus: Interventional cardiology trials
   - **Prime territory for interventional cardiologist**
   - Editorial sweet spot: 2-4 trials/month

8. **Circulation: Cardiovascular Interventions** - IF: ~7
   - PubMed search: `"Circ Cardiovasc Interv"[Journal]`
   - Focus: PCI, structural, peripheral interventions
   - Editorial sweet spot: 1-2 trials/month

9. **EuroIntervention** - IF: ~4
   - PubMed search: `"EuroIntervention"[Journal]`
   - Focus: European interventional trials, devices
   - Editorial sweet spot: 1-2 trials/month

### Tier 3: Subspecialty Focused
10. **JSCAI (Journal of the Society for Cardiovascular Angiography and Interventions)** - IF: ~3
    - PubMed search: `"J Soc Cardiovasc Angiogr Interv"[Journal]` OR `"JSCAI"[Journal]`
    - Focus: SCAI society journal, emerging data
    - Editorial opportunity: 1 trial/month

11. **Catheterization and Cardiovascular Interventions (CCI)** - IF: ~3
    - PubMed search: `"Catheter Cardiovasc Interv"[Journal]`
    - Focus: Technical interventional studies
    - Editorial opportunity: 1 trial/month

### Also Monitor (JAMA Family)
12. **JAMA Cardiology** - IF: ~18
    - PubMed search: `"JAMA Cardiol"[Journal]`
    - Focus: High-quality cardiology trials
    - Editorial sweet spot: 2-3 trials/month

## Search Strategies by Priority

### Strategy 1: High-Impact Sweep (Daily/Weekly)
Prioritize journals most likely to publish practice-changing trials.

```
PubMed search query:
("N Engl J Med"[Journal] OR "Lancet"[Journal] OR "JAMA"[Journal] OR 
"J Am Coll Cardiol"[Journal] OR "Eur Heart J"[Journal] OR 
"Circulation"[Journal] OR "JACC Cardiovasc Interv"[Journal] OR 
"JAMA Cardiol"[Journal]) AND 
("randomized controlled trial"[Publication Type] OR "meta-analysis"[Publication Type]) AND 
("cardiovascular"[All Fields] OR "cardiac"[All Fields] OR "coronary"[All Fields] OR 
"heart"[All Fields] OR "aortic"[All Fields] OR "mitral"[All Fields])
```

Date filter: Past 30 days

Expected yield: 15-25 trials/month

### Strategy 2: Interventional Focus (Weekly)
For interventional cardiology specialist audience.

```
PubMed search query:
("JACC Cardiovasc Interv"[Journal] OR "Circ Cardiovasc Interv"[Journal] OR 
"EuroIntervention"[Journal] OR "Catheter Cardiovasc Interv"[Journal] OR 
"J Soc Cardiovasc Angiogr Interv"[Journal]) AND 
("randomized controlled trial"[Publication Type] OR "prospective"[All Fields]) AND 
("percutaneous coronary intervention"[All Fields] OR "PCI"[All Fields] OR 
"TAVR"[All Fields] OR "transcatheter"[All Fields] OR "structural heart"[All Fields] OR 
"mitral clip"[All Fields] OR "left atrial appendage"[All Fields])
```

Date filter: Past 30 days

Expected yield: 10-15 trials/month

### Strategy 3: Topic-Specific Deep Dive
When focusing on specific intervention or condition.

**Example: TAVR/Structural Heart**
```
("transcatheter aortic valve"[All Fields] OR "TAVR"[All Fields] OR 
"TAVI"[All Fields] OR "mitral valve repair"[All Fields] OR 
"MitraClip"[All Fields] OR "tricuspid valve"[All Fields]) AND 
("randomized controlled trial"[Publication Type] OR "prospective"[All Fields])
```

**Example: Complex PCI**
```
("chronic total occlusion"[All Fields] OR "CTO"[All Fields] OR 
"left main"[All Fields] OR "bifurcation"[All Fields] OR 
"multivessel PCI"[All Fields] OR "drug-eluting stent"[All Fields]) AND 
("randomized controlled trial"[Publication Type] OR "registry"[All Fields])
```

**Example: Heart Failure Interventions**
```
("heart failure"[All Fields] AND ("device"[All Fields] OR "intervention"[All Fields])) AND 
("cardiac resynchronization"[All Fields] OR "CRT"[All Fields] OR 
"left ventricular assist"[All Fields] OR "LVAD"[All Fields] OR 
"mitral regurgitation"[All Fields] AND "heart failure"[All Fields])
```

### Strategy 4: Meta-Analyses and Guidelines
When individual trials are sparse, synthesize evidence.

```
("meta-analysis"[Publication Type] OR "systematic review"[Publication Type] OR 
"guideline"[Publication Type]) AND 
("cardiovascular"[All Fields] OR "cardiology"[All Fields]) AND 
("JACC"[Journal] OR "Eur Heart J"[Journal] OR "Circulation"[Journal] OR 
"N Engl J Med"[Journal] OR "Lancet"[Journal])
```

Date filter: Past 90 days

Expected yield: 5-10 high-quality reviews/month

## Trial Discovery Workflow

### Step-by-Step Process

1. **Weekly high-impact sweep** (Strategy 1)
   - Run search for past 7 days
   - Retrieve PMIDs for all results
   - Extract abstracts using PubMed:get_article_metadata

2. **Score all trials** using trial-scoring system
   - Run LLM metadata extraction on each abstract
   - Calculate importance scores
   - Rank order by score

3. **Weekly interventional focus** (Strategy 2)
   - Run search for past 7 days
   - Add to candidate pool
   - Re-score and re-rank combined pool

4. **Identify top 5 candidates**
   - Present to user with scores and summaries
   - User selects or requests alternatives

5. **If no strong candidates**, expand:
   - Increase date range to 30 days
   - Run Strategy 4 (meta-analyses)
   - Consider topic-specific deep dive (Strategy 3)

### Seasonality and Conference Timing

**Peak trial publication months:**
- **March**: ACC conference → high JACC, JACC-CI output
- **May**: ESC conference → high EHJ, EuroIntervention output
- **August**: ESC congress → late-breaking trials
- **November**: AHA conference → high Circulation output

**Adjust search strategy:**
- During conference months: search daily, not weekly
- Post-conference (1-2 months later): expect embargoed trials to publish

## Special Scenarios

### Negative Trials
Don't overlook high-quality null results:
```
Additional filter: "no significant difference"[All Fields] OR "non-inferiority"[All Fields]
```

Negative trials can be just as important as positive ones for editorial purposes.

### Device/Procedural Studies
May not use "randomized controlled trial" MeSH term:
```
Alternative filter: "prospective"[All Fields] AND "consecutive"[All Fields]
```

### Registry Studies
Large-scale real-world data:
```
"registry"[All Fields] OR "database"[All Fields] AND "outcomes"[All Fields]
AND sample size filter: look for N > 10,000
```

### Controversies and Retractions
Monitor for debates worth editorializing:
```
"retracted"[All Fields] OR "concern"[All Fields] OR "controversy"[All Fields]
```

Rare, but high editorial value when legitimate scientific debate emerges.

## Automation Notes

For systematic trial discovery, ideal workflow:

1. **Daily automated PubMed search** (Strategy 1)
2. **Extract metadata** for all new results
3. **Score trials** using importance algorithm
4. **Alert user** when high-scoring trial (>12 points) appears
5. **Present top 3-5 weekly** for editorial selection

This ensures user never misses landmark trials while avoiding alert fatigue.

## Quality Filters

Beyond journal and study design, consider:

**Include if:**
- Sample size > 300 for RCTs
- Sample size > 1000 for registries
- Hard clinical endpoints (death, MI, stroke)
- Pre-registered on clinicaltrials.gov
- Industry-sponsored but independently monitored

**Exclude if:**
- Case series (N < 10)
- Single-center studies (unless exceptionally novel)
- Pure imaging/diagnostic studies (unless breakthrough)
- Editorials/commentaries (we're writing those, not reading them)
- Retracted or major concerns raised

## PubMed MCP Integration

**Key tools to use:**

1. `PubMed:search_articles(query, date_from, date_to, sort="pub_date", max_results=50)`
   - Run searches with strategies above
   - Retrieve recent trials

2. `PubMed:get_article_metadata(pmids=["12345678", ...])`
   - Get abstracts, titles, authors, journals
   - Feed into scoring algorithm

3. `PubMed:convert_article_ids(ids=["12345678"], id_type="pmid")`
   - Check if PMCID exists (full text available)
   - If PMCID present, can retrieve full text

4. `PubMed:get_full_text_article(pmc_ids=["PMC1234567"])`
   - Retrieve complete article when available
   - Enables deeper analysis for editorial

5. `PubMed:find_related_articles(pmids=["12345678"], link_type="pubmed_pubmed")`
   - Discover prior trials in same domain
   - Build context for editorial

## Deliverable Format

When presenting trial candidates to user:

```
**Top 5 Editorial Candidates (Past 30 Days)**

1. **[Trial Name/First Author]** - NEJM, Oct 2024 | Score: 16/18
   - Design: Large RCT (N=5000) | Endpoints: Hard clinical
   - Finding: SGLT2i reduced HF hospitalization by 35% in CKD patients
   - Why it matters: Expands SGLT2i to non-diabetic CKD population
   - Full text: Available (PMCID: PMC12345678)

2. **[Trial Name/First Author]** - JACC-CI, Oct 2024 | Score: 14/18
   - Design: Large RCT (N=2000) | Endpoints: Hard clinical
   - Finding: Drug-coated balloon non-inferior to DES for small vessels
   - Why it matters: Potential paradigm shift in small vessel PCI
   - Full text: Abstract only

[Continue for remaining 3...]

Which trial would you like me to write an editorial on? Or would you like to see alternatives?
```
