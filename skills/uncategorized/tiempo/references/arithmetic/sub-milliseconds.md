# subMilliseconds

Subtracts the specified number of milliseconds from a datetime.

## Signature

```ts
function subMilliseconds(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  milliseconds: number
): Temporal.ZonedDateTime
```

## Example

```ts
import { subMilliseconds } from '@gobrand/tiempo';

const instant = Temporal.Instant.from('2025-01-20T12:00:01.500Z');

subMilliseconds(instant, 500);
// 2025-01-20T12:00:01Z[UTC]

subMilliseconds(instant, 1500);
// 2025-01-20T12:00:00Z[UTC]
```
