# differenceInMilliseconds

Returns the number of milliseconds between two datetimes.

## Signature

```ts
function differenceInMilliseconds(
  laterDate: Temporal.Instant | Temporal.ZonedDateTime,
  earlierDate: Temporal.Instant | Temporal.ZonedDateTime
): number
```

## Example

```ts
import { differenceInMilliseconds } from '@gobrand/tiempo';

const later = Temporal.Instant.from('2025-01-20T10:00:01.500Z');
const earlier = Temporal.Instant.from('2025-01-20T10:00:00Z');

differenceInMilliseconds(later, earlier); // 1500
```

## Common Patterns

### Performance measurement

```ts
import { differenceInMilliseconds } from '@gobrand/tiempo';

async function measureOperation<T>(
  operation: () => Promise<T>
): Promise<{ result: T; durationMs: number }> {
  const start = Temporal.Now.zonedDateTimeISO();
  const result = await operation();
  const end = Temporal.Now.zonedDateTimeISO();

  return {
    result,
    durationMs: differenceInMilliseconds(end, start),
  };
}
```
