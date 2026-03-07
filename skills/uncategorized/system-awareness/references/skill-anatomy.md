# Skill Anatomy - What Makes a Good Skill

This document defines the structure and qualities of well-designed skills in the integrated cowriting system.

## Skill Complexity Tiers

### Tier 1: Documentation-Only Skills
**Structure:**
```
skill-name/
├── SKILL.md              # Main documentation
└── references/           # Optional reference files
    └── guide.md
```

**Characteristics:**
- Prompt engineering only
- No code execution
- Claude follows instructions from SKILL.md
- Examples: `authentic-voice`, `content-reflection`

### Tier 2: Reference-Enhanced Skills
**Structure:**
```
skill-name/
├── SKILL.md
├── references/
│   ├── examples.md       # Example outputs
│   ├── framework.md      # Structured approach
│   └── templates.md      # Reusable templates
└── assets/               # Optional static assets
    └── template.md
```

**Characteristics:**
- Rich documentation with examples
- Structured frameworks and templates
- Still prompt-based, no scripts
- Examples: `x-post-creator-skill`, `cardiology-tweet-writer`

### Tier 3: Script-Enhanced Skills
**Structure:**
```
skill-name/
├── SKILL.md
├── scripts/
│   ├── main_script.py    # Primary functionality
│   └── helper.py         # Supporting utilities
├── references/
│   └── api-docs.md
└── data/                 # Optional data files
    └── config.json
```

**Characteristics:**
- Python scripts for computation
- May call external APIs
- Processing logic beyond prompts
- Examples: `viral-content-predictor`, `cardiology-trial-editorial`

### Tier 4: Full Pipeline Skills
**Structure:**
```
skill-name/
├── SKILL.md
├── scripts/
│   ├── pipeline.py
│   ├── fetcher.py
│   ├── processor.py
│   └── output.py
├── references/
├── assets/
├── data/
│   ├── config.json
│   └── templates/
└── output/               # Generated outputs
```

**Characteristics:**
- Multi-stage processing
- Multiple scripts working together
- Data persistence
- Examples: `knowledge-pipeline`, `cardiology-visual-system`

---

## Essential SKILL.md Sections

Every skill should have these sections:

### 1. Header & Purpose (Required)
```markdown
# Skill Name

> One-line description

## Purpose
What problem does this solve? Who benefits?
```

### 2. Quick Start (Required)
```markdown
## Quick Start
Show the simplest way to use this skill in 3 lines or less.
```

### 3. Inputs & Outputs (Required)
```markdown
## Inputs
- What data/information does this need?

## Outputs
- What does this produce?
```

### 4. Use Cases (Recommended)
```markdown
## Use Cases
1. Primary scenario
2. Secondary scenario
```

### 5. Examples (Recommended)
```markdown
## Examples
Concrete input → output examples
```

### 6. Best Practices (Optional)
```markdown
## Best Practices
Tips for getting the best results
```

---

## Quality Checklist

Before deploying a skill, verify:

### Clarity
- [ ] Purpose is clear in first 2 sentences
- [ ] Quick start works as documented
- [ ] Examples are realistic and helpful

### Completeness
- [ ] All inputs are documented
- [ ] All outputs are documented
- [ ] Dependencies are listed

### Usability
- [ ] Can be used without reading entire document
- [ ] Error cases are handled or noted
- [ ] Edge cases are addressed

### Maintainability
- [ ] No hardcoded values that will become stale
- [ ] References are version-appropriate
- [ ] Scripts have error handling

---

## Naming Conventions

### Skill Names
- Use kebab-case: `cardiology-tweet-writer`
- Be specific: `youtube-script-master` not `script-writer`
- Include domain: `cardiology-` prefix for cardiology skills

### File Names
- SKILL.md (always uppercase)
- References: lowercase with hyphens
- Scripts: lowercase with underscores

### Categories
Standard categories:
- `content-creation` - Creating content
- `research` - Finding information
- `analysis` - Processing data
- `visual` - Generating graphics
- `quality` - Review and refinement
- `utilities` - Supporting tools

---

## Anti-Patterns to Avoid

### 1. The Kitchen Sink
❌ One skill that does everything
✅ Focused skills that do one thing well

### 2. The Orphan
❌ Skill with no examples or use cases
✅ Clear scenarios showing when to use

### 3. The Black Box
❌ Vague inputs/outputs without types
✅ Specific, documented data contracts

### 4. The Stale Reference
❌ Outdated URLs, versions, or examples
✅ Timeless or regularly updated content

### 5. The Dependency Hell
❌ Skill that requires 10 other skills
✅ Minimal, well-documented dependencies

---

## Evolution Patterns

### Growth Path
```
Documentation-Only → Reference-Enhanced → Script-Enhanced
```

### Split Pattern
When a skill gets too complex, split it:
```
mega-skill → core-skill + helper-skill + advanced-skill
```

### Merge Pattern
When skills overlap, merge them:
```
skill-a + skill-b → unified-skill
```

---

*Reference for creating and evaluating skills in the integrated cowriting system.*
