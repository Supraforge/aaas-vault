# Packaging Print Production - Validations

## RGB Color Mode in Print Files

### **Id**
rgb-color-mode-detection
### **Description**
Detects files that may be in RGB mode instead of CMYK
### **Severity**
critical
### **Category**
color-management
### **File Patterns**
  - *.ai
  - *.psd
  - *.indd
  - *.pdf
  - *.svg
### **Check Type**
content_pattern
### **Patterns**
  
---
    ##### **Pattern**
ColorSpace.*RGB
    ##### **Message**
File contains RGB color space - convert to CMYK before printing
  
---
    ##### **Pattern**
rgb\s*\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*\)
    ##### **Message**
Found RGB color values - use CMYK for print production
  
---
    ##### **Pattern**
fill="#[0-9A-Fa-f]{6}"
    ##### **Message**
SVG contains hex colors (RGB) - export as CMYK PDF for print
### **Fix Guidance**
  1. Open file in native application
  2. Convert color mode: File > Document Color Mode > CMYK
  3. Use Proof Colors (View > Proof Colors) to preview CMYK output
  4. Adjust out-of-gamut colors manually
  5. Re-export as CMYK PDF/X-4
  

## K100 Black in Large Areas

### **Id**
pure-black-large-areas
### **Description**
Detects pure black (K100 only) in areas that should use rich black
### **Severity**
high
### **Category**
color-management
### **File Patterns**
  - *.ai
  - *.svg
  - *.pdf
### **Check Type**
content_pattern
### **Patterns**
  
---
    ##### **Pattern**
fill\s*[=:]\s*["']?(?:black|#000000|#000|rgb\s*\(\s*0\s*,\s*0\s*,\s*0\s*\))
    ##### **Message**
Found pure black - for large areas use rich black (C60 M40 Y40 K100)
  
---
    ##### **Pattern**
k\s*[=:]\s*100.*[cm].*[=:]\s*0
    ##### **Message**
Found K100 with 0% CMY - add CMY values for rich black in large areas
### **Exceptions**
  - Text elements under 12pt
  - Barcodes
  - QR codes
  - Fine lines under 1pt
### **Fix Guidance**
  For large black areas (backgrounds, borders):
  - Change from: C=0, M=0, Y=0, K=100
  - Change to:   C=60, M=40, Y=40, K=100 (neutral rich black)
  
  Keep K100 only for:
  - Small text (under 12pt)
  - Barcodes and QR codes
  - Fine lines and details
  

## Out-of-Gamut Colors

### **Id**
out-of-gamut-colors
### **Description**
Warns about colors that cannot be reproduced in CMYK
### **Severity**
high
### **Category**
color-management
### **File Patterns**
  - *.svg
  - *.css
  - *.html
### **Check Type**
content_pattern
### **Patterns**
  
---
    ##### **Pattern**
rgb\s*\(\s*0\s*,\s*25[0-5]\s*,\s*0\s*\)
    ##### **Message**
Neon green (0,255,0) cannot be reproduced in CMYK - will become dull
  
---
    ##### **Pattern**
rgb\s*\(\s*25[0-5]\s*,\s*0\s*,\s*25[0-5]\s*\)
    ##### **Message**
Neon magenta (255,0,255) cannot be reproduced in CMYK - will lose vibrancy
  
---
    ##### **Pattern**
rgb\s*\(\s*0\s*,\s*25[0-5]\s*,\s*25[0-5]\s*\)
    ##### **Message**
Neon cyan (0,255,255) cannot be reproduced in CMYK
  
---
    ##### **Pattern**
#00FF00|#0F0\b
    ##### **Message**
Pure green (#00FF00) is out of CMYK gamut
  
---
    ##### **Pattern**
#FF00FF|#F0F\b
    ##### **Message**
Pure magenta (#FF00FF) is out of CMYK gamut
  
---
    ##### **Pattern**
#00FFFF|#0FF\b
    ##### **Message**
Pure cyan (#00FFFF) is out of CMYK gamut
### **Fix Guidance**
  1. Enable gamut warning in your design application
  2. Identify flagged colors and find CMYK-safe alternatives
  3. Accept that some vibrancy loss is unavoidable
  4. Consider Pantone spot colors for critical brand colors
  5. Test with physical proof before production
  

## Missing or Insufficient Bleed

### **Id**
missing-bleed
### **Description**
Checks for proper bleed area in print files
### **Severity**
critical
### **Category**
file-preparation
### **File Patterns**
  - *.pdf
  - *.ai
  - *.indd
### **Check Type**
content_pattern
### **Patterns**
  
---
    ##### **Pattern**
/BleedBox.*\[\s*0\s+0\s+
    ##### **Message**
PDF BleedBox starts at origin - verify bleed is included
  
---
    ##### **Pattern**
/TrimBox.*\[\s*(\d+\.?\d*)\s+(\d+\.?\d*)\s+(\d+\.?\d*)\s+(\d+\.?\d*)\s*\]
    ##### **Message**
Verify TrimBox is smaller than MediaBox/BleedBox by 3mm on each side
### **Manual Check**
  Automated bleed detection is limited. Manually verify:
  1. Document has 3mm bleed defined
  2. All edge-touching artwork extends to bleed boundary
  3. No important content within 4-5mm of trim line (safe zone)
  
### **Fix Guidance**
  Standard bleed requirements:
  - Cards: 3mm all edges
  - Boxes: 3mm all edges
  - Game boards: 10mm for fold-over edges
  - Punchboards: 3mm around entire board, 3mm around each token
  
  Add bleed in design application before export.
  

## Low Resolution Images for Print

### **Id**
low-resolution-images
### **Description**
Detects images that may be too low resolution for quality printing
### **Severity**
high
### **Category**
file-preparation
### **File Patterns**
  - *.html
  - *.css
  - *.svg
### **Check Type**
content_pattern
### **Patterns**
  
---
    ##### **Pattern**
(?:72|96)\s*(?:dpi|ppi)
    ##### **Message**
Image at screen resolution (72/96 dpi) - print requires 300 dpi minimum
  
---
    ##### **Pattern**
resolution\s*[=:]\s*[1-9]\d?\s*(?:dpi|ppi)
    ##### **Message**
Image below 100 dpi - will appear pixelated in print
### **Note**
  Resolution in linked files cannot be fully verified via pattern matching.
  Use design application's preflight tools:
  - Illustrator: Window > Document Info > Linked Files
  - InDesign: Window > Links (check effective ppi)
  - Acrobat: Print Production > Preflight
  
### **Fix Guidance**
  All images must be:
  - 300 DPI minimum at final print size
  - No upscaling (enlarging increases apparent low resolution)
  - Embedded, not linked (for final production files)
  
  Formula: Final print size (inches) x 300 = required pixel dimensions
  

## Fonts Not Converted to Outlines

### **Id**
font-not-outlined
### **Description**
Checks for fonts that should be outlined for print production
### **Severity**
medium
### **Category**
file-preparation
### **File Patterns**
  - *.pdf
### **Check Type**
content_pattern
### **Patterns**
  
---
    ##### **Pattern**
/Type\s*/Font
    ##### **Message**
PDF contains embedded fonts - consider outlining all text for production
### **Note**
  Embedded fonts are acceptable if:
  - Full font is embedded (not subset)
  - Manufacturer confirms font support
  
  Outlining is safer but increases file size and prevents text editing.
  
### **Fix Guidance**
  To outline fonts in Illustrator:
  1. Select All (Cmd/Ctrl + A)
  2. Type > Create Outlines (Cmd/Ctrl + Shift + O)
  3. Save as new file (preserve editable version)
  
  Verify no text remains:
  - Type > Find Font should show empty list
  

## Fonts Below Minimum Print Size

### **Id**
small-font-detection
### **Description**
Detects font sizes that may be too small for print legibility
### **Severity**
high
### **Category**
typography
### **File Patterns**
  - *.svg
  - *.css
  - *.html
### **Check Type**
content_pattern
### **Patterns**
  
---
    ##### **Pattern**
font-size\s*[=:]\s*[1-5](?:\.\d+)?(?:pt|px)
    ##### **Message**
Font size under 6pt - may be illegible in print
  
---
    ##### **Pattern**
font-size\s*[=:]\s*6(?:\.\d+)?(?:pt|px)
    ##### **Message**
6pt font detected - verify this is only for footnotes/legal text
  
---
    ##### **Pattern**
font-size\s*[=:]\s*7(?:\.\d+)?(?:pt|px)
    ##### **Message**
7pt font detected - acceptable for secondary text only
### **Recommendations**
  Minimum font sizes for print:
  - Body text: 8pt minimum
  - Secondary text: 7pt
  - Fine print/footnotes: 6pt (absolute minimum)
  - Reversed text (light on dark): Add 1pt to above
  

## Thin Font Weights for Small Text

### **Id**
thin-font-weights
### **Description**
Warns about light/thin font weights that may not print well at small sizes
### **Severity**
medium
### **Category**
typography
### **File Patterns**
  - *.svg
  - *.css
### **Check Type**
content_pattern
### **Patterns**
  
---
    ##### **Pattern**
font-weight\s*[=:]\s*(?:100|200|thin|hairline|extra-?light)
    ##### **Message**
Thin/light font weight may not print clearly - use regular (400) or bold for small text
  
---
    ##### **Pattern**
font-family.*(?:Thin|Light|Hairline)
    ##### **Message**
Light font variant detected - verify legibility at print size
### **Fix Guidance**
  For text under 10pt:
  - Use Regular (400) or Medium (500) weight minimum
  - Avoid Thin (100), Extra-Light (200), Light (300)
  - Sans-serif fonts maintain legibility better than serif at small sizes
  

## Non-Standard Dieline Colors

### **Id**
dieline-color-standards
### **Description**
Checks for correct dieline color coding
### **Severity**
medium
### **Category**
file-structure
### **File Patterns**
  - *.ai
  - *.svg
  - *.pdf
### **Check Type**
content_pattern
### **Patterns**
  
---
    ##### **Pattern**
(?:cut|die).*(?:line|path).*(?:black|#000)
    ##### **Message**
Cut/die lines should be Magenta (not black) for industry standard
  
---
    ##### **Pattern**
(?:fold|score).*(?:line|path).*(?:black|#000)
    ##### **Message**
Fold/score lines should be Cyan (not black) for industry standard
### **Note**
  Industry standard dieline colors:
  - Cut lines: 100% Magenta (red appearance)
  - Fold lines: 100% Cyan (blue appearance)
  - Bleed boundary: 50% Magenta + 100% Yellow (orange)
  
  Dieline layer should be:
  - Non-printing (set to spot color marked "non-printing")
  - Locked (prevent accidental modification)
  - Named clearly: "DIELINE" or "DIE"
  

## Spot Color Not Properly Separated

### **Id**
spot-color-separation
### **Description**
Checks for spot colors that may not be properly set up
### **Severity**
medium
### **Category**
file-structure
### **File Patterns**
  - *.pdf
  - *.ai
### **Check Type**
content_pattern
### **Patterns**
  
---
    ##### **Pattern**
/Separation.*PANTONE
    ##### **Message**
Pantone spot color detected - verify with manufacturer that spot colors are expected
  
---
    ##### **Pattern**
/DeviceN.*\[.*PANTONE
    ##### **Message**
Multiple spot colors detected - confirm separations with printer
### **Note**
  Spot colors are appropriate for:
  - Foil stamping (separate layer)
  - Spot UV (separate layer)
  - Pantone brand colors (premium printing)
  
  Spot colors NOT appropriate for:
  - Standard CMYK printing (will be converted, may shift)
  - Low-budget print runs
  

## Insufficient Box Clearance

### **Id**
box-clearance-check
### **Description**
Checks for proper component clearance in box specifications
### **Severity**
medium
### **Category**
dimensions
### **Check Type**
specification_review
### **Rules**
  When reviewing box specifications:
  
  Minimum internal clearances:
  - Width: largest component + 15mm
  - Length: largest component + 15mm
  - Height: component stack + insert + 15mm
  
  Punchboard sizing:
  - Punchboard should be 15mm smaller per dimension than box top
  
  Insert compartments:
  - Unsleeved cards: +2mm width, +3mm height
  - Sleeved cards: +5mm width, +5mm height
  - Tokens: +3mm per dimension
  
  Verify against manufacturer templates.
  
### **Manual Check**


## Punchboard Token Spacing

### **Id**
token-spacing-check
### **Description**
Validates proper spacing between tokens on punchboards
### **Severity**
medium
### **Category**
dimensions
### **Check Type**
specification_review
### **Rules**
  Punchboard spacing requirements:
  
  Between tokens: 6mm minimum between any die lines
  Token to edge: 3mm bleed + 3mm margin = 6mm from artwork edge to board edge
  Token internal margin: 3mm from die line to non-background artwork
  
  If tokens are closer than 6mm:
  - Risk of tokens tearing during punching
  - Die cannot be manufactured accurately
  
  Verify with manufacturer's punchboard template.
  
### **Manual Check**


## Suboptimal Card Counts

### **Id**
card-count-optimization
### **Description**
Identifies card counts that don't optimize sheet usage
### **Severity**
low
### **Category**
cost-optimization
### **Check Type**
specification_review
### **Rules**
  Standard poker cards fit ~54 per sheet.
  Optimal deck sizes: 54, 108, 162, 216 (multiples of 54)
  
  Inefficient counts (examples):
  - 55-108 cards = 2 sheets (same as 108 cards)
  - 109-162 cards = 3 sheets (same as 162 cards)
  
  If your count is just over a multiple:
  - Consider adding content to fill sheet
  - Consider reducing cards to previous multiple
  
  Ask manufacturer for their specific sheet capacity.
  
### **Manual Check**


## Potentially Unnecessary Custom Die

### **Id**
unnecessary-custom-die
### **Description**
Flags custom shapes that could be simplified to standard dies
### **Severity**
low
### **Category**
cost-optimization
### **Check Type**
specification_review
### **Rules**
  Custom die costs: $200-500 per unique die
  
  Before using custom shapes, consider:
  - Can tokens be rectangular? (much cheaper)
  - Can similar tokens share a die pattern?
  - Does box match any standard manufacturer template?
  
  Standard (free) die shapes:
  - Rectangle with 3mm corner radius
  - Square with 3mm corner radius
  - Standard card sizes (poker, tarot, mini, etc.)
  - Standard box templates
  
  Review components and identify custom die requirements.
  
### **Manual Check**
