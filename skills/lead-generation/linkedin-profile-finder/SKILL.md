---
name: linkedin-profile-finder
description: Autonomous LinkedIn profile URL discovery by ICP criteria. Generates queries from persona/industry/location definitions, searches via Tavily or Google CSE, tags each result with ICP metadata for activation. Use when prospecting, building lead lists, or targeting ICPs.
version: 3.0.0
metadata:
  filePattern: "**/linkedin*find*,**/linkedin*search*,**/linkedin*scrape*,**/icp*linkedin*,**/prospect*linkedin*,**/lead*list*"
  bashPattern: "linkedin.profile.finder|linkedin_tavily|linkedin_google|icp.*linkedin"
tags: [linkedin, tavily, google-cse, lead-generation, icp, prospecting, autonomous]
---

# LinkedIn Profile Finder

Autonomous agent skill for bulk LinkedIn profile URL discovery by ICP criteria. Finds profile links only — enrichment happens separately.

## How It Works

1. **Define ICPs** → personas × industries × locations
2. **Generate queries** → structured search matrix with metadata tags
3. **Search** → Tavily or Google CSE finds `site:linkedin.com/in` profiles
4. **Tag** → each result carries persona, industry, location, region
5. **Output** → JSONL file filterable for activation

## Output Format (JSONL)

Each line is a tagged profile:
```json
{
  "url": "https://www.linkedin.com/in/jane-doe",
  "name": "Jane Doe",
  "title": "Jane Doe - CISO - FinCorp | LinkedIn",
  "snippet": "Chief Information Security Officer at FinCorp...",
  "persona": "delia_ciso",
  "title_searched": "CISO",
  "industry": "fintech",
  "industry_term": "fintech",
  "location": "Berlin",
  "region": "dach",
  "source_query": "CISO fintech Berlin"
}
```

Filter for activation:
```bash
# All CISOs in fintech DACH
jq 'select(.persona=="delia_ciso" and .industry=="fintech" and .region=="dach")' profiles.jsonl

# All Berlin profiles regardless of persona
jq 'select(.location=="Berlin")' profiles.jsonl

# Count by persona
jq -r '.persona' profiles.jsonl | sort | uniq -c | sort -rn
```

## Search Engines

### Google CSE (recommended for recurring use)
- **Cost**: $5/1K queries or free at 100 queries/day
- **Yield**: ~80 LinkedIn profiles per query (10 pages × 10 results)
- **50K profiles**: ~625 queries = **$3.13** or free over 7 days
- **Setup**: Requires one-time Google CSE creation + TOS acceptance
- **Env**: `GOOGLE_CSE_API_KEY` + `GOOGLE_CSE_ID`
- **Script**: `scripts/linkedin_google_cse.py`

### Tavily (recommended for quick runs)
- **Cost**: $8/1K queries, 1K free/month
- **Yield**: ~13 unique LinkedIn profiles per query
- **50K profiles**: ~3,846 queries = **$30.77**
- **Setup**: Just needs API key (already configured)
- **Env**: `TAVILY_API_KEY`
- **Script**: `scripts/linkedin_tavily.py`

## Autonomous Agent Usage

The skill includes an ICP definition generator and batch runner. To run autonomously:

### Step 1: Define ICPs

Create or edit `context/icp-targets.json`:
```json
{
  "personas": {
    "alex_cto": {
      "titles": ["CTO", "Chief Technology Officer", "VP Engineering"],
      "weight": 3
    },
    "delia_ciso": {
      "titles": ["CISO", "VP Security", "Head of Information Security"],
      "weight": 3
    }
  },
  "industries": {
    "fintech": ["fintech", "neobank", "payments"],
    "saas": ["SaaS", "B2B SaaS", "cloud software"]
  },
  "locations": {
    "dach": ["Berlin", "Munich", "Frankfurt", "Zurich", "Vienna"],
    "uk": ["London", "Manchester", "Edinburgh"]
  },
  "target_count": 50000
}
```

### Step 2: Generate Query Matrix

```bash
python3 scripts/generate_icp_queries.py \
  --config context/icp-targets.json \
  --region dach \
  --output context/queries-dach.json
```

### Step 3: Run Search

```bash
# Tavily
python3 scripts/linkedin_tavily.py -b context/queries-dach.json -o context/profiles-dach.jsonl

# Google CSE
python3 scripts/linkedin_google_cse.py -b context/queries-dach.json -o context/profiles-dach.jsonl
```

### Step 4: Analyze Results

```bash
python3 scripts/analyze_results.py context/profiles-dach.jsonl
```

## SQUR ICP Reference

| Persona | Role | Priority | Search Titles |
|---------|------|----------|--------------|
| **Alex** | CTO / VP Eng | Primary budget owner | CTO, Chief Technology Officer, VP Engineering, Head of Engineering |
| **Delia** | Strategic CISO | Key decision maker | CISO, VP Security, Director of Security, Chief Security Officer |
| **Beatrice** | Budget CISO | Coverage optimizer | Head of Security, Security Manager, IT Security Manager |
| **Felix** | Head of IT (SMB) | Owns security by default | Head of IT, IT Director, IT Manager, Director of IT |
| **Greta** | AppSec Engineer | Bottom-up champion | AppSec Engineer, Security Engineer, Penetration Tester |
| **Hanna** | Founder/CEO | First pentest buyer | Founder, CEO, Co-Founder, Managing Director |
| **Carlos** | Engineering Lead | Influencer | Engineering Lead, Principal Engineer, Engineering Manager |
| **Evan** | Product Manager | Influencer | Head of Product, VP Product, Product Lead |

## Industries (9 segments)

Fintech, SaaS, Cybersecurity, LegalTech, HealthTech, Insurance, E-commerce, GovTech, RegTech

## Geographies

| Region | Cities |
|--------|--------|
| **DACH** | Berlin, Munich, Frankfurt, Hamburg, Zurich, Vienna, Stuttgart, Cologne, Dusseldorf |
| **UK/Ireland** | London, Manchester, Edinburgh, Dublin, Bristol, Cambridge |
| **Nordics** | Stockholm, Copenhagen, Oslo, Helsinki |
| **Benelux** | Amsterdam, Rotterdam, Brussels, Luxembourg |
| **Southern EU** | Barcelona, Madrid, Milan, Lisbon |
| **France** | Paris, Lyon |
| **Global** | Singapore, Sydney, Toronto, Tel Aviv, San Francisco, New York, Austin |
