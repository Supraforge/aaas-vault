# Link Analyzer - Reference Guide

## Link Classification

### Internal Links
Links pointing to the same domain or configured internal domains.

**Detection:**
```python
def is_internal(href: str, internal_domains: list[str]) -> bool:
    if href.startswith('/'):
        return True
    for domain in internal_domains:
        if domain in href:
            return True
    return False
```

### External Links
Links pointing outside the site.

**Categories:**
| Category | Detection Pattern |
|----------|------------------|
| Social Media | twitter.com, facebook.com, linkedin.com, instagram.com, youtube.com |
| E-commerce | amazon.com, gumroad.com, shopify.com |
| Email | mailto: prefix |
| Phone | tel: prefix |
| App Stores | apps.apple.com, play.google.com |
| GitHub | github.com |
| External Website | All other http/https links |

## Link Graph Metrics

### Inbound Links (Backlinks)
Number of internal pages linking TO this page.

```python
def count_inbound(page: str, link_graph: dict) -> int:
    count = 0
    for source, targets in link_graph.items():
        if page in targets:
            count += 1
    return count
```

### Outbound Links
Number of internal links FROM this page to other internal pages.

```python
def count_outbound(page: str, link_graph: dict) -> int:
    return len(link_graph.get(page, []))
```

### Link Flow Ratio
```python
def link_flow_ratio(inbound: int, outbound: int) -> float:
    if outbound == 0:
        return float('inf') if inbound > 0 else 0
    return inbound / outbound
```

**Interpretation:**
- Ratio > 2.0: Page receives more than it gives (potential authority page)
- Ratio 0.5-2.0: Balanced link flow (healthy)
- Ratio < 0.5: Page gives more than it receives (could be over-linking)
- Ratio = inf: Link sink (receives but doesn't give)

## Page Categories

### Orphan Pages
**Definition:** Pages with zero inbound internal links.

**SEO Impact:** Critical
- Search engines may not discover/index these pages
- Pages have no internal authority signals
- Often indicates forgotten or draft content

**Common Causes:**
- Removed from navigation but still published
- New pages not yet linked
- Content moved without redirects

**Recommendations:**
1. Add to relevant hub/pillar pages
2. Include in related posts sections
3. Add to navigation if important
4. Consider removing if obsolete

### Under-linked Pages
**Definition:** Pages with fewer than N inbound links (default: 3).

**SEO Impact:** High
- Reduced crawl priority
- Lower perceived importance
- Missed ranking opportunities

**Recommendations:**
1. Identify topically related pages
2. Add contextual links from high-authority pages
3. Create hub pages that link to multiple related content
4. Use "related posts" functionality

### Over-linked Pages
**Definition:** Pages with more than N outbound links (default: 50).

**SEO Impact:** Medium
- Each link passes less equity (dilution)
- Can appear spammy to search engines
- User experience degradation

**Common Causes:**
- Resource/links pages
- Archives with many posts
- Footers with excessive links

**Recommendations:**
1. Prioritize most important links
2. Use nofollow for less important links
3. Consider pagination or categorization
4. Review link relevance

### Link Sinks
**Definition:** Pages with high inbound but very low outbound (< N, default: 2).

**SEO Impact:** Medium
- Don't distribute link equity to other pages
- Create "dead ends" in site structure
- Waste internal linking potential

**Common Examples:**
- About/Contact pages
- Landing pages
- Heavily linked cornerstone content

**Recommendations:**
1. Add relevant internal links
2. Include "related content" sections
3. Link to deeper content from high-authority pages
4. Balance receiving and distributing equity

## HTTP Status Codes

### Success Codes
| Code | Meaning | Action |
|------|---------|--------|
| 200 | OK | Link working |
| 301 | Permanent Redirect | Consider updating to final URL |
| 302 | Temporary Redirect | Usually OK |

### Error Codes
| Code | Meaning | Action |
|------|---------|--------|
| 400 | Bad Request | Check URL format |
| 401 | Unauthorized | May be paywalled content |
| 403 | Forbidden | Often bot blocking |
| 404 | Not Found | Remove or replace link |
| 410 | Gone | Content permanently removed |
| 429 | Too Many Requests | Rate limiting |
| 500 | Server Error | Temporary - recheck |
| 502 | Bad Gateway | Temporary - recheck |
| 503 | Service Unavailable | Temporary - recheck |

### Special Cases
| Status | Meaning | Action |
|--------|---------|--------|
| 520 | Cloudflare Unknown | Twitter rate limiting |
| 999 | Custom | LinkedIn bot blocking |
| Timeout | No response | May be dead or blocking |
| SSL Error | Certificate issue | Security concern |
| Connection Error | Domain unreachable | Likely dead domain |

## False Positive Filtering

### Known Bot Blockers
Sites that block automated link checkers:
- linkedin.com (returns 999)
- twitter.com/x.com (returns 520)
- stackoverflow.com (returns 403)
- facebook.com (returns 403)
- instagram.com (returns various)

### Image Attribution Sites
Often block bot access:
- pixabay.com
- unsplash.com
- pexels.com

### Recommendation
Mark these as "unchecked" rather than "broken" and periodically verify manually.

## Report Formats

### JSON Data Format
```json
{
  "metadata": {
    "analyzed_at": "2025-01-15T10:30:00Z",
    "pages_analyzed": 1500,
    "links_found": 25000
  },
  "link_graph": {
    "/page-a/": ["/page-b/", "/page-c/"],
    "/page-b/": ["/page-a/"]
  },
  "metrics": {
    "/page-a/": {
      "inbound": 5,
      "outbound": 10,
      "ratio": 0.5
    }
  },
  "orphans": ["/orphan-page/"],
  "underlinked": [
    {"page": "/underlinked/", "inbound": 2}
  ],
  "overlinked": [
    {"page": "/resources/", "outbound": 127}
  ],
  "link_sinks": [
    {"page": "/about/", "inbound": 15, "outbound": 0}
  ]
}
```

### Markdown Report Format
```markdown
# Link Analysis Report

**Generated:** 2025-01-15
**Pages Analyzed:** 1,500
**Total Links:** 25,000

## Critical Issues

### Orphan Pages (15)
These pages have no internal links pointing to them.
| Page | Recommendation |
|------|----------------|
| /old-post/ | Add links or remove |

## Optimization Opportunities

### Under-linked Pages (47)
...
```

## Performance Optimization

### Parallel HTTP Checking
```python
from concurrent.futures import ThreadPoolExecutor

def check_urls_parallel(urls: list, max_workers: int = 20):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(check_single_url, urls))
    return results
```

### Recommended Settings by Site Size
| Pages | Max Workers | Timeout | Retry |
|-------|-------------|---------|-------|
| < 100 | 20 | 5s | 2 |
| 100-1000 | 15 | 5s | 1 |
| 1000+ | 10 | 3s | 1 |

### Caching
Store HTTP check results to avoid rechecking:
- Cache successful checks for 7 days
- Cache permanent errors (404, 410) for 30 days
- Always recheck timeouts and temporary errors
