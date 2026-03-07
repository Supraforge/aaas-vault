# differenceInSeconds

Returns the number of seconds between two datetimes.

## Signature

```ts
function differenceInSeconds(
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

The number of seconds between the two datetimes.

## Examples

```ts
import { differenceInSeconds } from '@gobrand/tiempo';

const later = Temporal.Instant.from('2025-01-20T10:01:30Z');
const earlier = Temporal.Instant.from('2025-01-20T10:00:00Z');

differenceInSeconds(later, earlier); // 90
```

## Common Patterns

### Format duration

```ts
import {
  differenceInHours,
  differenceInMinutes,
  differenceInSeconds,
} from '@gobrand/tiempo';

function formatDuration(
  start: Temporal.ZonedDateTime,
  end: Temporal.ZonedDateTime
): string {
  const totalSeconds = differenceInSeconds(end, start);
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;

  return `${hours}h ${minutes}m ${seconds}s`;
}
```
