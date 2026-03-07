# Difference Functions Overview

Calculate the difference between two datetimes in various units.

## Functions

| Function | Returns |
|----------|---------|
| `differenceInYears(later, earlier)` | Years between dates |
| `differenceInMonths(later, earlier)` | Months between dates |
| `differenceInWeeks(later, earlier)` | Weeks between dates |
| `differenceInDays(later, earlier)` | Days between dates (DST-aware) |
| `differenceInHours(later, earlier)` | Hours between dates |
| `differenceInMinutes(later, earlier)` | Minutes between dates |
| `differenceInSeconds(later, earlier)` | Seconds between dates |
| `differenceInMilliseconds(later, earlier)` | Milliseconds between dates |
| `differenceInMicroseconds(later, earlier)` | Microseconds between dates |
| `differenceInNanoseconds(later, earlier)` | Nanoseconds between dates |

## Common Signature

```ts
function differenceInX(
  laterDate: Temporal.Instant | Temporal.ZonedDateTime,
  earlierDate: Temporal.Instant | Temporal.ZonedDateTime
): number
```

## Examples

### Basic Usage

```ts
import { differenceInDays, differenceInHours } from '@gobrand/tiempo';

const later = Temporal.Instant.from('2025-01-25T12:00:00Z');
const earlier = Temporal.Instant.from('2025-01-20T12:00:00Z');

differenceInDays(later, earlier);   // 5
differenceInHours(later, earlier);  // 120
```

### With ZonedDateTime

```ts
const laterZoned = Temporal.ZonedDateTime.from('2025-01-25T15:00:00-05:00[America/New_York]');
const earlierZoned = Temporal.ZonedDateTime.from('2025-01-20T15:00:00-05:00[America/New_York]');

differenceInDays(laterZoned, earlierZoned); // 5
```

### DST Handling

Calendar-aware calculation handles DST transitions correctly:

```ts
const afterDst = Temporal.ZonedDateTime.from('2025-03-10T12:00:00-04:00[America/New_York]');
const beforeDst = Temporal.ZonedDateTime.from('2025-03-08T12:00:00-05:00[America/New_York]');

differenceInDays(afterDst, beforeDst); // 2 (calendar days, not 48 hours)
```

### Time Until Event

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

### Order Matters

The first argument should be the later date:

```ts
differenceInDays(later, earlier);  // 5 (positive)
differenceInDays(earlier, later);  // -5 (negative)
```
