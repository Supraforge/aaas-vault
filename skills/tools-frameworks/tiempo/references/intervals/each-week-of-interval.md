# eachWeekOfInterval

Returns an array of ZonedDateTime objects for each week within the interval. Each element represents the first moment of the week (Monday at midnight). Uses ISO 8601 week definition where weeks start on Monday. The interval is inclusive of both start and end weeks.

## Signature

```ts
function eachWeekOfInterval(interval: {
  start: Temporal.Instant | Temporal.ZonedDateTime;
  end: Temporal.Instant | Temporal.ZonedDateTime;
}): Temporal.ZonedDateTime[]
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `interval` | `{ start, end }` | The interval with start and end datetimes |

## Returns

Array of `Temporal.ZonedDateTime` at the start of each week (Monday) in the interval.

For `Instant` inputs, UTC is used as the timezone. For `ZonedDateTime` inputs, the timezone of the start date is preserved.

## Examples

### Basic usage

```ts
import { eachWeekOfInterval } from '@gobrand/tiempo';

const start = Temporal.ZonedDateTime.from('2025-01-06T10:00:00Z[UTC]'); // Monday
const end = Temporal.ZonedDateTime.from('2025-01-22T14:00:00Z[UTC]');   // Wednesday

const weeks = eachWeekOfInterval({ start, end });
// [
//   2025-01-06T00:00:00Z[UTC],  // Week 2
//   2025-01-13T00:00:00Z[UTC],  // Week 3
//   2025-01-20T00:00:00Z[UTC]   // Week 4
// ]
```

### Mid-week start

```ts
const start = Temporal.ZonedDateTime.from('2025-01-08T10:00:00Z[UTC]'); // Wednesday
const end = Temporal.ZonedDateTime.from('2025-01-15T14:00:00Z[UTC]');   // Wednesday

const weeks = eachWeekOfInterval({ start, end });
// [
//   2025-01-06T00:00:00Z[UTC],  // Monday of week containing Jan 8
//   2025-01-13T00:00:00Z[UTC]   // Monday of week containing Jan 15
// ]
```

### Cross-year boundary

```ts
const start = Temporal.ZonedDateTime.from('2024-12-25T00:00:00Z[UTC]');
const end = Temporal.ZonedDateTime.from('2025-01-08T00:00:00Z[UTC]');

const weeks = eachWeekOfInterval({ start, end });
// [
//   2024-12-23T00:00:00Z[UTC],  // Monday of week containing Dec 25
//   2024-12-30T00:00:00Z[UTC],  // Monday of week containing Dec 30
//   2025-01-06T00:00:00Z[UTC]   // Monday of week containing Jan 8
// ]
```

## Common Patterns

### Generate weekly schedule

```ts
import { eachWeekOfInterval, addWeeks } from '@gobrand/tiempo';

function getWeeklySchedule(
  scheduleStart: Temporal.ZonedDateTime,
  scheduleEnd: Temporal.ZonedDateTime
) {
  return eachWeekOfInterval({ start: scheduleStart, end: scheduleEnd }).map((weekStart, index) => ({
    weekNumber: index + 1,
    start: weekStart,
    end: addWeeks(weekStart, 1).subtract({ nanoseconds: 1 })
  }));
}
```

### Build week picker

```ts
import { eachWeekOfInterval, format } from '@gobrand/tiempo';

function getWeekOptions(
  rangeStart: Temporal.ZonedDateTime,
  rangeEnd: Temporal.ZonedDateTime
) {
  return eachWeekOfInterval({ start: rangeStart, end: rangeEnd }).map(weekStart => ({
    value: weekStart.toString(),
    label: `Week of ${format(weekStart, 'MMM d, yyyy')}`
  }));
}
```
