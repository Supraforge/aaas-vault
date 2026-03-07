# subNanoseconds

Subtracts the specified number of nanoseconds from a datetime.

## Signature

```ts
function subNanoseconds(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  nanoseconds: number
): Temporal.ZonedDateTime
```

## Example

```ts
import { subNanoseconds } from '@gobrand/tiempo';

const instant = Temporal.Instant.from('2025-01-20T12:00:00.000001500Z');

subNanoseconds(instant, 500);
// 2025-01-20T12:00:00.000001Z[UTC]

subNanoseconds(instant, 1500);
// 2025-01-20T12:00:00Z[UTC]
```
