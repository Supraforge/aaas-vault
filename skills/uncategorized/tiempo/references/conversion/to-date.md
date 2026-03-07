# toDate

Convert a `Temporal.Instant` or `ZonedDateTime` to a JavaScript `Date` object.

## Signature

```ts
function toDate(
  input: Temporal.Instant | Temporal.ZonedDateTime
): Date
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `Temporal.Instant \| Temporal.ZonedDateTime` | A Temporal.Instant or Temporal.ZonedDateTime |

## Returns

A JavaScript `Date` object representing the same moment in time.

## Examples

### From Instant

```ts
import { toDate } from '@gobrand/tiempo';

const instant = Temporal.Instant.from("2025-01-20T20:00:00Z");
const date = toDate(instant);
// date.toISOString() === "2025-01-20T20:00:00.000Z"
```

### From ZonedDateTime

```ts
const zoned = Temporal.ZonedDateTime.from("2025-01-20T15:00:00-05:00[America/New_York]");
const date = toDate(zoned);
// date.toISOString() === "2025-01-20T20:00:00.000Z"
```

## Common Patterns

### ORM Integration (Drizzle, Prisma, etc.)

```ts
import { toDate } from '@gobrand/tiempo';

// Writing: Convert back to Date for storage
const instant = Temporal.Instant.from("2025-01-20T20:00:00Z");
const date = toDate(instant);
await db.update(posts).set({ publishedAt: date });
```
