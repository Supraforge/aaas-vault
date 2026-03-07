# differenceInMinutes

Returns the number of minutes between two datetimes.

## Signature

```ts
function differenceInMinutes(
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

The number of minutes between the two datetimes.

## Examples

```ts
import { differenceInMinutes } from '@gobrand/tiempo';

const later = Temporal.Instant.from('2025-01-20T10:45:00Z');
const earlier = Temporal.Instant.from('2025-01-20T10:00:00Z');

differenceInMinutes(later, earlier); // 45
```
