---
name: laravelperformance-select-columns
description: >-
  Select only required columns to reduce memory and transfer costs; apply to
  base queries and relations
version: 1.0.0
compatibility: 'agent-zero, claude-code, cursor'
---

# Select Only Needed Columns

Reduce payloads by selecting exact fields:

```php
User::select(['id', 'name'])->paginate();

Post::with(['author:id,name'])->select(['id','author_id','title'])->get();
```

- Avoid `*`; keep DTOs/resources aligned with selected fields
- Combine with eager loading to avoid N+1

