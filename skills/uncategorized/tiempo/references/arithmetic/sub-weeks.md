# subWeeks

Subtracts the specified number of weeks from a datetime.

## Signature

```ts
function subWeeks(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  weeks: number
): Temporal.ZonedDateTime
```

## Example

```ts
import { subWeeks } from '@gobrand/tiempo';

const now = Temporal.Now.zonedDateTimeISO();

// Get last week
const lastWeek = subWeeks(now, 1);

// Get 4 weeks ago
const fourWeeksAgo = subWeeks(now, 4);
```
