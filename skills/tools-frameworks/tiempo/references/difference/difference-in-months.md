# differenceInMonths

Returns the number of months between two datetimes.

## Signature

```ts
function differenceInMonths(
  laterDate: Temporal.Instant | Temporal.ZonedDateTime,
  earlierDate: Temporal.Instant | Temporal.ZonedDateTime
): number
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `laterDate` | `Temporal.Instant \| Temporal.ZonedDateTime` | The later datetime |
| `earlierDate` | `Temporal.Instant \| Temporal.ZonedDateTime` | The earlier datetime |

## Returns

The number of months between the two datetimes. Positive if `laterDate` is after `earlierDate`, negative if before.

## Examples

```ts
import { differenceInMonths } from '@gobrand/tiempo';

const jan = Temporal.Instant.from('2025-01-15T12:00:00Z');
const jun = Temporal.Instant.from('2025-06-15T12:00:00Z');

differenceInMonths(jun, jan); // 5
differenceInMonths(jan, jun); // -5
```
