# eachMinuteOfInterval

Returns an array of ZonedDateTime objects for each minute within the interval. Each element represents the start of the minute (seconds/etc. set to 0). The interval is inclusive of both start and end minutes.

**Warning:** Large intervals can produce very large arrays. For example, a 24-hour interval produces 1,441 elements. Consider whether this is appropriate for your use case.

## Signature

```ts
function eachMinuteOfInterval(interval: {
  start: Temporal.Instant | Temporal.ZonedDateTime;
  end: Temporal.Instant | Temporal.ZonedDateTime;
}): Temporal.ZonedDateTime[]
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `interval` | `{ start, end }` | The interval with start and end datetimes |

## Returns

Array of `Temporal.ZonedDateTime` at the start of each minute in the interval.

For `Instant` inputs, UTC is used as the timezone. For `ZonedDateTime` inputs, the timezone of the start date is preserved.

## Examples

### Basic usage

```ts
import { eachMinuteOfInterval } from '@gobrand/tiempo';

const start = Temporal.ZonedDateTime.from('2025-01-06T10:30:00Z[UTC]');
const end = Temporal.ZonedDateTime.from('2025-01-06T10:33:45Z[UTC]');

const minutes = eachMinuteOfInterval({ start, end });
// [
//   2025-01-06T10:30:00Z[UTC],
//   2025-01-06T10:31:00Z[UTC],
//   2025-01-06T10:32:00Z[UTC],
//   2025-01-06T10:33:00Z[UTC]
// ]
```

### Cross-hour boundary

```ts
const start = Temporal.ZonedDateTime.from('2025-01-06T10:58:00Z[UTC]');
const end = Temporal.ZonedDateTime.from('2025-01-06T11:02:00Z[UTC]');

const minutes = eachMinuteOfInterval({ start, end });
// [
//   2025-01-06T10:58:00Z[UTC],
//   2025-01-06T10:59:00Z[UTC],
//   2025-01-06T11:00:00Z[UTC],
//   2025-01-06T11:01:00Z[UTC],
//   2025-01-06T11:02:00Z[UTC]
// ]
```

### With timezone

```ts
const start = Temporal.ZonedDateTime.from('2025-01-06T10:00:00-05:00[America/New_York]');
const end = Temporal.ZonedDateTime.from('2025-01-06T10:05:00-05:00[America/New_York]');

const minutes = eachMinuteOfInterval({ start, end });
// [
//   2025-01-06T10:00:00-05:00[America/New_York],
//   2025-01-06T10:01:00-05:00[America/New_York],
//   2025-01-06T10:02:00-05:00[America/New_York],
//   2025-01-06T10:03:00-05:00[America/New_York],
//   2025-01-06T10:04:00-05:00[America/New_York],
//   2025-01-06T10:05:00-05:00[America/New_York]
// ]
```

## Common Patterns

### Generate minute-level time slots

```ts
import { eachMinuteOfInterval, addMinutes, format } from '@gobrand/tiempo';

function getMinuteSlots(
  start: Temporal.ZonedDateTime,
  end: Temporal.ZonedDateTime,
  stepMinutes: number = 15
) {
  return eachMinuteOfInterval({ start, end })
    .filter((_, index) => index % stepMinutes === 0)
    .map(minute => ({
      time: minute,
      label: format(minute, 'h:mm a')
    }));
}
```

### Build minute picker (15-minute intervals)

```ts
import { eachMinuteOfInterval, format } from '@gobrand/tiempo';

function getMinuteOptions(hour: Temporal.ZonedDateTime) {
  const hourStart = hour.round({ smallestUnit: 'hour', roundingMode: 'floor' });
  const hourEnd = hourStart.add({ minutes: 59 });

  return eachMinuteOfInterval({ start: hourStart, end: hourEnd })
    .filter(minute => minute.minute % 15 === 0)
    .map(minute => ({
      value: minute.minute,
      label: format(minute, 'mm')
    }));
}
```
