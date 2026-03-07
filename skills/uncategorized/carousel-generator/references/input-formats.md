# Input Formats for Content-OS Generators

## Overview

All content-os generators accept multiple input formats for flexibility. The generators auto-detect the format based on content structure.

## Format 1: Markdown with Separators (Recommended)

Best for quick content creation. Use `#` for title slide, `##` for content slides, `---` for explicit slide breaks.

```markdown
# Main Title
Optional subtitle text

---

## Slide 2 Title
Body text for this slide.

• Bullet point 1
• Bullet point 2
• Bullet point 3

---

## Slide 3 Title
- Also supports dash bullets
- Like this

---

## Final Slide
Call to action or summary here.
```

### Rules:
- `# Title` = Title slide (teal background)
- `## Title` = Content slide title
- `---` = Explicit slide separator
- `•` or `-` or `*` = Bullet points
- Blank lines are preserved as spacing

## Format 2: JSON Array

Best for programmatic generation or complex layouts.

```json
[
  {
    "title": "Main Title",
    "body": "Subtitle text",
    "type": "title"
  },
  {
    "title": "Content Slide",
    "body": "Body text here.\n• Bullet 1\n• Bullet 2",
    "type": "content"
  },
  {
    "title": "Another Slide",
    "body": "More content",
    "type": "content"
  }
]
```

### Fields:
- `title` (required): Slide title text
- `body` (optional): Body content, use `\n` for line breaks
- `type` (optional): `"title"` or `"content"`, defaults to `"content"`

## Format 3: JSON Object with Slides Array

Alternative JSON structure with metadata wrapper.

```json
{
  "slides": [
    {"title": "Title", "body": "Subtitle", "type": "title"},
    {"title": "Slide 2", "body": "Content", "type": "content"}
  ],
  "metadata": {
    "topic": "Hypertension",
    "created": "2024-12-29"
  }
}
```

## Format 4: Plain Text (Fallback)

If no structure is detected, content becomes a single slide.

```
This is just plain text.
It will all appear on one slide.
```

## Best Practices

### For Educational Content
```markdown
# 5 Signs of Heart Attack
Know these warning signs

---

## 1. Chest Discomfort
• Pressure or squeezing feeling
• Center of chest
• Lasts more than few minutes

---

## 2. Shortness of Breath
• May occur with or without chest pain
• Often the first symptom in women

---

## Take Action
Call emergency services immediately if you experience these symptoms.
```

### For Data-Heavy Content
```markdown
# Statin Benefits
What the research shows

---

## JUPITER Trial Results
• 44% reduction in heart attacks
• 48% reduction in strokes
• NNT = 95 over 2 years

---

## Who Benefits Most?
• High-risk patients
• Those with elevated CRP
• Family history of early CVD
```

### For Myth-Busting
```markdown
# Cholesterol Myths Debunked
What you've been told vs. the truth

---

## Myth: Eggs are bad for your heart
TRUTH: For most people, dietary cholesterol has minimal impact on blood cholesterol. 1-3 eggs daily is fine for healthy adults.

---

## Myth: All fats are bad
TRUTH: Unsaturated fats (olive oil, nuts, fish) are heart-protective. It's trans fats you should avoid.
```

## Character Limits

| Element | Recommended | Maximum |
|---------|-------------|---------|
| Title | 40 chars | 80 chars |
| Body per slide | 200 chars | 400 chars |
| Bullet points | 3-5 per slide | 7 max |
| Total slides | 8 | 10 |

## Tips

1. **Keep it scannable**: Use bullets over paragraphs
2. **One idea per slide**: Don't overcrowd
3. **Strong title slide**: Hook the viewer immediately
4. **End with CTA**: Follow, share, or learn more
5. **Use data**: Specific numbers are more compelling
