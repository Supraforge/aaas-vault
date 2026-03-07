# Comparison Functions Overview

Compare two datetimes or check if a datetime is in the past/future.

## Order Comparison

| Function | Description |
|----------|-------------|
| `isBefore(a, b)` | Check if a is before b |
| `isAfter(a, b)` | Check if a is after b |
| `isFuture(input)` | Check if datetime is in the future |
| `isPast(input)` | Check if datetime is in the past |

## Same Period Comparison

| Function | Description |
|----------|-------------|
| `isSameDay(a, b)` | Same calendar day |
| `isSameWeek(a, b)` | Same calendar week |
| `isSameMonth(a, b)` | Same calendar month |
| `isSameYear(a, b)` | Same calendar year |
| `isSameHour(a, b)` | Same hour |
| `isSameMinute(a, b)` | Same minute |
| `isSameSecond(a, b)` | Same second |
| `isSameMillisecond(a, b)` | Same millisecond |
| `isSameMicrosecond(a, b)` | Same microsecond |
| `isSameNanosecond(a, b)` | Same nanosecond |

## PlainDate Comparison

| Function | Description |
|----------|-------------|
| `isPlainDateBefore(a, b)` | PlainDate a is before b |
| `isPlainDateAfter(a, b)` | PlainDate a is after b |
| `isPlainDateEqual(a, b)` | PlainDates are equal |

## Examples

### Basic Order Comparison

```ts
import { isBefore, isAfter, isFuture, isPast } from '@gobrand/tiempo';

const earlier = Temporal.ZonedDateTime.from('2025-01-20T10:00:00-05:00[America/New_York]');
const later = Temporal.ZonedDateTime.from('2025-01-20T16:00:00-05:00[America/New_York]');

isBefore(earlier, later);  // true
isAfter(later, earlier);   // true
isBefore(earlier, earlier); // false (equal is not before)

// Check against current time
isFuture(eventDate);  // true if event is in the future
isPast(eventDate);    // true if event is in the past
```

### Same Period Comparison

```ts
import { isSameDay, isSameMonth } from '@gobrand/tiempo';

const date1 = Temporal.ZonedDateTime.from('2025-01-20T10:00:00[America/New_York]');
const date2 = Temporal.ZonedDateTime.from('2025-01-20T22:00:00[America/New_York]');

isSameDay(date1, date2);   // true (same calendar day)
isSameMonth(date1, date2); // true (same month)
```

### Different Timezones

Comparisons work correctly across timezones (compares the instant in time):

```ts
const ny = Temporal.ZonedDateTime.from('2025-01-20T10:00:00-05:00[America/New_York]');
const tokyo = Temporal.ZonedDateTime.from('2025-01-21T00:00:00+09:00[Asia/Tokyo]');

isBefore(ny, tokyo); // true (compares the actual moment in time)
```

### Validate Event Dates

```ts
import { isBefore } from '@gobrand/tiempo';

function validateEventDates(start: Temporal.ZonedDateTime, end: Temporal.ZonedDateTime) {
  if (!isBefore(start, end)) {
    throw new Error('Event end date must be after start date');
  }
}
```
