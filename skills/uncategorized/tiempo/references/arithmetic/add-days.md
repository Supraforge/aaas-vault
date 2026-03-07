# addDays

Add days to a datetime. DST-safe—adds calendar days, not 24-hour periods.

## Signature

```ts
function addDays(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  days: number
): Temporal.ZonedDateTime
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `Temporal.Instant \| Temporal.ZonedDateTime` | The datetime to add days to |
| `days` | `number` | Number of days to add (can be negative) |

## Returns

A `Temporal.ZonedDateTime` with the days added.

## Examples

### Basic usage

```ts
import { addDays } from '@gobrand/tiempo';

const instant = Temporal.Instant.from('2025-01-20T12:00:00Z');
addDays(instant, 5);
// 2025-01-25T12:00:00Z[UTC]
```

### Preserves timezone

```ts
const zoned = Temporal.ZonedDateTime.from('2025-01-20T15:30:00-05:00[America/New_York]');
addDays(zoned, 10);
// 2025-01-30T15:30:00-05:00[America/New_York]
```

### Negative values subtract

```ts
addDays(instant, -7);
// 2025-01-13T12:00:00Z[UTC]
```

## DST Handling

`addDays` properly handles Daylight Saving Time transitions:

```ts
import { addDays, addHours } from '@gobrand/tiempo';

// DST transition in US (March 9, 2025 at 2:00 AM)
const beforeDst = Temporal.ZonedDateTime.from('2025-03-08T12:00:00-05:00[America/New_York]');

// Adding 1 day = calendar day (still 12:00 PM)
const nextDay = addDays(beforeDst, 1);
// 2025-03-09T12:00:00-04:00[America/New_York]

// Compare with addHours: Adding 24 hours = 24 hours of elapsed time
const plus24h = addHours(beforeDst, 24);
// 2025-03-09T13:00:00-04:00[America/New_York]
// (One hour later because DST "lost" an hour)
```
