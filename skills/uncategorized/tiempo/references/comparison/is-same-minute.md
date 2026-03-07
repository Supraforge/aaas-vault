# isSameMinute

Returns true if both datetimes are in the same minute.

## Signature

```ts
function isSameMinute(
  date1: Temporal.Instant | Temporal.ZonedDateTime,
  date2: Temporal.Instant | Temporal.ZonedDateTime
): boolean
```

## Example

```ts
import { isSameMinute } from '@gobrand/tiempo';

const time1 = Temporal.ZonedDateTime.from('2025-01-20T15:30:45.123Z[UTC]');
const time2 = Temporal.ZonedDateTime.from('2025-01-20T15:30:59.999Z[UTC]');
const time3 = Temporal.ZonedDateTime.from('2025-01-20T15:31:00.000Z[UTC]');

isSameMinute(time1, time2); // true (both at 15:30:xx)
isSameMinute(time1, time3); // false (different minute)
```
