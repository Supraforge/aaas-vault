# Accessibility Design - Sharp Edges

## Aria Misuse

### **Id**
aria-misuse
### **Summary**
Using ARIA incorrectly makes things worse than no ARIA at all
### **Severity**
critical
### **Situation**
  Adding aria-label to elements that already have accessible names,
  using role="button" on clickable divs without keyboard handling,
  aria-hidden="true" on visible interactive content.
  
### **Why**
  ARIA overrides native semantics. Incorrect ARIA creates confusion for screen reader
  users who hear conflicting information. A button with role="button" that doesn't
  respond to Enter/Space is worse than a div - users expect it to work.
  First rule of ARIA: Don't use ARIA if you can use native HTML.
  
### **Solution**
  # BEFORE USING ARIA, ask:
  # 1. Can I use a native HTML element instead? (Usually yes)
  # 2. Am I implementing ALL expected behaviors?
  # 3. Have I tested with actual screen readers?
  
  # BAD: ARIA on element with accessible name
  <button aria-label="Submit">Submit</button>
  <!-- Now screen reader says "Submit Submit" -->
  
  # BAD: role without behavior
  <div role="button">Click me</div>
  <!-- No keyboard support, not focusable -->
  
  # GOOD: Native HTML
  <button type="submit">Submit</button>
  
  # GOOD: If ARIA is necessary, implement fully
  <div role="button" tabindex="0"
       onkeydown="handleKeyDown(event)"
       onclick="handleClick()">
    Click me
  </div>
  
### **Symptoms**
  - Screen reader announces elements incorrectly
  - Keyboard users can't activate "buttons"
  - Elements announced as clickable but aren't
  - Double announcements of labels
### **Detection Pattern**
role="button"(?![^>]*tabindex)|aria-hidden="true"[^>]*(?:onclick|href)

## Focus Trap Escape

### **Id**
focus-trap-escape
### **Summary**
Modal focus traps that don't allow escape
### **Severity**
critical
### **Situation**
  Custom modal or dialog implementation that traps focus but has no escape route.
  Focus cycles within modal but Escape key doesn't close it, no visible close button,
  or close button isn't keyboard accessible.
  
### **Why**
  Keyboard and screen reader users are literally trapped. They cannot close the modal
  or return to the main page content. This is a complete blocker - not a minor issue.
  WCAG 2.1.2 requires that content not trap keyboard focus.
  
### **Solution**
  # Focus trap implementation requirements:
  1. Focus moves to modal on open
  2. Tab cycles through modal elements only
  3. Shift+Tab cycles backwards
  4. Escape key closes modal
  5. Close button is focusable and announced
  6. Focus returns to trigger element on close
  
  # Use native dialog element (handles most of this)
  <dialog id="modal">
    <button autofocus onclick="modal.close()">Close</button>
  </dialog>
  
  # Or implement manually:
  modal.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeModal();
    if (e.key === 'Tab') trapFocus(e);
  });
  
  function closeModal() {
    modal.hidden = true;
    triggerButton.focus(); // Return focus!
  }
  
### **Symptoms**
  - Users report being "stuck" in popups
  - Pressing Escape does nothing
  - Tab key doesn't move focus as expected
  - Support tickets about "frozen" interface
### **Detection Pattern**
role="dialog"(?![^>]*(?:aria-modal|onkeydown))

## Dynamic Content Not Announced

### **Id**
dynamic-content-not-announced
### **Summary**
Dynamic content updates not announced to screen reader users
### **Severity**
high
### **Situation**
  Search results update, form validation errors appear, notifications display,
  counter changes - all without any announcement to screen reader users.
  They don't know anything changed.
  
### **Why**
  Screen readers only read what they're pointed at. Dynamic content that appears
  elsewhere on screen is invisible unless explicitly announced. Users miss
  critical information, error feedback, and confirmation of actions.
  
### **Solution**
  # Use ARIA live regions for dynamic content
  
  # For status messages (non-urgent)
  <div role="status" aria-live="polite">
    <!-- Updates here are announced at next pause -->
    3 results found
  </div>
  
  # For errors/alerts (urgent)
  <div role="alert">
    <!-- Interrupts immediately -->
    Your session will expire in 5 minutes
  </div>
  
  # For loading states
  <div aria-live="polite" aria-busy="true">
    Loading...
  </div>
  
  Key rules:
  1. Live region must exist in DOM BEFORE content changes
  2. Use polite for most cases, assertive only for critical
  3. Keep messages brief and actionable
  4. Do not announce every keystroke (debounce search)
  
### **Symptoms**
  - Screen reader users miss notifications
  - Form errors not communicated
  - Users don't know search results updated
  - Users confused whether anything happened
### **Detection Pattern**


## Touch Target Too Small

### **Id**
touch-target-too-small
### **Summary**
Interactive elements smaller than minimum touch target size
### **Severity**
high
### **Situation**
  Icon buttons at 24px, links in dense text, close buttons in corners,
  checkbox labels that don't expand the clickable area.
  
### **Why**
  Small targets cause frustration for everyone and are impossible for users
  with motor impairments. WCAG 2.5.8 requires 24x24px minimum (AA) and recommends
  44x44px (AAA). Apple and Google both require 44px minimum.
  
### **Solution**
  # Minimum sizes:
  # WCAG AA: 24x24 CSS pixels
  # WCAG AAA / Mobile: 44x44 CSS pixels
  
  # Padding expands touch target
  <button style="padding: 12px;">
    <svg width="20" height="20"><!-- icon --></svg>
  </button>
  <!-- 20px icon + 24px padding = 44px target -->
  
  # Pseudo-element expansion (invisible)
  .icon-button {
    position: relative;
  }
  .icon-button::after {
    content: '';
    position: absolute;
    inset: -12px; /* Expands target invisibly */
  }
  
  # Labels expand checkbox targets
  <label>
    <input type="checkbox" />
    <span>Remember me</span>
  </label>
  <!-- Entire label is clickable -->
  
### **Symptoms**
  - High error rate on mobile
  - Users tapping wrong elements
  - Frustration with icons/small links
  - Motor-impaired users cannot interact
### **Detection Pattern**
width:\s*[0-2]?[0-9]px.*height:\s*[0-2]?[0-9]px|p-1\s|padding:\s*[0-4]px

## Heading Structure Chaos

### **Id**
heading-structure-chaos
### **Summary**
Missing, skipped, or illogical heading hierarchy
### **Severity**
high
### **Situation**
  Page has no h1, jumps from h1 to h4, uses headings for styling only,
  or has multiple h1s in main content (aside from header/logo).
  
### **Why**
  Screen reader users navigate by headings - it's like a table of contents.
  Skip levels (h1 to h3) create confusion. Multiple h1s or missing h1 breaks
  document structure. Headings used for styling (not structure) create false landmarks.
  
### **Solution**
  # Proper heading hierarchy
  <h1>Page Title</h1>           <!-- One per page -->
    <h2>Section 1</h2>          <!-- Major sections -->
      <h3>Subsection 1.1</h3>   <!-- Subsections -->
      <h3>Subsection 1.2</h3>
    <h2>Section 2</h2>
      <h3>Subsection 2.1</h3>
        <h4>Detail 2.1.1</h4>   <!-- Deeper nesting -->
  
  # Rules:
  - Exactly one h1 per page (the page title)
  - Never skip levels (h1 -> h3)
  - Use for structure, not styling
  - If you need the style without the semantics, use CSS classes
  
  # Checking structure:
  document.querySelectorAll('h1, h2, h3, h4, h5, h6')
  
### **Symptoms**
  - Screen reader users can't navigate page
  - Users lost and confused about location
  - Headings list in screen reader is useless
  - SEO penalties for poor structure
### **Detection Pattern**
<h3[^>]*>(?![^<]*<\/h3>[^<]*<h2)|<h4[^>]*>(?![^<]*<\/h4>[^<]*<h3)

## Low Contrast Text

### **Id**
low-contrast-text
### **Summary**
Text that fails WCAG contrast requirements
### **Severity**
critical
### **Situation**
  Light gray text on white backgrounds, placeholder text too faint,
  disabled states that are invisible, colored text on colored backgrounds.
  
### **Why**
  Affects 20%+ of users: low vision, color blindness, aging eyes, bright
  sunlight viewing, poor monitors. WCAG requires 4.5:1 for normal text,
  3:1 for large text. This is also one of the most common accessibility lawsuit triggers.
  
### **Solution**
  # Minimum contrast ratios (WCAG AA):
  - Normal text (<18px): 4.5:1
  - Large text (18px+ or 14px bold): 3:1
  - UI components and graphics: 3:1
  
  # BAD: Common failures
  #999999 on #FFFFFF → 2.85:1 (FAILS)
  #CCCCCC on #F5F5F5 → 1.4:1 (FAILS)
  
  # GOOD: Passing combinations
  #595959 on #FFFFFF → 7.0:1 (AAA)
  #767676 on #FFFFFF → 4.54:1 (AA)
  
  # Tools:
  - Chrome DevTools > Rendering > Emulate vision deficiencies
  - WebAIM Contrast Checker
  - Stark Figma plugin
  - Polypane color contrast tool
  
### **Symptoms**
  - Users complain they cannot read the text
  - Users zooming constantly
  - Complaints about specific pages/sections
  - Accessibility audit failures
### **Detection Pattern**
color:\s*#[cdef][cdef][cdef]|text-gray-[34]00\s|opacity:\s*0\.[0-4]

## Images Without Alt

### **Id**
images-without-alt
### **Summary**
Images missing alt text or using meaningless alt text
### **Severity**
critical
### **Situation**
  Images with no alt attribute, alt="image", alt="IMG_1234.jpg",
  or decorative images with descriptive alt text.
  
### **Why**
  Screen readers either skip images without alt (confusing) or read filename
  (useless). Images are 30%+ of web content - missing alt means missing 30% of
  your content for blind users. Also SEO penalty and legal liability.
  
### **Solution**
  # Decision tree for alt text:
  
  # 1. Decorative image? (borders, spacers, backgrounds)
  <img src="decorative.png" alt="" />
  <!-- Empty alt, announced as nothing -->
  
  # 2. Contains text?
  <img src="logo.png" alt="Acme Corporation" />
  <!-- Include ALL text in image -->
  
  # 3. Is a link/button?
  <a href="/search"><img src="search.png" alt="Search" /></a>
  <!-- Describe function, not appearance -->
  
  # 4. Informative image?
  <img src="chart.png" alt="Sales up 40% from Q1 to Q2 2024" />
  <!-- Describe the information conveyed -->
  
  # 5. Complex image needing long description?
  <figure>
    <img src="infographic.png" alt="2024 market overview infographic" />
    <figcaption>
      <a href="/infographic-text">Full text description</a>
    </figcaption>
  </figure>
  
### **Symptoms**
  - Screen readers say "image" with no context
  - Filenames read aloud
  - Blind users miss critical information
  - Accessibility lawsuits
### **Detection Pattern**
<img(?![^>]*alt=)|alt=""|alt="image"|alt="img"|alt="photo"

## Form Input No Label

### **Id**
form-input-no-label
### **Summary**
Form inputs without programmatically associated labels
### **Severity**
critical
### **Situation**
  Inputs with placeholder only, labels not connected via for/id,
  visual label present but not associated, aria-label used incorrectly.
  
### **Why**
  Screen reader users hear "edit text" with no context of what to enter.
  Clicking label doesn't focus input. Placeholder disappears when typing,
  leaving users unsure what field they're in. Most common WCAG failure.
  
### **Solution**
  # Method 1: for/id association (preferred)
  <label for="email">Email address</label>
  <input type="email" id="email" name="email" />
  
  # Method 2: Wrapping (works but less flexible)
  <label>
    Email address
    <input type="email" name="email" />
  </label>
  
  # Method 3: aria-labelledby (for complex layouts)
  <span id="email-label">Email address</span>
  <input type="email" aria-labelledby="email-label" />
  
  # Method 4: aria-label (when no visible label - avoid if possible)
  <input type="search" aria-label="Search products" />
  
  # NEVER rely on placeholder alone:
  # BAD: <input placeholder="Email" />
  # Placeholder is a hint, not a label
  
### **Symptoms**
  - Screen reader says "edit text" with no context
  - Clicking labels doesn't focus inputs
  - Users forget what field they're filling
  - Form abandonment
### **Detection Pattern**
<input(?![^>]*(?:aria-label|id="[^"]+"))|<input[^>]*id="([^"]+)"(?![^<]*for="\1")

## Keyboard Inaccessible Content

### **Id**
keyboard-inaccessible-content
### **Summary**
Interactive content that cannot be reached or activated via keyboard
### **Severity**
critical
### **Situation**
  Custom dropdowns, sliders, date pickers built with divs that aren't focusable.
  onClick handlers without keyboard equivalents. Content revealed only on hover.
  tabindex="-1" on interactive elements that should be focusable.
  
### **Why**
  15-20% of users navigate via keyboard: screen reader users, motor impairments,
  power users, temporary injuries. If it can't be reached and activated by
  keyboard, it doesn't exist for these users. WCAG 2.1.1 requires full keyboard access.
  
### **Solution**
  # Make elements focusable:
  # Native elements (<button>, <a>, <input>) are already focusable
  
  # Custom elements need tabindex="0":
  <div role="button" tabindex="0" onclick="..." onkeydown="...">
    Custom Button
  </div>
  
  # Keyboard activation (for custom controls):
  element.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      handleClick();
    }
  });
  
  # Test: Can you Tab to it and activate with Enter/Space?
  # If no, it's inaccessible.
  
  # Hover content must have keyboard equivalent:
  .tooltip { display: none; }
  .trigger:hover .tooltip,
  .trigger:focus .tooltip { display: block; }
  
### **Symptoms**
  - Tab key skips elements
  - Can't activate buttons with keyboard
  - Dropdown menus inaccessible
  - Features inaccessible to keyboard users
### **Detection Pattern**
onclick="[^"]*"(?![^>]*(?:onkeydown|tabindex|button|<a))

## Auto Playing Media

### **Id**
auto-playing-media
### **Summary**
Audio or video that plays automatically
### **Severity**
high
### **Situation**
  Background videos, audio players, auto-playing hero videos,
  video ads that play without user action.
  
### **Why**
  Interferes with screen reader output (audio overlap), startles users,
  can trigger seizures (flashing), wastes data/battery on mobile,
  disrupts users in quiet environments. WCAG requires user control.
  
### **Solution**
  # BAD
  <video autoplay>
  <audio autoplay>
  
  # ACCEPTABLE (if essential): Muted + controls
  <video autoplay muted playsinline>
    <track kind="captions" src="captions.vtt" srclang="en">
  </video>
  <button onclick="togglePlay()">Play/Pause</button>
  
  # BEST: No autoplay
  <video controls>
    <track kind="captions" src="captions.vtt" srclang="en">
  </video>
  
  # Rules for auto-playing content:
  - Must be muted (autoplay muted)
  - Must have visible pause control
  - Should stop after 5 seconds
  - Must have reduced motion alternative
  - Must not auto-restart
  
### **Symptoms**
  - Screen reader users can't hear announcements
  - Complaints about noise
  - Users immediately leaving page
  - Battery/data complaints on mobile
### **Detection Pattern**
<video[^>]*autoplay(?![^>]*muted)|<audio[^>]*autoplay

## Missing Language Attribute

### **Id**
missing-language-attribute
### **Summary**
Page or content sections missing language declaration
### **Severity**
medium
### **Situation**
  HTML element without lang attribute, or content in different language
  without lang attribute on that element.
  
### **Why**
  Screen readers use lang attribute to determine pronunciation. Without it,
  French text might be read with English pronunciation (incomprehensible).
  Also affects translation tools and search engines.
  
### **Solution**
  # Set page language
  <html lang="en">
  
  # Set different language for sections
  <p>The French word for hello is <span lang="fr">bonjour</span>.</p>
  
  # Common language codes:
  - en (English)
  - es (Spanish)
  - fr (French)
  - de (German)
  - zh (Chinese)
  - ja (Japanese)
  - ar (Arabic - also add dir="rtl")
  
  # Validate with:
  document.documentElement.lang // Should not be empty
  
### **Symptoms**
  - Foreign words mispronounced by screen readers
  - Translation tools confused
  - SEO issues for multilingual sites
### **Detection Pattern**
<html(?![^>]*lang=)

## Timing Without Extension

### **Id**
timing-without-extension
### **Summary**
Time limits that cannot be extended or disabled
### **Severity**
high
### **Situation**
  Session timeouts, timed forms, auto-advancing carousels,
  any action that expires or changes without user control.
  
### **Why**
  Users with disabilities need more time: screen reader users read slower,
  users with cognitive disabilities process slower, motor-impaired users
  type slower. WCAG 2.2.1 requires user control over timing.
  
### **Solution**
  # Session timeout: Warn and allow extension
  function warnBeforeTimeout() {
    // Show modal 2 minutes before expiry
    showModal({
      message: "Session expires in 2 minutes",
      actions: [
        { label: "Extend session", action: extendSession },
        { label: "Log out now", action: logout }
      ],
      // Focus the extend button
      autoFocus: 'extend'
    });
  }
  
  # Carousels: Let user control
  <div role="region" aria-label="Featured items">
    <button aria-label="Pause rotation">Pause</button>
    <button aria-label="Previous slide">Previous</button>
    <button aria-label="Next slide">Next</button>
  </div>
  
  # WCAG timing requirements:
  - User can turn off time limit, OR
  - User can extend time (at least 10x), OR
  - Time limit is 20+ hours
  
### **Symptoms**
  - Users lose work due to timeouts
  - Can't complete forms in time
  - Carousels change before users finish reading
  - Frustration complaints
### **Detection Pattern**
setTimeout.*logout|setInterval.*next.*slide