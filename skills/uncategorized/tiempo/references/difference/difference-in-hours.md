# differenceInHours

Returns the number of hours between two datetimes.

## Signature

```ts
function differenceInHours(
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

The number of hours between the two datetimes.

## Examples

```ts
import { differenceInHours } from '@gobrand/tiempo';

const later = Temporal.Instant.from('2025-01-20T15:00:00Z');
const earlier = Temporal.Instant.from('2025-01-20T10:00:00Z');

differenceInHours(later, earlier); // 5
```
