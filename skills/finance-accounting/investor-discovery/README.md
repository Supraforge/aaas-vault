# Investor Discovery

**Discovers project-relevant investors using a smart local search method.**

This skill provides a high-efficiency way to find venture capital firms, angel investors, and funds that match your specific project criteria. It leverages the community-sourced OpenVC database (20,000+ investors) to give you a head start in fundraising.

## 🚀 Highlights

- **Low Cost**: $0 monthly cost (OpenVC free tier).
- **Comprehensive**: Access to 20,000+ verified investors.
- **Project-Specific**: Filter by industry, stage, geography, and check size.
- **Intelligent Scoring**: Ranks investors by relevance to your project.
- **Multi-Format Output**: JSON, CSV, and Markdown reports.

## 🛠️ Setup

1. **Initialize Skill**:
   Ensure you are in the project folder where you want to use the skill results.

2. **Download Database**:
   Run the helper script and follow the instructions:
   ```bash
   python ~/.gemini/antigravity-vault/skills/investor-discovery/scripts/download_openvc.py
   ```

3. **Install Dependencies**:
   Ensure you have `pandas` installed:
   ```bash
   pip install pandas
   ```

## 🔍 Usage

Perform a search using the following command structure:

```bash
python ~/.gemini/antigravity-vault/skills/investor-discovery/scripts/search_investors.py \
  --project "AI Quality Layer for Automotive" \
  --industry "automotive,AI,compliance" \
  --stage "Seed" \
  --geography "Europe,USA" \
  --check-size "500K-2M"
```

### Parameters:
- `--project`: Brief name/description.
- `--industry`: Comma-separated keywords.
- `--stage`: Current target stage (Seed, Series A, etc.).
- `--geography`: (Optional) Target regions (Europe, USA, etc.).
- `--check-size`: (Optional) Target check size (e.g. 500K-2M).
- `--max-results`: (Optional) Default is 50.

## 📁 Output

All searches generate files in the `output/` directory:
- `investors_[timestamp].json`: Full data for programmatic use.
- `investors_[timestamp].csv`: Best for Excel/Google Sheets.
- `investors_[timestamp]_report.md`: Best for readable review.

## 🎯 Scoring Algorithm

The skill ranks results based on:
1. **Industry (40%)**: Keyword and synonym matching.
2. **Stage (25%)**: Compliance with target funding round.
3. **Geography (20%)**: Match with HQ or regional focus.
4. **Check Size (15%)**: Overlap with target investment range.

---
*Built with ❤️ for Antigravity.*
