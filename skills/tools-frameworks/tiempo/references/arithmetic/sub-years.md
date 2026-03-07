# subYears

Subtracts the specified number of years from a datetime.

## Signature

```ts
function subYears(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  years: number
): Temporal.ZonedDateTime
```

## Example

```ts
import { subYears } from '@gobrand/tiempo';

const now = Temporal.Now.zonedDateTimeISO();

// Get 5 years ago
const fiveYearsAgo = subYears(now, 5);

// Get 1 year ago
const lastYear = subYears(now, 1);
```
