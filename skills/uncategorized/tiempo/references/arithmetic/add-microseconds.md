# addMicroseconds

Adds the specified number of microseconds to a datetime.

## Signature

```ts
function addMicroseconds(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  microseconds: number
): Temporal.ZonedDateTime
```

## Example

```ts
import { addMicroseconds } from '@gobrand/tiempo';

const instant = Temporal.Instant.from('2025-01-20T12:00:00Z');

addMicroseconds(instant, 1500);
// 2025-01-20T12:00:00.001500Z[UTC]

addMicroseconds(instant, 1000000);
// 2025-01-20T12:00:01Z[UTC] (1 million microseconds = 1 second)
```
