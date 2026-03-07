# isSameMillisecond

Returns true if both datetimes are in the same millisecond.

## Signature

```ts
function isSameMillisecond(
  date1: Temporal.Instant | Temporal.ZonedDateTime,
  date2: Temporal.Instant | Temporal.ZonedDateTime
): boolean
```

## Example

```ts
import { isSameMillisecond } from '@gobrand/tiempo';

const time1 = Temporal.ZonedDateTime.from('2025-01-20T15:30:45.123456Z[UTC]');
const time2 = Temporal.ZonedDateTime.from('2025-01-20T15:30:45.123999Z[UTC]');
const time3 = Temporal.ZonedDateTime.from('2025-01-20T15:30:45.124000Z[UTC]');

isSameMillisecond(time1, time2); // true (both at .123xxx)
isSameMillisecond(time1, time3); // false (different millisecond)
```
