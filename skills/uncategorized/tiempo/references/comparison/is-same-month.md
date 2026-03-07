# isSameMonth

Returns true if both datetimes are in the same calendar month.

## Signature

```ts
function isSameMonth(
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

`true` if both datetimes are in the same calendar month, `false` otherwise.

## Examples

```ts
import { isSameMonth } from '@gobrand/tiempo';

const jan1 = Temporal.ZonedDateTime.from('2025-01-01T00:00:00Z[UTC]');
const jan31 = Temporal.ZonedDateTime.from('2025-01-31T23:59:59Z[UTC]');
const feb1 = Temporal.ZonedDateTime.from('2025-02-01T00:00:00Z[UTC]');

isSameMonth(jan1, jan31); // true
isSameMonth(jan31, feb1); // false
```
