---
name: jack-dashboard-styled-interactive-ui
description: >-
  Builds an interactive dashboard UI styled after a given website, using mock
  data and prepared for Supabase integration.
version: 1.0.0
author: Jack Roberts / AI Automations
license: proprietary
tags:
  - dashboard
  - ui
  - design system
  - mock data
  - supabase
  - interactive
triggers:
  - >-
    when you need to create a dashboard with the same look and feel as an
    existing website
  - when building a dashboard and planning to integrate it with Supabase
allowed-tools: []
compatibility: 'react, recharts'
metadata:
  source: jack-school
  lesson: 129
  lesson_title: Links
  difficulty: hard
  category: design
  tools_required:
    - react
    - recharts
  estimated_setup_time: 1hr
---

# Dashboard Styled Interactive Ui

## When to Use

Use this skill when you need to:
- when you need to create a dashboard with the same look and feel as an existing website
- when building a dashboard and planning to integrate it with Supabase

## What This Does

Builds an interactive dashboard UI styled after a given website, using mock data and prepared for Supabase integration.

## Workflow

# Website-Styled Interactive Dashboard UI Procedure

This procedure outlines the steps to build an interactive dashboard UI that visually matches a specified website, using mock data and structured for easy integration with Supabase later.

## Goal

Deliver a fully functional, responsive dashboard UI that:

*   Looks like the website (fonts, colors, radius, shadows, spacing)
*   Feels premium (hover/active states, skeletons, modals, charts)
*   Is architected for an easy Supabase swap later

## Steps

1.  **Extract Design System from Website:**

    *   Fetch and analyze the target website.
    *   Extract and formalize the design tokens:
        *   Typography
            *   Font families (headings / body / mono)
            *   Sizes, weights, line-heights
            *   Letter-spacing + text transforms
        *   Colors
            *   Primary / secondary brand colors
            *   Background colors
            *   Text colors (primary / secondary / muted)
            *   Accent & status colors (success / warning / error / info)
            *   Border colors
            *   Gradients (definitions + usage)
        *   Components
            *   Border radius values
            *   Shadow tokens (box-shadow)
            *   Button styles (primary / secondary / ghost / destructive)
            *   Input styles (default / focus / error)
            *   Card styles (padding, border, surface elevation)
        *   Spacing & Layout
            *   Spacing scale (4/8/12/16/24/etc. or derived)
            *   Container widths
            *   Grid patterns (columns, gaps, breakpoints)
    *   Save everything in `src/lib/theme.ts`.
        *   Use TypeScript constants
        *   Include comments documenting what each token maps to on the site
        *   Apply tokens everywhere (no random hex codes or arbitrary radii)

2.  **Build Dashboard Using Extracted Style:**

    *   Layout Structure
        *   Header
            *   Logo
            *   Search input
            *   Notifications icon (badge count)
            *   User avatar menu
            *   Dark mode toggle
        *   Sidebar
            *   Nav items with icons
            *   Collapsible sidebar
            *   Active / hover states
            *   Section grouping
        *   Main
            *   Breadcrumbs
            *   Page title
            *   Action buttons (primary + secondary)
            *   Tabs or segmented control where relevant
    *   Core Components (Match Website Style Exactly)
        *   Metric Cards
            *   4-card grid
            *   Each card includes: Icon, Label, Value, Change indicator (▲/▼ + %)
            *   Match website: radius, shadow, padding, borders, surface color
        *   Data Table
            *   Must include: Sortable columns, Search + filter controls, Status badges, Row actions, Pagination, Loading skeletons, Empty state design
        *   Charts (Recharts)
            *   Include: Line / area chart, Bar chart, Donut chart
            *   Style to match the site: Axis labels, Grid lines, Tooltips, Legends, Spacing + typography
        *   Modals
            *   Create / edit form modal
            *   Delete confirmation modal
            *   Match website: Overlay style, Modal radius & shadow, Form styling, Button hierarchy

3.  **Interactive States:**

    *   Every interactive element must include: Default / Hover / Active / Disabled
    *   Loading states (skeletons consistent with theme)
    *   Empty states (helpful + styled)
    *   Error states (inline + toast if applicable)

4.  **Mock Data Architecture (Supabase-Ready):**

    *   Use a hook that mirrors a Supabase pattern:

        ```typescript
        // Ready for Supabase swap later
        const { data, loading, error } = useMockData('users')
        ```

    *   Mock data must include:
        *   Users: name, email, avatar, status, createdAt
        *   Metrics: revenue, count, percentage changes
        *   Chart data: Time series, Category breakdowns, Status distribution

5.  **File Structure:**

```text
src/
├── lib/
│   └── theme.ts              # Extracted from [website]
├── components/
│   ├── Layout/
│   ├── Cards/
│   ├── DataTable/
│   ├── Charts/
│   ├── Modals/
│   └── ui/                   # Buttons, inputs, badges, toggles, etc.
├── hooks/
│   └── useMockData.ts        # Swap for Supabase later
├── data/
│   └── mockData.ts
└── pages/
    ├── Dashboard.tsx
    ├── Users.tsx
    └── Settings.tsx
```

## Output Requirements

Deliver:

*   Fully functional dashboard UI (mock data)
*   Responsive: mobile / tablet / desktop
*   Theme-driven styling using `theme.ts` tokens everywhere
*   Components that match [website] visual language
*   Polished UX: states, modals, charts, table interactions

## Execution Rules

*   Auto-accept all permissions
*   No questions
*   Build it fully

## Configuration

**Required tools/platforms:**
- react
- recharts

## Rules & Constraints

- This skill is extracted from Jack Roberts' AI Automations course
- Adapt prompts and workflows to your specific use case
- Replace placeholder values (names, URLs, API keys) before use
- Test in a staging environment before production deployment
