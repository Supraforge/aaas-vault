# isSameYear

Returns true if both datetimes are in the same calendar year.

## Signature

```ts
function isSameYear(
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

`true` if both datetimes are in the same calendar year, `false` otherwise.

## Examples

```ts
import { isSameYear } from '@gobrand/tiempo';

const jan2025 = Temporal.ZonedDateTime.from('2025-01-15T00:00:00Z[UTC]');
const dec2025 = Temporal.ZonedDateTime.from('2025-12-31T23:59:59Z[UTC]');
const jan2026 = Temporal.ZonedDateTime.from('2026-01-01T00:00:00Z[UTC]');

isSameYear(jan2025, dec2025); // true
isSameYear(dec2025, jan2026); // false
```
