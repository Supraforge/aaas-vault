# subSeconds

Subtracts the specified number of seconds from a datetime.

## Signature

```ts
function subSeconds(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  seconds: number
): Temporal.ZonedDateTime
```

## Example

```ts
import { subSeconds } from '@gobrand/tiempo';

const now = Temporal.Now.zonedDateTimeISO();

// Get 30 seconds ago
const thirtySecondsAgo = subSeconds(now, 30);

// Get 1 minute ago
const minuteAgo = subSeconds(now, 60);
```
