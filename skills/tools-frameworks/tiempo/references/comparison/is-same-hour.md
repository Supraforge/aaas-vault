# isSameHour

Returns true if both datetimes are in the same hour.

## Signature

```ts
function isSameHour(
  date1: Temporal.Instant | Temporal.ZonedDateTime,
  date2: Temporal.Instant | Temporal.ZonedDateTime
): boolean
```

## Example

```ts
import { isSameHour } from '@gobrand/tiempo';

const time1 = Temporal.ZonedDateTime.from('2025-01-20T15:30:45.123Z[UTC]');
const time2 = Temporal.ZonedDateTime.from('2025-01-20T15:45:00.000Z[UTC]');
const time3 = Temporal.ZonedDateTime.from('2025-01-20T16:00:00.000Z[UTC]');

isSameHour(time1, time2); // true (both at 15:xx)
isSameHour(time1, time3); // false (different hour)
```
