# eachMonthOfInterval

Returns an array of ZonedDateTime objects for each month within the interval. Each element represents the first moment of the month (day 1 at midnight). The interval is inclusive of both start and end months.

## Signature

```ts
function eachMonthOfInterval(interval: {
  start: Temporal.Instant | Temporal.ZonedDateTime;
  end: Temporal.Instant | Temporal.ZonedDateTime;
}): Temporal.ZonedDateTime[]
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `interval` | `{ start, end }` | The interval with start and end datetimes |

## Returns

Array of `Temporal.ZonedDateTime` at the start of each month in the interval.

For `Instant` inputs, UTC is used as the timezone. For `ZonedDateTime` inputs, the timezone of the start date is preserved.

## Examples

### Basic usage

```ts
import { eachMonthOfInterval } from '@gobrand/tiempo';

const start = Temporal.ZonedDateTime.from('2025-01-15T10:00:00Z[UTC]');
const end = Temporal.ZonedDateTime.from('2025-04-20T14:00:00Z[UTC]');

const months = eachMonthOfInterval({ start, end });
// [
//   2025-01-01T00:00:00Z[UTC],
//   2025-02-01T00:00:00Z[UTC],
//   2025-03-01T00:00:00Z[UTC],
//   2025-04-01T00:00:00Z[UTC]
// ]
```

### Cross-year boundary

```ts
const start = Temporal.ZonedDateTime.from('2024-11-15T00:00:00Z[UTC]');
const end = Temporal.ZonedDateTime.from('2025-02-15T00:00:00Z[UTC]');

const months = eachMonthOfInterval({ start, end });
// [
//   2024-11-01T00:00:00Z[UTC],
//   2024-12-01T00:00:00Z[UTC],
//   2025-01-01T00:00:00Z[UTC],
//   2025-02-01T00:00:00Z[UTC]
// ]
```

### With timezone

```ts
const start = Temporal.ZonedDateTime.from('2025-01-15T00:00:00-05:00[America/New_York]');
const end = Temporal.ZonedDateTime.from('2025-03-15T00:00:00-04:00[America/New_York]');

const months = eachMonthOfInterval({ start, end });
// [
//   2025-01-01T00:00:00-05:00[America/New_York],
//   2025-02-01T00:00:00-05:00[America/New_York],
//   2025-03-01T00:00:00-05:00[America/New_York]
// ]
```

## Common Patterns

### Generate monthly billing periods

```ts
import { eachMonthOfInterval, addMonths } from '@gobrand/tiempo';

function getMonthlyBillingPeriods(
  contractStart: Temporal.ZonedDateTime,
  contractEnd: Temporal.ZonedDateTime
) {
  return eachMonthOfInterval({ start: contractStart, end: contractEnd }).map(monthStart => ({
    periodStart: monthStart,
    periodEnd: addMonths(monthStart, 1).subtract({ nanoseconds: 1 })
  }));
}
```

### Build month selector options

```ts
import { eachMonthOfInterval, format } from '@gobrand/tiempo';

function getMonthOptions(year: number, timezone: string) {
  const start = Temporal.ZonedDateTime.from(`${year}-01-01T00:00:00[${timezone}]`);
  const end = Temporal.ZonedDateTime.from(`${year}-12-31T00:00:00[${timezone}]`);

  return eachMonthOfInterval({ start, end }).map(month => ({
    value: month.toPlainYearMonth().toString(),
    label: format(month, 'MMMM yyyy')
  }));
}
```
