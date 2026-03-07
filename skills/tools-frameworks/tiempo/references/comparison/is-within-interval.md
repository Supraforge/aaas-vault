# isWithinInterval

Returns true if the given datetime is within the interval (inclusive of start and end). Compares by the underlying instant (epoch time), not by calendar date/time.

## Signature

```ts
function isWithinInterval(
  date: Temporal.Instant | Temporal.ZonedDateTime,
  interval: {
    start: Temporal.Instant | Temporal.ZonedDateTime;
    end: Temporal.Instant | Temporal.ZonedDateTime;
  }
): boolean
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `date` | `Temporal.Instant \| Temporal.ZonedDateTime` | The datetime to check |
| `interval` | `{ start, end }` | The interval with start and end datetimes |

## Returns

`true` if `date` is within the interval (inclusive), `false` otherwise.

## Examples

### Basic usage

```ts
import { isWithinInterval } from '@gobrand/tiempo';

const start = Temporal.ZonedDateTime.from('2025-01-01T00:00:00Z[UTC]');
const end = Temporal.ZonedDateTime.from('2025-01-07T00:00:00Z[UTC]');
const date = Temporal.ZonedDateTime.from('2025-01-03T00:00:00Z[UTC]');

isWithinInterval(date, { start, end }); // true
```

### Date outside the interval

```ts
const start = Temporal.ZonedDateTime.from('2025-01-01T00:00:00Z[UTC]');
const end = Temporal.ZonedDateTime.from('2025-01-07T00:00:00Z[UTC]');
const date = Temporal.ZonedDateTime.from('2025-01-10T00:00:00Z[UTC]');

isWithinInterval(date, { start, end }); // false
```

### Inclusive boundaries

```ts
const start = Temporal.ZonedDateTime.from('2025-01-01T00:00:00Z[UTC]');
const end = Temporal.ZonedDateTime.from('2025-01-07T00:00:00Z[UTC]');

// Date equal to interval start (inclusive)
isWithinInterval(start, { start, end }); // true

// Date equal to interval end (inclusive)
isWithinInterval(end, { start, end }); // true
```

### With Instant

```ts
const start = Temporal.Instant.from('2025-01-01T00:00:00Z');
const end = Temporal.Instant.from('2025-01-07T00:00:00Z');
const date = Temporal.Instant.from('2025-01-03T00:00:00Z');

isWithinInterval(date, { start, end }); // true
```

### Different timezones - compares by instant

```ts
const start = Temporal.ZonedDateTime.from('2025-01-01T00:00:00-05:00[America/New_York]');
const end = Temporal.ZonedDateTime.from('2025-01-07T00:00:00+09:00[Asia/Tokyo]');
const date = Temporal.ZonedDateTime.from('2025-01-03T12:00:00Z[UTC]');

isWithinInterval(date, { start, end }); // true
```

## Common Patterns

### Validate booking availability

```ts
import { isWithinInterval } from '@gobrand/tiempo';

function isSlotAvailable(
  slot: Temporal.ZonedDateTime,
  availableFrom: Temporal.ZonedDateTime,
  availableUntil: Temporal.ZonedDateTime
) {
  return isWithinInterval(slot, { start: availableFrom, end: availableUntil });
}
```

### Check if event is currently active

```ts
import { isWithinInterval, now } from '@gobrand/tiempo';

function isEventActive(
  eventStart: Temporal.ZonedDateTime,
  eventEnd: Temporal.ZonedDateTime,
  timezone: string
) {
  const currentTime = now(timezone);
  return isWithinInterval(currentTime, { start: eventStart, end: eventEnd });
}
```
