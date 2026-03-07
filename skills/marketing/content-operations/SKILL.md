---
name: content-operations
description: Manage content templates, calendar, and automated reports. Includes template library with CRUD operations, content calendar management, visual calendar generation, and weekly report automation. Use for content planning, scheduling, template management, or generating progress reports.
license: MIT
metadata:
  version: 1.0.0
  author: [PROJECT_NAME] AI
  category: marketing
  domain: content-operations
  updated: 2026-02-12
  python-tools: template_manager.py, calendar_manager.py, calendar_visualizer.py, weekly_report_generator.py
  tech-stack: Python, JSON, Jinja2
  integrations: brand-qa, content-factory, sales-enablement
---

# Content Operations

Central hub for content templates, calendar management, and automated reporting. Foundation skill used by content-generating skills.

## Keywords

content calendar, template library, content planning, content scheduling, marketing calendar, content templates, weekly reports, content management, editorial calendar, content pipeline, content tracking

## Quick Start

### List Available Templates
```bash
python scripts/template_manager.py list
python scripts/template_manager.py list --category email
```

### Add Calendar Entry
```bash
python scripts/calendar_manager.py add \
  --title "LinkedIn Thought Leadership" \
  --type social \
  --platform linkedin \
  --date 2026-02-15
```

### Generate Weekly Report
```bash
python scripts/weekly_report_generator.py --week-start 2026-02-10
```

### Visualize Calendar
```bash
python scripts/calendar_visualizer.py --month 2 --year 2026 --format html
```

## Core Workflows

### 1. Template-Based Content Creation

**Goal**: Use templates to ensure consistent content structure

**Process**:
1. Find appropriate template
2. Instantiate with variables
3. Edit generated content
4. Validate with brand-qa

```bash
# Find email templates
python scripts/template_manager.py list --category email

# Get template details
python scripts/template_manager.py get nurture_sequence

# Instantiate template
python scripts/template_manager.py instantiate nurture_sequence \
  --vars '{"prospect_name": "John", "company": "Acme"}' \
  --output drafts/email_sequence.md
```

### 2. Content Calendar Management

**Goal**: Plan and track content publication

**Process**:
1. Add content ideas to calendar
2. Update status as work progresses
3. Review upcoming deadlines
4. Generate reports on activity

```bash
# View this week's calendar
python scripts/calendar_manager.py get --start today --end +7d

# Update entry status
python scripts/calendar_manager.py update cal_001 --status drafted

# View by platform
python scripts/calendar_manager.py get --platform linkedin
```

### 3. Weekly Content Reporting

**Goal**: Track content performance and pipeline

**Process**:
1. Run weekly report generator
2. Review published content
3. Check pipeline status
4. Plan next week

```bash
python scripts/weekly_report_generator.py --week-start 2026-02-10 --brand [PROJECT_NAME]
```

## Key Scripts

### template_manager.py

Manage content templates with CRUD operations.

**Usage**:
```bash
# List all templates
python scripts/template_manager.py list

# List by category
python scripts/template_manager.py list --category email

# Get template details
python scripts/template_manager.py get <template_id>

# Instantiate template with variables
python scripts/template_manager.py instantiate <template_id> \
  --vars '{"key": "value"}' \
  --output output.md
```

**Template Categories**:
- `email`: Nurture sequences, follow-ups, investor updates
- `social`: LinkedIn posts, carousel briefs, ad copy
- `documents`: Press releases, FAQs, meeting briefs
- `reports`: Weekly reports, performance summaries

### calendar_manager.py

CRUD operations for content calendar.

**Usage**:
```bash
# Add entry
python scripts/calendar_manager.py add \
  --title "Title" \
  --type social \
  --platform linkedin \
  --date 2026-02-15 \
  --pillar thought_leadership

# Get entries (with filters)
python scripts/calendar_manager.py get \
  --start 2026-02-01 \
  --end 2026-02-28 \
  --platform linkedin \
  --status planned

# Update entry
python scripts/calendar_manager.py update <id> --status published

# Delete entry
python scripts/calendar_manager.py delete <id>
```

**Entry Statuses**:
- `idea`: Initial concept
- `planned`: Scheduled but not started
- `drafted`: Content written
- `scheduled`: Ready for publication
- `published`: Live
- `archived`: Completed/removed

### calendar_visualizer.py

Generate visual calendar views.

**Usage**:
```bash
# HTML calendar (opens in browser)
python scripts/calendar_visualizer.py --month 2 --year 2026 --format html

# Markdown calendar
python scripts/calendar_visualizer.py --month 2 --year 2026 --format markdown

# JSON export
python scripts/calendar_visualizer.py --month 2 --year 2026 --format json
```

### weekly_report_generator.py

Automated weekly content performance reports.

**Usage**:
```bash
python scripts/weekly_report_generator.py \
  --week-start 2026-02-10 \
  --brand [PROJECT_NAME] \
  --output reports/week_of_2026-02-10.md
```

**Report Includes**:
- Content published this week
- Content pipeline status
- Upcoming content schedule
- Action items for next week
- Key metrics summary

## Template Schema

Templates use YAML frontmatter + Jinja2 content:

```markdown
---
id: template_id
name: Human Readable Name
category: email|social|documents|reports
tags: [tag1, tag2]
variables:
  - name: variable_name
    required: true
    default: "optional default"
    description: "What this variable is for"
---

# Template Title

Hello {{ prospect_name }},

Content with {{ variables }} that get replaced.

{% if optional_section %}
Optional content block
{% endif %}
```

## Calendar Entry Schema

```json
{
  "id": "cal_001",
  "title": "Entry Title",
  "content_type": "social|email|blog|video",
  "platform": "linkedin|twitter|email|website",
  "pillar": "educational|thought_leadership|engagement|promotional",
  "scheduled_date": "2026-02-15",
  "scheduled_time": "09:00",
  "status": "planned|drafted|scheduled|published",
  "content_path": "path/to/content.md",
  "assets": ["path/to/asset.png"],
  "tags": ["tag1", "tag2"],
  "created_at": "2026-02-10T14:30:00Z",
  "updated_at": "2026-02-12T09:15:00Z"
}
```

## Content Pillars

Follow the 40/25/25/10 ratio:

| Pillar | Ratio | Description |
|--------|-------|-------------|
| Educational | 40% | How-to guides, best practices, insights |
| Thought Leadership | 25% | Opinion pieces, trend analysis, predictions |
| Engagement | 25% | Questions, polls, community discussions |
| Promotional | 10% | Product updates, case studies, announcements |

## Integration Points

This skill provides foundation for:
- **content-factory**: Uses templates for content generation
- **sales-enablement**: Uses email templates
- **pr-communications**: Uses document templates
- **visual-content-generator**: Tracks visual asset deadlines

## Best Practices

### Template Management
- Use descriptive template IDs
- Include all required variables in frontmatter
- Provide defaults where sensible
- Keep templates focused (one purpose each)

### Calendar Management
- Add entries as soon as ideas emerge
- Update status regularly
- Use consistent naming conventions
- Tag entries for easy filtering

### Weekly Reports
- Generate reports on the same day each week
- Review metrics before planning new content
- Track trends over time
- Share reports with stakeholders

## File Locations

```
skills/content-operations/
├── scripts/
│   ├── template_manager.py
│   ├── calendar_manager.py
│   ├── calendar_visualizer.py
│   └── weekly_report_generator.py
├── resources/
│   └── templates/
│       ├── email/
│       ├── social/
│       ├── documents/
│       └── reports/
├── data/
│   ├── calendar.json
│   └── template_index.json
└── references/
    └── template_schema.md
```
