# Batch Mode Guide

**Production-scale carousel generation with reliability and performance tracking.**

---

## Overview

Batch mode allows you to generate multiple carousels in a single run, with:
- Sequential processing with progress tracking
- Automatic retry on failure (3 attempts)
- Output validation (file size, dimensions)
- Performance metrics and reporting
- Error recovery (continues even if one carousel fails)

---

## Quick Start

```bash
# Basic batch generation
python -m scripts.carousel_generator examples/batch-example.json --batch

# With verification
python -m scripts.carousel_generator batch.json --batch --verify

# With quality reports
python -m scripts.carousel_generator batch.json --batch --quality-report
```

---

## Batch JSON Format

### Minimal Format

```json
{
  "carousels": [
    {
      "topic": "Statin side effects"
    },
    {
      "topic": "Heart healthy diet"
    }
  ]
}
```

### Full Format with Options

```json
{
  "description": "Weekly cardiology content batch",
  "carousels": [
    {
      "topic": "GLP-1 for weight loss",
      "template": "tips_5",
      "account": 1,
      "ratio": "4:5",
      "both_ratios": true,
      "use_ai": false,
      "check_quality": true
    },
    {
      "topic": "Statin myths debunked",
      "template": "myth_busting",
      "account": 1,
      "ratio": "4:5"
    },
    {
      "topic": "SGLT2 inhibitor benefits",
      "template": "data_driven",
      "account": 2,
      "both_ratios": false
    }
  ]
}
```

### Config Options Per Carousel

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `topic` | string | *required* | Carousel topic |
| `template` | string | `tips_5` | Template preset (tips_5, myth_busting, etc.) |
| `account` | int | `1` | Account number (1 or 2) |
| `ratio` | string | `4:5` | Aspect ratio (4:5 or 1:1) |
| `both_ratios` | bool | `false` | Generate both 4:5 and 1:1 outputs |
| `use_ai` | bool | `true` | Use AI content structuring |
| `check_quality` | bool | `true` | Run quality checks |

---

## Output Structure

```
batch-20260101-143022/
├── carousel-01/          # First carousel
│   ├── slide_01_4x5.png
│   ├── slide_01_1x1.png  # If both_ratios=true
│   ├── slide_02_4x5.png
│   ├── slide_02_1x1.png
│   └── metadata.json
│
├── carousel-02/          # Second carousel
│   ├── slide_01_4x5.png
│   ├── slide_02_4x5.png
│   └── metadata.json
│
├── carousel-03/          # Third carousel
│   └── ...
│
└── batch-report.json     # Summary report
```

---

## Batch Report

The `batch-report.json` file contains a summary of the entire batch run:

```json
{
  "timestamp": "20260101-143022",
  "batch_file": "/path/to/batch.json",
  "total_carousels": 5,
  "successful": 4,
  "failed": 1,
  "total_time_seconds": 234.5,
  "results": [
    {
      "index": 1,
      "topic": "GLP-1 for weight loss",
      "slides": 8,
      "output": "carousel-01/",
      "time_ms": 45230
    },
    {
      "index": 2,
      "topic": "Statin myths",
      "slides": 6,
      "output": "carousel-02/",
      "time_ms": 38450
    }
  ],
  "failures": [
    {
      "index": 3,
      "topic": "Failed carousel",
      "reason": "Puppeteer timeout"
    }
  ]
}
```

---

## Reliability Features

### 1. Retry Logic

If a slide fails to render, the system automatically retries up to 3 times:

```
Attempt 1: Immediate render
  ↓ (fail)
Attempt 2: Wait 1s, retry
  ↓ (fail)
Attempt 3: Wait 2s, retry
  ↓ (fail)
ERROR: Failed after 3 attempts
```

Exponential backoff prevents overwhelming the system.

### 2. Output Validation

When `--verify` flag is used, each output is validated:

- **File exists**: Checks PNG was actually created
- **File size**: 10KB < size < 5MB (catches corrupted or empty files)
- **Dimensions**: Validates 1080×1080 (1:1) or 1080×1350 (4:5)
- **Image format**: Uses PIL to verify valid PNG structure

### 3. Error Recovery

If one carousel fails, the batch continues:

```
[1/5] GLP-1 for weight loss
✅ Complete (45230ms)

[2/5] Statin myths
✅ Complete (38450ms)

[3/5] SGLT2 inhibitors
❌ Failed: Puppeteer timeout

[4/5] Blood pressure tips
✅ Complete (42100ms)

[5/5] CAC scoring
✅ Complete (39800ms)

BATCH SUMMARY
Total: 5 | Successful: 4 | Failed: 1
```

### 4. Performance Tracking

Each slide render is timed:

```
📊 Performance:
   Total: 234.5s
   Average: 4.2s per slide
   Fastest: 2.8s
   Slowest: 6.1s
```

---

## Performance Characteristics

Based on benchmarking with React + Puppeteer renderer:

| Metric | Value | Notes |
|--------|-------|-------|
| **Vite Startup** | 2-3s | One-time per batch |
| **Slide Render** | 2-4s | Varies by complexity |
| **Batch Throughput** | 30-40 slides/min | Sequential processing |
| **Memory Usage** | ~300MB | Puppeteer browser instance |
| **Retry Overhead** | <5% | Retries rarely triggered |

### Optimization Tips

1. **Batch Similar Templates Together**: Same template type renders faster
2. **Disable AI for Curated Content**: Use `use_ai: false` if topic is in database
3. **Skip Quality Checks for Speed**: Use `check_quality: false` for drafts
4. **Use Single Ratio**: Dual ratio doubles render time

### Expected Timings

**Small Batch (3 carousels, 24 slides total)**
- Total: ~2 minutes
- Per carousel: ~40s

**Medium Batch (10 carousels, 80 slides total)**
- Total: ~6-8 minutes
- Per carousel: ~45s

**Large Batch (50 carousels, 400 slides total)**
- Total: ~35-40 minutes
- Per carousel: ~48s

---

## Example Workflows

### Weekly Content Batch

```json
{
  "description": "Week of January 6, 2026",
  "carousels": [
    {
      "topic": "Monday: Statin myths",
      "template": "myth_busting",
      "both_ratios": true
    },
    {
      "topic": "Wednesday: GLP-1 benefits",
      "template": "tips_5"
    },
    {
      "topic": "Friday: Blood pressure tips",
      "template": "tips_5"
    }
  ]
}
```

### Client Deliverables

```json
{
  "description": "Client XYZ - Q1 2026",
  "carousels": [
    {
      "topic": "Product launch carousel",
      "template": "tips_5",
      "account": 2,
      "both_ratios": true,
      "check_quality": true
    },
    {
      "topic": "Testimonial carousel",
      "template": "patient_story",
      "account": 2
    }
  ]
}
```

### Content Testing

```json
{
  "description": "A/B test variations",
  "carousels": [
    {
      "topic": "Statin myths - short version",
      "template": "myth_busting"
    },
    {
      "topic": "Statin myths - data-driven version",
      "template": "data_driven"
    },
    {
      "topic": "Statin myths - story version",
      "template": "patient_story"
    }
  ]
}
```

---

## Error Handling

### Common Errors and Solutions

**"Vite dev server startup timeout"**
- **Cause**: Node/npm not available or port conflict
- **Solution**: Check npm installed, try different port

**"Slide container not found"**
- **Cause**: React component failed to render
- **Solution**: Check slide data format, review console logs

**"Output file too small"**
- **Cause**: Screenshot captured blank page
- **Solution**: Increase render delay, check CSS rendering

**"Verification failed: Unexpected dimensions"**
- **Cause**: Viewport not set correctly
- **Solution**: Check `--width` and `--height` flags match ratio

### Debug Mode

```bash
# Enable verbose output
DEBUG=* python -m scripts.carousel_generator batch.json --batch

# Check individual carousel before batching
python -m scripts.carousel_generator "Test topic" --verify
```

---

## Best Practices

1. **Start Small**: Test with 2-3 carousels before large batches
2. **Use Verification**: Always use `--verify` for production batches
3. **Monitor First Run**: Watch the first carousel render to catch issues early
4. **Check Batch Report**: Review `batch-report.json` for timing anomalies
5. **Separate Accounts**: Batch by account if using different branding
6. **Version Control**: Keep batch JSON files in git for reproducibility

---

## Troubleshooting

### Batch Runs Slowly

- Check if AI is enabled unnecessarily (`use_ai: false` for known topics)
- Disable quality checks for drafts (`check_quality: false`)
- Use single ratio instead of both

### Some Carousels Fail

- Check `batch-report.json` for error messages
- Re-run just the failed carousel to debug
- Look for pattern (same template, same account, etc.)

### Memory Issues

- Reduce batch size (split into multiple smaller batches)
- Close other applications
- Check system resources (Puppeteer is memory-intensive)

---

## Next Steps

- See `PERFORMANCE.md` for detailed benchmarking
- See `SKILL.md` for full CLI reference
- See `examples/` for more batch JSON templates
