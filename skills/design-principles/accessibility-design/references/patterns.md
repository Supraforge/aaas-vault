# Accessibility Design

## Patterns


---
  #### **Name**
Semantic HTML First
  #### **Description**
Use native HTML elements with built-in accessibility before reaching for ARIA
  #### **When**
Building any user interface component
  #### **Example**
    # BAD: Div soup with ARIA
    <div role="button" tabindex="0" onclick="handleClick()">
      Submit
    </div>
    
    # GOOD: Native HTML
    <button type="submit">Submit</button>
    
    Semantic element benefits:
    - <button> - keyboard accessible, role announced, click on Enter/Space
    - <a href> - focusable, role announced, click on Enter
    - <nav> - landmark region for screen readers
    - <main> - skip to main content target
    - <form> - groups related inputs, handles submit
    - <label for="id"> - clicks focus input, announced by screen readers
    
    Rule: Only use ARIA when HTML cannot express the semantics.
    

---
  #### **Name**
Visible Focus Indicators
  #### **Description**
Ensure all interactive elements have clear, visible focus states for keyboard users
  #### **When**
Styling any focusable element (buttons, links, inputs, custom controls)
  #### **Example**
    # BAD: Removes focus without alternative
    button:focus { outline: none; }
    
    # GOOD: Custom focus-visible style
    button:focus { outline: none; }
    button:focus-visible {
      outline: 2px solid #005fcc;
      outline-offset: 2px;
    }
    
    Focus indicator requirements:
    - Contrast ratio 3:1 against adjacent colors
    - Minimum 2px thickness
    - Surrounds entire component or has clear indicator
    - Works in both light and dark mode
    - Never removed entirely, only styled appropriately
    

---
  #### **Name**
Color Is Not The Only Indicator
  #### **Description**
Never rely solely on color to convey meaning - always provide additional cues
  #### **When**
Designing status indicators, errors, required fields, data visualizations
  #### **Example**
    # BAD: Color only
    <span style="color: red;">*</span>
    <div class="status-green"></div>
    
    # GOOD: Color + icon + text
    <span aria-hidden="true">*</span>
    <span class="visually-hidden">(required)</span>
    
    <div class="status">
      <svg aria-hidden="true"><!-- checkmark --></svg>
      <span>Completed</span>
    </div>
    
    For charts/graphs:
    - Use patterns/textures in addition to colors
    - Add direct labels, not just legends
    - Use distinct line styles (solid, dashed, dotted)
    

---
  #### **Name**
Accessible Form Design
  #### **Description**
Design forms that are usable by screen readers, keyboard users, and those with cognitive disabilities
  #### **When**
Creating any form input, validation, or form flow
  #### **Example**
    <form>
      <!-- Label explicitly connected -->
      <label for="email">Email address</label>
      <input
        type="email"
        id="email"
        name="email"
        aria-describedby="email-hint email-error"
        aria-invalid="true"
        required
      />
      <span id="email-hint">We'll never share your email</span>
      <span id="email-error" role="alert">
        Please enter a valid email address
      </span>
    </form>
    
    Form accessibility checklist:
    - [ ] Every input has a visible label (not just placeholder)
    - [ ] Labels are programmatically associated (for/id)
    - [ ] Error messages are announced (role="alert" or aria-live)
    - [ ] Required fields are indicated visually AND programmatically
    - [ ] Instructions appear before the form, not just after
    - [ ] Tab order follows visual order
    

---
  #### **Name**
Skip Links for Navigation
  #### **Description**
Provide skip links to let keyboard users bypass repetitive content
  #### **When**
Page has navigation, header content, or repetitive elements before main content
  #### **Example**
    <!-- First focusable element on page -->
    <a href="#main-content" class="skip-link">
      Skip to main content
    </a>
    
    <header><!-- Logo, nav, etc. --></header>
    
    <main id="main-content" tabindex="-1">
      <!-- Main page content -->
    </main>
    
    CSS for skip link (visible on focus):
    .skip-link {
      position: absolute;
      left: -10000px;
      top: auto;
      width: 1px;
      height: 1px;
      overflow: hidden;
    }
    
    .skip-link:focus {
      position: fixed;
      top: 0;
      left: 0;
      width: auto;
      height: auto;
      padding: 1rem;
      background: #000;
      color: #fff;
      z-index: 9999;
    }
    

---
  #### **Name**
Focus Management for Dynamic Content
  #### **Description**
Manage focus intentionally when content changes dynamically (modals, page transitions, deletions)
  #### **When**
Opening modals, single-page app navigation, removing items, showing alerts
  #### **Example**
    // Modal opens: Move focus to modal
    function openModal() {
      modal.showModal(); // Native dialog handles focus
      // Or manually: firstFocusableElement.focus();
    }
    
    // Modal closes: Return focus to trigger
    function closeModal() {
      modal.close();
      triggerButton.focus();
    }
    
    // Item deleted: Move focus to logical place
    function deleteItem(item) {
      const nextItem = item.nextSibling || item.previousSibling;
      item.remove();
      nextItem?.focus(); // Don't leave focus in void
    }
    
    // SPA navigation: Focus main content
    router.afterEach(() => {
      document.getElementById('main-content').focus();
    });
    

---
  #### **Name**
ARIA Live Regions for Dynamic Updates
  #### **Description**
Use ARIA live regions to announce dynamic content changes to screen reader users
  #### **When**
Content updates without page refresh (notifications, search results, counters)
  #### **Example**
    <!-- Polite: Announced at next pause -->
    <div aria-live="polite" aria-atomic="true">
      3 results found
    </div>
    
    <!-- Assertive: Interrupts immediately (use sparingly) -->
    <div role="alert">
      Your session will expire in 5 minutes
    </div>
    
    <!-- Status role: Polite by default -->
    <div role="status">
      Saving...
    </div>
    
    Live region rules:
    - aria-live="polite" for non-urgent (most cases)
    - aria-live="assertive" or role="alert" for urgent only
    - aria-atomic="true" to read entire region, not just changes
    - Keep messages concise
    - Region must exist in DOM before content changes
    

---
  #### **Name**
Alternative Text Strategy
  #### **Description**
Provide meaningful alt text for images that conveys the same information or function
  #### **When**
Adding any image to a design or implementation
  #### **Example**
    # Informative images: Describe the content
    <img src="chart.png" alt="Sales increased 40% from Q1 to Q2 2024" />
    
    # Functional images: Describe the function
    <img src="search-icon.png" alt="Search" />
    
    # Decorative images: Empty alt
    <img src="decorative-border.png" alt="" />
    
    # Complex images: Detailed description
    <figure>
      <img src="flowchart.png" alt="User registration flow" />
      <figcaption>
        <details>
          <summary>Full description</summary>
          Step 1: Enter email. Step 2: Verify email...
        </details>
      </figcaption>
    </figure>
    
    Alt text decision tree:
    1. Is it purely decorative? -> alt=""
    2. Does it contain text? -> Include all text in alt
    3. Is it a link/button? -> Describe destination/action
    4. Is it informative? -> Describe the information
    5. Is it complex? -> Provide long description
    

---
  #### **Name**
Touch Target Sizing
  #### **Description**
Ensure all interactive elements have adequate touch target size for motor accessibility
  #### **When**
Designing buttons, links, form controls, or any clickable element
  #### **Example**
    Touch target requirements:
    - WCAG 2.2 Level AA: 24x24 CSS pixels minimum
    - WCAG 2.2 Level AAA: 44x44 CSS pixels
    - Apple HIG: 44x44 points
    - Material Design: 48x48 dp
    
    # Small icon with adequate target
    <button style="padding: 12px">
      <svg width="20" height="20"><!-- icon --></svg>
    </button>
    <!-- 20px icon + 12px padding each side = 44px target -->
    
    # Expand clickable area with pseudo-element
    .small-button {
      position: relative;
    }
    .small-button::after {
      content: '';
      position: absolute;
      inset: -12px; /* Expands target by 12px each direction */
    }
    

---
  #### **Name**
Reduced Motion Respect
  #### **Description**
Respect user's prefers-reduced-motion setting and provide alternatives to animation
  #### **When**
Adding any animation, transition, or motion to the interface
  #### **Example**
    /* Default animations */
    .card {
      transition: transform 0.3s ease;
    }
    .card:hover {
      transform: scale(1.05);
    }
    
    /* Reduced motion alternative */
    @media (prefers-reduced-motion: reduce) {
      .card {
        transition: none;
      }
      .card:hover {
        transform: none;
        /* Use non-motion alternative */
        box-shadow: 0 0 0 2px var(--focus-color);
      }
    }
    
    Reduced motion guidelines:
    - Remove parallax scrolling entirely
    - Replace slide transitions with fades or instant
    - Stop auto-playing animations
    - Provide controls for any essential motion
    - Never remove functionality, only motion
    

---
  #### **Name**
Logical Reading and Tab Order
  #### **Description**
Ensure content order in DOM matches visual order and creates logical navigation flow
  #### **When**
Laying out page content, creating navigation, using CSS Grid/Flexbox
  #### **Example**
    # BAD: Visual order differs from DOM order
    <div style="display: flex; flex-direction: row-reverse;">
      <button>Cancel</button>  <!-- Tab 1: But appears last visually -->
      <button>Submit</button>  <!-- Tab 2: But appears first visually -->
    </div>
    
    # GOOD: DOM matches visual order
    <div style="display: flex;">
      <button>Submit</button>  <!-- Tab 1: Appears first -->
      <button>Cancel</button>  <!-- Tab 2: Appears second -->
    </div>
    
    Tab order rules:
    - DOM order = reading order = tab order
    - Never use tabindex > 0 (creates maintenance nightmare)
    - Use tabindex="0" to make non-interactive elements focusable
    - Use tabindex="-1" for programmatic focus only
    - CSS order/flex-direction/grid-area don't change tab order
    

---
  #### **Name**
Accessible Data Tables
  #### **Description**
Structure data tables so screen readers can navigate and understand relationships
  #### **When**
Presenting tabular data (not for layout - never use tables for layout)
  #### **Example**
    <table>
      <caption>Q4 2024 Sales by Region</caption>
      <thead>
        <tr>
          <th scope="col">Region</th>
          <th scope="col">Q3 Sales</th>
          <th scope="col">Q4 Sales</th>
          <th scope="col">Change</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">North America</th>
          <td>$1.2M</td>
          <td>$1.5M</td>
          <td>+25%</td>
        </tr>
      </tbody>
    </table>
    
    Table accessibility requirements:
    - <caption> describes the table's purpose
    - <th scope="col"> for column headers
    - <th scope="row"> for row headers
    - Complex tables: Use headers/id attributes
    - Never use tables for layout
    - Consider mobile: tables may need horizontal scroll
    

## Anti-Patterns


---
  #### **Name**
Color-Only Status Indicators
  #### **Description**
Using only color to indicate status, errors, or required fields
  #### **Why**
8% of men and 0.5% of women have color vision deficiency. Information conveyed by color alone is invisible to them.
  #### **Instead**
    # BAD
    <input class="error-border-red" />
    <span class="status-green"></span>
    
    # GOOD
    <input class="error" aria-invalid="true" aria-describedby="error-msg" />
    <span id="error-msg" class="error-message">
      <svg><!-- error icon --></svg>
      Invalid email format
    </span>
    
    Always add: icon, text, pattern, or position change alongside color.
    

---
  #### **Name**
Mouse-Only Interactions
  #### **Description**
Features that only work with mouse hover or click without keyboard alternatives
  #### **Why**
Keyboard-only users, screen reader users, and users with motor impairments cannot use mouse-dependent interfaces.
  #### **Instead**
    # BAD: Hover-only dropdown
    .dropdown:hover .menu { display: block; }
    
    # GOOD: Keyboard accessible
    .dropdown:hover .menu,
    .dropdown:focus-within .menu { display: block; }
    
    <!-- Or use disclosure pattern -->
    <button aria-expanded="false" aria-controls="menu">Menu</button>
    <div id="menu" hidden>...</div>
    
    All interactions need: mouse + keyboard + touch equivalents.
    

---
  #### **Name**
Auto-Playing Media
  #### **Description**
Audio or video that plays automatically without user initiation
  #### **Why**
Interferes with screen readers, startles users, causes cognitive overload, wastes data on mobile.
  #### **Instead**
    # BAD
    <video autoplay>
    
    # GOOD
    <video controls>
      <track kind="captions" src="captions.vtt" srclang="en" label="English">
    </video>
    
    If autoplay is essential:
    - Mute by default (autoplay muted)
    - Provide visible pause/stop control
    - Keep under 5 seconds
    - No auto-repeating
    

---
  #### **Name**
Removing Focus Outlines Without Alternatives
  #### **Description**
Using outline:none or outline:0 globally without providing visible focus alternatives
  #### **Why**
Keyboard users cannot see where they are on the page. It's equivalent to hiding the mouse cursor.
  #### **Instead**
    # THE CRIME
    *:focus { outline: none; }
    
    # THE FIX
    *:focus { outline: none; }
    *:focus-visible {
      outline: 2px solid var(--focus-color);
      outline-offset: 2px;
    }
    
    Focus-visible shows outlines for keyboard, hides for mouse clicks.
    

---
  #### **Name**
Placeholder Text as Labels
  #### **Description**
Using placeholder attribute as the only label for form inputs
  #### **Why**
Placeholder disappears when typing, fails contrast requirements, not reliably announced by screen readers.
  #### **Instead**
    # BAD
    <input placeholder="Email address" />
    
    # GOOD
    <label for="email">Email address</label>
    <input id="email" placeholder="you@example.com" />
    
    Placeholder is a hint, not a label. Labels must persist.
    

---
  #### **Name**
ARIA Overload
  #### **Description**
Using ARIA attributes when native HTML semantics would work
  #### **Why**
ARIA is a last resort. Native HTML has built-in accessibility. ARIA requires manual implementation of all behaviors.
  #### **Instead**
    # BAD: ARIA overload
    <div role="button" tabindex="0" aria-pressed="false"
         onkeydown="handleKeyDown(event)" onclick="handleClick()">
      Toggle
    </div>
    
    # GOOD: Native HTML
    <button type="button" aria-pressed="false">
      Toggle
    </button>
    
    First rule of ARIA: Don't use ARIA if you can use native HTML.
    

---
  #### **Name**
Time Limits Without Extensions
  #### **Description**
Session timeouts or timed actions without warning or extension capability
  #### **Why**
Users with disabilities may need more time to read, understand, and complete actions.
  #### **Instead**
    # BAD: Silent timeout
    setTimeout(logout, 15 * 60 * 1000);
    
    # GOOD: Warning with extension
    function warnTimeout() {
      showModal({
        title: "Session Expiring",
        message: "Your session will expire in 2 minutes.",
        actions: [
          { label: "Extend Session", action: extendSession },
          { label: "Log Out", action: logout }
        ],
        autoFocus: true
      });
    }
    
    WCAG requires: warn before timeout, allow extension, or allow 20+ hours.
    

---
  #### **Name**
Keyboard Traps
  #### **Description**
Components that trap keyboard focus without an escape route
  #### **Why**
Keyboard users get stuck and cannot continue using the page.
  #### **Instead**
    # Modal MUST have escape route
    dialog.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeModal();
      }
    });
    
    # Focus trap must cycle within modal
    # Tab from last element goes to first
    # Shift+Tab from first goes to last
    
    Always provide: Escape key to close, or clear close button, or both.
    

---
  #### **Name**
Missing Skip Links
  #### **Description**
No way to skip repetitive navigation content
  #### **Why**
Screen reader and keyboard users must tab through all navigation on every page load.
  #### **Instead**
    <!-- First element in body -->
    <a href="#main" class="skip-link">Skip to main content</a>
    
    For complex pages, offer multiple skip links:
    - Skip to main content
    - Skip to search
    - Skip to footer
    

---
  #### **Name**
Non-Dismissible Overlays
  #### **Description**
Popups, modals, or overlays that cannot be dismissed via keyboard
  #### **Why**
Keyboard users cannot close the overlay and continue using the page.
  #### **Instead**
    Modal requirements:
    1. Escape key closes modal
    2. Close button is focusable and announced
    3. Click outside closes (optional but expected)
    4. Focus returns to trigger element on close
    
    <button onclick="openModal()" id="trigger">Open</button>
    <dialog onclose="document.getElementById('trigger').focus()">
      <button onclick="this.closest('dialog').close()">Close</button>
    </dialog>
    

---
  #### **Name**
Missing Error Identification
  #### **Description**
Form errors that don't clearly identify which field has the problem
  #### **Why**
Users cannot fix errors if they don't know which field is wrong or what's wrong with it.
  #### **Instead**
    # BAD: Generic error
    <div class="error">Please fix the errors above.</div>
    
    # GOOD: Specific, associated errors
    <input id="email" aria-invalid="true" aria-describedby="email-error" />
    <span id="email-error" role="alert">
      Email address must include @ symbol
    </span>
    
    Error messages must: identify the field, explain the problem, suggest fix.
    