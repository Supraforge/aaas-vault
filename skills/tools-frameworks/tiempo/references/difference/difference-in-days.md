# differenceInDays

Returns the number of days between two datetimes. Uses calendar-aware calculation, which means it properly handles DST transitions where days can be 23, 24, or 25 hours long.

## Signature

```ts
function differenceInDays(
  laterDate: Temporal.Instant | Temporal.ZonedDateTime,
  earlierDate: Temporal.Instant | Temporal.ZonedDateTime
): number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `laterDate` | `Temporal.Instant \| Temporal.ZonedDateTime` | The later datetime |
| `earlierDate` | `Temporal.Instant \| Temporal.ZonedDateTime` | The earlier datetime |

## Returns

The number of days between the two datetimes.

## Examples

### Basic usage

```ts
import { differenceInDays } from '@gobrand/tiempo';

const later = Temporal.Instant.from('2025-01-25T12:00:00Z');
const earlier = Temporal.Instant.from('2025-01-20T12:00:00Z');

differenceInDays(later, earlier); // 5
```

### With ZonedDateTime

```ts
const laterZoned = Temporal.ZonedDateTime.from('2025-01-25T15:00:00-05:00[America/New_York]');
const earlierZoned = Temporal.ZonedDateTime.from('2025-01-20T15:00:00-05:00[America/New_York]');
differenceInDays(laterZoned, earlierZoned); // 5
```

### Handles DST transitions correctly

```ts
const afterDst = Temporal.ZonedDateTime.from('2025-03-10T12:00:00-04:00[America/New_York]');
const beforeDst = Temporal.ZonedDateTime.from('2025-03-08T12:00:00-05:00[America/New_York]');
differenceInDays(afterDst, beforeDst); // 2 (calendar days, not 48 hours)
```

## Common Patterns

### Time until event

```ts
import { differenceInDays, differenceInHours, differenceInMinutes } from '@gobrand/tiempo';

function timeUntil(eventDate: Temporal.ZonedDateTime): string {
  const now = Temporal.Now.zonedDateTimeISO();

  const days = differenceInDays(eventDate, now);
  if (days > 1) return `${days} days`;

  const hours = differenceInHours(eventDate, now);
  if (hours > 1) return `${hours} hours`;

  const minutes = differenceInMinutes(eventDate, now);
  return `${minutes} minutes`;
}
```
