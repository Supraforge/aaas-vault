# toZonedTime

Convert a UTC ISO string, Date, Instant, or ZonedDateTime to a `ZonedDateTime` in the specified timezone.

## Signature

```ts
function toZonedTime(
  input: string | Date | Temporal.Instant | Temporal.ZonedDateTime,
  timezone: Timezone
): Temporal.ZonedDateTime

type Timezone = 'UTC' | string;
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `string \| Date \| Temporal.Instant \| Temporal.ZonedDateTime` | A UTC ISO 8601 string, Date object, Temporal.Instant, or Temporal.ZonedDateTime |
| `timezone` | `Timezone` | IANA timezone identifier (e.g., "America/New_York", "Europe/London") or "UTC" |

## Returns

A `Temporal.ZonedDateTime` in the specified timezone.

## Examples

### Server-side: Convert to UTC

```ts
import { toZonedTime } from '@gobrand/tiempo';

const utcTime = toZonedTime("2025-01-20T20:00:00Z", "UTC");
```

### Server-side: Convert to user's timezone

```ts
import { toZonedTime } from '@gobrand/tiempo';

// Get timezone from user preferences (stored in DB)
const userTime = toZonedTime("2025-01-20T20:00:00Z", user.timezone);
```

### Client-side: Convert to browser's timezone

```ts
import { toZonedTime, browserTimezone } from '@gobrand/tiempo';

const localTime = toZonedTime("2025-01-20T20:00:00Z", browserTimezone());
```

### From Date (e.g., from Drizzle ORM)

```ts
const date = new Date("2025-01-20T20:00:00.000Z");
const zoned = toZonedTime(date, "America/New_York");
```

### From Instant

```ts
const instant = Temporal.Instant.from("2025-01-20T20:00:00Z");
const zoned = toZonedTime(instant, "Asia/Tokyo");
```

### From ZonedDateTime (convert to different timezone)

```ts
const nyTime = Temporal.ZonedDateTime.from("2025-01-20T15:00:00-05:00[America/New_York]");
const tokyoTime = toZonedTime(nyTime, "Asia/Tokyo");
```

## Common Patterns

### ORM Integration

```ts
import { toZonedTime } from '@gobrand/tiempo';

// Reading: Convert database Date to user's timezone
const post = await db.query.posts.findFirst();
const localTime = toZonedTime(post.createdAt, userTimezone);
```
