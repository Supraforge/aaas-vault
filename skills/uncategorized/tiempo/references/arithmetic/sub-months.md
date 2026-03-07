# subMonths

Subtracts the specified number of months from a datetime.

## Signature

```ts
function subMonths(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  months: number
): Temporal.ZonedDateTime
```

## Example

```ts
import { subMonths } from '@gobrand/tiempo';

const now = Temporal.Now.zonedDateTimeISO();

// Get last month
const lastMonth = subMonths(now, 1);

// Get 6 months ago
const sixMonthsAgo = subMonths(now, 6);
```
