# isSameWeek

Returns true if both datetimes are in the same ISO week (Monday–Sunday).

## Signature

```ts
function isSameWeek(
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

`true` if both datetimes are in the same ISO week, `false` otherwise.

## Examples

```ts
import { isSameWeek } from '@gobrand/tiempo';

const monday = Temporal.ZonedDateTime.from('2025-01-20T00:00:00Z[UTC]');
const sunday = Temporal.ZonedDateTime.from('2025-01-26T23:59:59Z[UTC]');
const nextMonday = Temporal.ZonedDateTime.from('2025-01-27T00:00:00Z[UTC]');

isSameWeek(monday, sunday); // true
isSameWeek(sunday, nextMonday); // false
```
