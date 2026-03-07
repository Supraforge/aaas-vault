# Wbcom Admin Wrapper - Improvement Notes

## High Priority Improvements

### 1. Accessibility (ARIA, Focus States)
**Priority**: High
**Effort**: 1 day
**Status**: In Progress

#### Current Issues
- Toggle switches lack `role="switch"` and `aria-checked` attributes
- Missing focus indicators on interactive elements
- No `aria-label` on icon-only buttons
- Screen reader text missing for key controls

#### Required Fixes

**a) Toggle Switches** (`wbcom-admin-setting.css`)
```css
/* Add visible focus indicator */
.wb-admin-switch input:focus + label {
    outline: 2px solid var(--primary-color);
    outline-offset: 2px;
}

/* Screen reader text class */
.screen-reader-text {
    position: absolute !important;
    width: 1px !important;
    height: 1px !important;
    padding: 0 !important;
    margin: -1px !important;
    overflow: hidden !important;
    clip: rect(0, 0, 0, 0) !important;
    white-space: nowrap !important;
    border: 0 !important;
}
```

**b) HTML Updates** (templates)
```php
<!-- Toggle switch with ARIA -->
<div class="wb-admin-switch" role="switch" aria-checked="<?php echo $checked ? 'true' : 'false'; ?>">
    <input type="hidden" name="..." value="no" />
    <input type="checkbox" id="..." name="..." value="yes"
           aria-describedby="desc-..."
           <?php checked(...); ?> />
    <label for="..."><span class="screen-reader-text"><?php _e('Toggle setting', 'text-domain'); ?></span></label>
</div>
<p class="description" id="desc-..."><?php _e('Description text', 'text-domain'); ?></p>
```

**c) Focus States for All Controls**
```css
/* Focus styles for all form elements */
.wbcom-settings-section-options input[type="text"]:focus,
.wbcom-settings-section-options input[type="number"]:focus,
.wbcom-settings-section-options select:focus,
.wbcom-settings-section-options textarea:focus {
    border-color: var(--primary-color);
    box-shadow: 0 0 0 2px rgba(42, 50, 239, 0.2);
    outline: none;
}

/* Focus indicator for checkboxes and radios */
.wbcom-settings-section-options input[type="checkbox"]:focus,
.wbcom-settings-section-options input[type="radio"]:focus {
    outline: 2px solid var(--primary-color);
    outline-offset: 2px;
}

/* Visible focus for buttons */
.wbcom-settings-section-options .button:focus {
    border-color: var(--primary-color);
    box-shadow: 0 0 0 2px rgba(42, 50, 239, 0.3);
}
```

---

### 2. RTL Logical Properties
**Priority**: High
**Effort**: 0.5 day
**Status**: In Progress

#### Current Issues
- Physical properties (`left`, `right`, `margin-left`, `padding-right`) don't flip for RTL
- Border radius corners don't flip
- Icons with directional meaning may need flipping

#### Required Fixes

**a) Replace Physical Properties with Logical**
```css
/* BEFORE (physical) */
.wbcom-settings-section-options-heading {
    padding-right: 20px;
    border-left: 3px solid var(--primary-color);
}

/* AFTER (logical) */
.wbcom-settings-section-options-heading {
    padding-inline-end: 20px;
    border-inline-start: 3px solid var(--primary-color);
}
```

**b) Mapping Reference**
| Physical Property | Logical Property |
|-------------------|------------------|
| `margin-left` | `margin-inline-start` |
| `margin-right` | `margin-inline-end` |
| `padding-left` | `padding-inline-start` |
| `padding-right` | `padding-inline-end` |
| `border-left` | `border-inline-start` |
| `border-right` | `border-inline-end` |
| `left` | `inset-inline-start` |
| `right` | `inset-inline-end` |
| `text-align: left` | `text-align: start` |
| `text-align: right` | `text-align: end` |
| `border-radius: 10px 0 0 10px` | `border-start-start-radius: 10px; border-end-start-radius: 10px;` |

**c) Icon Flipping for RTL**
```css
/* Icons that need to flip in RTL */
[dir="rtl"] .wbcom-icon-arrow,
[dir="rtl"] .wbcom-icon-chevron {
    transform: scaleX(-1);
}
```

---

## Medium Priority Improvements

### 3. Dark Mode Support
**Priority**: Medium
**Effort**: 2 days

```css
@media (prefers-color-scheme: dark) {
    :root {
        --background-light: #1a1a2e;
        --background-lighter: #16213e;
        --text-dark: #eaeaea;
        --text-medium: #b8b8b8;
        --border-color: rgba(255, 255, 255, 0.1);
    }
}
```

### 4. Variable Naming Consistency
**Priority**: Medium
**Effort**: 0.5 day

Standardize to semantic naming:
- `--color-primary` instead of `--primary-color`
- `--space-sm/md/lg` instead of `--spacing-sm/md/lg`
- `--radius-sm/md/lg` instead of `--border-radius-sm/md/lg`

---

## Low Priority Improvements

### 5. Remove Font Awesome Dependency
**Priority**: Low
**Effort**: 1 day

Replace with:
- Dashicons (WordPress built-in)
- SVG icons inline
- Custom icon font

### 6. Container Queries
**Priority**: Low
**Effort**: 0.5 day

```css
@container (min-width: 400px) {
    .wbcom-settings-section-wrap {
        flex-direction: row;
    }
}
```

---

## Implementation Checklist

### Accessibility (High)
- [ ] Add focus styles to `wbcom-admin-setting.css`
- [ ] Update toggle switch HTML in all templates
- [ ] Add `aria-describedby` to form controls
- [ ] Add `.screen-reader-text` class
- [ ] Test with keyboard navigation
- [ ] Test with screen reader

### RTL (High)
- [ ] Audit CSS for physical properties
- [ ] Replace with logical properties
- [ ] Test in RTL language (Arabic, Hebrew)
- [ ] Add icon flip rules where needed

---

## Testing

### Accessibility Testing
1. Navigate entire admin page using only Tab key
2. All focused elements should have visible indicator
3. Test with VoiceOver (Mac) or NVDA (Windows)
4. Run Lighthouse accessibility audit

### RTL Testing
1. Install WordPress in Arabic
2. Switch admin to RTL
3. Verify all layouts flip correctly
4. Check text alignment and spacing
