# differenceInWeeks

Returns the number of weeks between two datetimes.

## Signature

```ts
function differenceInWeeks(
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

The number of weeks between the two datetimes.

## Examples

```ts
import { differenceInWeeks } from '@gobrand/tiempo';

const later = Temporal.Instant.from('2025-02-03T12:00:00Z');
const earlier = Temporal.Instant.from('2025-01-20T12:00:00Z');

differenceInWeeks(later, earlier); // 2
```
