# isSameNanosecond

Returns true if both datetimes are in the same nanosecond. This is the highest precision comparison available.

## Signature

```ts
function isSameNanosecond(
  date1: Temporal.Instant | Temporal.ZonedDateTime,
  date2: Temporal.Instant | Temporal.ZonedDateTime
): boolean
```

## Example

```ts
import { isSameNanosecond } from '@gobrand/tiempo';

const time1 = Temporal.ZonedDateTime.from('2025-01-20T15:30:45.123456789Z[UTC]');
const time2 = Temporal.ZonedDateTime.from('2025-01-20T15:30:45.123456789Z[UTC]');
const time3 = Temporal.ZonedDateTime.from('2025-01-20T15:30:45.123456790Z[UTC]');

isSameNanosecond(time1, time2); // true (exact match)
isSameNanosecond(time1, time3); // false (different nanosecond)
```
