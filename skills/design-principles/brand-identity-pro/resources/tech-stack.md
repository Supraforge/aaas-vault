# AaaS Technical Implementation Guidelines

## Canonical Brand Reference
**Single source of truth:** https://aaas-platform.web.app/aaas-brand-reference.html
All design tokens, colors, typography, and component patterns are defined there. When in doubt, fetch that page.

## Core Stack

### Platform Website (agents-as-a-service.com)
* **Framework**: Next.js 14 (App Router) with static export
* **Styling**: Tailwind CSS with CSS custom properties
* **Fonts**: Inter (body/display) + JetBrains Mono (code/labels) via `next/font/google`
* **Hosting**: Firebase Hosting
* **Monorepo**: Turborepo — `apps/platform/` + `packages/ui/`

### Knowledge Index (aaas.blog)
* **Framework**: Next.js 14 (App Router) with Firebase App Hosting (server-rendered)
* **Data**: Firestore-backed entity system
* **Styling**: Tailwind CSS, same token system as platform

### Toolbox Templates (108 assets)
* **Structure**: Single-file HTML pages
* **Styling**: Tailwind CSS via CDN with inline config
* **Engine**: `template-base.js` (bridge) + `template-base.css` (tokens)
* **Hosting**: Firebase Hosting (`aaas-platform.web.app`)

## CSS Variable Pattern
All colors use the CSS custom property pattern for Tailwind opacity support:
```css
:root[data-theme="light"] {
  --bg: #ffffff;
  --bg-secondary: #f7f7f6;
  --bg-tertiary: #efefed;
  --text: #111113;
  --text-secondary: rgba(17,17,19,0.62);
  --text-muted: rgba(17,17,19,0.38);
  --circuit: #0088A0;
  --accent-red: #C9335A;
}

:root[data-theme="dark"] {
  --bg: #080809;
  --bg-secondary: #111113;
  --bg-tertiary: #1a1a1c;
  --text: #e0e0de;
  --text-secondary: rgba(224,224,222,0.55);
  --text-muted: rgba(224,224,222,0.30);
  --circuit: #00F3FF;
  --accent-red: #F43F6C;
}
```

## Theme System
- Theme toggle via `data-theme` attribute on `<html>`
- Persisted to localStorage key `aaas-theme`
- Default: follows system preference via `prefers-color-scheme`

## Implementation Rules
1. **Theme-first**: All components must support both light and dark themes
2. **CSS vars only**: Never hardcode hex colors — always use `var(--token)`
3. **Glassmorphism cards**: Dark = `rgba(255,255,255,0.04)` + `blur(24px)`, Light = `rgba(255,255,255,0.82)` + `blur(16px)`
4. **Typography**: Inter for all prose, JetBrains Mono for code/labels/system text
5. **Border radius**: Use `--radius-sm` (0.25rem), `--radius` (0.5rem), `--radius-lg` (0.75rem)
6. **Spacing**: Follow 4px base scale (0.25rem increments)
