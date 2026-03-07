---
name: investor-discovery
description: >-
  Discovers project-relevant investors using OpenVC database with smart
  filtering, scoring, and ranking. Finds VCs, angels, and funds matching your
  industry, stage, geography, and check size requirements.
version: 1.0.0
dependencies: []
compatibility: 'agent-zero, claude-code, cursor'
---

# Investor Discovery Skill

**Find the right investors for your project in minutes, not weeks.**

This skill uses the OpenVC database (20,000+ verified investors) with intelligent filtering and scoring to match your project with relevant venture capital firms, angel investors, and funds.

---

## 🎯 When to Use This Skill

- "Find investors for my [industry] startup"
- "Who invests in [stage] companies in [geography]?"
- "I need seed investors for an AI/automotive project"
- "Find VCs that write $500K-$2M checks"
- "Show me investors who focus on [vertical]"

---

## 🚀 Quick Start

### **Step 1: Download OpenVC Database**

```bash
# Run the download script
python ~/.gemini/antigravity-vault/skills/investor-discovery/scripts/download_openvc.py
```

This will:
1. Guide you to create a free OpenVC account
2. Download the investor CSV database
3. Save it to `resources/openvc_investors.csv`

### **Step 2: Search for Investors**

```bash
# Run the search script
python ~/.gemini/antigravity-vault/skills/investor-discovery/scripts/search_investors.py \
  --project "AI Quality Layer for Automotive Engineering" \
  --industry "automotive,AI,compliance" \
  --stage "Seed" \
  --geography "Europe,USA" \
  --check-size "500K-2M" \
  --max-results 50
```

### **Step 3: Review Results**

Results are saved to:
- `output/investors_[timestamp].json` - Structured data
- `output/investors_[timestamp].csv` - Spreadsheet format
- `output/investors_[timestamp]_report.md` - Human-readable report

---

## 📋 Input Parameters

| Parameter | Description | Example | Required |
|-----------|-------------|---------|----------|
| `project` | Brief project description | "AI Quality Layer for Automotive" | Yes |
| `industry` | Comma-separated keywords | "automotive,AI,SaaS,compliance" | Yes |
| `stage` | Funding stage | "Seed", "Series A", "Pre-Seed" | Yes |
| `geography` | Target regions | "Europe,USA,Asia" | No |
| `check-size` | Investment range | "500K-2M", "1M-5M" | No |
| `max-results` | Maximum matches | 50 (default) | No |

---

## 📊 Output Format

### **JSON Output:**
```json
{
  "search_metadata": {
    "timestamp": "2026-01-28T13:27:47Z",
    "project": "AI Quality Layer for Automotive",
    "filters": {
      "industry": ["automotive", "AI", "compliance"],
      "stage": "Seed",
      "geography": ["Europe", "USA"],
      "check_size": "500K-2M"
    },
    "total_found": 127,
    "returned": 50
  },
  "investors": [
    {
      "name": "Automotive Ventures",
      "type": "Venture Capital",
      "hq": "Detroit, USA",
      "geography": "USA, Europe",
      "verticals": ["automotive", "mobility", "AI"],
      "stages": ["Seed", "Series A"],
      "check_size": "500K-3M",
      "contact_method": "email",
      "contact_info": "pitch@automotiveventures.com",
      "verified": true,
      "relevance_score": 0.95,
      "match_reasons": [
        "Exact match: automotive",
        "Exact match: AI",
        "Stage match: Seed",
        "Geography match: USA",
        "Check size match: 500K-3M"
      ]
    }
  ]
}
```

### **CSV Output:**
Spreadsheet with columns: Name, Type, HQ, Verticals, Stages, Check Size, Contact, Relevance Score

### **Markdown Report:**
Human-readable report with top matches, contact info, and next steps.

---

## 🔧 How It Works

### **1. Data Loading**
Loads the OpenVC investor database (CSV format) with 20,000+ verified investors.

### **2. Keyword Matching**
Matches your industry keywords against investor verticals using:
- Exact matching
- Partial matching (e.g., "fintech" matches "financial technology")
- Synonym expansion (e.g., "AI" matches "artificial intelligence", "machine learning")

### **3. Stage Filtering**
Filters investors by funding stage:
- Pre-Seed → Seed → Series A → Series B → Growth

### **4. Geography Filtering**
Matches investor HQ and target geographies:
- Country-level matching
- Region-level matching (e.g., "Europe" matches "Germany", "France")

### **5. Check Size Filtering**
Filters by typical investment amount:
- Parses ranges like "$500K-$2M"
- Matches against investor check sizes

### **6. Scoring & Ranking**
Calculates relevance score (0-1) based on:
- **Industry match (40%)**: Exact > Partial > Synonym
- **Stage match (25%)**: Exact match required
- **Geography match (20%)**: Investor HQ or target region
- **Check size match (15%)**: Investment range overlap

### **7. Output Generation**
Exports top matches in multiple formats for easy review and outreach.

---

## 📁 File Structure

```
investor-discovery/
├── SKILL.md                          # This file
├── README.md                         # Quick start guide
├── scripts/
│   ├── download_openvc.py           # Download OpenVC database
│   ├── search_investors.py          # Main search script
│   └── scoring.py                   # Scoring algorithm
├── resources/
│   ├── openvc_investors.csv         # OpenVC database (you download)
│   ├── synonyms.json                # Industry keyword synonyms
│   └── geography_mapping.json       # Country/region mappings
└── output/
    └── (generated search results)
```

---

## 🎓 Best Practices

### **1. Use Specific Keywords**
❌ Bad: "tech startup"  
✅ Good: "automotive,AI,compliance,SaaS,B2B"

### **2. Be Realistic About Stage**
Match your actual stage, not aspirational:
- Pre-Seed: Idea/prototype
- Seed: Early revenue/traction
- Series A: Product-market fit

### **3. Target Geography Strategically**
Consider:
- Where your company is incorporated
- Where your customers are
- Investor travel preferences

### **4. Set Appropriate Check Size**
Research typical ranges:
- Pre-Seed: $50K-$500K
- Seed: $500K-$2M
- Series A: $2M-$10M

### **5. Review Top 20 First**
Focus on highest-scoring matches (0.8+) before expanding.

---

## 🔄 Updating the Database

OpenVC is community-driven and frequently updated. Refresh your database:

```bash
# Re-download latest data
python scripts/download_openvc.py --force-update
```

Recommended: Update monthly or before major fundraising campaigns.

---

## 🚀 Future Enhancements (Phase 2)

This MVP can be extended with:
- [ ] Google Custom Search API enrichment (websites, LinkedIn)
- [ ] Apify integration for deep dives (PitchBook data)
- [ ] CUFinder for recent funding rounds
- [ ] AI-powered project description analysis
- [ ] Automated email outreach templates
- [ ] Warm introduction finder

---

## 📊 Example Searches

### **Example 1: Automotive AI Startup**
```bash
python scripts/search_investors.py \
  --project "AI-powered quality assurance for automotive engineering" \
  --industry "automotive,AI,enterprise software,compliance" \
  --stage "Seed" \
  --geography "Europe,USA" \
  --check-size "500K-2M" \
  --max-results 50
```

### **Example 2: Fintech Seed**
```bash
python scripts/search_investors.py \
  --project "Mobile banking for Gen Z" \
  --industry "fintech,mobile,consumer,banking" \
  --stage "Seed" \
  --geography "USA" \
  --check-size "1M-3M" \
  --max-results 30
```

### **Example 3: Climate Tech Series A**
```bash
python scripts/search_investors.py \
  --project "Carbon capture technology" \
  --industry "climate tech,sustainability,deep tech" \
  --stage "Series A" \
  --geography "USA,Europe" \
  --check-size "5M-15M" \
  --max-results 40
```

---

## ⚠️ Limitations

1. **Data Source**: Relies on OpenVC database (community-sourced)
2. **Manual Download**: CSV must be manually exported from OpenVC
3. **Static Data**: No real-time updates (refresh manually)
4. **Basic Scoring**: Keyword-based (no AI/ML in MVP)
5. **No Enrichment**: Contact info limited to OpenVC data

**Phase 2 will address these with API integrations and AI-powered features.**

---

## 🆘 Troubleshooting

### **"CSV file not found"**
Run `python scripts/download_openvc.py` first.

### **"No matches found"**
- Broaden your industry keywords
- Remove geography filter
- Expand check size range
- Try different stage

### **"Too many results"**
- Add more specific industry keywords
- Narrow geography
- Tighten check size range
- Reduce max-results

---

## 📚 Related Resources

- [OpenVC Database](https://openvc.app/investors)
- [Investor Discovery Strategy](../../enora/INVESTOR_DISCOVERY_STRATEGY.md)
- [Quick Reference Guide](../../enora/INVESTOR_DISCOVERY_QUICK_REF.md)

---

**Built with ❤️ using the Antigravity Skill System**
