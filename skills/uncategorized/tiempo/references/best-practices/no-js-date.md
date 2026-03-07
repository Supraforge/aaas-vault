# Don't Use JavaScript Date for Timezone Work

JavaScript Date has fundamental limitations that cause timezone bugs. Use tiempo instead.

## Problems with JavaScript Date

1. **No timezone awareness**: Date stores UTC internally but displays in local timezone
2. **Mutation**: Methods like `setHours()` mutate the object
3. **Ambiguous parsing**: `new Date("2025-03-09")` parses differently across browsers
4. **DST bugs**: Manual arithmetic ignores DST transitions

## Anti-Patterns

```ts
// ❌ Bad - Date loses timezone information
const date = new Date();
date.setHours(date.getHours() + 5);  // DST bugs lurking

// ❌ Bad - Ambiguous parsing
const date = new Date("2025-03-09");

// ❌ Bad - Implicit UTC assumption
const now = new Date().toISOString();

// ❌ Bad - Manual math ignores DST
const hours = (date2.getTime() - date1.getTime()) / (1000 * 60 * 60);
```

## Correct Patterns

```ts
import { toZonedTime, addHours, toIso, now, differenceInHours } from '@gobrand/tiempo';

// ✅ Good - explicit timezone
const zonedTime = toZonedTime(new Date(), 'America/New_York');

// ✅ Good - DST-safe arithmetic
const later = addHours(zonedTime, 5);

// ✅ Good - explicit conversion to ISO
const utcString = toIso(zonedTime);

// ✅ Good - timezone-aware current time
const currentTime = now('America/New_York');

// ✅ Good - proper difference calculation
const hours = differenceInHours(zoned2, zoned1);
```

## When Date is Acceptable

- ORM integration (Drizzle, Prisma expect Date objects)
- Legacy API compatibility
- Simple timestamp storage (convert immediately with `toZonedTime`)

```ts
// ORM reads Date, immediately convert to ZonedDateTime
const post = await db.query.posts.findFirst();
const localTime = toZonedTime(post.createdAt, userTimezone);

// Convert back to Date only for ORM writes
await db.update(posts).set({ publishedAt: toDate(zonedTime) });
```
