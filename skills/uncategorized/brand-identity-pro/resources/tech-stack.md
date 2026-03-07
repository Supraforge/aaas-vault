# GoodHabitz Technical Implementation Guidelines

## Core Stack (Landing Pages)
*   **Structure**: Semantic HTML5.
*   **Styling**: Vanilla CSS with Design Tokens (CSS Variables).
*   **Interactivity**: Vanilla JavaScript (Intersection Observer for animations).
*   **Fonts**: Plus Jakarta Sans (loaded via Google Fonts).

## Implementation Rules
1.  **CSS Variables**: All brand colors, fonts, and spacing MUST be defined in `:root` variables.
2.  **Alignment**: Strictly left-align hero content with the brand logo. Max-width for hero content: `640px`.
3.  **Containers**: Standard max-width `1400px` with `60px` global padding.
4.  **Animations**:
    *   Use `IntersectionObserver` to trigger `.visible` classes.
    *   Micro-animations on hover for all buttons (`scale(1.02)`).
    *   Smooth scroll for anchor links.
5.  **Responsiveness**: Mobile-first or breakpoint-driven (`1024px`). Grid/Flex for layouts.

## UI Tokens
*   **Border Radius**: `16px` for cards/inputs, `8px` for buttons.
*   **Spacing Unit**: `4px` base.
*   **Typography**: H1 `56px`, H2/Body `18px`.
