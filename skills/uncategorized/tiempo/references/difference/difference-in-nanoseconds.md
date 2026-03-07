# differenceInNanoseconds

Returns the number of nanoseconds between two datetimes. Returns a `bigint` for precision.

## Signature

```ts
function differenceInNanoseconds(
  laterDate: Temporal.Instant | Temporal.ZonedDateTime,
  earlierDate: Temporal.Instant | Temporal.ZonedDateTime
): bigint
```

## Example

```ts
import { differenceInNanoseconds } from '@gobrand/tiempo';

const later = Temporal.Instant.from('2025-01-20T10:00:00.000001500Z');
const earlier = Temporal.Instant.from('2025-01-20T10:00:00Z');

differenceInNanoseconds(later, earlier); // 1500n (bigint)
```
