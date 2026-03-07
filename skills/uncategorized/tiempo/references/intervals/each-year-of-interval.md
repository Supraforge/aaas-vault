# eachYearOfInterval

Returns an array of ZonedDateTime objects for each year within the interval. Each element represents the first moment of the year (January 1st at midnight). The interval is inclusive of both start and end years.

## Signature

```ts
function eachYearOfInterval(interval: {
  start: Temporal.Instant | Temporal.ZonedDateTime;
  end: Temporal.Instant | Temporal.ZonedDateTime;
}): Temporal.ZonedDateTime[]
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `interval` | `{ start, end }` | The interval with start and end datetimes |

## Returns

Array of `Temporal.ZonedDateTime` at the start of each year in the interval.

For `Instant` inputs, UTC is used as the timezone. For `ZonedDateTime` inputs, the timezone of the start date is preserved.

## Examples

### Basic usage

```ts
import { eachYearOfInterval } from '@gobrand/tiempo';

const start = Temporal.ZonedDateTime.from('2022-06-15T10:00:00Z[UTC]');
const end = Temporal.ZonedDateTime.from('2025-03-20T14:00:00Z[UTC]');

const years = eachYearOfInterval({ start, end });
// [
//   2022-01-01T00:00:00Z[UTC],
//   2023-01-01T00:00:00Z[UTC],
//   2024-01-01T00:00:00Z[UTC],
//   2025-01-01T00:00:00Z[UTC]
// ]
```

### Single year

```ts
const start = Temporal.ZonedDateTime.from('2025-01-15T00:00:00Z[UTC]');
const end = Temporal.ZonedDateTime.from('2025-12-31T23:59:59Z[UTC]');

eachYearOfInterval({ start, end });
// [2025-01-01T00:00:00Z[UTC]]
```

### With timezone

```ts
const start = Temporal.ZonedDateTime.from('2024-01-01T00:00:00-05:00[America/New_York]');
const end = Temporal.ZonedDateTime.from('2026-06-15T00:00:00-04:00[America/New_York]');

const years = eachYearOfInterval({ start, end });
// [
//   2024-01-01T00:00:00-05:00[America/New_York],
//   2025-01-01T00:00:00-05:00[America/New_York],
//   2026-01-01T00:00:00-05:00[America/New_York]
// ]
```

## Common Patterns

### Generate yearly report periods

```ts
import { eachYearOfInterval, addYears } from '@gobrand/tiempo';

function getYearlyReportPeriods(
  startYear: Temporal.ZonedDateTime,
  endYear: Temporal.ZonedDateTime
) {
  return eachYearOfInterval({ start: startYear, end: endYear }).map(yearStart => ({
    start: yearStart,
    end: addYears(yearStart, 1).subtract({ nanoseconds: 1 })
  }));
}
```
