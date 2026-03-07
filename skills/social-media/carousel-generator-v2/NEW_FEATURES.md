# Carousel Generator V2 - New Features

**Last Updated:** 2026-01-01
**Status:** Production Ready

## Overview

Two major P1 features have been implemented to complete the Carousel Generator V2 visual overhaul:

1. **DataSlide with Plotly Integration** - Publication-grade data visualization
2. **Author Profile Configuration System** - Dynamic branding without code edits

---

## Feature 1: DataSlide with Plotly Charts

### What It Does

Embeds publication-quality Plotly charts (forest plots, bar charts, line graphs, survival curves) directly into carousel slides at 300 DPI resolution.

### When to Use

| Slide Type | Use Case |
|------------|----------|
| **StatSlide** | Simple statistics (percentages, single numbers, ratios) |
| **DataSlide** | Complex data visualizations (forest plots, multi-group comparisons, trends) |

### Architecture

```
SlideContent (chart_data) → Plotly Chart Generation → PNG @ 300 DPI → DataSlide React Component → Puppeteer Screenshot
```

### Supported Chart Types

| Type | Use Case | Example |
|------|----------|---------|
| **forest** | Meta-analysis results | Hazard ratios across trials |
| **bar** | Group comparisons | Treatment vs Control outcomes |
| **line** | Trends over time | Mortality rate changes |
| **survival** | Kaplan-Meier curves | Survival probability over time |

### Code Example

```python
from puppeteer_renderer import PuppeteerRenderer

renderer = PuppeteerRenderer(dimensions="portrait")

# Forest plot example
forest_data = {
    "studies": ["PARADIGM-HF", "DAPA-HF", "EMPEROR-Reduced"],
    "estimates": [0.80, 0.74, 0.75],
    "lower_ci": [0.73, 0.65, 0.65],
    "upper_ci": [0.87, 0.85, 0.86],
    "null_value": 1.0
}

data_slide = renderer.create_data_slide(
    slide_number=3,
    total_slides=6,
    title="Hazard Ratios Across Trials",
    chart_data=forest_data,
    chart_type="forest",
    caption="All trials showed significant mortality reduction",
    source="Meta-analysis 2024",
    icon="BarChart3"
)

# Bar chart example
bar_data = {
    "data": {
        "Outcome": ["Primary Endpoint", "Secondary Endpoint", "Safety Event"],
        "Treatment": [12.3, 8.5, 3.2],
        "Placebo": [18.7, 14.2, 2.8]
    },
    "x": "Outcome",
    "y": "Treatment"
}

bar_slide = renderer.create_data_slide(
    slide_number=4,
    total_slides=6,
    title="Treatment Outcomes",
    chart_data=bar_data,
    chart_type="bar",
    caption="Treatment showed superior outcomes",
    source="RCT 2024"
)
```

### React Component

**Location:** `renderer/src/components/templates/DataSlide.tsx`

**Props:**
```typescript
interface DataSlideData {
  slideNumber: number;
  totalSlides: number;
  title: string;
  chartPath: string;        // Path to Plotly-generated PNG
  caption?: string;
  source?: string;
  icon?: string;            // lucide-react icon name
  dimensions?: 'square' | 'portrait';
}
```

**Design Features:**
- Publication-grade chart container with rounded corners and shadow
- Icon badge matching brand colors
- Title and caption with proper hierarchy
- Source citation in italics
- Responsive to square (1080×1080) or portrait (1080×1350) layouts

### Fallback Behavior

If Plotly is not installed or chart generation fails:
- Automatically falls back to **StatSlide** template
- No carousel generation failure
- Warning printed to console

### Dependencies

```bash
pip install plotly pandas kaleido
```

---

## Feature 2: Author Profile Configuration

### What It Does

Centralizes author branding (name, credentials, photo, handles, follower counts) in a JSON config file. CTA slides automatically use the correct profile without code edits.

### Configuration File

**Location:** `config/author-config.json`

```json
{
  "author": {
    "name": "Dr Shailesh Singh",
    "credentials": "Cardiologist | Evidence-Based Medicine",
    "photo": "assets/5e4311be9235ba207024edfb13240abe8cf20f3f.png",
    "accounts": {
      "1": {
        "handle": "@heartdocshailesh",
        "platform": "Instagram",
        "followerCount": "50K+",
        "bio": "Follow for evidence-based cardiology insights"
      },
      "2": {
        "handle": "@dr.shailesh.singh",
        "platform": "Instagram",
        "followerCount": "25K+",
        "bio": "Clinical cardiology and lifestyle medicine"
      }
    },
    "defaultAccount": "1"
  },
  "branding": {
    "tagline": "Evidence-Based Cardiology",
    "secondaryText": "New posts every week",
    "valueProposition": "Follow for myth-busting cardiology content"
  }
}
```

### Usage

```python
# Account 1 (primary)
renderer = PuppeteerRenderer(dimensions="portrait", account=1)
cta_slide = renderer.create_cta_slide(slide_number=6, total_slides=6)
# Uses: @heartdocshailesh, 50K+ followers

# Account 2 (secondary)
renderer = PuppeteerRenderer(dimensions="portrait", account=2)
cta_slide = renderer.create_cta_slide(slide_number=6, total_slides=6)
# Uses: @dr.shailesh.singh, 25K+ followers

# Override specific fields
cta_slide = renderer.create_cta_slide(
    slide_number=6,
    total_slides=6,
    value_proposition="Custom message here",
    follower_count="100K+"
)
```

### CTA Slide Output

**With Account 1:**
- Name: Dr Shailesh Singh
- Credentials: Cardiologist | Evidence-Based Medicine
- Handle: @heartdocshailesh (coral accent color)
- Follower count: 50K+
- Photo: Circular profile image with heart badge
- Value proposition: "Follow for myth-busting cardiology content"
- Secondary text: "New posts every week"

### Photo Path Resolution

The system supports multiple photo path formats:

```json
{
  "photo": "assets/photo.png"                           // Resolved to @/assets/photo.png
  "photo": "@/assets/photo.png"                          // Used as-is
  "photo": "https://example.com/photo.jpg"               // External URL (used as-is)
}
```

React alias `@/` maps to `renderer/src/` directory.

### Fallback Behavior

If config file is missing or malformed:
- Uses hardcoded default values
- Warning printed to console
- No carousel generation failure

---

## Integration with Existing Pipeline

### carousel_employee.py

No changes needed. The `PuppeteerRenderer` is already integrated as the default renderer.

### carousel_generator.py

```python
from scripts.puppeteer_renderer import PuppeteerRenderer

# Initialize with account selection
renderer = PuppeteerRenderer(
    dimensions="portrait",
    account=1  # or 2
)

# Generate carousel
result = generator.generate_from_topic(
    "Heart failure trials",
    template="data_driven",
    use_ai=True
)
```

### SlideContent Model Extension

To use DataSlide from content pipeline, add these fields to `SlideContent`:

```python
class SlideContent:
    # ... existing fields ...
    chart_data: Optional[Dict[str, Any]] = None      # Plotly chart data
    chart_type: Optional[str] = None                 # 'bar', 'forest', 'line', 'survival'
```

When `slide_type == "data"` and `chart_data` is present, the renderer automatically generates a Plotly chart and uses DataSlide.

---

## File Structure

```
carousel-generator-v2/
├── config/
│   └── author-config.json              # Author profile configuration (NEW)
│
├── renderer/
│   └── src/
│       └── components/
│           ├── RenderPage.tsx          # Updated: Added 'data' slide type
│           └── templates/
│               ├── DataSlide.tsx       # NEW: Chart embed slide
│               ├── CTASlide.tsx        # Updated: Uses photoPath prop
│               ├── HookSlide.tsx
│               ├── MythSlide.tsx
│               ├── StatSlide.tsx
│               └── TipsSlide.tsx
│
└── scripts/
    ├── puppeteer_renderer.py           # Updated: Config loading, Plotly integration
    └── test_new_features.py            # NEW: Test suite for new features
```

---

## Testing

Run the test suite to verify all features:

```bash
cd skills/cardiology/carousel-generator-v2
python scripts/test_new_features.py
```

**Test Coverage:**
1. DataSlide with forest plot
2. DataSlide with bar chart
3. Author config with Account 1
4. Author config with Account 2
5. Full carousel with all features

**Output:** Generated carousels in `outputs/test_*` directories

---

## Troubleshooting

### Plotly charts not generating

**Symptom:** DataSlide falls back to StatSlide
**Solution:**
```bash
pip install plotly pandas kaleido --break-system-packages
```

### CTA slide shows initials instead of photo

**Symptom:** "DS" initials displayed instead of profile photo
**Solution:**
1. Verify `photo` path in `config/author-config.json`
2. Ensure photo file exists in `renderer/src/assets/`
3. Check console for warnings

### Config not loading

**Symptom:** Warning "Failed to load author config"
**Solution:**
1. Verify JSON syntax in `config/author-config.json`
2. Check file permissions
3. Default values will be used as fallback

---

## Performance Notes

| Metric | Value |
|--------|-------|
| **DataSlide render time** | +2-3 seconds (Plotly chart generation) |
| **Chart resolution** | 800×600px @ 4x scale (3200×2400px, ~300 DPI) |
| **Config load time** | <10ms (cached after first load) |
| **StatSlide render time** | Unchanged (~1 second) |

---

## Future Enhancements

- [ ] Support for custom Plotly templates (beyond bar/forest/line/survival)
- [ ] Animated data visualizations (GIF export)
- [ ] Multiple author profiles in single carousel (co-authored content)
- [ ] Photo URL fetching from remote sources
- [ ] Account-specific color themes

---

## API Reference

### PuppeteerRenderer

```python
class PuppeteerRenderer:
    def __init__(
        self,
        renderer_dir: Optional[str] = None,
        dimensions: str = "portrait",  # "square" or "portrait"
        account: int = 1               # 1 or 2
    )

    def create_data_slide(
        self,
        slide_number: int,
        total_slides: int,
        title: str,
        chart_data: Dict[str, Any],
        chart_type: str = "bar",       # "bar", "forest", "line", "survival"
        caption: Optional[str] = None,
        source: Optional[str] = None,
        icon: Optional[str] = None,
        output_dir: Optional[str] = None
    ) -> Dict[str, Any]

    def create_cta_slide(
        self,
        slide_number: int,
        total_slides: int,
        value_proposition: Optional[str] = None,
        name: Optional[str] = None,
        credentials: Optional[str] = None,
        handle: Optional[str] = None,
        secondary_text: Optional[str] = None,
        follower_count: Optional[str] = None
    ) -> Dict[str, Any]
```

---

*Part of Carousel Generator V2 - Production-ready Instagram carousel system with publication-grade visuals*
