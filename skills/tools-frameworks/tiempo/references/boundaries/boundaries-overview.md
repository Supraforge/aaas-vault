# Boundary Functions Overview

Get the start or end of a time period (day, week, month, year).

## Functions

| Function | Returns |
|----------|---------|
| `startOfDay(input)` | 00:00:00.000000000 |
| `endOfDay(input)` | 23:59:59.999999999 |
| `startOfWeek(input)` | Sunday 00:00:00 |
| `endOfWeek(input)` | Saturday 23:59:59 |
| `startOfMonth(input)` | 1st day 00:00:00 |
| `endOfMonth(input)` | Last day 23:59:59 |
| `startOfYear(input)` | Jan 1 00:00:00 |
| `endOfYear(input)` | Dec 31 23:59:59 |

## Common Signature

```ts
function startOfX(
  input: Temporal.Instant | Temporal.ZonedDateTime
): Temporal.ZonedDateTime
```

## Examples

### Start/End of Day

```ts
import { startOfDay, endOfDay } from '@gobrand/tiempo';

const now = Temporal.Now.zonedDateTimeISO('America/New_York');
const dayStart = startOfDay(now);  // 00:00:00.000000000
const dayEnd = endOfDay(now);      // 23:59:59.999999999
```

### Start/End of Month

```ts
import { startOfMonth, endOfMonth } from '@gobrand/tiempo';

const monthStart = startOfMonth(now);  // First day at 00:00:00
const monthEnd = endOfMonth(now);      // Last day at 23:59:59
```

### Date Range Queries

```ts
import { startOfDay, endOfDay, toIso9075 } from '@gobrand/tiempo';

const dayStart = startOfDay(now);
const dayEnd = endOfDay(now);

// SQL query
const sql = `
  SELECT * FROM events
  WHERE created_at >= '${toIso9075(dayStart)}'
    AND created_at <= '${toIso9075(dayEnd)}'
`;
```

## Timezone Behavior

- **Instant input**: Uses UTC timezone
- **ZonedDateTime input**: Uses the input's timezone

```ts
// From Instant (always UTC)
const instant = Temporal.Instant.from('2025-01-20T12:00:00Z');
startOfDay(instant);
// 2025-01-20T00:00:00Z[UTC]

// From ZonedDateTime (uses its timezone)
const zoned = Temporal.ZonedDateTime.from('2025-01-20T15:30:00-05:00[America/New_York]');
startOfDay(zoned);
// 2025-01-20T00:00:00-05:00[America/New_York]
```
