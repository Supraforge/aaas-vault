# Content OS Output Template

When Content OS runs, it creates this structure:

```
/output/content-os/[topic-slug]/
│
├── research/
│   └── research-brief.md         # Foundation for all content
│
├── long-form/                     # Full quality pipeline
│   ├── youtube-script.md         # Hinglish script
│   ├── newsletter-b2c.md         # Patient newsletter
│   ├── newsletter-b2b.md         # Doctor newsletter
│   ├── editorial.md              # Eric Topol style
│   └── blog.md                   # SEO optimized
│
├── short-form/                    # Quick accuracy pass
│   ├── tweets.md                 # 5-10 tweets
│   ├── thread.md                 # Twitter thread
│   ├── snippets.md               # Quotable sections
│   └── carousel-content.md       # Input for carousel
│
├── visual/
│   ├── carousel/                 # Generated PNG slides
│   │   ├── slide-01.png
│   │   ├── slide-02.png
│   │   └── ...
│   └── infographic-concepts.md   # Infographic ideas
│
└── summary.md                     # What was produced
```

## File Headers

Each content file includes metadata:

```markdown
---
topic: [Original topic]
content_type: [youtube-script|newsletter-b2c|newsletter-b2b|editorial|blog|tweets|thread]
quality_status: [passed|pending]
accuracy_status: [checked|pending]
generated_at: [timestamp]
---
```

## Quality Markers

Long-form files include quality pipeline results:

```markdown
---
quality_pipeline:
  scientific_critical_thinking: PASS
  peer_review: PASS
  content_reflection: PASS
  authentic_voice: PASS
---
```

Short-form files include accuracy check:

```markdown
---
accuracy_check:
  status: PASS
  claims_verified: 5
  corrections_made: 0
---
```
