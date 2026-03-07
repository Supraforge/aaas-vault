# subMinutes

Subtracts the specified number of minutes from a datetime.

## Signature

```ts
function subMinutes(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  minutes: number
): Temporal.ZonedDateTime
```

## Example

```ts
import { subMinutes } from '@gobrand/tiempo';

const now = Temporal.Now.zonedDateTimeISO();

// Get 30 minutes ago
const thirtyMinutesAgo = subMinutes(now, 30);

// Get 1 hour ago
const hourAgo = subMinutes(now, 60);
```
