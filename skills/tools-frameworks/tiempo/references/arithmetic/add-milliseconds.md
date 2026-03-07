# addMilliseconds

Adds the specified number of milliseconds to a datetime.

## Signature

```ts
function addMilliseconds(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  milliseconds: number
): Temporal.ZonedDateTime
```

## Example

```ts
import { addMilliseconds } from '@gobrand/tiempo';

const instant = Temporal.Instant.from('2025-01-20T12:00:00Z');

addMilliseconds(instant, 500);
// 2025-01-20T12:00:00.500Z[UTC]

addMilliseconds(instant, 1500);
// 2025-01-20T12:00:01.500Z[UTC]
```
