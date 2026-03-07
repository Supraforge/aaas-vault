# isSameSecond

Returns true if both datetimes are in the same second.

## Signature

```ts
function isSameSecond(
  date1: Temporal.Instant | Temporal.ZonedDateTime,
  date2: Temporal.Instant | Temporal.ZonedDateTime
): boolean
```

## Example

```ts
import { isSameSecond } from '@gobrand/tiempo';

const time1 = Temporal.ZonedDateTime.from('2025-01-20T15:30:45.123Z[UTC]');
const time2 = Temporal.ZonedDateTime.from('2025-01-20T15:30:45.999Z[UTC]');
const time3 = Temporal.ZonedDateTime.from('2025-01-20T15:30:46.000Z[UTC]');

isSameSecond(time1, time2); // true (both at 15:30:45.xxx)
isSameSecond(time1, time3); // false (different second)
```
