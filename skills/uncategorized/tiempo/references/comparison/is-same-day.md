# isSameDay

Returns true if both datetimes fall on the same calendar day.

**Important**: This compares the local calendar day in each datetime's timezone. Convert to a common timezone before calling if you need to compare from a specific perspective.

## Signature

```ts
function isSameDay(
  date1: Temporal.Instant | Temporal.ZonedDateTime,
  date2: Temporal.Instant | Temporal.ZonedDateTime
): boolean
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `date1` | `Temporal.Instant \| Temporal.ZonedDateTime` | The first datetime |
| `date2` | `Temporal.Instant \| Temporal.ZonedDateTime` | The second datetime |

## Returns

`true` if both datetimes are on the same calendar day, `false` otherwise.

## Examples

### Same timezone, same day

```ts
import { isSameDay } from '@gobrand/tiempo';

const morning = Temporal.ZonedDateTime.from('2025-01-20T08:00:00Z[UTC]');
const evening = Temporal.ZonedDateTime.from('2025-01-20T23:00:00Z[UTC]');
isSameDay(morning, evening); // true
```

### Same timezone, different days

```ts
const today = Temporal.ZonedDateTime.from('2025-01-20T23:59:59Z[UTC]');
const tomorrow = Temporal.ZonedDateTime.from('2025-01-21T00:00:00Z[UTC]');
isSameDay(today, tomorrow); // false
```

### Different timezones - compares their local calendar days

```ts
const ny = Temporal.ZonedDateTime.from('2025-01-20T23:00:00-05:00[America/New_York]');
const tokyo = Temporal.ZonedDateTime.from('2025-01-21T13:00:00+09:00[Asia/Tokyo]');
// Same instant, different calendar days
isSameDay(ny, tokyo); // false (Jan 20 in NY, Jan 21 in Tokyo)
```

### Convert to same timezone to compare from one perspective

```ts
isSameDay(ny.withTimeZone('UTC'), tokyo.withTimeZone('UTC')); // true (both Jan 21 in UTC)
```

## Common Patterns

### Group items by day

```ts
import { isSameDay } from '@gobrand/tiempo';

function groupByDay<T extends { date: Temporal.ZonedDateTime }>(items: T[]): T[][] {
  const groups: T[][] = [];

  for (const item of items) {
    const existingGroup = groups.find(group =>
      group[0] && isSameDay(group[0].date, item.date)
    );

    if (existingGroup) {
      existingGroup.push(item);
    } else {
      groups.push([item]);
    }
  }

  return groups;
}
```
