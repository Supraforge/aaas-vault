# eachDayOfInterval

Returns an array of ZonedDateTime objects for each calendar day within the interval. Each element represents the start of day (midnight) in the timezone of the interval start. The interval is inclusive of both start and end days.

## Signature

```ts
function eachDayOfInterval(interval: {
  start: Temporal.Instant | Temporal.ZonedDateTime;
  end: Temporal.Instant | Temporal.ZonedDateTime;
}): Temporal.ZonedDateTime[]
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `interval` | `{ start, end }` | The interval with start and end datetimes |

## Returns

Array of `Temporal.ZonedDateTime` at the start of each day in the interval.

For `Instant` inputs, UTC is used as the timezone. For `ZonedDateTime` inputs, the timezone of the start date is preserved.

## Examples

### Basic usage

```ts
import { eachDayOfInterval } from '@gobrand/tiempo';

const start = Temporal.ZonedDateTime.from('2025-01-06T10:00:00Z[UTC]');
const end = Temporal.ZonedDateTime.from('2025-01-10T14:00:00Z[UTC]');

const days = eachDayOfInterval({ start, end });
// [
//   2025-01-06T00:00:00Z[UTC],
//   2025-01-07T00:00:00Z[UTC],
//   2025-01-08T00:00:00Z[UTC],
//   2025-01-09T00:00:00Z[UTC],
//   2025-01-10T00:00:00Z[UTC]
// ]
```

### With timezone

```ts
const start = Temporal.ZonedDateTime.from('2025-01-06T10:00:00-05:00[America/New_York]');
const end = Temporal.ZonedDateTime.from('2025-01-08T14:00:00-05:00[America/New_York]');

const days = eachDayOfInterval({ start, end });
// [
//   2025-01-06T00:00:00-05:00[America/New_York],
//   2025-01-07T00:00:00-05:00[America/New_York],
//   2025-01-08T00:00:00-05:00[America/New_York]
// ]
```

### With Instant (uses UTC)

```ts
const start = Temporal.Instant.from('2025-01-06T00:00:00Z');
const end = Temporal.Instant.from('2025-01-08T00:00:00Z');

const days = eachDayOfInterval({ start, end });
// [
//   2025-01-06T00:00:00Z[UTC],
//   2025-01-07T00:00:00Z[UTC],
//   2025-01-08T00:00:00Z[UTC]
// ]
```

### Single day interval

```ts
const date = Temporal.ZonedDateTime.from('2025-01-15T12:00:00Z[UTC]');

eachDayOfInterval({ start: date, end: date });
// [2025-01-15T00:00:00Z[UTC]]
```

## Common Patterns

### Build a calendar grid

```ts
import { eachDayOfInterval, startOfMonth, endOfMonth, startOfWeek, endOfWeek } from '@gobrand/tiempo';

function getCalendarDays(month: Temporal.ZonedDateTime) {
  const monthStart = startOfMonth(month);
  const monthEnd = endOfMonth(month);

  // Extend to full weeks for calendar grid
  const calendarStart = startOfWeek(monthStart);
  const calendarEnd = endOfWeek(monthEnd);

  return eachDayOfInterval({ start: calendarStart, end: calendarEnd });
}
```

### Generate date range for availability

```ts
import { eachDayOfInterval, isSameDay } from '@gobrand/tiempo';

function getAvailableDays(
  rangeStart: Temporal.ZonedDateTime,
  rangeEnd: Temporal.ZonedDateTime,
  bookedDates: Temporal.ZonedDateTime[]
) {
  return eachDayOfInterval({ start: rangeStart, end: rangeEnd })
    .filter(day => !bookedDates.some(booked => isSameDay(day, booked)));
}
```
