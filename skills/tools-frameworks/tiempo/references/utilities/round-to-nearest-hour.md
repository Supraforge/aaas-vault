# roundToNearestHour

Round a datetime to the nearest hour boundary with configurable rounding modes and multi-hour intervals.

## Signature

```ts
import { Temporal } from '@js-temporal/polyfill';

function roundToNearestHour(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  options?: RoundToNearestHourOptions
): Temporal.ZonedDateTime

interface RoundToNearestHourOptions {
  mode?: 'round' | 'ceil' | 'floor';
  nearestTo?: 1 | 2 | 3 | 4 | 6 | 8 | 12;
}
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `Temporal.Instant \| Temporal.ZonedDateTime` | The datetime to round |
| `options.mode` | `'round' \| 'ceil' \| 'floor'` | Rounding mode. Default: `'round'` |
| `options.nearestTo` | `1 \| 2 \| 3 \| 4 \| 6 \| 8 \| 12` | Round to N-hour intervals. Default: `1` |

## Returns

A `Temporal.ZonedDateTime` rounded to the hour boundary.

## Rounding Modes

```
Given time 14:20:

14:00 ─────────────●───────────────── 15:00
                 14:20

'round' → 14:00  (nearest hour - 20 min < 30)
'ceil'  → 15:00  (next hour - always up)
'floor' → 14:00  (current hour - always down)
```

## Examples

### Basic rounding (nearest hour)

```ts
import { roundToNearestHour } from '@gobrand/tiempo';
import { Temporal } from '@js-temporal/polyfill';

const time = Temporal.ZonedDateTime.from('2025-01-20T14:20:00[America/New_York]');

roundToNearestHour(time);                     // → 14:00 (20 min < 30)
roundToNearestHour(time, { mode: 'ceil' });   // → 15:00 (always up)
roundToNearestHour(time, { mode: 'floor' });  // → 14:00 (always down)
```

### Past the halfway point

```ts
const time = Temporal.ZonedDateTime.from('2025-01-20T14:37:00[America/New_York]');

roundToNearestHour(time);                     // → 15:00 (37 min >= 30)
roundToNearestHour(time, { mode: 'ceil' });   // → 15:00 (always up)
roundToNearestHour(time, { mode: 'floor' });  // → 14:00 (always down)
```

### Multi-hour intervals (shift scheduling)

```ts
// Round to 6-hour blocks: 00:00, 06:00, 12:00, 18:00
const time = Temporal.ZonedDateTime.from('2025-01-20T14:00:00[America/New_York]');

roundToNearestHour(time, { nearestTo: 6 });                   // → 12:00 (nearest)
roundToNearestHour(time, { mode: 'ceil', nearestTo: 6 });     // → 18:00 (next 6h block)
roundToNearestHour(time, { mode: 'floor', nearestTo: 6 });    // → 12:00 (current 6h block)
```

### From Temporal.Instant

```ts
const instant = Temporal.Instant.from('2025-01-20T14:45:00Z');
const result = roundToNearestHour(instant);

// → 15:00 UTC (rounds up, 45 min >= 30)
// Returns ZonedDateTime in UTC
```

## Common Patterns

### Shift scheduling

```ts
import { roundToNearestHour } from '@gobrand/tiempo';

const clockIn = Temporal.ZonedDateTime.from('2025-01-20T08:15:00[America/New_York]');

// Find the 6-hour shift that contains this time
const shiftStart = roundToNearestHour(clockIn, { mode: 'floor', nearestTo: 6 });
// → 06:00 (employee clocked in during the 06:00-12:00 shift)
```

### Approximate time display

```ts
const exactTime = Temporal.ZonedDateTime.from('2025-01-20T14:37:42[America/New_York]');
const approxTime = roundToNearestHour(exactTime);
// → 15:00 ("about 3pm")
```

### Billing in hour blocks

```ts
const sessionEnd = Temporal.ZonedDateTime.from('2025-01-20T10:15:00[America/New_York]');
const billableEnd = roundToNearestHour(sessionEnd, { mode: 'ceil' });
// → 11:00 (bill for the full hour)
```

## Timezone Preservation

The function preserves the input timezone:

```ts
const tokyo = Temporal.ZonedDateTime.from('2025-01-20T14:37:00+09:00[Asia/Tokyo]');
const result = roundToNearestHour(tokyo);

result.timeZoneId // → "Asia/Tokyo"
```
