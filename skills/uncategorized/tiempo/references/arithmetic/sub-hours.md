# subHours

Subtracts the specified number of hours from a datetime.

## Signature

```ts
function subHours(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  hours: number
): Temporal.ZonedDateTime
```

## Example

```ts
import { subHours } from '@gobrand/tiempo';

const now = Temporal.Now.zonedDateTimeISO();

// Get 1 hour ago
const oneHourAgo = subHours(now, 1);

// Get 24 hours ago
const dayAgo = subHours(now, 24);
```
