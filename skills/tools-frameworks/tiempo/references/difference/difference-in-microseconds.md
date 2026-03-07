# differenceInMicroseconds

Returns the number of microseconds between two datetimes. Useful for high-precision timing operations.

## Signature

```ts
function differenceInMicroseconds(
  laterDate: Temporal.Instant | Temporal.ZonedDateTime,
  earlierDate: Temporal.Instant | Temporal.ZonedDateTime
): number
```

## Example

```ts
import { differenceInMicroseconds } from '@gobrand/tiempo';

const later = Temporal.Instant.from('2025-01-20T10:00:00.001500Z');
const earlier = Temporal.Instant.from('2025-01-20T10:00:00Z');

differenceInMicroseconds(later, earlier); // 1500
```
