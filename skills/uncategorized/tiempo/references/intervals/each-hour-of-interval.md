# eachHourOfInterval

Returns an array of ZonedDateTime objects for each hour within the interval. Each element represents the start of the hour (minute/second/etc. set to 0). The interval is inclusive of both start and end hours.

Note: During DST transitions, some hours may be skipped (spring forward) or the array may contain fewer/more hours than expected based on wall-clock time.

## Signature

```ts
function eachHourOfInterval(interval: {
  start: Temporal.Instant | Temporal.ZonedDateTime;
  end: Temporal.Instant | Temporal.ZonedDateTime;
}): Temporal.ZonedDateTime[]
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `interval` | `{ start, end }` | The interval with start and end datetimes |

## Returns

Array of `Temporal.ZonedDateTime` at the start of each hour in the interval.

For `Instant` inputs, UTC is used as the timezone. For `ZonedDateTime` inputs, the timezone of the start date is preserved.

## Examples

### Basic usage

```ts
import { eachHourOfInterval } from '@gobrand/tiempo';

const start = Temporal.ZonedDateTime.from('2025-01-06T10:30:00Z[UTC]');
const end = Temporal.ZonedDateTime.from('2025-01-06T14:15:00Z[UTC]');

const hours = eachHourOfInterval({ start, end });
// [
//   2025-01-06T10:00:00Z[UTC],
//   2025-01-06T11:00:00Z[UTC],
//   2025-01-06T12:00:00Z[UTC],
//   2025-01-06T13:00:00Z[UTC],
//   2025-01-06T14:00:00Z[UTC]
// ]
```

### Cross-day boundary

```ts
const start = Temporal.ZonedDateTime.from('2025-01-06T22:00:00Z[UTC]');
const end = Temporal.ZonedDateTime.from('2025-01-07T02:00:00Z[UTC]');

const hours = eachHourOfInterval({ start, end });
// [
//   2025-01-06T22:00:00Z[UTC],
//   2025-01-06T23:00:00Z[UTC],
//   2025-01-07T00:00:00Z[UTC],
//   2025-01-07T01:00:00Z[UTC],
//   2025-01-07T02:00:00Z[UTC]
// ]
```

### With timezone

```ts
const start = Temporal.ZonedDateTime.from('2025-01-06T09:00:00-05:00[America/New_York]');
const end = Temporal.ZonedDateTime.from('2025-01-06T12:00:00-05:00[America/New_York]');

const hours = eachHourOfInterval({ start, end });
// [
//   2025-01-06T09:00:00-05:00[America/New_York],
//   2025-01-06T10:00:00-05:00[America/New_York],
//   2025-01-06T11:00:00-05:00[America/New_York],
//   2025-01-06T12:00:00-05:00[America/New_York]
// ]
```

## Common Patterns

### Generate hourly time slots

```ts
import { eachHourOfInterval, addHours, format } from '@gobrand/tiempo';

function getHourlySlots(
  dayStart: Temporal.ZonedDateTime,
  dayEnd: Temporal.ZonedDateTime
) {
  return eachHourOfInterval({ start: dayStart, end: dayEnd }).map(hour => ({
    start: hour,
    end: addHours(hour, 1),
    label: format(hour, 'h:mm a')
  }));
}
```

### Build hour picker

```ts
import { eachHourOfInterval, format } from '@gobrand/tiempo';

function getHourOptions(date: Temporal.ZonedDateTime) {
  const dayStart = date.startOfDay();
  const dayEnd = dayStart.add({ hours: 23 });

  return eachHourOfInterval({ start: dayStart, end: dayEnd }).map(hour => ({
    value: hour.hour,
    label: format(hour, 'h:mm a')
  }));
}
```
