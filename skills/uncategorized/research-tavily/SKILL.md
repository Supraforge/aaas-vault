---
name: research-tavily
description: >-
  Perform deep, fact-based web research using the Tavily AI API. Superior to
  standard Google Search for answering complex questions.
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---

# Research (Tavily)

**PURPOSE:**
Use this skill to research complex topics, find recent facts, or aggregate data from multiple sources without the noise of SEO-spam sites. Tavily is optimized for LLM consumption.

**WHEN TO USE:**
- "Find the latest news on X."
- "Research the background of Y."
- "What are the competitors of Z?"
- "Deep dive into topic A."

**DO NOT USE FOR:**
- Simple navigation (visiting a known URL).
- Checking localhost.

---

## 1. Usage

### A. Quick Fact Check (Basic)
Use this for simple queries like "Who is the CEO of Google?" or "Latest stock price of Apple".
```bash
python3 skills/research-tavily/scripts/tavily_search.py --query "Your Question Here" --depth "basic"
```

### B. Deep Dive (Advanced)
Use this for broad topics requiring comprehensive analysis. This mode takes longer but scrapes more sources.
```bash
python3 skills/research-tavily/scripts/tavily_search.py --query "Comprehensive analysis of AI Agent architectures in 2025" --depth "advanced"
```

---

## 2. API Key Requirement
This skill requires the `TAVILY_API_KEY` to be set in the `.env` file of the workspace. If it is missing, the script will fail gracefully and ask the user to provide it.

**Get a key:** [https://tavily.com](https://tavily.com)
