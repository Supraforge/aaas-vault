# startOfDay

Returns a `ZonedDateTime` at the first moment of the day (midnight, 00:00:00.000000000).

## Signature

```ts
function startOfDay(
  input: Temporal.Instant | Temporal.ZonedDateTime
): Temporal.ZonedDateTime
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `Temporal.Instant \| Temporal.ZonedDateTime` | The datetime to get the start of day for |

## Returns

A `Temporal.ZonedDateTime` at midnight of the same day.

## Examples

### From Instant (always UTC)

```ts
import { startOfDay } from '@gobrand/tiempo';

const instant = Temporal.Instant.from('2025-01-20T12:00:00Z');
startOfDay(instant);
// 2025-01-20T00:00:00Z[UTC]
```

### From ZonedDateTime (uses its timezone)

```ts
const zoned = Temporal.ZonedDateTime.from('2025-01-20T15:30:00-05:00[America/New_York]');
startOfDay(zoned);
// 2025-01-20T00:00:00-05:00[America/New_York]
```

### Need a different timezone? Convert first

```ts
const instant = Temporal.Instant.from('2025-01-20T12:00:00Z');
const nyTime = instant.toZonedDateTimeISO('America/New_York');
startOfDay(nyTime);
// 2025-01-20T00:00:00-05:00[America/New_York]
```

## Common Patterns

### Date range for current day

```ts
import { startOfDay, endOfDay } from '@gobrand/tiempo';

const now = Temporal.Now.zonedDateTimeISO('America/New_York');
const dayStart = startOfDay(now);
const dayEnd = endOfDay(now);

// Use for database queries
// WHERE created_at >= dayStart AND created_at <= dayEnd
```
