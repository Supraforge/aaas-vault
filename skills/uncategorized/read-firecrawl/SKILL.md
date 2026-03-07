---
name: reading-firecrawl
description: "Turns any website, documentation, or wiki into clean LLM-ready Markdown using the Firecrawl API. Best for ingestion."
version: 1.0.0
dependencies: ["python3", "requests"]
inputs:
  - name: url
    description: The URL to scrape or crawl.
  - name: mode
    description: "scrape" (single page) or "crawl" (full site).
outputs:
  - type: stdout
    description: Clean Markdown content.
---

# Reading (Firecrawl)

**PURPOSE:**
Use this skill to "read" the internet. While Tavily finds links, Firecrawl **ingests** them. It is optimized to handle complex JavaScript, dynamic content, and documentation sites, returning clean Markdown.

**WHEN TO USE:**
- "Read the documentation for library X."
- "Ingest this blog post."
- "Scrape the pricing page of Y."

---

## 2. Usage

### A. Scrape (Single Page)
Use this to get the content of one specific URL.
```bash
python3 skills/read-firecrawl/scripts/firecrawl_read.py --url "https://docs.example.com/intro" --mode "scrape"
```

### B. Crawl (Full Site)
Use this to map and ingest a sub-domain (e.g., all docs). **Use with caution** to avoid context overflow.
```bash
python3 skills/read-firecrawl/scripts/firecrawl_read.py --url "https://docs.example.com" --mode "crawl" --max_depth 2
```

---

## 3. API Key Requirement
This skill requires the `FIRECRAWL_API_KEY` to be set in the `.env` file.

**Get a key:** [https://firecrawl.dev](https://firecrawl.dev)
