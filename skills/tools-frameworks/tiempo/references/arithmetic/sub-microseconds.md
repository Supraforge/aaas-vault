# subMicroseconds

Subtracts the specified number of microseconds from a datetime.

## Signature

```ts
function subMicroseconds(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  microseconds: number
): Temporal.ZonedDateTime
```

## Example

```ts
import { subMicroseconds } from '@gobrand/tiempo';

const instant = Temporal.Instant.from('2025-01-20T12:00:00.001500Z');

subMicroseconds(instant, 500);
// 2025-01-20T12:00:00.001Z[UTC]

subMicroseconds(instant, 1500);
// 2025-01-20T12:00:00Z[UTC]
```
