# roundToNearestSecond

Round a datetime to the nearest second boundary with configurable rounding modes and multi-second intervals.

## Signature

```ts
import { Temporal } from '@js-temporal/polyfill';

function roundToNearestSecond(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  options?: RoundToNearestSecondOptions
): Temporal.ZonedDateTime

interface RoundToNearestSecondOptions {
  mode?: 'round' | 'ceil' | 'floor';
  nearestTo?: 1 | 2 | 3 | 4 | 5 | 6 | 10 | 12 | 15 | 20 | 30;
}
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `Temporal.Instant \| Temporal.ZonedDateTime` | The datetime to round |
| `options.mode` | `'round' \| 'ceil' \| 'floor'` | Rounding mode. Default: `'round'` |
| `options.nearestTo` | `1 \| 2 \| 3 \| 4 \| 5 \| 6 \| 10 \| 12 \| 15 \| 20 \| 30` | Round to N-second intervals. Default: `1` |

## Returns

A `Temporal.ZonedDateTime` rounded to the second boundary.

## Rounding Modes

```
Given time 14:37:42.567:

:42 ─────────────────●─────────────── :43
                   .567

'round' → :43  (nearest second - 567ms >= 500)
'ceil'  → :43  (next second - always up)
'floor' → :42  (current second - always down)
```

## Examples

### Basic rounding (nearest second)

```ts
import { roundToNearestSecond } from '@gobrand/tiempo';
import { Temporal } from '@js-temporal/polyfill';

const time = Temporal.ZonedDateTime.from('2025-01-20T14:37:42.567[America/New_York]');

roundToNearestSecond(time);                     // → 14:37:43 (567ms >= 500)
roundToNearestSecond(time, { mode: 'ceil' });   // → 14:37:43 (always up)
roundToNearestSecond(time, { mode: 'floor' });  // → 14:37:42 (always down)
```

### Remove sub-second precision (logging)

```ts
// Clean up timestamps for logging
const logTime = Temporal.ZonedDateTime.from('2025-01-20T14:37:42.123456789[UTC]');
const cleanTime = roundToNearestSecond(logTime, { mode: 'floor' });
// → 14:37:42.000000000 (no sub-second data)
```

### 10-second intervals (video timestamps)

```ts
const timestamp = Temporal.ZonedDateTime.from('2025-01-20T00:02:37[UTC]');

roundToNearestSecond(timestamp, { nearestTo: 10 });                   // → 00:02:40
roundToNearestSecond(timestamp, { mode: 'ceil', nearestTo: 10 });     // → 00:02:40
roundToNearestSecond(timestamp, { mode: 'floor', nearestTo: 10 });    // → 00:02:30
```

### 30-second intervals

```ts
const time = Temporal.ZonedDateTime.from('2025-01-20T14:37:42[America/New_York]');

roundToNearestSecond(time, { nearestTo: 30 });
// → 14:37:30 (42 is closer to 30 than 60)
```

### From Temporal.Instant

```ts
const instant = Temporal.Instant.from('2025-01-20T14:37:42.567Z');
const result = roundToNearestSecond(instant);

// → 14:37:43 UTC (rounds up, 567ms >= 500)
// Returns ZonedDateTime in UTC
```

## Common Patterns

### Video chapter markers

```ts
import { roundToNearestSecond } from '@gobrand/tiempo';

// Snap chapter markers to 10-second intervals
const userClick = Temporal.ZonedDateTime.from('2025-01-20T00:05:37[UTC]');
const chapterMark = roundToNearestSecond(userClick, { nearestTo: 10 });
// → 00:05:40
```

### Countdown timer

```ts
// Round up to next second for clean countdown display
const currentTime = Temporal.ZonedDateTime.from('2025-01-20T14:37:42.100[America/New_York]');
const nextSecond = roundToNearestSecond(currentTime, { mode: 'ceil' });
// → 14:37:43
```

### Animation keyframes

```ts
// Snap keyframes to 5-second intervals
const keyframe = Temporal.ZonedDateTime.from('2025-01-20T00:00:17[UTC]');
const snappedKeyframe = roundToNearestSecond(keyframe, { nearestTo: 5 });
// → 00:00:15
```

### Data synchronization

```ts
// Round timestamps for data bucketing
const dataPoint = Temporal.ZonedDateTime.from('2025-01-20T14:37:42.789[UTC]');
const bucket = roundToNearestSecond(dataPoint, { mode: 'floor', nearestTo: 15 });
// → 14:37:30 (15-second bucket)
```

## Timezone Preservation

The function preserves the input timezone:

```ts
const tokyo = Temporal.ZonedDateTime.from('2025-01-20T14:37:42.567+09:00[Asia/Tokyo]');
const result = roundToNearestSecond(tokyo);

result.timeZoneId // → "Asia/Tokyo"
```
