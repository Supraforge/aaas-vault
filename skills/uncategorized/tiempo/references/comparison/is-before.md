# isBefore

Returns true if the first datetime is before the second datetime.

## Signature

```ts
function isBefore(
  date1: Temporal.Instant | Temporal.ZonedDateTime,
  date2: Temporal.Instant | Temporal.ZonedDateTime
): boolean
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `date1` | `Temporal.Instant \| Temporal.ZonedDateTime` | The first datetime |
| `date2` | `Temporal.Instant \| Temporal.ZonedDateTime` | The second datetime |

## Returns

`true` if `date1` is before `date2`, `false` otherwise.

## Examples

### Basic usage

```ts
import { isBefore } from '@gobrand/tiempo';

const earlier = Temporal.ZonedDateTime.from('2025-01-20T10:00:00-05:00[America/New_York]');
const later = Temporal.ZonedDateTime.from('2025-01-20T16:00:00-05:00[America/New_York]');

isBefore(earlier, later);  // true
isBefore(later, earlier);  // false
isBefore(earlier, earlier); // false
```

### With Instant

```ts
const instant1 = Temporal.Instant.from('2025-01-20T15:00:00Z');
const instant2 = Temporal.Instant.from('2025-01-20T16:00:00Z');
isBefore(instant1, instant2); // true
```

### Different timezones - compares by instant

```ts
const ny = Temporal.ZonedDateTime.from('2025-01-20T10:00:00-05:00[America/New_York]');
const tokyo = Temporal.ZonedDateTime.from('2025-01-21T00:00:00+09:00[Asia/Tokyo]');
isBefore(ny, tokyo); // true (NY 10:00 AM = 15:00 UTC, Tokyo midnight = 15:00 UTC previous day)
```

## Common Patterns

### Validate event dates

```ts
import { isBefore } from '@gobrand/tiempo';

function validateEventDates(start: Temporal.ZonedDateTime, end: Temporal.ZonedDateTime) {
  if (!isBefore(start, end)) {
    throw new Error('Event end date must be after start date');
  }
}
```
