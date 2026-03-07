# isAfter

Returns true if the first datetime is after the second datetime.

## Signature

```ts
function isAfter(
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

`true` if `date1` is after `date2`, `false` otherwise.

## Examples

```ts
import { isAfter } from '@gobrand/tiempo';

const earlier = Temporal.ZonedDateTime.from('2025-01-20T10:00:00-05:00[America/New_York]');
const later = Temporal.ZonedDateTime.from('2025-01-20T16:00:00-05:00[America/New_York]');

isAfter(later, earlier);  // true
isAfter(earlier, later);  // false
isAfter(earlier, earlier); // false
```

## Common Patterns

### Check date ranges

```ts
import { isBefore, isAfter } from '@gobrand/tiempo';

function isWithinRange(
  date: Temporal.ZonedDateTime,
  start: Temporal.ZonedDateTime,
  end: Temporal.ZonedDateTime
): boolean {
  return !isBefore(date, start) && !isAfter(date, end);
}
```
