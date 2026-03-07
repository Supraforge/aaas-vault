# isSameMicrosecond

Returns true if both datetimes are in the same microsecond.

## Signature

```ts
function isSameMicrosecond(
  date1: Temporal.Instant | Temporal.ZonedDateTime,
  date2: Temporal.Instant | Temporal.ZonedDateTime
): boolean
```

## Example

```ts
import { isSameMicrosecond } from '@gobrand/tiempo';

const time1 = Temporal.ZonedDateTime.from('2025-01-20T15:30:45.123456789Z[UTC]');
const time2 = Temporal.ZonedDateTime.from('2025-01-20T15:30:45.123456999Z[UTC]');
const time3 = Temporal.ZonedDateTime.from('2025-01-20T15:30:45.123457000Z[UTC]');

isSameMicrosecond(time1, time2); // true (both at .123456xxx)
isSameMicrosecond(time1, time3); // false (different microsecond)
```
