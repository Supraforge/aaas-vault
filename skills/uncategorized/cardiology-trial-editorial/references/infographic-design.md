# Infographic Design Guide

Create engaging visual summaries that increase platform dwell time and make complex trials accessible at a glance.

## Design Philosophy

**Goal:** Professional medical infographic that works on LinkedIn, Twitter/X, Instagram, and newsletter platforms

**Key principles:**
- Evidence-based aesthetic (credible, not sensational)
- Mobile-first design (readable on phone screens)
- Screenshot-ready (no cropping needed)
- Accessible to physicians scrolling quickly
- Complements editorial (doesn't replace it)

## Dimensions and Format

**Optimal size:** 1200px width × 1600px height (3:4 aspect ratio)
- Works well on Instagram, LinkedIn, Twitter
- Mobile-friendly vertical orientation
- Professional portrait layout

**File format:** HTML with inline CSS/SVG
- Single self-contained file
- No external dependencies
- Easy to render and screenshot
- Can be opened in any browser

## Color Palette

### Primary Colors (Cardiology Theme)
```css
--navy-dark: #1E3A8A      /* Headers, emphasis */
--blue-primary: #3B82F6   /* Key metrics, icons */
--blue-light: #60A5FA     /* Backgrounds, accents */
--blue-pale: #DBEAFE      /* Section backgrounds */
```

### Accent Colors
```css
--red-warning: #EF4444    /* Cautions, limitations */
--green-positive: #10B981 /* Benefits, improvements */
--amber-neutral: #F59E0B  /* Wait/uncertain */
--gray-text: #374151      /* Body text */
--gray-light: #F3F4F6     /* Subtle backgrounds */
```

### Usage Guidelines
- **Headers:** Navy dark (#1E3A8A)
- **Key metrics:** Blue primary (#3B82F6), large and bold
- **Benefits/Change practice:** Green positive (#10B981)
- **Limitations/Wait:** Amber neutral (#F59E0B)
- **Unknowns/Gaps:** Red warning (#EF4444)
- **Body text:** Gray text (#374151)
- **Backgrounds:** White primary, blue pale for sections

## Typography

### Font Stack
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 
             'Helvetica Neue', Arial, sans-serif;
```

### Size Hierarchy
```css
--h1: 36px / 2.25rem   /* Trial name */
--h2: 28px / 1.75rem   /* Section headers */
--h3: 20px / 1.25rem   /* Subsection labels */
--body: 16px / 1rem    /* Details */
--metric: 48px / 3rem  /* Key numbers */
--small: 14px / 0.875rem /* Citations */
```

### Weight Hierarchy
- **Trial name:** 700 (bold)
- **Key metric:** 700 (bold)
- **Section headers:** 600 (semibold)
- **Body text:** 400 (regular)
- **Citations:** 400 (regular)

## Layout Structure

### Six-Section Vertical Layout

```
┌─────────────────────────────────────────┐
│ 1. HEADER SECTION                       │ ← 200px
│    • Trial acronym/name                 │
│    • One-line hook                      │
├─────────────────────────────────────────┤
│ 2. HERO METRIC                          │ ← 300px
│    • Large visual of key finding       │
│    • Icon + number + context           │
│    • NNT if applicable                 │
├─────────────────────────────────────────┤
│ 3. TRIAL DETAILS                        │ ← 200px
│    • Design, N, endpoint               │
│    • Brief description                 │
├─────────────────────────────────────────┤
│ 4. THREE-PANEL COMPARISON               │ ← 500px
│    ┌──────┬──────┬──────┐              │
│    │ ✓    │ ⚠    │ ❓    │              │
│    │CHANGE│ WAIT │UNKNOWN│              │
│    │      │      │       │              │
│    └──────┴──────┴──────┘              │
├─────────────────────────────────────────┤
│ 5. BOTTOM LINE                          │ ← 200px
│    • Key takeaway box                  │
│    • Actionable insight                │
├─────────────────────────────────────────┤
│ 6. FOOTER                               │ ← 200px
│    • Citation                          │
│    • Dr. [Your Name]                   │
└─────────────────────────────────────────┘
Total: ~1600px
```

## Section-by-Section Design

### Section 1: Header (200px)

```html
<div class="header">
  <h1>TRIAL ACRONYM</h1>
  <p class="hook">Compelling one-liner about what changed</p>
</div>
```

**Design specs:**
- Background: White or blue-pale gradient
- Trial name: Navy dark, 36px, bold, uppercase
- Hook: Gray text, 20px, regular
- Padding: 40px top/bottom, 30px sides

**Example:**
```
PARTNER 3
TAVR Moves to Low-Risk Patients with Superior Outcomes
```

### Section 2: Hero Metric (300px)

```html
<div class="hero-metric">
  <div class="icon">❤️</div>
  <div class="comparison">
    <div class="result">8.5%</div>
    <div class="vs">vs</div>
    <div class="comparator">15.1%</div>
  </div>
  <div class="context">Death, Stroke, or Rehospitalization at 1 Year</div>
  <div class="nnt">NNT = 15</div>
</div>
```

**Design specs:**
- Background: Blue pale (#DBEAFE)
- Icon: 64px, centered, heart or relevant medical symbol
- Numbers: 48px, bold, blue primary for result, gray for comparator
- VS: 24px, gray, between numbers
- Context: 18px, gray text
- NNT: 20px, navy dark, highlighted box

**Visual layout:**
```
       ❤️
    
   8.5%  vs  15.1%
   
Death, Stroke, or Rehospitalization at 1 Year

    NNT = 15
```

### Section 3: Trial Details (200px)

```html
<div class="trial-details">
  <div class="detail-row">
    <span class="label">Design:</span>
    <span class="value">Multicenter RCT</span>
  </div>
  <div class="detail-row">
    <span class="label">Patients:</span>
    <span class="value">N=1,000 (low surgical risk, severe AS)</span>
  </div>
  <div class="detail-row">
    <span class="label">Intervention:</span>
    <span class="value">TAVR vs Surgical AVR</span>
  </div>
</div>
```

**Design specs:**
- Background: White
- Layout: Two-column (label left, value right)
- Label: 16px, semibold, gray text
- Value: 16px, regular, navy dark
- Border: Subtle gray divider between rows
- Padding: 20px all sides

### Section 4: Three-Panel Comparison (500px)

```html
<div class="three-panel">
  <div class="panel change-practice">
    <div class="panel-icon">✓</div>
    <h3>Change Practice</h3>
    <ul>
      <li>Low-risk severe AS</li>
      <li>Age < 80 years</li>
      <li>Transfemoral access</li>
    </ul>
  </div>
  
  <div class="panel wait">
    <div class="panel-icon">⚠</div>
    <h3>Wait for Data</h3>
    <ul>
      <li>Age < 65 years</li>
      <li>Bicuspid valves</li>
      <li>Need for longevity</li>
    </ul>
  </div>
  
  <div class="panel unknown">
    <div class="panel-icon">❓</div>
    <h3>Still Unknown</h3>
    <ul>
      <li>Durability > 5 years</li>
      <li>RV impact of PPM</li>
      <li>Cost-effectiveness</li>
    </ul>
  </div>
</div>
```

**Design specs:**
- Layout: 3 equal columns (33% each)
- Panel backgrounds:
  - Change Practice: Light green tint (#ECFDF5)
  - Wait: Light amber tint (#FEF3C7)
  - Unknown: Light red tint (#FEE2E2)
- Icons: 32px, matching panel color
- Headers: 20px, semibold, matching panel color (darker shade)
- List items: 15px, regular, gray text
- Bullets: Panel-colored circles
- Padding: 20px all sides
- Border radius: 8px

**Visual layout:**
```
┌──────────┬──────────┬──────────┐
│    ✓     │    ⚠     │    ❓     │
│  CHANGE  │   WAIT   │  UNKNOWN │
│ PRACTICE │          │          │
│          │          │          │
│ • Item 1 │ • Item 1 │ • Item 1 │
│ • Item 2 │ • Item 2 │ • Item 2 │
│ • Item 3 │ • Item 3 │ • Item 3 │
└──────────┴──────────┴──────────┘
```

### Section 5: Bottom Line (200px)

```html
<div class="bottom-line">
  <div class="icon">🎯</div>
  <p class="takeaway">For low-risk severe AS patients, TAVR is now a 
  guideline-supported option alongside surgery, with superior short-term 
  outcomes balanced against uncertain long-term durability.</p>
</div>
```

**Design specs:**
- Background: Navy dark (#1E3A8A)
- Text color: White
- Icon: 32px, gold/yellow emoji
- Takeaway: 18px, regular, white text
- Padding: 30px all sides
- Border: 3px solid blue primary

**Visual emphasis:**
- This is the "screenshot gold" - what people remember
- Should be quotable and actionable
- Max 2 sentences

### Section 6: Footer (200px)

```html
<div class="footer">
  <div class="citation">
    <strong>Source:</strong> Mack MJ, et al. NEJM 2019;380(18):1695-1705. 
    PMID: 30883058
  </div>
  <div class="attribution">
    <div class="author">Dr. [Your Name]</div>
    <div class="credentials">Interventional Cardiologist</div>
  </div>
</div>
```

**Design specs:**
- Background: Gray light (#F3F4F6)
- Citation: 14px, regular, gray text
- Author: 18px, semibold, navy dark
- Credentials: 14px, regular, gray text
- Layout: Two-column (citation left, author right)
- Padding: 30px all sides

## Icon Library

### Medical Symbols (Unicode)
- Heart: ❤️ (U+2764)
- Medical symbol: ⚕️ (U+2695)
- Check mark: ✓ (U+2713)
- Warning: ⚠ (U+26A0)
- Question: ❓ (U+2753)
- Target: 🎯 (U+1F3AF)
- Chart: 📊 (U+1F4CA)
- Syringe: 💉 (U+1F489)
- Pills: 💊 (U+1F48A)
- Microscope: 🔬 (U+1F52C)

### Simple SVG Icons (When Unicode Insufficient)

**Heart with EKG Line:**
```svg
<svg width="64" height="64" viewBox="0 0 64 64">
  <path d="M32 54L10 32C4 26 4 16 10 10C16 4 26 4 32 10C38 4 48 4 54 10C60 16 60 26 54 32L32 54Z" 
        fill="#3B82F6"/>
  <path d="M10 32L20 32L24 28L28 36L32 32L54 32" 
        stroke="#FFFFFF" stroke-width="2" fill="none"/>
</svg>
```

**Stethoscope:**
```svg
<svg width="64" height="64" viewBox="0 0 64 64">
  <circle cx="48" cy="48" r="8" fill="#3B82F6"/>
  <path d="M20 10C20 6 24 6 24 10L24 30C24 40 34 50 48 50" 
        stroke="#3B82F6" stroke-width="3" fill="none"/>
  <circle cx="20" cy="10" r="4" fill="#1E3A8A"/>
  <circle cx="24" cy="10" r="4" fill="#1E3A8A"/>
</svg>
```

## Data Visualization

### Comparison Bars

For showing differences between groups:

```html
<div class="comparison-bars">
  <div class="bar-group">
    <div class="bar-label">TAVR</div>
    <div class="bar" style="width: 8.5%;">
      <span class="bar-value">8.5%</span>
    </div>
  </div>
  <div class="bar-group">
    <div class="bar-label">Surgery</div>
    <div class="bar" style="width: 15.1%;">
      <span class="bar-value">15.1%</span>
    </div>
  </div>
</div>
```

**Design specs:**
- Bar height: 40px
- TAVR bar: Green (#10B981)
- Surgery bar: Gray (#6B7280)
- Values: 16px, bold, white text inside bar
- Labels: 16px, regular, gray text on left
- Normalize to make visual difference clear

### Simple Risk Reduction

Visual representation of NNT:

```html
<div class="nnt-visual">
  <div class="people-grid">
    <!-- 15 person icons, 1 highlighted -->
    <div class="person highlighted">👤</div>
    <div class="person">👤</div>
    <!-- ... repeat 13 more times -->
  </div>
  <p class="nnt-text">1 in 15 patients benefits from TAVR</p>
</div>
```

## Complete HTML Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[Trial Name] - Infographic</title>
<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 
               'Helvetica Neue', Arial, sans-serif;
  background: #ffffff;
  width: 1200px;
  height: 1600px;
  margin: 0 auto;
}

.infographic {
  width: 100%;
  height: 100%;
  background: white;
  display: flex;
  flex-direction: column;
}

/* Header Section */
.header {
  background: linear-gradient(135deg, #DBEAFE 0%, #ffffff 100%);
  padding: 40px 30px;
  text-align: center;
  border-bottom: 4px solid #3B82F6;
}

.header h1 {
  font-size: 36px;
  font-weight: 700;
  color: #1E3A8A;
  margin-bottom: 10px;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.header .hook {
  font-size: 20px;
  color: #374151;
  line-height: 1.4;
}

/* Hero Metric Section */
.hero-metric {
  background: #DBEAFE;
  padding: 40px 30px;
  text-align: center;
}

.hero-metric .icon {
  font-size: 64px;
  margin-bottom: 20px;
}

.hero-metric .comparison {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  margin-bottom: 15px;
}

.hero-metric .result {
  font-size: 48px;
  font-weight: 700;
  color: #3B82F6;
}

.hero-metric .vs {
  font-size: 24px;
  color: #6B7280;
}

.hero-metric .comparator {
  font-size: 48px;
  font-weight: 700;
  color: #9CA3AF;
}

.hero-metric .context {
  font-size: 18px;
  color: #374151;
  margin-bottom: 15px;
}

.hero-metric .nnt {
  display: inline-block;
  background: #1E3A8A;
  color: white;
  font-size: 20px;
  font-weight: 600;
  padding: 10px 30px;
  border-radius: 25px;
}

/* Trial Details Section */
.trial-details {
  background: white;
  padding: 30px;
}

.detail-row {
  display: flex;
  padding: 12px 0;
  border-bottom: 1px solid #E5E7EB;
}

.detail-row:last-child {
  border-bottom: none;
}

.detail-row .label {
  font-size: 16px;
  font-weight: 600;
  color: #6B7280;
  width: 150px;
  flex-shrink: 0;
}

.detail-row .value {
  font-size: 16px;
  color: #1E3A8A;
  flex-grow: 1;
}

/* Three-Panel Section */
.three-panel {
  display: flex;
  gap: 20px;
  padding: 30px;
  background: #F9FAFB;
}

.panel {
  flex: 1;
  padding: 25px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.panel.change-practice {
  background: #ECFDF5;
  border: 2px solid #10B981;
}

.panel.wait {
  background: #FEF3C7;
  border: 2px solid #F59E0B;
}

.panel.unknown {
  background: #FEE2E2;
  border: 2px solid #EF4444;
}

.panel-icon {
  font-size: 32px;
  text-align: center;
  margin-bottom: 15px;
}

.panel h3 {
  font-size: 20px;
  font-weight: 600;
  text-align: center;
  margin-bottom: 20px;
}

.panel.change-practice h3 {
  color: #059669;
}

.panel.wait h3 {
  color: #D97706;
}

.panel.unknown h3 {
  color: #DC2626;
}

.panel ul {
  list-style: none;
}

.panel li {
  font-size: 15px;
  color: #374151;
  line-height: 1.6;
  padding: 8px 0;
  padding-left: 25px;
  position: relative;
}

.panel li::before {
  content: "●";
  position: absolute;
  left: 0;
  font-size: 18px;
}

.panel.change-practice li::before {
  color: #10B981;
}

.panel.wait li::before {
  color: #F59E0B;
}

.panel.unknown li::before {
  color: #EF4444;
}

/* Bottom Line Section */
.bottom-line {
  background: #1E3A8A;
  padding: 35px 40px;
  border: 3px solid #3B82F6;
  margin: 20px 30px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  gap: 20px;
}

.bottom-line .icon {
  font-size: 32px;
  flex-shrink: 0;
}

.bottom-line .takeaway {
  font-size: 18px;
  color: white;
  line-height: 1.6;
  font-weight: 400;
}

/* Footer Section */
.footer {
  background: #F3F4F6;
  padding: 30px;
  margin-top: auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.footer .citation {
  font-size: 14px;
  color: #6B7280;
  max-width: 60%;
}

.footer .citation strong {
  color: #374151;
}

.footer .attribution {
  text-align: right;
}

.footer .author {
  font-size: 18px;
  font-weight: 600;
  color: #1E3A8A;
  margin-bottom: 4px;
}

.footer .credentials {
  font-size: 14px;
  color: #6B7280;
}
</style>
</head>
<body>
<div class="infographic">
  
  <!-- Header Section -->
  <div class="header">
    <h1>[TRIAL ACRONYM]</h1>
    <p class="hook">[Compelling one-liner about key finding]</p>
  </div>
  
  <!-- Hero Metric Section -->
  <div class="hero-metric">
    <div class="icon">❤️</div>
    <div class="comparison">
      <div class="result">[X.X%]</div>
      <div class="vs">vs</div>
      <div class="comparator">[Y.Y%]</div>
    </div>
    <div class="context">[Primary endpoint description]</div>
    <div class="nnt">NNT = [Z]</div>
  </div>
  
  <!-- Trial Details Section -->
  <div class="trial-details">
    <div class="detail-row">
      <span class="label">Design:</span>
      <span class="value">[Study design]</span>
    </div>
    <div class="detail-row">
      <span class="label">Patients:</span>
      <span class="value">[N and population]</span>
    </div>
    <div class="detail-row">
      <span class="label">Intervention:</span>
      <span class="value">[Treatment vs control]</span>
    </div>
  </div>
  
  <!-- Three-Panel Comparison -->
  <div class="three-panel">
    <div class="panel change-practice">
      <div class="panel-icon">✓</div>
      <h3>Change Practice</h3>
      <ul>
        <li>[Population characteristic]</li>
        <li>[Population characteristic]</li>
        <li>[Population characteristic]</li>
      </ul>
    </div>
    
    <div class="panel wait">
      <div class="panel-icon">⚠</div>
      <h3>Wait for Data</h3>
      <ul>
        <li>[Uncertain population]</li>
        <li>[Uncertain population]</li>
        <li>[Uncertain population]</li>
      </ul>
    </div>
    
    <div class="panel unknown">
      <div class="panel-icon">❓</div>
      <h3>Still Unknown</h3>
      <ul>
        <li>[Unanswered question]</li>
        <li>[Unanswered question]</li>
        <li>[Unanswered question]</li>
      </ul>
    </div>
  </div>
  
  <!-- Bottom Line -->
  <div class="bottom-line">
    <div class="icon">🎯</div>
    <p class="takeaway">[2-sentence actionable clinical takeaway]</p>
  </div>
  
  <!-- Footer -->
  <div class="footer">
    <div class="citation">
      <strong>Source:</strong> [First Author] et al. [Journal] [Year];[Vol]([Issue]):[Pages]. PMID: [PMID]
    </div>
    <div class="attribution">
      <div class="author">Dr. [Your Name]</div>
      <div class="credentials">Interventional Cardiologist</div>
    </div>
  </div>
  
</div>
</body>
</html>
```

## Content Guidelines

### What to Include

**Header:**
- Trial acronym or short name (e.g., "PARTNER 3", "ISCHEMIA", "COAPT")
- Hook must be outcome-focused, not process-focused
  - Good: "TAVR Superior to Surgery in Low-Risk Patients"
  - Bad: "New Study Compares TAVR and Surgery"

**Hero Metric:**
- Primary endpoint result as comparison
- Always show absolute numbers, not just relative
- Include NNT when meaningful (typically NNT 5-50 range)
- Use icons that relate to outcome (heart for cardiac, brain for stroke)

**Trial Details:**
- Design: Be specific (e.g., "Double-blind RCT" not just "RCT")
- Patients: Include N and key population feature
- Intervention: Show both arms clearly

**Three Panels:**
- Change Practice: Specific population characteristics where benefit is clear
- Wait: Populations where more data needed or benefit uncertain
- Unknown: Key unanswered questions (durability, long-term safety, cost)
- Each panel: 2-4 bullet points max

**Bottom Line:**
- Max 2 sentences
- Actionable and quotable
- Balance benefit and uncertainty
- Patient-centered when possible

**Footer:**
- Full citation with PMID for traceability
- Your name and credentials for authority

### What to Avoid

**Don't:**
- Use more than 3 colors in data visualizations
- Include p-values unless truly necessary (focus on effect size)
- Crowd the design - white space is professional
- Use clipart or stock photos
- Include more than 1 chart/graph per infographic
- Make font sizes smaller than 14px
- Use all caps except for trial name
- Include your photo (keeps focus on science)

## Responsive Considerations

While designed at 1200×1600px, ensure readability when scaled:

**At 600px width (50% scale):**
- Minimum 7px font size
- Icons still recognizable
- Three panels stack vertically on very narrow screens (not typical for this size)

**Testing checklist:**
- Open HTML in browser at 100%
- Take screenshot (should be 1200×1600)
- View at 50% zoom - still readable?
- Print to PDF - maintains quality?

## Export and Usage

**For LinkedIn:**
- Screenshot the full HTML page
- Upload as image post
- Add editorial text as caption
- Tag relevant hashtags (#Cardiology #TAVR #MedEd)

**For Twitter/X:**
- Same screenshot
- Thread: Infographic as first tweet, editorial key points as subsequent tweets
- Alt text for accessibility

**For Instagram:**
- Screenshot works well in feed
- Consider adding branded border if posting regularly
- Use stories for swipe-up to full editorial

**For Newsletter:**
- Embed HTML directly OR
- Include screenshot with link to read full editorial
- Infographic increases open rate and engagement

## Accessibility

**Alt text template:**
```
"[Trial Name] infographic showing [key finding]: [intervention] resulted in 
[X%] vs [Y%] for [comparator] in [population]. Change practice for 
[specific population], wait for data on [uncertain populations], 
still unknown: [key questions]."
```

**Screen reader friendly:**
- Use semantic HTML (header, section, footer)
- Ensure color contrast meets WCAG AA standards (4.5:1 for normal text)
- All data conveyed in text, not just visually

## Quality Checklist

Before delivering infographic:
- [ ] Trial name/acronym is accurate
- [ ] Numbers match editorial (primary endpoint, NNT)
- [ ] Citation is complete with PMID
- [ ] User's name and credentials included
- [ ] Three panels have 2-4 items each
- [ ] Bottom line is quotable and actionable
- [ ] All fonts are readable at mobile size
- [ ] Color contrast is sufficient
- [ ] No spelling or grammar errors
- [ ] HTML renders correctly in Chrome/Safari/Firefox
- [ ] File is self-contained (no external dependencies)
- [ ] Screenshot dimensions are 1200×1600

## Advanced: Animated Version (Optional)

For higher engagement on social media, consider subtle animations:

```css
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.header { animation: fadeIn 0.6s ease-out; }
.hero-metric { animation: fadeIn 0.8s ease-out 0.2s backwards; }
.three-panel { animation: fadeIn 1s ease-out 0.4s backwards; }
```

**Only use if:**
- Posting on platforms that support HTML/CSS (rare)
- Creating video version (screen record the HTML)
- User specifically requests animated version

**Default:** Static screenshot is preferred for maximum compatibility
