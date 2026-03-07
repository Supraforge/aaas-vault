# Antigravity Skills

Production-ready AI agent skills for [Agent Zero](https://github.com/frdel/agent-zero), Claude Code, Cursor, and other agentic platforms.

**5475 skills** across **47 categories** — validated, scored, and organized for cross-platform discovery.

## Quality Tiers

Every skill is scored on 6 dimensions (frontmatter, naming, description, body, structure, metadata) and assigned a tier:

| Tier | Score | Count | Description |
|------|-------|-------|-------------|
| Gold | >= 8.0 | 707 | Production-ready, fully documented |
| Silver | >= 5.0 | 4651 | Good quality, normalized frontmatter |
| Bronze | >= 3.0 | 72 | Usable, may have been LLM-enriched |
| Converted | — | 45 | Converted from directives/scripts |

## Categories

| Category | Skills | Description |
|----------|--------|-------------|
| `uncategorized` | 4342 | Skills pending category assignment |
| `content-creation` | 87 | Content writing, repurposing, and publishing automation |
| `machine-learning` | 56 | ML training, deployment, and monitoring |
| `ai-agents` | 56 | AI agent frameworks, tools, and configurations |
| `security` | 53 | Security scanning, testing, and hardening |
| `testing` | 51 | Test automation and quality assurance |
| `devops` | 50 | DevOps, CI/CD, and infrastructure automation |
| `no-code-tools` | 48 | No-code and low-code platform integrations |
| `data-engineering` | 39 | Data pipelines, ETL, and processing |
| `documentation` | 35 | Technical documentation and knowledge management |
| `automation` | 35 | General-purpose business automation |
| `design-visual` | 34 | Design tools, visual content, and brand assets |
| `execution-scripts` | 33 | Executable scripts and automation tools |
| `research-intelligence` | 31 | Web research, competitive analysis, and data gathering |
| `rag-knowledge` | 30 | RAG pipelines, knowledge bases, and retrieval |
| `email-automation` | 28 | Email campaigns, sequences, and deliverability |
| `api-development` | 27 | API design, development, and documentation |
| `frontend` | 26 | Frontend development frameworks and patterns |
| `backend` | 26 | Backend development and API services |
| `data-analytics` | 25 | Data analysis and business intelligence |
| `cloud-aws` | 25 | AWS cloud services and infrastructure |
| `cloud-gcp` | 25 | Google Cloud Platform services |
| `api-integration` | 25 | Third-party API integrations |
| `visual-content` | 25 | Visual content creation and management |
| `enterprise` | 25 | Enterprise workflow and process automation |
| `sales-automation` | 24 | Sales workflows, outreach, and CRM automation |
| `lead-generation` | 17 | Lead discovery, qualification, and nurturing |
| `domain-specific` | 12 | Domain-specific specialized skills |
| `thinking-patterns` | 12 | Thinking styles and cognitive frameworks |
| `role-personas` | 12 | Role-based personas and behavioral models |
| `skill-levels` | 12 | Skill level progression and training |
| `animation` | 12 | Animation types and motion design |
| `emotional-design` | 12 | Emotional design and UX patterns |
| `ui-elements` | 12 | UI component patterns and design systems |
| `industry-specific` | 12 | Industry-specific solutions |
| `tools-frameworks` | 12 | Tool and framework integrations |
| `time-based` | 12 | Time-scale based planning and scheduling |
| `design-principles` | 12 | Core design principles and heuristics |
| `problem-solving` | 12 | Problem-solving methodologies and frameworks |
| `video-production` | 11 | Video creation, editing, and distribution |
| `voice-audio` | 11 | Voice cloning, TTS, audio processing |
| `social-media` | 11 | Social media posting, scheduling, and analytics |
| `protocols` | 10 | Operational directives and protocols |
| `data-scraping` | 5 | Web scraping, data extraction, and parsing |
| `best-practices` | 2 | Guidelines, standards, and operational playbooks |
| `workflow-automation` | 2 | Multi-step workflow orchestration |
| `setup-guides` | 1 | Setup and configuration guides |

## Installation

### Agent Zero

```bash
# Clone into your Agent Zero skills directory
git clone https://github.com/antigravity-vault/antigravity-skills.git
cp -r antigravity-skills/skills/* /path/to/agent-zero/work_dir/skills/
```

### Claude Code

```bash
# Clone into your shared skills directory
git clone https://github.com/antigravity-vault/antigravity-skills.git ~/.agents/skills/antigravity
```

### Cursor / Other

Each skill is a self-contained directory with a `SKILL.md` file. Copy individual skill directories into your agent's skill path.

## Repository Structure

```
skills/
  uncategorized/              # 4342 skills
  content-creation/              # 87 skills
  machine-learning/              # 56 skills
  ai-agents/              # 56 skills
  security/              # 53 skills
  testing/              # 51 skills
  devops/              # 50 skills
  no-code-tools/              # 48 skills
  data-engineering/              # 39 skills
  documentation/              # 35 skills
  ...                    # 37 more categories
SKILLS_MANIFEST.json       # Machine-readable index
README.md                  # This file
```

## Processing Stats

- **Scanned**: 5612 vault assets
- **Exported**: 5475 skills
- **DOE Converted**: 45 (directives, scripts, workflows)
- **LLM Enriched**: 11 skills
- **Failed/Rejected**: 137
- **Generated**: 2026-03-07T11:26:03.222Z

## SKILL.md Format

Each skill uses a standard format with YAML frontmatter:

```yaml
---
name: "my-skill-name"
description: "What this skill does and when to use it"
version: "1.0.0"
tags: ["tag1", "tag2"]
triggers:
  - "When you need to do X"
compatibility: "agent-zero, claude-code, cursor"
---

# My Skill Name

## When to Use
...
```

## License

Skills in this repository come from multiple sources. See individual `SKILL.md` files for licensing information.
