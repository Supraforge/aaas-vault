# differenceInYears

Returns the number of years between two datetimes.

## Signature

```ts
function differenceInYears(
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

The number of years between the two datetimes. Positive if `laterDate` is after `earlierDate`, negative if before.

## Examples

```ts
import { differenceInYears } from '@gobrand/tiempo';

const date2020 = Temporal.Instant.from('2020-06-15T12:00:00Z');
const date2025 = Temporal.Instant.from('2025-06-15T12:00:00Z');

differenceInYears(date2025, date2020); // 5
```

## Common Patterns

### Calculate age

```ts
import { differenceInYears } from '@gobrand/tiempo';

function calculateAge(birthDate: Temporal.PlainDate): number {
  const now = Temporal.Now.zonedDateTimeISO();
  const birth = birthDate.toZonedDateTime({
    timeZone: now.timeZoneId,
    plainTime: Temporal.PlainTime.from('00:00:00'),
  });
  return differenceInYears(now, birth);
}
```
