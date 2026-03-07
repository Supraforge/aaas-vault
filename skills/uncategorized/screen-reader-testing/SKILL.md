---
name: screen-reader-testing
description: >-
  Test web applications with screen readers including VoiceOver, NVDA, and JAWS.
  Use when validating screen reader compatibility, debugging accessibility
  issues, or ensuring assistive technology support.
version: 1.0.0
dependencies: []
compatibility: 'agent-zero, claude-code, cursor'
---

# Screen Reader Testing

Practical guide to testing web applications with screen readers for comprehensive accessibility validation.

## When to Use This Skill

- Validating screen reader compatibility
- Testing ARIA implementations
- Debugging assistive technology issues
- Verifying form accessibility
- Testing dynamic content announcements
- Ensuring navigation accessibility

## Core Concepts

### 1. Major Screen Readers

| Screen Reader | Platform  | Browser        | Usage |
| ------------- | --------- | -------------- | ----- |
| **VoiceOver** | macOS/iOS | Safari         | ~15%  |
| **NVDA**      | Windows   | Firefox/Chrome | ~31%  |
| **JAWS**      | Windows   | Chrome/IE      | ~40%  |
| **TalkBack**  | Android   | Chrome         | ~10%  |
| **Narrator**  | Windows   | Edge           | ~4%   |

### 2. Testing Priority

```
Minimum Coverage:
1. NVDA + Firefox (Windows)
2. VoiceOver + Safari (macOS)
3. VoiceOver + Safari (iOS)

Comprehensive Coverage:
+ JAWS + Chrome (Windows)
+ TalkBack + Chrome (Android)
+ Narrator + Edge (Windows)
```

### 3. Testing Modes

| Mode          | Description                     | Keyboard Shortcut          |
| ------------- | ------------------------------- | -------------------------- |
| **Browse**    | Navigate by elements            | Arrow keys                 |
| **Focus**     | Navigate by focusable items     | Tab                        |
| **Forms**     | Navigate form controls          | F (NVDA), Ctrl+Opt+U (VO)  |
| **Headings**  | Jump between headings           | H (NVDA), Cmd+Opt+H (VO)   |
| **Landmarks** | Jump between landmarks          | D (NVDA), Cmd+Opt+U (VO)   |

## Testing Checklist

### Page Structure
- [ ] Page has a logical heading structure (h1-h6)
- [ ] Landmarks are used appropriately (main, nav, aside, etc.)
- [ ] Page title is descriptive and unique
- [ ] Language attribute is set (`lang="en"`)
- [ ] Skip links are present and functional

### Navigation
- [ ] All interactive elements are keyboard accessible
- [ ] Focus order follows visual order
- [ ] Focus indicators are visible
- [ ] Modal dialogs trap focus
- [ ] Tabindex values are appropriate (0 or -1, never >0)

### Images & Media
- [ ] All images have alt text
- [ ] Decorative images have empty alt (`alt=""`)
- [ ] Complex images have long descriptions
- [ ] Video/audio has captions and transcripts
- [ ] SVG elements have proper accessibility attributes

### Forms
- [ ] All form fields have labels
- [ ] Required fields are indicated with `aria-required`
- [ ] Error messages are associated with fields (`aria-describedby`)
- [ ] Field instructions are clear and accessible
- [ ] Custom controls have proper ARIA roles

### Dynamic Content
- [ ] Live regions are used for dynamic updates (`aria-live`)
- [ ] Status messages are announced
- [ ] Loading states are communicated
- [ ] AJAX updates don't disrupt navigation
- [ ] Single Page App navigation is announced

### Tables
- [ ] Data tables have proper headers (`<th>`)
- [ ] Complex tables have captions and summaries
- [ ] Table cells are associated with headers
- [ ] Layout tables don't use table semantics

### Common Issues & Fixes

```html
<!-- Issue: Button not announcing purpose -->
<button><svg>...</svg></button>

<!-- Fix -->
<button aria-label="Close dialog"><svg aria-hidden="true">...</svg></button>

<!-- Issue: Dynamic content not announced -->
<div id="results">New results loaded</div>

<!-- Fix -->
<div id="results" role="status" aria-live="polite">New results loaded</div>

<!-- Issue: Form error not read -->
<input type="email" />
<span class="error">Invalid email</span>

<!-- Fix -->
<input type="email" aria-invalid="true" aria-describedby="email-error" />
<span id="email-error" role="alert">Invalid email</span>
```

## NVDA (Windows)

### Setup

```
Download: nvaccess.org
Start: Ctrl + Alt + N
Stop: Insert + Q
```

### Essential Commands

```
Navigation:
Insert = NVDA modifier

Down Arrow         Next line
Up Arrow           Previous line
Tab                Next focusable
Shift + Tab        Previous focusable

Reading:
NVDA + Down Arrow  Say all
Ctrl               Stop speech
NVDA + Up Arrow    Current line

Headings:
H                  Next heading
Shift + H          Previous heading
1-6                Heading level 1-6

Forms:
F                  Next form field
Shift + F          Previous form field
Space              Activate button/link
Enter              Activate button/link

Tables:
T                  Next table
Shift + T          Previous table
Ctrl + Alt + Arrows Navigate table cells
```

## VoiceOver (macOS)

### Setup

```
Enable: Cmd + F5
Open rotor: Ctrl + Opt + U
Web rotor: Ctrl + Opt + U twice
```

### Essential Commands

```
Navigation:
Ctrl + Opt + Right  Next item
Ctrl + Opt + Left   Previous item
Ctrl + Opt + Shift+Down Enter container
Ctrl + Opt + Shift+Up Exit container

Reading:
Ctrl + Opt + A      Read from current position
Ctrl + Opt + L      Read line
Ctrl + Opt + H      Read heading

Rotor Navigation:
Ctrl + Opt + U      Open rotor
Left/Right arrows   Rotor category
Up/Down arrows      Rotor item

Forms:
Ctrl + Opt + U, then F Forms rotor
Tab                Next form field
Shift + Tab        Previous form field
```

## JAWS (Windows)

### Setup

```
Commercial software - requires license
Start: Insert + J
Stop: Insert + F4
```

### Essential Commands

```
Navigation:
Insert + Numpad 5  Say current item
Insert + Down Arrow Read next line
Insert + Up Arrow  Read previous line
Tab               Next focusable
Shift + Tab       Previous focusable

Headings:
H                 Next heading
Shift + H         Previous heading
1-6               Heading level 1-6

Forms:
F                 Next form field
Shift + F         Previous form field
Enter             Activate button/link
Space             Activate button/link

Tables:
T                 Next table
Shift + T         Previous table
Ctrl + Alt + Arrows Navigate table cells
```

## Testing Workflow

### 1. Initial Setup

```bash
# Check if on appropriate platform
uname -a
# Check browser availability
which firefox which chrome which safari
```

### 2. Test Navigation

1. **Keyboard Only** - Navigate without mouse
2. **Screen Reader** - Navigate with screen reader
3. **Compare** - Ensure experiences are equivalent

### 3. Document Findings

```markdown
## Accessibility Test Results

### Page: Homepage

| Issue | Severity | Element | Screen Reader | Fix |
|-------|----------|---------|---------------|-----|
| Missing alt text | High | Hero image | NVDA, VoiceOver | Add descriptive alt attribute |
| Form label missing | High | Email input | JAWS | Add <label> or aria-label |
```

## Advanced Testing

### ARIA Widget Testing

```html
<!-- Test accordion -->
<div class="accordion">
  <button 
    aria-expanded="false" 
    aria-controls="panel-1"
    id="accordion-1"
  >
    Section 1
  </button>
  <div 
    id="panel-1" 
    role="region" 
    aria-labelledby="accordion-1"
    hidden
  >
    Content...
  </div>
</div>
```

### Tab Testing

```html
<div role="tablist">
  <button role="tab" id="tab-1" aria-selected="true" aria-controls="panel-1">
    Description
  </button>
  <button
    role="tab"
    id="tab-2"
    aria-selected="false"
    aria-controls="panel-2"
    tabindex="-1"
  >
    Reviews
  </button>
</div>

<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">
  Product description content...
</div>

<div role="tabpanel" id="panel-2" aria-labelledby="tab-2" hidden>
  Reviews content...
</div>
```

```javascript
// Tab keyboard navigation
tablist.addEventListener("keydown", (e) => {
  const tabs = [...tablist.querySelectorAll('[role="tab"]')];
  const index = tabs.indexOf(document.activeElement);

  let newIndex;
  switch (e.key) {
    case "ArrowRight":
      newIndex = (index + 1) % tabs.length;
      break;
    case "ArrowLeft":
      newIndex = (index - 1 + tabs.length) % tabs.length;
      break;
    case "Home":
      newIndex = 0;
      break;
    case "End":
      newIndex = tabs.length - 1;
      break;
    default:
      return;
  }

  tabs[newIndex].focus();
  activateTab(tabs[newIndex]);
  e.preventDefault();
});
```

## Debugging Tips

```javascript
// Log what screen reader sees
function logAccessibleName(element) {
  const computed = window.getComputedStyle(element);
  console.log({
    role: element.getAttribute("role") || element.tagName,
    name:
      element.getAttribute("aria-label") ||
      element.getAttribute("aria-labelledby") ||
      element.textContent,
    state: {
      expanded: element.getAttribute("aria-expanded"),
      selected: element.getAttribute("aria-selected"),
      checked: element.getAttribute("aria-checked"),
      disabled: element.disabled,
    },
    visible: computed.display !== "none" && computed.visibility !== "hidden",
  });
}
```

## Best Practices

### Do's

- **Test with actual screen readers** - Not just simulators
- **Use semantic HTML first** - ARIA is supplemental
- **Test in browse and focus modes** - Different experiences
- **Verify focus management** - Especially for SPAs
- **Test keyboard only first** - Foundation for SR testing

### Don'ts

- **Don't assume one SR is enough** - Test multiple
- **Don't ignore mobile** - Growing user base
- **Don't test only happy path** - Test error states
- **Don't skip dynamic content** - Most common issues
- **Don't rely on visual testing** - Different experience

## Resources

- [VoiceOver User Guide](https://support.apple.com/guide/voiceover/welcome/mac)
- [NVDA User Guide](https://www.nvaccess.org/files/nvda/documentation/userGuide.html)
- [JAWS Documentation](https://support.freedomscientific.com/Products/Blindness/JAWS)
- [WebAIM Screen Reader Survey](https://webaim.org/projects/screenreadersurvey/)
