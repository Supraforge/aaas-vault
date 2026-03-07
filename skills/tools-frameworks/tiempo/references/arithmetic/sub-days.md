# subDays

Subtracts the specified number of days from a datetime.

## Signature

```ts
function subDays(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  days: number
): Temporal.ZonedDateTime
```

## Example

```ts
import { subDays } from '@gobrand/tiempo';

const now = Temporal.Now.zonedDateTimeISO();

// Get yesterday
const yesterday = subDays(now, 1);

// Get a week ago
const weekAgo = subDays(now, 7);
```
