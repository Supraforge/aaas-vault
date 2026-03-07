# addNanoseconds

Adds the specified number of nanoseconds to a datetime.

## Signature

```ts
function addNanoseconds(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  nanoseconds: number
): Temporal.ZonedDateTime
```

## Example

```ts
import { addNanoseconds } from '@gobrand/tiempo';

const instant = Temporal.Instant.from('2025-01-20T12:00:00Z');

addNanoseconds(instant, 1500);
// 2025-01-20T12:00:00.000001500Z[UTC]

addNanoseconds(instant, 1000000000);
// 2025-01-20T12:00:01Z[UTC] (1 billion nanoseconds = 1 second)
```
