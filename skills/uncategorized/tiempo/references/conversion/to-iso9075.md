# toIso9075

Convert a `Temporal.Instant` or `ZonedDateTime` to an ISO 9075 (SQL) formatted string.

This format uses a space separator instead of 'T' and omits the timezone indicator, making it compatible with SQL databases.

## Signature

```ts
function toIso9075(
  input: Temporal.Instant,
  options?: { representation?: 'complete' | 'date' | 'time' }
): string

function toIso9075(
  input: Temporal.ZonedDateTime,
  options?: ToIso9075Options
): string

interface ToIso9075Options {
  mode?: 'utc' | 'local';
  representation?: 'complete' | 'date' | 'time';
}
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `Temporal.Instant \| Temporal.ZonedDateTime` | A Temporal.Instant or Temporal.ZonedDateTime |
| `options.mode` | `'utc' \| 'local'` | `'utc'` (default) converts to UTC before formatting, `'local'` uses the local time of the ZonedDateTime |
| `options.representation` | `'complete' \| 'date' \| 'time'` | `'complete'` (default) includes date and time |

## Returns

An ISO 9075 formatted string (e.g., `"2019-09-18 19:00:52"`).

Sub-second precision is dropped for SQL DATETIME compatibility.

## Examples

### Default (UTC mode)

```ts
import { toIso9075 } from '@gobrand/tiempo';

// 7pm New York (EDT, UTC-4) = 11pm UTC
const zoned = Temporal.ZonedDateTime.from("2019-09-18T19:00:52-04:00[America/New_York]");

toIso9075(zoned);
// => "2019-09-18 23:00:52"
```

### Local Mode

```ts
const zoned = Temporal.ZonedDateTime.from("2025-01-20T15:00:00-05:00[America/New_York]");

toIso9075(zoned, { mode: 'local' });
// => "2025-01-20 15:00:00"

toIso9075(zoned, { mode: 'utc' });
// => "2025-01-20 20:00:00"
```

### Date Only

```ts
toIso9075(zoned, { representation: 'date' });
// => "2025-01-20"
```

### Time Only

```ts
toIso9075(zoned, { representation: 'time' });
// => "20:00:00" (UTC)

toIso9075(zoned, { mode: 'local', representation: 'time' });
// => "15:00:00" (local)
```

### From Instant

Instants are always formatted in UTC (no `mode` option):

```ts
const instant = Temporal.Instant.from("2025-01-20T20:00:00Z");

toIso9075(instant);
// => "2025-01-20 20:00:00"

toIso9075(instant, { representation: 'date' });
// => "2025-01-20"
```

## Common Patterns

### SQL INSERT (UTC for storage)

```ts
import { toIso9075 } from '@gobrand/tiempo';

// Store in UTC for consistency
const sqlValue = toIso9075(eventTime);

await db.execute(`INSERT INTO events (created_at) VALUES ('${sqlValue}')`);
```

### SQL INSERT (Local time for display)

```ts
import { toIso9075, toZonedTime } from '@gobrand/tiempo';

// Convert to user's timezone, then format as local time
const userTime = toZonedTime(eventTime, userTimezone);
const sqlValue = toIso9075(userTime, { mode: 'local' });

await db.execute(`INSERT INTO events (display_time) VALUES ('${sqlValue}')`);
```

### Date-only Column

```ts
const dateOnly = toIso9075(zoned, { representation: 'date' });
// => "2025-01-20"
```
